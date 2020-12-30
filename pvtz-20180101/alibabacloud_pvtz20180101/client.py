# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_pvtz20180101 import models as pvtz_20180101_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('pvtz', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_zone_with_options(
        self,
        request: pvtz_20180101_models.AddZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.AddZoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.AddZoneResponse().from_map(
            self.do_rpcrequest('AddZone', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_zone_with_options_async(
        self,
        request: pvtz_20180101_models.AddZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.AddZoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.AddZoneResponse().from_map(
            await self.do_rpcrequest_async('AddZone', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_zone(
        self,
        request: pvtz_20180101_models.AddZoneRequest,
    ) -> pvtz_20180101_models.AddZoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_zone_with_options(request, runtime)

    async def add_zone_async(
        self,
        request: pvtz_20180101_models.AddZoneRequest,
    ) -> pvtz_20180101_models.AddZoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_zone_with_options_async(request, runtime)

    def add_zone_record_with_options(
        self,
        request: pvtz_20180101_models.AddZoneRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.AddZoneRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.AddZoneRecordResponse().from_map(
            self.do_rpcrequest('AddZoneRecord', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_zone_record_with_options_async(
        self,
        request: pvtz_20180101_models.AddZoneRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.AddZoneRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.AddZoneRecordResponse().from_map(
            await self.do_rpcrequest_async('AddZoneRecord', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_zone_record(
        self,
        request: pvtz_20180101_models.AddZoneRecordRequest,
    ) -> pvtz_20180101_models.AddZoneRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_zone_record_with_options(request, runtime)

    async def add_zone_record_async(
        self,
        request: pvtz_20180101_models.AddZoneRecordRequest,
    ) -> pvtz_20180101_models.AddZoneRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_zone_record_with_options_async(request, runtime)

    def bind_zone_vpc_with_options(
        self,
        request: pvtz_20180101_models.BindZoneVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.BindZoneVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.BindZoneVpcResponse().from_map(
            self.do_rpcrequest('BindZoneVpc', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_zone_vpc_with_options_async(
        self,
        request: pvtz_20180101_models.BindZoneVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.BindZoneVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.BindZoneVpcResponse().from_map(
            await self.do_rpcrequest_async('BindZoneVpc', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_zone_vpc(
        self,
        request: pvtz_20180101_models.BindZoneVpcRequest,
    ) -> pvtz_20180101_models.BindZoneVpcResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_zone_vpc_with_options(request, runtime)

    async def bind_zone_vpc_async(
        self,
        request: pvtz_20180101_models.BindZoneVpcRequest,
    ) -> pvtz_20180101_models.BindZoneVpcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_zone_vpc_with_options_async(request, runtime)

    def check_zone_name_with_options(
        self,
        request: pvtz_20180101_models.CheckZoneNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.CheckZoneNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.CheckZoneNameResponse().from_map(
            self.do_rpcrequest('CheckZoneName', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_zone_name_with_options_async(
        self,
        request: pvtz_20180101_models.CheckZoneNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.CheckZoneNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.CheckZoneNameResponse().from_map(
            await self.do_rpcrequest_async('CheckZoneName', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_zone_name(
        self,
        request: pvtz_20180101_models.CheckZoneNameRequest,
    ) -> pvtz_20180101_models.CheckZoneNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_zone_name_with_options(request, runtime)

    async def check_zone_name_async(
        self,
        request: pvtz_20180101_models.CheckZoneNameRequest,
    ) -> pvtz_20180101_models.CheckZoneNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_zone_name_with_options_async(request, runtime)

    def delete_zone_with_options(
        self,
        request: pvtz_20180101_models.DeleteZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DeleteZoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.DeleteZoneResponse().from_map(
            self.do_rpcrequest('DeleteZone', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_zone_with_options_async(
        self,
        request: pvtz_20180101_models.DeleteZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DeleteZoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.DeleteZoneResponse().from_map(
            await self.do_rpcrequest_async('DeleteZone', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_zone(
        self,
        request: pvtz_20180101_models.DeleteZoneRequest,
    ) -> pvtz_20180101_models.DeleteZoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_zone_with_options(request, runtime)

    async def delete_zone_async(
        self,
        request: pvtz_20180101_models.DeleteZoneRequest,
    ) -> pvtz_20180101_models.DeleteZoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_zone_with_options_async(request, runtime)

    def delete_zone_record_with_options(
        self,
        request: pvtz_20180101_models.DeleteZoneRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DeleteZoneRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.DeleteZoneRecordResponse().from_map(
            self.do_rpcrequest('DeleteZoneRecord', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_zone_record_with_options_async(
        self,
        request: pvtz_20180101_models.DeleteZoneRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DeleteZoneRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.DeleteZoneRecordResponse().from_map(
            await self.do_rpcrequest_async('DeleteZoneRecord', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_zone_record(
        self,
        request: pvtz_20180101_models.DeleteZoneRecordRequest,
    ) -> pvtz_20180101_models.DeleteZoneRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_zone_record_with_options(request, runtime)

    async def delete_zone_record_async(
        self,
        request: pvtz_20180101_models.DeleteZoneRecordRequest,
    ) -> pvtz_20180101_models.DeleteZoneRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_zone_record_with_options_async(request, runtime)

    def describe_change_logs_with_options(
        self,
        request: pvtz_20180101_models.DescribeChangeLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeChangeLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.DescribeChangeLogsResponse().from_map(
            self.do_rpcrequest('DescribeChangeLogs', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_change_logs_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeChangeLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeChangeLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.DescribeChangeLogsResponse().from_map(
            await self.do_rpcrequest_async('DescribeChangeLogs', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_change_logs(
        self,
        request: pvtz_20180101_models.DescribeChangeLogsRequest,
    ) -> pvtz_20180101_models.DescribeChangeLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_change_logs_with_options(request, runtime)

    async def describe_change_logs_async(
        self,
        request: pvtz_20180101_models.DescribeChangeLogsRequest,
    ) -> pvtz_20180101_models.DescribeChangeLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_change_logs_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: pvtz_20180101_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: pvtz_20180101_models.DescribeRegionsRequest,
    ) -> pvtz_20180101_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: pvtz_20180101_models.DescribeRegionsRequest,
    ) -> pvtz_20180101_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_request_graph_with_options(
        self,
        request: pvtz_20180101_models.DescribeRequestGraphRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeRequestGraphResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.DescribeRequestGraphResponse().from_map(
            self.do_rpcrequest('DescribeRequestGraph', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_request_graph_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeRequestGraphRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeRequestGraphResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.DescribeRequestGraphResponse().from_map(
            await self.do_rpcrequest_async('DescribeRequestGraph', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_request_graph(
        self,
        request: pvtz_20180101_models.DescribeRequestGraphRequest,
    ) -> pvtz_20180101_models.DescribeRequestGraphResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_request_graph_with_options(request, runtime)

    async def describe_request_graph_async(
        self,
        request: pvtz_20180101_models.DescribeRequestGraphRequest,
    ) -> pvtz_20180101_models.DescribeRequestGraphResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_request_graph_with_options_async(request, runtime)

    def describe_statistic_summary_with_options(
        self,
        request: pvtz_20180101_models.DescribeStatisticSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeStatisticSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.DescribeStatisticSummaryResponse().from_map(
            self.do_rpcrequest('DescribeStatisticSummary', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_statistic_summary_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeStatisticSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeStatisticSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.DescribeStatisticSummaryResponse().from_map(
            await self.do_rpcrequest_async('DescribeStatisticSummary', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_statistic_summary(
        self,
        request: pvtz_20180101_models.DescribeStatisticSummaryRequest,
    ) -> pvtz_20180101_models.DescribeStatisticSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_statistic_summary_with_options(request, runtime)

    async def describe_statistic_summary_async(
        self,
        request: pvtz_20180101_models.DescribeStatisticSummaryRequest,
    ) -> pvtz_20180101_models.DescribeStatisticSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_statistic_summary_with_options_async(request, runtime)

    def describe_user_service_status_with_options(
        self,
        request: pvtz_20180101_models.DescribeUserServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeUserServiceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.DescribeUserServiceStatusResponse().from_map(
            self.do_rpcrequest('DescribeUserServiceStatus', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_service_status_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeUserServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeUserServiceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.DescribeUserServiceStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserServiceStatus', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_service_status(
        self,
        request: pvtz_20180101_models.DescribeUserServiceStatusRequest,
    ) -> pvtz_20180101_models.DescribeUserServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_service_status_with_options(request, runtime)

    async def describe_user_service_status_async(
        self,
        request: pvtz_20180101_models.DescribeUserServiceStatusRequest,
    ) -> pvtz_20180101_models.DescribeUserServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_service_status_with_options_async(request, runtime)

    def describe_zone_info_with_options(
        self,
        request: pvtz_20180101_models.DescribeZoneInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeZoneInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.DescribeZoneInfoResponse().from_map(
            self.do_rpcrequest('DescribeZoneInfo', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_zone_info_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeZoneInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeZoneInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.DescribeZoneInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeZoneInfo', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_zone_info(
        self,
        request: pvtz_20180101_models.DescribeZoneInfoRequest,
    ) -> pvtz_20180101_models.DescribeZoneInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_zone_info_with_options(request, runtime)

    async def describe_zone_info_async(
        self,
        request: pvtz_20180101_models.DescribeZoneInfoRequest,
    ) -> pvtz_20180101_models.DescribeZoneInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_zone_info_with_options_async(request, runtime)

    def describe_zone_records_with_options(
        self,
        request: pvtz_20180101_models.DescribeZoneRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeZoneRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.DescribeZoneRecordsResponse().from_map(
            self.do_rpcrequest('DescribeZoneRecords', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_zone_records_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeZoneRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeZoneRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.DescribeZoneRecordsResponse().from_map(
            await self.do_rpcrequest_async('DescribeZoneRecords', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_zone_records(
        self,
        request: pvtz_20180101_models.DescribeZoneRecordsRequest,
    ) -> pvtz_20180101_models.DescribeZoneRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_zone_records_with_options(request, runtime)

    async def describe_zone_records_async(
        self,
        request: pvtz_20180101_models.DescribeZoneRecordsRequest,
    ) -> pvtz_20180101_models.DescribeZoneRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_zone_records_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: pvtz_20180101_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.DescribeZonesResponse().from_map(
            self.do_rpcrequest('DescribeZones', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.DescribeZonesResponse().from_map(
            await self.do_rpcrequest_async('DescribeZones', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_zones(
        self,
        request: pvtz_20180101_models.DescribeZonesRequest,
    ) -> pvtz_20180101_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: pvtz_20180101_models.DescribeZonesRequest,
    ) -> pvtz_20180101_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def describe_zone_vpc_tree_with_options(
        self,
        request: pvtz_20180101_models.DescribeZoneVpcTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeZoneVpcTreeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.DescribeZoneVpcTreeResponse().from_map(
            self.do_rpcrequest('DescribeZoneVpcTree', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_zone_vpc_tree_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeZoneVpcTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeZoneVpcTreeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.DescribeZoneVpcTreeResponse().from_map(
            await self.do_rpcrequest_async('DescribeZoneVpcTree', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_zone_vpc_tree(
        self,
        request: pvtz_20180101_models.DescribeZoneVpcTreeRequest,
    ) -> pvtz_20180101_models.DescribeZoneVpcTreeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_zone_vpc_tree_with_options(request, runtime)

    async def describe_zone_vpc_tree_async(
        self,
        request: pvtz_20180101_models.DescribeZoneVpcTreeRequest,
    ) -> pvtz_20180101_models.DescribeZoneVpcTreeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_zone_vpc_tree_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: pvtz_20180101_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.MoveResourceGroupResponse().from_map(
            self.do_rpcrequest('MoveResourceGroup', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: pvtz_20180101_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.MoveResourceGroupResponse().from_map(
            await self.do_rpcrequest_async('MoveResourceGroup', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def move_resource_group(
        self,
        request: pvtz_20180101_models.MoveResourceGroupRequest,
    ) -> pvtz_20180101_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: pvtz_20180101_models.MoveResourceGroupRequest,
    ) -> pvtz_20180101_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def set_proxy_pattern_with_options(
        self,
        request: pvtz_20180101_models.SetProxyPatternRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.SetProxyPatternResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.SetProxyPatternResponse().from_map(
            self.do_rpcrequest('SetProxyPattern', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_proxy_pattern_with_options_async(
        self,
        request: pvtz_20180101_models.SetProxyPatternRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.SetProxyPatternResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.SetProxyPatternResponse().from_map(
            await self.do_rpcrequest_async('SetProxyPattern', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_proxy_pattern(
        self,
        request: pvtz_20180101_models.SetProxyPatternRequest,
    ) -> pvtz_20180101_models.SetProxyPatternResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_proxy_pattern_with_options(request, runtime)

    async def set_proxy_pattern_async(
        self,
        request: pvtz_20180101_models.SetProxyPatternRequest,
    ) -> pvtz_20180101_models.SetProxyPatternResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_proxy_pattern_with_options_async(request, runtime)

    def set_zone_record_status_with_options(
        self,
        request: pvtz_20180101_models.SetZoneRecordStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.SetZoneRecordStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.SetZoneRecordStatusResponse().from_map(
            self.do_rpcrequest('SetZoneRecordStatus', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_zone_record_status_with_options_async(
        self,
        request: pvtz_20180101_models.SetZoneRecordStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.SetZoneRecordStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.SetZoneRecordStatusResponse().from_map(
            await self.do_rpcrequest_async('SetZoneRecordStatus', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_zone_record_status(
        self,
        request: pvtz_20180101_models.SetZoneRecordStatusRequest,
    ) -> pvtz_20180101_models.SetZoneRecordStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_zone_record_status_with_options(request, runtime)

    async def set_zone_record_status_async(
        self,
        request: pvtz_20180101_models.SetZoneRecordStatusRequest,
    ) -> pvtz_20180101_models.SetZoneRecordStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_zone_record_status_with_options_async(request, runtime)

    def update_record_remark_with_options(
        self,
        request: pvtz_20180101_models.UpdateRecordRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UpdateRecordRemarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.UpdateRecordRemarkResponse().from_map(
            self.do_rpcrequest('UpdateRecordRemark', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_record_remark_with_options_async(
        self,
        request: pvtz_20180101_models.UpdateRecordRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UpdateRecordRemarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.UpdateRecordRemarkResponse().from_map(
            await self.do_rpcrequest_async('UpdateRecordRemark', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_record_remark(
        self,
        request: pvtz_20180101_models.UpdateRecordRemarkRequest,
    ) -> pvtz_20180101_models.UpdateRecordRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_record_remark_with_options(request, runtime)

    async def update_record_remark_async(
        self,
        request: pvtz_20180101_models.UpdateRecordRemarkRequest,
    ) -> pvtz_20180101_models.UpdateRecordRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_record_remark_with_options_async(request, runtime)

    def update_zone_record_with_options(
        self,
        request: pvtz_20180101_models.UpdateZoneRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UpdateZoneRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.UpdateZoneRecordResponse().from_map(
            self.do_rpcrequest('UpdateZoneRecord', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_zone_record_with_options_async(
        self,
        request: pvtz_20180101_models.UpdateZoneRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UpdateZoneRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.UpdateZoneRecordResponse().from_map(
            await self.do_rpcrequest_async('UpdateZoneRecord', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_zone_record(
        self,
        request: pvtz_20180101_models.UpdateZoneRecordRequest,
    ) -> pvtz_20180101_models.UpdateZoneRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_zone_record_with_options(request, runtime)

    async def update_zone_record_async(
        self,
        request: pvtz_20180101_models.UpdateZoneRecordRequest,
    ) -> pvtz_20180101_models.UpdateZoneRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_zone_record_with_options_async(request, runtime)

    def update_zone_remark_with_options(
        self,
        request: pvtz_20180101_models.UpdateZoneRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UpdateZoneRemarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.UpdateZoneRemarkResponse().from_map(
            self.do_rpcrequest('UpdateZoneRemark', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_zone_remark_with_options_async(
        self,
        request: pvtz_20180101_models.UpdateZoneRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UpdateZoneRemarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return pvtz_20180101_models.UpdateZoneRemarkResponse().from_map(
            await self.do_rpcrequest_async('UpdateZoneRemark', '2018-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_zone_remark(
        self,
        request: pvtz_20180101_models.UpdateZoneRemarkRequest,
    ) -> pvtz_20180101_models.UpdateZoneRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_zone_remark_with_options(request, runtime)

    async def update_zone_remark_async(
        self,
        request: pvtz_20180101_models.UpdateZoneRemarkRequest,
    ) -> pvtz_20180101_models.UpdateZoneRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_zone_remark_with_options_async(request, runtime)
