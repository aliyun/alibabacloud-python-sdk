# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_safe20220116 import models as safe_20220116_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('safe', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_alarm_event_with_options(
        self,
        request: safe_20220116_models.CreateAlarmEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220116_models.CreateAlarmEventResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_id):
            body['AlarmId'] = request.alarm_id
        if not UtilClient.is_unset(request.alarm_timestamp):
            body['AlarmTimestamp'] = request.alarm_timestamp
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.app_secret):
            body['AppSecret'] = request.app_secret
        if not UtilClient.is_unset(request.attach):
            body['Attach'] = request.attach
        if not UtilClient.is_unset(request.dynamic_alarm_id):
            body['DynamicAlarmId'] = request.dynamic_alarm_id
        if not UtilClient.is_unset(request.impact):
            body['Impact'] = request.impact
        if not UtilClient.is_unset(request.link):
            body['Link'] = request.link
        if not UtilClient.is_unset(request.message):
            body['Message'] = request.message
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.source_key):
            body['SourceKey'] = request.source_key
        if not UtilClient.is_unset(request.source_system):
            body['SourceSystem'] = request.source_system
        if not UtilClient.is_unset(request.strategy):
            body['Strategy'] = request.strategy
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.uid):
            body['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAlarmEvent',
            version='2022-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220116_models.CreateAlarmEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alarm_event_with_options_async(
        self,
        request: safe_20220116_models.CreateAlarmEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220116_models.CreateAlarmEventResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_id):
            body['AlarmId'] = request.alarm_id
        if not UtilClient.is_unset(request.alarm_timestamp):
            body['AlarmTimestamp'] = request.alarm_timestamp
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.app_secret):
            body['AppSecret'] = request.app_secret
        if not UtilClient.is_unset(request.attach):
            body['Attach'] = request.attach
        if not UtilClient.is_unset(request.dynamic_alarm_id):
            body['DynamicAlarmId'] = request.dynamic_alarm_id
        if not UtilClient.is_unset(request.impact):
            body['Impact'] = request.impact
        if not UtilClient.is_unset(request.link):
            body['Link'] = request.link
        if not UtilClient.is_unset(request.message):
            body['Message'] = request.message
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.source_key):
            body['SourceKey'] = request.source_key
        if not UtilClient.is_unset(request.source_system):
            body['SourceSystem'] = request.source_system
        if not UtilClient.is_unset(request.strategy):
            body['Strategy'] = request.strategy
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.uid):
            body['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAlarmEvent',
            version='2022-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220116_models.CreateAlarmEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alarm_event(
        self,
        request: safe_20220116_models.CreateAlarmEventRequest,
    ) -> safe_20220116_models.CreateAlarmEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_alarm_event_with_options(request, runtime)

    async def create_alarm_event_async(
        self,
        request: safe_20220116_models.CreateAlarmEventRequest,
    ) -> safe_20220116_models.CreateAlarmEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_alarm_event_with_options_async(request, runtime)

    def get_fault_detail_with_options(
        self,
        request: safe_20220116_models.GetFaultDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220116_models.GetFaultDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFaultDetail',
            version='2022-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220116_models.GetFaultDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fault_detail_with_options_async(
        self,
        request: safe_20220116_models.GetFaultDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220116_models.GetFaultDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFaultDetail',
            version='2022-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220116_models.GetFaultDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fault_detail(
        self,
        request: safe_20220116_models.GetFaultDetailRequest,
    ) -> safe_20220116_models.GetFaultDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_fault_detail_with_options(request, runtime)

    async def get_fault_detail_async(
        self,
        request: safe_20220116_models.GetFaultDetailRequest,
    ) -> safe_20220116_models.GetFaultDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_fault_detail_with_options_async(request, runtime)

    def report_influence_with_options(
        self,
        request: safe_20220116_models.ReportInfluenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220116_models.ReportInfluenceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.app_secret):
            body['AppSecret'] = request.app_secret
        if not UtilClient.is_unset(request.area):
            body['Area'] = request.area
        if not UtilClient.is_unset(request.channel_code):
            body['ChannelCode'] = request.channel_code
        if not UtilClient.is_unset(request.cluster):
            body['Cluster'] = request.cluster
        if not UtilClient.is_unset(request.create_id):
            body['CreateId'] = request.create_id
        if not UtilClient.is_unset(request.customer_impact_desc):
            body['CustomerImpactDesc'] = request.customer_impact_desc
        if not UtilClient.is_unset(request.fault_vid):
            body['FaultVid'] = request.fault_vid
        if not UtilClient.is_unset(request.issue_desc):
            body['IssueDesc'] = request.issue_desc
        if not UtilClient.is_unset(request.product_line_id):
            body['ProductLineId'] = request.product_line_id
        if not UtilClient.is_unset(request.regions):
            body['Regions'] = request.regions
        if not UtilClient.is_unset(request.room):
            body['Room'] = request.room
        if not UtilClient.is_unset(request.time):
            body['Time'] = request.time
        if not UtilClient.is_unset(request.total_desc):
            body['TotalDesc'] = request.total_desc
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReportInfluence',
            version='2022-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220116_models.ReportInfluenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_influence_with_options_async(
        self,
        request: safe_20220116_models.ReportInfluenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220116_models.ReportInfluenceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.app_secret):
            body['AppSecret'] = request.app_secret
        if not UtilClient.is_unset(request.area):
            body['Area'] = request.area
        if not UtilClient.is_unset(request.channel_code):
            body['ChannelCode'] = request.channel_code
        if not UtilClient.is_unset(request.cluster):
            body['Cluster'] = request.cluster
        if not UtilClient.is_unset(request.create_id):
            body['CreateId'] = request.create_id
        if not UtilClient.is_unset(request.customer_impact_desc):
            body['CustomerImpactDesc'] = request.customer_impact_desc
        if not UtilClient.is_unset(request.fault_vid):
            body['FaultVid'] = request.fault_vid
        if not UtilClient.is_unset(request.issue_desc):
            body['IssueDesc'] = request.issue_desc
        if not UtilClient.is_unset(request.product_line_id):
            body['ProductLineId'] = request.product_line_id
        if not UtilClient.is_unset(request.regions):
            body['Regions'] = request.regions
        if not UtilClient.is_unset(request.room):
            body['Room'] = request.room
        if not UtilClient.is_unset(request.time):
            body['Time'] = request.time
        if not UtilClient.is_unset(request.total_desc):
            body['TotalDesc'] = request.total_desc
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReportInfluence',
            version='2022-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220116_models.ReportInfluenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_influence(
        self,
        request: safe_20220116_models.ReportInfluenceRequest,
    ) -> safe_20220116_models.ReportInfluenceResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_influence_with_options(request, runtime)

    async def report_influence_async(
        self,
        request: safe_20220116_models.ReportInfluenceRequest,
    ) -> safe_20220116_models.ReportInfluenceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_influence_with_options_async(request, runtime)

    def report_reason_detail_with_options(
        self,
        request: safe_20220116_models.ReportReasonDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220116_models.ReportReasonDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.app_secret):
            body['AppSecret'] = request.app_secret
        if not UtilClient.is_unset(request.channel_code):
            body['ChannelCode'] = request.channel_code
        if not UtilClient.is_unset(request.create_id):
            body['CreateId'] = request.create_id
        if not UtilClient.is_unset(request.detail_url):
            body['DetailUrl'] = request.detail_url
        if not UtilClient.is_unset(request.fault_vid):
            body['FaultVid'] = request.fault_vid
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReportReasonDetail',
            version='2022-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220116_models.ReportReasonDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_reason_detail_with_options_async(
        self,
        request: safe_20220116_models.ReportReasonDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220116_models.ReportReasonDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.app_secret):
            body['AppSecret'] = request.app_secret
        if not UtilClient.is_unset(request.channel_code):
            body['ChannelCode'] = request.channel_code
        if not UtilClient.is_unset(request.create_id):
            body['CreateId'] = request.create_id
        if not UtilClient.is_unset(request.detail_url):
            body['DetailUrl'] = request.detail_url
        if not UtilClient.is_unset(request.fault_vid):
            body['FaultVid'] = request.fault_vid
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReportReasonDetail',
            version='2022-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220116_models.ReportReasonDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_reason_detail(
        self,
        request: safe_20220116_models.ReportReasonDetailRequest,
    ) -> safe_20220116_models.ReportReasonDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_reason_detail_with_options(request, runtime)

    async def report_reason_detail_async(
        self,
        request: safe_20220116_models.ReportReasonDetailRequest,
    ) -> safe_20220116_models.ReportReasonDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_reason_detail_with_options_async(request, runtime)

    def report_recover_action_with_options(
        self,
        request: safe_20220116_models.ReportRecoverActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220116_models.ReportRecoverActionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action_type):
            body['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.app_secret):
            body['AppSecret'] = request.app_secret
        if not UtilClient.is_unset(request.channel_code):
            body['ChannelCode'] = request.channel_code
        if not UtilClient.is_unset(request.create_id):
            body['CreateId'] = request.create_id
        if not UtilClient.is_unset(request.current_desc):
            body['CurrentDesc'] = request.current_desc
        if not UtilClient.is_unset(request.current_progress):
            body['CurrentProgress'] = request.current_progress
        if not UtilClient.is_unset(request.expected_repaired_time):
            body['ExpectedRepairedTime'] = request.expected_repaired_time
        if not UtilClient.is_unset(request.fault_vid):
            body['FaultVid'] = request.fault_vid
        if not UtilClient.is_unset(request.is_recovery):
            body['IsRecovery'] = request.is_recovery
        if not UtilClient.is_unset(request.product_line_id):
            body['ProductLineId'] = request.product_line_id
        if not UtilClient.is_unset(request.recovery_duration):
            body['RecoveryDuration'] = request.recovery_duration
        if not UtilClient.is_unset(request.recovery_time):
            body['RecoveryTime'] = request.recovery_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReportRecoverAction',
            version='2022-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220116_models.ReportRecoverActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_recover_action_with_options_async(
        self,
        request: safe_20220116_models.ReportRecoverActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> safe_20220116_models.ReportRecoverActionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action_type):
            body['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.app_secret):
            body['AppSecret'] = request.app_secret
        if not UtilClient.is_unset(request.channel_code):
            body['ChannelCode'] = request.channel_code
        if not UtilClient.is_unset(request.create_id):
            body['CreateId'] = request.create_id
        if not UtilClient.is_unset(request.current_desc):
            body['CurrentDesc'] = request.current_desc
        if not UtilClient.is_unset(request.current_progress):
            body['CurrentProgress'] = request.current_progress
        if not UtilClient.is_unset(request.expected_repaired_time):
            body['ExpectedRepairedTime'] = request.expected_repaired_time
        if not UtilClient.is_unset(request.fault_vid):
            body['FaultVid'] = request.fault_vid
        if not UtilClient.is_unset(request.is_recovery):
            body['IsRecovery'] = request.is_recovery
        if not UtilClient.is_unset(request.product_line_id):
            body['ProductLineId'] = request.product_line_id
        if not UtilClient.is_unset(request.recovery_duration):
            body['RecoveryDuration'] = request.recovery_duration
        if not UtilClient.is_unset(request.recovery_time):
            body['RecoveryTime'] = request.recovery_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReportRecoverAction',
            version='2022-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            safe_20220116_models.ReportRecoverActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_recover_action(
        self,
        request: safe_20220116_models.ReportRecoverActionRequest,
    ) -> safe_20220116_models.ReportRecoverActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_recover_action_with_options(request, runtime)

    async def report_recover_action_async(
        self,
        request: safe_20220116_models.ReportRecoverActionRequest,
    ) -> safe_20220116_models.ReportRecoverActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_recover_action_with_options_async(request, runtime)
