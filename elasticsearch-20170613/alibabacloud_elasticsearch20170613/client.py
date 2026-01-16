# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_elasticsearch20170613 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def activate_zones_with_options(
        self,
        instance_id: str,
        request: main_models.ActivateZonesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ActivateZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'ActivateZones',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/recover-zones',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActivateZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_zones_with_options_async(
        self,
        instance_id: str,
        request: main_models.ActivateZonesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ActivateZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'ActivateZones',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/recover-zones',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActivateZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def activate_zones(
        self,
        instance_id: str,
        request: main_models.ActivateZonesRequest,
    ) -> main_models.ActivateZonesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.activate_zones_with_options(instance_id, request, headers, runtime)

    async def activate_zones_async(
        self,
        instance_id: str,
        request: main_models.ActivateZonesRequest,
    ) -> main_models.ActivateZonesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.activate_zones_with_options_async(instance_id, request, headers, runtime)

    def add_connectable_cluster_with_options(
        self,
        instance_id: str,
        request: main_models.AddConnectableClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddConnectableClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'AddConnectableCluster',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/connected-clusters',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddConnectableClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_connectable_cluster_with_options_async(
        self,
        instance_id: str,
        request: main_models.AddConnectableClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddConnectableClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'AddConnectableCluster',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/connected-clusters',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddConnectableClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_connectable_cluster(
        self,
        instance_id: str,
        request: main_models.AddConnectableClusterRequest,
    ) -> main_models.AddConnectableClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_connectable_cluster_with_options(instance_id, request, headers, runtime)

    async def add_connectable_cluster_async(
        self,
        instance_id: str,
        request: main_models.AddConnectableClusterRequest,
    ) -> main_models.AddConnectableClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_connectable_cluster_with_options_async(instance_id, request, headers, runtime)

    def add_snapshot_repo_with_options(
        self,
        instance_id: str,
        request: main_models.AddSnapshotRepoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddSnapshotRepoResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'AddSnapshotRepo',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/snapshot-repos',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSnapshotRepoResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_snapshot_repo_with_options_async(
        self,
        instance_id: str,
        request: main_models.AddSnapshotRepoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddSnapshotRepoResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'AddSnapshotRepo',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/snapshot-repos',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSnapshotRepoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_snapshot_repo(
        self,
        instance_id: str,
        request: main_models.AddSnapshotRepoRequest,
    ) -> main_models.AddSnapshotRepoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_snapshot_repo_with_options(instance_id, request, headers, runtime)

    async def add_snapshot_repo_async(
        self,
        instance_id: str,
        request: main_models.AddSnapshotRepoRequest,
    ) -> main_models.AddSnapshotRepoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_snapshot_repo_with_options_async(instance_id, request, headers, runtime)

    def cancel_deletion_with_options(
        self,
        instance_id: str,
        request: main_models.CancelDeletionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelDeletionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelDeletion',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/cancel-deletion',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelDeletionResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_deletion_with_options_async(
        self,
        instance_id: str,
        request: main_models.CancelDeletionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelDeletionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelDeletion',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/cancel-deletion',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelDeletionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_deletion(
        self,
        instance_id: str,
        request: main_models.CancelDeletionRequest,
    ) -> main_models.CancelDeletionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.cancel_deletion_with_options(instance_id, request, headers, runtime)

    async def cancel_deletion_async(
        self,
        instance_id: str,
        request: main_models.CancelDeletionRequest,
    ) -> main_models.CancelDeletionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.cancel_deletion_with_options_async(instance_id, request, headers, runtime)

    def cancel_logstash_deletion_with_options(
        self,
        instance_id: str,
        request: main_models.CancelLogstashDeletionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelLogstashDeletionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelLogstashDeletion',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/actions/cancel-deletion',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelLogstashDeletionResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_logstash_deletion_with_options_async(
        self,
        instance_id: str,
        request: main_models.CancelLogstashDeletionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelLogstashDeletionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelLogstashDeletion',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/actions/cancel-deletion',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelLogstashDeletionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_logstash_deletion(
        self,
        instance_id: str,
        request: main_models.CancelLogstashDeletionRequest,
    ) -> main_models.CancelLogstashDeletionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.cancel_logstash_deletion_with_options(instance_id, request, headers, runtime)

    async def cancel_logstash_deletion_async(
        self,
        instance_id: str,
        request: main_models.CancelLogstashDeletionRequest,
    ) -> main_models.CancelLogstashDeletionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.cancel_logstash_deletion_with_options_async(instance_id, request, headers, runtime)

    def cancel_task_with_options(
        self,
        instance_id: str,
        request: main_models.CancelTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.task_type):
            query['taskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelTask',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/cancel-task',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_task_with_options_async(
        self,
        instance_id: str,
        request: main_models.CancelTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.task_type):
            query['taskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelTask',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/cancel-task',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_task(
        self,
        instance_id: str,
        request: main_models.CancelTaskRequest,
    ) -> main_models.CancelTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.cancel_task_with_options(instance_id, request, headers, runtime)

    async def cancel_task_async(
        self,
        instance_id: str,
        request: main_models.CancelTaskRequest,
    ) -> main_models.CancelTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.cancel_task_with_options_async(instance_id, request, headers, runtime)

    def capacity_plan_with_options(
        self,
        request: main_models.CapacityPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CapacityPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.complex_query_available):
            body['complexQueryAvailable'] = request.complex_query_available
        if not DaraCore.is_null(request.data_info):
            body['dataInfo'] = request.data_info
        if not DaraCore.is_null(request.metric):
            body['metric'] = request.metric
        if not DaraCore.is_null(request.usage_scenario):
            body['usageScenario'] = request.usage_scenario
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CapacityPlan',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/assist/actions/capacity-plan',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CapacityPlanResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def capacity_plan_with_options_async(
        self,
        request: main_models.CapacityPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CapacityPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.complex_query_available):
            body['complexQueryAvailable'] = request.complex_query_available
        if not DaraCore.is_null(request.data_info):
            body['dataInfo'] = request.data_info
        if not DaraCore.is_null(request.metric):
            body['metric'] = request.metric
        if not DaraCore.is_null(request.usage_scenario):
            body['usageScenario'] = request.usage_scenario
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CapacityPlan',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/assist/actions/capacity-plan',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CapacityPlanResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def capacity_plan(
        self,
        request: main_models.CapacityPlanRequest,
    ) -> main_models.CapacityPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.capacity_plan_with_options(request, headers, runtime)

    async def capacity_plan_async(
        self,
        request: main_models.CapacityPlanRequest,
    ) -> main_models.CapacityPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.capacity_plan_with_options_async(request, headers, runtime)

    def close_diagnosis_with_options(
        self,
        instance_id: str,
        request: main_models.CloseDiagnosisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloseDiagnosisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloseDiagnosis',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/diagnosis/instances/{DaraURL.percent_encode(instance_id)}/actions/close-diagnosis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_diagnosis_with_options_async(
        self,
        instance_id: str,
        request: main_models.CloseDiagnosisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloseDiagnosisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloseDiagnosis',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/diagnosis/instances/{DaraURL.percent_encode(instance_id)}/actions/close-diagnosis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_diagnosis(
        self,
        instance_id: str,
        request: main_models.CloseDiagnosisRequest,
    ) -> main_models.CloseDiagnosisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.close_diagnosis_with_options(instance_id, request, headers, runtime)

    async def close_diagnosis_async(
        self,
        instance_id: str,
        request: main_models.CloseDiagnosisRequest,
    ) -> main_models.CloseDiagnosisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.close_diagnosis_with_options_async(instance_id, request, headers, runtime)

    def close_https_with_options(
        self,
        instance_id: str,
        request: main_models.CloseHttpsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloseHttpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloseHttps',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/close-https',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseHttpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_https_with_options_async(
        self,
        instance_id: str,
        request: main_models.CloseHttpsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloseHttpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloseHttps',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/close-https',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseHttpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_https(
        self,
        instance_id: str,
        request: main_models.CloseHttpsRequest,
    ) -> main_models.CloseHttpsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.close_https_with_options(instance_id, request, headers, runtime)

    async def close_https_async(
        self,
        instance_id: str,
        request: main_models.CloseHttpsRequest,
    ) -> main_models.CloseHttpsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.close_https_with_options_async(instance_id, request, headers, runtime)

    def close_managed_index_with_options(
        self,
        instance_id: str,
        index: str,
        request: main_models.CloseManagedIndexRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloseManagedIndexResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloseManagedIndex',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/indices/{DaraURL.percent_encode(index)}/close-managed',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseManagedIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_managed_index_with_options_async(
        self,
        instance_id: str,
        index: str,
        request: main_models.CloseManagedIndexRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloseManagedIndexResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloseManagedIndex',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/indices/{DaraURL.percent_encode(index)}/close-managed',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseManagedIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_managed_index(
        self,
        instance_id: str,
        index: str,
        request: main_models.CloseManagedIndexRequest,
    ) -> main_models.CloseManagedIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.close_managed_index_with_options(instance_id, index, request, headers, runtime)

    async def close_managed_index_async(
        self,
        instance_id: str,
        index: str,
        request: main_models.CloseManagedIndexRequest,
    ) -> main_models.CloseManagedIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.close_managed_index_with_options_async(instance_id, index, request, headers, runtime)

    def create_collector_with_options(
        self,
        request: main_models.CreateCollectorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCollectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.collector_paths):
            body['collectorPaths'] = request.collector_paths
        if not DaraCore.is_null(request.configs):
            body['configs'] = request.configs
        if not DaraCore.is_null(request.dry_run):
            body['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.extend_configs):
            body['extendConfigs'] = request.extend_configs
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.res_type):
            body['resType'] = request.res_type
        if not DaraCore.is_null(request.res_version):
            body['resVersion'] = request.res_version
        if not DaraCore.is_null(request.vpc_id):
            body['vpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCollector',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/collectors',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCollectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_collector_with_options_async(
        self,
        request: main_models.CreateCollectorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCollectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.collector_paths):
            body['collectorPaths'] = request.collector_paths
        if not DaraCore.is_null(request.configs):
            body['configs'] = request.configs
        if not DaraCore.is_null(request.dry_run):
            body['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.extend_configs):
            body['extendConfigs'] = request.extend_configs
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.res_type):
            body['resType'] = request.res_type
        if not DaraCore.is_null(request.res_version):
            body['resVersion'] = request.res_version
        if not DaraCore.is_null(request.vpc_id):
            body['vpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCollector',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/collectors',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCollectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_collector(
        self,
        request: main_models.CreateCollectorRequest,
    ) -> main_models.CreateCollectorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_collector_with_options(request, headers, runtime)

    async def create_collector_async(
        self,
        request: main_models.CreateCollectorRequest,
    ) -> main_models.CreateCollectorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_collector_with_options_async(request, headers, runtime)

    def create_component_index_with_options(
        self,
        instance_id: str,
        name: str,
        request: main_models.CreateComponentIndexRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateComponentIndexResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.meta):
            body['_meta'] = request.meta
        if not DaraCore.is_null(request.template):
            body['template'] = request.template
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateComponentIndex',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/component-index/{DaraURL.percent_encode(name)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateComponentIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_component_index_with_options_async(
        self,
        instance_id: str,
        name: str,
        request: main_models.CreateComponentIndexRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateComponentIndexResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.meta):
            body['_meta'] = request.meta
        if not DaraCore.is_null(request.template):
            body['template'] = request.template
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateComponentIndex',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/component-index/{DaraURL.percent_encode(name)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateComponentIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_component_index(
        self,
        instance_id: str,
        name: str,
        request: main_models.CreateComponentIndexRequest,
    ) -> main_models.CreateComponentIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_component_index_with_options(instance_id, name, request, headers, runtime)

    async def create_component_index_async(
        self,
        instance_id: str,
        name: str,
        request: main_models.CreateComponentIndexRequest,
    ) -> main_models.CreateComponentIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_component_index_with_options_async(instance_id, name, request, headers, runtime)

    def create_data_stream_with_options(
        self,
        instance_id: str,
        request: main_models.CreateDataStreamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'CreateDataStream',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/data-streams',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_stream_with_options_async(
        self,
        instance_id: str,
        request: main_models.CreateDataStreamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'CreateDataStream',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/data-streams',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_stream(
        self,
        instance_id: str,
        request: main_models.CreateDataStreamRequest,
    ) -> main_models.CreateDataStreamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_data_stream_with_options(instance_id, request, headers, runtime)

    async def create_data_stream_async(
        self,
        instance_id: str,
        request: main_models.CreateDataStreamRequest,
    ) -> main_models.CreateDataStreamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_data_stream_with_options_async(instance_id, request, headers, runtime)

    def create_ilmpolicy_with_options(
        self,
        instance_id: str,
        request: main_models.CreateILMPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateILMPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'CreateILMPolicy',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/ilm-policies',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateILMPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ilmpolicy_with_options_async(
        self,
        instance_id: str,
        request: main_models.CreateILMPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateILMPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'CreateILMPolicy',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/ilm-policies',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateILMPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ilmpolicy(
        self,
        instance_id: str,
        request: main_models.CreateILMPolicyRequest,
    ) -> main_models.CreateILMPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_ilmpolicy_with_options(instance_id, request, headers, runtime)

    async def create_ilmpolicy_async(
        self,
        instance_id: str,
        request: main_models.CreateILMPolicyRequest,
    ) -> main_models.CreateILMPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_ilmpolicy_with_options_async(instance_id, request, headers, runtime)

    def create_index_template_with_options(
        self,
        instance_id: str,
        request: main_models.CreateIndexTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIndexTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.data_stream):
            body['dataStream'] = request.data_stream
        if not DaraCore.is_null(request.ilm_policy):
            body['ilmPolicy'] = request.ilm_policy
        if not DaraCore.is_null(request.index_patterns):
            body['indexPatterns'] = request.index_patterns
        if not DaraCore.is_null(request.index_template):
            body['indexTemplate'] = request.index_template
        if not DaraCore.is_null(request.priority):
            body['priority'] = request.priority
        if not DaraCore.is_null(request.template):
            body['template'] = request.template
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIndexTemplate',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/index-templates',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIndexTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_index_template_with_options_async(
        self,
        instance_id: str,
        request: main_models.CreateIndexTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIndexTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.data_stream):
            body['dataStream'] = request.data_stream
        if not DaraCore.is_null(request.ilm_policy):
            body['ilmPolicy'] = request.ilm_policy
        if not DaraCore.is_null(request.index_patterns):
            body['indexPatterns'] = request.index_patterns
        if not DaraCore.is_null(request.index_template):
            body['indexTemplate'] = request.index_template
        if not DaraCore.is_null(request.priority):
            body['priority'] = request.priority
        if not DaraCore.is_null(request.template):
            body['template'] = request.template
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIndexTemplate',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/index-templates',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIndexTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_index_template(
        self,
        instance_id: str,
        request: main_models.CreateIndexTemplateRequest,
    ) -> main_models.CreateIndexTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_index_template_with_options(instance_id, request, headers, runtime)

    async def create_index_template_async(
        self,
        instance_id: str,
        request: main_models.CreateIndexTemplateRequest,
    ) -> main_models.CreateIndexTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_index_template_with_options_async(instance_id, request, headers, runtime)

    def create_logstash_with_options(
        self,
        request: main_models.CreateLogstashRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLogstashResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.network_config):
            body['networkConfig'] = request.network_config
        if not DaraCore.is_null(request.node_amount):
            body['nodeAmount'] = request.node_amount
        if not DaraCore.is_null(request.node_spec):
            body['nodeSpec'] = request.node_spec
        if not DaraCore.is_null(request.payment_info):
            body['paymentInfo'] = request.payment_info
        if not DaraCore.is_null(request.payment_type):
            body['paymentType'] = request.payment_type
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLogstash',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLogstashResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_logstash_with_options_async(
        self,
        request: main_models.CreateLogstashRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLogstashResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.network_config):
            body['networkConfig'] = request.network_config
        if not DaraCore.is_null(request.node_amount):
            body['nodeAmount'] = request.node_amount
        if not DaraCore.is_null(request.node_spec):
            body['nodeSpec'] = request.node_spec
        if not DaraCore.is_null(request.payment_info):
            body['paymentInfo'] = request.payment_info
        if not DaraCore.is_null(request.payment_type):
            body['paymentType'] = request.payment_type
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLogstash',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLogstashResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_logstash(
        self,
        request: main_models.CreateLogstashRequest,
    ) -> main_models.CreateLogstashResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_logstash_with_options(request, headers, runtime)

    async def create_logstash_async(
        self,
        request: main_models.CreateLogstashRequest,
    ) -> main_models.CreateLogstashResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_logstash_with_options_async(request, headers, runtime)

    def create_pipelines_with_options(
        self,
        instance_id: str,
        request: main_models.CreatePipelinesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePipelinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.trigger):
            query['trigger'] = request.trigger
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePipelines',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/pipelines',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pipelines_with_options_async(
        self,
        instance_id: str,
        request: main_models.CreatePipelinesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePipelinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.trigger):
            query['trigger'] = request.trigger
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePipelines',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/pipelines',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePipelinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pipelines(
        self,
        instance_id: str,
        request: main_models.CreatePipelinesRequest,
    ) -> main_models.CreatePipelinesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_pipelines_with_options(instance_id, request, headers, runtime)

    async def create_pipelines_async(
        self,
        instance_id: str,
        request: main_models.CreatePipelinesRequest,
    ) -> main_models.CreatePipelinesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_pipelines_with_options_async(instance_id, request, headers, runtime)

    def create_snapshot_with_options(
        self,
        instance_id: str,
        request: main_models.CreateSnapshotRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'CreateSnapshot',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/snapshots',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_snapshot_with_options_async(
        self,
        instance_id: str,
        request: main_models.CreateSnapshotRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'CreateSnapshot',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/snapshots',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_snapshot(
        self,
        instance_id: str,
        request: main_models.CreateSnapshotRequest,
    ) -> main_models.CreateSnapshotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_snapshot_with_options(instance_id, request, headers, runtime)

    async def create_snapshot_async(
        self,
        instance_id: str,
        request: main_models.CreateSnapshotRequest,
    ) -> main_models.CreateSnapshotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_snapshot_with_options_async(instance_id, request, headers, runtime)

    def create_vpc_endpoint_with_options(
        self,
        instance_id: str,
        request: main_models.CreateVpcEndpointRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpcEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.service_id):
            body['serviceId'] = request.service_id
        if not DaraCore.is_null(request.zone_id):
            body['zoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpcEndpoint',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/vpc-endpoints',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVpcEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpc_endpoint_with_options_async(
        self,
        instance_id: str,
        request: main_models.CreateVpcEndpointRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpcEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.service_id):
            body['serviceId'] = request.service_id
        if not DaraCore.is_null(request.zone_id):
            body['zoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpcEndpoint',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/vpc-endpoints',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVpcEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vpc_endpoint(
        self,
        instance_id: str,
        request: main_models.CreateVpcEndpointRequest,
    ) -> main_models.CreateVpcEndpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_vpc_endpoint_with_options(instance_id, request, headers, runtime)

    async def create_vpc_endpoint_async(
        self,
        instance_id: str,
        request: main_models.CreateVpcEndpointRequest,
    ) -> main_models.CreateVpcEndpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_vpc_endpoint_with_options_async(instance_id, request, headers, runtime)

    def deactivate_zones_with_options(
        self,
        instance_id: str,
        request: main_models.DeactivateZonesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeactivateZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'DeactivateZones',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/down-zones',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeactivateZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def deactivate_zones_with_options_async(
        self,
        instance_id: str,
        request: main_models.DeactivateZonesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeactivateZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'DeactivateZones',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/down-zones',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeactivateZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deactivate_zones(
        self,
        instance_id: str,
        request: main_models.DeactivateZonesRequest,
    ) -> main_models.DeactivateZonesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.deactivate_zones_with_options(instance_id, request, headers, runtime)

    async def deactivate_zones_async(
        self,
        instance_id: str,
        request: main_models.DeactivateZonesRequest,
    ) -> main_models.DeactivateZonesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.deactivate_zones_with_options_async(instance_id, request, headers, runtime)

    def delete_collector_with_options(
        self,
        res_id: str,
        request: main_models.DeleteCollectorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCollectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCollector',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/collectors/{DaraURL.percent_encode(res_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCollectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_collector_with_options_async(
        self,
        res_id: str,
        request: main_models.DeleteCollectorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCollectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCollector',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/collectors/{DaraURL.percent_encode(res_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCollectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_collector(
        self,
        res_id: str,
        request: main_models.DeleteCollectorRequest,
    ) -> main_models.DeleteCollectorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_collector_with_options(res_id, request, headers, runtime)

    async def delete_collector_async(
        self,
        res_id: str,
        request: main_models.DeleteCollectorRequest,
    ) -> main_models.DeleteCollectorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_collector_with_options_async(res_id, request, headers, runtime)

    def delete_component_index_with_options(
        self,
        instance_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteComponentIndexResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteComponentIndex',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/component-index/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteComponentIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_component_index_with_options_async(
        self,
        instance_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteComponentIndexResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteComponentIndex',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/component-index/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteComponentIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_component_index(
        self,
        instance_id: str,
        name: str,
    ) -> main_models.DeleteComponentIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_component_index_with_options(instance_id, name, headers, runtime)

    async def delete_component_index_async(
        self,
        instance_id: str,
        name: str,
    ) -> main_models.DeleteComponentIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_component_index_with_options_async(instance_id, name, headers, runtime)

    def delete_connected_cluster_with_options(
        self,
        instance_id: str,
        request: main_models.DeleteConnectedClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConnectedClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.connected_instance_id):
            query['connectedInstanceId'] = request.connected_instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConnectedCluster',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/connected-clusters',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConnectedClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_connected_cluster_with_options_async(
        self,
        instance_id: str,
        request: main_models.DeleteConnectedClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConnectedClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.connected_instance_id):
            query['connectedInstanceId'] = request.connected_instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConnectedCluster',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/connected-clusters',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConnectedClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_connected_cluster(
        self,
        instance_id: str,
        request: main_models.DeleteConnectedClusterRequest,
    ) -> main_models.DeleteConnectedClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_connected_cluster_with_options(instance_id, request, headers, runtime)

    async def delete_connected_cluster_async(
        self,
        instance_id: str,
        request: main_models.DeleteConnectedClusterRequest,
    ) -> main_models.DeleteConnectedClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_connected_cluster_with_options_async(instance_id, request, headers, runtime)

    def delete_data_stream_with_options(
        self,
        instance_id: str,
        data_stream: str,
        request: main_models.DeleteDataStreamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataStream',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/data-streams/{DaraURL.percent_encode(data_stream)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_stream_with_options_async(
        self,
        instance_id: str,
        data_stream: str,
        request: main_models.DeleteDataStreamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataStream',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/data-streams/{DaraURL.percent_encode(data_stream)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_stream(
        self,
        instance_id: str,
        data_stream: str,
        request: main_models.DeleteDataStreamRequest,
    ) -> main_models.DeleteDataStreamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_data_stream_with_options(instance_id, data_stream, request, headers, runtime)

    async def delete_data_stream_async(
        self,
        instance_id: str,
        data_stream: str,
        request: main_models.DeleteDataStreamRequest,
    ) -> main_models.DeleteDataStreamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_data_stream_with_options_async(instance_id, data_stream, request, headers, runtime)

    def delete_data_task_with_options(
        self,
        instance_id: str,
        request: main_models.DeleteDataTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataTask',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/data-task',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_task_with_options_async(
        self,
        instance_id: str,
        request: main_models.DeleteDataTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataTask',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/data-task',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_task(
        self,
        instance_id: str,
        request: main_models.DeleteDataTaskRequest,
    ) -> main_models.DeleteDataTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_data_task_with_options(instance_id, request, headers, runtime)

    async def delete_data_task_async(
        self,
        instance_id: str,
        request: main_models.DeleteDataTaskRequest,
    ) -> main_models.DeleteDataTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_data_task_with_options_async(instance_id, request, headers, runtime)

    def delete_deprecated_template_with_options(
        self,
        instance_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDeprecatedTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDeprecatedTemplate',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/deprecated-templates/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDeprecatedTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_deprecated_template_with_options_async(
        self,
        instance_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDeprecatedTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDeprecatedTemplate',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/deprecated-templates/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDeprecatedTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_deprecated_template(
        self,
        instance_id: str,
        name: str,
    ) -> main_models.DeleteDeprecatedTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_deprecated_template_with_options(instance_id, name, headers, runtime)

    async def delete_deprecated_template_async(
        self,
        instance_id: str,
        name: str,
    ) -> main_models.DeleteDeprecatedTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_deprecated_template_with_options_async(instance_id, name, headers, runtime)

    def delete_ilmpolicy_with_options(
        self,
        instance_id: str,
        policy_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteILMPolicyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteILMPolicy',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/ilm-policies/{DaraURL.percent_encode(policy_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteILMPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ilmpolicy_with_options_async(
        self,
        instance_id: str,
        policy_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteILMPolicyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteILMPolicy',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/ilm-policies/{DaraURL.percent_encode(policy_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteILMPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ilmpolicy(
        self,
        instance_id: str,
        policy_name: str,
    ) -> main_models.DeleteILMPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_ilmpolicy_with_options(instance_id, policy_name, headers, runtime)

    async def delete_ilmpolicy_async(
        self,
        instance_id: str,
        policy_name: str,
    ) -> main_models.DeleteILMPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_ilmpolicy_with_options_async(instance_id, policy_name, headers, runtime)

    def delete_index_template_with_options(
        self,
        instance_id: str,
        index_template: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIndexTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteIndexTemplate',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/index-templates/{DaraURL.percent_encode(index_template)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIndexTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_index_template_with_options_async(
        self,
        instance_id: str,
        index_template: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIndexTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteIndexTemplate',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/index-templates/{DaraURL.percent_encode(index_template)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIndexTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_index_template(
        self,
        instance_id: str,
        index_template: str,
    ) -> main_models.DeleteIndexTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_index_template_with_options(instance_id, index_template, headers, runtime)

    async def delete_index_template_async(
        self,
        instance_id: str,
        index_template: str,
    ) -> main_models.DeleteIndexTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_index_template_with_options_async(instance_id, index_template, headers, runtime)

    def delete_instance_with_options(
        self,
        instance_id: str,
        request: main_models.DeleteInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.delete_type):
            query['deleteType'] = request.delete_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        instance_id: str,
        request: main_models.DeleteInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.delete_type):
            query['deleteType'] = request.delete_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        instance_id: str,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_instance_with_options(instance_id, request, headers, runtime)

    async def delete_instance_async(
        self,
        instance_id: str,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_instance_with_options_async(instance_id, request, headers, runtime)

    def delete_logstash_with_options(
        self,
        instance_id: str,
        request: main_models.DeleteLogstashRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLogstashResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.delete_type):
            query['deleteType'] = request.delete_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLogstash',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLogstashResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_logstash_with_options_async(
        self,
        instance_id: str,
        request: main_models.DeleteLogstashRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLogstashResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.delete_type):
            query['deleteType'] = request.delete_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLogstash',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLogstashResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_logstash(
        self,
        instance_id: str,
        request: main_models.DeleteLogstashRequest,
    ) -> main_models.DeleteLogstashResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_logstash_with_options(instance_id, request, headers, runtime)

    async def delete_logstash_async(
        self,
        instance_id: str,
        request: main_models.DeleteLogstashRequest,
    ) -> main_models.DeleteLogstashResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_logstash_with_options_async(instance_id, request, headers, runtime)

    def delete_pipelines_with_options(
        self,
        instance_id: str,
        request: main_models.DeletePipelinesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePipelinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.pipeline_ids):
            query['pipelineIds'] = request.pipeline_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePipelines',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/pipelines',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pipelines_with_options_async(
        self,
        instance_id: str,
        request: main_models.DeletePipelinesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePipelinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.pipeline_ids):
            query['pipelineIds'] = request.pipeline_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePipelines',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/pipelines',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePipelinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pipelines(
        self,
        instance_id: str,
        request: main_models.DeletePipelinesRequest,
    ) -> main_models.DeletePipelinesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_pipelines_with_options(instance_id, request, headers, runtime)

    async def delete_pipelines_async(
        self,
        instance_id: str,
        request: main_models.DeletePipelinesRequest,
    ) -> main_models.DeletePipelinesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_pipelines_with_options_async(instance_id, request, headers, runtime)

    def delete_snapshot_repo_with_options(
        self,
        instance_id: str,
        request: main_models.DeleteSnapshotRepoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSnapshotRepoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.repo_path):
            query['repoPath'] = request.repo_path
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSnapshotRepo',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/snapshot-repos',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSnapshotRepoResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_snapshot_repo_with_options_async(
        self,
        instance_id: str,
        request: main_models.DeleteSnapshotRepoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSnapshotRepoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.repo_path):
            query['repoPath'] = request.repo_path
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSnapshotRepo',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/snapshot-repos',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSnapshotRepoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_snapshot_repo(
        self,
        instance_id: str,
        request: main_models.DeleteSnapshotRepoRequest,
    ) -> main_models.DeleteSnapshotRepoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_snapshot_repo_with_options(instance_id, request, headers, runtime)

    async def delete_snapshot_repo_async(
        self,
        instance_id: str,
        request: main_models.DeleteSnapshotRepoRequest,
    ) -> main_models.DeleteSnapshotRepoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_snapshot_repo_with_options_async(instance_id, request, headers, runtime)

    def delete_vpc_endpoint_with_options(
        self,
        instance_id: str,
        endpoint_id: str,
        request: main_models.DeleteVpcEndpointRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVpcEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVpcEndpoint',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/vpc-endpoints/{DaraURL.percent_encode(endpoint_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVpcEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vpc_endpoint_with_options_async(
        self,
        instance_id: str,
        endpoint_id: str,
        request: main_models.DeleteVpcEndpointRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVpcEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVpcEndpoint',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/vpc-endpoints/{DaraURL.percent_encode(endpoint_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVpcEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vpc_endpoint(
        self,
        instance_id: str,
        endpoint_id: str,
        request: main_models.DeleteVpcEndpointRequest,
    ) -> main_models.DeleteVpcEndpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_vpc_endpoint_with_options(instance_id, endpoint_id, request, headers, runtime)

    async def delete_vpc_endpoint_async(
        self,
        instance_id: str,
        endpoint_id: str,
        request: main_models.DeleteVpcEndpointRequest,
    ) -> main_models.DeleteVpcEndpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_vpc_endpoint_with_options_async(instance_id, endpoint_id, request, headers, runtime)

    def describe_ack_operator_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAckOperatorResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeAckOperator',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/ack-clusters/{DaraURL.percent_encode(cluster_id)}/operator',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAckOperatorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ack_operator_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAckOperatorResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeAckOperator',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/ack-clusters/{DaraURL.percent_encode(cluster_id)}/operator',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAckOperatorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ack_operator(
        self,
        cluster_id: str,
    ) -> main_models.DescribeAckOperatorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_ack_operator_with_options(cluster_id, headers, runtime)

    async def describe_ack_operator_async(
        self,
        cluster_id: str,
    ) -> main_models.DescribeAckOperatorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_ack_operator_with_options_async(cluster_id, headers, runtime)

    def describe_collector_with_options(
        self,
        res_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCollectorResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeCollector',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/collectors/{DaraURL.percent_encode(res_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCollectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_collector_with_options_async(
        self,
        res_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCollectorResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeCollector',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/collectors/{DaraURL.percent_encode(res_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCollectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_collector(
        self,
        res_id: str,
    ) -> main_models.DescribeCollectorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_collector_with_options(res_id, headers, runtime)

    async def describe_collector_async(
        self,
        res_id: str,
    ) -> main_models.DescribeCollectorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_collector_with_options_async(res_id, headers, runtime)

    def describe_component_index_with_options(
        self,
        instance_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeComponentIndexResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeComponentIndex',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/component-index/{DaraURL.percent_encode(name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeComponentIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_component_index_with_options_async(
        self,
        instance_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeComponentIndexResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeComponentIndex',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/component-index/{DaraURL.percent_encode(name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeComponentIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_component_index(
        self,
        instance_id: str,
        name: str,
    ) -> main_models.DescribeComponentIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_component_index_with_options(instance_id, name, headers, runtime)

    async def describe_component_index_async(
        self,
        instance_id: str,
        name: str,
    ) -> main_models.DescribeComponentIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_component_index_with_options_async(instance_id, name, headers, runtime)

    def describe_connectable_clusters_with_options(
        self,
        instance_id: str,
        request: main_models.DescribeConnectableClustersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConnectableClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.already_set_items):
            query['alreadySetItems'] = request.already_set_items
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConnectableClusters',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/connectable-clusters',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConnectableClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_connectable_clusters_with_options_async(
        self,
        instance_id: str,
        request: main_models.DescribeConnectableClustersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConnectableClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.already_set_items):
            query['alreadySetItems'] = request.already_set_items
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConnectableClusters',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/connectable-clusters',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConnectableClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_connectable_clusters(
        self,
        instance_id: str,
        request: main_models.DescribeConnectableClustersRequest,
    ) -> main_models.DescribeConnectableClustersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_connectable_clusters_with_options(instance_id, request, headers, runtime)

    async def describe_connectable_clusters_async(
        self,
        instance_id: str,
        request: main_models.DescribeConnectableClustersRequest,
    ) -> main_models.DescribeConnectableClustersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_connectable_clusters_with_options_async(instance_id, request, headers, runtime)

    def describe_deprecated_template_with_options(
        self,
        instance_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeprecatedTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeDeprecatedTemplate',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/deprecated-templates/{DaraURL.percent_encode(name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeprecatedTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_deprecated_template_with_options_async(
        self,
        instance_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeprecatedTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeDeprecatedTemplate',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/deprecated-templates/{DaraURL.percent_encode(name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeprecatedTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_deprecated_template(
        self,
        instance_id: str,
        name: str,
    ) -> main_models.DescribeDeprecatedTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_deprecated_template_with_options(instance_id, name, headers, runtime)

    async def describe_deprecated_template_async(
        self,
        instance_id: str,
        name: str,
    ) -> main_models.DescribeDeprecatedTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_deprecated_template_with_options_async(instance_id, name, headers, runtime)

    def describe_diagnose_report_with_options(
        self,
        instance_id: str,
        report_id: str,
        request: main_models.DescribeDiagnoseReportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnoseReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnoseReport',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/diagnosis/instances/{DaraURL.percent_encode(instance_id)}/reports/{DaraURL.percent_encode(report_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnoseReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnose_report_with_options_async(
        self,
        instance_id: str,
        report_id: str,
        request: main_models.DescribeDiagnoseReportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnoseReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnoseReport',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/diagnosis/instances/{DaraURL.percent_encode(instance_id)}/reports/{DaraURL.percent_encode(report_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnoseReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnose_report(
        self,
        instance_id: str,
        report_id: str,
        request: main_models.DescribeDiagnoseReportRequest,
    ) -> main_models.DescribeDiagnoseReportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_diagnose_report_with_options(instance_id, report_id, request, headers, runtime)

    async def describe_diagnose_report_async(
        self,
        instance_id: str,
        report_id: str,
        request: main_models.DescribeDiagnoseReportRequest,
    ) -> main_models.DescribeDiagnoseReportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_diagnose_report_with_options_async(instance_id, report_id, request, headers, runtime)

    def describe_diagnosis_settings_with_options(
        self,
        instance_id: str,
        request: main_models.DescribeDiagnosisSettingsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnosisSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosisSettings',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/diagnosis/instances/{DaraURL.percent_encode(instance_id)}/settings',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnosisSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_settings_with_options_async(
        self,
        instance_id: str,
        request: main_models.DescribeDiagnosisSettingsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnosisSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosisSettings',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/diagnosis/instances/{DaraURL.percent_encode(instance_id)}/settings',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnosisSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_settings(
        self,
        instance_id: str,
        request: main_models.DescribeDiagnosisSettingsRequest,
    ) -> main_models.DescribeDiagnosisSettingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_diagnosis_settings_with_options(instance_id, request, headers, runtime)

    async def describe_diagnosis_settings_async(
        self,
        instance_id: str,
        request: main_models.DescribeDiagnosisSettingsRequest,
    ) -> main_models.DescribeDiagnosisSettingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_diagnosis_settings_with_options_async(instance_id, request, headers, runtime)

    def describe_dynamic_settings_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDynamicSettingsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeDynamicSettings',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/dynamic-settings',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDynamicSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dynamic_settings_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDynamicSettingsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeDynamicSettings',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/dynamic-settings',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDynamicSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dynamic_settings(
        self,
        instance_id: str,
    ) -> main_models.DescribeDynamicSettingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_dynamic_settings_with_options(instance_id, headers, runtime)

    async def describe_dynamic_settings_async(
        self,
        instance_id: str,
    ) -> main_models.DescribeDynamicSettingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_dynamic_settings_with_options_async(instance_id, headers, runtime)

    def describe_elasticsearch_health_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticsearchHealthResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticsearchHealth',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/elasticsearch-health',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticsearchHealthResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_elasticsearch_health_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticsearchHealthResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticsearchHealth',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/elasticsearch-health',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticsearchHealthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_elasticsearch_health(
        self,
        instance_id: str,
    ) -> main_models.DescribeElasticsearchHealthResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_elasticsearch_health_with_options(instance_id, headers, runtime)

    async def describe_elasticsearch_health_async(
        self,
        instance_id: str,
    ) -> main_models.DescribeElasticsearchHealthResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_elasticsearch_health_with_options_async(instance_id, headers, runtime)

    def describe_ilmpolicy_with_options(
        self,
        instance_id: str,
        policy_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeILMPolicyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeILMPolicy',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/ilm-policies/{DaraURL.percent_encode(policy_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeILMPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ilmpolicy_with_options_async(
        self,
        instance_id: str,
        policy_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeILMPolicyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeILMPolicy',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/ilm-policies/{DaraURL.percent_encode(policy_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeILMPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ilmpolicy(
        self,
        instance_id: str,
        policy_name: str,
    ) -> main_models.DescribeILMPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_ilmpolicy_with_options(instance_id, policy_name, headers, runtime)

    async def describe_ilmpolicy_async(
        self,
        instance_id: str,
        policy_name: str,
    ) -> main_models.DescribeILMPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_ilmpolicy_with_options_async(instance_id, policy_name, headers, runtime)

    def describe_index_template_with_options(
        self,
        instance_id: str,
        index_template: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIndexTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeIndexTemplate',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/index-templates/{DaraURL.percent_encode(index_template)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIndexTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_index_template_with_options_async(
        self,
        instance_id: str,
        index_template: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIndexTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeIndexTemplate',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/index-templates/{DaraURL.percent_encode(index_template)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIndexTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_index_template(
        self,
        instance_id: str,
        index_template: str,
    ) -> main_models.DescribeIndexTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_index_template_with_options(instance_id, index_template, headers, runtime)

    async def describe_index_template_async(
        self,
        instance_id: str,
        index_template: str,
    ) -> main_models.DescribeIndexTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_index_template_with_options_async(instance_id, index_template, headers, runtime)

    def describe_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstance',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstance',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance(
        self,
        instance_id: str,
    ) -> main_models.DescribeInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_instance_with_options(instance_id, headers, runtime)

    async def describe_instance_async(
        self,
        instance_id: str,
    ) -> main_models.DescribeInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_instance_with_options_async(instance_id, headers, runtime)

    def describe_kibana_settings_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKibanaSettingsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeKibanaSettings',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/kibana-settings',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeKibanaSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_kibana_settings_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKibanaSettingsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeKibanaSettings',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/kibana-settings',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeKibanaSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_kibana_settings(
        self,
        instance_id: str,
    ) -> main_models.DescribeKibanaSettingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_kibana_settings_with_options(instance_id, headers, runtime)

    async def describe_kibana_settings_async(
        self,
        instance_id: str,
    ) -> main_models.DescribeKibanaSettingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_kibana_settings_with_options_async(instance_id, headers, runtime)

    def describe_logstash_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogstashResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogstash',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogstashResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_logstash_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogstashResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogstash',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogstashResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_logstash(
        self,
        instance_id: str,
    ) -> main_models.DescribeLogstashResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_logstash_with_options(instance_id, headers, runtime)

    async def describe_logstash_async(
        self,
        instance_id: str,
    ) -> main_models.DescribeLogstashResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_logstash_with_options_async(instance_id, headers, runtime)

    def describe_pipeline_with_options(
        self,
        instance_id: str,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribePipelineResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribePipeline',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/pipelines/{DaraURL.percent_encode(pipeline_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pipeline_with_options_async(
        self,
        instance_id: str,
        pipeline_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribePipelineResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribePipeline',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/pipelines/{DaraURL.percent_encode(pipeline_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pipeline(
        self,
        instance_id: str,
        pipeline_id: str,
    ) -> main_models.DescribePipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_pipeline_with_options(instance_id, pipeline_id, headers, runtime)

    async def describe_pipeline_async(
        self,
        instance_id: str,
        pipeline_id: str,
    ) -> main_models.DescribePipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_pipeline_with_options_async(instance_id, pipeline_id, headers, runtime)

    def describe_pipeline_management_config_with_options(
        self,
        instance_id: str,
        request: main_models.DescribePipelineManagementConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribePipelineManagementConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePipelineManagementConfig',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/pipeline-management-config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePipelineManagementConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pipeline_management_config_with_options_async(
        self,
        instance_id: str,
        request: main_models.DescribePipelineManagementConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribePipelineManagementConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePipelineManagementConfig',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/pipeline-management-config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePipelineManagementConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pipeline_management_config(
        self,
        instance_id: str,
        request: main_models.DescribePipelineManagementConfigRequest,
    ) -> main_models.DescribePipelineManagementConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_pipeline_management_config_with_options(instance_id, request, headers, runtime)

    async def describe_pipeline_management_config_async(
        self,
        instance_id: str,
        request: main_models.DescribePipelineManagementConfigRequest,
    ) -> main_models.DescribePipelineManagementConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_pipeline_management_config_with_options_async(instance_id, request, headers, runtime)

    def describe_regions_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/regions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/regions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(self) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(headers, runtime)

    async def describe_regions_async(self) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(headers, runtime)

    def describe_snapshot_setting_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSnapshotSettingResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeSnapshotSetting',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/snapshot-setting',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSnapshotSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_snapshot_setting_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSnapshotSettingResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeSnapshotSetting',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/snapshot-setting',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSnapshotSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_snapshot_setting(
        self,
        instance_id: str,
    ) -> main_models.DescribeSnapshotSettingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_snapshot_setting_with_options(instance_id, headers, runtime)

    async def describe_snapshot_setting_async(
        self,
        instance_id: str,
    ) -> main_models.DescribeSnapshotSettingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_snapshot_setting_with_options_async(instance_id, headers, runtime)

    def describe_templates_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTemplatesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeTemplates',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/templates',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_templates_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTemplatesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeTemplates',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/templates',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_templates(
        self,
        instance_id: str,
    ) -> main_models.DescribeTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_templates_with_options(instance_id, headers, runtime)

    async def describe_templates_async(
        self,
        instance_id: str,
    ) -> main_models.DescribeTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_templates_with_options_async(instance_id, headers, runtime)

    def describe_xpack_monitor_config_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeXpackMonitorConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeXpackMonitorConfig',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/xpack-monitor-config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeXpackMonitorConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_xpack_monitor_config_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeXpackMonitorConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeXpackMonitorConfig',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/xpack-monitor-config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeXpackMonitorConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_xpack_monitor_config(
        self,
        instance_id: str,
    ) -> main_models.DescribeXpackMonitorConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_xpack_monitor_config_with_options(instance_id, headers, runtime)

    async def describe_xpack_monitor_config_async(
        self,
        instance_id: str,
    ) -> main_models.DescribeXpackMonitorConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_xpack_monitor_config_with_options_async(instance_id, headers, runtime)

    def diagnose_instance_with_options(
        self,
        instance_id: str,
        request: main_models.DiagnoseInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DiagnoseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        body = {}
        if not DaraCore.is_null(request.diagnose_items):
            body['diagnoseItems'] = request.diagnose_items
        if not DaraCore.is_null(request.indices):
            body['indices'] = request.indices
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DiagnoseInstance',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/diagnosis/instances/{DaraURL.percent_encode(instance_id)}/actions/diagnose',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DiagnoseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def diagnose_instance_with_options_async(
        self,
        instance_id: str,
        request: main_models.DiagnoseInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DiagnoseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        body = {}
        if not DaraCore.is_null(request.diagnose_items):
            body['diagnoseItems'] = request.diagnose_items
        if not DaraCore.is_null(request.indices):
            body['indices'] = request.indices
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DiagnoseInstance',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/diagnosis/instances/{DaraURL.percent_encode(instance_id)}/actions/diagnose',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DiagnoseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def diagnose_instance(
        self,
        instance_id: str,
        request: main_models.DiagnoseInstanceRequest,
    ) -> main_models.DiagnoseInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.diagnose_instance_with_options(instance_id, request, headers, runtime)

    async def diagnose_instance_async(
        self,
        instance_id: str,
        request: main_models.DiagnoseInstanceRequest,
    ) -> main_models.DiagnoseInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.diagnose_instance_with_options_async(instance_id, request, headers, runtime)

    def disable_kibana_pvl_network_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableKibanaPvlNetworkResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DisableKibanaPvlNetwork',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/disable-kibana-private',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableKibanaPvlNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_kibana_pvl_network_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableKibanaPvlNetworkResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DisableKibanaPvlNetwork',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/disable-kibana-private',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableKibanaPvlNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_kibana_pvl_network(
        self,
        instance_id: str,
    ) -> main_models.DisableKibanaPvlNetworkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.disable_kibana_pvl_network_with_options(instance_id, headers, runtime)

    async def disable_kibana_pvl_network_async(
        self,
        instance_id: str,
    ) -> main_models.DisableKibanaPvlNetworkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.disable_kibana_pvl_network_with_options_async(instance_id, headers, runtime)

    def enable_kibana_pvl_network_with_options(
        self,
        instance_id: str,
        request: main_models.EnableKibanaPvlNetworkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableKibanaPvlNetworkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.endpoint_name):
            body['endpointName'] = request.endpoint_name
        if not DaraCore.is_null(request.security_groups):
            body['securityGroups'] = request.security_groups
        if not DaraCore.is_null(request.v_switch_ids_zone):
            body['vSwitchIdsZone'] = request.v_switch_ids_zone
        if not DaraCore.is_null(request.vpc_id):
            body['vpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableKibanaPvlNetwork',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/enable-kibana-private',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableKibanaPvlNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_kibana_pvl_network_with_options_async(
        self,
        instance_id: str,
        request: main_models.EnableKibanaPvlNetworkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableKibanaPvlNetworkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.endpoint_name):
            body['endpointName'] = request.endpoint_name
        if not DaraCore.is_null(request.security_groups):
            body['securityGroups'] = request.security_groups
        if not DaraCore.is_null(request.v_switch_ids_zone):
            body['vSwitchIdsZone'] = request.v_switch_ids_zone
        if not DaraCore.is_null(request.vpc_id):
            body['vpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableKibanaPvlNetwork',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/enable-kibana-private',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableKibanaPvlNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_kibana_pvl_network(
        self,
        instance_id: str,
        request: main_models.EnableKibanaPvlNetworkRequest,
    ) -> main_models.EnableKibanaPvlNetworkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.enable_kibana_pvl_network_with_options(instance_id, request, headers, runtime)

    async def enable_kibana_pvl_network_async(
        self,
        instance_id: str,
        request: main_models.EnableKibanaPvlNetworkRequest,
    ) -> main_models.EnableKibanaPvlNetworkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.enable_kibana_pvl_network_with_options_async(instance_id, request, headers, runtime)

    def estimated_logstash_restart_time_with_options(
        self,
        instance_id: str,
        request: main_models.EstimatedLogstashRestartTimeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EstimatedLogstashRestartTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['force'] = request.force
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'EstimatedLogstashRestartTime',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/estimated-time/restart-time',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EstimatedLogstashRestartTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def estimated_logstash_restart_time_with_options_async(
        self,
        instance_id: str,
        request: main_models.EstimatedLogstashRestartTimeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EstimatedLogstashRestartTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['force'] = request.force
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'EstimatedLogstashRestartTime',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/estimated-time/restart-time',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EstimatedLogstashRestartTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def estimated_logstash_restart_time(
        self,
        instance_id: str,
        request: main_models.EstimatedLogstashRestartTimeRequest,
    ) -> main_models.EstimatedLogstashRestartTimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.estimated_logstash_restart_time_with_options(instance_id, request, headers, runtime)

    async def estimated_logstash_restart_time_async(
        self,
        instance_id: str,
        request: main_models.EstimatedLogstashRestartTimeRequest,
    ) -> main_models.EstimatedLogstashRestartTimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.estimated_logstash_restart_time_with_options_async(instance_id, request, headers, runtime)

    def estimated_restart_time_with_options(
        self,
        instance_id: str,
        request: main_models.EstimatedRestartTimeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EstimatedRestartTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['force'] = request.force
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'EstimatedRestartTime',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/estimated-time/restart-time',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EstimatedRestartTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def estimated_restart_time_with_options_async(
        self,
        instance_id: str,
        request: main_models.EstimatedRestartTimeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EstimatedRestartTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['force'] = request.force
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'EstimatedRestartTime',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/estimated-time/restart-time',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EstimatedRestartTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def estimated_restart_time(
        self,
        instance_id: str,
        request: main_models.EstimatedRestartTimeRequest,
    ) -> main_models.EstimatedRestartTimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.estimated_restart_time_with_options(instance_id, request, headers, runtime)

    async def estimated_restart_time_async(
        self,
        instance_id: str,
        request: main_models.EstimatedRestartTimeRequest,
    ) -> main_models.EstimatedRestartTimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.estimated_restart_time_with_options_async(instance_id, request, headers, runtime)

    def get_cluster_data_information_with_options(
        self,
        request: main_models.GetClusterDataInformationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterDataInformationResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'GetClusterDataInformation',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/cluster/data-information',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterDataInformationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_data_information_with_options_async(
        self,
        request: main_models.GetClusterDataInformationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterDataInformationResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'GetClusterDataInformation',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/cluster/data-information',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterDataInformationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_data_information(
        self,
        request: main_models.GetClusterDataInformationRequest,
    ) -> main_models.GetClusterDataInformationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_cluster_data_information_with_options(request, headers, runtime)

    async def get_cluster_data_information_async(
        self,
        request: main_models.GetClusterDataInformationRequest,
    ) -> main_models.GetClusterDataInformationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_cluster_data_information_with_options_async(request, headers, runtime)

    def get_elastictask_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetElastictaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetElastictask',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/elastic-task',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetElastictaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_elastictask_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetElastictaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetElastictask',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/elastic-task',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetElastictaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_elastictask(
        self,
        instance_id: str,
    ) -> main_models.GetElastictaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_elastictask_with_options(instance_id, headers, runtime)

    async def get_elastictask_async(
        self,
        instance_id: str,
    ) -> main_models.GetElastictaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_elastictask_with_options_async(instance_id, headers, runtime)

    def get_emon_alarm_record_statistics_distribute_with_options(
        self,
        request: main_models.GetEmonAlarmRecordStatisticsDistributeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEmonAlarmRecordStatisticsDistributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.body):
            query['body'] = request.body
        if not DaraCore.is_null(request.group_id):
            query['groupId'] = request.group_id
        if not DaraCore.is_null(request.time_end):
            query['timeEnd'] = request.time_end
        if not DaraCore.is_null(request.time_start):
            query['timeStart'] = request.time_start
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEmonAlarmRecordStatisticsDistribute',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/emon/alarm-record-statistics/distribute',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEmonAlarmRecordStatisticsDistributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_emon_alarm_record_statistics_distribute_with_options_async(
        self,
        request: main_models.GetEmonAlarmRecordStatisticsDistributeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEmonAlarmRecordStatisticsDistributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.body):
            query['body'] = request.body
        if not DaraCore.is_null(request.group_id):
            query['groupId'] = request.group_id
        if not DaraCore.is_null(request.time_end):
            query['timeEnd'] = request.time_end
        if not DaraCore.is_null(request.time_start):
            query['timeStart'] = request.time_start
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEmonAlarmRecordStatisticsDistribute',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/emon/alarm-record-statistics/distribute',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEmonAlarmRecordStatisticsDistributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_emon_alarm_record_statistics_distribute(
        self,
        request: main_models.GetEmonAlarmRecordStatisticsDistributeRequest,
    ) -> main_models.GetEmonAlarmRecordStatisticsDistributeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_emon_alarm_record_statistics_distribute_with_options(request, headers, runtime)

    async def get_emon_alarm_record_statistics_distribute_async(
        self,
        request: main_models.GetEmonAlarmRecordStatisticsDistributeRequest,
    ) -> main_models.GetEmonAlarmRecordStatisticsDistributeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_emon_alarm_record_statistics_distribute_with_options_async(request, headers, runtime)

    def get_emon_grafana_alerts_with_options(
        self,
        project_id: str,
        request: main_models.GetEmonGrafanaAlertsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEmonGrafanaAlertsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.body):
            query['body'] = request.body
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEmonGrafanaAlerts',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/emon/projects/{DaraURL.percent_encode(project_id)}/grafana/proxy/api/alerts',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEmonGrafanaAlertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_emon_grafana_alerts_with_options_async(
        self,
        project_id: str,
        request: main_models.GetEmonGrafanaAlertsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEmonGrafanaAlertsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.body):
            query['body'] = request.body
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEmonGrafanaAlerts',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/emon/projects/{DaraURL.percent_encode(project_id)}/grafana/proxy/api/alerts',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEmonGrafanaAlertsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_emon_grafana_alerts(
        self,
        project_id: str,
        request: main_models.GetEmonGrafanaAlertsRequest,
    ) -> main_models.GetEmonGrafanaAlertsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_emon_grafana_alerts_with_options(project_id, request, headers, runtime)

    async def get_emon_grafana_alerts_async(
        self,
        project_id: str,
        request: main_models.GetEmonGrafanaAlertsRequest,
    ) -> main_models.GetEmonGrafanaAlertsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_emon_grafana_alerts_with_options_async(project_id, request, headers, runtime)

    def get_emon_grafana_dashboards_with_options(
        self,
        project_id: str,
        request: main_models.GetEmonGrafanaDashboardsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEmonGrafanaDashboardsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.body):
            query['body'] = request.body
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEmonGrafanaDashboards',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/emon/projects/{DaraURL.percent_encode(project_id)}/grafana/proxy/api/search',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEmonGrafanaDashboardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_emon_grafana_dashboards_with_options_async(
        self,
        project_id: str,
        request: main_models.GetEmonGrafanaDashboardsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEmonGrafanaDashboardsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.body):
            query['body'] = request.body
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEmonGrafanaDashboards',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/emon/projects/{DaraURL.percent_encode(project_id)}/grafana/proxy/api/search',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEmonGrafanaDashboardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_emon_grafana_dashboards(
        self,
        project_id: str,
        request: main_models.GetEmonGrafanaDashboardsRequest,
    ) -> main_models.GetEmonGrafanaDashboardsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_emon_grafana_dashboards_with_options(project_id, request, headers, runtime)

    async def get_emon_grafana_dashboards_async(
        self,
        project_id: str,
        request: main_models.GetEmonGrafanaDashboardsRequest,
    ) -> main_models.GetEmonGrafanaDashboardsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_emon_grafana_dashboards_with_options_async(project_id, request, headers, runtime)

    def get_emon_monitor_data_with_options(
        self,
        project_id: str,
        request: main_models.GetEmonMonitorDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEmonMonitorDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.body):
            query['body'] = request.body
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEmonMonitorData',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/emon/projects/{DaraURL.percent_encode(project_id)}/metrics/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEmonMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_emon_monitor_data_with_options_async(
        self,
        project_id: str,
        request: main_models.GetEmonMonitorDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEmonMonitorDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.body):
            query['body'] = request.body
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEmonMonitorData',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/emon/projects/{DaraURL.percent_encode(project_id)}/metrics/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEmonMonitorDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_emon_monitor_data(
        self,
        project_id: str,
        request: main_models.GetEmonMonitorDataRequest,
    ) -> main_models.GetEmonMonitorDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_emon_monitor_data_with_options(project_id, request, headers, runtime)

    async def get_emon_monitor_data_async(
        self,
        project_id: str,
        request: main_models.GetEmonMonitorDataRequest,
    ) -> main_models.GetEmonMonitorDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_emon_monitor_data_with_options_async(project_id, request, headers, runtime)

    def get_open_store_usage_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOpenStoreUsageResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetOpenStoreUsage',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/openstore/usage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOpenStoreUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_open_store_usage_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOpenStoreUsageResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetOpenStoreUsage',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/openstore/usage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOpenStoreUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_open_store_usage(
        self,
        instance_id: str,
    ) -> main_models.GetOpenStoreUsageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_open_store_usage_with_options(instance_id, headers, runtime)

    async def get_open_store_usage_async(
        self,
        instance_id: str,
    ) -> main_models.GetOpenStoreUsageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_open_store_usage_with_options_async(instance_id, headers, runtime)

    def get_region_configuration_with_options(
        self,
        request: main_models.GetRegionConfigurationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRegionConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.zone_id):
            query['zoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRegionConfiguration',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/region',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRegionConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_region_configuration_with_options_async(
        self,
        request: main_models.GetRegionConfigurationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRegionConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.zone_id):
            query['zoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRegionConfiguration',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/region',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRegionConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_region_configuration(
        self,
        request: main_models.GetRegionConfigurationRequest,
    ) -> main_models.GetRegionConfigurationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_region_configuration_with_options(request, headers, runtime)

    async def get_region_configuration_async(
        self,
        request: main_models.GetRegionConfigurationRequest,
    ) -> main_models.GetRegionConfigurationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_region_configuration_with_options_async(request, headers, runtime)

    def get_regional_instance_config_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRegionalInstanceConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetRegionalInstanceConfig',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/regions/instance-config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRegionalInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_regional_instance_config_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRegionalInstanceConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetRegionalInstanceConfig',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/regions/instance-config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRegionalInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_regional_instance_config(self) -> main_models.GetRegionalInstanceConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_regional_instance_config_with_options(headers, runtime)

    async def get_regional_instance_config_async(self) -> main_models.GetRegionalInstanceConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_regional_instance_config_with_options_async(headers, runtime)

    def get_suggest_shrinkable_nodes_with_options(
        self,
        instance_id: str,
        request: main_models.GetSuggestShrinkableNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSuggestShrinkableNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.count):
            query['count'] = request.count
        if not DaraCore.is_null(request.ignore_status):
            query['ignoreStatus'] = request.ignore_status
        if not DaraCore.is_null(request.node_type):
            query['nodeType'] = request.node_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSuggestShrinkableNodes',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/suggest-shrinkable-nodes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSuggestShrinkableNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_suggest_shrinkable_nodes_with_options_async(
        self,
        instance_id: str,
        request: main_models.GetSuggestShrinkableNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSuggestShrinkableNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.count):
            query['count'] = request.count
        if not DaraCore.is_null(request.ignore_status):
            query['ignoreStatus'] = request.ignore_status
        if not DaraCore.is_null(request.node_type):
            query['nodeType'] = request.node_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSuggestShrinkableNodes',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/suggest-shrinkable-nodes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSuggestShrinkableNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_suggest_shrinkable_nodes(
        self,
        instance_id: str,
        request: main_models.GetSuggestShrinkableNodesRequest,
    ) -> main_models.GetSuggestShrinkableNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_suggest_shrinkable_nodes_with_options(instance_id, request, headers, runtime)

    async def get_suggest_shrinkable_nodes_async(
        self,
        instance_id: str,
        request: main_models.GetSuggestShrinkableNodesRequest,
    ) -> main_models.GetSuggestShrinkableNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_suggest_shrinkable_nodes_with_options_async(instance_id, request, headers, runtime)

    def get_transferable_nodes_with_options(
        self,
        instance_id: str,
        request: main_models.GetTransferableNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTransferableNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.count):
            query['count'] = request.count
        if not DaraCore.is_null(request.node_type):
            query['nodeType'] = request.node_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTransferableNodes',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/transferable-nodes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTransferableNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_transferable_nodes_with_options_async(
        self,
        instance_id: str,
        request: main_models.GetTransferableNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTransferableNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.count):
            query['count'] = request.count
        if not DaraCore.is_null(request.node_type):
            query['nodeType'] = request.node_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTransferableNodes',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/transferable-nodes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTransferableNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_transferable_nodes(
        self,
        instance_id: str,
        request: main_models.GetTransferableNodesRequest,
    ) -> main_models.GetTransferableNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_transferable_nodes_with_options(instance_id, request, headers, runtime)

    async def get_transferable_nodes_async(
        self,
        instance_id: str,
        request: main_models.GetTransferableNodesRequest,
    ) -> main_models.GetTransferableNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_transferable_nodes_with_options_async(instance_id, request, headers, runtime)

    def initialize_operation_role_with_options(
        self,
        request: main_models.InitializeOperationRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InitializeOperationRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'InitializeOperationRole',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/user/slr',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitializeOperationRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def initialize_operation_role_with_options_async(
        self,
        request: main_models.InitializeOperationRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InitializeOperationRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'InitializeOperationRole',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/user/slr',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitializeOperationRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def initialize_operation_role(
        self,
        request: main_models.InitializeOperationRoleRequest,
    ) -> main_models.InitializeOperationRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.initialize_operation_role_with_options(request, headers, runtime)

    async def initialize_operation_role_async(
        self,
        request: main_models.InitializeOperationRoleRequest,
    ) -> main_models.InitializeOperationRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.initialize_operation_role_with_options_async(request, headers, runtime)

    def install_ack_operator_with_options(
        self,
        cluster_id: str,
        request: main_models.InstallAckOperatorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallAckOperatorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'InstallAckOperator',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/ack-clusters/{DaraURL.percent_encode(cluster_id)}/operator',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallAckOperatorResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_ack_operator_with_options_async(
        self,
        cluster_id: str,
        request: main_models.InstallAckOperatorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallAckOperatorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'InstallAckOperator',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/ack-clusters/{DaraURL.percent_encode(cluster_id)}/operator',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallAckOperatorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_ack_operator(
        self,
        cluster_id: str,
        request: main_models.InstallAckOperatorRequest,
    ) -> main_models.InstallAckOperatorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.install_ack_operator_with_options(cluster_id, request, headers, runtime)

    async def install_ack_operator_async(
        self,
        cluster_id: str,
        request: main_models.InstallAckOperatorRequest,
    ) -> main_models.InstallAckOperatorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.install_ack_operator_with_options_async(cluster_id, request, headers, runtime)

    def install_kibana_system_plugin_with_options(
        self,
        instance_id: str,
        request: main_models.InstallKibanaSystemPluginRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallKibanaSystemPluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'InstallKibanaSystemPlugin',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/kibana-plugins/system/actions/install',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallKibanaSystemPluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_kibana_system_plugin_with_options_async(
        self,
        instance_id: str,
        request: main_models.InstallKibanaSystemPluginRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallKibanaSystemPluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'InstallKibanaSystemPlugin',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/kibana-plugins/system/actions/install',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallKibanaSystemPluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_kibana_system_plugin(
        self,
        instance_id: str,
        request: main_models.InstallKibanaSystemPluginRequest,
    ) -> main_models.InstallKibanaSystemPluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.install_kibana_system_plugin_with_options(instance_id, request, headers, runtime)

    async def install_kibana_system_plugin_async(
        self,
        instance_id: str,
        request: main_models.InstallKibanaSystemPluginRequest,
    ) -> main_models.InstallKibanaSystemPluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.install_kibana_system_plugin_with_options_async(instance_id, request, headers, runtime)

    def install_logstash_system_plugin_with_options(
        self,
        instance_id: str,
        request: main_models.InstallLogstashSystemPluginRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallLogstashSystemPluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'InstallLogstashSystemPlugin',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/plugins/system/actions/install',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallLogstashSystemPluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_logstash_system_plugin_with_options_async(
        self,
        instance_id: str,
        request: main_models.InstallLogstashSystemPluginRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallLogstashSystemPluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'InstallLogstashSystemPlugin',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/plugins/system/actions/install',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallLogstashSystemPluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_logstash_system_plugin(
        self,
        instance_id: str,
        request: main_models.InstallLogstashSystemPluginRequest,
    ) -> main_models.InstallLogstashSystemPluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.install_logstash_system_plugin_with_options(instance_id, request, headers, runtime)

    async def install_logstash_system_plugin_async(
        self,
        instance_id: str,
        request: main_models.InstallLogstashSystemPluginRequest,
    ) -> main_models.InstallLogstashSystemPluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.install_logstash_system_plugin_with_options_async(instance_id, request, headers, runtime)

    def install_system_plugin_with_options(
        self,
        instance_id: str,
        request: main_models.InstallSystemPluginRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallSystemPluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'InstallSystemPlugin',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/plugins/system/actions/install',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallSystemPluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_system_plugin_with_options_async(
        self,
        instance_id: str,
        request: main_models.InstallSystemPluginRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallSystemPluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'InstallSystemPlugin',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/plugins/system/actions/install',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallSystemPluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_system_plugin(
        self,
        instance_id: str,
        request: main_models.InstallSystemPluginRequest,
    ) -> main_models.InstallSystemPluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.install_system_plugin_with_options(instance_id, request, headers, runtime)

    async def install_system_plugin_async(
        self,
        instance_id: str,
        request: main_models.InstallSystemPluginRequest,
    ) -> main_models.InstallSystemPluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.install_system_plugin_with_options_async(instance_id, request, headers, runtime)

    def install_user_plugins_with_options(
        self,
        instance_id: str,
        request: main_models.InstallUserPluginsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallUserPluginsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['force'] = request.force
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'InstallUserPlugins',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/plugins/user/actions/install',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallUserPluginsResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_user_plugins_with_options_async(
        self,
        instance_id: str,
        request: main_models.InstallUserPluginsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallUserPluginsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['force'] = request.force
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'InstallUserPlugins',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/plugins/user/actions/install',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallUserPluginsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_user_plugins(
        self,
        instance_id: str,
        request: main_models.InstallUserPluginsRequest,
    ) -> main_models.InstallUserPluginsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.install_user_plugins_with_options(instance_id, request, headers, runtime)

    async def install_user_plugins_async(
        self,
        instance_id: str,
        request: main_models.InstallUserPluginsRequest,
    ) -> main_models.InstallUserPluginsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.install_user_plugins_with_options_async(instance_id, request, headers, runtime)

    def interrupt_elasticsearch_task_with_options(
        self,
        instance_id: str,
        request: main_models.InterruptElasticsearchTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InterruptElasticsearchTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InterruptElasticsearchTask',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/interrupt',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InterruptElasticsearchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def interrupt_elasticsearch_task_with_options_async(
        self,
        instance_id: str,
        request: main_models.InterruptElasticsearchTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InterruptElasticsearchTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InterruptElasticsearchTask',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/interrupt',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InterruptElasticsearchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def interrupt_elasticsearch_task(
        self,
        instance_id: str,
        request: main_models.InterruptElasticsearchTaskRequest,
    ) -> main_models.InterruptElasticsearchTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.interrupt_elasticsearch_task_with_options(instance_id, request, headers, runtime)

    async def interrupt_elasticsearch_task_async(
        self,
        instance_id: str,
        request: main_models.InterruptElasticsearchTaskRequest,
    ) -> main_models.InterruptElasticsearchTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.interrupt_elasticsearch_task_with_options_async(instance_id, request, headers, runtime)

    def interrupt_logstash_task_with_options(
        self,
        instance_id: str,
        request: main_models.InterruptLogstashTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InterruptLogstashTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InterruptLogstashTask',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/actions/interrupt',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InterruptLogstashTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def interrupt_logstash_task_with_options_async(
        self,
        instance_id: str,
        request: main_models.InterruptLogstashTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InterruptLogstashTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InterruptLogstashTask',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/actions/interrupt',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InterruptLogstashTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def interrupt_logstash_task(
        self,
        instance_id: str,
        request: main_models.InterruptLogstashTaskRequest,
    ) -> main_models.InterruptLogstashTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.interrupt_logstash_task_with_options(instance_id, request, headers, runtime)

    async def interrupt_logstash_task_async(
        self,
        instance_id: str,
        request: main_models.InterruptLogstashTaskRequest,
    ) -> main_models.InterruptLogstashTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.interrupt_logstash_task_with_options_async(instance_id, request, headers, runtime)

    def list_ack_clusters_with_options(
        self,
        request: main_models.ListAckClustersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAckClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.vpc_id):
            query['vpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAckClusters',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/ack-clusters',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAckClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ack_clusters_with_options_async(
        self,
        request: main_models.ListAckClustersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAckClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.vpc_id):
            query['vpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAckClusters',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/ack-clusters',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAckClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ack_clusters(
        self,
        request: main_models.ListAckClustersRequest,
    ) -> main_models.ListAckClustersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_ack_clusters_with_options(request, headers, runtime)

    async def list_ack_clusters_async(
        self,
        request: main_models.ListAckClustersRequest,
    ) -> main_models.ListAckClustersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_ack_clusters_with_options_async(request, headers, runtime)

    def list_ack_namespaces_with_options(
        self,
        cluster_id: str,
        request: main_models.ListAckNamespacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAckNamespacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAckNamespaces',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/ack-clusters/{DaraURL.percent_encode(cluster_id)}/namespaces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAckNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ack_namespaces_with_options_async(
        self,
        cluster_id: str,
        request: main_models.ListAckNamespacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAckNamespacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAckNamespaces',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/ack-clusters/{DaraURL.percent_encode(cluster_id)}/namespaces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAckNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ack_namespaces(
        self,
        cluster_id: str,
        request: main_models.ListAckNamespacesRequest,
    ) -> main_models.ListAckNamespacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_ack_namespaces_with_options(cluster_id, request, headers, runtime)

    async def list_ack_namespaces_async(
        self,
        cluster_id: str,
        request: main_models.ListAckNamespacesRequest,
    ) -> main_models.ListAckNamespacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_ack_namespaces_with_options_async(cluster_id, request, headers, runtime)

    def list_action_records_with_options(
        self,
        instance_id: str,
        request: main_models.ListActionRecordsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListActionRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_names):
            query['actionNames'] = request.action_names
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.filter):
            query['filter'] = request.filter
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.request_id):
            query['requestId'] = request.request_id
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.user_id):
            query['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListActionRecords',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/action-records',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListActionRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_action_records_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListActionRecordsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListActionRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_names):
            query['actionNames'] = request.action_names
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.filter):
            query['filter'] = request.filter
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.request_id):
            query['requestId'] = request.request_id
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.user_id):
            query['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListActionRecords',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/action-records',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListActionRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_action_records(
        self,
        instance_id: str,
        request: main_models.ListActionRecordsRequest,
    ) -> main_models.ListActionRecordsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_action_records_with_options(instance_id, request, headers, runtime)

    async def list_action_records_async(
        self,
        instance_id: str,
        request: main_models.ListActionRecordsRequest,
    ) -> main_models.ListActionRecordsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_action_records_with_options_async(instance_id, request, headers, runtime)

    def list_all_node_with_options(
        self,
        instance_id: str,
        request: main_models.ListAllNodeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAllNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.extended):
            query['extended'] = request.extended
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAllNode',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/nodes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAllNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_node_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListAllNodeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAllNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.extended):
            query['extended'] = request.extended
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAllNode',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/nodes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAllNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_all_node(
        self,
        instance_id: str,
        request: main_models.ListAllNodeRequest,
    ) -> main_models.ListAllNodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_all_node_with_options(instance_id, request, headers, runtime)

    async def list_all_node_async(
        self,
        instance_id: str,
        request: main_models.ListAllNodeRequest,
    ) -> main_models.ListAllNodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_all_node_with_options_async(instance_id, request, headers, runtime)

    def list_alternative_snapshot_repos_with_options(
        self,
        instance_id: str,
        request: main_models.ListAlternativeSnapshotReposRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAlternativeSnapshotReposResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.already_set_items):
            query['alreadySetItems'] = request.already_set_items
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlternativeSnapshotRepos',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/alternative-snapshot-repos',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlternativeSnapshotReposResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alternative_snapshot_repos_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListAlternativeSnapshotReposRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAlternativeSnapshotReposResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.already_set_items):
            query['alreadySetItems'] = request.already_set_items
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlternativeSnapshotRepos',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/alternative-snapshot-repos',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlternativeSnapshotReposResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alternative_snapshot_repos(
        self,
        instance_id: str,
        request: main_models.ListAlternativeSnapshotReposRequest,
    ) -> main_models.ListAlternativeSnapshotReposResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_alternative_snapshot_repos_with_options(instance_id, request, headers, runtime)

    async def list_alternative_snapshot_repos_async(
        self,
        instance_id: str,
        request: main_models.ListAlternativeSnapshotReposRequest,
    ) -> main_models.ListAlternativeSnapshotReposResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_alternative_snapshot_repos_with_options_async(instance_id, request, headers, runtime)

    def list_available_es_instance_ids_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAvailableEsInstanceIdsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListAvailableEsInstanceIds',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/available-elasticsearch-for-centralized-management',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAvailableEsInstanceIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_available_es_instance_ids_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAvailableEsInstanceIdsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListAvailableEsInstanceIds',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/available-elasticsearch-for-centralized-management',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAvailableEsInstanceIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_available_es_instance_ids(
        self,
        instance_id: str,
    ) -> main_models.ListAvailableEsInstanceIdsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_available_es_instance_ids_with_options(instance_id, headers, runtime)

    async def list_available_es_instance_ids_async(
        self,
        instance_id: str,
    ) -> main_models.ListAvailableEsInstanceIdsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_available_es_instance_ids_with_options_async(instance_id, headers, runtime)

    def list_collectors_with_options(
        self,
        request: main_models.ListCollectorsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCollectorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.res_id):
            query['resId'] = request.res_id
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.source_type):
            query['sourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCollectors',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/collectors',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCollectorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_collectors_with_options_async(
        self,
        request: main_models.ListCollectorsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCollectorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.res_id):
            query['resId'] = request.res_id
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.source_type):
            query['sourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCollectors',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/collectors',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCollectorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_collectors(
        self,
        request: main_models.ListCollectorsRequest,
    ) -> main_models.ListCollectorsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_collectors_with_options(request, headers, runtime)

    async def list_collectors_async(
        self,
        request: main_models.ListCollectorsRequest,
    ) -> main_models.ListCollectorsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_collectors_with_options_async(request, headers, runtime)

    def list_component_indices_with_options(
        self,
        instance_id: str,
        request: main_models.ListComponentIndicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListComponentIndicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListComponentIndices',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/component-index',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComponentIndicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_component_indices_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListComponentIndicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListComponentIndicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListComponentIndices',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/component-index',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComponentIndicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_component_indices(
        self,
        instance_id: str,
        request: main_models.ListComponentIndicesRequest,
    ) -> main_models.ListComponentIndicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_component_indices_with_options(instance_id, request, headers, runtime)

    async def list_component_indices_async(
        self,
        instance_id: str,
        request: main_models.ListComponentIndicesRequest,
    ) -> main_models.ListComponentIndicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_component_indices_with_options_async(instance_id, request, headers, runtime)

    def list_connected_clusters_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConnectedClustersResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListConnectedClusters',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/connected-clusters',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConnectedClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_connected_clusters_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConnectedClustersResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListConnectedClusters',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/connected-clusters',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConnectedClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_connected_clusters(
        self,
        instance_id: str,
    ) -> main_models.ListConnectedClustersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_connected_clusters_with_options(instance_id, headers, runtime)

    async def list_connected_clusters_async(
        self,
        instance_id: str,
    ) -> main_models.ListConnectedClustersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_connected_clusters_with_options_async(instance_id, headers, runtime)

    def list_data_streams_with_options(
        self,
        instance_id: str,
        request: main_models.ListDataStreamsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataStreamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_managed):
            query['isManaged'] = request.is_managed
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataStreams',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/data-streams',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataStreamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_streams_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListDataStreamsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataStreamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_managed):
            query['isManaged'] = request.is_managed
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataStreams',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/data-streams',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataStreamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_streams(
        self,
        instance_id: str,
        request: main_models.ListDataStreamsRequest,
    ) -> main_models.ListDataStreamsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_data_streams_with_options(instance_id, request, headers, runtime)

    async def list_data_streams_async(
        self,
        instance_id: str,
        request: main_models.ListDataStreamsRequest,
    ) -> main_models.ListDataStreamsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_data_streams_with_options_async(instance_id, request, headers, runtime)

    def list_data_tasks_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataTasksResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListDataTasks',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/data-task',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_tasks_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataTasksResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListDataTasks',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/data-task',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_tasks(
        self,
        instance_id: str,
    ) -> main_models.ListDataTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_data_tasks_with_options(instance_id, headers, runtime)

    async def list_data_tasks_async(
        self,
        instance_id: str,
    ) -> main_models.ListDataTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_data_tasks_with_options_async(instance_id, headers, runtime)

    def list_default_collector_configurations_with_options(
        self,
        request: main_models.ListDefaultCollectorConfigurationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDefaultCollectorConfigurationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.res_type):
            query['resType'] = request.res_type
        if not DaraCore.is_null(request.res_version):
            query['resVersion'] = request.res_version
        if not DaraCore.is_null(request.source_type):
            query['sourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDefaultCollectorConfigurations',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/beats/default-configurations',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDefaultCollectorConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_default_collector_configurations_with_options_async(
        self,
        request: main_models.ListDefaultCollectorConfigurationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDefaultCollectorConfigurationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.res_type):
            query['resType'] = request.res_type
        if not DaraCore.is_null(request.res_version):
            query['resVersion'] = request.res_version
        if not DaraCore.is_null(request.source_type):
            query['sourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDefaultCollectorConfigurations',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/beats/default-configurations',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDefaultCollectorConfigurationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_default_collector_configurations(
        self,
        request: main_models.ListDefaultCollectorConfigurationsRequest,
    ) -> main_models.ListDefaultCollectorConfigurationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_default_collector_configurations_with_options(request, headers, runtime)

    async def list_default_collector_configurations_async(
        self,
        request: main_models.ListDefaultCollectorConfigurationsRequest,
    ) -> main_models.ListDefaultCollectorConfigurationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_default_collector_configurations_with_options_async(request, headers, runtime)

    def list_deprecated_templates_with_options(
        self,
        instance_id: str,
        request: main_models.ListDeprecatedTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDeprecatedTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeprecatedTemplates',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/deprecated-templates',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeprecatedTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deprecated_templates_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListDeprecatedTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDeprecatedTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeprecatedTemplates',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/deprecated-templates',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeprecatedTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deprecated_templates(
        self,
        instance_id: str,
        request: main_models.ListDeprecatedTemplatesRequest,
    ) -> main_models.ListDeprecatedTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_deprecated_templates_with_options(instance_id, request, headers, runtime)

    async def list_deprecated_templates_async(
        self,
        instance_id: str,
        request: main_models.ListDeprecatedTemplatesRequest,
    ) -> main_models.ListDeprecatedTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_deprecated_templates_with_options_async(instance_id, request, headers, runtime)

    def list_diagnose_indices_with_options(
        self,
        instance_id: str,
        request: main_models.ListDiagnoseIndicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDiagnoseIndicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDiagnoseIndices',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/diagnosis/instances/{DaraURL.percent_encode(instance_id)}/indices',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDiagnoseIndicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_diagnose_indices_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListDiagnoseIndicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDiagnoseIndicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDiagnoseIndices',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/diagnosis/instances/{DaraURL.percent_encode(instance_id)}/indices',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDiagnoseIndicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_diagnose_indices(
        self,
        instance_id: str,
        request: main_models.ListDiagnoseIndicesRequest,
    ) -> main_models.ListDiagnoseIndicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_diagnose_indices_with_options(instance_id, request, headers, runtime)

    async def list_diagnose_indices_async(
        self,
        instance_id: str,
        request: main_models.ListDiagnoseIndicesRequest,
    ) -> main_models.ListDiagnoseIndicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_diagnose_indices_with_options_async(instance_id, request, headers, runtime)

    def list_diagnose_report_with_options(
        self,
        instance_id: str,
        request: main_models.ListDiagnoseReportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDiagnoseReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.detail):
            query['detail'] = request.detail
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.trigger):
            query['trigger'] = request.trigger
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDiagnoseReport',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/diagnosis/instances/{DaraURL.percent_encode(instance_id)}/reports',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDiagnoseReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_diagnose_report_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListDiagnoseReportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDiagnoseReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.detail):
            query['detail'] = request.detail
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.trigger):
            query['trigger'] = request.trigger
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDiagnoseReport',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/diagnosis/instances/{DaraURL.percent_encode(instance_id)}/reports',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDiagnoseReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_diagnose_report(
        self,
        instance_id: str,
        request: main_models.ListDiagnoseReportRequest,
    ) -> main_models.ListDiagnoseReportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_diagnose_report_with_options(instance_id, request, headers, runtime)

    async def list_diagnose_report_async(
        self,
        instance_id: str,
        request: main_models.ListDiagnoseReportRequest,
    ) -> main_models.ListDiagnoseReportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_diagnose_report_with_options_async(instance_id, request, headers, runtime)

    def list_diagnose_report_ids_with_options(
        self,
        instance_id: str,
        request: main_models.ListDiagnoseReportIdsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDiagnoseReportIdsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.trigger):
            query['trigger'] = request.trigger
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDiagnoseReportIds',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/diagnosis/instances/{DaraURL.percent_encode(instance_id)}/report-ids',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDiagnoseReportIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_diagnose_report_ids_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListDiagnoseReportIdsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDiagnoseReportIdsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.trigger):
            query['trigger'] = request.trigger
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDiagnoseReportIds',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/diagnosis/instances/{DaraURL.percent_encode(instance_id)}/report-ids',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDiagnoseReportIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_diagnose_report_ids(
        self,
        instance_id: str,
        request: main_models.ListDiagnoseReportIdsRequest,
    ) -> main_models.ListDiagnoseReportIdsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_diagnose_report_ids_with_options(instance_id, request, headers, runtime)

    async def list_diagnose_report_ids_async(
        self,
        instance_id: str,
        request: main_models.ListDiagnoseReportIdsRequest,
    ) -> main_models.ListDiagnoseReportIdsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_diagnose_report_ids_with_options_async(instance_id, request, headers, runtime)

    def list_diagnosis_items_with_options(
        self,
        request: main_models.ListDiagnosisItemsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDiagnosisItemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDiagnosisItems',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/diagnosis/items',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDiagnosisItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_diagnosis_items_with_options_async(
        self,
        request: main_models.ListDiagnosisItemsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDiagnosisItemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDiagnosisItems',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/diagnosis/items',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDiagnosisItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_diagnosis_items(
        self,
        request: main_models.ListDiagnosisItemsRequest,
    ) -> main_models.ListDiagnosisItemsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_diagnosis_items_with_options(request, headers, runtime)

    async def list_diagnosis_items_async(
        self,
        request: main_models.ListDiagnosisItemsRequest,
    ) -> main_models.ListDiagnosisItemsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_diagnosis_items_with_options_async(request, headers, runtime)

    def list_dict_information_with_options(
        self,
        instance_id: str,
        request: main_models.ListDictInformationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDictInformationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.analyzer_type):
            query['analyzerType'] = request.analyzer_type
        if not DaraCore.is_null(request.bucket_name):
            query['bucketName'] = request.bucket_name
        if not DaraCore.is_null(request.key):
            query['key'] = request.key
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDictInformation',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/dict/_info',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDictInformationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dict_information_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListDictInformationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDictInformationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.analyzer_type):
            query['analyzerType'] = request.analyzer_type
        if not DaraCore.is_null(request.bucket_name):
            query['bucketName'] = request.bucket_name
        if not DaraCore.is_null(request.key):
            query['key'] = request.key
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDictInformation',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/dict/_info',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDictInformationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dict_information(
        self,
        instance_id: str,
        request: main_models.ListDictInformationRequest,
    ) -> main_models.ListDictInformationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_dict_information_with_options(instance_id, request, headers, runtime)

    async def list_dict_information_async(
        self,
        instance_id: str,
        request: main_models.ListDictInformationRequest,
    ) -> main_models.ListDictInformationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_dict_information_with_options_async(instance_id, request, headers, runtime)

    def list_dicts_with_options(
        self,
        instance_id: str,
        request: main_models.ListDictsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDictsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.analyzer_type):
            query['analyzerType'] = request.analyzer_type
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDicts',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/dicts',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDictsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dicts_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListDictsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDictsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.analyzer_type):
            query['analyzerType'] = request.analyzer_type
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDicts',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/dicts',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDictsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dicts(
        self,
        instance_id: str,
        request: main_models.ListDictsRequest,
    ) -> main_models.ListDictsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_dicts_with_options(instance_id, request, headers, runtime)

    async def list_dicts_async(
        self,
        instance_id: str,
        request: main_models.ListDictsRequest,
    ) -> main_models.ListDictsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_dicts_with_options_async(instance_id, request, headers, runtime)

    def list_ecs_instances_with_options(
        self,
        request: main_models.ListEcsInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEcsInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ecs_instance_ids):
            query['ecsInstanceIds'] = request.ecs_instance_ids
        if not DaraCore.is_null(request.ecs_instance_name):
            query['ecsInstanceName'] = request.ecs_instance_name
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.tags):
            query['tags'] = request.tags
        if not DaraCore.is_null(request.vpc_id):
            query['vpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEcsInstances',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/ecs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEcsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ecs_instances_with_options_async(
        self,
        request: main_models.ListEcsInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEcsInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ecs_instance_ids):
            query['ecsInstanceIds'] = request.ecs_instance_ids
        if not DaraCore.is_null(request.ecs_instance_name):
            query['ecsInstanceName'] = request.ecs_instance_name
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.tags):
            query['tags'] = request.tags
        if not DaraCore.is_null(request.vpc_id):
            query['vpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEcsInstances',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/ecs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEcsInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ecs_instances(
        self,
        request: main_models.ListEcsInstancesRequest,
    ) -> main_models.ListEcsInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_ecs_instances_with_options(request, headers, runtime)

    async def list_ecs_instances_async(
        self,
        request: main_models.ListEcsInstancesRequest,
    ) -> main_models.ListEcsInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_ecs_instances_with_options_async(request, headers, runtime)

    def list_extendfiles_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListExtendfilesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListExtendfiles',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/extendfiles',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExtendfilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_extendfiles_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListExtendfilesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListExtendfiles',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/extendfiles',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExtendfilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_extendfiles(
        self,
        instance_id: str,
    ) -> main_models.ListExtendfilesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_extendfiles_with_options(instance_id, headers, runtime)

    async def list_extendfiles_async(
        self,
        instance_id: str,
    ) -> main_models.ListExtendfilesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_extendfiles_with_options_async(instance_id, headers, runtime)

    def list_ilmpolicies_with_options(
        self,
        instance_id: str,
        request: main_models.ListILMPoliciesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListILMPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['policyName'] = request.policy_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListILMPolicies',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/ilm-policies',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListILMPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ilmpolicies_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListILMPoliciesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListILMPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_name):
            query['policyName'] = request.policy_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListILMPolicies',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/ilm-policies',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListILMPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ilmpolicies(
        self,
        instance_id: str,
        request: main_models.ListILMPoliciesRequest,
    ) -> main_models.ListILMPoliciesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_ilmpolicies_with_options(instance_id, request, headers, runtime)

    async def list_ilmpolicies_async(
        self,
        instance_id: str,
        request: main_models.ListILMPoliciesRequest,
    ) -> main_models.ListILMPoliciesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_ilmpolicies_with_options_async(instance_id, request, headers, runtime)

    def list_index_templates_with_options(
        self,
        instance_id: str,
        request: main_models.ListIndexTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIndexTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.index_template):
            query['indexTemplate'] = request.index_template
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIndexTemplates',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/index-templates',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIndexTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_index_templates_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListIndexTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIndexTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.index_template):
            query['indexTemplate'] = request.index_template
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIndexTemplates',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/index-templates',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIndexTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_index_templates(
        self,
        instance_id: str,
        request: main_models.ListIndexTemplatesRequest,
    ) -> main_models.ListIndexTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_index_templates_with_options(instance_id, request, headers, runtime)

    async def list_index_templates_async(
        self,
        instance_id: str,
        request: main_models.ListIndexTemplatesRequest,
    ) -> main_models.ListIndexTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_index_templates_with_options_async(instance_id, request, headers, runtime)

    def list_instance_with_options(
        self,
        request: main_models.ListInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.es_version):
            query['esVersion'] = request.es_version
        if not DaraCore.is_null(request.instance_category):
            query['instanceCategory'] = request.instance_category
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.payment_type):
            query['paymentType'] = request.payment_type
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.tags):
            query['tags'] = request.tags
        if not DaraCore.is_null(request.vpc_id):
            query['vpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['zoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstance',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_with_options_async(
        self,
        request: main_models.ListInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.es_version):
            query['esVersion'] = request.es_version
        if not DaraCore.is_null(request.instance_category):
            query['instanceCategory'] = request.instance_category
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.payment_type):
            query['paymentType'] = request.payment_type
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.tags):
            query['tags'] = request.tags
        if not DaraCore.is_null(request.vpc_id):
            query['vpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['zoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstance',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance(
        self,
        request: main_models.ListInstanceRequest,
    ) -> main_models.ListInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_instance_with_options(request, headers, runtime)

    async def list_instance_async(
        self,
        request: main_models.ListInstanceRequest,
    ) -> main_models.ListInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_instance_with_options_async(request, headers, runtime)

    def list_instance_history_events_with_options(
        self,
        tmp_req: main_models.ListInstanceHistoryEventsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceHistoryEventsResponse:
        tmp_req.validate()
        request = main_models.ListInstanceHistoryEventsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.event_cycle_status):
            request.event_cycle_status_shrink = Utils.array_to_string_with_specified_style(tmp_req.event_cycle_status, 'eventCycleStatus', 'simple')
        if not DaraCore.is_null(tmp_req.event_level):
            request.event_level_shrink = Utils.array_to_string_with_specified_style(tmp_req.event_level, 'eventLevel', 'simple')
        if not DaraCore.is_null(tmp_req.event_type):
            request.event_type_shrink = Utils.array_to_string_with_specified_style(tmp_req.event_type, 'eventType', 'simple')
        query = {}
        if not DaraCore.is_null(request.event_create_end_time):
            query['eventCreateEndTime'] = request.event_create_end_time
        if not DaraCore.is_null(request.event_create_start_time):
            query['eventCreateStartTime'] = request.event_create_start_time
        if not DaraCore.is_null(request.event_cycle_status_shrink):
            query['eventCycleStatus'] = request.event_cycle_status_shrink
        if not DaraCore.is_null(request.event_execute_end_time):
            query['eventExecuteEndTime'] = request.event_execute_end_time
        if not DaraCore.is_null(request.event_execute_start_time):
            query['eventExecuteStartTime'] = request.event_execute_start_time
        if not DaraCore.is_null(request.event_finash_end_time):
            query['eventFinashEndTime'] = request.event_finash_end_time
        if not DaraCore.is_null(request.event_finash_start_time):
            query['eventFinashStartTime'] = request.event_finash_start_time
        if not DaraCore.is_null(request.event_level_shrink):
            query['eventLevel'] = request.event_level_shrink
        if not DaraCore.is_null(request.event_type_shrink):
            query['eventType'] = request.event_type_shrink
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_ip):
            query['nodeIP'] = request.node_ip
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceHistoryEvents',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/events',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceHistoryEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_history_events_with_options_async(
        self,
        tmp_req: main_models.ListInstanceHistoryEventsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceHistoryEventsResponse:
        tmp_req.validate()
        request = main_models.ListInstanceHistoryEventsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.event_cycle_status):
            request.event_cycle_status_shrink = Utils.array_to_string_with_specified_style(tmp_req.event_cycle_status, 'eventCycleStatus', 'simple')
        if not DaraCore.is_null(tmp_req.event_level):
            request.event_level_shrink = Utils.array_to_string_with_specified_style(tmp_req.event_level, 'eventLevel', 'simple')
        if not DaraCore.is_null(tmp_req.event_type):
            request.event_type_shrink = Utils.array_to_string_with_specified_style(tmp_req.event_type, 'eventType', 'simple')
        query = {}
        if not DaraCore.is_null(request.event_create_end_time):
            query['eventCreateEndTime'] = request.event_create_end_time
        if not DaraCore.is_null(request.event_create_start_time):
            query['eventCreateStartTime'] = request.event_create_start_time
        if not DaraCore.is_null(request.event_cycle_status_shrink):
            query['eventCycleStatus'] = request.event_cycle_status_shrink
        if not DaraCore.is_null(request.event_execute_end_time):
            query['eventExecuteEndTime'] = request.event_execute_end_time
        if not DaraCore.is_null(request.event_execute_start_time):
            query['eventExecuteStartTime'] = request.event_execute_start_time
        if not DaraCore.is_null(request.event_finash_end_time):
            query['eventFinashEndTime'] = request.event_finash_end_time
        if not DaraCore.is_null(request.event_finash_start_time):
            query['eventFinashStartTime'] = request.event_finash_start_time
        if not DaraCore.is_null(request.event_level_shrink):
            query['eventLevel'] = request.event_level_shrink
        if not DaraCore.is_null(request.event_type_shrink):
            query['eventType'] = request.event_type_shrink
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_ip):
            query['nodeIP'] = request.node_ip
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceHistoryEvents',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/events',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceHistoryEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_history_events(
        self,
        request: main_models.ListInstanceHistoryEventsRequest,
    ) -> main_models.ListInstanceHistoryEventsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_instance_history_events_with_options(request, headers, runtime)

    async def list_instance_history_events_async(
        self,
        request: main_models.ListInstanceHistoryEventsRequest,
    ) -> main_models.ListInstanceHistoryEventsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_instance_history_events_with_options_async(request, headers, runtime)

    def list_instance_indices_with_options(
        self,
        instance_id: str,
        request: main_models.ListInstanceIndicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceIndicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['all'] = request.all
        if not DaraCore.is_null(request.is_managed):
            query['isManaged'] = request.is_managed
        if not DaraCore.is_null(request.is_openstore):
            query['isOpenstore'] = request.is_openstore
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceIndices',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/indices',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceIndicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_indices_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListInstanceIndicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceIndicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['all'] = request.all
        if not DaraCore.is_null(request.is_managed):
            query['isManaged'] = request.is_managed
        if not DaraCore.is_null(request.is_openstore):
            query['isOpenstore'] = request.is_openstore
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceIndices',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/indices',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceIndicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_indices(
        self,
        instance_id: str,
        request: main_models.ListInstanceIndicesRequest,
    ) -> main_models.ListInstanceIndicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_instance_indices_with_options(instance_id, request, headers, runtime)

    async def list_instance_indices_async(
        self,
        instance_id: str,
        request: main_models.ListInstanceIndicesRequest,
    ) -> main_models.ListInstanceIndicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_instance_indices_with_options_async(instance_id, request, headers, runtime)

    def list_kibana_plugins_with_options(
        self,
        instance_id: str,
        request: main_models.ListKibanaPluginsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListKibanaPluginsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKibanaPlugins',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/kibana-plugins',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKibanaPluginsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_kibana_plugins_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListKibanaPluginsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListKibanaPluginsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKibanaPlugins',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/kibana-plugins',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKibanaPluginsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_kibana_plugins(
        self,
        instance_id: str,
        request: main_models.ListKibanaPluginsRequest,
    ) -> main_models.ListKibanaPluginsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_kibana_plugins_with_options(instance_id, request, headers, runtime)

    async def list_kibana_plugins_async(
        self,
        instance_id: str,
        request: main_models.ListKibanaPluginsRequest,
    ) -> main_models.ListKibanaPluginsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_kibana_plugins_with_options_async(instance_id, request, headers, runtime)

    def list_kibana_pvl_network_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListKibanaPvlNetworkResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListKibanaPvlNetwork',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/get-kibana-private',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKibanaPvlNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_kibana_pvl_network_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListKibanaPvlNetworkResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListKibanaPvlNetwork',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/get-kibana-private',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKibanaPvlNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_kibana_pvl_network(
        self,
        instance_id: str,
    ) -> main_models.ListKibanaPvlNetworkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_kibana_pvl_network_with_options(instance_id, headers, runtime)

    async def list_kibana_pvl_network_async(
        self,
        instance_id: str,
    ) -> main_models.ListKibanaPvlNetworkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_kibana_pvl_network_with_options_async(instance_id, headers, runtime)

    def list_logstash_with_options(
        self,
        request: main_models.ListLogstashRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLogstashResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.tags):
            query['tags'] = request.tags
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLogstash',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLogstashResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_logstash_with_options_async(
        self,
        request: main_models.ListLogstashRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLogstashResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.tags):
            query['tags'] = request.tags
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLogstash',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLogstashResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_logstash(
        self,
        request: main_models.ListLogstashRequest,
    ) -> main_models.ListLogstashResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_logstash_with_options(request, headers, runtime)

    async def list_logstash_async(
        self,
        request: main_models.ListLogstashRequest,
    ) -> main_models.ListLogstashResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_logstash_with_options_async(request, headers, runtime)

    def list_logstash_log_with_options(
        self,
        instance_id: str,
        request: main_models.ListLogstashLogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLogstashLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLogstashLog',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/search-log',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLogstashLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_logstash_log_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListLogstashLogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLogstashLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLogstashLog',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/search-log',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLogstashLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_logstash_log(
        self,
        instance_id: str,
        request: main_models.ListLogstashLogRequest,
    ) -> main_models.ListLogstashLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_logstash_log_with_options(instance_id, request, headers, runtime)

    async def list_logstash_log_async(
        self,
        instance_id: str,
        request: main_models.ListLogstashLogRequest,
    ) -> main_models.ListLogstashLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_logstash_log_with_options_async(instance_id, request, headers, runtime)

    def list_logstash_plugins_with_options(
        self,
        instance_id: str,
        request: main_models.ListLogstashPluginsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLogstashPluginsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLogstashPlugins',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/plugins',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLogstashPluginsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_logstash_plugins_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListLogstashPluginsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLogstashPluginsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLogstashPlugins',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/plugins',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLogstashPluginsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_logstash_plugins(
        self,
        instance_id: str,
        request: main_models.ListLogstashPluginsRequest,
    ) -> main_models.ListLogstashPluginsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_logstash_plugins_with_options(instance_id, request, headers, runtime)

    async def list_logstash_plugins_async(
        self,
        instance_id: str,
        request: main_models.ListLogstashPluginsRequest,
    ) -> main_models.ListLogstashPluginsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_logstash_plugins_with_options_async(instance_id, request, headers, runtime)

    def list_nodes_with_options(
        self,
        res_id: str,
        request: main_models.ListNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ecs_instance_ids):
            query['ecsInstanceIds'] = request.ecs_instance_ids
        if not DaraCore.is_null(request.ecs_instance_name):
            query['ecsInstanceName'] = request.ecs_instance_name
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.tags):
            query['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNodes',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/collectors/{DaraURL.percent_encode(res_id)}/nodes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nodes_with_options_async(
        self,
        res_id: str,
        request: main_models.ListNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ecs_instance_ids):
            query['ecsInstanceIds'] = request.ecs_instance_ids
        if not DaraCore.is_null(request.ecs_instance_name):
            query['ecsInstanceName'] = request.ecs_instance_name
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.tags):
            query['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNodes',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/collectors/{DaraURL.percent_encode(res_id)}/nodes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nodes(
        self,
        res_id: str,
        request: main_models.ListNodesRequest,
    ) -> main_models.ListNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_nodes_with_options(res_id, request, headers, runtime)

    async def list_nodes_async(
        self,
        res_id: str,
        request: main_models.ListNodesRequest,
    ) -> main_models.ListNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_nodes_with_options_async(res_id, request, headers, runtime)

    def list_pipeline_with_options(
        self,
        instance_id: str,
        request: main_models.ListPipelineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPipelineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.pipeline_id):
            query['pipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPipeline',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/pipelines',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListPipelineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPipelineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.pipeline_id):
            query['pipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPipeline',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/pipelines',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline(
        self,
        instance_id: str,
        request: main_models.ListPipelineRequest,
    ) -> main_models.ListPipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_pipeline_with_options(instance_id, request, headers, runtime)

    async def list_pipeline_async(
        self,
        instance_id: str,
        request: main_models.ListPipelineRequest,
    ) -> main_models.ListPipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_pipeline_with_options_async(instance_id, request, headers, runtime)

    def list_pipeline_ids_with_options(
        self,
        instance_id: str,
        request: main_models.ListPipelineIdsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPipelineIdsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'ListPipelineIds',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/pipeline-ids',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPipelineIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipeline_ids_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListPipelineIdsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPipelineIdsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'ListPipelineIds',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/pipeline-ids',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPipelineIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipeline_ids(
        self,
        instance_id: str,
        request: main_models.ListPipelineIdsRequest,
    ) -> main_models.ListPipelineIdsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_pipeline_ids_with_options(instance_id, request, headers, runtime)

    async def list_pipeline_ids_async(
        self,
        instance_id: str,
        request: main_models.ListPipelineIdsRequest,
    ) -> main_models.ListPipelineIdsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_pipeline_ids_with_options_async(instance_id, request, headers, runtime)

    def list_plugins_with_options(
        self,
        instance_id: str,
        request: main_models.ListPluginsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPluginsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPlugins',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/plugins',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPluginsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_plugins_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListPluginsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPluginsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPlugins',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/plugins',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPluginsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_plugins(
        self,
        instance_id: str,
        request: main_models.ListPluginsRequest,
    ) -> main_models.ListPluginsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_plugins_with_options(instance_id, request, headers, runtime)

    async def list_plugins_async(
        self,
        instance_id: str,
        request: main_models.ListPluginsRequest,
    ) -> main_models.ListPluginsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_plugins_with_options_async(instance_id, request, headers, runtime)

    def list_search_log_with_options(
        self,
        instance_id: str,
        request: main_models.ListSearchLogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSearchLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSearchLog',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/search-log',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSearchLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_search_log_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListSearchLogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSearchLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['beginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSearchLog',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/search-log',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSearchLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_search_log(
        self,
        instance_id: str,
        request: main_models.ListSearchLogRequest,
    ) -> main_models.ListSearchLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_search_log_with_options(instance_id, request, headers, runtime)

    async def list_search_log_async(
        self,
        instance_id: str,
        request: main_models.ListSearchLogRequest,
    ) -> main_models.ListSearchLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_search_log_with_options_async(instance_id, request, headers, runtime)

    def list_shard_recoveries_with_options(
        self,
        instance_id: str,
        request: main_models.ListShardRecoveriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListShardRecoveriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active_only):
            query['activeOnly'] = request.active_only
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListShardRecoveries',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/cat-recovery',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListShardRecoveriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_shard_recoveries_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListShardRecoveriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListShardRecoveriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active_only):
            query['activeOnly'] = request.active_only
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListShardRecoveries',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/cat-recovery',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListShardRecoveriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_shard_recoveries(
        self,
        instance_id: str,
        request: main_models.ListShardRecoveriesRequest,
    ) -> main_models.ListShardRecoveriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_shard_recoveries_with_options(instance_id, request, headers, runtime)

    async def list_shard_recoveries_async(
        self,
        instance_id: str,
        request: main_models.ListShardRecoveriesRequest,
    ) -> main_models.ListShardRecoveriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_shard_recoveries_with_options_async(instance_id, request, headers, runtime)

    def list_snapshot_repos_by_instance_id_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSnapshotReposByInstanceIdResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListSnapshotReposByInstanceId',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/snapshot-repos',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSnapshotReposByInstanceIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_snapshot_repos_by_instance_id_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSnapshotReposByInstanceIdResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListSnapshotReposByInstanceId',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/snapshot-repos',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSnapshotReposByInstanceIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_snapshot_repos_by_instance_id(
        self,
        instance_id: str,
    ) -> main_models.ListSnapshotReposByInstanceIdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_snapshot_repos_by_instance_id_with_options(instance_id, headers, runtime)

    async def list_snapshot_repos_by_instance_id_async(
        self,
        instance_id: str,
    ) -> main_models.ListSnapshotReposByInstanceIdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_snapshot_repos_by_instance_id_with_options_async(instance_id, headers, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/tags',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/tags',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_tag_resources_with_options_async(request, headers, runtime)

    def list_tags_with_options(
        self,
        request: main_models.ListTagsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTags',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/tags/all-tags',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tags_with_options_async(
        self,
        request: main_models.ListTagsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTags',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/tags/all-tags',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tags(
        self,
        request: main_models.ListTagsRequest,
    ) -> main_models.ListTagsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_tags_with_options(request, headers, runtime)

    async def list_tags_async(
        self,
        request: main_models.ListTagsRequest,
    ) -> main_models.ListTagsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_tags_with_options_async(request, headers, runtime)

    def list_vpc_endpoints_with_options(
        self,
        instance_id: str,
        request: main_models.ListVpcEndpointsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVpcEndpoints',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/vpc-endpoints',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_endpoints_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListVpcEndpointsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVpcEndpoints',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/vpc-endpoints',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_endpoints(
        self,
        instance_id: str,
        request: main_models.ListVpcEndpointsRequest,
    ) -> main_models.ListVpcEndpointsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_vpc_endpoints_with_options(instance_id, request, headers, runtime)

    async def list_vpc_endpoints_async(
        self,
        instance_id: str,
        request: main_models.ListVpcEndpointsRequest,
    ) -> main_models.ListVpcEndpointsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_vpc_endpoints_with_options_async(instance_id, request, headers, runtime)

    def migrate_to_other_zone_with_options(
        self,
        instance_id: str,
        request: main_models.MigrateToOtherZoneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.MigrateToOtherZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'MigrateToOtherZone',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/migrate-zones',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MigrateToOtherZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def migrate_to_other_zone_with_options_async(
        self,
        instance_id: str,
        request: main_models.MigrateToOtherZoneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.MigrateToOtherZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'MigrateToOtherZone',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/migrate-zones',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MigrateToOtherZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def migrate_to_other_zone(
        self,
        instance_id: str,
        request: main_models.MigrateToOtherZoneRequest,
    ) -> main_models.MigrateToOtherZoneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.migrate_to_other_zone_with_options(instance_id, request, headers, runtime)

    async def migrate_to_other_zone_async(
        self,
        instance_id: str,
        request: main_models.MigrateToOtherZoneRequest,
    ) -> main_models.MigrateToOtherZoneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.migrate_to_other_zone_with_options_async(instance_id, request, headers, runtime)

    def modify_deploy_machine_with_options(
        self,
        res_id: str,
        request: main_models.ModifyDeployMachineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDeployMachineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'ModifyDeployMachine',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/collectors/{DaraURL.percent_encode(res_id)}/actions/modify-deploy-machines',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDeployMachineResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_deploy_machine_with_options_async(
        self,
        res_id: str,
        request: main_models.ModifyDeployMachineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDeployMachineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'ModifyDeployMachine',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/collectors/{DaraURL.percent_encode(res_id)}/actions/modify-deploy-machines',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDeployMachineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_deploy_machine(
        self,
        res_id: str,
        request: main_models.ModifyDeployMachineRequest,
    ) -> main_models.ModifyDeployMachineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_deploy_machine_with_options(res_id, request, headers, runtime)

    async def modify_deploy_machine_async(
        self,
        res_id: str,
        request: main_models.ModifyDeployMachineRequest,
    ) -> main_models.ModifyDeployMachineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_deploy_machine_with_options_async(res_id, request, headers, runtime)

    def modify_elastictask_with_options(
        self,
        instance_id: str,
        request: main_models.ModifyElastictaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyElastictaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'ModifyElastictask',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/elastic-task',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyElastictaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_elastictask_with_options_async(
        self,
        instance_id: str,
        request: main_models.ModifyElastictaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyElastictaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'ModifyElastictask',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/elastic-task',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyElastictaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_elastictask(
        self,
        instance_id: str,
        request: main_models.ModifyElastictaskRequest,
    ) -> main_models.ModifyElastictaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_elastictask_with_options(instance_id, request, headers, runtime)

    async def modify_elastictask_async(
        self,
        instance_id: str,
        request: main_models.ModifyElastictaskRequest,
    ) -> main_models.ModifyElastictaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_elastictask_with_options_async(instance_id, request, headers, runtime)

    def modify_instance_maintain_time_with_options(
        self,
        instance_id: str,
        request: main_models.ModifyInstanceMaintainTimeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceMaintainTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceMaintainTime',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/modify-maintaintime',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_maintain_time_with_options_async(
        self,
        instance_id: str,
        request: main_models.ModifyInstanceMaintainTimeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceMaintainTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceMaintainTime',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/modify-maintaintime',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceMaintainTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_maintain_time(
        self,
        instance_id: str,
        request: main_models.ModifyInstanceMaintainTimeRequest,
    ) -> main_models.ModifyInstanceMaintainTimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_instance_maintain_time_with_options(instance_id, request, headers, runtime)

    async def modify_instance_maintain_time_async(
        self,
        instance_id: str,
        request: main_models.ModifyInstanceMaintainTimeRequest,
    ) -> main_models.ModifyInstanceMaintainTimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_instance_maintain_time_with_options_async(instance_id, request, headers, runtime)

    def modify_white_ips_with_options(
        self,
        instance_id: str,
        request: main_models.ModifyWhiteIpsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWhiteIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.modify_mode):
            body['modifyMode'] = request.modify_mode
        if not DaraCore.is_null(request.network_type):
            body['networkType'] = request.network_type
        if not DaraCore.is_null(request.node_type):
            body['nodeType'] = request.node_type
        if not DaraCore.is_null(request.white_ip_group):
            body['whiteIpGroup'] = request.white_ip_group
        if not DaraCore.is_null(request.white_ip_list):
            body['whiteIpList'] = request.white_ip_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWhiteIps',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/modify-white-ips',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWhiteIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_white_ips_with_options_async(
        self,
        instance_id: str,
        request: main_models.ModifyWhiteIpsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyWhiteIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.modify_mode):
            body['modifyMode'] = request.modify_mode
        if not DaraCore.is_null(request.network_type):
            body['networkType'] = request.network_type
        if not DaraCore.is_null(request.node_type):
            body['nodeType'] = request.node_type
        if not DaraCore.is_null(request.white_ip_group):
            body['whiteIpGroup'] = request.white_ip_group
        if not DaraCore.is_null(request.white_ip_list):
            body['whiteIpList'] = request.white_ip_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyWhiteIps',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/modify-white-ips',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyWhiteIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_white_ips(
        self,
        instance_id: str,
        request: main_models.ModifyWhiteIpsRequest,
    ) -> main_models.ModifyWhiteIpsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_white_ips_with_options(instance_id, request, headers, runtime)

    async def modify_white_ips_async(
        self,
        instance_id: str,
        request: main_models.ModifyWhiteIpsRequest,
    ) -> main_models.ModifyWhiteIpsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_white_ips_with_options_async(instance_id, request, headers, runtime)

    def move_resource_group_with_options(
        self,
        instance_id: str,
        request: main_models.MoveResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/resourcegroup',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        instance_id: str,
        request: main_models.MoveResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/resourcegroup',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource_group(
        self,
        instance_id: str,
        request: main_models.MoveResourceGroupRequest,
    ) -> main_models.MoveResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.move_resource_group_with_options(instance_id, request, headers, runtime)

    async def move_resource_group_async(
        self,
        instance_id: str,
        request: main_models.MoveResourceGroupRequest,
    ) -> main_models.MoveResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.move_resource_group_with_options_async(instance_id, request, headers, runtime)

    def open_diagnosis_with_options(
        self,
        instance_id: str,
        request: main_models.OpenDiagnosisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OpenDiagnosisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenDiagnosis',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/diagnosis/instances/{DaraURL.percent_encode(instance_id)}/actions/open-diagnosis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_diagnosis_with_options_async(
        self,
        instance_id: str,
        request: main_models.OpenDiagnosisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OpenDiagnosisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenDiagnosis',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/diagnosis/instances/{DaraURL.percent_encode(instance_id)}/actions/open-diagnosis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_diagnosis(
        self,
        instance_id: str,
        request: main_models.OpenDiagnosisRequest,
    ) -> main_models.OpenDiagnosisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.open_diagnosis_with_options(instance_id, request, headers, runtime)

    async def open_diagnosis_async(
        self,
        instance_id: str,
        request: main_models.OpenDiagnosisRequest,
    ) -> main_models.OpenDiagnosisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.open_diagnosis_with_options_async(instance_id, request, headers, runtime)

    def open_https_with_options(
        self,
        instance_id: str,
        request: main_models.OpenHttpsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OpenHttpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenHttps',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/open-https',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenHttpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_https_with_options_async(
        self,
        instance_id: str,
        request: main_models.OpenHttpsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OpenHttpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenHttps',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/open-https',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenHttpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_https(
        self,
        instance_id: str,
        request: main_models.OpenHttpsRequest,
    ) -> main_models.OpenHttpsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.open_https_with_options(instance_id, request, headers, runtime)

    async def open_https_async(
        self,
        instance_id: str,
        request: main_models.OpenHttpsRequest,
    ) -> main_models.OpenHttpsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.open_https_with_options_async(instance_id, request, headers, runtime)

    def post_emon_try_alarm_rule_with_options(
        self,
        project_id: str,
        alarm_group_id: str,
        request: main_models.PostEmonTryAlarmRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PostEmonTryAlarmRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.body):
            query['body'] = request.body
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PostEmonTryAlarmRule',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/emon/projects/{DaraURL.percent_encode(project_id)}/alarm-groups/{DaraURL.percent_encode(alarm_group_id)}/alarm-rules/_test',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PostEmonTryAlarmRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def post_emon_try_alarm_rule_with_options_async(
        self,
        project_id: str,
        alarm_group_id: str,
        request: main_models.PostEmonTryAlarmRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PostEmonTryAlarmRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.body):
            query['body'] = request.body
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PostEmonTryAlarmRule',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/emon/projects/{DaraURL.percent_encode(project_id)}/alarm-groups/{DaraURL.percent_encode(alarm_group_id)}/alarm-rules/_test',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PostEmonTryAlarmRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def post_emon_try_alarm_rule(
        self,
        project_id: str,
        alarm_group_id: str,
        request: main_models.PostEmonTryAlarmRuleRequest,
    ) -> main_models.PostEmonTryAlarmRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.post_emon_try_alarm_rule_with_options(project_id, alarm_group_id, request, headers, runtime)

    async def post_emon_try_alarm_rule_async(
        self,
        project_id: str,
        alarm_group_id: str,
        request: main_models.PostEmonTryAlarmRuleRequest,
    ) -> main_models.PostEmonTryAlarmRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.post_emon_try_alarm_rule_with_options_async(project_id, alarm_group_id, request, headers, runtime)

    def recommend_templates_with_options(
        self,
        instance_id: str,
        request: main_models.RecommendTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RecommendTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.usage_scenario):
            query['usageScenario'] = request.usage_scenario
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecommendTemplates',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/recommended-templates',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecommendTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def recommend_templates_with_options_async(
        self,
        instance_id: str,
        request: main_models.RecommendTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RecommendTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.usage_scenario):
            query['usageScenario'] = request.usage_scenario
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecommendTemplates',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/recommended-templates',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecommendTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recommend_templates(
        self,
        instance_id: str,
        request: main_models.RecommendTemplatesRequest,
    ) -> main_models.RecommendTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.recommend_templates_with_options(instance_id, request, headers, runtime)

    async def recommend_templates_async(
        self,
        instance_id: str,
        request: main_models.RecommendTemplatesRequest,
    ) -> main_models.RecommendTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.recommend_templates_with_options_async(instance_id, request, headers, runtime)

    def reinstall_collector_with_options(
        self,
        res_id: str,
        request: main_models.ReinstallCollectorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReinstallCollectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'ReinstallCollector',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/collectors/{DaraURL.percent_encode(res_id)}/actions/reinstall',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReinstallCollectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def reinstall_collector_with_options_async(
        self,
        res_id: str,
        request: main_models.ReinstallCollectorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReinstallCollectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'ReinstallCollector',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/collectors/{DaraURL.percent_encode(res_id)}/actions/reinstall',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReinstallCollectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reinstall_collector(
        self,
        res_id: str,
        request: main_models.ReinstallCollectorRequest,
    ) -> main_models.ReinstallCollectorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.reinstall_collector_with_options(res_id, request, headers, runtime)

    async def reinstall_collector_async(
        self,
        res_id: str,
        request: main_models.ReinstallCollectorRequest,
    ) -> main_models.ReinstallCollectorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.reinstall_collector_with_options_async(res_id, request, headers, runtime)

    def renew_instance_with_options(
        self,
        instance_id: str,
        request: main_models.RenewInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RenewInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'RenewInstance',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/renew',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        instance_id: str,
        request: main_models.RenewInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RenewInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'RenewInstance',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/renew',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_instance(
        self,
        instance_id: str,
        request: main_models.RenewInstanceRequest,
    ) -> main_models.RenewInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.renew_instance_with_options(instance_id, request, headers, runtime)

    async def renew_instance_async(
        self,
        instance_id: str,
        request: main_models.RenewInstanceRequest,
    ) -> main_models.RenewInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.renew_instance_with_options_async(instance_id, request, headers, runtime)

    def renew_logstash_with_options(
        self,
        instance_id: str,
        request: main_models.RenewLogstashRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RenewLogstashResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'RenewLogstash',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/actions/renew',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewLogstashResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_logstash_with_options_async(
        self,
        instance_id: str,
        request: main_models.RenewLogstashRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RenewLogstashResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'RenewLogstash',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/actions/renew',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewLogstashResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_logstash(
        self,
        instance_id: str,
        request: main_models.RenewLogstashRequest,
    ) -> main_models.RenewLogstashResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.renew_logstash_with_options(instance_id, request, headers, runtime)

    async def renew_logstash_async(
        self,
        instance_id: str,
        request: main_models.RenewLogstashRequest,
    ) -> main_models.RenewLogstashResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.renew_logstash_with_options_async(instance_id, request, headers, runtime)

    def restart_collector_with_options(
        self,
        res_id: str,
        request: main_models.RestartCollectorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartCollectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartCollector',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/collectors/{DaraURL.percent_encode(res_id)}/actions/restart',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartCollectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_collector_with_options_async(
        self,
        res_id: str,
        request: main_models.RestartCollectorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartCollectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartCollector',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/collectors/{DaraURL.percent_encode(res_id)}/actions/restart',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartCollectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_collector(
        self,
        res_id: str,
        request: main_models.RestartCollectorRequest,
    ) -> main_models.RestartCollectorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.restart_collector_with_options(res_id, request, headers, runtime)

    async def restart_collector_async(
        self,
        res_id: str,
        request: main_models.RestartCollectorRequest,
    ) -> main_models.RestartCollectorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.restart_collector_with_options_async(res_id, request, headers, runtime)

    def restart_instance_with_options(
        self,
        instance_id: str,
        request: main_models.RestartInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.force):
            query['force'] = request.force
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'RestartInstance',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/restart',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_instance_with_options_async(
        self,
        instance_id: str,
        request: main_models.RestartInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.force):
            query['force'] = request.force
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'RestartInstance',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/restart',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_instance(
        self,
        instance_id: str,
        request: main_models.RestartInstanceRequest,
    ) -> main_models.RestartInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.restart_instance_with_options(instance_id, request, headers, runtime)

    async def restart_instance_async(
        self,
        instance_id: str,
        request: main_models.RestartInstanceRequest,
    ) -> main_models.RestartInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.restart_instance_with_options_async(instance_id, request, headers, runtime)

    def restart_logstash_with_options(
        self,
        instance_id: str,
        request: main_models.RestartLogstashRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartLogstashResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.force):
            query['force'] = request.force
        body = {}
        if not DaraCore.is_null(request.batch_count):
            body['batchCount'] = request.batch_count
        if not DaraCore.is_null(request.blue_green_dep):
            body['blueGreenDep'] = request.blue_green_dep
        if not DaraCore.is_null(request.node_types):
            body['nodeTypes'] = request.node_types
        if not DaraCore.is_null(request.nodes):
            body['nodes'] = request.nodes
        if not DaraCore.is_null(request.restart_type):
            body['restartType'] = request.restart_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RestartLogstash',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/actions/restart',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartLogstashResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_logstash_with_options_async(
        self,
        instance_id: str,
        request: main_models.RestartLogstashRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartLogstashResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.force):
            query['force'] = request.force
        body = {}
        if not DaraCore.is_null(request.batch_count):
            body['batchCount'] = request.batch_count
        if not DaraCore.is_null(request.blue_green_dep):
            body['blueGreenDep'] = request.blue_green_dep
        if not DaraCore.is_null(request.node_types):
            body['nodeTypes'] = request.node_types
        if not DaraCore.is_null(request.nodes):
            body['nodes'] = request.nodes
        if not DaraCore.is_null(request.restart_type):
            body['restartType'] = request.restart_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RestartLogstash',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/actions/restart',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartLogstashResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_logstash(
        self,
        instance_id: str,
        request: main_models.RestartLogstashRequest,
    ) -> main_models.RestartLogstashResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.restart_logstash_with_options(instance_id, request, headers, runtime)

    async def restart_logstash_async(
        self,
        instance_id: str,
        request: main_models.RestartLogstashRequest,
    ) -> main_models.RestartLogstashResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.restart_logstash_with_options_async(instance_id, request, headers, runtime)

    def resume_elasticsearch_task_with_options(
        self,
        instance_id: str,
        request: main_models.ResumeElasticsearchTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResumeElasticsearchTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeElasticsearchTask',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/resume',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeElasticsearchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_elasticsearch_task_with_options_async(
        self,
        instance_id: str,
        request: main_models.ResumeElasticsearchTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResumeElasticsearchTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeElasticsearchTask',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/resume',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeElasticsearchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_elasticsearch_task(
        self,
        instance_id: str,
        request: main_models.ResumeElasticsearchTaskRequest,
    ) -> main_models.ResumeElasticsearchTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.resume_elasticsearch_task_with_options(instance_id, request, headers, runtime)

    async def resume_elasticsearch_task_async(
        self,
        instance_id: str,
        request: main_models.ResumeElasticsearchTaskRequest,
    ) -> main_models.ResumeElasticsearchTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.resume_elasticsearch_task_with_options_async(instance_id, request, headers, runtime)

    def resume_logstash_task_with_options(
        self,
        instance_id: str,
        request: main_models.ResumeLogstashTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResumeLogstashTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeLogstashTask',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/actions/resume',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeLogstashTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_logstash_task_with_options_async(
        self,
        instance_id: str,
        request: main_models.ResumeLogstashTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResumeLogstashTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeLogstashTask',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/actions/resume',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeLogstashTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_logstash_task(
        self,
        instance_id: str,
        request: main_models.ResumeLogstashTaskRequest,
    ) -> main_models.ResumeLogstashTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.resume_logstash_task_with_options(instance_id, request, headers, runtime)

    async def resume_logstash_task_async(
        self,
        instance_id: str,
        request: main_models.ResumeLogstashTaskRequest,
    ) -> main_models.ResumeLogstashTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.resume_logstash_task_with_options_async(instance_id, request, headers, runtime)

    def rollover_data_stream_with_options(
        self,
        instance_id: str,
        data_stream: str,
        request: main_models.RolloverDataStreamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RolloverDataStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RolloverDataStream',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/data-streams/{DaraURL.percent_encode(data_stream)}/rollover',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RolloverDataStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollover_data_stream_with_options_async(
        self,
        instance_id: str,
        data_stream: str,
        request: main_models.RolloverDataStreamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RolloverDataStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RolloverDataStream',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/data-streams/{DaraURL.percent_encode(data_stream)}/rollover',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RolloverDataStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollover_data_stream(
        self,
        instance_id: str,
        data_stream: str,
        request: main_models.RolloverDataStreamRequest,
    ) -> main_models.RolloverDataStreamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.rollover_data_stream_with_options(instance_id, data_stream, request, headers, runtime)

    async def rollover_data_stream_async(
        self,
        instance_id: str,
        data_stream: str,
        request: main_models.RolloverDataStreamRequest,
    ) -> main_models.RolloverDataStreamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.rollover_data_stream_with_options_async(instance_id, data_stream, request, headers, runtime)

    def run_pipelines_with_options(
        self,
        instance_id: str,
        request: main_models.RunPipelinesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunPipelinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'RunPipelines',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/pipelines/action/run',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunPipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_pipelines_with_options_async(
        self,
        instance_id: str,
        request: main_models.RunPipelinesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunPipelinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'RunPipelines',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/pipelines/action/run',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunPipelinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_pipelines(
        self,
        instance_id: str,
        request: main_models.RunPipelinesRequest,
    ) -> main_models.RunPipelinesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_pipelines_with_options(instance_id, request, headers, runtime)

    async def run_pipelines_async(
        self,
        instance_id: str,
        request: main_models.RunPipelinesRequest,
    ) -> main_models.RunPipelinesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_pipelines_with_options_async(instance_id, request, headers, runtime)

    def shrink_node_with_options(
        self,
        instance_id: str,
        request: main_models.ShrinkNodeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ShrinkNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.count):
            query['count'] = request.count
        if not DaraCore.is_null(request.ignore_status):
            query['ignoreStatus'] = request.ignore_status
        if not DaraCore.is_null(request.node_type):
            query['nodeType'] = request.node_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ShrinkNode',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/shrink',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ShrinkNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def shrink_node_with_options_async(
        self,
        instance_id: str,
        request: main_models.ShrinkNodeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ShrinkNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.count):
            query['count'] = request.count
        if not DaraCore.is_null(request.ignore_status):
            query['ignoreStatus'] = request.ignore_status
        if not DaraCore.is_null(request.node_type):
            query['nodeType'] = request.node_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ShrinkNode',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/shrink',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ShrinkNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def shrink_node(
        self,
        instance_id: str,
        request: main_models.ShrinkNodeRequest,
    ) -> main_models.ShrinkNodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.shrink_node_with_options(instance_id, request, headers, runtime)

    async def shrink_node_async(
        self,
        instance_id: str,
        request: main_models.ShrinkNodeRequest,
    ) -> main_models.ShrinkNodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.shrink_node_with_options_async(instance_id, request, headers, runtime)

    def start_collector_with_options(
        self,
        res_id: str,
        request: main_models.StartCollectorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartCollectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartCollector',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/collectors/{DaraURL.percent_encode(res_id)}/actions/start',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartCollectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_collector_with_options_async(
        self,
        res_id: str,
        request: main_models.StartCollectorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartCollectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartCollector',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/collectors/{DaraURL.percent_encode(res_id)}/actions/start',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartCollectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_collector(
        self,
        res_id: str,
        request: main_models.StartCollectorRequest,
    ) -> main_models.StartCollectorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_collector_with_options(res_id, request, headers, runtime)

    async def start_collector_async(
        self,
        res_id: str,
        request: main_models.StartCollectorRequest,
    ) -> main_models.StartCollectorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_collector_with_options_async(res_id, request, headers, runtime)

    def stop_collector_with_options(
        self,
        res_id: str,
        request: main_models.StopCollectorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopCollectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopCollector',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/collectors/{DaraURL.percent_encode(res_id)}/actions/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopCollectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_collector_with_options_async(
        self,
        res_id: str,
        request: main_models.StopCollectorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopCollectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopCollector',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/collectors/{DaraURL.percent_encode(res_id)}/actions/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopCollectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_collector(
        self,
        res_id: str,
        request: main_models.StopCollectorRequest,
    ) -> main_models.StopCollectorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_collector_with_options(res_id, request, headers, runtime)

    async def stop_collector_async(
        self,
        res_id: str,
        request: main_models.StopCollectorRequest,
    ) -> main_models.StopCollectorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_collector_with_options_async(res_id, request, headers, runtime)

    def stop_pipelines_with_options(
        self,
        instance_id: str,
        request: main_models.StopPipelinesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopPipelinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'StopPipelines',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/pipelines/action/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopPipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_pipelines_with_options_async(
        self,
        instance_id: str,
        request: main_models.StopPipelinesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopPipelinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'StopPipelines',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/pipelines/action/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopPipelinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_pipelines(
        self,
        instance_id: str,
        request: main_models.StopPipelinesRequest,
    ) -> main_models.StopPipelinesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_pipelines_with_options(instance_id, request, headers, runtime)

    async def stop_pipelines_async(
        self,
        instance_id: str,
        request: main_models.StopPipelinesRequest,
    ) -> main_models.StopPipelinesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_pipelines_with_options_async(instance_id, request, headers, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.tag_resources_with_options_async(request, headers, runtime)

    def transfer_node_with_options(
        self,
        instance_id: str,
        request: main_models.TransferNodeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TransferNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.node_type):
            query['nodeType'] = request.node_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'TransferNode',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/transfer',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_node_with_options_async(
        self,
        instance_id: str,
        request: main_models.TransferNodeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TransferNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.node_type):
            query['nodeType'] = request.node_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'TransferNode',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/transfer',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_node(
        self,
        instance_id: str,
        request: main_models.TransferNodeRequest,
    ) -> main_models.TransferNodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.transfer_node_with_options(instance_id, request, headers, runtime)

    async def transfer_node_async(
        self,
        instance_id: str,
        request: main_models.TransferNodeRequest,
    ) -> main_models.TransferNodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.transfer_node_with_options_async(instance_id, request, headers, runtime)

    def trigger_network_with_options(
        self,
        instance_id: str,
        request: main_models.TriggerNetworkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TriggerNetworkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.action_type):
            body['actionType'] = request.action_type
        if not DaraCore.is_null(request.network_type):
            body['networkType'] = request.network_type
        if not DaraCore.is_null(request.node_type):
            body['nodeType'] = request.node_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TriggerNetwork',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/network-trigger',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TriggerNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_network_with_options_async(
        self,
        instance_id: str,
        request: main_models.TriggerNetworkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TriggerNetworkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.action_type):
            body['actionType'] = request.action_type
        if not DaraCore.is_null(request.network_type):
            body['networkType'] = request.network_type
        if not DaraCore.is_null(request.node_type):
            body['nodeType'] = request.node_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TriggerNetwork',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/network-trigger',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TriggerNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trigger_network(
        self,
        instance_id: str,
        request: main_models.TriggerNetworkRequest,
    ) -> main_models.TriggerNetworkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.trigger_network_with_options(instance_id, request, headers, runtime)

    async def trigger_network_async(
        self,
        instance_id: str,
        request: main_models.TriggerNetworkRequest,
    ) -> main_models.TriggerNetworkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.trigger_network_with_options_async(instance_id, request, headers, runtime)

    def turn_off_zone_with_options(
        self,
        instance_id: str,
        request: main_models.TurnOffZoneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TurnOffZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.zone):
            query['zone'] = request.zone
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TurnOffZone',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/turnOff-zone',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TurnOffZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def turn_off_zone_with_options_async(
        self,
        instance_id: str,
        request: main_models.TurnOffZoneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TurnOffZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.zone):
            query['zone'] = request.zone
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TurnOffZone',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/turnOff-zone',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TurnOffZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def turn_off_zone(
        self,
        instance_id: str,
        request: main_models.TurnOffZoneRequest,
    ) -> main_models.TurnOffZoneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.turn_off_zone_with_options(instance_id, request, headers, runtime)

    async def turn_off_zone_async(
        self,
        instance_id: str,
        request: main_models.TurnOffZoneRequest,
    ) -> main_models.TurnOffZoneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.turn_off_zone_with_options_async(instance_id, request, headers, runtime)

    def turn_on_zone_with_options(
        self,
        instance_id: str,
        request: main_models.TurnOnZoneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TurnOnZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.zone):
            query['zone'] = request.zone
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TurnOnZone',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/turnOn-zone',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TurnOnZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def turn_on_zone_with_options_async(
        self,
        instance_id: str,
        request: main_models.TurnOnZoneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TurnOnZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.zone):
            query['zone'] = request.zone
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TurnOnZone',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/turnOn-zone',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TurnOnZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def turn_on_zone(
        self,
        instance_id: str,
        request: main_models.TurnOnZoneRequest,
    ) -> main_models.TurnOnZoneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.turn_on_zone_with_options(instance_id, request, headers, runtime)

    async def turn_on_zone_async(
        self,
        instance_id: str,
        request: main_models.TurnOnZoneRequest,
    ) -> main_models.TurnOnZoneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.turn_on_zone_with_options_async(instance_id, request, headers, runtime)

    def uninstall_kibana_plugin_with_options(
        self,
        instance_id: str,
        request: main_models.UninstallKibanaPluginRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UninstallKibanaPluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UninstallKibanaPlugin',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/kibana-plugins/actions/uninstall',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallKibanaPluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_kibana_plugin_with_options_async(
        self,
        instance_id: str,
        request: main_models.UninstallKibanaPluginRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UninstallKibanaPluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UninstallKibanaPlugin',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/kibana-plugins/actions/uninstall',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallKibanaPluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_kibana_plugin(
        self,
        instance_id: str,
        request: main_models.UninstallKibanaPluginRequest,
    ) -> main_models.UninstallKibanaPluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.uninstall_kibana_plugin_with_options(instance_id, request, headers, runtime)

    async def uninstall_kibana_plugin_async(
        self,
        instance_id: str,
        request: main_models.UninstallKibanaPluginRequest,
    ) -> main_models.UninstallKibanaPluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.uninstall_kibana_plugin_with_options_async(instance_id, request, headers, runtime)

    def uninstall_logstash_plugin_with_options(
        self,
        instance_id: str,
        request: main_models.UninstallLogstashPluginRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UninstallLogstashPluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UninstallLogstashPlugin',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/plugins/actions/uninstall',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallLogstashPluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_logstash_plugin_with_options_async(
        self,
        instance_id: str,
        request: main_models.UninstallLogstashPluginRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UninstallLogstashPluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UninstallLogstashPlugin',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/plugins/actions/uninstall',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallLogstashPluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_logstash_plugin(
        self,
        instance_id: str,
        request: main_models.UninstallLogstashPluginRequest,
    ) -> main_models.UninstallLogstashPluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.uninstall_logstash_plugin_with_options(instance_id, request, headers, runtime)

    async def uninstall_logstash_plugin_async(
        self,
        instance_id: str,
        request: main_models.UninstallLogstashPluginRequest,
    ) -> main_models.UninstallLogstashPluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.uninstall_logstash_plugin_with_options_async(instance_id, request, headers, runtime)

    def uninstall_plugin_with_options(
        self,
        instance_id: str,
        request: main_models.UninstallPluginRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UninstallPluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.force):
            query['force'] = request.force
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UninstallPlugin',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/plugins/actions/uninstall',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallPluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_plugin_with_options_async(
        self,
        instance_id: str,
        request: main_models.UninstallPluginRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UninstallPluginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.force):
            query['force'] = request.force
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UninstallPlugin',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/plugins/actions/uninstall',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallPluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_plugin(
        self,
        instance_id: str,
        request: main_models.UninstallPluginRequest,
    ) -> main_models.UninstallPluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.uninstall_plugin_with_options(instance_id, request, headers, runtime)

    async def uninstall_plugin_async(
        self,
        instance_id: str,
        request: main_models.UninstallPluginRequest,
    ) -> main_models.UninstallPluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.uninstall_plugin_with_options_async(instance_id, request, headers, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        if not DaraCore.is_null(request.body):
            query['body'] = request.body
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/tags',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        if not DaraCore.is_null(request.body):
            query['body'] = request.body
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/tags',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.untag_resources_with_options_async(request, headers, runtime)

    def update_admin_password_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateAdminPasswordRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAdminPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.es_admin_password):
            body['esAdminPassword'] = request.es_admin_password
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAdminPassword',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/admin-pwd',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAdminPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_admin_password_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateAdminPasswordRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAdminPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.es_admin_password):
            body['esAdminPassword'] = request.es_admin_password
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAdminPassword',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/admin-pwd',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAdminPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_admin_password(
        self,
        instance_id: str,
        request: main_models.UpdateAdminPasswordRequest,
    ) -> main_models.UpdateAdminPasswordResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_admin_password_with_options(instance_id, request, headers, runtime)

    async def update_admin_password_async(
        self,
        instance_id: str,
        request: main_models.UpdateAdminPasswordRequest,
    ) -> main_models.UpdateAdminPasswordResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_admin_password_with_options_async(instance_id, request, headers, runtime)

    def update_advanced_setting_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateAdvancedSettingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAdvancedSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateAdvancedSetting',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/update-advanced-setting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAdvancedSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_advanced_setting_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateAdvancedSettingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAdvancedSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateAdvancedSetting',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/update-advanced-setting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAdvancedSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_advanced_setting(
        self,
        instance_id: str,
        request: main_models.UpdateAdvancedSettingRequest,
    ) -> main_models.UpdateAdvancedSettingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_advanced_setting_with_options(instance_id, request, headers, runtime)

    async def update_advanced_setting_async(
        self,
        instance_id: str,
        request: main_models.UpdateAdvancedSettingRequest,
    ) -> main_models.UpdateAdvancedSettingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_advanced_setting_with_options_async(instance_id, request, headers, runtime)

    def update_aliws_dict_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateAliwsDictRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAliwsDictResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateAliwsDict',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/aliws-dict',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAliwsDictResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_aliws_dict_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateAliwsDictRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAliwsDictResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateAliwsDict',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/aliws-dict',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAliwsDictResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_aliws_dict(
        self,
        instance_id: str,
        request: main_models.UpdateAliwsDictRequest,
    ) -> main_models.UpdateAliwsDictResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_aliws_dict_with_options(instance_id, request, headers, runtime)

    async def update_aliws_dict_async(
        self,
        instance_id: str,
        request: main_models.UpdateAliwsDictRequest,
    ) -> main_models.UpdateAliwsDictResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_aliws_dict_with_options_async(instance_id, request, headers, runtime)

    def update_black_ips_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateBlackIpsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBlackIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBlackIps',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/black-ips',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBlackIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_black_ips_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateBlackIpsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBlackIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBlackIps',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/black-ips',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBlackIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_black_ips(
        self,
        instance_id: str,
        request: main_models.UpdateBlackIpsRequest,
    ) -> main_models.UpdateBlackIpsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_black_ips_with_options(instance_id, request, headers, runtime)

    async def update_black_ips_async(
        self,
        instance_id: str,
        request: main_models.UpdateBlackIpsRequest,
    ) -> main_models.UpdateBlackIpsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_black_ips_with_options_async(instance_id, request, headers, runtime)

    def update_collector_with_options(
        self,
        res_id: str,
        request: main_models.UpdateCollectorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCollectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateCollector',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/collectors/{DaraURL.percent_encode(res_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCollectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_collector_with_options_async(
        self,
        res_id: str,
        request: main_models.UpdateCollectorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCollectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateCollector',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/collectors/{DaraURL.percent_encode(res_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCollectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_collector(
        self,
        res_id: str,
        request: main_models.UpdateCollectorRequest,
    ) -> main_models.UpdateCollectorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_collector_with_options(res_id, request, headers, runtime)

    async def update_collector_async(
        self,
        res_id: str,
        request: main_models.UpdateCollectorRequest,
    ) -> main_models.UpdateCollectorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_collector_with_options_async(res_id, request, headers, runtime)

    def update_collector_name_with_options(
        self,
        res_id: str,
        request: main_models.UpdateCollectorNameRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCollectorNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateCollectorName',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/collectors/{DaraURL.percent_encode(res_id)}/actions/rename',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCollectorNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_collector_name_with_options_async(
        self,
        res_id: str,
        request: main_models.UpdateCollectorNameRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCollectorNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateCollectorName',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/collectors/{DaraURL.percent_encode(res_id)}/actions/rename',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCollectorNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_collector_name(
        self,
        res_id: str,
        request: main_models.UpdateCollectorNameRequest,
    ) -> main_models.UpdateCollectorNameResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_collector_name_with_options(res_id, request, headers, runtime)

    async def update_collector_name_async(
        self,
        res_id: str,
        request: main_models.UpdateCollectorNameRequest,
    ) -> main_models.UpdateCollectorNameResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_collector_name_with_options_async(res_id, request, headers, runtime)

    def update_component_index_with_options(
        self,
        instance_id: str,
        name: str,
        request: main_models.UpdateComponentIndexRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComponentIndexResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.meta):
            body['_meta'] = request.meta
        if not DaraCore.is_null(request.template):
            body['template'] = request.template
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComponentIndex',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/component-index/{DaraURL.percent_encode(name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComponentIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_component_index_with_options_async(
        self,
        instance_id: str,
        name: str,
        request: main_models.UpdateComponentIndexRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComponentIndexResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.meta):
            body['_meta'] = request.meta
        if not DaraCore.is_null(request.template):
            body['template'] = request.template
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComponentIndex',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/component-index/{DaraURL.percent_encode(name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComponentIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_component_index(
        self,
        instance_id: str,
        name: str,
        request: main_models.UpdateComponentIndexRequest,
    ) -> main_models.UpdateComponentIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_component_index_with_options(instance_id, name, request, headers, runtime)

    async def update_component_index_async(
        self,
        instance_id: str,
        name: str,
        request: main_models.UpdateComponentIndexRequest,
    ) -> main_models.UpdateComponentIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_component_index_with_options_async(instance_id, name, request, headers, runtime)

    def update_description_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateDescriptionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDescription',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/description',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_description_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateDescriptionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDescription',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/description',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_description(
        self,
        instance_id: str,
        request: main_models.UpdateDescriptionRequest,
    ) -> main_models.UpdateDescriptionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_description_with_options(instance_id, request, headers, runtime)

    async def update_description_async(
        self,
        instance_id: str,
        request: main_models.UpdateDescriptionRequest,
    ) -> main_models.UpdateDescriptionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_description_with_options_async(instance_id, request, headers, runtime)

    def update_diagnosis_settings_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateDiagnosisSettingsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDiagnosisSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateDiagnosisSettings',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/diagnosis/instances/{DaraURL.percent_encode(instance_id)}/settings',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDiagnosisSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_diagnosis_settings_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateDiagnosisSettingsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDiagnosisSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateDiagnosisSettings',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/diagnosis/instances/{DaraURL.percent_encode(instance_id)}/settings',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDiagnosisSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_diagnosis_settings(
        self,
        instance_id: str,
        request: main_models.UpdateDiagnosisSettingsRequest,
    ) -> main_models.UpdateDiagnosisSettingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_diagnosis_settings_with_options(instance_id, request, headers, runtime)

    async def update_diagnosis_settings_async(
        self,
        instance_id: str,
        request: main_models.UpdateDiagnosisSettingsRequest,
    ) -> main_models.UpdateDiagnosisSettingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_diagnosis_settings_with_options_async(instance_id, request, headers, runtime)

    def update_dict_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateDictRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDictResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateDict',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/dict',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDictResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dict_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateDictRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDictResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateDict',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/dict',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDictResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dict(
        self,
        instance_id: str,
        request: main_models.UpdateDictRequest,
    ) -> main_models.UpdateDictResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_dict_with_options(instance_id, request, headers, runtime)

    async def update_dict_async(
        self,
        instance_id: str,
        request: main_models.UpdateDictRequest,
    ) -> main_models.UpdateDictResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_dict_with_options_async(instance_id, request, headers, runtime)

    def update_dynamic_settings_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateDynamicSettingsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDynamicSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.mode):
            query['mode'] = request.mode
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateDynamicSettings',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/dynamic-settings',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDynamicSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dynamic_settings_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateDynamicSettingsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDynamicSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.mode):
            query['mode'] = request.mode
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateDynamicSettings',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/dynamic-settings',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDynamicSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dynamic_settings(
        self,
        instance_id: str,
        request: main_models.UpdateDynamicSettingsRequest,
    ) -> main_models.UpdateDynamicSettingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_dynamic_settings_with_options(instance_id, request, headers, runtime)

    async def update_dynamic_settings_async(
        self,
        instance_id: str,
        request: main_models.UpdateDynamicSettingsRequest,
    ) -> main_models.UpdateDynamicSettingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_dynamic_settings_with_options_async(instance_id, request, headers, runtime)

    def update_extend_config_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateExtendConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExtendConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateExtendConfig',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/extend-configs/actions/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExtendConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_extend_config_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateExtendConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExtendConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateExtendConfig',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/extend-configs/actions/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExtendConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_extend_config(
        self,
        instance_id: str,
        request: main_models.UpdateExtendConfigRequest,
    ) -> main_models.UpdateExtendConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_extend_config_with_options(instance_id, request, headers, runtime)

    async def update_extend_config_async(
        self,
        instance_id: str,
        request: main_models.UpdateExtendConfigRequest,
    ) -> main_models.UpdateExtendConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_extend_config_with_options_async(instance_id, request, headers, runtime)

    def update_extendfiles_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateExtendfilesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExtendfilesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateExtendfiles',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/extendfiles',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExtendfilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_extendfiles_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateExtendfilesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExtendfilesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateExtendfiles',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/extendfiles',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExtendfilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_extendfiles(
        self,
        instance_id: str,
        request: main_models.UpdateExtendfilesRequest,
    ) -> main_models.UpdateExtendfilesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_extendfiles_with_options(instance_id, request, headers, runtime)

    async def update_extendfiles_async(
        self,
        instance_id: str,
        request: main_models.UpdateExtendfilesRequest,
    ) -> main_models.UpdateExtendfilesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_extendfiles_with_options_async(instance_id, request, headers, runtime)

    def update_hot_ik_dicts_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateHotIkDictsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHotIkDictsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateHotIkDicts',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/ik-hot-dict',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHotIkDictsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_hot_ik_dicts_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateHotIkDictsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHotIkDictsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateHotIkDicts',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/ik-hot-dict',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHotIkDictsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_hot_ik_dicts(
        self,
        instance_id: str,
        request: main_models.UpdateHotIkDictsRequest,
    ) -> main_models.UpdateHotIkDictsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_hot_ik_dicts_with_options(instance_id, request, headers, runtime)

    async def update_hot_ik_dicts_async(
        self,
        instance_id: str,
        request: main_models.UpdateHotIkDictsRequest,
    ) -> main_models.UpdateHotIkDictsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_hot_ik_dicts_with_options_async(instance_id, request, headers, runtime)

    def update_ilmpolicy_with_options(
        self,
        instance_id: str,
        policy_name: str,
        request: main_models.UpdateILMPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateILMPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateILMPolicy',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/ilm-policies/{DaraURL.percent_encode(policy_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateILMPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ilmpolicy_with_options_async(
        self,
        instance_id: str,
        policy_name: str,
        request: main_models.UpdateILMPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateILMPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateILMPolicy',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/ilm-policies/{DaraURL.percent_encode(policy_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateILMPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ilmpolicy(
        self,
        instance_id: str,
        policy_name: str,
        request: main_models.UpdateILMPolicyRequest,
    ) -> main_models.UpdateILMPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_ilmpolicy_with_options(instance_id, policy_name, request, headers, runtime)

    async def update_ilmpolicy_async(
        self,
        instance_id: str,
        policy_name: str,
        request: main_models.UpdateILMPolicyRequest,
    ) -> main_models.UpdateILMPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_ilmpolicy_with_options_async(instance_id, policy_name, request, headers, runtime)

    def update_index_template_with_options(
        self,
        instance_id: str,
        index_template: str,
        request: main_models.UpdateIndexTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIndexTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateIndexTemplate',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/index-templates/{DaraURL.percent_encode(index_template)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIndexTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_index_template_with_options_async(
        self,
        instance_id: str,
        index_template: str,
        request: main_models.UpdateIndexTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIndexTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateIndexTemplate',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/index-templates/{DaraURL.percent_encode(index_template)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIndexTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_index_template(
        self,
        instance_id: str,
        index_template: str,
        request: main_models.UpdateIndexTemplateRequest,
    ) -> main_models.UpdateIndexTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_index_template_with_options(instance_id, index_template, request, headers, runtime)

    async def update_index_template_async(
        self,
        instance_id: str,
        index_template: str,
        request: main_models.UpdateIndexTemplateRequest,
    ) -> main_models.UpdateIndexTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_index_template_with_options_async(instance_id, index_template, request, headers, runtime)

    def update_instance_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.force):
            query['force'] = request.force
        if not DaraCore.is_null(request.order_action_type):
            query['orderActionType'] = request.order_action_type
        body = {}
        if not DaraCore.is_null(request.client_node_configuration):
            body['clientNodeConfiguration'] = request.client_node_configuration
        if not DaraCore.is_null(request.elastic_data_node_configuration):
            body['elasticDataNodeConfiguration'] = request.elastic_data_node_configuration
        if not DaraCore.is_null(request.instance_category):
            body['instanceCategory'] = request.instance_category
        if not DaraCore.is_null(request.kibana_configuration):
            body['kibanaConfiguration'] = request.kibana_configuration
        if not DaraCore.is_null(request.master_configuration):
            body['masterConfiguration'] = request.master_configuration
        if not DaraCore.is_null(request.node_amount):
            body['nodeAmount'] = request.node_amount
        if not DaraCore.is_null(request.node_spec):
            body['nodeSpec'] = request.node_spec
        if not DaraCore.is_null(request.update_type):
            body['updateType'] = request.update_type
        if not DaraCore.is_null(request.warm_node_configuration):
            body['warmNodeConfiguration'] = request.warm_node_configuration
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstance',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.force):
            query['force'] = request.force
        if not DaraCore.is_null(request.order_action_type):
            query['orderActionType'] = request.order_action_type
        body = {}
        if not DaraCore.is_null(request.client_node_configuration):
            body['clientNodeConfiguration'] = request.client_node_configuration
        if not DaraCore.is_null(request.elastic_data_node_configuration):
            body['elasticDataNodeConfiguration'] = request.elastic_data_node_configuration
        if not DaraCore.is_null(request.instance_category):
            body['instanceCategory'] = request.instance_category
        if not DaraCore.is_null(request.kibana_configuration):
            body['kibanaConfiguration'] = request.kibana_configuration
        if not DaraCore.is_null(request.master_configuration):
            body['masterConfiguration'] = request.master_configuration
        if not DaraCore.is_null(request.node_amount):
            body['nodeAmount'] = request.node_amount
        if not DaraCore.is_null(request.node_spec):
            body['nodeSpec'] = request.node_spec
        if not DaraCore.is_null(request.update_type):
            body['updateType'] = request.update_type
        if not DaraCore.is_null(request.warm_node_configuration):
            body['warmNodeConfiguration'] = request.warm_node_configuration
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstance',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceRequest,
    ) -> main_models.UpdateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_instance_with_options(instance_id, request, headers, runtime)

    async def update_instance_async(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceRequest,
    ) -> main_models.UpdateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_instance_with_options_async(instance_id, request, headers, runtime)

    def update_instance_charge_type_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceChargeTypeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceChargeTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.payment_info):
            body['paymentInfo'] = request.payment_info
        if not DaraCore.is_null(request.payment_type):
            body['paymentType'] = request.payment_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceChargeType',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/convert-pay-type',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_charge_type_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceChargeTypeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceChargeTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.payment_info):
            body['paymentInfo'] = request.payment_info
        if not DaraCore.is_null(request.payment_type):
            body['paymentType'] = request.payment_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceChargeType',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/convert-pay-type',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceChargeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_charge_type(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceChargeTypeRequest,
    ) -> main_models.UpdateInstanceChargeTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_instance_charge_type_with_options(instance_id, request, headers, runtime)

    async def update_instance_charge_type_async(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceChargeTypeRequest,
    ) -> main_models.UpdateInstanceChargeTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_instance_charge_type_with_options_async(instance_id, request, headers, runtime)

    def update_instance_settings_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceSettingsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.force):
            query['force'] = request.force
        if not DaraCore.is_null(request.update_strategy):
            query['updateStrategy'] = request.update_strategy
        body = {}
        if not DaraCore.is_null(request.es_config):
            body['esConfig'] = request.es_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceSettings',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/instance-settings',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_settings_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceSettingsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.force):
            query['force'] = request.force
        if not DaraCore.is_null(request.update_strategy):
            query['updateStrategy'] = request.update_strategy
        body = {}
        if not DaraCore.is_null(request.es_config):
            body['esConfig'] = request.es_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceSettings',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/instance-settings',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_settings(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceSettingsRequest,
    ) -> main_models.UpdateInstanceSettingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_instance_settings_with_options(instance_id, request, headers, runtime)

    async def update_instance_settings_async(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceSettingsRequest,
    ) -> main_models.UpdateInstanceSettingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_instance_settings_with_options_async(instance_id, request, headers, runtime)

    def update_kibana_pvl_network_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateKibanaPvlNetworkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKibanaPvlNetworkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.pvl_id):
            query['pvlId'] = request.pvl_id
        body = {}
        if not DaraCore.is_null(request.endpoint_name):
            body['endpointName'] = request.endpoint_name
        if not DaraCore.is_null(request.security_groups):
            body['securityGroups'] = request.security_groups
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKibanaPvlNetwork',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/update-kibana-private',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKibanaPvlNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_kibana_pvl_network_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateKibanaPvlNetworkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKibanaPvlNetworkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.pvl_id):
            query['pvlId'] = request.pvl_id
        body = {}
        if not DaraCore.is_null(request.endpoint_name):
            body['endpointName'] = request.endpoint_name
        if not DaraCore.is_null(request.security_groups):
            body['securityGroups'] = request.security_groups
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKibanaPvlNetwork',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/update-kibana-private',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKibanaPvlNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_kibana_pvl_network(
        self,
        instance_id: str,
        request: main_models.UpdateKibanaPvlNetworkRequest,
    ) -> main_models.UpdateKibanaPvlNetworkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_kibana_pvl_network_with_options(instance_id, request, headers, runtime)

    async def update_kibana_pvl_network_async(
        self,
        instance_id: str,
        request: main_models.UpdateKibanaPvlNetworkRequest,
    ) -> main_models.UpdateKibanaPvlNetworkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_kibana_pvl_network_with_options_async(instance_id, request, headers, runtime)

    def update_kibana_settings_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateKibanaSettingsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKibanaSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateKibanaSettings',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/update-kibana-settings',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKibanaSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_kibana_settings_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateKibanaSettingsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKibanaSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateKibanaSettings',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/update-kibana-settings',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKibanaSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_kibana_settings(
        self,
        instance_id: str,
        request: main_models.UpdateKibanaSettingsRequest,
    ) -> main_models.UpdateKibanaSettingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_kibana_settings_with_options(instance_id, request, headers, runtime)

    async def update_kibana_settings_async(
        self,
        instance_id: str,
        request: main_models.UpdateKibanaSettingsRequest,
    ) -> main_models.UpdateKibanaSettingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_kibana_settings_with_options_async(instance_id, request, headers, runtime)

    def update_kibana_white_ips_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateKibanaWhiteIpsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKibanaWhiteIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.modify_mode):
            query['modifyMode'] = request.modify_mode
        body = {}
        if not DaraCore.is_null(request.kibana_ipwhitelist):
            body['kibanaIPWhitelist'] = request.kibana_ipwhitelist
        if not DaraCore.is_null(request.white_ip_group):
            body['whiteIpGroup'] = request.white_ip_group
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKibanaWhiteIps',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/kibana-white-ips',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKibanaWhiteIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_kibana_white_ips_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateKibanaWhiteIpsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKibanaWhiteIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.modify_mode):
            query['modifyMode'] = request.modify_mode
        body = {}
        if not DaraCore.is_null(request.kibana_ipwhitelist):
            body['kibanaIPWhitelist'] = request.kibana_ipwhitelist
        if not DaraCore.is_null(request.white_ip_group):
            body['whiteIpGroup'] = request.white_ip_group
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKibanaWhiteIps',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/kibana-white-ips',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKibanaWhiteIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_kibana_white_ips(
        self,
        instance_id: str,
        request: main_models.UpdateKibanaWhiteIpsRequest,
    ) -> main_models.UpdateKibanaWhiteIpsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_kibana_white_ips_with_options(instance_id, request, headers, runtime)

    async def update_kibana_white_ips_async(
        self,
        instance_id: str,
        request: main_models.UpdateKibanaWhiteIpsRequest,
    ) -> main_models.UpdateKibanaWhiteIpsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_kibana_white_ips_with_options_async(instance_id, request, headers, runtime)

    def update_logstash_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateLogstashRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLogstashResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.node_amount):
            body['nodeAmount'] = request.node_amount
        if not DaraCore.is_null(request.node_spec):
            body['nodeSpec'] = request.node_spec
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLogstash',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLogstashResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_logstash_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateLogstashRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLogstashResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.node_amount):
            body['nodeAmount'] = request.node_amount
        if not DaraCore.is_null(request.node_spec):
            body['nodeSpec'] = request.node_spec
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLogstash',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLogstashResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_logstash(
        self,
        instance_id: str,
        request: main_models.UpdateLogstashRequest,
    ) -> main_models.UpdateLogstashResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_logstash_with_options(instance_id, request, headers, runtime)

    async def update_logstash_async(
        self,
        instance_id: str,
        request: main_models.UpdateLogstashRequest,
    ) -> main_models.UpdateLogstashResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_logstash_with_options_async(instance_id, request, headers, runtime)

    def update_logstash_charge_type_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateLogstashChargeTypeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLogstashChargeTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateLogstashChargeType',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/actions/convert-pay-type',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLogstashChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_logstash_charge_type_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateLogstashChargeTypeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLogstashChargeTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateLogstashChargeType',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/actions/convert-pay-type',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLogstashChargeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_logstash_charge_type(
        self,
        instance_id: str,
        request: main_models.UpdateLogstashChargeTypeRequest,
    ) -> main_models.UpdateLogstashChargeTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_logstash_charge_type_with_options(instance_id, request, headers, runtime)

    async def update_logstash_charge_type_async(
        self,
        instance_id: str,
        request: main_models.UpdateLogstashChargeTypeRequest,
    ) -> main_models.UpdateLogstashChargeTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_logstash_charge_type_with_options_async(instance_id, request, headers, runtime)

    def update_logstash_description_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateLogstashDescriptionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLogstashDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLogstashDescription',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/description',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLogstashDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_logstash_description_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateLogstashDescriptionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLogstashDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLogstashDescription',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/description',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLogstashDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_logstash_description(
        self,
        instance_id: str,
        request: main_models.UpdateLogstashDescriptionRequest,
    ) -> main_models.UpdateLogstashDescriptionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_logstash_description_with_options(instance_id, request, headers, runtime)

    async def update_logstash_description_async(
        self,
        instance_id: str,
        request: main_models.UpdateLogstashDescriptionRequest,
    ) -> main_models.UpdateLogstashDescriptionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_logstash_description_with_options_async(instance_id, request, headers, runtime)

    def update_logstash_settings_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateLogstashSettingsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLogstashSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateLogstashSettings',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/instance-settings',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLogstashSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_logstash_settings_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateLogstashSettingsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLogstashSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateLogstashSettings',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/instance-settings',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLogstashSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_logstash_settings(
        self,
        instance_id: str,
        request: main_models.UpdateLogstashSettingsRequest,
    ) -> main_models.UpdateLogstashSettingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_logstash_settings_with_options(instance_id, request, headers, runtime)

    async def update_logstash_settings_async(
        self,
        instance_id: str,
        request: main_models.UpdateLogstashSettingsRequest,
    ) -> main_models.UpdateLogstashSettingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_logstash_settings_with_options_async(instance_id, request, headers, runtime)

    def update_pipeline_management_config_with_options(
        self,
        instance_id: str,
        request: main_models.UpdatePipelineManagementConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePipelineManagementConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.endpoints):
            body['endpoints'] = request.endpoints
        if not DaraCore.is_null(request.es_instance_id):
            body['esInstanceId'] = request.es_instance_id
        if not DaraCore.is_null(request.password):
            body['password'] = request.password
        if not DaraCore.is_null(request.pipeline_ids):
            body['pipelineIds'] = request.pipeline_ids
        if not DaraCore.is_null(request.pipeline_management_type):
            body['pipelineManagementType'] = request.pipeline_management_type
        if not DaraCore.is_null(request.user_name):
            body['userName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePipelineManagementConfig',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/pipeline-management-config',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePipelineManagementConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pipeline_management_config_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdatePipelineManagementConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePipelineManagementConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.endpoints):
            body['endpoints'] = request.endpoints
        if not DaraCore.is_null(request.es_instance_id):
            body['esInstanceId'] = request.es_instance_id
        if not DaraCore.is_null(request.password):
            body['password'] = request.password
        if not DaraCore.is_null(request.pipeline_ids):
            body['pipelineIds'] = request.pipeline_ids
        if not DaraCore.is_null(request.pipeline_management_type):
            body['pipelineManagementType'] = request.pipeline_management_type
        if not DaraCore.is_null(request.user_name):
            body['userName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePipelineManagementConfig',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/pipeline-management-config',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePipelineManagementConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pipeline_management_config(
        self,
        instance_id: str,
        request: main_models.UpdatePipelineManagementConfigRequest,
    ) -> main_models.UpdatePipelineManagementConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_pipeline_management_config_with_options(instance_id, request, headers, runtime)

    async def update_pipeline_management_config_async(
        self,
        instance_id: str,
        request: main_models.UpdatePipelineManagementConfigRequest,
    ) -> main_models.UpdatePipelineManagementConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_pipeline_management_config_with_options_async(instance_id, request, headers, runtime)

    def update_pipelines_with_options(
        self,
        instance_id: str,
        request: main_models.UpdatePipelinesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePipelinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.trigger):
            query['trigger'] = request.trigger
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdatePipelines',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/pipelines',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pipelines_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdatePipelinesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePipelinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.trigger):
            query['trigger'] = request.trigger
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdatePipelines',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/pipelines',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePipelinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pipelines(
        self,
        instance_id: str,
        request: main_models.UpdatePipelinesRequest,
    ) -> main_models.UpdatePipelinesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_pipelines_with_options(instance_id, request, headers, runtime)

    async def update_pipelines_async(
        self,
        instance_id: str,
        request: main_models.UpdatePipelinesRequest,
    ) -> main_models.UpdatePipelinesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_pipelines_with_options_async(instance_id, request, headers, runtime)

    def update_private_network_white_ips_with_options(
        self,
        instance_id: str,
        request: main_models.UpdatePrivateNetworkWhiteIpsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrivateNetworkWhiteIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.modify_mode):
            query['modifyMode'] = request.modify_mode
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrivateNetworkWhiteIps',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/private-network-white-ips',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrivateNetworkWhiteIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_private_network_white_ips_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdatePrivateNetworkWhiteIpsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrivateNetworkWhiteIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.modify_mode):
            query['modifyMode'] = request.modify_mode
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrivateNetworkWhiteIps',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/private-network-white-ips',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrivateNetworkWhiteIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_private_network_white_ips(
        self,
        instance_id: str,
        request: main_models.UpdatePrivateNetworkWhiteIpsRequest,
    ) -> main_models.UpdatePrivateNetworkWhiteIpsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_private_network_white_ips_with_options(instance_id, request, headers, runtime)

    async def update_private_network_white_ips_async(
        self,
        instance_id: str,
        request: main_models.UpdatePrivateNetworkWhiteIpsRequest,
    ) -> main_models.UpdatePrivateNetworkWhiteIpsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_private_network_white_ips_with_options_async(instance_id, request, headers, runtime)

    def update_public_network_with_options(
        self,
        instance_id: str,
        request: main_models.UpdatePublicNetworkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePublicNetworkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdatePublicNetwork',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/public-network',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePublicNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_public_network_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdatePublicNetworkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePublicNetworkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdatePublicNetwork',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/public-network',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePublicNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_public_network(
        self,
        instance_id: str,
        request: main_models.UpdatePublicNetworkRequest,
    ) -> main_models.UpdatePublicNetworkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_public_network_with_options(instance_id, request, headers, runtime)

    async def update_public_network_async(
        self,
        instance_id: str,
        request: main_models.UpdatePublicNetworkRequest,
    ) -> main_models.UpdatePublicNetworkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_public_network_with_options_async(instance_id, request, headers, runtime)

    def update_public_white_ips_with_options(
        self,
        instance_id: str,
        request: main_models.UpdatePublicWhiteIpsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePublicWhiteIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.modify_mode):
            query['modifyMode'] = request.modify_mode
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdatePublicWhiteIps',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/public-white-ips',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePublicWhiteIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_public_white_ips_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdatePublicWhiteIpsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePublicWhiteIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.modify_mode):
            query['modifyMode'] = request.modify_mode
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdatePublicWhiteIps',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/public-white-ips',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePublicWhiteIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_public_white_ips(
        self,
        instance_id: str,
        request: main_models.UpdatePublicWhiteIpsRequest,
    ) -> main_models.UpdatePublicWhiteIpsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_public_white_ips_with_options(instance_id, request, headers, runtime)

    async def update_public_white_ips_async(
        self,
        instance_id: str,
        request: main_models.UpdatePublicWhiteIpsRequest,
    ) -> main_models.UpdatePublicWhiteIpsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_public_white_ips_with_options_async(instance_id, request, headers, runtime)

    def update_read_write_policy_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateReadWritePolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateReadWritePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateReadWritePolicy',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/update-read-write-policy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateReadWritePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_read_write_policy_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateReadWritePolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateReadWritePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateReadWritePolicy',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/update-read-write-policy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateReadWritePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_read_write_policy(
        self,
        instance_id: str,
        request: main_models.UpdateReadWritePolicyRequest,
    ) -> main_models.UpdateReadWritePolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_read_write_policy_with_options(instance_id, request, headers, runtime)

    async def update_read_write_policy_async(
        self,
        instance_id: str,
        request: main_models.UpdateReadWritePolicyRequest,
    ) -> main_models.UpdateReadWritePolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_read_write_policy_with_options_async(instance_id, request, headers, runtime)

    def update_snapshot_setting_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateSnapshotSettingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSnapshotSettingResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateSnapshotSetting',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/snapshot-setting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSnapshotSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_snapshot_setting_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateSnapshotSettingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSnapshotSettingResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateSnapshotSetting',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/snapshot-setting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSnapshotSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_snapshot_setting(
        self,
        instance_id: str,
        request: main_models.UpdateSnapshotSettingRequest,
    ) -> main_models.UpdateSnapshotSettingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_snapshot_setting_with_options(instance_id, request, headers, runtime)

    async def update_snapshot_setting_async(
        self,
        instance_id: str,
        request: main_models.UpdateSnapshotSettingRequest,
    ) -> main_models.UpdateSnapshotSettingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_snapshot_setting_with_options_async(instance_id, request, headers, runtime)

    def update_synonyms_dicts_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateSynonymsDictsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSynonymsDictsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateSynonymsDicts',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/synonymsDict',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSynonymsDictsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_synonyms_dicts_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateSynonymsDictsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSynonymsDictsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateSynonymsDicts',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/synonymsDict',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSynonymsDictsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_synonyms_dicts(
        self,
        instance_id: str,
        request: main_models.UpdateSynonymsDictsRequest,
    ) -> main_models.UpdateSynonymsDictsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_synonyms_dicts_with_options(instance_id, request, headers, runtime)

    async def update_synonyms_dicts_async(
        self,
        instance_id: str,
        request: main_models.UpdateSynonymsDictsRequest,
    ) -> main_models.UpdateSynonymsDictsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_synonyms_dicts_with_options_async(instance_id, request, headers, runtime)

    def update_template_with_options(
        self,
        instance_id: str,
        template_name: str,
        request: main_models.UpdateTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateTemplate',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/templates/{DaraURL.percent_encode(template_name)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_template_with_options_async(
        self,
        instance_id: str,
        template_name: str,
        request: main_models.UpdateTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateTemplate',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/templates/{DaraURL.percent_encode(template_name)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_template(
        self,
        instance_id: str,
        template_name: str,
        request: main_models.UpdateTemplateRequest,
    ) -> main_models.UpdateTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_template_with_options(instance_id, template_name, request, headers, runtime)

    async def update_template_async(
        self,
        instance_id: str,
        template_name: str,
        request: main_models.UpdateTemplateRequest,
    ) -> main_models.UpdateTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_template_with_options_async(instance_id, template_name, request, headers, runtime)

    def update_white_ips_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateWhiteIpsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWhiteIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.modify_mode):
            query['modifyMode'] = request.modify_mode
        body = {}
        if not DaraCore.is_null(request.es_ipwhitelist):
            body['esIPWhitelist'] = request.es_ipwhitelist
        if not DaraCore.is_null(request.white_ip_group):
            body['whiteIpGroup'] = request.white_ip_group
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWhiteIps',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/white-ips',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWhiteIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_white_ips_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateWhiteIpsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWhiteIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.modify_mode):
            query['modifyMode'] = request.modify_mode
        body = {}
        if not DaraCore.is_null(request.es_ipwhitelist):
            body['esIPWhitelist'] = request.es_ipwhitelist
        if not DaraCore.is_null(request.white_ip_group):
            body['whiteIpGroup'] = request.white_ip_group
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWhiteIps',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/white-ips',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWhiteIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_white_ips(
        self,
        instance_id: str,
        request: main_models.UpdateWhiteIpsRequest,
    ) -> main_models.UpdateWhiteIpsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_white_ips_with_options(instance_id, request, headers, runtime)

    async def update_white_ips_async(
        self,
        instance_id: str,
        request: main_models.UpdateWhiteIpsRequest,
    ) -> main_models.UpdateWhiteIpsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_white_ips_with_options_async(instance_id, request, headers, runtime)

    def update_xpack_monitor_config_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateXpackMonitorConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateXpackMonitorConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.endpoints):
            body['endpoints'] = request.endpoints
        if not DaraCore.is_null(request.password):
            body['password'] = request.password
        if not DaraCore.is_null(request.user_name):
            body['userName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateXpackMonitorConfig',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/xpack-monitor-config',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateXpackMonitorConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_xpack_monitor_config_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateXpackMonitorConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateXpackMonitorConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.endpoints):
            body['endpoints'] = request.endpoints
        if not DaraCore.is_null(request.password):
            body['password'] = request.password
        if not DaraCore.is_null(request.user_name):
            body['userName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateXpackMonitorConfig',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/xpack-monitor-config',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateXpackMonitorConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_xpack_monitor_config(
        self,
        instance_id: str,
        request: main_models.UpdateXpackMonitorConfigRequest,
    ) -> main_models.UpdateXpackMonitorConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_xpack_monitor_config_with_options(instance_id, request, headers, runtime)

    async def update_xpack_monitor_config_async(
        self,
        instance_id: str,
        request: main_models.UpdateXpackMonitorConfigRequest,
    ) -> main_models.UpdateXpackMonitorConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_xpack_monitor_config_with_options_async(instance_id, request, headers, runtime)

    def upgrade_engine_version_with_options(
        self,
        instance_id: str,
        request: main_models.UpgradeEngineVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeEngineVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.update_strategy):
            query['updateStrategy'] = request.update_strategy
        body = {}
        if not DaraCore.is_null(request.plugins):
            body['plugins'] = request.plugins
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeEngineVersion',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/upgrade-version',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeEngineVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_engine_version_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpgradeEngineVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeEngineVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.update_strategy):
            query['updateStrategy'] = request.update_strategy
        body = {}
        if not DaraCore.is_null(request.plugins):
            body['plugins'] = request.plugins
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeEngineVersion',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/actions/upgrade-version',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeEngineVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_engine_version(
        self,
        instance_id: str,
        request: main_models.UpgradeEngineVersionRequest,
    ) -> main_models.UpgradeEngineVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.upgrade_engine_version_with_options(instance_id, request, headers, runtime)

    async def upgrade_engine_version_async(
        self,
        instance_id: str,
        request: main_models.UpgradeEngineVersionRequest,
    ) -> main_models.UpgradeEngineVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.upgrade_engine_version_with_options_async(instance_id, request, headers, runtime)

    def validate_connection_with_options(
        self,
        instance_id: str,
        request: main_models.ValidateConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ValidateConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'ValidateConnection',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/validate-connection',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_connection_with_options_async(
        self,
        instance_id: str,
        request: main_models.ValidateConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ValidateConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'ValidateConnection',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/logstashes/{DaraURL.percent_encode(instance_id)}/validate-connection',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_connection(
        self,
        instance_id: str,
        request: main_models.ValidateConnectionRequest,
    ) -> main_models.ValidateConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.validate_connection_with_options(instance_id, request, headers, runtime)

    async def validate_connection_async(
        self,
        instance_id: str,
        request: main_models.ValidateConnectionRequest,
    ) -> main_models.ValidateConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.validate_connection_with_options_async(instance_id, request, headers, runtime)

    def validate_shrink_nodes_with_options(
        self,
        instance_id: str,
        request: main_models.ValidateShrinkNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ValidateShrinkNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.count):
            query['count'] = request.count
        if not DaraCore.is_null(request.ignore_status):
            query['ignoreStatus'] = request.ignore_status
        if not DaraCore.is_null(request.node_type):
            query['nodeType'] = request.node_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ValidateShrinkNodes',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/validate-shrink-nodes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateShrinkNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_shrink_nodes_with_options_async(
        self,
        instance_id: str,
        request: main_models.ValidateShrinkNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ValidateShrinkNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.count):
            query['count'] = request.count
        if not DaraCore.is_null(request.ignore_status):
            query['ignoreStatus'] = request.ignore_status
        if not DaraCore.is_null(request.node_type):
            query['nodeType'] = request.node_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ValidateShrinkNodes',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/validate-shrink-nodes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateShrinkNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_shrink_nodes(
        self,
        instance_id: str,
        request: main_models.ValidateShrinkNodesRequest,
    ) -> main_models.ValidateShrinkNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.validate_shrink_nodes_with_options(instance_id, request, headers, runtime)

    async def validate_shrink_nodes_async(
        self,
        instance_id: str,
        request: main_models.ValidateShrinkNodesRequest,
    ) -> main_models.ValidateShrinkNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.validate_shrink_nodes_with_options_async(instance_id, request, headers, runtime)

    def validate_slr_permission_with_options(
        self,
        request: main_models.ValidateSlrPermissionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ValidateSlrPermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.rolename):
            query['rolename'] = request.rolename
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidateSlrPermission',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/user/servicerolepermission',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateSlrPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_slr_permission_with_options_async(
        self,
        request: main_models.ValidateSlrPermissionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ValidateSlrPermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.rolename):
            query['rolename'] = request.rolename
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidateSlrPermission',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/user/servicerolepermission',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateSlrPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_slr_permission(
        self,
        request: main_models.ValidateSlrPermissionRequest,
    ) -> main_models.ValidateSlrPermissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.validate_slr_permission_with_options(request, headers, runtime)

    async def validate_slr_permission_async(
        self,
        request: main_models.ValidateSlrPermissionRequest,
    ) -> main_models.ValidateSlrPermissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.validate_slr_permission_with_options_async(request, headers, runtime)

    def validate_transferable_nodes_with_options(
        self,
        instance_id: str,
        request: main_models.ValidateTransferableNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ValidateTransferableNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.node_type):
            query['nodeType'] = request.node_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ValidateTransferableNodes',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/validate-transfer-nodes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateTransferableNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_transferable_nodes_with_options_async(
        self,
        instance_id: str,
        request: main_models.ValidateTransferableNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ValidateTransferableNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.node_type):
            query['nodeType'] = request.node_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ValidateTransferableNodes',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances/{DaraURL.percent_encode(instance_id)}/validate-transfer-nodes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateTransferableNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_transferable_nodes(
        self,
        instance_id: str,
        request: main_models.ValidateTransferableNodesRequest,
    ) -> main_models.ValidateTransferableNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.validate_transferable_nodes_with_options(instance_id, request, headers, runtime)

    async def validate_transferable_nodes_async(
        self,
        instance_id: str,
        request: main_models.ValidateTransferableNodesRequest,
    ) -> main_models.ValidateTransferableNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.validate_transferable_nodes_with_options_async(instance_id, request, headers, runtime)

    def create_instance_with_options(
        self,
        request: main_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.client_node_configuration):
            body['clientNodeConfiguration'] = request.client_node_configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.elastic_data_node_configuration):
            body['elasticDataNodeConfiguration'] = request.elastic_data_node_configuration
        if not DaraCore.is_null(request.es_admin_password):
            body['esAdminPassword'] = request.es_admin_password
        if not DaraCore.is_null(request.es_version):
            body['esVersion'] = request.es_version
        if not DaraCore.is_null(request.instance_category):
            body['instanceCategory'] = request.instance_category
        if not DaraCore.is_null(request.kibana_configuration):
            body['kibanaConfiguration'] = request.kibana_configuration
        if not DaraCore.is_null(request.master_configuration):
            body['masterConfiguration'] = request.master_configuration
        if not DaraCore.is_null(request.network_config):
            body['networkConfig'] = request.network_config
        if not DaraCore.is_null(request.node_amount):
            body['nodeAmount'] = request.node_amount
        if not DaraCore.is_null(request.node_spec):
            body['nodeSpec'] = request.node_spec
        if not DaraCore.is_null(request.payment_info):
            body['paymentInfo'] = request.payment_info
        if not DaraCore.is_null(request.payment_type):
            body['paymentType'] = request.payment_type
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.warm_node_configuration):
            body['warmNodeConfiguration'] = request.warm_node_configuration
        if not DaraCore.is_null(request.zone_count):
            body['zoneCount'] = request.zone_count
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'createInstance',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: main_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.client_node_configuration):
            body['clientNodeConfiguration'] = request.client_node_configuration
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.elastic_data_node_configuration):
            body['elasticDataNodeConfiguration'] = request.elastic_data_node_configuration
        if not DaraCore.is_null(request.es_admin_password):
            body['esAdminPassword'] = request.es_admin_password
        if not DaraCore.is_null(request.es_version):
            body['esVersion'] = request.es_version
        if not DaraCore.is_null(request.instance_category):
            body['instanceCategory'] = request.instance_category
        if not DaraCore.is_null(request.kibana_configuration):
            body['kibanaConfiguration'] = request.kibana_configuration
        if not DaraCore.is_null(request.master_configuration):
            body['masterConfiguration'] = request.master_configuration
        if not DaraCore.is_null(request.network_config):
            body['networkConfig'] = request.network_config
        if not DaraCore.is_null(request.node_amount):
            body['nodeAmount'] = request.node_amount
        if not DaraCore.is_null(request.node_spec):
            body['nodeSpec'] = request.node_spec
        if not DaraCore.is_null(request.payment_info):
            body['paymentInfo'] = request.payment_info
        if not DaraCore.is_null(request.payment_type):
            body['paymentType'] = request.payment_type
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.warm_node_configuration):
            body['warmNodeConfiguration'] = request.warm_node_configuration
        if not DaraCore.is_null(request.zone_count):
            body['zoneCount'] = request.zone_count
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'createInstance',
            version = '2017-06-13',
            protocol = 'HTTPS',
            pathname = f'/openapi/instances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    async def create_instance_async(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_instance_with_options_async(request, headers, runtime)
