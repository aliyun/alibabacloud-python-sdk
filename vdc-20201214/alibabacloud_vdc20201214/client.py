# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_vdc20201214 import models as vdc_20201214_models
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
        self._endpoint = self.get_endpoint('vdc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_fault_diagnosis_overall_data(
        self,
        request: vdc_20201214_models.DescribeFaultDiagnosisOverallDataRequest,
    ) -> vdc_20201214_models.DescribeFaultDiagnosisOverallDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_fault_diagnosis_overall_data_with_options(request, headers, runtime)

    async def describe_fault_diagnosis_overall_data_async(
        self,
        request: vdc_20201214_models.DescribeFaultDiagnosisOverallDataRequest,
    ) -> vdc_20201214_models.DescribeFaultDiagnosisOverallDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_fault_diagnosis_overall_data_with_options_async(request, headers, runtime)

    def describe_fault_diagnosis_overall_data_with_options(
        self,
        request: vdc_20201214_models.DescribeFaultDiagnosisOverallDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeFaultDiagnosisOverallDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeFaultDiagnosisOverallDataResponse(),
            self.do_roarequest('DescribeFaultDiagnosisOverallData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/diagnosis/describeFaultDiagnosisOverallData', 'json', req, runtime)
        )

    async def describe_fault_diagnosis_overall_data_with_options_async(
        self,
        request: vdc_20201214_models.DescribeFaultDiagnosisOverallDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeFaultDiagnosisOverallDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeFaultDiagnosisOverallDataResponse(),
            await self.do_roarequest_async('DescribeFaultDiagnosisOverallData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/diagnosis/describeFaultDiagnosisOverallData', 'json', req, runtime)
        )

    def describe_rtc_channel_users(
        self,
        request: vdc_20201214_models.DescribeRtcChannelUsersRequest,
    ) -> vdc_20201214_models.DescribeRtcChannelUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_rtc_channel_users_with_options(request, headers, runtime)

    async def describe_rtc_channel_users_async(
        self,
        request: vdc_20201214_models.DescribeRtcChannelUsersRequest,
    ) -> vdc_20201214_models.DescribeRtcChannelUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_rtc_channel_users_with_options_async(request, headers, runtime)

    def describe_rtc_channel_users_with_options(
        self,
        request: vdc_20201214_models.DescribeRtcChannelUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeRtcChannelUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.time_point):
            query['TimePoint'] = request.time_point
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeRtcChannelUsersResponse(),
            self.do_roarequest('DescribeRtcChannelUsers', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/channel/describeRtcChannelUsers', 'json', req, runtime)
        )

    async def describe_rtc_channel_users_with_options_async(
        self,
        request: vdc_20201214_models.DescribeRtcChannelUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeRtcChannelUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.time_point):
            query['TimePoint'] = request.time_point
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeRtcChannelUsersResponse(),
            await self.do_roarequest_async('DescribeRtcChannelUsers', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/channel/describeRtcChannelUsers', 'json', req, runtime)
        )

    def describe_channel_overall_data(
        self,
        request: vdc_20201214_models.DescribeChannelOverallDataRequest,
    ) -> vdc_20201214_models.DescribeChannelOverallDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_channel_overall_data_with_options(request, headers, runtime)

    async def describe_channel_overall_data_async(
        self,
        request: vdc_20201214_models.DescribeChannelOverallDataRequest,
    ) -> vdc_20201214_models.DescribeChannelOverallDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_channel_overall_data_with_options_async(request, headers, runtime)

    def describe_channel_overall_data_with_options(
        self,
        request: vdc_20201214_models.DescribeChannelOverallDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeChannelOverallDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeChannelOverallDataResponse(),
            self.do_roarequest('DescribeChannelOverallData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/channel/describeChannelOverallData', 'json', req, runtime)
        )

    async def describe_channel_overall_data_with_options_async(
        self,
        request: vdc_20201214_models.DescribeChannelOverallDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeChannelOverallDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeChannelOverallDataResponse(),
            await self.do_roarequest_async('DescribeChannelOverallData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/channel/describeChannelOverallData', 'json', req, runtime)
        )

    def describe_usage_os_sdk_version_distribution_stat_data(
        self,
        request: vdc_20201214_models.DescribeUsageOsSdkVersionDistributionStatDataRequest,
    ) -> vdc_20201214_models.DescribeUsageOsSdkVersionDistributionStatDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_usage_os_sdk_version_distribution_stat_data_with_options(request, headers, runtime)

    async def describe_usage_os_sdk_version_distribution_stat_data_async(
        self,
        request: vdc_20201214_models.DescribeUsageOsSdkVersionDistributionStatDataRequest,
    ) -> vdc_20201214_models.DescribeUsageOsSdkVersionDistributionStatDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_usage_os_sdk_version_distribution_stat_data_with_options_async(request, headers, runtime)

    def describe_usage_os_sdk_version_distribution_stat_data_with_options(
        self,
        request: vdc_20201214_models.DescribeUsageOsSdkVersionDistributionStatDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeUsageOsSdkVersionDistributionStatDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeUsageOsSdkVersionDistributionStatDataResponse(),
            self.do_roarequest('DescribeUsageOsSdkVersionDistributionStatData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/usage/describeUsageOsSdkVersionDistributionStatData', 'json', req, runtime)
        )

    async def describe_usage_os_sdk_version_distribution_stat_data_with_options_async(
        self,
        request: vdc_20201214_models.DescribeUsageOsSdkVersionDistributionStatDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeUsageOsSdkVersionDistributionStatDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeUsageOsSdkVersionDistributionStatDataResponse(),
            await self.do_roarequest_async('DescribeUsageOsSdkVersionDistributionStatData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/usage/describeUsageOsSdkVersionDistributionStatData', 'json', req, runtime)
        )

    def describe_ice_dur_period_by_day_sub_type(
        self,
        request: vdc_20201214_models.DescribeIceDurPeriodByDaySubTypeRequest,
    ) -> vdc_20201214_models.DescribeIceDurPeriodByDaySubTypeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_ice_dur_period_by_day_sub_type_with_options(request, headers, runtime)

    async def describe_ice_dur_period_by_day_sub_type_async(
        self,
        request: vdc_20201214_models.DescribeIceDurPeriodByDaySubTypeRequest,
    ) -> vdc_20201214_models.DescribeIceDurPeriodByDaySubTypeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_ice_dur_period_by_day_sub_type_with_options_async(request, headers, runtime)

    def describe_ice_dur_period_by_day_sub_type_with_options(
        self,
        request: vdc_20201214_models.DescribeIceDurPeriodByDaySubTypeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeIceDurPeriodByDaySubTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.time_zone):
            query['TimeZone'] = request.time_zone
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeIceDurPeriodByDaySubTypeResponse(),
            self.do_roarequest('DescribeIceDurPeriodByDaySubType', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/ice/describeIceDurPeriodByDaySubType', 'json', req, runtime)
        )

    async def describe_ice_dur_period_by_day_sub_type_with_options_async(
        self,
        request: vdc_20201214_models.DescribeIceDurPeriodByDaySubTypeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeIceDurPeriodByDaySubTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.time_zone):
            query['TimeZone'] = request.time_zone
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeIceDurPeriodByDaySubTypeResponse(),
            await self.do_roarequest_async('DescribeIceDurPeriodByDaySubType', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/ice/describeIceDurPeriodByDaySubType', 'json', req, runtime)
        )

    def describe_call_list(
        self,
        request: vdc_20201214_models.DescribeCallListRequest,
    ) -> vdc_20201214_models.DescribeCallListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_call_list_with_options(request, headers, runtime)

    async def describe_call_list_async(
        self,
        request: vdc_20201214_models.DescribeCallListRequest,
    ) -> vdc_20201214_models.DescribeCallListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_call_list_with_options_async(request, headers, runtime)

    def describe_call_list_with_options(
        self,
        request: vdc_20201214_models.DescribeCallListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeCallListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.call_status):
            query['CallStatus'] = request.call_status
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.query_mode):
            query['QueryMode'] = request.query_mode
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeCallListResponse(),
            self.do_roarequest('DescribeCallList', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/call/describeCallList', 'json', req, runtime)
        )

    async def describe_call_list_with_options_async(
        self,
        request: vdc_20201214_models.DescribeCallListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeCallListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.call_status):
            query['CallStatus'] = request.call_status
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.query_mode):
            query['QueryMode'] = request.query_mode
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeCallListResponse(),
            await self.do_roarequest_async('DescribeCallList', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/call/describeCallList', 'json', req, runtime)
        )

    def describe_quality_area_distribution_stat_data(
        self,
        request: vdc_20201214_models.DescribeQualityAreaDistributionStatDataRequest,
    ) -> vdc_20201214_models.DescribeQualityAreaDistributionStatDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_quality_area_distribution_stat_data_with_options(request, headers, runtime)

    async def describe_quality_area_distribution_stat_data_async(
        self,
        request: vdc_20201214_models.DescribeQualityAreaDistributionStatDataRequest,
    ) -> vdc_20201214_models.DescribeQualityAreaDistributionStatDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_quality_area_distribution_stat_data_with_options_async(request, headers, runtime)

    def describe_quality_area_distribution_stat_data_with_options(
        self,
        request: vdc_20201214_models.DescribeQualityAreaDistributionStatDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeQualityAreaDistributionStatDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.parent_area):
            query['ParentArea'] = request.parent_area
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeQualityAreaDistributionStatDataResponse(),
            self.do_roarequest('DescribeQualityAreaDistributionStatData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/quality/describeQualityAreaDistributionStatData', 'json', req, runtime)
        )

    async def describe_quality_area_distribution_stat_data_with_options_async(
        self,
        request: vdc_20201214_models.DescribeQualityAreaDistributionStatDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeQualityAreaDistributionStatDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.parent_area):
            query['ParentArea'] = request.parent_area
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeQualityAreaDistributionStatDataResponse(),
            await self.do_roarequest_async('DescribeQualityAreaDistributionStatData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/quality/describeQualityAreaDistributionStatData', 'json', req, runtime)
        )

    def describe_rtc_user_event_list(
        self,
        request: vdc_20201214_models.DescribeRtcUserEventListRequest,
    ) -> vdc_20201214_models.DescribeRtcUserEventListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_rtc_user_event_list_with_options(request, headers, runtime)

    async def describe_rtc_user_event_list_async(
        self,
        request: vdc_20201214_models.DescribeRtcUserEventListRequest,
    ) -> vdc_20201214_models.DescribeRtcUserEventListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_rtc_user_event_list_with_options_async(request, headers, runtime)

    def describe_rtc_user_event_list_with_options(
        self,
        request: vdc_20201214_models.DescribeRtcUserEventListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeRtcUserEventListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeRtcUserEventListResponse(),
            self.do_roarequest('DescribeRtcUserEventList', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/call/describeRtcUserEventList', 'json', req, runtime)
        )

    async def describe_rtc_user_event_list_with_options_async(
        self,
        request: vdc_20201214_models.DescribeRtcUserEventListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeRtcUserEventListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeRtcUserEventListResponse(),
            await self.do_roarequest_async('DescribeRtcUserEventList', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/call/describeRtcUserEventList', 'json', req, runtime)
        )

    def delete_app_exp_metric_rule(
        self,
        request: vdc_20201214_models.DeleteAppExpMetricRuleRequest,
    ) -> vdc_20201214_models.DeleteAppExpMetricRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_app_exp_metric_rule_with_options(request, headers, runtime)

    async def delete_app_exp_metric_rule_async(
        self,
        request: vdc_20201214_models.DeleteAppExpMetricRuleRequest,
    ) -> vdc_20201214_models.DeleteAppExpMetricRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_app_exp_metric_rule_with_options_async(request, headers, runtime)

    def delete_app_exp_metric_rule_with_options(
        self,
        request: vdc_20201214_models.DeleteAppExpMetricRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DeleteAppExpMetricRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DeleteAppExpMetricRuleResponse(),
            self.do_roarequest('DeleteAppExpMetricRule', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/config/deleteAppExpMetricRule', 'json', req, runtime)
        )

    async def delete_app_exp_metric_rule_with_options_async(
        self,
        request: vdc_20201214_models.DeleteAppExpMetricRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DeleteAppExpMetricRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DeleteAppExpMetricRuleResponse(),
            await self.do_roarequest_async('DeleteAppExpMetricRule', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/config/deleteAppExpMetricRule', 'json', req, runtime)
        )

    def describe_end_point_event_list(
        self,
        request: vdc_20201214_models.DescribeEndPointEventListRequest,
    ) -> vdc_20201214_models.DescribeEndPointEventListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_end_point_event_list_with_options(request, headers, runtime)

    async def describe_end_point_event_list_async(
        self,
        request: vdc_20201214_models.DescribeEndPointEventListRequest,
    ) -> vdc_20201214_models.DescribeEndPointEventListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_end_point_event_list_with_options_async(request, headers, runtime)

    def describe_end_point_event_list_with_options(
        self,
        request: vdc_20201214_models.DescribeEndPointEventListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeEndPointEventListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeEndPointEventListResponse(),
            self.do_roarequest('DescribeEndPointEventList', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/call/describeEndPointEventList', 'json', req, runtime)
        )

    async def describe_end_point_event_list_with_options_async(
        self,
        request: vdc_20201214_models.DescribeEndPointEventListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeEndPointEventListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeEndPointEventListResponse(),
            await self.do_roarequest_async('DescribeEndPointEventList', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/call/describeEndPointEventList', 'json', req, runtime)
        )

    def describe_quality_distribution_stat_data(
        self,
        request: vdc_20201214_models.DescribeQualityDistributionStatDataRequest,
    ) -> vdc_20201214_models.DescribeQualityDistributionStatDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_quality_distribution_stat_data_with_options(request, headers, runtime)

    async def describe_quality_distribution_stat_data_async(
        self,
        request: vdc_20201214_models.DescribeQualityDistributionStatDataRequest,
    ) -> vdc_20201214_models.DescribeQualityDistributionStatDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_quality_distribution_stat_data_with_options_async(request, headers, runtime)

    def describe_quality_distribution_stat_data_with_options(
        self,
        request: vdc_20201214_models.DescribeQualityDistributionStatDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeQualityDistributionStatDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.stat_dim):
            query['StatDim'] = request.stat_dim
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeQualityDistributionStatDataResponse(),
            self.do_roarequest('DescribeQualityDistributionStatData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/quality/describeQualityDistributionStatData', 'json', req, runtime)
        )

    async def describe_quality_distribution_stat_data_with_options_async(
        self,
        request: vdc_20201214_models.DescribeQualityDistributionStatDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeQualityDistributionStatDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.stat_dim):
            query['StatDim'] = request.stat_dim
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeQualityDistributionStatDataResponse(),
            await self.do_roarequest_async('DescribeQualityDistributionStatData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/quality/describeQualityDistributionStatData', 'json', req, runtime)
        )

    def describe_call_list_test(
        self,
        request: vdc_20201214_models.DescribeCallListTestRequest,
    ) -> vdc_20201214_models.DescribeCallListTestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_call_list_test_with_options(request, headers, runtime)

    async def describe_call_list_test_async(
        self,
        request: vdc_20201214_models.DescribeCallListTestRequest,
    ) -> vdc_20201214_models.DescribeCallListTestResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_call_list_test_with_options_async(request, headers, runtime)

    def describe_call_list_test_with_options(
        self,
        request: vdc_20201214_models.DescribeCallListTestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeCallListTestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeCallListTestResponse(),
            self.do_roarequest('DescribeCallListTest', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/call/describeCallListTest', 'json', req, runtime)
        )

    async def describe_call_list_test_with_options_async(
        self,
        request: vdc_20201214_models.DescribeCallListTestRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeCallListTestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeCallListTestResponse(),
            await self.do_roarequest_async('DescribeCallListTest', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/call/describeCallListTest', 'json', req, runtime)
        )

    def describe_call(
        self,
        request: vdc_20201214_models.DescribeCallRequest,
    ) -> vdc_20201214_models.DescribeCallResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_call_with_options(request, headers, runtime)

    async def describe_call_async(
        self,
        request: vdc_20201214_models.DescribeCallRequest,
    ) -> vdc_20201214_models.DescribeCallResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_call_with_options_async(request, headers, runtime)

    def describe_call_with_options(
        self,
        request: vdc_20201214_models.DescribeCallRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeCallResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.ext_data_type):
            query['ExtDataType'] = request.ext_data_type
        if not UtilClient.is_unset(request.query_exp_info):
            query['QueryExpInfo'] = request.query_exp_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeCallResponse(),
            self.do_roarequest('DescribeCall', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/call/describeCall', 'json', req, runtime)
        )

    async def describe_call_with_options_async(
        self,
        request: vdc_20201214_models.DescribeCallRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeCallResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.ext_data_type):
            query['ExtDataType'] = request.ext_data_type
        if not UtilClient.is_unset(request.query_exp_info):
            query['QueryExpInfo'] = request.query_exp_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeCallResponse(),
            await self.do_roarequest_async('DescribeCall', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/call/describeCall', 'json', req, runtime)
        )

    def describe_app_follow_call_rule_list(self) -> vdc_20201214_models.DescribeAppFollowCallRuleListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_follow_call_rule_list_with_options(headers, runtime)

    async def describe_app_follow_call_rule_list_async(self) -> vdc_20201214_models.DescribeAppFollowCallRuleListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_app_follow_call_rule_list_with_options_async(headers, runtime)

    def describe_app_follow_call_rule_list_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeAppFollowCallRuleListResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeAppFollowCallRuleListResponse(),
            self.do_roarequest('DescribeAppFollowCallRuleList', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/config/describeAppFollowCallRuleList', 'json', req, runtime)
        )

    async def describe_app_follow_call_rule_list_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeAppFollowCallRuleListResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeAppFollowCallRuleListResponse(),
            await self.do_roarequest_async('DescribeAppFollowCallRuleList', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/config/describeAppFollowCallRuleList', 'json', req, runtime)
        )

    def describe_channel_area_distribution_stat_data(
        self,
        request: vdc_20201214_models.DescribeChannelAreaDistributionStatDataRequest,
    ) -> vdc_20201214_models.DescribeChannelAreaDistributionStatDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_channel_area_distribution_stat_data_with_options(request, headers, runtime)

    async def describe_channel_area_distribution_stat_data_async(
        self,
        request: vdc_20201214_models.DescribeChannelAreaDistributionStatDataRequest,
    ) -> vdc_20201214_models.DescribeChannelAreaDistributionStatDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_channel_area_distribution_stat_data_with_options_async(request, headers, runtime)

    def describe_channel_area_distribution_stat_data_with_options(
        self,
        request: vdc_20201214_models.DescribeChannelAreaDistributionStatDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeChannelAreaDistributionStatDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.parent_area):
            query['ParentArea'] = request.parent_area
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeChannelAreaDistributionStatDataResponse(),
            self.do_roarequest('DescribeChannelAreaDistributionStatData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/channel/describeChannelAreaDistributionStatData', 'json', req, runtime)
        )

    async def describe_channel_area_distribution_stat_data_with_options_async(
        self,
        request: vdc_20201214_models.DescribeChannelAreaDistributionStatDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeChannelAreaDistributionStatDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.parent_area):
            query['ParentArea'] = request.parent_area
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeChannelAreaDistributionStatDataResponse(),
            await self.do_roarequest_async('DescribeChannelAreaDistributionStatData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/channel/describeChannelAreaDistributionStatData', 'json', req, runtime)
        )

    def describe_app_exp_metric_rule(
        self,
        request: vdc_20201214_models.DescribeAppExpMetricRuleRequest,
    ) -> vdc_20201214_models.DescribeAppExpMetricRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_exp_metric_rule_with_options(request, headers, runtime)

    async def describe_app_exp_metric_rule_async(
        self,
        request: vdc_20201214_models.DescribeAppExpMetricRuleRequest,
    ) -> vdc_20201214_models.DescribeAppExpMetricRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_app_exp_metric_rule_with_options_async(request, headers, runtime)

    def describe_app_exp_metric_rule_with_options(
        self,
        request: vdc_20201214_models.DescribeAppExpMetricRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeAppExpMetricRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeAppExpMetricRuleResponse(),
            self.do_roarequest('DescribeAppExpMetricRule', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/config/describeAppExpMetricRule', 'json', req, runtime)
        )

    async def describe_app_exp_metric_rule_with_options_async(
        self,
        request: vdc_20201214_models.DescribeAppExpMetricRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeAppExpMetricRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeAppExpMetricRuleResponse(),
            await self.do_roarequest_async('DescribeAppExpMetricRule', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/config/describeAppExpMetricRule', 'json', req, runtime)
        )

    def describe_rtc_channel_details(
        self,
        request: vdc_20201214_models.DescribeRtcChannelDetailsRequest,
    ) -> vdc_20201214_models.DescribeRtcChannelDetailsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_rtc_channel_details_with_options(request, headers, runtime)

    async def describe_rtc_channel_details_async(
        self,
        request: vdc_20201214_models.DescribeRtcChannelDetailsRequest,
    ) -> vdc_20201214_models.DescribeRtcChannelDetailsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_rtc_channel_details_with_options_async(request, headers, runtime)

    def describe_rtc_channel_details_with_options(
        self,
        request: vdc_20201214_models.DescribeRtcChannelDetailsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeRtcChannelDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeRtcChannelDetailsResponse(),
            self.do_roarequest('DescribeRtcChannelDetails', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/channel/describeRtcChannelDetails', 'json', req, runtime)
        )

    async def describe_rtc_channel_details_with_options_async(
        self,
        request: vdc_20201214_models.DescribeRtcChannelDetailsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeRtcChannelDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeRtcChannelDetailsResponse(),
            await self.do_roarequest_async('DescribeRtcChannelDetails', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/channel/describeRtcChannelDetails', 'json', req, runtime)
        )

    def describe_ice_dur_summary_overview(
        self,
        request: vdc_20201214_models.DescribeIceDurSummaryOverviewRequest,
    ) -> vdc_20201214_models.DescribeIceDurSummaryOverviewResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_ice_dur_summary_overview_with_options(request, headers, runtime)

    async def describe_ice_dur_summary_overview_async(
        self,
        request: vdc_20201214_models.DescribeIceDurSummaryOverviewRequest,
    ) -> vdc_20201214_models.DescribeIceDurSummaryOverviewResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_ice_dur_summary_overview_with_options_async(request, headers, runtime)

    def describe_ice_dur_summary_overview_with_options(
        self,
        request: vdc_20201214_models.DescribeIceDurSummaryOverviewRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeIceDurSummaryOverviewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cur_ts):
            query['CurTs'] = request.cur_ts
        if not UtilClient.is_unset(request.time_zone):
            query['TimeZone'] = request.time_zone
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeIceDurSummaryOverviewResponse(),
            self.do_roarequest('DescribeIceDurSummaryOverview', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/ice/describeIceDurSummaryOverview', 'json', req, runtime)
        )

    async def describe_ice_dur_summary_overview_with_options_async(
        self,
        request: vdc_20201214_models.DescribeIceDurSummaryOverviewRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeIceDurSummaryOverviewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cur_ts):
            query['CurTs'] = request.cur_ts
        if not UtilClient.is_unset(request.time_zone):
            query['TimeZone'] = request.time_zone
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeIceDurSummaryOverviewResponse(),
            await self.do_roarequest_async('DescribeIceDurSummaryOverview', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/ice/describeIceDurSummaryOverview', 'json', req, runtime)
        )

    def describe_call_user_exp(
        self,
        request: vdc_20201214_models.DescribeCallUserExpRequest,
    ) -> vdc_20201214_models.DescribeCallUserExpResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_call_user_exp_with_options(request, headers, runtime)

    async def describe_call_user_exp_async(
        self,
        request: vdc_20201214_models.DescribeCallUserExpRequest,
    ) -> vdc_20201214_models.DescribeCallUserExpResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_call_user_exp_with_options_async(request, headers, runtime)

    def describe_call_user_exp_with_options(
        self,
        request: vdc_20201214_models.DescribeCallUserExpRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeCallUserExpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeCallUserExpResponse(),
            self.do_roarequest('DescribeCallUserExp', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/call/describeCallUserExp', 'json', req, runtime)
        )

    async def describe_call_user_exp_with_options_async(
        self,
        request: vdc_20201214_models.DescribeCallUserExpRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeCallUserExpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeCallUserExpResponse(),
            await self.do_roarequest_async('DescribeCallUserExp', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/call/describeCallUserExp', 'json', req, runtime)
        )

    def describe_channel_join_info(
        self,
        request: vdc_20201214_models.DescribeChannelJoinInfoRequest,
    ) -> vdc_20201214_models.DescribeChannelJoinInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_channel_join_info_with_options(request, headers, runtime)

    async def describe_channel_join_info_async(
        self,
        request: vdc_20201214_models.DescribeChannelJoinInfoRequest,
    ) -> vdc_20201214_models.DescribeChannelJoinInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_channel_join_info_with_options_async(request, headers, runtime)

    def describe_channel_join_info_with_options(
        self,
        request: vdc_20201214_models.DescribeChannelJoinInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeChannelJoinInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeChannelJoinInfoResponse(),
            self.do_roarequest('DescribeChannelJoinInfo', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/channel/describeChannelJoinInfo', 'json', req, runtime)
        )

    async def describe_channel_join_info_with_options_async(
        self,
        request: vdc_20201214_models.DescribeChannelJoinInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeChannelJoinInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeChannelJoinInfoResponse(),
            await self.do_roarequest_async('DescribeChannelJoinInfo', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/channel/describeChannelJoinInfo', 'json', req, runtime)
        )

    def delete_app_follow_call_rule(
        self,
        request: vdc_20201214_models.DeleteAppFollowCallRuleRequest,
    ) -> vdc_20201214_models.DeleteAppFollowCallRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_app_follow_call_rule_with_options(request, headers, runtime)

    async def delete_app_follow_call_rule_async(
        self,
        request: vdc_20201214_models.DeleteAppFollowCallRuleRequest,
    ) -> vdc_20201214_models.DeleteAppFollowCallRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_app_follow_call_rule_with_options_async(request, headers, runtime)

    def delete_app_follow_call_rule_with_options(
        self,
        request: vdc_20201214_models.DeleteAppFollowCallRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DeleteAppFollowCallRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DeleteAppFollowCallRuleResponse(),
            self.do_roarequest('DeleteAppFollowCallRule', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/config/deleteAppFollowCallRule', 'json', req, runtime)
        )

    async def delete_app_follow_call_rule_with_options_async(
        self,
        request: vdc_20201214_models.DeleteAppFollowCallRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DeleteAppFollowCallRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DeleteAppFollowCallRuleResponse(),
            await self.do_roarequest_async('DeleteAppFollowCallRule', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/config/deleteAppFollowCallRule', 'json', req, runtime)
        )

    def describe_app_exp_metric_rule_list(self) -> vdc_20201214_models.DescribeAppExpMetricRuleListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_exp_metric_rule_list_with_options(headers, runtime)

    async def describe_app_exp_metric_rule_list_async(self) -> vdc_20201214_models.DescribeAppExpMetricRuleListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_app_exp_metric_rule_list_with_options_async(headers, runtime)

    def describe_app_exp_metric_rule_list_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeAppExpMetricRuleListResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeAppExpMetricRuleListResponse(),
            self.do_roarequest('DescribeAppExpMetricRuleList', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/config/describeAppExpMetricRuleList', 'json', req, runtime)
        )

    async def describe_app_exp_metric_rule_list_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeAppExpMetricRuleListResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeAppExpMetricRuleListResponse(),
            await self.do_roarequest_async('DescribeAppExpMetricRuleList', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/config/describeAppExpMetricRuleList', 'json', req, runtime)
        )

    def describe_channel_top_pub_user_list(
        self,
        request: vdc_20201214_models.DescribeChannelTopPubUserListRequest,
    ) -> vdc_20201214_models.DescribeChannelTopPubUserListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_channel_top_pub_user_list_with_options(request, headers, runtime)

    async def describe_channel_top_pub_user_list_async(
        self,
        request: vdc_20201214_models.DescribeChannelTopPubUserListRequest,
    ) -> vdc_20201214_models.DescribeChannelTopPubUserListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_channel_top_pub_user_list_with_options_async(request, headers, runtime)

    def describe_channel_top_pub_user_list_with_options(
        self,
        request: vdc_20201214_models.DescribeChannelTopPubUserListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeChannelTopPubUserListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeChannelTopPubUserListResponse(),
            self.do_roarequest('DescribeChannelTopPubUserList', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/channel/describeChannelTopPubUserList', 'json', req, runtime)
        )

    async def describe_channel_top_pub_user_list_with_options_async(
        self,
        request: vdc_20201214_models.DescribeChannelTopPubUserListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeChannelTopPubUserListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeChannelTopPubUserListResponse(),
            await self.do_roarequest_async('DescribeChannelTopPubUserList', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/channel/describeChannelTopPubUserList', 'json', req, runtime)
        )

    def describe_app_follow_call_rule(
        self,
        request: vdc_20201214_models.DescribeAppFollowCallRuleRequest,
    ) -> vdc_20201214_models.DescribeAppFollowCallRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_follow_call_rule_with_options(request, headers, runtime)

    async def describe_app_follow_call_rule_async(
        self,
        request: vdc_20201214_models.DescribeAppFollowCallRuleRequest,
    ) -> vdc_20201214_models.DescribeAppFollowCallRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_app_follow_call_rule_with_options_async(request, headers, runtime)

    def describe_app_follow_call_rule_with_options(
        self,
        request: vdc_20201214_models.DescribeAppFollowCallRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeAppFollowCallRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeAppFollowCallRuleResponse(),
            self.do_roarequest('DescribeAppFollowCallRule', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/config/describeAppFollowCallRule', 'json', req, runtime)
        )

    async def describe_app_follow_call_rule_with_options_async(
        self,
        request: vdc_20201214_models.DescribeAppFollowCallRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeAppFollowCallRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeAppFollowCallRuleResponse(),
            await self.do_roarequest_async('DescribeAppFollowCallRule', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/config/describeAppFollowCallRule', 'json', req, runtime)
        )

    def describe_usage_distribution_stat_data(
        self,
        request: vdc_20201214_models.DescribeUsageDistributionStatDataRequest,
    ) -> vdc_20201214_models.DescribeUsageDistributionStatDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_usage_distribution_stat_data_with_options(request, headers, runtime)

    async def describe_usage_distribution_stat_data_async(
        self,
        request: vdc_20201214_models.DescribeUsageDistributionStatDataRequest,
    ) -> vdc_20201214_models.DescribeUsageDistributionStatDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_usage_distribution_stat_data_with_options_async(request, headers, runtime)

    def describe_usage_distribution_stat_data_with_options(
        self,
        request: vdc_20201214_models.DescribeUsageDistributionStatDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeUsageDistributionStatDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.stat_dim):
            query['StatDim'] = request.stat_dim
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeUsageDistributionStatDataResponse(),
            self.do_roarequest('DescribeUsageDistributionStatData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/usage/describeUsageDistributionStatData', 'json', req, runtime)
        )

    async def describe_usage_distribution_stat_data_with_options_async(
        self,
        request: vdc_20201214_models.DescribeUsageDistributionStatDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeUsageDistributionStatDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.stat_dim):
            query['StatDim'] = request.stat_dim
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeUsageDistributionStatDataResponse(),
            await self.do_roarequest_async('DescribeUsageDistributionStatData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/usage/describeUsageDistributionStatData', 'json', req, runtime)
        )

    def describe_usage_area_distribution_stat_data(
        self,
        request: vdc_20201214_models.DescribeUsageAreaDistributionStatDataRequest,
    ) -> vdc_20201214_models.DescribeUsageAreaDistributionStatDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_usage_area_distribution_stat_data_with_options(request, headers, runtime)

    async def describe_usage_area_distribution_stat_data_async(
        self,
        request: vdc_20201214_models.DescribeUsageAreaDistributionStatDataRequest,
    ) -> vdc_20201214_models.DescribeUsageAreaDistributionStatDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_usage_area_distribution_stat_data_with_options_async(request, headers, runtime)

    def describe_usage_area_distribution_stat_data_with_options(
        self,
        request: vdc_20201214_models.DescribeUsageAreaDistributionStatDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeUsageAreaDistributionStatDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.parent_area):
            query['ParentArea'] = request.parent_area
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeUsageAreaDistributionStatDataResponse(),
            self.do_roarequest('DescribeUsageAreaDistributionStatData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/usage/describeUsageAreaDistributionStatData', 'json', req, runtime)
        )

    async def describe_usage_area_distribution_stat_data_with_options_async(
        self,
        request: vdc_20201214_models.DescribeUsageAreaDistributionStatDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeUsageAreaDistributionStatDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.parent_area):
            query['ParentArea'] = request.parent_area
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeUsageAreaDistributionStatDataResponse(),
            await self.do_roarequest_async('DescribeUsageAreaDistributionStatData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/usage/describeUsageAreaDistributionStatData', 'json', req, runtime)
        )

    def describe_end_point_metric_data(
        self,
        request: vdc_20201214_models.DescribeEndPointMetricDataRequest,
    ) -> vdc_20201214_models.DescribeEndPointMetricDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_end_point_metric_data_with_options(request, headers, runtime)

    async def describe_end_point_metric_data_async(
        self,
        request: vdc_20201214_models.DescribeEndPointMetricDataRequest,
    ) -> vdc_20201214_models.DescribeEndPointMetricDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_end_point_metric_data_with_options_async(request, headers, runtime)

    def describe_end_point_metric_data_with_options(
        self,
        request: vdc_20201214_models.DescribeEndPointMetricDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeEndPointMetricDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not UtilClient.is_unset(request.pub_user_id):
            query['PubUserId'] = request.pub_user_id
        if not UtilClient.is_unset(request.pub_call_id_list):
            query['PubCallIdList'] = request.pub_call_id_list
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeEndPointMetricDataResponse(),
            self.do_roarequest('DescribeEndPointMetricData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/call/describeEndPointMetricData', 'json', req, runtime)
        )

    async def describe_end_point_metric_data_with_options_async(
        self,
        request: vdc_20201214_models.DescribeEndPointMetricDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeEndPointMetricDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        if not UtilClient.is_unset(request.pub_user_id):
            query['PubUserId'] = request.pub_user_id
        if not UtilClient.is_unset(request.pub_call_id_list):
            query['PubCallIdList'] = request.pub_call_id_list
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeEndPointMetricDataResponse(),
            await self.do_roarequest_async('DescribeEndPointMetricData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/call/describeEndPointMetricData', 'json', req, runtime)
        )

    def describe_app_config(
        self,
        request: vdc_20201214_models.DescribeAppConfigRequest,
    ) -> vdc_20201214_models.DescribeAppConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_config_with_options(request, headers, runtime)

    async def describe_app_config_async(
        self,
        request: vdc_20201214_models.DescribeAppConfigRequest,
    ) -> vdc_20201214_models.DescribeAppConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_app_config_with_options_async(request, headers, runtime)

    def describe_app_config_with_options(
        self,
        request: vdc_20201214_models.DescribeAppConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeAppConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeAppConfigResponse(),
            self.do_roarequest('DescribeAppConfig', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/config/describeAppConfig', 'json', req, runtime)
        )

    async def describe_app_config_with_options_async(
        self,
        request: vdc_20201214_models.DescribeAppConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeAppConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeAppConfigResponse(),
            await self.do_roarequest_async('DescribeAppConfig', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/config/describeAppConfig', 'json', req, runtime)
        )

    def describe_usage_overall_data(
        self,
        request: vdc_20201214_models.DescribeUsageOverallDataRequest,
    ) -> vdc_20201214_models.DescribeUsageOverallDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_usage_overall_data_with_options(request, headers, runtime)

    async def describe_usage_overall_data_async(
        self,
        request: vdc_20201214_models.DescribeUsageOverallDataRequest,
    ) -> vdc_20201214_models.DescribeUsageOverallDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_usage_overall_data_with_options_async(request, headers, runtime)

    def describe_usage_overall_data_with_options(
        self,
        request: vdc_20201214_models.DescribeUsageOverallDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeUsageOverallDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeUsageOverallDataResponse(),
            self.do_roarequest('DescribeUsageOverallData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/usage/describeUsageOverallData', 'json', req, runtime)
        )

    async def describe_usage_overall_data_with_options_async(
        self,
        request: vdc_20201214_models.DescribeUsageOverallDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeUsageOverallDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeUsageOverallDataResponse(),
            await self.do_roarequest_async('DescribeUsageOverallData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/usage/describeUsageOverallData', 'json', req, runtime)
        )

    def update_app_exp_metric_rule(
        self,
        request: vdc_20201214_models.UpdateAppExpMetricRuleRequest,
    ) -> vdc_20201214_models.UpdateAppExpMetricRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_app_exp_metric_rule_with_options(request, headers, runtime)

    async def update_app_exp_metric_rule_async(
        self,
        request: vdc_20201214_models.UpdateAppExpMetricRuleRequest,
    ) -> vdc_20201214_models.UpdateAppExpMetricRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_app_exp_metric_rule_with_options_async(request, headers, runtime)

    def update_app_exp_metric_rule_with_options(
        self,
        request: vdc_20201214_models.UpdateAppExpMetricRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.UpdateAppExpMetricRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule):
            query['Rule'] = request.rule
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.UpdateAppExpMetricRuleResponse(),
            self.do_roarequest('UpdateAppExpMetricRule', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/config/updateAppExpMetricRule', 'json', req, runtime)
        )

    async def update_app_exp_metric_rule_with_options_async(
        self,
        request: vdc_20201214_models.UpdateAppExpMetricRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.UpdateAppExpMetricRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule):
            query['Rule'] = request.rule
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.UpdateAppExpMetricRuleResponse(),
            await self.do_roarequest_async('UpdateAppExpMetricRule', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/config/updateAppExpMetricRule', 'json', req, runtime)
        )

    def describe_fault_diagnosis_user_detail(
        self,
        request: vdc_20201214_models.DescribeFaultDiagnosisUserDetailRequest,
    ) -> vdc_20201214_models.DescribeFaultDiagnosisUserDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_fault_diagnosis_user_detail_with_options(request, headers, runtime)

    async def describe_fault_diagnosis_user_detail_async(
        self,
        request: vdc_20201214_models.DescribeFaultDiagnosisUserDetailRequest,
    ) -> vdc_20201214_models.DescribeFaultDiagnosisUserDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_fault_diagnosis_user_detail_with_options_async(request, headers, runtime)

    def describe_fault_diagnosis_user_detail_with_options(
        self,
        request: vdc_20201214_models.DescribeFaultDiagnosisUserDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeFaultDiagnosisUserDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.fault_type):
            query['FaultType'] = request.fault_type
        if not UtilClient.is_unset(request.query_call_user_info):
            query['QueryCallUserInfo'] = request.query_call_user_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeFaultDiagnosisUserDetailResponse(),
            self.do_roarequest('DescribeFaultDiagnosisUserDetail', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/diagnosis/describeFaultDiagnosisUserDetail', 'json', req, runtime)
        )

    async def describe_fault_diagnosis_user_detail_with_options_async(
        self,
        request: vdc_20201214_models.DescribeFaultDiagnosisUserDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeFaultDiagnosisUserDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.fault_type):
            query['FaultType'] = request.fault_type
        if not UtilClient.is_unset(request.query_call_user_info):
            query['QueryCallUserInfo'] = request.query_call_user_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeFaultDiagnosisUserDetailResponse(),
            await self.do_roarequest_async('DescribeFaultDiagnosisUserDetail', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/diagnosis/describeFaultDiagnosisUserDetail', 'json', req, runtime)
        )

    def describe_channel_distribution_stat_data(
        self,
        request: vdc_20201214_models.DescribeChannelDistributionStatDataRequest,
    ) -> vdc_20201214_models.DescribeChannelDistributionStatDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_channel_distribution_stat_data_with_options(request, headers, runtime)

    async def describe_channel_distribution_stat_data_async(
        self,
        request: vdc_20201214_models.DescribeChannelDistributionStatDataRequest,
    ) -> vdc_20201214_models.DescribeChannelDistributionStatDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_channel_distribution_stat_data_with_options_async(request, headers, runtime)

    def describe_channel_distribution_stat_data_with_options(
        self,
        request: vdc_20201214_models.DescribeChannelDistributionStatDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeChannelDistributionStatDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeChannelDistributionStatDataResponse(),
            self.do_roarequest('DescribeChannelDistributionStatData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/channel/describeChannelDistributionStatData', 'json', req, runtime)
        )

    async def describe_channel_distribution_stat_data_with_options_async(
        self,
        request: vdc_20201214_models.DescribeChannelDistributionStatDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeChannelDistributionStatDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeChannelDistributionStatDataResponse(),
            await self.do_roarequest_async('DescribeChannelDistributionStatData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/channel/describeChannelDistributionStatData', 'json', req, runtime)
        )

    def describe_channel_user_metrics(
        self,
        request: vdc_20201214_models.DescribeChannelUserMetricsRequest,
    ) -> vdc_20201214_models.DescribeChannelUserMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_channel_user_metrics_with_options(request, headers, runtime)

    async def describe_channel_user_metrics_async(
        self,
        request: vdc_20201214_models.DescribeChannelUserMetricsRequest,
    ) -> vdc_20201214_models.DescribeChannelUserMetricsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_channel_user_metrics_with_options_async(request, headers, runtime)

    def describe_channel_user_metrics_with_options(
        self,
        request: vdc_20201214_models.DescribeChannelUserMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeChannelUserMetricsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeChannelUserMetricsResponse(),
            self.do_roarequest('DescribeChannelUserMetrics', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/channel/describeChannelUserMetrics', 'json', req, runtime)
        )

    async def describe_channel_user_metrics_with_options_async(
        self,
        request: vdc_20201214_models.DescribeChannelUserMetricsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeChannelUserMetricsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeChannelUserMetricsResponse(),
            await self.do_roarequest_async('DescribeChannelUserMetrics', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/channel/describeChannelUserMetrics', 'json', req, runtime)
        )

    def describe_fault_diagnosis_factor_distribution_stat(
        self,
        request: vdc_20201214_models.DescribeFaultDiagnosisFactorDistributionStatRequest,
    ) -> vdc_20201214_models.DescribeFaultDiagnosisFactorDistributionStatResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_fault_diagnosis_factor_distribution_stat_with_options(request, headers, runtime)

    async def describe_fault_diagnosis_factor_distribution_stat_async(
        self,
        request: vdc_20201214_models.DescribeFaultDiagnosisFactorDistributionStatRequest,
    ) -> vdc_20201214_models.DescribeFaultDiagnosisFactorDistributionStatResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_fault_diagnosis_factor_distribution_stat_with_options_async(request, headers, runtime)

    def describe_fault_diagnosis_factor_distribution_stat_with_options(
        self,
        request: vdc_20201214_models.DescribeFaultDiagnosisFactorDistributionStatRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeFaultDiagnosisFactorDistributionStatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeFaultDiagnosisFactorDistributionStatResponse(),
            self.do_roarequest('DescribeFaultDiagnosisFactorDistributionStat', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/diagnosis/describeFaultDiagnosisFactorDistributionStat', 'json', req, runtime)
        )

    async def describe_fault_diagnosis_factor_distribution_stat_with_options_async(
        self,
        request: vdc_20201214_models.DescribeFaultDiagnosisFactorDistributionStatRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeFaultDiagnosisFactorDistributionStatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeFaultDiagnosisFactorDistributionStatResponse(),
            await self.do_roarequest_async('DescribeFaultDiagnosisFactorDistributionStat', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/diagnosis/describeFaultDiagnosisFactorDistributionStat', 'json', req, runtime)
        )

    def describe_rtc_channel_list(
        self,
        request: vdc_20201214_models.DescribeRtcChannelListRequest,
    ) -> vdc_20201214_models.DescribeRtcChannelListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_rtc_channel_list_with_options(request, headers, runtime)

    async def describe_rtc_channel_list_async(
        self,
        request: vdc_20201214_models.DescribeRtcChannelListRequest,
    ) -> vdc_20201214_models.DescribeRtcChannelListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_rtc_channel_list_with_options_async(request, headers, runtime)

    def describe_rtc_channel_list_with_options(
        self,
        request: vdc_20201214_models.DescribeRtcChannelListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeRtcChannelListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeRtcChannelListResponse(),
            self.do_roarequest('DescribeRtcChannelList', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/channel/describeRtcChannelList', 'json', req, runtime)
        )

    async def describe_rtc_channel_list_with_options_async(
        self,
        request: vdc_20201214_models.DescribeRtcChannelListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeRtcChannelListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeRtcChannelListResponse(),
            await self.do_roarequest_async('DescribeRtcChannelList', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/channel/describeRtcChannelList', 'json', req, runtime)
        )

    def describe_fault_diagnosis_user_list(
        self,
        request: vdc_20201214_models.DescribeFaultDiagnosisUserListRequest,
    ) -> vdc_20201214_models.DescribeFaultDiagnosisUserListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_fault_diagnosis_user_list_with_options(request, headers, runtime)

    async def describe_fault_diagnosis_user_list_async(
        self,
        request: vdc_20201214_models.DescribeFaultDiagnosisUserListRequest,
    ) -> vdc_20201214_models.DescribeFaultDiagnosisUserListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_fault_diagnosis_user_list_with_options_async(request, headers, runtime)

    def describe_fault_diagnosis_user_list_with_options(
        self,
        request: vdc_20201214_models.DescribeFaultDiagnosisUserListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeFaultDiagnosisUserListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.fault_types):
            query['FaultTypes'] = request.fault_types
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeFaultDiagnosisUserListResponse(),
            self.do_roarequest('DescribeFaultDiagnosisUserList', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/diagnosis/describeFaultDiagnosisUserList', 'json', req, runtime)
        )

    async def describe_fault_diagnosis_user_list_with_options_async(
        self,
        request: vdc_20201214_models.DescribeFaultDiagnosisUserListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeFaultDiagnosisUserListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.fault_types):
            query['FaultTypes'] = request.fault_types
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeFaultDiagnosisUserListResponse(),
            await self.do_roarequest_async('DescribeFaultDiagnosisUserList', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/diagnosis/describeFaultDiagnosisUserList', 'json', req, runtime)
        )

    def describe_rtc_channel_metric_list(
        self,
        request: vdc_20201214_models.DescribeRtcChannelMetricListRequest,
    ) -> vdc_20201214_models.DescribeRtcChannelMetricListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_rtc_channel_metric_list_with_options(request, headers, runtime)

    async def describe_rtc_channel_metric_list_async(
        self,
        request: vdc_20201214_models.DescribeRtcChannelMetricListRequest,
    ) -> vdc_20201214_models.DescribeRtcChannelMetricListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_rtc_channel_metric_list_with_options_async(request, headers, runtime)

    def describe_rtc_channel_metric_list_with_options(
        self,
        request: vdc_20201214_models.DescribeRtcChannelMetricListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeRtcChannelMetricListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.pub_uid):
            query['PubUid'] = request.pub_uid
        if not UtilClient.is_unset(request.sub_uid):
            query['SubUid'] = request.sub_uid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeRtcChannelMetricListResponse(),
            self.do_roarequest('DescribeRtcChannelMetricList', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/call/describeRtcChannelMetricList', 'json', req, runtime)
        )

    async def describe_rtc_channel_metric_list_with_options_async(
        self,
        request: vdc_20201214_models.DescribeRtcChannelMetricListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeRtcChannelMetricListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.pub_uid):
            query['PubUid'] = request.pub_uid
        if not UtilClient.is_unset(request.sub_uid):
            query['SubUid'] = request.sub_uid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeRtcChannelMetricListResponse(),
            await self.do_roarequest_async('DescribeRtcChannelMetricList', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/call/describeRtcChannelMetricList', 'json', req, runtime)
        )

    def describe_qoe_metric_data(
        self,
        request: vdc_20201214_models.DescribeQoeMetricDataRequest,
    ) -> vdc_20201214_models.DescribeQoeMetricDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_qoe_metric_data_with_options(request, headers, runtime)

    async def describe_qoe_metric_data_async(
        self,
        request: vdc_20201214_models.DescribeQoeMetricDataRequest,
    ) -> vdc_20201214_models.DescribeQoeMetricDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_qoe_metric_data_with_options_async(request, headers, runtime)

    def describe_qoe_metric_data_with_options(
        self,
        request: vdc_20201214_models.DescribeQoeMetricDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeQoeMetricDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeQoeMetricDataResponse(),
            self.do_roarequest('DescribeQoeMetricData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/call/describeQoeMetricData', 'json', req, runtime)
        )

    async def describe_qoe_metric_data_with_options_async(
        self,
        request: vdc_20201214_models.DescribeQoeMetricDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeQoeMetricDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeQoeMetricDataResponse(),
            await self.do_roarequest_async('DescribeQoeMetricData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/call/describeQoeMetricData', 'json', req, runtime)
        )

    def describe_pub_user_list_by_sub_user(
        self,
        request: vdc_20201214_models.DescribePubUserListBySubUserRequest,
    ) -> vdc_20201214_models.DescribePubUserListBySubUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_pub_user_list_by_sub_user_with_options(request, headers, runtime)

    async def describe_pub_user_list_by_sub_user_async(
        self,
        request: vdc_20201214_models.DescribePubUserListBySubUserRequest,
    ) -> vdc_20201214_models.DescribePubUserListBySubUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_pub_user_list_by_sub_user_with_options_async(request, headers, runtime)

    def describe_pub_user_list_by_sub_user_with_options(
        self,
        request: vdc_20201214_models.DescribePubUserListBySubUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribePubUserListBySubUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribePubUserListBySubUserResponse(),
            self.do_roarequest('DescribePubUserListBySubUser', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/call/describePubUserListBySubUser', 'json', req, runtime)
        )

    async def describe_pub_user_list_by_sub_user_with_options_async(
        self,
        request: vdc_20201214_models.DescribePubUserListBySubUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribePubUserListBySubUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribePubUserListBySubUserResponse(),
            await self.do_roarequest_async('DescribePubUserListBySubUser', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/call/describePubUserListBySubUser', 'json', req, runtime)
        )

    def update_app_follow_call_rule(
        self,
        request: vdc_20201214_models.UpdateAppFollowCallRuleRequest,
    ) -> vdc_20201214_models.UpdateAppFollowCallRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_app_follow_call_rule_with_options(request, headers, runtime)

    async def update_app_follow_call_rule_async(
        self,
        request: vdc_20201214_models.UpdateAppFollowCallRuleRequest,
    ) -> vdc_20201214_models.UpdateAppFollowCallRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_app_follow_call_rule_with_options_async(request, headers, runtime)

    def update_app_follow_call_rule_with_options(
        self,
        request: vdc_20201214_models.UpdateAppFollowCallRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.UpdateAppFollowCallRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule):
            query['Rule'] = request.rule
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.UpdateAppFollowCallRuleResponse(),
            self.do_roarequest('UpdateAppFollowCallRule', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/config/updateAppFollowCallRule', 'json', req, runtime)
        )

    async def update_app_follow_call_rule_with_options_async(
        self,
        request: vdc_20201214_models.UpdateAppFollowCallRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.UpdateAppFollowCallRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule):
            query['Rule'] = request.rule
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.UpdateAppFollowCallRuleResponse(),
            await self.do_roarequest_async('UpdateAppFollowCallRule', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/config/updateAppFollowCallRule', 'json', req, runtime)
        )

    def describe_quality_os_sdk_version_distribution_stat_data(
        self,
        request: vdc_20201214_models.DescribeQualityOsSdkVersionDistributionStatDataRequest,
    ) -> vdc_20201214_models.DescribeQualityOsSdkVersionDistributionStatDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_quality_os_sdk_version_distribution_stat_data_with_options(request, headers, runtime)

    async def describe_quality_os_sdk_version_distribution_stat_data_async(
        self,
        request: vdc_20201214_models.DescribeQualityOsSdkVersionDistributionStatDataRequest,
    ) -> vdc_20201214_models.DescribeQualityOsSdkVersionDistributionStatDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_quality_os_sdk_version_distribution_stat_data_with_options_async(request, headers, runtime)

    def describe_quality_os_sdk_version_distribution_stat_data_with_options(
        self,
        request: vdc_20201214_models.DescribeQualityOsSdkVersionDistributionStatDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeQualityOsSdkVersionDistributionStatDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeQualityOsSdkVersionDistributionStatDataResponse(),
            self.do_roarequest('DescribeQualityOsSdkVersionDistributionStatData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/quality/describeQualityOsSdkVersionDistributionStatData', 'json', req, runtime)
        )

    async def describe_quality_os_sdk_version_distribution_stat_data_with_options_async(
        self,
        request: vdc_20201214_models.DescribeQualityOsSdkVersionDistributionStatDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeQualityOsSdkVersionDistributionStatDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeQualityOsSdkVersionDistributionStatDataResponse(),
            await self.do_roarequest_async('DescribeQualityOsSdkVersionDistributionStatData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/quality/describeQualityOsSdkVersionDistributionStatData', 'json', req, runtime)
        )

    def describe_rtc_record_metric_data(
        self,
        request: vdc_20201214_models.DescribeRtcRecordMetricDataRequest,
    ) -> vdc_20201214_models.DescribeRtcRecordMetricDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_rtc_record_metric_data_with_options(request, headers, runtime)

    async def describe_rtc_record_metric_data_async(
        self,
        request: vdc_20201214_models.DescribeRtcRecordMetricDataRequest,
    ) -> vdc_20201214_models.DescribeRtcRecordMetricDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_rtc_record_metric_data_with_options_async(request, headers, runtime)

    def describe_rtc_record_metric_data_with_options(
        self,
        request: vdc_20201214_models.DescribeRtcRecordMetricDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeRtcRecordMetricDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeRtcRecordMetricDataResponse(),
            self.do_roarequest('DescribeRtcRecordMetricData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/record/describeRtcRecordMetricData', 'json', req, runtime)
        )

    async def describe_rtc_record_metric_data_with_options_async(
        self,
        request: vdc_20201214_models.DescribeRtcRecordMetricDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeRtcRecordMetricDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeRtcRecordMetricDataResponse(),
            await self.do_roarequest_async('DescribeRtcRecordMetricData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/record/describeRtcRecordMetricData', 'json', req, runtime)
        )

    def describe_quality_overall_data(
        self,
        request: vdc_20201214_models.DescribeQualityOverallDataRequest,
    ) -> vdc_20201214_models.DescribeQualityOverallDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_quality_overall_data_with_options(request, headers, runtime)

    async def describe_quality_overall_data_async(
        self,
        request: vdc_20201214_models.DescribeQualityOverallDataRequest,
    ) -> vdc_20201214_models.DescribeQualityOverallDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_quality_overall_data_with_options_async(request, headers, runtime)

    def describe_quality_overall_data_with_options(
        self,
        request: vdc_20201214_models.DescribeQualityOverallDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeQualityOverallDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeQualityOverallDataResponse(),
            self.do_roarequest('DescribeQualityOverallData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/quality/describeQualityOverallData', 'json', req, runtime)
        )

    async def describe_quality_overall_data_with_options_async(
        self,
        request: vdc_20201214_models.DescribeQualityOverallDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> vdc_20201214_models.DescribeQualityOverallDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeQualityOverallDataResponse(),
            await self.do_roarequest_async('DescribeQualityOverallData', '2020-12-14', 'HTTPS', 'POST', 'AK', f'/api/quality/describeQualityOverallData', 'json', req, runtime)
        )
