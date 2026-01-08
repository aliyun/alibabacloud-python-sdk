# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_sae20190506 import models as main_models
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
        self._endpoint = self.get_endpoint('sae', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def abort_and_rollback_change_order_with_options(
        self,
        request: main_models.AbortAndRollbackChangeOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AbortAndRollbackChangeOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AbortAndRollbackChangeOrder',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/changeorder/AbortAndRollbackChangeOrder',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AbortAndRollbackChangeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def abort_and_rollback_change_order_with_options_async(
        self,
        request: main_models.AbortAndRollbackChangeOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AbortAndRollbackChangeOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AbortAndRollbackChangeOrder',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/changeorder/AbortAndRollbackChangeOrder',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AbortAndRollbackChangeOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abort_and_rollback_change_order(
        self,
        request: main_models.AbortAndRollbackChangeOrderRequest,
    ) -> main_models.AbortAndRollbackChangeOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.abort_and_rollback_change_order_with_options(request, headers, runtime)

    async def abort_and_rollback_change_order_async(
        self,
        request: main_models.AbortAndRollbackChangeOrderRequest,
    ) -> main_models.AbortAndRollbackChangeOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.abort_and_rollback_change_order_with_options_async(request, headers, runtime)

    def abort_change_order_with_options(
        self,
        request: main_models.AbortChangeOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AbortChangeOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        if not DaraCore.is_null(request.rollback):
            query['Rollback'] = request.rollback
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AbortChangeOrder',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/changeorder/AbortChangeOrder',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AbortChangeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def abort_change_order_with_options_async(
        self,
        request: main_models.AbortChangeOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AbortChangeOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        if not DaraCore.is_null(request.rollback):
            query['Rollback'] = request.rollback
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AbortChangeOrder',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/changeorder/AbortChangeOrder',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AbortChangeOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abort_change_order(
        self,
        request: main_models.AbortChangeOrderRequest,
    ) -> main_models.AbortChangeOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.abort_change_order_with_options(request, headers, runtime)

    async def abort_change_order_async(
        self,
        request: main_models.AbortChangeOrderRequest,
    ) -> main_models.AbortChangeOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.abort_change_order_with_options_async(request, headers, runtime)

    def batch_restart_applications_with_options(
        self,
        request: main_models.BatchRestartApplicationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchRestartApplicationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchRestartApplications',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/batchRestartApplications',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchRestartApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_restart_applications_with_options_async(
        self,
        request: main_models.BatchRestartApplicationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchRestartApplicationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchRestartApplications',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/batchRestartApplications',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchRestartApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_restart_applications(
        self,
        request: main_models.BatchRestartApplicationsRequest,
    ) -> main_models.BatchRestartApplicationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_restart_applications_with_options(request, headers, runtime)

    async def batch_restart_applications_async(
        self,
        request: main_models.BatchRestartApplicationsRequest,
    ) -> main_models.BatchRestartApplicationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_restart_applications_with_options_async(request, headers, runtime)

    def batch_start_applications_with_options(
        self,
        request: main_models.BatchStartApplicationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchStartApplicationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchStartApplications',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/batchStartApplications',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchStartApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_start_applications_with_options_async(
        self,
        request: main_models.BatchStartApplicationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchStartApplicationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchStartApplications',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/batchStartApplications',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchStartApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_start_applications(
        self,
        request: main_models.BatchStartApplicationsRequest,
    ) -> main_models.BatchStartApplicationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_start_applications_with_options(request, headers, runtime)

    async def batch_start_applications_async(
        self,
        request: main_models.BatchStartApplicationsRequest,
    ) -> main_models.BatchStartApplicationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_start_applications_with_options_async(request, headers, runtime)

    def batch_stop_applications_with_options(
        self,
        request: main_models.BatchStopApplicationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchStopApplicationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchStopApplications',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/batchStopApplications',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchStopApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_stop_applications_with_options_async(
        self,
        request: main_models.BatchStopApplicationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchStopApplicationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchStopApplications',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/batchStopApplications',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchStopApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_stop_applications(
        self,
        request: main_models.BatchStopApplicationsRequest,
    ) -> main_models.BatchStopApplicationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_stop_applications_with_options(request, headers, runtime)

    async def batch_stop_applications_async(
        self,
        request: main_models.BatchStopApplicationsRequest,
    ) -> main_models.BatchStopApplicationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_stop_applications_with_options_async(request, headers, runtime)

    def bind_nlb_with_options(
        self,
        request: main_models.BindNlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BindNlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.listeners):
            query['Listeners'] = request.listeners
        if not DaraCore.is_null(request.nlb_id):
            query['NlbId'] = request.nlb_id
        if not DaraCore.is_null(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindNlb',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/nlb',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindNlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_nlb_with_options_async(
        self,
        request: main_models.BindNlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BindNlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.listeners):
            query['Listeners'] = request.listeners
        if not DaraCore.is_null(request.nlb_id):
            query['NlbId'] = request.nlb_id
        if not DaraCore.is_null(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindNlb',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/nlb',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindNlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_nlb(
        self,
        request: main_models.BindNlbRequest,
    ) -> main_models.BindNlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.bind_nlb_with_options(request, headers, runtime)

    async def bind_nlb_async(
        self,
        request: main_models.BindNlbRequest,
    ) -> main_models.BindNlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.bind_nlb_with_options_async(request, headers, runtime)

    def bind_slb_with_options(
        self,
        request: main_models.BindSlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BindSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.internet):
            query['Internet'] = request.internet
        if not DaraCore.is_null(request.internet_slb_charge_type):
            query['InternetSlbChargeType'] = request.internet_slb_charge_type
        if not DaraCore.is_null(request.internet_slb_id):
            query['InternetSlbId'] = request.internet_slb_id
        if not DaraCore.is_null(request.intranet):
            query['Intranet'] = request.intranet
        if not DaraCore.is_null(request.intranet_slb_charge_type):
            query['IntranetSlbChargeType'] = request.intranet_slb_charge_type
        if not DaraCore.is_null(request.intranet_slb_id):
            query['IntranetSlbId'] = request.intranet_slb_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindSlb',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/slb',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_slb_with_options_async(
        self,
        request: main_models.BindSlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BindSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.internet):
            query['Internet'] = request.internet
        if not DaraCore.is_null(request.internet_slb_charge_type):
            query['InternetSlbChargeType'] = request.internet_slb_charge_type
        if not DaraCore.is_null(request.internet_slb_id):
            query['InternetSlbId'] = request.internet_slb_id
        if not DaraCore.is_null(request.intranet):
            query['Intranet'] = request.intranet
        if not DaraCore.is_null(request.intranet_slb_charge_type):
            query['IntranetSlbChargeType'] = request.intranet_slb_charge_type
        if not DaraCore.is_null(request.intranet_slb_id):
            query['IntranetSlbId'] = request.intranet_slb_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindSlb',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/slb',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_slb(
        self,
        request: main_models.BindSlbRequest,
    ) -> main_models.BindSlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.bind_slb_with_options(request, headers, runtime)

    async def bind_slb_async(
        self,
        request: main_models.BindSlbRequest,
    ) -> main_models.BindSlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.bind_slb_with_options_async(request, headers, runtime)

    def confirm_pipeline_batch_with_options(
        self,
        request: main_models.ConfirmPipelineBatchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ConfirmPipelineBatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.confirm):
            query['Confirm'] = request.confirm
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfirmPipelineBatch',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/changeorder/ConfirmPipelineBatch',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfirmPipelineBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_pipeline_batch_with_options_async(
        self,
        request: main_models.ConfirmPipelineBatchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ConfirmPipelineBatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.confirm):
            query['Confirm'] = request.confirm
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfirmPipelineBatch',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/changeorder/ConfirmPipelineBatch',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfirmPipelineBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_pipeline_batch(
        self,
        request: main_models.ConfirmPipelineBatchRequest,
    ) -> main_models.ConfirmPipelineBatchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.confirm_pipeline_batch_with_options(request, headers, runtime)

    async def confirm_pipeline_batch_async(
        self,
        request: main_models.ConfirmPipelineBatchRequest,
    ) -> main_models.ConfirmPipelineBatchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.confirm_pipeline_batch_with_options_async(request, headers, runtime)

    def create_application_with_options(
        self,
        tmp_req: main_models.CreateApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationResponse:
        tmp_req.validate()
        request = main_models.CreateApplicationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.init_containers_config):
            request.init_containers_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.init_containers_config, 'InitContainersConfig', 'json')
        if not DaraCore.is_null(tmp_req.sidecar_containers_config):
            request.sidecar_containers_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.sidecar_containers_config, 'SidecarContainersConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not DaraCore.is_null(request.agent_version):
            query['AgentVersion'] = request.agent_version
        if not DaraCore.is_null(request.app_description):
            query['AppDescription'] = request.app_description
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_source):
            query['AppSource'] = request.app_source
        if not DaraCore.is_null(request.auto_config):
            query['AutoConfig'] = request.auto_config
        if not DaraCore.is_null(request.command):
            query['Command'] = request.command
        if not DaraCore.is_null(request.command_args):
            query['CommandArgs'] = request.command_args
        if not DaraCore.is_null(request.cpu):
            query['Cpu'] = request.cpu
        if not DaraCore.is_null(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not DaraCore.is_null(request.custom_image_network_type):
            query['CustomImageNetworkType'] = request.custom_image_network_type
        if not DaraCore.is_null(request.deploy):
            query['Deploy'] = request.deploy
        if not DaraCore.is_null(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not DaraCore.is_null(request.dotnet):
            query['Dotnet'] = request.dotnet
        if not DaraCore.is_null(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not DaraCore.is_null(request.enable_cpu_burst):
            query['EnableCpuBurst'] = request.enable_cpu_burst
        if not DaraCore.is_null(request.enable_ebpf):
            query['EnableEbpf'] = request.enable_ebpf
        if not DaraCore.is_null(request.enable_namespace_agent_version):
            query['EnableNamespaceAgentVersion'] = request.enable_namespace_agent_version
        if not DaraCore.is_null(request.enable_namespace_sls_config):
            query['EnableNamespaceSlsConfig'] = request.enable_namespace_sls_config
        if not DaraCore.is_null(request.enable_new_arms):
            query['EnableNewArms'] = request.enable_new_arms
        if not DaraCore.is_null(request.enable_prometheus):
            query['EnablePrometheus'] = request.enable_prometheus
        if not DaraCore.is_null(request.envs):
            query['Envs'] = request.envs
        if not DaraCore.is_null(request.gpu_config):
            query['GpuConfig'] = request.gpu_config
        if not DaraCore.is_null(request.headless_pvtz_discovery_svc):
            query['HeadlessPvtzDiscoverySvc'] = request.headless_pvtz_discovery_svc
        if not DaraCore.is_null(request.html):
            query['Html'] = request.html
        if not DaraCore.is_null(request.image_pull_secrets):
            query['ImagePullSecrets'] = request.image_pull_secrets
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.is_stateful):
            query['IsStateful'] = request.is_stateful
        if not DaraCore.is_null(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not DaraCore.is_null(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not DaraCore.is_null(request.jdk):
            query['Jdk'] = request.jdk
        if not DaraCore.is_null(request.kafka_configs):
            query['KafkaConfigs'] = request.kafka_configs
        if not DaraCore.is_null(request.liveness):
            query['Liveness'] = request.liveness
        if not DaraCore.is_null(request.loki_configs):
            query['LokiConfigs'] = request.loki_configs
        if not DaraCore.is_null(request.memory):
            query['Memory'] = request.memory
        if not DaraCore.is_null(request.micro_registration):
            query['MicroRegistration'] = request.micro_registration
        if not DaraCore.is_null(request.microservice_engine_config):
            query['MicroserviceEngineConfig'] = request.microservice_engine_config
        if not DaraCore.is_null(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not DaraCore.is_null(request.mount_host):
            query['MountHost'] = request.mount_host
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.nas_configs):
            query['NasConfigs'] = request.nas_configs
        if not DaraCore.is_null(request.nas_id):
            query['NasId'] = request.nas_id
        if not DaraCore.is_null(request.new_sae_version):
            query['NewSaeVersion'] = request.new_sae_version
        if not DaraCore.is_null(request.oidc_role_name):
            query['OidcRoleName'] = request.oidc_role_name
        if not DaraCore.is_null(request.package_type):
            query['PackageType'] = request.package_type
        if not DaraCore.is_null(request.package_url):
            query['PackageUrl'] = request.package_url
        if not DaraCore.is_null(request.package_version):
            query['PackageVersion'] = request.package_version
        if not DaraCore.is_null(request.php_arms_config_location):
            query['PhpArmsConfigLocation'] = request.php_arms_config_location
        if not DaraCore.is_null(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not DaraCore.is_null(request.post_start):
            query['PostStart'] = request.post_start
        if not DaraCore.is_null(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not DaraCore.is_null(request.programming_language):
            query['ProgrammingLanguage'] = request.programming_language
        if not DaraCore.is_null(request.pvtz_discovery_svc):
            query['PvtzDiscoverySvc'] = request.pvtz_discovery_svc
        if not DaraCore.is_null(request.python):
            query['Python'] = request.python
        if not DaraCore.is_null(request.python_modules):
            query['PythonModules'] = request.python_modules
        if not DaraCore.is_null(request.readiness):
            query['Readiness'] = request.readiness
        if not DaraCore.is_null(request.replicas):
            query['Replicas'] = request.replicas
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sae_version):
            query['SaeVersion'] = request.sae_version
        if not DaraCore.is_null(request.secret_mount_desc):
            query['SecretMountDesc'] = request.secret_mount_desc
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not DaraCore.is_null(request.sls_log_env_tags):
            query['SlsLogEnvTags'] = request.sls_log_env_tags
        if not DaraCore.is_null(request.startup_probe):
            query['StartupProbe'] = request.startup_probe
        if not DaraCore.is_null(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not DaraCore.is_null(request.timezone):
            query['Timezone'] = request.timezone
        if not DaraCore.is_null(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not DaraCore.is_null(request.web_container):
            query['WebContainer'] = request.web_container
        body = {}
        if not DaraCore.is_null(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not DaraCore.is_null(request.associate_eip):
            body['AssociateEip'] = request.associate_eip
        if not DaraCore.is_null(request.base_app_id):
            body['BaseAppId'] = request.base_app_id
        if not DaraCore.is_null(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not DaraCore.is_null(request.empty_dir_desc):
            body['EmptyDirDesc'] = request.empty_dir_desc
        if not DaraCore.is_null(request.enable_sidecar_resource_isolated):
            body['EnableSidecarResourceIsolated'] = request.enable_sidecar_resource_isolated
        if not DaraCore.is_null(request.init_containers_config_shrink):
            body['InitContainersConfig'] = request.init_containers_config_shrink
        if not DaraCore.is_null(request.micro_registration_config):
            body['MicroRegistrationConfig'] = request.micro_registration_config
        if not DaraCore.is_null(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not DaraCore.is_null(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not DaraCore.is_null(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not DaraCore.is_null(request.php):
            body['Php'] = request.php
        if not DaraCore.is_null(request.php_config):
            body['PhpConfig'] = request.php_config
        if not DaraCore.is_null(request.service_tags):
            body['ServiceTags'] = request.service_tags
        if not DaraCore.is_null(request.sidecar_containers_config_shrink):
            body['SidecarContainersConfig'] = request.sidecar_containers_config_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/createApplication',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_with_options_async(
        self,
        tmp_req: main_models.CreateApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationResponse:
        tmp_req.validate()
        request = main_models.CreateApplicationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.init_containers_config):
            request.init_containers_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.init_containers_config, 'InitContainersConfig', 'json')
        if not DaraCore.is_null(tmp_req.sidecar_containers_config):
            request.sidecar_containers_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.sidecar_containers_config, 'SidecarContainersConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not DaraCore.is_null(request.agent_version):
            query['AgentVersion'] = request.agent_version
        if not DaraCore.is_null(request.app_description):
            query['AppDescription'] = request.app_description
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_source):
            query['AppSource'] = request.app_source
        if not DaraCore.is_null(request.auto_config):
            query['AutoConfig'] = request.auto_config
        if not DaraCore.is_null(request.command):
            query['Command'] = request.command
        if not DaraCore.is_null(request.command_args):
            query['CommandArgs'] = request.command_args
        if not DaraCore.is_null(request.cpu):
            query['Cpu'] = request.cpu
        if not DaraCore.is_null(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not DaraCore.is_null(request.custom_image_network_type):
            query['CustomImageNetworkType'] = request.custom_image_network_type
        if not DaraCore.is_null(request.deploy):
            query['Deploy'] = request.deploy
        if not DaraCore.is_null(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not DaraCore.is_null(request.dotnet):
            query['Dotnet'] = request.dotnet
        if not DaraCore.is_null(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not DaraCore.is_null(request.enable_cpu_burst):
            query['EnableCpuBurst'] = request.enable_cpu_burst
        if not DaraCore.is_null(request.enable_ebpf):
            query['EnableEbpf'] = request.enable_ebpf
        if not DaraCore.is_null(request.enable_namespace_agent_version):
            query['EnableNamespaceAgentVersion'] = request.enable_namespace_agent_version
        if not DaraCore.is_null(request.enable_namespace_sls_config):
            query['EnableNamespaceSlsConfig'] = request.enable_namespace_sls_config
        if not DaraCore.is_null(request.enable_new_arms):
            query['EnableNewArms'] = request.enable_new_arms
        if not DaraCore.is_null(request.enable_prometheus):
            query['EnablePrometheus'] = request.enable_prometheus
        if not DaraCore.is_null(request.envs):
            query['Envs'] = request.envs
        if not DaraCore.is_null(request.gpu_config):
            query['GpuConfig'] = request.gpu_config
        if not DaraCore.is_null(request.headless_pvtz_discovery_svc):
            query['HeadlessPvtzDiscoverySvc'] = request.headless_pvtz_discovery_svc
        if not DaraCore.is_null(request.html):
            query['Html'] = request.html
        if not DaraCore.is_null(request.image_pull_secrets):
            query['ImagePullSecrets'] = request.image_pull_secrets
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.is_stateful):
            query['IsStateful'] = request.is_stateful
        if not DaraCore.is_null(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not DaraCore.is_null(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not DaraCore.is_null(request.jdk):
            query['Jdk'] = request.jdk
        if not DaraCore.is_null(request.kafka_configs):
            query['KafkaConfigs'] = request.kafka_configs
        if not DaraCore.is_null(request.liveness):
            query['Liveness'] = request.liveness
        if not DaraCore.is_null(request.loki_configs):
            query['LokiConfigs'] = request.loki_configs
        if not DaraCore.is_null(request.memory):
            query['Memory'] = request.memory
        if not DaraCore.is_null(request.micro_registration):
            query['MicroRegistration'] = request.micro_registration
        if not DaraCore.is_null(request.microservice_engine_config):
            query['MicroserviceEngineConfig'] = request.microservice_engine_config
        if not DaraCore.is_null(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not DaraCore.is_null(request.mount_host):
            query['MountHost'] = request.mount_host
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.nas_configs):
            query['NasConfigs'] = request.nas_configs
        if not DaraCore.is_null(request.nas_id):
            query['NasId'] = request.nas_id
        if not DaraCore.is_null(request.new_sae_version):
            query['NewSaeVersion'] = request.new_sae_version
        if not DaraCore.is_null(request.oidc_role_name):
            query['OidcRoleName'] = request.oidc_role_name
        if not DaraCore.is_null(request.package_type):
            query['PackageType'] = request.package_type
        if not DaraCore.is_null(request.package_url):
            query['PackageUrl'] = request.package_url
        if not DaraCore.is_null(request.package_version):
            query['PackageVersion'] = request.package_version
        if not DaraCore.is_null(request.php_arms_config_location):
            query['PhpArmsConfigLocation'] = request.php_arms_config_location
        if not DaraCore.is_null(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not DaraCore.is_null(request.post_start):
            query['PostStart'] = request.post_start
        if not DaraCore.is_null(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not DaraCore.is_null(request.programming_language):
            query['ProgrammingLanguage'] = request.programming_language
        if not DaraCore.is_null(request.pvtz_discovery_svc):
            query['PvtzDiscoverySvc'] = request.pvtz_discovery_svc
        if not DaraCore.is_null(request.python):
            query['Python'] = request.python
        if not DaraCore.is_null(request.python_modules):
            query['PythonModules'] = request.python_modules
        if not DaraCore.is_null(request.readiness):
            query['Readiness'] = request.readiness
        if not DaraCore.is_null(request.replicas):
            query['Replicas'] = request.replicas
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sae_version):
            query['SaeVersion'] = request.sae_version
        if not DaraCore.is_null(request.secret_mount_desc):
            query['SecretMountDesc'] = request.secret_mount_desc
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not DaraCore.is_null(request.sls_log_env_tags):
            query['SlsLogEnvTags'] = request.sls_log_env_tags
        if not DaraCore.is_null(request.startup_probe):
            query['StartupProbe'] = request.startup_probe
        if not DaraCore.is_null(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not DaraCore.is_null(request.timezone):
            query['Timezone'] = request.timezone
        if not DaraCore.is_null(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not DaraCore.is_null(request.web_container):
            query['WebContainer'] = request.web_container
        body = {}
        if not DaraCore.is_null(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not DaraCore.is_null(request.associate_eip):
            body['AssociateEip'] = request.associate_eip
        if not DaraCore.is_null(request.base_app_id):
            body['BaseAppId'] = request.base_app_id
        if not DaraCore.is_null(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not DaraCore.is_null(request.empty_dir_desc):
            body['EmptyDirDesc'] = request.empty_dir_desc
        if not DaraCore.is_null(request.enable_sidecar_resource_isolated):
            body['EnableSidecarResourceIsolated'] = request.enable_sidecar_resource_isolated
        if not DaraCore.is_null(request.init_containers_config_shrink):
            body['InitContainersConfig'] = request.init_containers_config_shrink
        if not DaraCore.is_null(request.micro_registration_config):
            body['MicroRegistrationConfig'] = request.micro_registration_config
        if not DaraCore.is_null(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not DaraCore.is_null(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not DaraCore.is_null(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not DaraCore.is_null(request.php):
            body['Php'] = request.php
        if not DaraCore.is_null(request.php_config):
            body['PhpConfig'] = request.php_config
        if not DaraCore.is_null(request.service_tags):
            body['ServiceTags'] = request.service_tags
        if not DaraCore.is_null(request.sidecar_containers_config_shrink):
            body['SidecarContainersConfig'] = request.sidecar_containers_config_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/createApplication',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application(
        self,
        request: main_models.CreateApplicationRequest,
    ) -> main_models.CreateApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_application_with_options(request, headers, runtime)

    async def create_application_async(
        self,
        request: main_models.CreateApplicationRequest,
    ) -> main_models.CreateApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_application_with_options_async(request, headers, runtime)

    def create_application_scaling_rule_with_options(
        self,
        request: main_models.CreateApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.enable_idle):
            query['EnableIdle'] = request.enable_idle
        if not DaraCore.is_null(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not DaraCore.is_null(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not DaraCore.is_null(request.scaling_rule_enable):
            query['ScalingRuleEnable'] = request.scaling_rule_enable
        if not DaraCore.is_null(request.scaling_rule_metric):
            query['ScalingRuleMetric'] = request.scaling_rule_metric
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not DaraCore.is_null(request.scaling_rule_timer):
            query['ScalingRuleTimer'] = request.scaling_rule_timer
        if not DaraCore.is_null(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplicationScalingRule',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/scale/applicationScalingRule',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_scaling_rule_with_options_async(
        self,
        request: main_models.CreateApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.enable_idle):
            query['EnableIdle'] = request.enable_idle
        if not DaraCore.is_null(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not DaraCore.is_null(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not DaraCore.is_null(request.scaling_rule_enable):
            query['ScalingRuleEnable'] = request.scaling_rule_enable
        if not DaraCore.is_null(request.scaling_rule_metric):
            query['ScalingRuleMetric'] = request.scaling_rule_metric
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not DaraCore.is_null(request.scaling_rule_timer):
            query['ScalingRuleTimer'] = request.scaling_rule_timer
        if not DaraCore.is_null(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplicationScalingRule',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/scale/applicationScalingRule',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application_scaling_rule(
        self,
        request: main_models.CreateApplicationScalingRuleRequest,
    ) -> main_models.CreateApplicationScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_application_scaling_rule_with_options(request, headers, runtime)

    async def create_application_scaling_rule_async(
        self,
        request: main_models.CreateApplicationScalingRuleRequest,
    ) -> main_models.CreateApplicationScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_application_scaling_rule_with_options_async(request, headers, runtime)

    def create_config_map_with_options(
        self,
        request: main_models.CreateConfigMapRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConfigMapResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        body = {}
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConfigMap',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/configmap/configMap',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConfigMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_config_map_with_options_async(
        self,
        request: main_models.CreateConfigMapRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConfigMapResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        body = {}
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConfigMap',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/configmap/configMap',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConfigMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_config_map(
        self,
        request: main_models.CreateConfigMapRequest,
    ) -> main_models.CreateConfigMapResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_config_map_with_options(request, headers, runtime)

    async def create_config_map_async(
        self,
        request: main_models.CreateConfigMapRequest,
    ) -> main_models.CreateConfigMapResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_config_map_with_options_async(request, headers, runtime)

    def create_grey_tag_route_with_options(
        self,
        request: main_models.CreateGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateGreyTagRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alb_rules):
            query['AlbRules'] = request.alb_rules
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dubbo_rules):
            query['DubboRules'] = request.dubbo_rules
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.sc_rules):
            query['ScRules'] = request.sc_rules
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGreyTagRoute',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/tagroute/greyTagRoute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGreyTagRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_grey_tag_route_with_options_async(
        self,
        request: main_models.CreateGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateGreyTagRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alb_rules):
            query['AlbRules'] = request.alb_rules
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dubbo_rules):
            query['DubboRules'] = request.dubbo_rules
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.sc_rules):
            query['ScRules'] = request.sc_rules
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGreyTagRoute',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/tagroute/greyTagRoute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGreyTagRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_grey_tag_route(
        self,
        request: main_models.CreateGreyTagRouteRequest,
    ) -> main_models.CreateGreyTagRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_grey_tag_route_with_options(request, headers, runtime)

    async def create_grey_tag_route_async(
        self,
        request: main_models.CreateGreyTagRouteRequest,
    ) -> main_models.CreateGreyTagRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_grey_tag_route_with_options_async(request, headers, runtime)

    def create_ingress_with_options(
        self,
        request: main_models.CreateIngressRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIngressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.cert_id):
            query['CertId'] = request.cert_id
        if not DaraCore.is_null(request.cert_ids):
            query['CertIds'] = request.cert_ids
        if not DaraCore.is_null(request.cors_config):
            query['CorsConfig'] = request.cors_config
        if not DaraCore.is_null(request.default_rule):
            query['DefaultRule'] = request.default_rule
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_gzip):
            query['EnableGzip'] = request.enable_gzip
        if not DaraCore.is_null(request.enable_xforwarded_for):
            query['EnableXForwardedFor'] = request.enable_xforwarded_for
        if not DaraCore.is_null(request.enable_xforwarded_for_client_src_port):
            query['EnableXForwardedForClientSrcPort'] = request.enable_xforwarded_for_client_src_port
        if not DaraCore.is_null(request.enable_xforwarded_for_proto):
            query['EnableXForwardedForProto'] = request.enable_xforwarded_for_proto
        if not DaraCore.is_null(request.enable_xforwarded_for_slb_id):
            query['EnableXForwardedForSlbId'] = request.enable_xforwarded_for_slb_id
        if not DaraCore.is_null(request.enable_xforwarded_for_slb_port):
            query['EnableXForwardedForSlbPort'] = request.enable_xforwarded_for_slb_port
        if not DaraCore.is_null(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not DaraCore.is_null(request.load_balance_type):
            query['LoadBalanceType'] = request.load_balance_type
        if not DaraCore.is_null(request.load_balancer_edition):
            query['LoadBalancerEdition'] = request.load_balancer_edition
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not DaraCore.is_null(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not DaraCore.is_null(request.slb_id):
            query['SlbId'] = request.slb_id
        if not DaraCore.is_null(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        body = {}
        if not DaraCore.is_null(request.rules):
            body['Rules'] = request.rules
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIngress',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/ingress/Ingress',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIngressResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ingress_with_options_async(
        self,
        request: main_models.CreateIngressRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIngressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.cert_id):
            query['CertId'] = request.cert_id
        if not DaraCore.is_null(request.cert_ids):
            query['CertIds'] = request.cert_ids
        if not DaraCore.is_null(request.cors_config):
            query['CorsConfig'] = request.cors_config
        if not DaraCore.is_null(request.default_rule):
            query['DefaultRule'] = request.default_rule
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_gzip):
            query['EnableGzip'] = request.enable_gzip
        if not DaraCore.is_null(request.enable_xforwarded_for):
            query['EnableXForwardedFor'] = request.enable_xforwarded_for
        if not DaraCore.is_null(request.enable_xforwarded_for_client_src_port):
            query['EnableXForwardedForClientSrcPort'] = request.enable_xforwarded_for_client_src_port
        if not DaraCore.is_null(request.enable_xforwarded_for_proto):
            query['EnableXForwardedForProto'] = request.enable_xforwarded_for_proto
        if not DaraCore.is_null(request.enable_xforwarded_for_slb_id):
            query['EnableXForwardedForSlbId'] = request.enable_xforwarded_for_slb_id
        if not DaraCore.is_null(request.enable_xforwarded_for_slb_port):
            query['EnableXForwardedForSlbPort'] = request.enable_xforwarded_for_slb_port
        if not DaraCore.is_null(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not DaraCore.is_null(request.load_balance_type):
            query['LoadBalanceType'] = request.load_balance_type
        if not DaraCore.is_null(request.load_balancer_edition):
            query['LoadBalancerEdition'] = request.load_balancer_edition
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not DaraCore.is_null(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not DaraCore.is_null(request.slb_id):
            query['SlbId'] = request.slb_id
        if not DaraCore.is_null(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        body = {}
        if not DaraCore.is_null(request.rules):
            body['Rules'] = request.rules
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIngress',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/ingress/Ingress',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIngressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ingress(
        self,
        request: main_models.CreateIngressRequest,
    ) -> main_models.CreateIngressResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_ingress_with_options(request, headers, runtime)

    async def create_ingress_async(
        self,
        request: main_models.CreateIngressRequest,
    ) -> main_models.CreateIngressResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_ingress_with_options_async(request, headers, runtime)

    def create_job_with_options(
        self,
        request: main_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not DaraCore.is_null(request.app_description):
            query['AppDescription'] = request.app_description
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.auto_config):
            query['AutoConfig'] = request.auto_config
        if not DaraCore.is_null(request.backoff_limit):
            query['BackoffLimit'] = request.backoff_limit
        if not DaraCore.is_null(request.best_effort_type):
            query['BestEffortType'] = request.best_effort_type
        if not DaraCore.is_null(request.command):
            query['Command'] = request.command
        if not DaraCore.is_null(request.command_args):
            query['CommandArgs'] = request.command_args
        if not DaraCore.is_null(request.concurrency_policy):
            query['ConcurrencyPolicy'] = request.concurrency_policy
        if not DaraCore.is_null(request.cpu):
            query['Cpu'] = request.cpu
        if not DaraCore.is_null(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not DaraCore.is_null(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not DaraCore.is_null(request.envs):
            query['Envs'] = request.envs
        if not DaraCore.is_null(request.image_pull_secrets):
            query['ImagePullSecrets'] = request.image_pull_secrets
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not DaraCore.is_null(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not DaraCore.is_null(request.jdk):
            query['Jdk'] = request.jdk
        if not DaraCore.is_null(request.memory):
            query['Memory'] = request.memory
        if not DaraCore.is_null(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not DaraCore.is_null(request.mount_host):
            query['MountHost'] = request.mount_host
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.nas_configs):
            query['NasConfigs'] = request.nas_configs
        if not DaraCore.is_null(request.nas_id):
            query['NasId'] = request.nas_id
        if not DaraCore.is_null(request.package_type):
            query['PackageType'] = request.package_type
        if not DaraCore.is_null(request.package_url):
            query['PackageUrl'] = request.package_url
        if not DaraCore.is_null(request.package_version):
            query['PackageVersion'] = request.package_version
        if not DaraCore.is_null(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not DaraCore.is_null(request.post_start):
            query['PostStart'] = request.post_start
        if not DaraCore.is_null(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not DaraCore.is_null(request.programming_language):
            query['ProgrammingLanguage'] = request.programming_language
        if not DaraCore.is_null(request.python):
            query['Python'] = request.python
        if not DaraCore.is_null(request.python_modules):
            query['PythonModules'] = request.python_modules
        if not DaraCore.is_null(request.ref_app_id):
            query['RefAppId'] = request.ref_app_id
        if not DaraCore.is_null(request.replicas):
            query['Replicas'] = request.replicas
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.slice):
            query['Slice'] = request.slice
        if not DaraCore.is_null(request.slice_envs):
            query['SliceEnvs'] = request.slice_envs
        if not DaraCore.is_null(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not DaraCore.is_null(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        if not DaraCore.is_null(request.timezone):
            query['Timezone'] = request.timezone
        if not DaraCore.is_null(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not DaraCore.is_null(request.trigger_config):
            query['TriggerConfig'] = request.trigger_config
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not DaraCore.is_null(request.web_container):
            query['WebContainer'] = request.web_container
        if not DaraCore.is_null(request.workload):
            query['Workload'] = request.workload
        body = {}
        if not DaraCore.is_null(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not DaraCore.is_null(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not DaraCore.is_null(request.enable_image_accl):
            body['EnableImageAccl'] = request.enable_image_accl
        if not DaraCore.is_null(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not DaraCore.is_null(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not DaraCore.is_null(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not DaraCore.is_null(request.php_config):
            body['PhpConfig'] = request.php_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateJob',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/job/createJob',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_with_options_async(
        self,
        request: main_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not DaraCore.is_null(request.app_description):
            query['AppDescription'] = request.app_description
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.auto_config):
            query['AutoConfig'] = request.auto_config
        if not DaraCore.is_null(request.backoff_limit):
            query['BackoffLimit'] = request.backoff_limit
        if not DaraCore.is_null(request.best_effort_type):
            query['BestEffortType'] = request.best_effort_type
        if not DaraCore.is_null(request.command):
            query['Command'] = request.command
        if not DaraCore.is_null(request.command_args):
            query['CommandArgs'] = request.command_args
        if not DaraCore.is_null(request.concurrency_policy):
            query['ConcurrencyPolicy'] = request.concurrency_policy
        if not DaraCore.is_null(request.cpu):
            query['Cpu'] = request.cpu
        if not DaraCore.is_null(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not DaraCore.is_null(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not DaraCore.is_null(request.envs):
            query['Envs'] = request.envs
        if not DaraCore.is_null(request.image_pull_secrets):
            query['ImagePullSecrets'] = request.image_pull_secrets
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not DaraCore.is_null(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not DaraCore.is_null(request.jdk):
            query['Jdk'] = request.jdk
        if not DaraCore.is_null(request.memory):
            query['Memory'] = request.memory
        if not DaraCore.is_null(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not DaraCore.is_null(request.mount_host):
            query['MountHost'] = request.mount_host
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.nas_configs):
            query['NasConfigs'] = request.nas_configs
        if not DaraCore.is_null(request.nas_id):
            query['NasId'] = request.nas_id
        if not DaraCore.is_null(request.package_type):
            query['PackageType'] = request.package_type
        if not DaraCore.is_null(request.package_url):
            query['PackageUrl'] = request.package_url
        if not DaraCore.is_null(request.package_version):
            query['PackageVersion'] = request.package_version
        if not DaraCore.is_null(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not DaraCore.is_null(request.post_start):
            query['PostStart'] = request.post_start
        if not DaraCore.is_null(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not DaraCore.is_null(request.programming_language):
            query['ProgrammingLanguage'] = request.programming_language
        if not DaraCore.is_null(request.python):
            query['Python'] = request.python
        if not DaraCore.is_null(request.python_modules):
            query['PythonModules'] = request.python_modules
        if not DaraCore.is_null(request.ref_app_id):
            query['RefAppId'] = request.ref_app_id
        if not DaraCore.is_null(request.replicas):
            query['Replicas'] = request.replicas
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.slice):
            query['Slice'] = request.slice
        if not DaraCore.is_null(request.slice_envs):
            query['SliceEnvs'] = request.slice_envs
        if not DaraCore.is_null(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not DaraCore.is_null(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        if not DaraCore.is_null(request.timezone):
            query['Timezone'] = request.timezone
        if not DaraCore.is_null(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not DaraCore.is_null(request.trigger_config):
            query['TriggerConfig'] = request.trigger_config
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not DaraCore.is_null(request.web_container):
            query['WebContainer'] = request.web_container
        if not DaraCore.is_null(request.workload):
            query['Workload'] = request.workload
        body = {}
        if not DaraCore.is_null(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not DaraCore.is_null(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not DaraCore.is_null(request.enable_image_accl):
            body['EnableImageAccl'] = request.enable_image_accl
        if not DaraCore.is_null(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not DaraCore.is_null(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not DaraCore.is_null(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not DaraCore.is_null(request.php_config):
            body['PhpConfig'] = request.php_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateJob',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/job/createJob',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job(
        self,
        request: main_models.CreateJobRequest,
    ) -> main_models.CreateJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_job_with_options(request, headers, runtime)

    async def create_job_async(
        self,
        request: main_models.CreateJobRequest,
    ) -> main_models.CreateJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_job_with_options_async(request, headers, runtime)

    def create_namespace_with_options(
        self,
        request: main_models.CreateNamespaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_micro_registration):
            query['EnableMicroRegistration'] = request.enable_micro_registration
        if not DaraCore.is_null(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not DaraCore.is_null(request.namespace_description):
            query['NamespaceDescription'] = request.namespace_description
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNamespace',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/paas/namespace',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_namespace_with_options_async(
        self,
        request: main_models.CreateNamespaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_micro_registration):
            query['EnableMicroRegistration'] = request.enable_micro_registration
        if not DaraCore.is_null(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not DaraCore.is_null(request.namespace_description):
            query['NamespaceDescription'] = request.namespace_description
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNamespace',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/paas/namespace',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_namespace(
        self,
        request: main_models.CreateNamespaceRequest,
    ) -> main_models.CreateNamespaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_namespace_with_options(request, headers, runtime)

    async def create_namespace_async(
        self,
        request: main_models.CreateNamespaceRequest,
    ) -> main_models.CreateNamespaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_namespace_with_options_async(request, headers, runtime)

    def create_or_update_swimming_lane_with_options(
        self,
        tmp_req: main_models.CreateOrUpdateSwimmingLaneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrUpdateSwimmingLaneResponse:
        tmp_req.validate()
        request = main_models.CreateOrUpdateSwimmingLaneShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.app_entry_rule):
            request.app_entry_rule_shrink = Utils.array_to_string_with_specified_style(tmp_req.app_entry_rule, 'AppEntryRule', 'json')
        if not DaraCore.is_null(tmp_req.mse_gateway_entry_rule):
            request.mse_gateway_entry_rule_shrink = Utils.array_to_string_with_specified_style(tmp_req.mse_gateway_entry_rule, 'MseGatewayEntryRule', 'json')
        query = {}
        if not DaraCore.is_null(request.app_entry_rule_shrink):
            query['AppEntryRule'] = request.app_entry_rule_shrink
        if not DaraCore.is_null(request.canary_model):
            query['CanaryModel'] = request.canary_model
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.lane_id):
            query['LaneId'] = request.lane_id
        if not DaraCore.is_null(request.lane_name):
            query['LaneName'] = request.lane_name
        if not DaraCore.is_null(request.lane_tag):
            query['LaneTag'] = request.lane_tag
        if not DaraCore.is_null(request.mse_gateway_entry_rule_shrink):
            query['MseGatewayEntryRule'] = request.mse_gateway_entry_rule_shrink
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrUpdateSwimmingLane',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/cas/gray/createOrUpdateSwimmingLane',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrUpdateSwimmingLaneResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_or_update_swimming_lane_with_options_async(
        self,
        tmp_req: main_models.CreateOrUpdateSwimmingLaneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrUpdateSwimmingLaneResponse:
        tmp_req.validate()
        request = main_models.CreateOrUpdateSwimmingLaneShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.app_entry_rule):
            request.app_entry_rule_shrink = Utils.array_to_string_with_specified_style(tmp_req.app_entry_rule, 'AppEntryRule', 'json')
        if not DaraCore.is_null(tmp_req.mse_gateway_entry_rule):
            request.mse_gateway_entry_rule_shrink = Utils.array_to_string_with_specified_style(tmp_req.mse_gateway_entry_rule, 'MseGatewayEntryRule', 'json')
        query = {}
        if not DaraCore.is_null(request.app_entry_rule_shrink):
            query['AppEntryRule'] = request.app_entry_rule_shrink
        if not DaraCore.is_null(request.canary_model):
            query['CanaryModel'] = request.canary_model
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.lane_id):
            query['LaneId'] = request.lane_id
        if not DaraCore.is_null(request.lane_name):
            query['LaneName'] = request.lane_name
        if not DaraCore.is_null(request.lane_tag):
            query['LaneTag'] = request.lane_tag
        if not DaraCore.is_null(request.mse_gateway_entry_rule_shrink):
            query['MseGatewayEntryRule'] = request.mse_gateway_entry_rule_shrink
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrUpdateSwimmingLane',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/cas/gray/createOrUpdateSwimmingLane',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrUpdateSwimmingLaneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_or_update_swimming_lane(
        self,
        request: main_models.CreateOrUpdateSwimmingLaneRequest,
    ) -> main_models.CreateOrUpdateSwimmingLaneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_or_update_swimming_lane_with_options(request, headers, runtime)

    async def create_or_update_swimming_lane_async(
        self,
        request: main_models.CreateOrUpdateSwimmingLaneRequest,
    ) -> main_models.CreateOrUpdateSwimmingLaneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_or_update_swimming_lane_with_options_async(request, headers, runtime)

    def create_or_update_swimming_lane_group_with_options(
        self,
        tmp_req: main_models.CreateOrUpdateSwimmingLaneGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrUpdateSwimmingLaneGroupResponse:
        tmp_req.validate()
        request = main_models.CreateOrUpdateSwimmingLaneGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.app_ids):
            request.app_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.app_ids, 'AppIds', 'json')
        query = {}
        if not DaraCore.is_null(request.app_ids_shrink):
            query['AppIds'] = request.app_ids_shrink
        if not DaraCore.is_null(request.entry_app_id):
            query['EntryAppId'] = request.entry_app_id
        if not DaraCore.is_null(request.entry_app_type):
            query['EntryAppType'] = request.entry_app_type
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.swim_version):
            query['SwimVersion'] = request.swim_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrUpdateSwimmingLaneGroup',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/cas/gray/createOrUpdateSwimmingLaneGroup',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrUpdateSwimmingLaneGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_or_update_swimming_lane_group_with_options_async(
        self,
        tmp_req: main_models.CreateOrUpdateSwimmingLaneGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrUpdateSwimmingLaneGroupResponse:
        tmp_req.validate()
        request = main_models.CreateOrUpdateSwimmingLaneGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.app_ids):
            request.app_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.app_ids, 'AppIds', 'json')
        query = {}
        if not DaraCore.is_null(request.app_ids_shrink):
            query['AppIds'] = request.app_ids_shrink
        if not DaraCore.is_null(request.entry_app_id):
            query['EntryAppId'] = request.entry_app_id
        if not DaraCore.is_null(request.entry_app_type):
            query['EntryAppType'] = request.entry_app_type
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.swim_version):
            query['SwimVersion'] = request.swim_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrUpdateSwimmingLaneGroup',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/cas/gray/createOrUpdateSwimmingLaneGroup',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrUpdateSwimmingLaneGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_or_update_swimming_lane_group(
        self,
        request: main_models.CreateOrUpdateSwimmingLaneGroupRequest,
    ) -> main_models.CreateOrUpdateSwimmingLaneGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_or_update_swimming_lane_group_with_options(request, headers, runtime)

    async def create_or_update_swimming_lane_group_async(
        self,
        request: main_models.CreateOrUpdateSwimmingLaneGroupRequest,
    ) -> main_models.CreateOrUpdateSwimmingLaneGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_or_update_swimming_lane_group_with_options_async(request, headers, runtime)

    def create_secret_with_options(
        self,
        tmp_req: main_models.CreateSecretRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecretResponse:
        tmp_req.validate()
        request = main_models.CreateSecretShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.secret_data):
            request.secret_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.secret_data, 'SecretData', 'json')
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.secret_data_shrink):
            query['SecretData'] = request.secret_data_shrink
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.secret_type):
            query['SecretType'] = request.secret_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecret',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/secret/secret',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_secret_with_options_async(
        self,
        tmp_req: main_models.CreateSecretRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecretResponse:
        tmp_req.validate()
        request = main_models.CreateSecretShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.secret_data):
            request.secret_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.secret_data, 'SecretData', 'json')
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.secret_data_shrink):
            query['SecretData'] = request.secret_data_shrink
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.secret_type):
            query['SecretType'] = request.secret_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecret',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/secret/secret',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_secret(
        self,
        request: main_models.CreateSecretRequest,
    ) -> main_models.CreateSecretResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_secret_with_options(request, headers, runtime)

    async def create_secret_async(
        self,
        request: main_models.CreateSecretRequest,
    ) -> main_models.CreateSecretResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_secret_with_options_async(request, headers, runtime)

    def create_web_application_with_options(
        self,
        request: main_models.CreateWebApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateWebApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWebApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/applications',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWebApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_web_application_with_options_async(
        self,
        request: main_models.CreateWebApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateWebApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWebApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/applications',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWebApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_web_application(
        self,
        request: main_models.CreateWebApplicationRequest,
    ) -> main_models.CreateWebApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_web_application_with_options(request, headers, runtime)

    async def create_web_application_async(
        self,
        request: main_models.CreateWebApplicationRequest,
    ) -> main_models.CreateWebApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_web_application_with_options_async(request, headers, runtime)

    def create_web_custom_domain_with_options(
        self,
        request: main_models.CreateWebCustomDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateWebCustomDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWebCustomDomain',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/custom-domains',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWebCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_web_custom_domain_with_options_async(
        self,
        request: main_models.CreateWebCustomDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateWebCustomDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWebCustomDomain',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/custom-domains',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWebCustomDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_web_custom_domain(
        self,
        request: main_models.CreateWebCustomDomainRequest,
    ) -> main_models.CreateWebCustomDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_web_custom_domain_with_options(request, headers, runtime)

    async def create_web_custom_domain_async(
        self,
        request: main_models.CreateWebCustomDomainRequest,
    ) -> main_models.CreateWebCustomDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_web_custom_domain_with_options_async(request, headers, runtime)

    def delete_application_with_options(
        self,
        request: main_models.DeleteApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/deleteApplication',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_with_options_async(
        self,
        request: main_models.DeleteApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/deleteApplication',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application(
        self,
        request: main_models.DeleteApplicationRequest,
    ) -> main_models.DeleteApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_application_with_options(request, headers, runtime)

    async def delete_application_async(
        self,
        request: main_models.DeleteApplicationRequest,
    ) -> main_models.DeleteApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_application_with_options_async(request, headers, runtime)

    def delete_application_scaling_rule_with_options(
        self,
        request: main_models.DeleteApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplicationScalingRule',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/scale/applicationScalingRule',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_scaling_rule_with_options_async(
        self,
        request: main_models.DeleteApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplicationScalingRule',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/scale/applicationScalingRule',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application_scaling_rule(
        self,
        request: main_models.DeleteApplicationScalingRuleRequest,
    ) -> main_models.DeleteApplicationScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_application_scaling_rule_with_options(request, headers, runtime)

    async def delete_application_scaling_rule_async(
        self,
        request: main_models.DeleteApplicationScalingRuleRequest,
    ) -> main_models.DeleteApplicationScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_application_scaling_rule_with_options_async(request, headers, runtime)

    def delete_config_map_with_options(
        self,
        request: main_models.DeleteConfigMapRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConfigMapResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_map_id):
            query['ConfigMapId'] = request.config_map_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConfigMap',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/configmap/configMap',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConfigMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_config_map_with_options_async(
        self,
        request: main_models.DeleteConfigMapRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConfigMapResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_map_id):
            query['ConfigMapId'] = request.config_map_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConfigMap',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/configmap/configMap',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConfigMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_config_map(
        self,
        request: main_models.DeleteConfigMapRequest,
    ) -> main_models.DeleteConfigMapResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_config_map_with_options(request, headers, runtime)

    async def delete_config_map_async(
        self,
        request: main_models.DeleteConfigMapRequest,
    ) -> main_models.DeleteConfigMapResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_config_map_with_options_async(request, headers, runtime)

    def delete_grey_tag_route_with_options(
        self,
        request: main_models.DeleteGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGreyTagRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.grey_tag_route_id):
            query['GreyTagRouteId'] = request.grey_tag_route_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGreyTagRoute',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/tagroute/greyTagRoute',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGreyTagRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_grey_tag_route_with_options_async(
        self,
        request: main_models.DeleteGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGreyTagRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.grey_tag_route_id):
            query['GreyTagRouteId'] = request.grey_tag_route_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGreyTagRoute',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/tagroute/greyTagRoute',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGreyTagRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_grey_tag_route(
        self,
        request: main_models.DeleteGreyTagRouteRequest,
    ) -> main_models.DeleteGreyTagRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_grey_tag_route_with_options(request, headers, runtime)

    async def delete_grey_tag_route_async(
        self,
        request: main_models.DeleteGreyTagRouteRequest,
    ) -> main_models.DeleteGreyTagRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_grey_tag_route_with_options_async(request, headers, runtime)

    def delete_history_job_with_options(
        self,
        request: main_models.DeleteHistoryJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHistoryJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHistoryJob',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/job/deleteHistoryJob',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHistoryJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_history_job_with_options_async(
        self,
        request: main_models.DeleteHistoryJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHistoryJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHistoryJob',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/job/deleteHistoryJob',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHistoryJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_history_job(
        self,
        request: main_models.DeleteHistoryJobRequest,
    ) -> main_models.DeleteHistoryJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_history_job_with_options(request, headers, runtime)

    async def delete_history_job_async(
        self,
        request: main_models.DeleteHistoryJobRequest,
    ) -> main_models.DeleteHistoryJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_history_job_with_options_async(request, headers, runtime)

    def delete_ingress_with_options(
        self,
        request: main_models.DeleteIngressRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIngressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ingress_id):
            query['IngressId'] = request.ingress_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIngress',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/ingress/Ingress',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIngressResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ingress_with_options_async(
        self,
        request: main_models.DeleteIngressRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIngressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ingress_id):
            query['IngressId'] = request.ingress_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIngress',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/ingress/Ingress',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIngressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ingress(
        self,
        request: main_models.DeleteIngressRequest,
    ) -> main_models.DeleteIngressResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_ingress_with_options(request, headers, runtime)

    async def delete_ingress_async(
        self,
        request: main_models.DeleteIngressRequest,
    ) -> main_models.DeleteIngressResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_ingress_with_options_async(request, headers, runtime)

    def delete_instances_with_options(
        self,
        request: main_models.DeleteInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstances',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/deleteInstances',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instances_with_options_async(
        self,
        request: main_models.DeleteInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstances',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/deleteInstances',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instances(
        self,
        request: main_models.DeleteInstancesRequest,
    ) -> main_models.DeleteInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_instances_with_options(request, headers, runtime)

    async def delete_instances_async(
        self,
        request: main_models.DeleteInstancesRequest,
    ) -> main_models.DeleteInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_instances_with_options_async(request, headers, runtime)

    def delete_job_with_options(
        self,
        request: main_models.DeleteJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteJob',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/job/deleteJob',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_job_with_options_async(
        self,
        request: main_models.DeleteJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteJob',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/job/deleteJob',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_job(
        self,
        request: main_models.DeleteJobRequest,
    ) -> main_models.DeleteJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_job_with_options(request, headers, runtime)

    async def delete_job_async(
        self,
        request: main_models.DeleteJobRequest,
    ) -> main_models.DeleteJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_job_with_options_async(request, headers, runtime)

    def delete_namespace_with_options(
        self,
        request: main_models.DeleteNamespaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNamespace',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/paas/namespace',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_namespace_with_options_async(
        self,
        request: main_models.DeleteNamespaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNamespace',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/paas/namespace',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_namespace(
        self,
        request: main_models.DeleteNamespaceRequest,
    ) -> main_models.DeleteNamespaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_namespace_with_options(request, headers, runtime)

    async def delete_namespace_async(
        self,
        request: main_models.DeleteNamespaceRequest,
    ) -> main_models.DeleteNamespaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_namespace_with_options_async(request, headers, runtime)

    def delete_secret_with_options(
        self,
        request: main_models.DeleteSecretRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecret',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/secret/secret',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_secret_with_options_async(
        self,
        request: main_models.DeleteSecretRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecret',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/secret/secret',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_secret(
        self,
        request: main_models.DeleteSecretRequest,
    ) -> main_models.DeleteSecretResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_secret_with_options(request, headers, runtime)

    async def delete_secret_async(
        self,
        request: main_models.DeleteSecretRequest,
    ) -> main_models.DeleteSecretResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_secret_with_options_async(request, headers, runtime)

    def delete_swimming_lane_group_with_options(
        self,
        request: main_models.DeleteSwimmingLaneGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSwimmingLaneGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSwimmingLaneGroup',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/cas/gray/deleteSwimmingLaneGroup',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSwimmingLaneGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_swimming_lane_group_with_options_async(
        self,
        request: main_models.DeleteSwimmingLaneGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSwimmingLaneGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSwimmingLaneGroup',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/cas/gray/deleteSwimmingLaneGroup',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSwimmingLaneGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_swimming_lane_group(
        self,
        request: main_models.DeleteSwimmingLaneGroupRequest,
    ) -> main_models.DeleteSwimmingLaneGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_swimming_lane_group_with_options(request, headers, runtime)

    async def delete_swimming_lane_group_async(
        self,
        request: main_models.DeleteSwimmingLaneGroupRequest,
    ) -> main_models.DeleteSwimmingLaneGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_swimming_lane_group_with_options_async(request, headers, runtime)

    def delete_web_application_with_options(
        self,
        application_id: str,
        request: main_models.DeleteWebApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWebApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWebApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/applications/{DaraURL.percent_encode(application_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWebApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_web_application_with_options_async(
        self,
        application_id: str,
        request: main_models.DeleteWebApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWebApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWebApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/applications/{DaraURL.percent_encode(application_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWebApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_web_application(
        self,
        application_id: str,
        request: main_models.DeleteWebApplicationRequest,
    ) -> main_models.DeleteWebApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_web_application_with_options(application_id, request, headers, runtime)

    async def delete_web_application_async(
        self,
        application_id: str,
        request: main_models.DeleteWebApplicationRequest,
    ) -> main_models.DeleteWebApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_web_application_with_options_async(application_id, request, headers, runtime)

    def delete_web_application_revision_with_options(
        self,
        application_id: str,
        revision_id: str,
        request: main_models.DeleteWebApplicationRevisionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWebApplicationRevisionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWebApplicationRevision',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/application-revisions/{DaraURL.percent_encode(application_id)}/revisions/{DaraURL.percent_encode(revision_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWebApplicationRevisionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_web_application_revision_with_options_async(
        self,
        application_id: str,
        revision_id: str,
        request: main_models.DeleteWebApplicationRevisionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWebApplicationRevisionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWebApplicationRevision',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/application-revisions/{DaraURL.percent_encode(application_id)}/revisions/{DaraURL.percent_encode(revision_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWebApplicationRevisionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_web_application_revision(
        self,
        application_id: str,
        revision_id: str,
        request: main_models.DeleteWebApplicationRevisionRequest,
    ) -> main_models.DeleteWebApplicationRevisionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_web_application_revision_with_options(application_id, revision_id, request, headers, runtime)

    async def delete_web_application_revision_async(
        self,
        application_id: str,
        revision_id: str,
        request: main_models.DeleteWebApplicationRevisionRequest,
    ) -> main_models.DeleteWebApplicationRevisionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_web_application_revision_with_options_async(application_id, revision_id, request, headers, runtime)

    def delete_web_custom_domain_with_options(
        self,
        domain_name: str,
        request: main_models.DeleteWebCustomDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWebCustomDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWebCustomDomain',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/custom-domains/{DaraURL.percent_encode(domain_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWebCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_web_custom_domain_with_options_async(
        self,
        domain_name: str,
        request: main_models.DeleteWebCustomDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWebCustomDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWebCustomDomain',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/custom-domains/{DaraURL.percent_encode(domain_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWebCustomDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_web_custom_domain(
        self,
        domain_name: str,
        request: main_models.DeleteWebCustomDomainRequest,
    ) -> main_models.DeleteWebCustomDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_web_custom_domain_with_options(domain_name, request, headers, runtime)

    async def delete_web_custom_domain_async(
        self,
        domain_name: str,
        request: main_models.DeleteWebCustomDomainRequest,
    ) -> main_models.DeleteWebCustomDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_web_custom_domain_with_options_async(domain_name, request, headers, runtime)

    def deploy_application_with_options(
        self,
        tmp_req: main_models.DeployApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeployApplicationResponse:
        tmp_req.validate()
        request = main_models.DeployApplicationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.init_containers_config):
            request.init_containers_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.init_containers_config, 'InitContainersConfig', 'json')
        if not DaraCore.is_null(tmp_req.sidecar_containers_config):
            request.sidecar_containers_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.sidecar_containers_config, 'SidecarContainersConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not DaraCore.is_null(request.agent_version):
            query['AgentVersion'] = request.agent_version
        if not DaraCore.is_null(request.alb_ingress_readiness_gate):
            query['AlbIngressReadinessGate'] = request.alb_ingress_readiness_gate
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not DaraCore.is_null(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not DaraCore.is_null(request.change_order_desc):
            query['ChangeOrderDesc'] = request.change_order_desc
        if not DaraCore.is_null(request.command):
            query['Command'] = request.command
        if not DaraCore.is_null(request.command_args):
            query['CommandArgs'] = request.command_args
        if not DaraCore.is_null(request.cpu):
            query['Cpu'] = request.cpu
        if not DaraCore.is_null(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not DaraCore.is_null(request.custom_image_network_type):
            query['CustomImageNetworkType'] = request.custom_image_network_type
        if not DaraCore.is_null(request.deploy):
            query['Deploy'] = request.deploy
        if not DaraCore.is_null(request.dotnet):
            query['Dotnet'] = request.dotnet
        if not DaraCore.is_null(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not DaraCore.is_null(request.enable_ahas):
            query['EnableAhas'] = request.enable_ahas
        if not DaraCore.is_null(request.enable_cpu_burst):
            query['EnableCpuBurst'] = request.enable_cpu_burst
        if not DaraCore.is_null(request.enable_grey_tag_route):
            query['EnableGreyTagRoute'] = request.enable_grey_tag_route
        if not DaraCore.is_null(request.enable_namespace_agent_version):
            query['EnableNamespaceAgentVersion'] = request.enable_namespace_agent_version
        if not DaraCore.is_null(request.enable_new_arms):
            query['EnableNewArms'] = request.enable_new_arms
        if not DaraCore.is_null(request.enable_prometheus):
            query['EnablePrometheus'] = request.enable_prometheus
        if not DaraCore.is_null(request.envs):
            query['Envs'] = request.envs
        if not DaraCore.is_null(request.gpu_config):
            query['GpuConfig'] = request.gpu_config
        if not DaraCore.is_null(request.html):
            query['Html'] = request.html
        if not DaraCore.is_null(request.image_pull_secrets):
            query['ImagePullSecrets'] = request.image_pull_secrets
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not DaraCore.is_null(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not DaraCore.is_null(request.jdk):
            query['Jdk'] = request.jdk
        if not DaraCore.is_null(request.kafka_configs):
            query['KafkaConfigs'] = request.kafka_configs
        if not DaraCore.is_null(request.liveness):
            query['Liveness'] = request.liveness
        if not DaraCore.is_null(request.loki_configs):
            query['LokiConfigs'] = request.loki_configs
        if not DaraCore.is_null(request.max_surge_instance_ratio):
            query['MaxSurgeInstanceRatio'] = request.max_surge_instance_ratio
        if not DaraCore.is_null(request.max_surge_instances):
            query['MaxSurgeInstances'] = request.max_surge_instances
        if not DaraCore.is_null(request.memory):
            query['Memory'] = request.memory
        if not DaraCore.is_null(request.micro_registration):
            query['MicroRegistration'] = request.micro_registration
        if not DaraCore.is_null(request.microservice_engine_config):
            query['MicroserviceEngineConfig'] = request.microservice_engine_config
        if not DaraCore.is_null(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not DaraCore.is_null(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not DaraCore.is_null(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not DaraCore.is_null(request.mount_host):
            query['MountHost'] = request.mount_host
        if not DaraCore.is_null(request.nas_configs):
            query['NasConfigs'] = request.nas_configs
        if not DaraCore.is_null(request.nas_id):
            query['NasId'] = request.nas_id
        if not DaraCore.is_null(request.new_sae_version):
            query['NewSaeVersion'] = request.new_sae_version
        if not DaraCore.is_null(request.oidc_role_name):
            query['OidcRoleName'] = request.oidc_role_name
        if not DaraCore.is_null(request.package_type):
            query['PackageType'] = request.package_type
        if not DaraCore.is_null(request.package_url):
            query['PackageUrl'] = request.package_url
        if not DaraCore.is_null(request.package_version):
            query['PackageVersion'] = request.package_version
        if not DaraCore.is_null(request.php_arms_config_location):
            query['PhpArmsConfigLocation'] = request.php_arms_config_location
        if not DaraCore.is_null(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not DaraCore.is_null(request.post_start):
            query['PostStart'] = request.post_start
        if not DaraCore.is_null(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not DaraCore.is_null(request.pvtz_discovery_svc):
            query['PvtzDiscoverySvc'] = request.pvtz_discovery_svc
        if not DaraCore.is_null(request.python):
            query['Python'] = request.python
        if not DaraCore.is_null(request.python_modules):
            query['PythonModules'] = request.python_modules
        if not DaraCore.is_null(request.readiness):
            query['Readiness'] = request.readiness
        if not DaraCore.is_null(request.replicas):
            query['Replicas'] = request.replicas
        if not DaraCore.is_null(request.secret_mount_desc):
            query['SecretMountDesc'] = request.secret_mount_desc
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not DaraCore.is_null(request.sls_log_env_tags):
            query['SlsLogEnvTags'] = request.sls_log_env_tags
        if not DaraCore.is_null(request.startup_probe):
            query['StartupProbe'] = request.startup_probe
        if not DaraCore.is_null(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not DaraCore.is_null(request.timezone):
            query['Timezone'] = request.timezone
        if not DaraCore.is_null(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not DaraCore.is_null(request.update_strategy):
            query['UpdateStrategy'] = request.update_strategy
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not DaraCore.is_null(request.web_container):
            query['WebContainer'] = request.web_container
        body = {}
        if not DaraCore.is_null(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not DaraCore.is_null(request.associate_eip):
            body['AssociateEip'] = request.associate_eip
        if not DaraCore.is_null(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not DaraCore.is_null(request.empty_dir_desc):
            body['EmptyDirDesc'] = request.empty_dir_desc
        if not DaraCore.is_null(request.enable_sidecar_resource_isolated):
            body['EnableSidecarResourceIsolated'] = request.enable_sidecar_resource_isolated
        if not DaraCore.is_null(request.init_containers_config_shrink):
            body['InitContainersConfig'] = request.init_containers_config_shrink
        if not DaraCore.is_null(request.micro_registration_config):
            body['MicroRegistrationConfig'] = request.micro_registration_config
        if not DaraCore.is_null(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not DaraCore.is_null(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not DaraCore.is_null(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not DaraCore.is_null(request.php):
            body['Php'] = request.php
        if not DaraCore.is_null(request.php_config):
            body['PhpConfig'] = request.php_config
        if not DaraCore.is_null(request.service_tags):
            body['ServiceTags'] = request.service_tags
        if not DaraCore.is_null(request.sidecar_containers_config_shrink):
            body['SidecarContainersConfig'] = request.sidecar_containers_config_shrink
        if not DaraCore.is_null(request.swimlane_pvtz_discovery_svc):
            body['SwimlanePvtzDiscoverySvc'] = request.swimlane_pvtz_discovery_svc
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeployApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/deployApplication',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_application_with_options_async(
        self,
        tmp_req: main_models.DeployApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeployApplicationResponse:
        tmp_req.validate()
        request = main_models.DeployApplicationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.init_containers_config):
            request.init_containers_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.init_containers_config, 'InitContainersConfig', 'json')
        if not DaraCore.is_null(tmp_req.sidecar_containers_config):
            request.sidecar_containers_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.sidecar_containers_config, 'SidecarContainersConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not DaraCore.is_null(request.agent_version):
            query['AgentVersion'] = request.agent_version
        if not DaraCore.is_null(request.alb_ingress_readiness_gate):
            query['AlbIngressReadinessGate'] = request.alb_ingress_readiness_gate
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not DaraCore.is_null(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not DaraCore.is_null(request.change_order_desc):
            query['ChangeOrderDesc'] = request.change_order_desc
        if not DaraCore.is_null(request.command):
            query['Command'] = request.command
        if not DaraCore.is_null(request.command_args):
            query['CommandArgs'] = request.command_args
        if not DaraCore.is_null(request.cpu):
            query['Cpu'] = request.cpu
        if not DaraCore.is_null(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not DaraCore.is_null(request.custom_image_network_type):
            query['CustomImageNetworkType'] = request.custom_image_network_type
        if not DaraCore.is_null(request.deploy):
            query['Deploy'] = request.deploy
        if not DaraCore.is_null(request.dotnet):
            query['Dotnet'] = request.dotnet
        if not DaraCore.is_null(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not DaraCore.is_null(request.enable_ahas):
            query['EnableAhas'] = request.enable_ahas
        if not DaraCore.is_null(request.enable_cpu_burst):
            query['EnableCpuBurst'] = request.enable_cpu_burst
        if not DaraCore.is_null(request.enable_grey_tag_route):
            query['EnableGreyTagRoute'] = request.enable_grey_tag_route
        if not DaraCore.is_null(request.enable_namespace_agent_version):
            query['EnableNamespaceAgentVersion'] = request.enable_namespace_agent_version
        if not DaraCore.is_null(request.enable_new_arms):
            query['EnableNewArms'] = request.enable_new_arms
        if not DaraCore.is_null(request.enable_prometheus):
            query['EnablePrometheus'] = request.enable_prometheus
        if not DaraCore.is_null(request.envs):
            query['Envs'] = request.envs
        if not DaraCore.is_null(request.gpu_config):
            query['GpuConfig'] = request.gpu_config
        if not DaraCore.is_null(request.html):
            query['Html'] = request.html
        if not DaraCore.is_null(request.image_pull_secrets):
            query['ImagePullSecrets'] = request.image_pull_secrets
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not DaraCore.is_null(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not DaraCore.is_null(request.jdk):
            query['Jdk'] = request.jdk
        if not DaraCore.is_null(request.kafka_configs):
            query['KafkaConfigs'] = request.kafka_configs
        if not DaraCore.is_null(request.liveness):
            query['Liveness'] = request.liveness
        if not DaraCore.is_null(request.loki_configs):
            query['LokiConfigs'] = request.loki_configs
        if not DaraCore.is_null(request.max_surge_instance_ratio):
            query['MaxSurgeInstanceRatio'] = request.max_surge_instance_ratio
        if not DaraCore.is_null(request.max_surge_instances):
            query['MaxSurgeInstances'] = request.max_surge_instances
        if not DaraCore.is_null(request.memory):
            query['Memory'] = request.memory
        if not DaraCore.is_null(request.micro_registration):
            query['MicroRegistration'] = request.micro_registration
        if not DaraCore.is_null(request.microservice_engine_config):
            query['MicroserviceEngineConfig'] = request.microservice_engine_config
        if not DaraCore.is_null(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not DaraCore.is_null(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not DaraCore.is_null(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not DaraCore.is_null(request.mount_host):
            query['MountHost'] = request.mount_host
        if not DaraCore.is_null(request.nas_configs):
            query['NasConfigs'] = request.nas_configs
        if not DaraCore.is_null(request.nas_id):
            query['NasId'] = request.nas_id
        if not DaraCore.is_null(request.new_sae_version):
            query['NewSaeVersion'] = request.new_sae_version
        if not DaraCore.is_null(request.oidc_role_name):
            query['OidcRoleName'] = request.oidc_role_name
        if not DaraCore.is_null(request.package_type):
            query['PackageType'] = request.package_type
        if not DaraCore.is_null(request.package_url):
            query['PackageUrl'] = request.package_url
        if not DaraCore.is_null(request.package_version):
            query['PackageVersion'] = request.package_version
        if not DaraCore.is_null(request.php_arms_config_location):
            query['PhpArmsConfigLocation'] = request.php_arms_config_location
        if not DaraCore.is_null(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not DaraCore.is_null(request.post_start):
            query['PostStart'] = request.post_start
        if not DaraCore.is_null(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not DaraCore.is_null(request.pvtz_discovery_svc):
            query['PvtzDiscoverySvc'] = request.pvtz_discovery_svc
        if not DaraCore.is_null(request.python):
            query['Python'] = request.python
        if not DaraCore.is_null(request.python_modules):
            query['PythonModules'] = request.python_modules
        if not DaraCore.is_null(request.readiness):
            query['Readiness'] = request.readiness
        if not DaraCore.is_null(request.replicas):
            query['Replicas'] = request.replicas
        if not DaraCore.is_null(request.secret_mount_desc):
            query['SecretMountDesc'] = request.secret_mount_desc
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not DaraCore.is_null(request.sls_log_env_tags):
            query['SlsLogEnvTags'] = request.sls_log_env_tags
        if not DaraCore.is_null(request.startup_probe):
            query['StartupProbe'] = request.startup_probe
        if not DaraCore.is_null(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not DaraCore.is_null(request.timezone):
            query['Timezone'] = request.timezone
        if not DaraCore.is_null(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not DaraCore.is_null(request.update_strategy):
            query['UpdateStrategy'] = request.update_strategy
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not DaraCore.is_null(request.web_container):
            query['WebContainer'] = request.web_container
        body = {}
        if not DaraCore.is_null(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not DaraCore.is_null(request.associate_eip):
            body['AssociateEip'] = request.associate_eip
        if not DaraCore.is_null(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not DaraCore.is_null(request.empty_dir_desc):
            body['EmptyDirDesc'] = request.empty_dir_desc
        if not DaraCore.is_null(request.enable_sidecar_resource_isolated):
            body['EnableSidecarResourceIsolated'] = request.enable_sidecar_resource_isolated
        if not DaraCore.is_null(request.init_containers_config_shrink):
            body['InitContainersConfig'] = request.init_containers_config_shrink
        if not DaraCore.is_null(request.micro_registration_config):
            body['MicroRegistrationConfig'] = request.micro_registration_config
        if not DaraCore.is_null(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not DaraCore.is_null(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not DaraCore.is_null(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not DaraCore.is_null(request.php):
            body['Php'] = request.php
        if not DaraCore.is_null(request.php_config):
            body['PhpConfig'] = request.php_config
        if not DaraCore.is_null(request.service_tags):
            body['ServiceTags'] = request.service_tags
        if not DaraCore.is_null(request.sidecar_containers_config_shrink):
            body['SidecarContainersConfig'] = request.sidecar_containers_config_shrink
        if not DaraCore.is_null(request.swimlane_pvtz_discovery_svc):
            body['SwimlanePvtzDiscoverySvc'] = request.swimlane_pvtz_discovery_svc
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeployApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/deployApplication',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_application(
        self,
        request: main_models.DeployApplicationRequest,
    ) -> main_models.DeployApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.deploy_application_with_options(request, headers, runtime)

    async def deploy_application_async(
        self,
        request: main_models.DeployApplicationRequest,
    ) -> main_models.DeployApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.deploy_application_with_options_async(request, headers, runtime)

    def describe_app_service_detail_with_options(
        self,
        request: main_models.DescribeAppServiceDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppServiceDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.nacos_instance_id):
            query['NacosInstanceId'] = request.nacos_instance_id
        if not DaraCore.is_null(request.nacos_namespace_id):
            query['NacosNamespaceId'] = request.nacos_namespace_id
        if not DaraCore.is_null(request.service_group):
            query['ServiceGroup'] = request.service_group
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppServiceDetail',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/service/describeAppServiceDetail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppServiceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_service_detail_with_options_async(
        self,
        request: main_models.DescribeAppServiceDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppServiceDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.nacos_instance_id):
            query['NacosInstanceId'] = request.nacos_instance_id
        if not DaraCore.is_null(request.nacos_namespace_id):
            query['NacosNamespaceId'] = request.nacos_namespace_id
        if not DaraCore.is_null(request.service_group):
            query['ServiceGroup'] = request.service_group
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppServiceDetail',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/service/describeAppServiceDetail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppServiceDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_service_detail(
        self,
        request: main_models.DescribeAppServiceDetailRequest,
    ) -> main_models.DescribeAppServiceDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_app_service_detail_with_options(request, headers, runtime)

    async def describe_app_service_detail_async(
        self,
        request: main_models.DescribeAppServiceDetailRequest,
    ) -> main_models.DescribeAppServiceDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_app_service_detail_with_options_async(request, headers, runtime)

    def describe_application_config_with_options(
        self,
        request: main_models.DescribeApplicationConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationConfig',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/describeApplicationConfig',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_config_with_options_async(
        self,
        request: main_models.DescribeApplicationConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationConfig',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/describeApplicationConfig',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_config(
        self,
        request: main_models.DescribeApplicationConfigRequest,
    ) -> main_models.DescribeApplicationConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_application_config_with_options(request, headers, runtime)

    async def describe_application_config_async(
        self,
        request: main_models.DescribeApplicationConfigRequest,
    ) -> main_models.DescribeApplicationConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_application_config_with_options_async(request, headers, runtime)

    def describe_application_groups_with_options(
        self,
        request: main_models.DescribeApplicationGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationGroups',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/describeApplicationGroups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_groups_with_options_async(
        self,
        request: main_models.DescribeApplicationGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationGroups',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/describeApplicationGroups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_groups(
        self,
        request: main_models.DescribeApplicationGroupsRequest,
    ) -> main_models.DescribeApplicationGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_application_groups_with_options(request, headers, runtime)

    async def describe_application_groups_async(
        self,
        request: main_models.DescribeApplicationGroupsRequest,
    ) -> main_models.DescribeApplicationGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_application_groups_with_options_async(request, headers, runtime)

    def describe_application_image_with_options(
        self,
        request: main_models.DescribeApplicationImageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationImage',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/container/describeApplicationImage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_image_with_options_async(
        self,
        request: main_models.DescribeApplicationImageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationImage',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/container/describeApplicationImage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_image(
        self,
        request: main_models.DescribeApplicationImageRequest,
    ) -> main_models.DescribeApplicationImageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_application_image_with_options(request, headers, runtime)

    async def describe_application_image_async(
        self,
        request: main_models.DescribeApplicationImageRequest,
    ) -> main_models.DescribeApplicationImageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_application_image_with_options_async(request, headers, runtime)

    def describe_application_instances_with_options(
        self,
        request: main_models.DescribeApplicationInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.reverse):
            query['Reverse'] = request.reverse
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationInstances',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/describeApplicationInstances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_instances_with_options_async(
        self,
        request: main_models.DescribeApplicationInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.reverse):
            query['Reverse'] = request.reverse
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationInstances',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/describeApplicationInstances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_instances(
        self,
        request: main_models.DescribeApplicationInstancesRequest,
    ) -> main_models.DescribeApplicationInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_application_instances_with_options(request, headers, runtime)

    async def describe_application_instances_async(
        self,
        request: main_models.DescribeApplicationInstancesRequest,
    ) -> main_models.DescribeApplicationInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_application_instances_with_options_async(request, headers, runtime)

    def describe_application_mse_service_with_options(
        self,
        request: main_models.DescribeApplicationMseServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationMseServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.enable_ahas):
            query['EnableAhas'] = request.enable_ahas
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationMseService',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/applicationMseService',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationMseServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_mse_service_with_options_async(
        self,
        request: main_models.DescribeApplicationMseServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationMseServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.enable_ahas):
            query['EnableAhas'] = request.enable_ahas
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationMseService',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/applicationMseService',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationMseServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_mse_service(
        self,
        request: main_models.DescribeApplicationMseServiceRequest,
    ) -> main_models.DescribeApplicationMseServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_application_mse_service_with_options(request, headers, runtime)

    async def describe_application_mse_service_async(
        self,
        request: main_models.DescribeApplicationMseServiceRequest,
    ) -> main_models.DescribeApplicationMseServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_application_mse_service_with_options_async(request, headers, runtime)

    def describe_application_nlbs_with_options(
        self,
        request: main_models.DescribeApplicationNlbsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationNlbsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationNlbs',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/nlb',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationNlbsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_nlbs_with_options_async(
        self,
        request: main_models.DescribeApplicationNlbsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationNlbsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationNlbs',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/nlb',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationNlbsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_nlbs(
        self,
        request: main_models.DescribeApplicationNlbsRequest,
    ) -> main_models.DescribeApplicationNlbsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_application_nlbs_with_options(request, headers, runtime)

    async def describe_application_nlbs_async(
        self,
        request: main_models.DescribeApplicationNlbsRequest,
    ) -> main_models.DescribeApplicationNlbsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_application_nlbs_with_options_async(request, headers, runtime)

    def describe_application_scaling_rule_with_options(
        self,
        request: main_models.DescribeApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationScalingRule',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/scale/applicationScalingRule',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_scaling_rule_with_options_async(
        self,
        request: main_models.DescribeApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationScalingRule',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/scale/applicationScalingRule',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_scaling_rule(
        self,
        request: main_models.DescribeApplicationScalingRuleRequest,
    ) -> main_models.DescribeApplicationScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_application_scaling_rule_with_options(request, headers, runtime)

    async def describe_application_scaling_rule_async(
        self,
        request: main_models.DescribeApplicationScalingRuleRequest,
    ) -> main_models.DescribeApplicationScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_application_scaling_rule_with_options_async(request, headers, runtime)

    def describe_application_scaling_rules_with_options(
        self,
        request: main_models.DescribeApplicationScalingRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationScalingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationScalingRules',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/scale/applicationScalingRules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationScalingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_scaling_rules_with_options_async(
        self,
        request: main_models.DescribeApplicationScalingRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationScalingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationScalingRules',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/scale/applicationScalingRules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationScalingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_scaling_rules(
        self,
        request: main_models.DescribeApplicationScalingRulesRequest,
    ) -> main_models.DescribeApplicationScalingRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_application_scaling_rules_with_options(request, headers, runtime)

    async def describe_application_scaling_rules_async(
        self,
        request: main_models.DescribeApplicationScalingRulesRequest,
    ) -> main_models.DescribeApplicationScalingRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_application_scaling_rules_with_options_async(request, headers, runtime)

    def describe_application_slbs_with_options(
        self,
        request: main_models.DescribeApplicationSlbsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationSlbsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationSlbs',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/slb',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationSlbsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_slbs_with_options_async(
        self,
        request: main_models.DescribeApplicationSlbsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationSlbsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationSlbs',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/slb',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationSlbsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_slbs(
        self,
        request: main_models.DescribeApplicationSlbsRequest,
    ) -> main_models.DescribeApplicationSlbsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_application_slbs_with_options(request, headers, runtime)

    async def describe_application_slbs_async(
        self,
        request: main_models.DescribeApplicationSlbsRequest,
    ) -> main_models.DescribeApplicationSlbsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_application_slbs_with_options_async(request, headers, runtime)

    def describe_application_status_with_options(
        self,
        request: main_models.DescribeApplicationStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationStatus',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/describeApplicationStatus',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_status_with_options_async(
        self,
        request: main_models.DescribeApplicationStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationStatus',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/describeApplicationStatus',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_status(
        self,
        request: main_models.DescribeApplicationStatusRequest,
    ) -> main_models.DescribeApplicationStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_application_status_with_options(request, headers, runtime)

    async def describe_application_status_async(
        self,
        request: main_models.DescribeApplicationStatusRequest,
    ) -> main_models.DescribeApplicationStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_application_status_with_options_async(request, headers, runtime)

    def describe_change_order_with_options(
        self,
        request: main_models.DescribeChangeOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChangeOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChangeOrder',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/changeorder/DescribeChangeOrder',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChangeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_change_order_with_options_async(
        self,
        request: main_models.DescribeChangeOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChangeOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChangeOrder',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/changeorder/DescribeChangeOrder',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChangeOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_change_order(
        self,
        request: main_models.DescribeChangeOrderRequest,
    ) -> main_models.DescribeChangeOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_change_order_with_options(request, headers, runtime)

    async def describe_change_order_async(
        self,
        request: main_models.DescribeChangeOrderRequest,
    ) -> main_models.DescribeChangeOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_change_order_with_options_async(request, headers, runtime)

    def describe_components_with_options(
        self,
        request: main_models.DescribeComponentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeComponentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeComponents',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/resource/components',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_components_with_options_async(
        self,
        request: main_models.DescribeComponentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeComponentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeComponents',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/resource/components',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeComponentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_components(
        self,
        request: main_models.DescribeComponentsRequest,
    ) -> main_models.DescribeComponentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_components_with_options(request, headers, runtime)

    async def describe_components_async(
        self,
        request: main_models.DescribeComponentsRequest,
    ) -> main_models.DescribeComponentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_components_with_options_async(request, headers, runtime)

    def describe_config_map_with_options(
        self,
        request: main_models.DescribeConfigMapRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConfigMapResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_map_id):
            query['ConfigMapId'] = request.config_map_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConfigMap',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/configmap/configMap',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConfigMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_config_map_with_options_async(
        self,
        request: main_models.DescribeConfigMapRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConfigMapResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_map_id):
            query['ConfigMapId'] = request.config_map_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConfigMap',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/configmap/configMap',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConfigMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_config_map(
        self,
        request: main_models.DescribeConfigMapRequest,
    ) -> main_models.DescribeConfigMapResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_config_map_with_options(request, headers, runtime)

    async def describe_config_map_async(
        self,
        request: main_models.DescribeConfigMapRequest,
    ) -> main_models.DescribeConfigMapResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_config_map_with_options_async(request, headers, runtime)

    def describe_configuration_price_with_options(
        self,
        request: main_models.DescribeConfigurationPriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConfigurationPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.best_effort_type):
            query['BestEffortType'] = request.best_effort_type
        if not DaraCore.is_null(request.cpu):
            query['Cpu'] = request.cpu
        if not DaraCore.is_null(request.memory):
            query['Memory'] = request.memory
        if not DaraCore.is_null(request.new_sae_version):
            query['NewSaeVersion'] = request.new_sae_version
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.workload):
            query['Workload'] = request.workload
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConfigurationPrice',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/paas/configurationPrice',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConfigurationPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_configuration_price_with_options_async(
        self,
        request: main_models.DescribeConfigurationPriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConfigurationPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.best_effort_type):
            query['BestEffortType'] = request.best_effort_type
        if not DaraCore.is_null(request.cpu):
            query['Cpu'] = request.cpu
        if not DaraCore.is_null(request.memory):
            query['Memory'] = request.memory
        if not DaraCore.is_null(request.new_sae_version):
            query['NewSaeVersion'] = request.new_sae_version
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.workload):
            query['Workload'] = request.workload
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConfigurationPrice',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/paas/configurationPrice',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConfigurationPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_configuration_price(
        self,
        request: main_models.DescribeConfigurationPriceRequest,
    ) -> main_models.DescribeConfigurationPriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_configuration_price_with_options(request, headers, runtime)

    async def describe_configuration_price_async(
        self,
        request: main_models.DescribeConfigurationPriceRequest,
    ) -> main_models.DescribeConfigurationPriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_configuration_price_with_options_async(request, headers, runtime)

    def describe_edas_containers_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEdasContainersResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeEdasContainers',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/resource/edasContainers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEdasContainersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_edas_containers_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEdasContainersResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeEdasContainers',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/resource/edasContainers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEdasContainersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_edas_containers(self) -> main_models.DescribeEdasContainersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_edas_containers_with_options(headers, runtime)

    async def describe_edas_containers_async(self) -> main_models.DescribeEdasContainersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_edas_containers_with_options_async(headers, runtime)

    def describe_grey_tag_route_with_options(
        self,
        request: main_models.DescribeGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGreyTagRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.grey_tag_route_id):
            query['GreyTagRouteId'] = request.grey_tag_route_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGreyTagRoute',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/tagroute/greyTagRoute',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGreyTagRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_grey_tag_route_with_options_async(
        self,
        request: main_models.DescribeGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGreyTagRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.grey_tag_route_id):
            query['GreyTagRouteId'] = request.grey_tag_route_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGreyTagRoute',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/tagroute/greyTagRoute',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGreyTagRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_grey_tag_route(
        self,
        request: main_models.DescribeGreyTagRouteRequest,
    ) -> main_models.DescribeGreyTagRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_grey_tag_route_with_options(request, headers, runtime)

    async def describe_grey_tag_route_async(
        self,
        request: main_models.DescribeGreyTagRouteRequest,
    ) -> main_models.DescribeGreyTagRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_grey_tag_route_with_options_async(request, headers, runtime)

    def describe_ingress_with_options(
        self,
        request: main_models.DescribeIngressRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIngressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ingress_id):
            query['IngressId'] = request.ingress_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIngress',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/ingress/Ingress',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIngressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ingress_with_options_async(
        self,
        request: main_models.DescribeIngressRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIngressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ingress_id):
            query['IngressId'] = request.ingress_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIngress',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/ingress/Ingress',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIngressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ingress(
        self,
        request: main_models.DescribeIngressRequest,
    ) -> main_models.DescribeIngressResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_ingress_with_options(request, headers, runtime)

    async def describe_ingress_async(
        self,
        request: main_models.DescribeIngressRequest,
    ) -> main_models.DescribeIngressResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_ingress_with_options_async(request, headers, runtime)

    def describe_instance_log_with_options(
        self,
        request: main_models.DescribeInstanceLogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.container_id):
            query['ContainerId'] = request.container_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.previous):
            query['Previous'] = request.previous
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceLog',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/instance/describeInstanceLog',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_log_with_options_async(
        self,
        request: main_models.DescribeInstanceLogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.container_id):
            query['ContainerId'] = request.container_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.previous):
            query['Previous'] = request.previous
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceLog',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/instance/describeInstanceLog',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_log(
        self,
        request: main_models.DescribeInstanceLogRequest,
    ) -> main_models.DescribeInstanceLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_instance_log_with_options(request, headers, runtime)

    async def describe_instance_log_async(
        self,
        request: main_models.DescribeInstanceLogRequest,
    ) -> main_models.DescribeInstanceLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_instance_log_with_options_async(request, headers, runtime)

    def describe_instance_specifications_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceSpecificationsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceSpecifications',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/paas/quota/instanceSpecifications',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceSpecificationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_specifications_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceSpecificationsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceSpecifications',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/paas/quota/instanceSpecifications',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceSpecificationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_specifications(self) -> main_models.DescribeInstanceSpecificationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_instance_specifications_with_options(headers, runtime)

    async def describe_instance_specifications_async(self) -> main_models.DescribeInstanceSpecificationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_instance_specifications_with_options_async(headers, runtime)

    def describe_job_with_options(
        self,
        request: main_models.DescribeJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJob',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/job/describeJob',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_with_options_async(
        self,
        request: main_models.DescribeJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJob',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/job/describeJob',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job(
        self,
        request: main_models.DescribeJobRequest,
    ) -> main_models.DescribeJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_job_with_options(request, headers, runtime)

    async def describe_job_async(
        self,
        request: main_models.DescribeJobRequest,
    ) -> main_models.DescribeJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_job_with_options_async(request, headers, runtime)

    def describe_job_history_with_options(
        self,
        request: main_models.DescribeJobHistoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJobHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJobHistory',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/job/describeJobHistory',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJobHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_history_with_options_async(
        self,
        request: main_models.DescribeJobHistoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJobHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJobHistory',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/job/describeJobHistory',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJobHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job_history(
        self,
        request: main_models.DescribeJobHistoryRequest,
    ) -> main_models.DescribeJobHistoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_job_history_with_options(request, headers, runtime)

    async def describe_job_history_async(
        self,
        request: main_models.DescribeJobHistoryRequest,
    ) -> main_models.DescribeJobHistoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_job_history_with_options_async(request, headers, runtime)

    def describe_job_status_with_options(
        self,
        request: main_models.DescribeJobStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJobStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJobStatus',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/job/describeJobStatus',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_status_with_options_async(
        self,
        request: main_models.DescribeJobStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJobStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJobStatus',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/job/describeJobStatus',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJobStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job_status(
        self,
        request: main_models.DescribeJobStatusRequest,
    ) -> main_models.DescribeJobStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_job_status_with_options(request, headers, runtime)

    async def describe_job_status_async(
        self,
        request: main_models.DescribeJobStatusRequest,
    ) -> main_models.DescribeJobStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_job_status_with_options_async(request, headers, runtime)

    def describe_namespace_with_options(
        self,
        request: main_models.DescribeNamespaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNamespace',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/paas/namespace',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_namespace_with_options_async(
        self,
        request: main_models.DescribeNamespaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNamespace',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/paas/namespace',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_namespace(
        self,
        request: main_models.DescribeNamespaceRequest,
    ) -> main_models.DescribeNamespaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_namespace_with_options(request, headers, runtime)

    async def describe_namespace_async(
        self,
        request: main_models.DescribeNamespaceRequest,
    ) -> main_models.DescribeNamespaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_namespace_with_options_async(request, headers, runtime)

    def describe_namespace_list_with_options(
        self,
        request: main_models.DescribeNamespaceListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNamespaceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contain_custom):
            query['ContainCustom'] = request.contain_custom
        if not DaraCore.is_null(request.hybrid_cloud_exclude):
            query['HybridCloudExclude'] = request.hybrid_cloud_exclude
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNamespaceList',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/namespace/describeNamespaceList',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNamespaceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_namespace_list_with_options_async(
        self,
        request: main_models.DescribeNamespaceListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNamespaceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contain_custom):
            query['ContainCustom'] = request.contain_custom
        if not DaraCore.is_null(request.hybrid_cloud_exclude):
            query['HybridCloudExclude'] = request.hybrid_cloud_exclude
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNamespaceList',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/namespace/describeNamespaceList',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNamespaceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_namespace_list(
        self,
        request: main_models.DescribeNamespaceListRequest,
    ) -> main_models.DescribeNamespaceListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_namespace_list_with_options(request, headers, runtime)

    async def describe_namespace_list_async(
        self,
        request: main_models.DescribeNamespaceListRequest,
    ) -> main_models.DescribeNamespaceListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_namespace_list_with_options_async(request, headers, runtime)

    def describe_namespace_resources_with_options(
        self,
        request: main_models.DescribeNamespaceResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNamespaceResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNamespaceResources',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/namespace/describeNamespaceResources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNamespaceResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_namespace_resources_with_options_async(
        self,
        request: main_models.DescribeNamespaceResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNamespaceResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNamespaceResources',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/namespace/describeNamespaceResources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNamespaceResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_namespace_resources(
        self,
        request: main_models.DescribeNamespaceResourcesRequest,
    ) -> main_models.DescribeNamespaceResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_namespace_resources_with_options(request, headers, runtime)

    async def describe_namespace_resources_async(
        self,
        request: main_models.DescribeNamespaceResourcesRequest,
    ) -> main_models.DescribeNamespaceResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_namespace_resources_with_options_async(request, headers, runtime)

    def describe_namespaces_with_options(
        self,
        request: main_models.DescribeNamespacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNamespacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNamespaces',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/paas/namespaces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_namespaces_with_options_async(
        self,
        request: main_models.DescribeNamespacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNamespacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNamespaces',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/paas/namespaces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_namespaces(
        self,
        request: main_models.DescribeNamespacesRequest,
    ) -> main_models.DescribeNamespacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_namespaces_with_options(request, headers, runtime)

    async def describe_namespaces_async(
        self,
        request: main_models.DescribeNamespacesRequest,
    ) -> main_models.DescribeNamespacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_namespaces_with_options_async(request, headers, runtime)

    def describe_pipeline_with_options(
        self,
        request: main_models.DescribePipelineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribePipelineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePipeline',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/changeorder/DescribePipeline',
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
        request: main_models.DescribePipelineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribePipelineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePipeline',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/changeorder/DescribePipeline',
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
        request: main_models.DescribePipelineRequest,
    ) -> main_models.DescribePipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_pipeline_with_options(request, headers, runtime)

    async def describe_pipeline_async(
        self,
        request: main_models.DescribePipelineRequest,
    ) -> main_models.DescribePipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_pipeline_with_options_async(request, headers, runtime)

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
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/paas/regionConfig',
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
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/paas/regionConfig',
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

    def describe_secret_with_options(
        self,
        request: main_models.DescribeSecretRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecret',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/secret/secret',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_secret_with_options_async(
        self,
        request: main_models.DescribeSecretRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecret',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/secret/secret',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_secret(
        self,
        request: main_models.DescribeSecretRequest,
    ) -> main_models.DescribeSecretResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_secret_with_options(request, headers, runtime)

    async def describe_secret_async(
        self,
        request: main_models.DescribeSecretRequest,
    ) -> main_models.DescribeSecretResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_secret_with_options_async(request, headers, runtime)

    def describe_swimming_lane_with_options(
        self,
        request: main_models.DescribeSwimmingLaneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSwimmingLaneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.lane_id):
            query['LaneId'] = request.lane_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSwimmingLane',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/cas/gray/describeSwimmingLane',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSwimmingLaneResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_swimming_lane_with_options_async(
        self,
        request: main_models.DescribeSwimmingLaneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSwimmingLaneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.lane_id):
            query['LaneId'] = request.lane_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSwimmingLane',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/cas/gray/describeSwimmingLane',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSwimmingLaneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_swimming_lane(
        self,
        request: main_models.DescribeSwimmingLaneRequest,
    ) -> main_models.DescribeSwimmingLaneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_swimming_lane_with_options(request, headers, runtime)

    async def describe_swimming_lane_async(
        self,
        request: main_models.DescribeSwimmingLaneRequest,
    ) -> main_models.DescribeSwimmingLaneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_swimming_lane_with_options_async(request, headers, runtime)

    def describe_web_application_with_options(
        self,
        application_id: str,
        request: main_models.DescribeWebApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/applications/{DaraURL.percent_encode(application_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_application_with_options_async(
        self,
        application_id: str,
        request: main_models.DescribeWebApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/applications/{DaraURL.percent_encode(application_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_application(
        self,
        application_id: str,
        request: main_models.DescribeWebApplicationRequest,
    ) -> main_models.DescribeWebApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_web_application_with_options(application_id, request, headers, runtime)

    async def describe_web_application_async(
        self,
        application_id: str,
        request: main_models.DescribeWebApplicationRequest,
    ) -> main_models.DescribeWebApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_web_application_with_options_async(application_id, request, headers, runtime)

    def describe_web_application_resource_statics_with_options(
        self,
        application_id: str,
        request: main_models.DescribeWebApplicationResourceStaticsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebApplicationResourceStaticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebApplicationResourceStatics',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/applications-observability/{DaraURL.percent_encode(application_id)}/resource',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebApplicationResourceStaticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_application_resource_statics_with_options_async(
        self,
        application_id: str,
        request: main_models.DescribeWebApplicationResourceStaticsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebApplicationResourceStaticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebApplicationResourceStatics',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/applications-observability/{DaraURL.percent_encode(application_id)}/resource',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebApplicationResourceStaticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_application_resource_statics(
        self,
        application_id: str,
        request: main_models.DescribeWebApplicationResourceStaticsRequest,
    ) -> main_models.DescribeWebApplicationResourceStaticsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_web_application_resource_statics_with_options(application_id, request, headers, runtime)

    async def describe_web_application_resource_statics_async(
        self,
        application_id: str,
        request: main_models.DescribeWebApplicationResourceStaticsRequest,
    ) -> main_models.DescribeWebApplicationResourceStaticsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_web_application_resource_statics_with_options_async(application_id, request, headers, runtime)

    def describe_web_application_revision_with_options(
        self,
        application_id: str,
        revision_id: str,
        request: main_models.DescribeWebApplicationRevisionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebApplicationRevisionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebApplicationRevision',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/application-revisions/{DaraURL.percent_encode(application_id)}/revisions/{DaraURL.percent_encode(revision_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebApplicationRevisionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_application_revision_with_options_async(
        self,
        application_id: str,
        revision_id: str,
        request: main_models.DescribeWebApplicationRevisionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebApplicationRevisionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebApplicationRevision',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/application-revisions/{DaraURL.percent_encode(application_id)}/revisions/{DaraURL.percent_encode(revision_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebApplicationRevisionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_application_revision(
        self,
        application_id: str,
        revision_id: str,
        request: main_models.DescribeWebApplicationRevisionRequest,
    ) -> main_models.DescribeWebApplicationRevisionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_web_application_revision_with_options(application_id, revision_id, request, headers, runtime)

    async def describe_web_application_revision_async(
        self,
        application_id: str,
        revision_id: str,
        request: main_models.DescribeWebApplicationRevisionRequest,
    ) -> main_models.DescribeWebApplicationRevisionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_web_application_revision_with_options_async(application_id, revision_id, request, headers, runtime)

    def describe_web_application_scaling_config_with_options(
        self,
        application_id: str,
        request: main_models.DescribeWebApplicationScalingConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebApplicationScalingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebApplicationScalingConfig',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/application-scaling/{DaraURL.percent_encode(application_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebApplicationScalingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_application_scaling_config_with_options_async(
        self,
        application_id: str,
        request: main_models.DescribeWebApplicationScalingConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebApplicationScalingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebApplicationScalingConfig',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/application-scaling/{DaraURL.percent_encode(application_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebApplicationScalingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_application_scaling_config(
        self,
        application_id: str,
        request: main_models.DescribeWebApplicationScalingConfigRequest,
    ) -> main_models.DescribeWebApplicationScalingConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_web_application_scaling_config_with_options(application_id, request, headers, runtime)

    async def describe_web_application_scaling_config_async(
        self,
        application_id: str,
        request: main_models.DescribeWebApplicationScalingConfigRequest,
    ) -> main_models.DescribeWebApplicationScalingConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_web_application_scaling_config_with_options_async(application_id, request, headers, runtime)

    def describe_web_application_traffic_config_with_options(
        self,
        application_id: str,
        request: main_models.DescribeWebApplicationTrafficConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebApplicationTrafficConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebApplicationTrafficConfig',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/application-traffic/{DaraURL.percent_encode(application_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebApplicationTrafficConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_application_traffic_config_with_options_async(
        self,
        application_id: str,
        request: main_models.DescribeWebApplicationTrafficConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebApplicationTrafficConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebApplicationTrafficConfig',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/application-traffic/{DaraURL.percent_encode(application_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebApplicationTrafficConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_application_traffic_config(
        self,
        application_id: str,
        request: main_models.DescribeWebApplicationTrafficConfigRequest,
    ) -> main_models.DescribeWebApplicationTrafficConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_web_application_traffic_config_with_options(application_id, request, headers, runtime)

    async def describe_web_application_traffic_config_async(
        self,
        application_id: str,
        request: main_models.DescribeWebApplicationTrafficConfigRequest,
    ) -> main_models.DescribeWebApplicationTrafficConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_web_application_traffic_config_with_options_async(application_id, request, headers, runtime)

    def describe_web_custom_domain_with_options(
        self,
        domain_name: str,
        request: main_models.DescribeWebCustomDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebCustomDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebCustomDomain',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/custom-domains/{DaraURL.percent_encode(domain_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_custom_domain_with_options_async(
        self,
        domain_name: str,
        request: main_models.DescribeWebCustomDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebCustomDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebCustomDomain',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/custom-domains/{DaraURL.percent_encode(domain_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebCustomDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_custom_domain(
        self,
        domain_name: str,
        request: main_models.DescribeWebCustomDomainRequest,
    ) -> main_models.DescribeWebCustomDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_web_custom_domain_with_options(domain_name, request, headers, runtime)

    async def describe_web_custom_domain_async(
        self,
        domain_name: str,
        request: main_models.DescribeWebCustomDomainRequest,
    ) -> main_models.DescribeWebCustomDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_web_custom_domain_with_options_async(domain_name, request, headers, runtime)

    def describe_web_instance_logs_with_options(
        self,
        application_id: str,
        instance_id: str,
        request: main_models.DescribeWebInstanceLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebInstanceLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebInstanceLogs',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/applications-observability/{DaraURL.percent_encode(application_id)}/instances/{DaraURL.percent_encode(instance_id)}/logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebInstanceLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_instance_logs_with_options_async(
        self,
        application_id: str,
        instance_id: str,
        request: main_models.DescribeWebInstanceLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebInstanceLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebInstanceLogs',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/applications-observability/{DaraURL.percent_encode(application_id)}/instances/{DaraURL.percent_encode(instance_id)}/logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebInstanceLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_instance_logs(
        self,
        application_id: str,
        instance_id: str,
        request: main_models.DescribeWebInstanceLogsRequest,
    ) -> main_models.DescribeWebInstanceLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_web_instance_logs_with_options(application_id, instance_id, request, headers, runtime)

    async def describe_web_instance_logs_async(
        self,
        application_id: str,
        instance_id: str,
        request: main_models.DescribeWebInstanceLogsRequest,
    ) -> main_models.DescribeWebInstanceLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_web_instance_logs_with_options_async(application_id, instance_id, request, headers, runtime)

    def disable_application_scaling_rule_with_options(
        self,
        request: main_models.DisableApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableApplicationScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableApplicationScalingRule',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/scale/disableApplicationScalingRule',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_application_scaling_rule_with_options_async(
        self,
        request: main_models.DisableApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableApplicationScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableApplicationScalingRule',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/scale/disableApplicationScalingRule',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_application_scaling_rule(
        self,
        request: main_models.DisableApplicationScalingRuleRequest,
    ) -> main_models.DisableApplicationScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.disable_application_scaling_rule_with_options(request, headers, runtime)

    async def disable_application_scaling_rule_async(
        self,
        request: main_models.DisableApplicationScalingRuleRequest,
    ) -> main_models.DisableApplicationScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.disable_application_scaling_rule_with_options_async(request, headers, runtime)

    def disable_arms_with_options(
        self,
        request: main_models.DisableArmsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableArmsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableArms',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/arms/disableArms',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableArmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_arms_with_options_async(
        self,
        request: main_models.DisableArmsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableArmsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableArms',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/arms/disableArms',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableArmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_arms(
        self,
        request: main_models.DisableArmsRequest,
    ) -> main_models.DisableArmsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.disable_arms_with_options(request, headers, runtime)

    async def disable_arms_async(
        self,
        request: main_models.DisableArmsRequest,
    ) -> main_models.DisableArmsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.disable_arms_with_options_async(request, headers, runtime)

    def downgrade_application_apm_service_with_options(
        self,
        request: main_models.DowngradeApplicationApmServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DowngradeApplicationApmServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DowngradeApplicationApmService',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/applicationApmService',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DowngradeApplicationApmServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def downgrade_application_apm_service_with_options_async(
        self,
        request: main_models.DowngradeApplicationApmServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DowngradeApplicationApmServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DowngradeApplicationApmService',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/applicationApmService',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DowngradeApplicationApmServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def downgrade_application_apm_service(
        self,
        request: main_models.DowngradeApplicationApmServiceRequest,
    ) -> main_models.DowngradeApplicationApmServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.downgrade_application_apm_service_with_options(request, headers, runtime)

    async def downgrade_application_apm_service_async(
        self,
        request: main_models.DowngradeApplicationApmServiceRequest,
    ) -> main_models.DowngradeApplicationApmServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.downgrade_application_apm_service_with_options_async(request, headers, runtime)

    def enable_application_scaling_rule_with_options(
        self,
        request: main_models.EnableApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableApplicationScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableApplicationScalingRule',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/scale/enableApplicationScalingRule',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_application_scaling_rule_with_options_async(
        self,
        request: main_models.EnableApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableApplicationScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableApplicationScalingRule',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/scale/enableApplicationScalingRule',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_application_scaling_rule(
        self,
        request: main_models.EnableApplicationScalingRuleRequest,
    ) -> main_models.EnableApplicationScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.enable_application_scaling_rule_with_options(request, headers, runtime)

    async def enable_application_scaling_rule_async(
        self,
        request: main_models.EnableApplicationScalingRuleRequest,
    ) -> main_models.EnableApplicationScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.enable_application_scaling_rule_with_options_async(request, headers, runtime)

    def exec_job_with_options(
        self,
        request: main_models.ExecJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.command):
            query['Command'] = request.command
        if not DaraCore.is_null(request.command_args):
            query['CommandArgs'] = request.command_args
        if not DaraCore.is_null(request.envs):
            query['Envs'] = request.envs
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not DaraCore.is_null(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not DaraCore.is_null(request.replicas):
            query['Replicas'] = request.replicas
        if not DaraCore.is_null(request.time):
            query['Time'] = request.time
        if not DaraCore.is_null(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecJob',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/job/execJob',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def exec_job_with_options_async(
        self,
        request: main_models.ExecJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.command):
            query['Command'] = request.command
        if not DaraCore.is_null(request.command_args):
            query['CommandArgs'] = request.command_args
        if not DaraCore.is_null(request.envs):
            query['Envs'] = request.envs
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not DaraCore.is_null(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not DaraCore.is_null(request.replicas):
            query['Replicas'] = request.replicas
        if not DaraCore.is_null(request.time):
            query['Time'] = request.time
        if not DaraCore.is_null(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecJob',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/job/execJob',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exec_job(
        self,
        request: main_models.ExecJobRequest,
    ) -> main_models.ExecJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.exec_job_with_options(request, headers, runtime)

    async def exec_job_async(
        self,
        request: main_models.ExecJobRequest,
    ) -> main_models.ExecJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.exec_job_with_options_async(request, headers, runtime)

    def get_application_with_options(
        self,
        request: main_models.GetApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/getApplication',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_with_options_async(
        self,
        request: main_models.GetApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/getApplication',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application(
        self,
        request: main_models.GetApplicationRequest,
    ) -> main_models.GetApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_application_with_options(request, headers, runtime)

    async def get_application_async(
        self,
        request: main_models.GetApplicationRequest,
    ) -> main_models.GetApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_application_with_options_async(request, headers, runtime)

    def get_arms_top_nmetric_with_options(
        self,
        request: main_models.GetArmsTopNMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetArmsTopNMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_source):
            query['AppSource'] = request.app_source
        if not DaraCore.is_null(request.cpu_strategy):
            query['CpuStrategy'] = request.cpu_strategy
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetArmsTopNMetric',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/getArmsTopNMetric',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetArmsTopNMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_arms_top_nmetric_with_options_async(
        self,
        request: main_models.GetArmsTopNMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetArmsTopNMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_source):
            query['AppSource'] = request.app_source
        if not DaraCore.is_null(request.cpu_strategy):
            query['CpuStrategy'] = request.cpu_strategy
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetArmsTopNMetric',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/getArmsTopNMetric',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetArmsTopNMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_arms_top_nmetric(
        self,
        request: main_models.GetArmsTopNMetricRequest,
    ) -> main_models.GetArmsTopNMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_arms_top_nmetric_with_options(request, headers, runtime)

    async def get_arms_top_nmetric_async(
        self,
        request: main_models.GetArmsTopNMetricRequest,
    ) -> main_models.GetArmsTopNMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_arms_top_nmetric_with_options_async(request, headers, runtime)

    def get_availability_metric_with_options(
        self,
        request: main_models.GetAvailabilityMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAvailabilityMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_source):
            query['AppSource'] = request.app_source
        if not DaraCore.is_null(request.cpu_strategy):
            query['CpuStrategy'] = request.cpu_strategy
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAvailabilityMetric',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/getAvailabilityMetric',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAvailabilityMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_availability_metric_with_options_async(
        self,
        request: main_models.GetAvailabilityMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAvailabilityMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_source):
            query['AppSource'] = request.app_source
        if not DaraCore.is_null(request.cpu_strategy):
            query['CpuStrategy'] = request.cpu_strategy
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAvailabilityMetric',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/getAvailabilityMetric',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAvailabilityMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_availability_metric(
        self,
        request: main_models.GetAvailabilityMetricRequest,
    ) -> main_models.GetAvailabilityMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_availability_metric_with_options(request, headers, runtime)

    async def get_availability_metric_async(
        self,
        request: main_models.GetAvailabilityMetricRequest,
    ) -> main_models.GetAvailabilityMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_availability_metric_with_options_async(request, headers, runtime)

    def get_change_order_metric_with_options(
        self,
        request: main_models.GetChangeOrderMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetChangeOrderMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_source):
            query['AppSource'] = request.app_source
        if not DaraCore.is_null(request.co_type):
            query['CoType'] = request.co_type
        if not DaraCore.is_null(request.cpu_strategy):
            query['CpuStrategy'] = request.cpu_strategy
        if not DaraCore.is_null(request.create_time):
            query['CreateTime'] = request.create_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChangeOrderMetric',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/getChangeOrderMetric',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChangeOrderMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_change_order_metric_with_options_async(
        self,
        request: main_models.GetChangeOrderMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetChangeOrderMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_source):
            query['AppSource'] = request.app_source
        if not DaraCore.is_null(request.co_type):
            query['CoType'] = request.co_type
        if not DaraCore.is_null(request.cpu_strategy):
            query['CpuStrategy'] = request.cpu_strategy
        if not DaraCore.is_null(request.create_time):
            query['CreateTime'] = request.create_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChangeOrderMetric',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/getChangeOrderMetric',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChangeOrderMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_change_order_metric(
        self,
        request: main_models.GetChangeOrderMetricRequest,
    ) -> main_models.GetChangeOrderMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_change_order_metric_with_options(request, headers, runtime)

    async def get_change_order_metric_async(
        self,
        request: main_models.GetChangeOrderMetricRequest,
    ) -> main_models.GetChangeOrderMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_change_order_metric_with_options_async(request, headers, runtime)

    def get_scale_app_metric_with_options(
        self,
        request: main_models.GetScaleAppMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetScaleAppMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_source):
            query['AppSource'] = request.app_source
        if not DaraCore.is_null(request.cpu_strategy):
            query['CpuStrategy'] = request.cpu_strategy
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScaleAppMetric',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/getScaleAppMetric',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScaleAppMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scale_app_metric_with_options_async(
        self,
        request: main_models.GetScaleAppMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetScaleAppMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_source):
            query['AppSource'] = request.app_source
        if not DaraCore.is_null(request.cpu_strategy):
            query['CpuStrategy'] = request.cpu_strategy
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScaleAppMetric',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/getScaleAppMetric',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScaleAppMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scale_app_metric(
        self,
        request: main_models.GetScaleAppMetricRequest,
    ) -> main_models.GetScaleAppMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_scale_app_metric_with_options(request, headers, runtime)

    async def get_scale_app_metric_async(
        self,
        request: main_models.GetScaleAppMetricRequest,
    ) -> main_models.GetScaleAppMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_scale_app_metric_with_options_async(request, headers, runtime)

    def get_warning_event_metric_with_options(
        self,
        request: main_models.GetWarningEventMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetWarningEventMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_source):
            query['AppSource'] = request.app_source
        if not DaraCore.is_null(request.cpu_strategy):
            query['CpuStrategy'] = request.cpu_strategy
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWarningEventMetric',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/getWarningEventMetric',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWarningEventMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_warning_event_metric_with_options_async(
        self,
        request: main_models.GetWarningEventMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetWarningEventMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_source):
            query['AppSource'] = request.app_source
        if not DaraCore.is_null(request.cpu_strategy):
            query['CpuStrategy'] = request.cpu_strategy
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWarningEventMetric',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/getWarningEventMetric',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWarningEventMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_warning_event_metric(
        self,
        request: main_models.GetWarningEventMetricRequest,
    ) -> main_models.GetWarningEventMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_warning_event_metric_with_options(request, headers, runtime)

    async def get_warning_event_metric_async(
        self,
        request: main_models.GetWarningEventMetricRequest,
    ) -> main_models.GetWarningEventMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_warning_event_metric_with_options_async(request, headers, runtime)

    def get_webshell_token_with_options(
        self,
        request: main_models.GetWebshellTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetWebshellTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.container_name):
            query['ContainerName'] = request.container_name
        if not DaraCore.is_null(request.pod_name):
            query['PodName'] = request.pod_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWebshellToken',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/instance/webshellToken',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWebshellTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_webshell_token_with_options_async(
        self,
        request: main_models.GetWebshellTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetWebshellTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.container_name):
            query['ContainerName'] = request.container_name
        if not DaraCore.is_null(request.pod_name):
            query['PodName'] = request.pod_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWebshellToken',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/instance/webshellToken',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWebshellTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_webshell_token(
        self,
        request: main_models.GetWebshellTokenRequest,
    ) -> main_models.GetWebshellTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_webshell_token_with_options(request, headers, runtime)

    async def get_webshell_token_async(
        self,
        request: main_models.GetWebshellTokenRequest,
    ) -> main_models.GetWebshellTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_webshell_token_with_options_async(request, headers, runtime)

    def list_all_swimming_lane_groups_with_options(
        self,
        request: main_models.ListAllSwimmingLaneGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAllSwimmingLaneGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAllSwimmingLaneGroups',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/cas/gray/listSwimmingLaneGroups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAllSwimmingLaneGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_swimming_lane_groups_with_options_async(
        self,
        request: main_models.ListAllSwimmingLaneGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAllSwimmingLaneGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAllSwimmingLaneGroups',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/cas/gray/listSwimmingLaneGroups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAllSwimmingLaneGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_all_swimming_lane_groups(
        self,
        request: main_models.ListAllSwimmingLaneGroupsRequest,
    ) -> main_models.ListAllSwimmingLaneGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_all_swimming_lane_groups_with_options(request, headers, runtime)

    async def list_all_swimming_lane_groups_async(
        self,
        request: main_models.ListAllSwimmingLaneGroupsRequest,
    ) -> main_models.ListAllSwimmingLaneGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_all_swimming_lane_groups_with_options_async(request, headers, runtime)

    def list_all_swimming_lanes_with_options(
        self,
        request: main_models.ListAllSwimmingLanesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAllSwimmingLanesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAllSwimmingLanes',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/cas/gray/listSwimmingLanes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAllSwimmingLanesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_swimming_lanes_with_options_async(
        self,
        request: main_models.ListAllSwimmingLanesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAllSwimmingLanesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAllSwimmingLanes',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/cas/gray/listSwimmingLanes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAllSwimmingLanesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_all_swimming_lanes(
        self,
        request: main_models.ListAllSwimmingLanesRequest,
    ) -> main_models.ListAllSwimmingLanesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_all_swimming_lanes_with_options(request, headers, runtime)

    async def list_all_swimming_lanes_async(
        self,
        request: main_models.ListAllSwimmingLanesRequest,
    ) -> main_models.ListAllSwimmingLanesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_all_swimming_lanes_with_options_async(request, headers, runtime)

    def list_app_events_with_options(
        self,
        request: main_models.ListAppEventsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAppEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.object_kind):
            query['ObjectKind'] = request.object_kind
        if not DaraCore.is_null(request.object_name):
            query['ObjectName'] = request.object_name
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reason):
            query['Reason'] = request.reason
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppEvents',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/listAppEvents',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_events_with_options_async(
        self,
        request: main_models.ListAppEventsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAppEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.object_kind):
            query['ObjectKind'] = request.object_kind
        if not DaraCore.is_null(request.object_name):
            query['ObjectName'] = request.object_name
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reason):
            query['Reason'] = request.reason
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppEvents',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/listAppEvents',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_events(
        self,
        request: main_models.ListAppEventsRequest,
    ) -> main_models.ListAppEventsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_app_events_with_options(request, headers, runtime)

    async def list_app_events_async(
        self,
        request: main_models.ListAppEventsRequest,
    ) -> main_models.ListAppEventsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_app_events_with_options_async(request, headers, runtime)

    def list_app_services_with_options(
        self,
        request: main_models.ListAppServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAppServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.nacos_instance_id):
            query['NacosInstanceId'] = request.nacos_instance_id
        if not DaraCore.is_null(request.nacos_namespace_id):
            query['NacosNamespaceId'] = request.nacos_namespace_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.registry_type):
            query['RegistryType'] = request.registry_type
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppServices',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/service/listAppServices',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_services_with_options_async(
        self,
        request: main_models.ListAppServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAppServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.nacos_instance_id):
            query['NacosInstanceId'] = request.nacos_instance_id
        if not DaraCore.is_null(request.nacos_namespace_id):
            query['NacosNamespaceId'] = request.nacos_namespace_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.registry_type):
            query['RegistryType'] = request.registry_type
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppServices',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/service/listAppServices',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_services(
        self,
        request: main_models.ListAppServicesRequest,
    ) -> main_models.ListAppServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_app_services_with_options(request, headers, runtime)

    async def list_app_services_async(
        self,
        request: main_models.ListAppServicesRequest,
    ) -> main_models.ListAppServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_app_services_with_options_async(request, headers, runtime)

    def list_app_services_page_with_options(
        self,
        request: main_models.ListAppServicesPageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAppServicesPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppServicesPage',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/service/listAppServicesPage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppServicesPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_services_page_with_options_async(
        self,
        request: main_models.ListAppServicesPageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAppServicesPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppServicesPage',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/service/listAppServicesPage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppServicesPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_services_page(
        self,
        request: main_models.ListAppServicesPageRequest,
    ) -> main_models.ListAppServicesPageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_app_services_page_with_options(request, headers, runtime)

    async def list_app_services_page_async(
        self,
        request: main_models.ListAppServicesPageRequest,
    ) -> main_models.ListAppServicesPageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_app_services_page_with_options_async(request, headers, runtime)

    def list_app_versions_with_options(
        self,
        request: main_models.ListAppVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAppVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppVersions',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/listAppVersions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_versions_with_options_async(
        self,
        request: main_models.ListAppVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAppVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppVersions',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/listAppVersions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_versions(
        self,
        request: main_models.ListAppVersionsRequest,
    ) -> main_models.ListAppVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_app_versions_with_options(request, headers, runtime)

    async def list_app_versions_async(
        self,
        request: main_models.ListAppVersionsRequest,
    ) -> main_models.ListAppVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_app_versions_with_options_async(request, headers, runtime)

    def list_applications_with_options(
        self,
        request: main_models.ListApplicationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_source):
            query['AppSource'] = request.app_source
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.field_type):
            query['FieldType'] = request.field_type
        if not DaraCore.is_null(request.field_value):
            query['FieldValue'] = request.field_value
        if not DaraCore.is_null(request.is_stateful):
            query['IsStateful'] = request.is_stateful
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.new_sae_version):
            query['NewSaeVersion'] = request.new_sae_version
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reverse):
            query['Reverse'] = request.reverse
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplications',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/listApplications',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_with_options_async(
        self,
        request: main_models.ListApplicationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_source):
            query['AppSource'] = request.app_source
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.field_type):
            query['FieldType'] = request.field_type
        if not DaraCore.is_null(request.field_value):
            query['FieldValue'] = request.field_value
        if not DaraCore.is_null(request.is_stateful):
            query['IsStateful'] = request.is_stateful
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.new_sae_version):
            query['NewSaeVersion'] = request.new_sae_version
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reverse):
            query['Reverse'] = request.reverse
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplications',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/listApplications',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications(
        self,
        request: main_models.ListApplicationsRequest,
    ) -> main_models.ListApplicationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_applications_with_options(request, headers, runtime)

    async def list_applications_async(
        self,
        request: main_models.ListApplicationsRequest,
    ) -> main_models.ListApplicationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_applications_with_options_async(request, headers, runtime)

    def list_applications_for_swimming_lane_with_options(
        self,
        request: main_models.ListApplicationsForSwimmingLaneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsForSwimmingLaneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationsForSwimmingLane',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/cas/gray/listApplicationsForSwimmingLane',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsForSwimmingLaneResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_for_swimming_lane_with_options_async(
        self,
        request: main_models.ListApplicationsForSwimmingLaneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsForSwimmingLaneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationsForSwimmingLane',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/cas/gray/listApplicationsForSwimmingLane',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsForSwimmingLaneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications_for_swimming_lane(
        self,
        request: main_models.ListApplicationsForSwimmingLaneRequest,
    ) -> main_models.ListApplicationsForSwimmingLaneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_applications_for_swimming_lane_with_options(request, headers, runtime)

    async def list_applications_for_swimming_lane_async(
        self,
        request: main_models.ListApplicationsForSwimmingLaneRequest,
    ) -> main_models.ListApplicationsForSwimmingLaneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_applications_for_swimming_lane_with_options_async(request, headers, runtime)

    def list_change_orders_with_options(
        self,
        request: main_models.ListChangeOrdersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListChangeOrdersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.co_status):
            query['CoStatus'] = request.co_status
        if not DaraCore.is_null(request.co_type):
            query['CoType'] = request.co_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reverse):
            query['Reverse'] = request.reverse
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChangeOrders',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/changeorder/ListChangeOrders',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChangeOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_change_orders_with_options_async(
        self,
        request: main_models.ListChangeOrdersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListChangeOrdersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.co_status):
            query['CoStatus'] = request.co_status
        if not DaraCore.is_null(request.co_type):
            query['CoType'] = request.co_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reverse):
            query['Reverse'] = request.reverse
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChangeOrders',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/changeorder/ListChangeOrders',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChangeOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_change_orders(
        self,
        request: main_models.ListChangeOrdersRequest,
    ) -> main_models.ListChangeOrdersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_change_orders_with_options(request, headers, runtime)

    async def list_change_orders_async(
        self,
        request: main_models.ListChangeOrdersRequest,
    ) -> main_models.ListChangeOrdersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_change_orders_with_options_async(request, headers, runtime)

    def list_consumed_services_with_options(
        self,
        request: main_models.ListConsumedServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumedServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConsumedServices',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/service/listConsumedServices',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConsumedServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_consumed_services_with_options_async(
        self,
        request: main_models.ListConsumedServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumedServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConsumedServices',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/service/listConsumedServices',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConsumedServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_consumed_services(
        self,
        request: main_models.ListConsumedServicesRequest,
    ) -> main_models.ListConsumedServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_consumed_services_with_options(request, headers, runtime)

    async def list_consumed_services_async(
        self,
        request: main_models.ListConsumedServicesRequest,
    ) -> main_models.ListConsumedServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_consumed_services_with_options_async(request, headers, runtime)

    def list_grey_tag_route_with_options(
        self,
        request: main_models.ListGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGreyTagRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGreyTagRoute',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/tagroute/greyTagRouteList',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGreyTagRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_grey_tag_route_with_options_async(
        self,
        request: main_models.ListGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGreyTagRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGreyTagRoute',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/tagroute/greyTagRouteList',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGreyTagRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_grey_tag_route(
        self,
        request: main_models.ListGreyTagRouteRequest,
    ) -> main_models.ListGreyTagRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_grey_tag_route_with_options(request, headers, runtime)

    async def list_grey_tag_route_async(
        self,
        request: main_models.ListGreyTagRouteRequest,
    ) -> main_models.ListGreyTagRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_grey_tag_route_with_options_async(request, headers, runtime)

    def list_ingresses_with_options(
        self,
        request: main_models.ListIngressesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIngressesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIngresses',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/ingress/IngressList',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIngressesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ingresses_with_options_async(
        self,
        request: main_models.ListIngressesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIngressesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIngresses',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/ingress/IngressList',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIngressesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ingresses(
        self,
        request: main_models.ListIngressesRequest,
    ) -> main_models.ListIngressesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_ingresses_with_options(request, headers, runtime)

    async def list_ingresses_async(
        self,
        request: main_models.ListIngressesRequest,
    ) -> main_models.ListIngressesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_ingresses_with_options_async(request, headers, runtime)

    def list_jobs_with_options(
        self,
        request: main_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.field_type):
            query['FieldType'] = request.field_type
        if not DaraCore.is_null(request.field_value):
            query['FieldValue'] = request.field_value
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reverse):
            query['Reverse'] = request.reverse
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.workload):
            query['Workload'] = request.workload
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobs',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/job/listJobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        request: main_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.field_type):
            query['FieldType'] = request.field_type
        if not DaraCore.is_null(request.field_value):
            query['FieldValue'] = request.field_value
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reverse):
            query['Reverse'] = request.reverse
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.workload):
            query['Workload'] = request.workload
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobs',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/job/listJobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        request: main_models.ListJobsRequest,
    ) -> main_models.ListJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_jobs_with_options(request, headers, runtime)

    async def list_jobs_async(
        self,
        request: main_models.ListJobsRequest,
    ) -> main_models.ListJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_jobs_with_options_async(request, headers, runtime)

    def list_log_configs_with_options(
        self,
        request: main_models.ListLogConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLogConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLogConfigs',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/log/listLogConfigs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLogConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_log_configs_with_options_async(
        self,
        request: main_models.ListLogConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLogConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLogConfigs',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/log/listLogConfigs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLogConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_log_configs(
        self,
        request: main_models.ListLogConfigsRequest,
    ) -> main_models.ListLogConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_log_configs_with_options(request, headers, runtime)

    async def list_log_configs_async(
        self,
        request: main_models.ListLogConfigsRequest,
    ) -> main_models.ListLogConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_log_configs_with_options_async(request, headers, runtime)

    def list_namespace_change_orders_with_options(
        self,
        request: main_models.ListNamespaceChangeOrdersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListNamespaceChangeOrdersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.co_status):
            query['CoStatus'] = request.co_status
        if not DaraCore.is_null(request.co_type):
            query['CoType'] = request.co_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNamespaceChangeOrders',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/changeorder/listNamespaceChangeOrders',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNamespaceChangeOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_namespace_change_orders_with_options_async(
        self,
        request: main_models.ListNamespaceChangeOrdersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListNamespaceChangeOrdersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.co_status):
            query['CoStatus'] = request.co_status
        if not DaraCore.is_null(request.co_type):
            query['CoType'] = request.co_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNamespaceChangeOrders',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/changeorder/listNamespaceChangeOrders',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNamespaceChangeOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_namespace_change_orders(
        self,
        request: main_models.ListNamespaceChangeOrdersRequest,
    ) -> main_models.ListNamespaceChangeOrdersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_namespace_change_orders_with_options(request, headers, runtime)

    async def list_namespace_change_orders_async(
        self,
        request: main_models.ListNamespaceChangeOrdersRequest,
    ) -> main_models.ListNamespaceChangeOrdersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_namespace_change_orders_with_options_async(request, headers, runtime)

    def list_namespaced_config_maps_with_options(
        self,
        request: main_models.ListNamespacedConfigMapsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListNamespacedConfigMapsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNamespacedConfigMaps',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/configmap/listNamespacedConfigMaps',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNamespacedConfigMapsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_namespaced_config_maps_with_options_async(
        self,
        request: main_models.ListNamespacedConfigMapsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListNamespacedConfigMapsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNamespacedConfigMaps',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/configmap/listNamespacedConfigMaps',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNamespacedConfigMapsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_namespaced_config_maps(
        self,
        request: main_models.ListNamespacedConfigMapsRequest,
    ) -> main_models.ListNamespacedConfigMapsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_namespaced_config_maps_with_options(request, headers, runtime)

    async def list_namespaced_config_maps_async(
        self,
        request: main_models.ListNamespacedConfigMapsRequest,
    ) -> main_models.ListNamespacedConfigMapsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_namespaced_config_maps_with_options_async(request, headers, runtime)

    def list_published_services_with_options(
        self,
        request: main_models.ListPublishedServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPublishedServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPublishedServices',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/service/listPublishedServices',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPublishedServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_published_services_with_options_async(
        self,
        request: main_models.ListPublishedServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPublishedServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPublishedServices',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/service/listPublishedServices',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPublishedServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_published_services(
        self,
        request: main_models.ListPublishedServicesRequest,
    ) -> main_models.ListPublishedServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_published_services_with_options(request, headers, runtime)

    async def list_published_services_async(
        self,
        request: main_models.ListPublishedServicesRequest,
    ) -> main_models.ListPublishedServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_published_services_with_options_async(request, headers, runtime)

    def list_secrets_with_options(
        self,
        request: main_models.ListSecretsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSecretsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecrets',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/secret/secrets',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecretsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_secrets_with_options_async(
        self,
        request: main_models.ListSecretsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSecretsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecrets',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/secret/secrets',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecretsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_secrets(
        self,
        request: main_models.ListSecretsRequest,
    ) -> main_models.ListSecretsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_secrets_with_options(request, headers, runtime)

    async def list_secrets_async(
        self,
        request: main_models.ListSecretsRequest,
    ) -> main_models.ListSecretsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_secrets_with_options_async(request, headers, runtime)

    def list_swimming_lane_gateway_routes_with_options(
        self,
        request: main_models.ListSwimmingLaneGatewayRoutesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSwimmingLaneGatewayRoutesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSwimmingLaneGatewayRoutes',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/cas/gray/listSwimmingLaneGatewayRoutes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSwimmingLaneGatewayRoutesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_swimming_lane_gateway_routes_with_options_async(
        self,
        request: main_models.ListSwimmingLaneGatewayRoutesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSwimmingLaneGatewayRoutesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSwimmingLaneGatewayRoutes',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/cas/gray/listSwimmingLaneGatewayRoutes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSwimmingLaneGatewayRoutesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_swimming_lane_gateway_routes(
        self,
        request: main_models.ListSwimmingLaneGatewayRoutesRequest,
    ) -> main_models.ListSwimmingLaneGatewayRoutesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_swimming_lane_gateway_routes_with_options(request, headers, runtime)

    async def list_swimming_lane_gateway_routes_async(
        self,
        request: main_models.ListSwimmingLaneGatewayRoutesRequest,
    ) -> main_models.ListSwimmingLaneGatewayRoutesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_swimming_lane_gateway_routes_with_options_async(request, headers, runtime)

    def list_swimming_lane_group_tags_with_options(
        self,
        request: main_models.ListSwimmingLaneGroupTagsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSwimmingLaneGroupTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSwimmingLaneGroupTags',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/cas/gray/listSwimmingLaneGroupTags',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSwimmingLaneGroupTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_swimming_lane_group_tags_with_options_async(
        self,
        request: main_models.ListSwimmingLaneGroupTagsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSwimmingLaneGroupTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSwimmingLaneGroupTags',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/cas/gray/listSwimmingLaneGroupTags',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSwimmingLaneGroupTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_swimming_lane_group_tags(
        self,
        request: main_models.ListSwimmingLaneGroupTagsRequest,
    ) -> main_models.ListSwimmingLaneGroupTagsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_swimming_lane_group_tags_with_options(request, headers, runtime)

    async def list_swimming_lane_group_tags_async(
        self,
        request: main_models.ListSwimmingLaneGroupTagsRequest,
    ) -> main_models.ListSwimmingLaneGroupTagsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_swimming_lane_group_tags_with_options_async(request, headers, runtime)

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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/tags',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/tags',
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

    def list_web_application_instances_with_options(
        self,
        application_id: str,
        tmp_req: main_models.ListWebApplicationInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWebApplicationInstancesResponse:
        tmp_req.validate()
        request = main_models.ListWebApplicationInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        if not DaraCore.is_null(tmp_req.statuses):
            request.statuses_shrink = Utils.array_to_string_with_specified_style(tmp_req.statuses, 'Statuses', 'json')
        if not DaraCore.is_null(tmp_req.version_ids):
            request.version_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.version_ids, 'VersionIds', 'json')
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.statuses_shrink):
            query['Statuses'] = request.statuses_shrink
        if not DaraCore.is_null(request.version_ids_shrink):
            query['VersionIds'] = request.version_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWebApplicationInstances',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/applications-observability/{DaraURL.percent_encode(application_id)}/instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWebApplicationInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_web_application_instances_with_options_async(
        self,
        application_id: str,
        tmp_req: main_models.ListWebApplicationInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWebApplicationInstancesResponse:
        tmp_req.validate()
        request = main_models.ListWebApplicationInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        if not DaraCore.is_null(tmp_req.statuses):
            request.statuses_shrink = Utils.array_to_string_with_specified_style(tmp_req.statuses, 'Statuses', 'json')
        if not DaraCore.is_null(tmp_req.version_ids):
            request.version_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.version_ids, 'VersionIds', 'json')
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.statuses_shrink):
            query['Statuses'] = request.statuses_shrink
        if not DaraCore.is_null(request.version_ids_shrink):
            query['VersionIds'] = request.version_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWebApplicationInstances',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/applications-observability/{DaraURL.percent_encode(application_id)}/instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWebApplicationInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_web_application_instances(
        self,
        application_id: str,
        request: main_models.ListWebApplicationInstancesRequest,
    ) -> main_models.ListWebApplicationInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_web_application_instances_with_options(application_id, request, headers, runtime)

    async def list_web_application_instances_async(
        self,
        application_id: str,
        request: main_models.ListWebApplicationInstancesRequest,
    ) -> main_models.ListWebApplicationInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_web_application_instances_with_options_async(application_id, request, headers, runtime)

    def list_web_application_revisions_with_options(
        self,
        application_id: str,
        request: main_models.ListWebApplicationRevisionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWebApplicationRevisionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWebApplicationRevisions',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/application-revisions/{DaraURL.percent_encode(application_id)}/revisions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWebApplicationRevisionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_web_application_revisions_with_options_async(
        self,
        application_id: str,
        request: main_models.ListWebApplicationRevisionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWebApplicationRevisionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWebApplicationRevisions',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/application-revisions/{DaraURL.percent_encode(application_id)}/revisions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWebApplicationRevisionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_web_application_revisions(
        self,
        application_id: str,
        request: main_models.ListWebApplicationRevisionsRequest,
    ) -> main_models.ListWebApplicationRevisionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_web_application_revisions_with_options(application_id, request, headers, runtime)

    async def list_web_application_revisions_async(
        self,
        application_id: str,
        request: main_models.ListWebApplicationRevisionsRequest,
    ) -> main_models.ListWebApplicationRevisionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_web_application_revisions_with_options_async(application_id, request, headers, runtime)

    def list_web_applications_with_options(
        self,
        request: main_models.ListWebApplicationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWebApplicationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.prefix):
            query['Prefix'] = request.prefix
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWebApplications',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/applications',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWebApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_web_applications_with_options_async(
        self,
        request: main_models.ListWebApplicationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWebApplicationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.prefix):
            query['Prefix'] = request.prefix
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWebApplications',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/applications',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWebApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_web_applications(
        self,
        request: main_models.ListWebApplicationsRequest,
    ) -> main_models.ListWebApplicationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_web_applications_with_options(request, headers, runtime)

    async def list_web_applications_async(
        self,
        request: main_models.ListWebApplicationsRequest,
    ) -> main_models.ListWebApplicationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_web_applications_with_options_async(request, headers, runtime)

    def list_web_custom_domains_with_options(
        self,
        request: main_models.ListWebCustomDomainsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWebCustomDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.prefix):
            query['Prefix'] = request.prefix
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWebCustomDomains',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/custom-domains',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWebCustomDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_web_custom_domains_with_options_async(
        self,
        request: main_models.ListWebCustomDomainsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWebCustomDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.prefix):
            query['Prefix'] = request.prefix
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWebCustomDomains',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/custom-domains',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWebCustomDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_web_custom_domains(
        self,
        request: main_models.ListWebCustomDomainsRequest,
    ) -> main_models.ListWebCustomDomainsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_web_custom_domains_with_options(request, headers, runtime)

    async def list_web_custom_domains_async(
        self,
        request: main_models.ListWebCustomDomainsRequest,
    ) -> main_models.ListWebCustomDomainsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_web_custom_domains_with_options_async(request, headers, runtime)

    def open_sae_service_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OpenSaeServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'OpenSaeService',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/service/open',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenSaeServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_sae_service_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OpenSaeServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'OpenSaeService',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/service/open',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenSaeServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_sae_service(self) -> main_models.OpenSaeServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.open_sae_service_with_options(headers, runtime)

    async def open_sae_service_async(self) -> main_models.OpenSaeServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.open_sae_service_with_options_async(headers, runtime)

    def publish_web_application_revision_with_options(
        self,
        application_id: str,
        request: main_models.PublishWebApplicationRevisionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PublishWebApplicationRevisionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'PublishWebApplicationRevision',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/application-revisions/{DaraURL.percent_encode(application_id)}/revisions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishWebApplicationRevisionResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_web_application_revision_with_options_async(
        self,
        application_id: str,
        request: main_models.PublishWebApplicationRevisionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PublishWebApplicationRevisionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'PublishWebApplicationRevision',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/application-revisions/{DaraURL.percent_encode(application_id)}/revisions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishWebApplicationRevisionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_web_application_revision(
        self,
        application_id: str,
        request: main_models.PublishWebApplicationRevisionRequest,
    ) -> main_models.PublishWebApplicationRevisionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.publish_web_application_revision_with_options(application_id, request, headers, runtime)

    async def publish_web_application_revision_async(
        self,
        application_id: str,
        request: main_models.PublishWebApplicationRevisionRequest,
    ) -> main_models.PublishWebApplicationRevisionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.publish_web_application_revision_with_options_async(application_id, request, headers, runtime)

    def query_arms_enable_with_options(
        self,
        request: main_models.QueryArmsEnableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryArmsEnableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryArmsEnable',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/arms/queryArms',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryArmsEnableResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_arms_enable_with_options_async(
        self,
        request: main_models.QueryArmsEnableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryArmsEnableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryArmsEnable',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/arms/queryArms',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryArmsEnableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_arms_enable(
        self,
        request: main_models.QueryArmsEnableRequest,
    ) -> main_models.QueryArmsEnableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_arms_enable_with_options(request, headers, runtime)

    async def query_arms_enable_async(
        self,
        request: main_models.QueryArmsEnableRequest,
    ) -> main_models.QueryArmsEnableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_arms_enable_with_options_async(request, headers, runtime)

    def query_resource_statics_with_options(
        self,
        request: main_models.QueryResourceStaticsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryResourceStaticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryResourceStatics',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/paas/quota/queryResourceStatics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryResourceStaticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_resource_statics_with_options_async(
        self,
        request: main_models.QueryResourceStaticsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryResourceStaticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryResourceStatics',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/paas/quota/queryResourceStatics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryResourceStaticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_resource_statics(
        self,
        request: main_models.QueryResourceStaticsRequest,
    ) -> main_models.QueryResourceStaticsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_resource_statics_with_options(request, headers, runtime)

    async def query_resource_statics_async(
        self,
        request: main_models.QueryResourceStaticsRequest,
    ) -> main_models.QueryResourceStaticsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_resource_statics_with_options_async(request, headers, runtime)

    def reduce_application_capacity_by_instance_ids_with_options(
        self,
        request: main_models.ReduceApplicationCapacityByInstanceIdsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReduceApplicationCapacityByInstanceIdsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReduceApplicationCapacityByInstanceIds',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/ScaleInApplicationWithInstanceIds',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReduceApplicationCapacityByInstanceIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def reduce_application_capacity_by_instance_ids_with_options_async(
        self,
        request: main_models.ReduceApplicationCapacityByInstanceIdsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReduceApplicationCapacityByInstanceIdsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReduceApplicationCapacityByInstanceIds',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/ScaleInApplicationWithInstanceIds',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReduceApplicationCapacityByInstanceIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reduce_application_capacity_by_instance_ids(
        self,
        request: main_models.ReduceApplicationCapacityByInstanceIdsRequest,
    ) -> main_models.ReduceApplicationCapacityByInstanceIdsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.reduce_application_capacity_by_instance_ids_with_options(request, headers, runtime)

    async def reduce_application_capacity_by_instance_ids_async(
        self,
        request: main_models.ReduceApplicationCapacityByInstanceIdsRequest,
    ) -> main_models.ReduceApplicationCapacityByInstanceIdsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.reduce_application_capacity_by_instance_ids_with_options_async(request, headers, runtime)

    def rescale_application_with_options(
        self,
        request: main_models.RescaleApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RescaleApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not DaraCore.is_null(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not DaraCore.is_null(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not DaraCore.is_null(request.replicas):
            query['Replicas'] = request.replicas
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RescaleApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/rescaleApplication',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RescaleApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def rescale_application_with_options_async(
        self,
        request: main_models.RescaleApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RescaleApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not DaraCore.is_null(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not DaraCore.is_null(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not DaraCore.is_null(request.replicas):
            query['Replicas'] = request.replicas
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RescaleApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/rescaleApplication',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RescaleApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rescale_application(
        self,
        request: main_models.RescaleApplicationRequest,
    ) -> main_models.RescaleApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.rescale_application_with_options(request, headers, runtime)

    async def rescale_application_async(
        self,
        request: main_models.RescaleApplicationRequest,
    ) -> main_models.RescaleApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.rescale_application_with_options_async(request, headers, runtime)

    def rescale_application_vertically_with_options(
        self,
        request: main_models.RescaleApplicationVerticallyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RescaleApplicationVerticallyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cpu):
            query['Cpu'] = request.cpu
        if not DaraCore.is_null(request.deploy):
            query['Deploy'] = request.deploy
        if not DaraCore.is_null(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not DaraCore.is_null(request.memory):
            query['Memory'] = request.memory
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.auto_enable_application_scaling_rule):
            query['autoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not DaraCore.is_null(request.min_ready_instance_ratio):
            query['minReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not DaraCore.is_null(request.min_ready_instances):
            query['minReadyInstances'] = request.min_ready_instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RescaleApplicationVertically',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/rescaleApplicationVertically',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RescaleApplicationVerticallyResponse(),
            self.call_api(params, req, runtime)
        )

    async def rescale_application_vertically_with_options_async(
        self,
        request: main_models.RescaleApplicationVerticallyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RescaleApplicationVerticallyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cpu):
            query['Cpu'] = request.cpu
        if not DaraCore.is_null(request.deploy):
            query['Deploy'] = request.deploy
        if not DaraCore.is_null(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not DaraCore.is_null(request.memory):
            query['Memory'] = request.memory
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.auto_enable_application_scaling_rule):
            query['autoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not DaraCore.is_null(request.min_ready_instance_ratio):
            query['minReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not DaraCore.is_null(request.min_ready_instances):
            query['minReadyInstances'] = request.min_ready_instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RescaleApplicationVertically',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/rescaleApplicationVertically',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RescaleApplicationVerticallyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rescale_application_vertically(
        self,
        request: main_models.RescaleApplicationVerticallyRequest,
    ) -> main_models.RescaleApplicationVerticallyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.rescale_application_vertically_with_options(request, headers, runtime)

    async def rescale_application_vertically_async(
        self,
        request: main_models.RescaleApplicationVerticallyRequest,
    ) -> main_models.RescaleApplicationVerticallyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.rescale_application_vertically_with_options_async(request, headers, runtime)

    def restart_application_with_options(
        self,
        request: main_models.RestartApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not DaraCore.is_null(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not DaraCore.is_null(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/restartApplication',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_application_with_options_async(
        self,
        request: main_models.RestartApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not DaraCore.is_null(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not DaraCore.is_null(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/restartApplication',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_application(
        self,
        request: main_models.RestartApplicationRequest,
    ) -> main_models.RestartApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.restart_application_with_options(request, headers, runtime)

    async def restart_application_async(
        self,
        request: main_models.RestartApplicationRequest,
    ) -> main_models.RestartApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.restart_application_with_options_async(request, headers, runtime)

    def restart_instances_with_options(
        self,
        request: main_models.RestartInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartInstances',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/restartInstances',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_instances_with_options_async(
        self,
        request: main_models.RestartInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartInstances',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/restartInstances',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_instances(
        self,
        request: main_models.RestartInstancesRequest,
    ) -> main_models.RestartInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.restart_instances_with_options(request, headers, runtime)

    async def restart_instances_async(
        self,
        request: main_models.RestartInstancesRequest,
    ) -> main_models.RestartInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.restart_instances_with_options_async(request, headers, runtime)

    def resume_traffic_with_options(
        self,
        request: main_models.ResumeTrafficRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResumeTrafficResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeTraffic',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/instanceTrafficResume',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeTrafficResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_traffic_with_options_async(
        self,
        request: main_models.ResumeTrafficRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResumeTrafficResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeTraffic',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/instanceTrafficResume',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeTrafficResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_traffic(
        self,
        request: main_models.ResumeTrafficRequest,
    ) -> main_models.ResumeTrafficResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.resume_traffic_with_options(request, headers, runtime)

    async def resume_traffic_async(
        self,
        request: main_models.ResumeTrafficRequest,
    ) -> main_models.ResumeTrafficResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.resume_traffic_with_options_async(request, headers, runtime)

    def rollback_application_with_options(
        self,
        request: main_models.RollbackApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RollbackApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not DaraCore.is_null(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not DaraCore.is_null(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not DaraCore.is_null(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not DaraCore.is_null(request.update_strategy):
            query['UpdateStrategy'] = request.update_strategy
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/rollbackApplication',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_application_with_options_async(
        self,
        request: main_models.RollbackApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RollbackApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not DaraCore.is_null(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not DaraCore.is_null(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not DaraCore.is_null(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not DaraCore.is_null(request.update_strategy):
            query['UpdateStrategy'] = request.update_strategy
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/rollbackApplication',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_application(
        self,
        request: main_models.RollbackApplicationRequest,
    ) -> main_models.RollbackApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.rollback_application_with_options(request, headers, runtime)

    async def rollback_application_async(
        self,
        request: main_models.RollbackApplicationRequest,
    ) -> main_models.RollbackApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.rollback_application_with_options_async(request, headers, runtime)

    def start_application_with_options(
        self,
        request: main_models.StartApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/startApplication',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_application_with_options_async(
        self,
        request: main_models.StartApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/startApplication',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_application(
        self,
        request: main_models.StartApplicationRequest,
    ) -> main_models.StartApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_application_with_options(request, headers, runtime)

    async def start_application_async(
        self,
        request: main_models.StartApplicationRequest,
    ) -> main_models.StartApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_application_with_options_async(request, headers, runtime)

    def start_web_application_with_options(
        self,
        application_id: str,
        request: main_models.StartWebApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartWebApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartWebApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/application-ops/{DaraURL.percent_encode(application_id)}/start',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartWebApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_web_application_with_options_async(
        self,
        application_id: str,
        request: main_models.StartWebApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartWebApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartWebApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/application-ops/{DaraURL.percent_encode(application_id)}/start',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartWebApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_web_application(
        self,
        application_id: str,
        request: main_models.StartWebApplicationRequest,
    ) -> main_models.StartWebApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_web_application_with_options(application_id, request, headers, runtime)

    async def start_web_application_async(
        self,
        application_id: str,
        request: main_models.StartWebApplicationRequest,
    ) -> main_models.StartWebApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_web_application_with_options_async(application_id, request, headers, runtime)

    def stop_application_with_options(
        self,
        request: main_models.StopApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/stopApplication',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_application_with_options_async(
        self,
        request: main_models.StopApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/stopApplication',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_application(
        self,
        request: main_models.StopApplicationRequest,
    ) -> main_models.StopApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_application_with_options(request, headers, runtime)

    async def stop_application_async(
        self,
        request: main_models.StopApplicationRequest,
    ) -> main_models.StopApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_application_with_options_async(request, headers, runtime)

    def stop_web_application_with_options(
        self,
        application_id: str,
        request: main_models.StopWebApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopWebApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopWebApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/application-ops/{DaraURL.percent_encode(application_id)}/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopWebApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_web_application_with_options_async(
        self,
        application_id: str,
        request: main_models.StopWebApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopWebApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopWebApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/application-ops/{DaraURL.percent_encode(application_id)}/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopWebApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_web_application(
        self,
        application_id: str,
        request: main_models.StopWebApplicationRequest,
    ) -> main_models.StopWebApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_web_application_with_options(application_id, request, headers, runtime)

    async def stop_web_application_async(
        self,
        application_id: str,
        request: main_models.StopWebApplicationRequest,
    ) -> main_models.StopWebApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_web_application_with_options_async(application_id, request, headers, runtime)

    def suspend_job_with_options(
        self,
        request: main_models.SuspendJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SuspendJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.suspend):
            query['Suspend'] = request.suspend
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SuspendJob',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/job/suspendJob',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_job_with_options_async(
        self,
        request: main_models.SuspendJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SuspendJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.suspend):
            query['Suspend'] = request.suspend
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SuspendJob',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/job/suspendJob',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_job(
        self,
        request: main_models.SuspendJobRequest,
    ) -> main_models.SuspendJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.suspend_job_with_options(request, headers, runtime)

    async def suspend_job_async(
        self,
        request: main_models.SuspendJobRequest,
    ) -> main_models.SuspendJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.suspend_job_with_options_async(request, headers, runtime)

    def suspend_traffic_with_options(
        self,
        request: main_models.SuspendTrafficRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SuspendTrafficResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SuspendTraffic',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/instanceTrafficSuspend',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendTrafficResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_traffic_with_options_async(
        self,
        request: main_models.SuspendTrafficRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SuspendTrafficResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SuspendTraffic',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/instanceTrafficSuspend',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendTrafficResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_traffic(
        self,
        request: main_models.SuspendTrafficRequest,
    ) -> main_models.SuspendTrafficResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.suspend_traffic_with_options(request, headers, runtime)

    async def suspend_traffic_async(
        self,
        request: main_models.SuspendTrafficRequest,
    ) -> main_models.SuspendTrafficResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.suspend_traffic_with_options_async(request, headers, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
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
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
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
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
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
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
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

    def unbind_nlb_with_options(
        self,
        request: main_models.UnbindNlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnbindNlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.nlb_id):
            query['NlbId'] = request.nlb_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindNlb',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/nlb',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindNlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_nlb_with_options_async(
        self,
        request: main_models.UnbindNlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnbindNlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.nlb_id):
            query['NlbId'] = request.nlb_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindNlb',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/nlb',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindNlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_nlb(
        self,
        request: main_models.UnbindNlbRequest,
    ) -> main_models.UnbindNlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.unbind_nlb_with_options(request, headers, runtime)

    async def unbind_nlb_async(
        self,
        request: main_models.UnbindNlbRequest,
    ) -> main_models.UnbindNlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.unbind_nlb_with_options_async(request, headers, runtime)

    def unbind_slb_with_options(
        self,
        request: main_models.UnbindSlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnbindSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.internet):
            query['Internet'] = request.internet
        if not DaraCore.is_null(request.intranet):
            query['Intranet'] = request.intranet
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindSlb',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/slb',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_slb_with_options_async(
        self,
        request: main_models.UnbindSlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnbindSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.internet):
            query['Internet'] = request.internet
        if not DaraCore.is_null(request.intranet):
            query['Intranet'] = request.intranet
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindSlb',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/slb',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_slb(
        self,
        request: main_models.UnbindSlbRequest,
    ) -> main_models.UnbindSlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.unbind_slb_with_options(request, headers, runtime)

    async def unbind_slb_async(
        self,
        request: main_models.UnbindSlbRequest,
    ) -> main_models.UnbindSlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.unbind_slb_with_options_async(request, headers, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_all):
            query['DeleteAll'] = request.delete_all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/tags',
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
        if not DaraCore.is_null(request.delete_all):
            query['DeleteAll'] = request.delete_all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/tags',
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

    def update_app_mode_with_options(
        self,
        request: main_models.UpdateAppModeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.enable_idle):
            query['EnableIdle'] = request.enable_idle
        if not DaraCore.is_null(request.idle_hour):
            query['IdleHour'] = request.idle_hour
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppMode',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/updateAppMode',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_mode_with_options_async(
        self,
        request: main_models.UpdateAppModeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.enable_idle):
            query['EnableIdle'] = request.enable_idle
        if not DaraCore.is_null(request.idle_hour):
            query['IdleHour'] = request.idle_hour
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppMode',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/updateAppMode',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_mode(
        self,
        request: main_models.UpdateAppModeRequest,
    ) -> main_models.UpdateAppModeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_app_mode_with_options(request, headers, runtime)

    async def update_app_mode_async(
        self,
        request: main_models.UpdateAppModeRequest,
    ) -> main_models.UpdateAppModeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_app_mode_with_options_async(request, headers, runtime)

    def update_app_security_group_with_options(
        self,
        request: main_models.UpdateAppSecurityGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppSecurityGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppSecurityGroup',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/updateAppSecurityGroup',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_security_group_with_options_async(
        self,
        request: main_models.UpdateAppSecurityGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppSecurityGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppSecurityGroup',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/updateAppSecurityGroup',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppSecurityGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_security_group(
        self,
        request: main_models.UpdateAppSecurityGroupRequest,
    ) -> main_models.UpdateAppSecurityGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_app_security_group_with_options(request, headers, runtime)

    async def update_app_security_group_async(
        self,
        request: main_models.UpdateAppSecurityGroupRequest,
    ) -> main_models.UpdateAppSecurityGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_app_security_group_with_options_async(request, headers, runtime)

    def update_application_description_with_options(
        self,
        request: main_models.UpdateApplicationDescriptionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_description):
            query['AppDescription'] = request.app_description
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationDescription',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/updateAppDescription',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_description_with_options_async(
        self,
        request: main_models.UpdateApplicationDescriptionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_description):
            query['AppDescription'] = request.app_description
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationDescription',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/updateAppDescription',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_description(
        self,
        request: main_models.UpdateApplicationDescriptionRequest,
    ) -> main_models.UpdateApplicationDescriptionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_application_description_with_options(request, headers, runtime)

    async def update_application_description_async(
        self,
        request: main_models.UpdateApplicationDescriptionRequest,
    ) -> main_models.UpdateApplicationDescriptionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_application_description_with_options_async(request, headers, runtime)

    def update_application_scaling_rule_with_options(
        self,
        request: main_models.UpdateApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.enable_idle):
            query['EnableIdle'] = request.enable_idle
        if not DaraCore.is_null(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not DaraCore.is_null(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not DaraCore.is_null(request.scaling_rule_metric):
            query['ScalingRuleMetric'] = request.scaling_rule_metric
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not DaraCore.is_null(request.scaling_rule_timer):
            query['ScalingRuleTimer'] = request.scaling_rule_timer
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationScalingRule',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/scale/applicationScalingRule',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_scaling_rule_with_options_async(
        self,
        request: main_models.UpdateApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.enable_idle):
            query['EnableIdle'] = request.enable_idle
        if not DaraCore.is_null(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not DaraCore.is_null(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not DaraCore.is_null(request.scaling_rule_metric):
            query['ScalingRuleMetric'] = request.scaling_rule_metric
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not DaraCore.is_null(request.scaling_rule_timer):
            query['ScalingRuleTimer'] = request.scaling_rule_timer
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationScalingRule',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/scale/applicationScalingRule',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_scaling_rule(
        self,
        request: main_models.UpdateApplicationScalingRuleRequest,
    ) -> main_models.UpdateApplicationScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_application_scaling_rule_with_options(request, headers, runtime)

    async def update_application_scaling_rule_async(
        self,
        request: main_models.UpdateApplicationScalingRuleRequest,
    ) -> main_models.UpdateApplicationScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_application_scaling_rule_with_options_async(request, headers, runtime)

    def update_application_vswitches_with_options(
        self,
        request: main_models.UpdateApplicationVswitchesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationVswitchesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.deploy):
            query['Deploy'] = request.deploy
        if not DaraCore.is_null(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not DaraCore.is_null(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationVswitches',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/updateAppVswitches',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationVswitchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_vswitches_with_options_async(
        self,
        request: main_models.UpdateApplicationVswitchesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationVswitchesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.deploy):
            query['Deploy'] = request.deploy
        if not DaraCore.is_null(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not DaraCore.is_null(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationVswitches',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/updateAppVswitches',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationVswitchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_vswitches(
        self,
        request: main_models.UpdateApplicationVswitchesRequest,
    ) -> main_models.UpdateApplicationVswitchesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_application_vswitches_with_options(request, headers, runtime)

    async def update_application_vswitches_async(
        self,
        request: main_models.UpdateApplicationVswitchesRequest,
    ) -> main_models.UpdateApplicationVswitchesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_application_vswitches_with_options_async(request, headers, runtime)

    def update_config_map_with_options(
        self,
        request: main_models.UpdateConfigMapRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConfigMapResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_map_id):
            query['ConfigMapId'] = request.config_map_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        body = {}
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConfigMap',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/configmap/configMap',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConfigMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_config_map_with_options_async(
        self,
        request: main_models.UpdateConfigMapRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConfigMapResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_map_id):
            query['ConfigMapId'] = request.config_map_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        body = {}
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConfigMap',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/configmap/configMap',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConfigMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_config_map(
        self,
        request: main_models.UpdateConfigMapRequest,
    ) -> main_models.UpdateConfigMapResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_config_map_with_options(request, headers, runtime)

    async def update_config_map_async(
        self,
        request: main_models.UpdateConfigMapRequest,
    ) -> main_models.UpdateConfigMapResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_config_map_with_options_async(request, headers, runtime)

    def update_grey_tag_route_with_options(
        self,
        request: main_models.UpdateGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGreyTagRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alb_rules):
            query['AlbRules'] = request.alb_rules
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dubbo_rules):
            query['DubboRules'] = request.dubbo_rules
        if not DaraCore.is_null(request.grey_tag_route_id):
            query['GreyTagRouteId'] = request.grey_tag_route_id
        if not DaraCore.is_null(request.sc_rules):
            query['ScRules'] = request.sc_rules
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGreyTagRoute',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/tagroute/greyTagRoute',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGreyTagRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_grey_tag_route_with_options_async(
        self,
        request: main_models.UpdateGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGreyTagRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alb_rules):
            query['AlbRules'] = request.alb_rules
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dubbo_rules):
            query['DubboRules'] = request.dubbo_rules
        if not DaraCore.is_null(request.grey_tag_route_id):
            query['GreyTagRouteId'] = request.grey_tag_route_id
        if not DaraCore.is_null(request.sc_rules):
            query['ScRules'] = request.sc_rules
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGreyTagRoute',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/tagroute/greyTagRoute',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGreyTagRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_grey_tag_route(
        self,
        request: main_models.UpdateGreyTagRouteRequest,
    ) -> main_models.UpdateGreyTagRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_grey_tag_route_with_options(request, headers, runtime)

    async def update_grey_tag_route_async(
        self,
        request: main_models.UpdateGreyTagRouteRequest,
    ) -> main_models.UpdateGreyTagRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_grey_tag_route_with_options_async(request, headers, runtime)

    def update_ingress_with_options(
        self,
        request: main_models.UpdateIngressRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIngressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_id):
            query['CertId'] = request.cert_id
        if not DaraCore.is_null(request.cert_ids):
            query['CertIds'] = request.cert_ids
        if not DaraCore.is_null(request.cors_config):
            query['CorsConfig'] = request.cors_config
        if not DaraCore.is_null(request.default_rule):
            query['DefaultRule'] = request.default_rule
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_gzip):
            query['EnableGzip'] = request.enable_gzip
        if not DaraCore.is_null(request.enable_xforwarded_for):
            query['EnableXForwardedFor'] = request.enable_xforwarded_for
        if not DaraCore.is_null(request.enable_xforwarded_for_client_src_port):
            query['EnableXForwardedForClientSrcPort'] = request.enable_xforwarded_for_client_src_port
        if not DaraCore.is_null(request.enable_xforwarded_for_proto):
            query['EnableXForwardedForProto'] = request.enable_xforwarded_for_proto
        if not DaraCore.is_null(request.enable_xforwarded_for_slb_id):
            query['EnableXForwardedForSlbId'] = request.enable_xforwarded_for_slb_id
        if not DaraCore.is_null(request.enable_xforwarded_for_slb_port):
            query['EnableXForwardedForSlbPort'] = request.enable_xforwarded_for_slb_port
        if not DaraCore.is_null(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not DaraCore.is_null(request.ingress_id):
            query['IngressId'] = request.ingress_id
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not DaraCore.is_null(request.load_balance_type):
            query['LoadBalanceType'] = request.load_balance_type
        if not DaraCore.is_null(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not DaraCore.is_null(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        body = {}
        if not DaraCore.is_null(request.rules):
            body['Rules'] = request.rules
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIngress',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/ingress/Ingress',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIngressResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ingress_with_options_async(
        self,
        request: main_models.UpdateIngressRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIngressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_id):
            query['CertId'] = request.cert_id
        if not DaraCore.is_null(request.cert_ids):
            query['CertIds'] = request.cert_ids
        if not DaraCore.is_null(request.cors_config):
            query['CorsConfig'] = request.cors_config
        if not DaraCore.is_null(request.default_rule):
            query['DefaultRule'] = request.default_rule
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_gzip):
            query['EnableGzip'] = request.enable_gzip
        if not DaraCore.is_null(request.enable_xforwarded_for):
            query['EnableXForwardedFor'] = request.enable_xforwarded_for
        if not DaraCore.is_null(request.enable_xforwarded_for_client_src_port):
            query['EnableXForwardedForClientSrcPort'] = request.enable_xforwarded_for_client_src_port
        if not DaraCore.is_null(request.enable_xforwarded_for_proto):
            query['EnableXForwardedForProto'] = request.enable_xforwarded_for_proto
        if not DaraCore.is_null(request.enable_xforwarded_for_slb_id):
            query['EnableXForwardedForSlbId'] = request.enable_xforwarded_for_slb_id
        if not DaraCore.is_null(request.enable_xforwarded_for_slb_port):
            query['EnableXForwardedForSlbPort'] = request.enable_xforwarded_for_slb_port
        if not DaraCore.is_null(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not DaraCore.is_null(request.ingress_id):
            query['IngressId'] = request.ingress_id
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not DaraCore.is_null(request.load_balance_type):
            query['LoadBalanceType'] = request.load_balance_type
        if not DaraCore.is_null(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not DaraCore.is_null(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        body = {}
        if not DaraCore.is_null(request.rules):
            body['Rules'] = request.rules
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIngress',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/ingress/Ingress',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIngressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ingress(
        self,
        request: main_models.UpdateIngressRequest,
    ) -> main_models.UpdateIngressResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_ingress_with_options(request, headers, runtime)

    async def update_ingress_async(
        self,
        request: main_models.UpdateIngressRequest,
    ) -> main_models.UpdateIngressResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_ingress_with_options_async(request, headers, runtime)

    def update_job_with_options(
        self,
        request: main_models.UpdateJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.backoff_limit):
            query['BackoffLimit'] = request.backoff_limit
        if not DaraCore.is_null(request.best_effort_type):
            query['BestEffortType'] = request.best_effort_type
        if not DaraCore.is_null(request.command):
            query['Command'] = request.command
        if not DaraCore.is_null(request.command_args):
            query['CommandArgs'] = request.command_args
        if not DaraCore.is_null(request.concurrency_policy):
            query['ConcurrencyPolicy'] = request.concurrency_policy
        if not DaraCore.is_null(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not DaraCore.is_null(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not DaraCore.is_null(request.envs):
            query['Envs'] = request.envs
        if not DaraCore.is_null(request.image_pull_secrets):
            query['ImagePullSecrets'] = request.image_pull_secrets
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not DaraCore.is_null(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not DaraCore.is_null(request.jdk):
            query['Jdk'] = request.jdk
        if not DaraCore.is_null(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not DaraCore.is_null(request.mount_host):
            query['MountHost'] = request.mount_host
        if not DaraCore.is_null(request.nas_configs):
            query['NasConfigs'] = request.nas_configs
        if not DaraCore.is_null(request.nas_id):
            query['NasId'] = request.nas_id
        if not DaraCore.is_null(request.package_url):
            query['PackageUrl'] = request.package_url
        if not DaraCore.is_null(request.package_version):
            query['PackageVersion'] = request.package_version
        if not DaraCore.is_null(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not DaraCore.is_null(request.post_start):
            query['PostStart'] = request.post_start
        if not DaraCore.is_null(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not DaraCore.is_null(request.programming_language):
            query['ProgrammingLanguage'] = request.programming_language
        if not DaraCore.is_null(request.python):
            query['Python'] = request.python
        if not DaraCore.is_null(request.python_modules):
            query['PythonModules'] = request.python_modules
        if not DaraCore.is_null(request.ref_app_id):
            query['RefAppId'] = request.ref_app_id
        if not DaraCore.is_null(request.replicas):
            query['Replicas'] = request.replicas
        if not DaraCore.is_null(request.slice):
            query['Slice'] = request.slice
        if not DaraCore.is_null(request.slice_envs):
            query['SliceEnvs'] = request.slice_envs
        if not DaraCore.is_null(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not DaraCore.is_null(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        if not DaraCore.is_null(request.timezone):
            query['Timezone'] = request.timezone
        if not DaraCore.is_null(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not DaraCore.is_null(request.trigger_config):
            query['TriggerConfig'] = request.trigger_config
        if not DaraCore.is_null(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not DaraCore.is_null(request.web_container):
            query['WebContainer'] = request.web_container
        body = {}
        if not DaraCore.is_null(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not DaraCore.is_null(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not DaraCore.is_null(request.enable_image_accl):
            body['EnableImageAccl'] = request.enable_image_accl
        if not DaraCore.is_null(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not DaraCore.is_null(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not DaraCore.is_null(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not DaraCore.is_null(request.php):
            body['Php'] = request.php
        if not DaraCore.is_null(request.php_config):
            body['PhpConfig'] = request.php_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateJob',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/job/updateJob',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_job_with_options_async(
        self,
        request: main_models.UpdateJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.backoff_limit):
            query['BackoffLimit'] = request.backoff_limit
        if not DaraCore.is_null(request.best_effort_type):
            query['BestEffortType'] = request.best_effort_type
        if not DaraCore.is_null(request.command):
            query['Command'] = request.command
        if not DaraCore.is_null(request.command_args):
            query['CommandArgs'] = request.command_args
        if not DaraCore.is_null(request.concurrency_policy):
            query['ConcurrencyPolicy'] = request.concurrency_policy
        if not DaraCore.is_null(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not DaraCore.is_null(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not DaraCore.is_null(request.envs):
            query['Envs'] = request.envs
        if not DaraCore.is_null(request.image_pull_secrets):
            query['ImagePullSecrets'] = request.image_pull_secrets
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not DaraCore.is_null(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not DaraCore.is_null(request.jdk):
            query['Jdk'] = request.jdk
        if not DaraCore.is_null(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not DaraCore.is_null(request.mount_host):
            query['MountHost'] = request.mount_host
        if not DaraCore.is_null(request.nas_configs):
            query['NasConfigs'] = request.nas_configs
        if not DaraCore.is_null(request.nas_id):
            query['NasId'] = request.nas_id
        if not DaraCore.is_null(request.package_url):
            query['PackageUrl'] = request.package_url
        if not DaraCore.is_null(request.package_version):
            query['PackageVersion'] = request.package_version
        if not DaraCore.is_null(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not DaraCore.is_null(request.post_start):
            query['PostStart'] = request.post_start
        if not DaraCore.is_null(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not DaraCore.is_null(request.programming_language):
            query['ProgrammingLanguage'] = request.programming_language
        if not DaraCore.is_null(request.python):
            query['Python'] = request.python
        if not DaraCore.is_null(request.python_modules):
            query['PythonModules'] = request.python_modules
        if not DaraCore.is_null(request.ref_app_id):
            query['RefAppId'] = request.ref_app_id
        if not DaraCore.is_null(request.replicas):
            query['Replicas'] = request.replicas
        if not DaraCore.is_null(request.slice):
            query['Slice'] = request.slice
        if not DaraCore.is_null(request.slice_envs):
            query['SliceEnvs'] = request.slice_envs
        if not DaraCore.is_null(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not DaraCore.is_null(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        if not DaraCore.is_null(request.timezone):
            query['Timezone'] = request.timezone
        if not DaraCore.is_null(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not DaraCore.is_null(request.trigger_config):
            query['TriggerConfig'] = request.trigger_config
        if not DaraCore.is_null(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not DaraCore.is_null(request.web_container):
            query['WebContainer'] = request.web_container
        body = {}
        if not DaraCore.is_null(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not DaraCore.is_null(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not DaraCore.is_null(request.enable_image_accl):
            body['EnableImageAccl'] = request.enable_image_accl
        if not DaraCore.is_null(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not DaraCore.is_null(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not DaraCore.is_null(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not DaraCore.is_null(request.php):
            body['Php'] = request.php
        if not DaraCore.is_null(request.php_config):
            body['PhpConfig'] = request.php_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateJob',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/job/updateJob',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_job(
        self,
        request: main_models.UpdateJobRequest,
    ) -> main_models.UpdateJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_job_with_options(request, headers, runtime)

    async def update_job_async(
        self,
        request: main_models.UpdateJobRequest,
    ) -> main_models.UpdateJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_job_with_options_async(request, headers, runtime)

    def update_namespace_with_options(
        self,
        request: main_models.UpdateNamespaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_micro_registration):
            query['EnableMicroRegistration'] = request.enable_micro_registration
        if not DaraCore.is_null(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not DaraCore.is_null(request.namespace_description):
            query['NamespaceDescription'] = request.namespace_description
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNamespace',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/paas/namespace',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_namespace_with_options_async(
        self,
        request: main_models.UpdateNamespaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_micro_registration):
            query['EnableMicroRegistration'] = request.enable_micro_registration
        if not DaraCore.is_null(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not DaraCore.is_null(request.namespace_description):
            query['NamespaceDescription'] = request.namespace_description
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNamespace',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/paas/namespace',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_namespace(
        self,
        request: main_models.UpdateNamespaceRequest,
    ) -> main_models.UpdateNamespaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_namespace_with_options(request, headers, runtime)

    async def update_namespace_async(
        self,
        request: main_models.UpdateNamespaceRequest,
    ) -> main_models.UpdateNamespaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_namespace_with_options_async(request, headers, runtime)

    def update_namespace_sls_configs_with_options(
        self,
        request: main_models.UpdateNamespaceSlsConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNamespaceSlsConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not DaraCore.is_null(request.sls_log_env_tags):
            query['SlsLogEnvTags'] = request.sls_log_env_tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNamespaceSlsConfigs',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/cas/namespace/updateNamespaceSlsConfigs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNamespaceSlsConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_namespace_sls_configs_with_options_async(
        self,
        request: main_models.UpdateNamespaceSlsConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNamespaceSlsConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not DaraCore.is_null(request.sls_log_env_tags):
            query['SlsLogEnvTags'] = request.sls_log_env_tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNamespaceSlsConfigs',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/cas/namespace/updateNamespaceSlsConfigs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNamespaceSlsConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_namespace_sls_configs(
        self,
        request: main_models.UpdateNamespaceSlsConfigsRequest,
    ) -> main_models.UpdateNamespaceSlsConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_namespace_sls_configs_with_options(request, headers, runtime)

    async def update_namespace_sls_configs_async(
        self,
        request: main_models.UpdateNamespaceSlsConfigsRequest,
    ) -> main_models.UpdateNamespaceSlsConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_namespace_sls_configs_with_options_async(request, headers, runtime)

    def update_namespace_vpc_with_options(
        self,
        request: main_models.UpdateNamespaceVpcRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNamespaceVpcResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNamespaceVpc',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/namespace/updateNamespaceVpc',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNamespaceVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_namespace_vpc_with_options_async(
        self,
        request: main_models.UpdateNamespaceVpcRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNamespaceVpcResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNamespaceVpc',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/namespace/updateNamespaceVpc',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNamespaceVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_namespace_vpc(
        self,
        request: main_models.UpdateNamespaceVpcRequest,
    ) -> main_models.UpdateNamespaceVpcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_namespace_vpc_with_options(request, headers, runtime)

    async def update_namespace_vpc_async(
        self,
        request: main_models.UpdateNamespaceVpcRequest,
    ) -> main_models.UpdateNamespaceVpcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_namespace_vpc_with_options_async(request, headers, runtime)

    def update_secret_with_options(
        self,
        tmp_req: main_models.UpdateSecretRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecretResponse:
        tmp_req.validate()
        request = main_models.UpdateSecretShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.secret_data):
            request.secret_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.secret_data, 'SecretData', 'json')
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.secret_data_shrink):
            query['SecretData'] = request.secret_data_shrink
        if not DaraCore.is_null(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecret',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/secret/secret',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_secret_with_options_async(
        self,
        tmp_req: main_models.UpdateSecretRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecretResponse:
        tmp_req.validate()
        request = main_models.UpdateSecretShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.secret_data):
            request.secret_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.secret_data, 'SecretData', 'json')
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.secret_data_shrink):
            query['SecretData'] = request.secret_data_shrink
        if not DaraCore.is_null(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecret',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/secret/secret',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_secret(
        self,
        request: main_models.UpdateSecretRequest,
    ) -> main_models.UpdateSecretResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_secret_with_options(request, headers, runtime)

    async def update_secret_async(
        self,
        request: main_models.UpdateSecretRequest,
    ) -> main_models.UpdateSecretResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_secret_with_options_async(request, headers, runtime)

    def update_swimming_lane_enable_attribute_with_options(
        self,
        request: main_models.UpdateSwimmingLaneEnableAttributeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSwimmingLaneEnableAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.lane_id):
            query['LaneId'] = request.lane_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSwimmingLaneEnableAttribute',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/cas/gray/updateSwimmingLaneEnableAttribute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSwimmingLaneEnableAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_swimming_lane_enable_attribute_with_options_async(
        self,
        request: main_models.UpdateSwimmingLaneEnableAttributeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSwimmingLaneEnableAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.lane_id):
            query['LaneId'] = request.lane_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSwimmingLaneEnableAttribute',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/cas/gray/updateSwimmingLaneEnableAttribute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSwimmingLaneEnableAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_swimming_lane_enable_attribute(
        self,
        request: main_models.UpdateSwimmingLaneEnableAttributeRequest,
    ) -> main_models.UpdateSwimmingLaneEnableAttributeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_swimming_lane_enable_attribute_with_options(request, headers, runtime)

    async def update_swimming_lane_enable_attribute_async(
        self,
        request: main_models.UpdateSwimmingLaneEnableAttributeRequest,
    ) -> main_models.UpdateSwimmingLaneEnableAttributeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_swimming_lane_enable_attribute_with_options_async(request, headers, runtime)

    def update_web_application_with_options(
        self,
        application_id: str,
        request: main_models.UpdateWebApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWebApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWebApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/applications/{DaraURL.percent_encode(application_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWebApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_web_application_with_options_async(
        self,
        application_id: str,
        request: main_models.UpdateWebApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWebApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWebApplication',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/applications/{DaraURL.percent_encode(application_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWebApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_web_application(
        self,
        application_id: str,
        request: main_models.UpdateWebApplicationRequest,
    ) -> main_models.UpdateWebApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_web_application_with_options(application_id, request, headers, runtime)

    async def update_web_application_async(
        self,
        application_id: str,
        request: main_models.UpdateWebApplicationRequest,
    ) -> main_models.UpdateWebApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_web_application_with_options_async(application_id, request, headers, runtime)

    def update_web_application_scaling_config_with_options(
        self,
        application_id: str,
        request: main_models.UpdateWebApplicationScalingConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWebApplicationScalingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWebApplicationScalingConfig',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/application-scaling/{DaraURL.percent_encode(application_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWebApplicationScalingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_web_application_scaling_config_with_options_async(
        self,
        application_id: str,
        request: main_models.UpdateWebApplicationScalingConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWebApplicationScalingConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWebApplicationScalingConfig',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/application-scaling/{DaraURL.percent_encode(application_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWebApplicationScalingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_web_application_scaling_config(
        self,
        application_id: str,
        request: main_models.UpdateWebApplicationScalingConfigRequest,
    ) -> main_models.UpdateWebApplicationScalingConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_web_application_scaling_config_with_options(application_id, request, headers, runtime)

    async def update_web_application_scaling_config_async(
        self,
        application_id: str,
        request: main_models.UpdateWebApplicationScalingConfigRequest,
    ) -> main_models.UpdateWebApplicationScalingConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_web_application_scaling_config_with_options_async(application_id, request, headers, runtime)

    def update_web_application_traffic_config_with_options(
        self,
        application_id: str,
        request: main_models.UpdateWebApplicationTrafficConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWebApplicationTrafficConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWebApplicationTrafficConfig',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/application-traffic/{DaraURL.percent_encode(application_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWebApplicationTrafficConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_web_application_traffic_config_with_options_async(
        self,
        application_id: str,
        request: main_models.UpdateWebApplicationTrafficConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWebApplicationTrafficConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWebApplicationTrafficConfig',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/application-traffic/{DaraURL.percent_encode(application_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWebApplicationTrafficConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_web_application_traffic_config(
        self,
        application_id: str,
        request: main_models.UpdateWebApplicationTrafficConfigRequest,
    ) -> main_models.UpdateWebApplicationTrafficConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_web_application_traffic_config_with_options(application_id, request, headers, runtime)

    async def update_web_application_traffic_config_async(
        self,
        application_id: str,
        request: main_models.UpdateWebApplicationTrafficConfigRequest,
    ) -> main_models.UpdateWebApplicationTrafficConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_web_application_traffic_config_with_options_async(application_id, request, headers, runtime)

    def update_web_custom_domain_with_options(
        self,
        domain_name: str,
        request: main_models.UpdateWebCustomDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWebCustomDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWebCustomDomain',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/custom-domains/{DaraURL.percent_encode(domain_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWebCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_web_custom_domain_with_options_async(
        self,
        domain_name: str,
        request: main_models.UpdateWebCustomDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWebCustomDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWebCustomDomain',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v2/api/web/custom-domains/{DaraURL.percent_encode(domain_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWebCustomDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_web_custom_domain(
        self,
        domain_name: str,
        request: main_models.UpdateWebCustomDomainRequest,
    ) -> main_models.UpdateWebCustomDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_web_custom_domain_with_options(domain_name, request, headers, runtime)

    async def update_web_custom_domain_async(
        self,
        domain_name: str,
        request: main_models.UpdateWebCustomDomainRequest,
    ) -> main_models.UpdateWebCustomDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_web_custom_domain_with_options_async(domain_name, request, headers, runtime)

    def upgrade_application_apm_service_with_options(
        self,
        request: main_models.UpgradeApplicationApmServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeApplicationApmServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeApplicationApmService',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/applicationApmService',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeApplicationApmServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_application_apm_service_with_options_async(
        self,
        request: main_models.UpgradeApplicationApmServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeApplicationApmServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeApplicationApmService',
            version = '2019-05-06',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/sam/app/applicationApmService',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeApplicationApmServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_application_apm_service(
        self,
        request: main_models.UpgradeApplicationApmServiceRequest,
    ) -> main_models.UpgradeApplicationApmServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.upgrade_application_apm_service_with_options(request, headers, runtime)

    async def upgrade_application_apm_service_async(
        self,
        request: main_models.UpgradeApplicationApmServiceRequest,
    ) -> main_models.UpgradeApplicationApmServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.upgrade_application_apm_service_with_options_async(request, headers, runtime)
