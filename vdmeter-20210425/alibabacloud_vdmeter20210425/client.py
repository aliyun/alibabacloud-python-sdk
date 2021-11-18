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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeHuYaRecordByDomainResponse(),
            self.do_rpcrequest('DescribeHuYaRecordByDomain', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_hu_ya_record_by_domain_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeHuYaRecordByDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeHuYaRecordByDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeHuYaRecordByDomainResponse(),
            await self.do_rpcrequest_async('DescribeHuYaRecordByDomain', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeHuYaScreenshotByDomainResponse(),
            self.do_rpcrequest('DescribeHuYaScreenshotByDomain', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_hu_ya_screenshot_by_domain_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeHuYaScreenshotByDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeHuYaScreenshotByDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeHuYaScreenshotByDomainResponse(),
            await self.do_rpcrequest_async('DescribeHuYaScreenshotByDomain', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeHuYaTranscodeByDomainResponse(),
            self.do_rpcrequest('DescribeHuYaTranscodeByDomain', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_hu_ya_transcode_by_domain_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeHuYaTranscodeByDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeHuYaTranscodeByDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeHuYaTranscodeByDomainResponse(),
            await self.do_rpcrequest_async('DescribeHuYaTranscodeByDomain', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterBypassRtUsageByTaskProfileResponse(),
            self.do_rpcrequest('DescribeMeterBypassRtUsageByTaskProfile', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_meter_bypass_rt_usage_by_task_profile_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterBypassRtUsageByTaskProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterBypassRtUsageByTaskProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterBypassRtUsageByTaskProfileResponse(),
            await self.do_rpcrequest_async('DescribeMeterBypassRtUsageByTaskProfile', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_meter_bypass_usage_by_task_profile_with_options(
        self,
        request: vdmeter_20210425_models.DescribeMeterBypassUsageByTaskProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterBypassUsageByTaskProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterBypassUsageByTaskProfileResponse(),
            self.do_rpcrequest('DescribeMeterBypassUsageByTaskProfile', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_meter_bypass_usage_by_task_profile_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterBypassUsageByTaskProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterBypassUsageByTaskProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterBypassUsageByTaskProfileResponse(),
            await self.do_rpcrequest_async('DescribeMeterBypassUsageByTaskProfile', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_meter_bypass_usage_by_task_profile(
        self,
        request: vdmeter_20210425_models.DescribeMeterBypassUsageByTaskProfileRequest,
    ) -> vdmeter_20210425_models.DescribeMeterBypassUsageByTaskProfileResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_bypass_usage_by_task_profile_with_options(request, runtime)

    async def describe_meter_bypass_usage_by_task_profile_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterBypassUsageByTaskProfileRequest,
    ) -> vdmeter_20210425_models.DescribeMeterBypassUsageByTaskProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_bypass_usage_by_task_profile_with_options_async(request, runtime)

    def describe_meter_mpu_transcode_rt_usage_by_task_profile_with_options(
        self,
        request: vdmeter_20210425_models.DescribeMeterMpuTranscodeRtUsageByTaskProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterMpuTranscodeRtUsageByTaskProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterMpuTranscodeRtUsageByTaskProfileResponse(),
            self.do_rpcrequest('DescribeMeterMpuTranscodeRtUsageByTaskProfile', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_meter_mpu_transcode_rt_usage_by_task_profile_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterMpuTranscodeRtUsageByTaskProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterMpuTranscodeRtUsageByTaskProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterMpuTranscodeRtUsageByTaskProfileResponse(),
            await self.do_rpcrequest_async('DescribeMeterMpuTranscodeRtUsageByTaskProfile', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRecordRtUsageByTaskProfileResponse(),
            self.do_rpcrequest('DescribeMeterRecordRtUsageByTaskProfile', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_meter_record_rt_usage_by_task_profile_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRecordRtUsageByTaskProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRecordRtUsageByTaskProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRecordRtUsageByTaskProfileResponse(),
            await self.do_rpcrequest_async('DescribeMeterRecordRtUsageByTaskProfile', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_meter_record_usage_by_task_profile_with_options(
        self,
        request: vdmeter_20210425_models.DescribeMeterRecordUsageByTaskProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRecordUsageByTaskProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRecordUsageByTaskProfileResponse(),
            self.do_rpcrequest('DescribeMeterRecordUsageByTaskProfile', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_meter_record_usage_by_task_profile_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRecordUsageByTaskProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRecordUsageByTaskProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRecordUsageByTaskProfileResponse(),
            await self.do_rpcrequest_async('DescribeMeterRecordUsageByTaskProfile', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_meter_record_usage_by_task_profile(
        self,
        request: vdmeter_20210425_models.DescribeMeterRecordUsageByTaskProfileRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRecordUsageByTaskProfileResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_record_usage_by_task_profile_with_options(request, runtime)

    async def describe_meter_record_usage_by_task_profile_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRecordUsageByTaskProfileRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRecordUsageByTaskProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_record_usage_by_task_profile_with_options_async(request, runtime)

    def describe_meter_rtc_approx_peak_rate_with_options(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcApproxPeakRateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcApproxPeakRateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcApproxPeakRateResponse(),
            self.do_rpcrequest('DescribeMeterRtcApproxPeakRate', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_meter_rtc_approx_peak_rate_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcApproxPeakRateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcApproxPeakRateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcApproxPeakRateResponse(),
            await self.do_rpcrequest_async('DescribeMeterRtcApproxPeakRate', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_meter_rtc_band_width_usage_with_options(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcBandWidthUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcBandWidthUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcBandWidthUsageResponse(),
            self.do_rpcrequest('DescribeMeterRtcBandWidthUsage', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_meter_rtc_band_width_usage_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcBandWidthUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcBandWidthUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcBandWidthUsageResponse(),
            await self.do_rpcrequest_async('DescribeMeterRtcBandWidthUsage', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_meter_rtc_band_width_usage(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcBandWidthUsageRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRtcBandWidthUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_rtc_band_width_usage_with_options(request, runtime)

    async def describe_meter_rtc_band_width_usage_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcBandWidthUsageRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRtcBandWidthUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_rtc_band_width_usage_with_options_async(request, runtime)

    def describe_meter_rtc_channel_cnt_data_with_options(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcChannelCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcChannelCntDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcChannelCntDataResponse(),
            self.do_rpcrequest('DescribeMeterRtcChannelCntData', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_meter_rtc_channel_cnt_data_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcChannelCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcChannelCntDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcChannelCntDataResponse(),
            await self.do_rpcrequest_async('DescribeMeterRtcChannelCntData', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcDurationResponse(),
            self.do_rpcrequest('DescribeMeterRtcDuration', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_meter_rtc_duration_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcDurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcDurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcDurationResponse(),
            await self.do_rpcrequest_async('DescribeMeterRtcDuration', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_meter_rtc_duration_by_app_id_with_options(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcDurationByAppIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcDurationByAppIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcDurationByAppIdResponse(),
            self.do_rpcrequest('DescribeMeterRtcDurationByAppId', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_meter_rtc_duration_by_app_id_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcDurationByAppIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcDurationByAppIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcDurationByAppIdResponse(),
            await self.do_rpcrequest_async('DescribeMeterRtcDurationByAppId', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_meter_rtc_duration_by_app_id(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcDurationByAppIdRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRtcDurationByAppIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_rtc_duration_by_app_id_with_options(request, runtime)

    async def describe_meter_rtc_duration_by_app_id_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcDurationByAppIdRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRtcDurationByAppIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_rtc_duration_by_app_id_with_options_async(request, runtime)

    def describe_meter_rtc_flow_usage_with_options(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcFlowUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcFlowUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcFlowUsageResponse(),
            self.do_rpcrequest('DescribeMeterRtcFlowUsage', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_meter_rtc_flow_usage_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcFlowUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcFlowUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcFlowUsageResponse(),
            await self.do_rpcrequest_async('DescribeMeterRtcFlowUsage', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_meter_rtc_flow_usage(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcFlowUsageRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRtcFlowUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_rtc_flow_usage_with_options(request, runtime)

    async def describe_meter_rtc_flow_usage_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcFlowUsageRequest,
    ) -> vdmeter_20210425_models.DescribeMeterRtcFlowUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_rtc_flow_usage_with_options_async(request, runtime)

    def describe_meter_rtc_peak_channel_cnt_data_with_options(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcPeakChannelCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcPeakChannelCntDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcPeakChannelCntDataResponse(),
            self.do_rpcrequest('DescribeMeterRtcPeakChannelCntData', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_meter_rtc_peak_channel_cnt_data_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcPeakChannelCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcPeakChannelCntDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcPeakChannelCntDataResponse(),
            await self.do_rpcrequest_async('DescribeMeterRtcPeakChannelCntData', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcPeakUserCntDataResponse(),
            self.do_rpcrequest('DescribeMeterRtcPeakUserCntData', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_meter_rtc_peak_user_cnt_data_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcPeakUserCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcPeakUserCntDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcPeakUserCntDataResponse(),
            await self.do_rpcrequest_async('DescribeMeterRtcPeakUserCntData', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcRtBandWidthUsageResponse(),
            self.do_rpcrequest('DescribeMeterRtcRtBandWidthUsage', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_meter_rtc_rt_band_width_usage_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcRtBandWidthUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcRtBandWidthUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcRtBandWidthUsageResponse(),
            await self.do_rpcrequest_async('DescribeMeterRtcRtBandWidthUsage', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcRtFlowUsageResponse(),
            self.do_rpcrequest('DescribeMeterRtcRtFlowUsage', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_meter_rtc_rt_flow_usage_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcRtFlowUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcRtFlowUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcRtFlowUsageResponse(),
            await self.do_rpcrequest_async('DescribeMeterRtcRtFlowUsage', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcUserCntDataResponse(),
            self.do_rpcrequest('DescribeMeterRtcUserCntData', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_meter_rtc_user_cnt_data_with_options_async(
        self,
        request: vdmeter_20210425_models.DescribeMeterRtcUserCntDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vdmeter_20210425_models.DescribeMeterRtcUserCntDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcUserCntDataResponse(),
            await self.do_rpcrequest_async('DescribeMeterRtcUserCntData', '2021-04-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
