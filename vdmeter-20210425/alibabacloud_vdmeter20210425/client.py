# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_vdmeter20210425 import models as vdmeter_20210425_models
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
        self._endpoint = self.get_endpoint('vdmeter', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_hu_ya_record_by_domain_with_options(
        self,
        request: vdmeter_20210425_models.DescribeHuYaRecordByDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeHuYaRecordByDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHuYaRecordByDomain',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeHuYaRecordByDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hu_ya_record_by_domain_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeHuYaRecordByDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeHuYaRecordByDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHuYaRecordByDomain',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeHuYaRecordByDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hu_ya_record_by_domain(
        self,
        request: vdmeter_20210425_models.DescribeHuYaRecordByDomainRequest,
    ) -> vdmeter_20210425_models.DescribeHuYaRecordByDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_hu_ya_record_by_domain_with_options(request, runtime)

    async def describe_hu_ya_record_by_domain_async(
        self,
        request: vdmeter_20210425_models.DescribeHuYaRecordByDomainRequest,
    ) -> vdmeter_20210425_models.DescribeHuYaRecordByDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_hu_ya_record_by_domain_with_options_async(request, runtime)

    def describe_hu_ya_screenshot_by_domain_with_options(
        self,
        request: vdmeter_20210425_models.DescribeHuYaScreenshotByDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeHuYaScreenshotByDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHuYaScreenshotByDomain',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeHuYaScreenshotByDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hu_ya_screenshot_by_domain_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeHuYaScreenshotByDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeHuYaScreenshotByDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHuYaScreenshotByDomain',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeHuYaScreenshotByDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hu_ya_screenshot_by_domain(
        self,
        request: vdmeter_20210425_models.DescribeHuYaScreenshotByDomainRequest,
    ) -> vdmeter_20210425_models.DescribeHuYaScreenshotByDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_hu_ya_screenshot_by_domain_with_options(request, runtime)

    async def describe_hu_ya_screenshot_by_domain_async(
        self,
        request: vdmeter_20210425_models.DescribeHuYaScreenshotByDomainRequest,
    ) -> vdmeter_20210425_models.DescribeHuYaScreenshotByDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_hu_ya_screenshot_by_domain_with_options_async(request, runtime)

    def describe_hu_ya_transcode_by_domain_with_options(
        self,
        request: vdmeter_20210425_models.DescribeHuYaTranscodeByDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeHuYaTranscodeByDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHuYaTranscodeByDomain',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeHuYaTranscodeByDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hu_ya_transcode_by_domain_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeHuYaTranscodeByDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeHuYaTranscodeByDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHuYaTranscodeByDomain',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeHuYaTranscodeByDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hu_ya_transcode_by_domain(
        self,
        request: vdmeter_20210425_models.DescribeHuYaTranscodeByDomainRequest,
    ) -> vdmeter_20210425_models.DescribeHuYaTranscodeByDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_hu_ya_transcode_by_domain_with_options(request, runtime)

    async def describe_hu_ya_transcode_by_domain_async(
        self,
        request: vdmeter_20210425_models.DescribeHuYaTranscodeByDomainRequest,
    ) -> vdmeter_20210425_models.DescribeHuYaTranscodeByDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_hu_ya_transcode_by_domain_with_options_async(request, runtime)

    def describe_meter_bypass_rt_usage_by_task_profile_with_options(
        self,
        request: vdmeter_20210425_models.DescribeMeterBypassRtUsageByTaskProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterBypassRtUsageByTaskProfileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterBypassRtUsageByTaskProfile',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterBypassRtUsageByTaskProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_bypass_rt_usage_by_task_profile_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterBypassRtUsageByTaskProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterBypassRtUsageByTaskProfileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterBypassRtUsageByTaskProfile',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterBypassRtUsageByTaskProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_bypass_rt_usage_by_task_profile(
        self,
        request: vdmeter_20210425_models.DescribeMeterBypassRtUsageByTaskProfileRequest,
    ) -> vdmeter_20210425_models.DescribeMeterBypassRtUsageByTaskProfileResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_bypass_rt_usage_by_task_profile_with_options(request, runtime)

    async def describe_meter_bypass_rt_usage_by_task_profile_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterBypassRtUsageByTaskProfileRequest,
    ) -> vdmeter_20210425_models.DescribeMeterBypassRtUsageByTaskProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_bypass_rt_usage_by_task_profile_with_options_async(request, runtime)

    def describe_meter_mpu_transcode_rt_usage_by_task_profile_with_options(
        self,
        request: vdmeter_20210425_models.DescribeMeterMpuTranscodeRtUsageByTaskProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterMpuTranscodeRtUsageByTaskProfileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterMpuTranscodeRtUsageByTaskProfile',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterMpuTranscodeRtUsageByTaskProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_mpu_transcode_rt_usage_by_task_profile_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterMpuTranscodeRtUsageByTaskProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterMpuTranscodeRtUsageByTaskProfileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterMpuTranscodeRtUsageByTaskProfile',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterMpuTranscodeRtUsageByTaskProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_mpu_transcode_rt_usage_by_task_profile(
        self,
        request: vdmeter_20210425_models.DescribeMeterMpuTranscodeRtUsageByTaskProfileRequest,
    ) -> vdmeter_20210425_models.DescribeMeterMpuTranscodeRtUsageByTaskProfileResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_mpu_transcode_rt_usage_by_task_profile_with_options(request, runtime)

    async def describe_meter_mpu_transcode_rt_usage_by_task_profile_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterMpuTranscodeRtUsageByTaskProfileRequest,
    ) -> vdmeter_20210425_models.DescribeMeterMpuTranscodeRtUsageByTaskProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_mpu_transcode_rt_usage_by_task_profile_with_options_async(request, runtime)

    def describe_meter_record_rt_usage_by_task_profile_with_options(
        self,
        request: vdmeter_20210425_models.DescribeMeterRecordRtUsageByTaskProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRecordRtUsageByTaskProfileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRecordRtUsageByTaskProfile',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRecordRtUsageByTaskProfileResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_record_rt_usage_by_task_profile_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRecordRtUsageByTaskProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRecordRtUsageByTaskProfileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRecordRtUsageByTaskProfile',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRecordRtUsageByTaskProfileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_record_rt_usage_by_task_profile(
        self,
        request: vdmeter_20210425_models.DescribeMeterRecordRtUsageByTaskProfileRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRecordRtUsageByTaskProfileResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_record_rt_usage_by_task_profile_with_options(request, runtime)

    async def describe_meter_record_rt_usage_by_task_profile_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRecordRtUsageByTaskProfileRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRecordRtUsageByTaskProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_record_rt_usage_by_task_profile_with_options_async(request, runtime)

    def describe_meter_rtc_approx_peak_rate_with_options(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcApproxPeakRateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcApproxPeakRateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRtcApproxPeakRate',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcApproxPeakRateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_rtc_approx_peak_rate_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcApproxPeakRateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcApproxPeakRateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRtcApproxPeakRate',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcApproxPeakRateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_rtc_approx_peak_rate(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcApproxPeakRateRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRtcApproxPeakRateResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_rtc_approx_peak_rate_with_options(request, runtime)

    async def describe_meter_rtc_approx_peak_rate_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcApproxPeakRateRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRtcApproxPeakRateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_rtc_approx_peak_rate_with_options_async(request, runtime)

    def describe_meter_rtc_channel_cnt_data_with_options(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcChannelCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcChannelCntDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRtcChannelCntData',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcChannelCntDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_rtc_channel_cnt_data_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcChannelCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcChannelCntDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRtcChannelCntData',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcChannelCntDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_rtc_channel_cnt_data(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcChannelCntDataRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRtcChannelCntDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_rtc_channel_cnt_data_with_options(request, runtime)

    async def describe_meter_rtc_channel_cnt_data_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcChannelCntDataRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRtcChannelCntDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_rtc_channel_cnt_data_with_options_async(request, runtime)

    def describe_meter_rtc_duration_with_options(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcDurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcDurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRtcDuration',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcDurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_rtc_duration_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcDurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcDurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRtcDuration',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcDurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_rtc_duration(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcDurationRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRtcDurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_rtc_duration_with_options(request, runtime)

    async def describe_meter_rtc_duration_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcDurationRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRtcDurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_rtc_duration_with_options_async(request, runtime)

    def describe_meter_rtc_peak_channel_cnt_data_with_options(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcPeakChannelCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcPeakChannelCntDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRtcPeakChannelCntData',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcPeakChannelCntDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_rtc_peak_channel_cnt_data_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcPeakChannelCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcPeakChannelCntDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRtcPeakChannelCntData',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcPeakChannelCntDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_rtc_peak_channel_cnt_data(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcPeakChannelCntDataRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRtcPeakChannelCntDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_rtc_peak_channel_cnt_data_with_options(request, runtime)

    async def describe_meter_rtc_peak_channel_cnt_data_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcPeakChannelCntDataRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRtcPeakChannelCntDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_rtc_peak_channel_cnt_data_with_options_async(request, runtime)

    def describe_meter_rtc_peak_user_cnt_data_with_options(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcPeakUserCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcPeakUserCntDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRtcPeakUserCntData',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcPeakUserCntDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_rtc_peak_user_cnt_data_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcPeakUserCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcPeakUserCntDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRtcPeakUserCntData',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcPeakUserCntDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_rtc_peak_user_cnt_data(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcPeakUserCntDataRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRtcPeakUserCntDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_rtc_peak_user_cnt_data_with_options(request, runtime)

    async def describe_meter_rtc_peak_user_cnt_data_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcPeakUserCntDataRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRtcPeakUserCntDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_rtc_peak_user_cnt_data_with_options_async(request, runtime)

    def describe_meter_rtc_rt_band_width_usage_with_options(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcRtBandWidthUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcRtBandWidthUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRtcRtBandWidthUsage',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcRtBandWidthUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_rtc_rt_band_width_usage_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcRtBandWidthUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcRtBandWidthUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRtcRtBandWidthUsage',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcRtBandWidthUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_rtc_rt_band_width_usage(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcRtBandWidthUsageRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRtcRtBandWidthUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_rtc_rt_band_width_usage_with_options(request, runtime)

    async def describe_meter_rtc_rt_band_width_usage_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcRtBandWidthUsageRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRtcRtBandWidthUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_rtc_rt_band_width_usage_with_options_async(request, runtime)

    def describe_meter_rtc_rt_flow_usage_with_options(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcRtFlowUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcRtFlowUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRtcRtFlowUsage',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcRtFlowUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_rtc_rt_flow_usage_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcRtFlowUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcRtFlowUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRtcRtFlowUsage',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcRtFlowUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_rtc_rt_flow_usage(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcRtFlowUsageRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRtcRtFlowUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_rtc_rt_flow_usage_with_options(request, runtime)

    async def describe_meter_rtc_rt_flow_usage_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcRtFlowUsageRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRtcRtFlowUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_rtc_rt_flow_usage_with_options_async(request, runtime)

    def describe_meter_rtc_user_cnt_data_with_options(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcUserCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcUserCntDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRtcUserCntData',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcUserCntDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_rtc_user_cnt_data_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcUserCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcUserCntDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRtcUserCntData',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcUserCntDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_rtc_user_cnt_data(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcUserCntDataRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRtcUserCntDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_rtc_user_cnt_data_with_options(request, runtime)

    async def describe_meter_rtc_user_cnt_data_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcUserCntDataRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRtcUserCntDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_rtc_user_cnt_data_with_options_async(request, runtime)

    def describe_new_play_video_play_session_event_detail_with_options(
        self,
        request: vdmeter_20210425_models.DescribeNewPlayVideoPlaySessionEventDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeNewPlayVideoPlaySessionEventDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_date):
            query['BizDate'] = request.biz_date
        if not UtilClient.is_unset(request.input_status):
            query['InputStatus'] = request.input_status
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.vps):
            query['VPS'] = request.vps
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNewPlayVideoPlaySessionEventDetail',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeNewPlayVideoPlaySessionEventDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_new_play_video_play_session_event_detail_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeNewPlayVideoPlaySessionEventDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeNewPlayVideoPlaySessionEventDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_date):
            query['BizDate'] = request.biz_date
        if not UtilClient.is_unset(request.input_status):
            query['InputStatus'] = request.input_status
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.vps):
            query['VPS'] = request.vps
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNewPlayVideoPlaySessionEventDetail',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeNewPlayVideoPlaySessionEventDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_new_play_video_play_session_event_detail(
        self,
        request: vdmeter_20210425_models.DescribeNewPlayVideoPlaySessionEventDetailRequest,
    ) -> vdmeter_20210425_models.DescribeNewPlayVideoPlaySessionEventDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_new_play_video_play_session_event_detail_with_options(request, runtime)

    async def describe_new_play_video_play_session_event_detail_async(
        self,
        request: vdmeter_20210425_models.DescribeNewPlayVideoPlaySessionEventDetailRequest,
    ) -> vdmeter_20210425_models.DescribeNewPlayVideoPlaySessionEventDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_new_play_video_play_session_event_detail_with_options_async(request, runtime)

    def describe_new_play_video_play_session_list_with_options(
        self,
        request: vdmeter_20210425_models.DescribeNewPlayVideoPlaySessionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeNewPlayVideoPlaySessionListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time_stamp):
            query['EndTimeStamp'] = request.end_time_stamp
        if not UtilClient.is_unset(request.input_status):
            query['InputStatus'] = request.input_status
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time_stamp):
            query['StartTimeStamp'] = request.start_time_stamp
        if not UtilClient.is_unset(request.unique_id):
            query['UniqueId'] = request.unique_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNewPlayVideoPlaySessionList',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeNewPlayVideoPlaySessionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_new_play_video_play_session_list_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeNewPlayVideoPlaySessionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeNewPlayVideoPlaySessionListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time_stamp):
            query['EndTimeStamp'] = request.end_time_stamp
        if not UtilClient.is_unset(request.input_status):
            query['InputStatus'] = request.input_status
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time_stamp):
            query['StartTimeStamp'] = request.start_time_stamp
        if not UtilClient.is_unset(request.unique_id):
            query['UniqueId'] = request.unique_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNewPlayVideoPlaySessionList',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeNewPlayVideoPlaySessionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_new_play_video_play_session_list(
        self,
        request: vdmeter_20210425_models.DescribeNewPlayVideoPlaySessionListRequest,
    ) -> vdmeter_20210425_models.DescribeNewPlayVideoPlaySessionListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_new_play_video_play_session_list_with_options(request, runtime)

    async def describe_new_play_video_play_session_list_async(
        self,
        request: vdmeter_20210425_models.DescribeNewPlayVideoPlaySessionListRequest,
    ) -> vdmeter_20210425_models.DescribeNewPlayVideoPlaySessionListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_new_play_video_play_session_list_with_options_async(request, runtime)

    def describe_new_play_video_play_sessioninfo_with_options(
        self,
        request: vdmeter_20210425_models.DescribeNewPlayVideoPlaySessioninfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeNewPlayVideoPlaySessioninfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vps):
            query['VPS'] = request.vps
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNewPlayVideoPlaySessioninfo',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeNewPlayVideoPlaySessioninfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_new_play_video_play_sessioninfo_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeNewPlayVideoPlaySessioninfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeNewPlayVideoPlaySessioninfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vps):
            query['VPS'] = request.vps
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNewPlayVideoPlaySessioninfo',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeNewPlayVideoPlaySessioninfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_new_play_video_play_sessioninfo(
        self,
        request: vdmeter_20210425_models.DescribeNewPlayVideoPlaySessioninfoRequest,
    ) -> vdmeter_20210425_models.DescribeNewPlayVideoPlaySessioninfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_new_play_video_play_sessioninfo_with_options(request, runtime)

    async def describe_new_play_video_play_sessioninfo_async(
        self,
        request: vdmeter_20210425_models.DescribeNewPlayVideoPlaySessioninfoRequest,
    ) -> vdmeter_20210425_models.DescribeNewPlayVideoPlaySessioninfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_new_play_video_play_sessioninfo_with_options_async(request, runtime)
