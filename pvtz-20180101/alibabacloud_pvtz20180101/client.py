# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_pvtz20180101 import models as pvtz_20180101_models
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
        query = {}
        query['Lang'] = request.lang
        query['ZoneName'] = request.zone_name
        query['ProxyPattern'] = request.proxy_pattern
        query['ResourceGroupId'] = request.resource_group_id
        query['ZoneType'] = request.zone_type
        query['ZoneTag'] = request.zone_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddZone',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.AddZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_zone_with_options_async(
        self,
        request: pvtz_20180101_models.AddZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.AddZoneResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ZoneName'] = request.zone_name
        query['ProxyPattern'] = request.proxy_pattern
        query['ResourceGroupId'] = request.resource_group_id
        query['ZoneType'] = request.zone_type
        query['ZoneTag'] = request.zone_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddZone',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.AddZoneResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ZoneId'] = request.zone_id
        query['Lang'] = request.lang
        query['Rr'] = request.rr
        query['Type'] = request.type
        query['Ttl'] = request.ttl
        query['Priority'] = request.priority
        query['Value'] = request.value
        query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddZoneRecord',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.AddZoneRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_zone_record_with_options_async(
        self,
        request: pvtz_20180101_models.AddZoneRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.AddZoneRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ZoneId'] = request.zone_id
        query['Lang'] = request.lang
        query['Rr'] = request.rr
        query['Type'] = request.type
        query['Ttl'] = request.ttl
        query['Priority'] = request.priority
        query['Value'] = request.value
        query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddZoneRecord',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.AddZoneRecordResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Lang'] = request.lang
        query['ZoneId'] = request.zone_id
        query['UserClientIp'] = request.user_client_ip
        query['Vpcs'] = request.vpcs
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BindZoneVpc',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.BindZoneVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_zone_vpc_with_options_async(
        self,
        request: pvtz_20180101_models.BindZoneVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.BindZoneVpcResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ZoneId'] = request.zone_id
        query['UserClientIp'] = request.user_client_ip
        query['Vpcs'] = request.vpcs
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BindZoneVpc',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.BindZoneVpcResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Lang'] = request.lang
        query['ZoneName'] = request.zone_name
        query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckZoneName',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.CheckZoneNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_zone_name_with_options_async(
        self,
        request: pvtz_20180101_models.CheckZoneNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.CheckZoneNameResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ZoneName'] = request.zone_name
        query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckZoneName',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.CheckZoneNameResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Lang'] = request.lang
        query['ZoneId'] = request.zone_id
        query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteZone',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DeleteZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_zone_with_options_async(
        self,
        request: pvtz_20180101_models.DeleteZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DeleteZoneResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ZoneId'] = request.zone_id
        query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteZone',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DeleteZoneResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Lang'] = request.lang
        query['RecordId'] = request.record_id
        query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteZoneRecord',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DeleteZoneRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_zone_record_with_options_async(
        self,
        request: pvtz_20180101_models.DeleteZoneRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DeleteZoneRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['RecordId'] = request.record_id
        query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteZoneRecord',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DeleteZoneRecordResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Keyword'] = request.keyword
        query['Lang'] = request.lang
        query['ZoneId'] = request.zone_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StartTimestamp'] = request.start_timestamp
        query['EndTimestamp'] = request.end_timestamp
        query['EntityType'] = request.entity_type
        query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeChangeLogs',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeChangeLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_change_logs_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeChangeLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeChangeLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Keyword'] = request.keyword
        query['Lang'] = request.lang
        query['ZoneId'] = request.zone_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StartTimestamp'] = request.start_timestamp
        query['EndTimestamp'] = request.end_timestamp
        query['EntityType'] = request.entity_type
        query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeChangeLogs',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeChangeLogsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['AcceptLanguage'] = request.accept_language
        query['AuthorizedUserId'] = request.authorized_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['AcceptLanguage'] = request.accept_language
        query['AuthorizedUserId'] = request.authorized_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['ZoneId'] = request.zone_id
        query['VpcId'] = request.vpc_id
        query['StartTimestamp'] = request.start_timestamp
        query['EndTimestamp'] = request.end_timestamp
        query['BizType'] = request.biz_type
        query['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRequestGraph',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeRequestGraphResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_request_graph_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeRequestGraphRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeRequestGraphResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        query['ZoneId'] = request.zone_id
        query['VpcId'] = request.vpc_id
        query['StartTimestamp'] = request.start_timestamp
        query['EndTimestamp'] = request.end_timestamp
        query['BizType'] = request.biz_type
        query['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRequestGraph',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeRequestGraphResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeStatisticSummary',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeStatisticSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_statistic_summary_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeStatisticSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeStatisticSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeStatisticSummary',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeStatisticSummaryResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_tags_with_options(
        self,
        request: pvtz_20180101_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ResourceType'] = request.resource_type
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tags_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ResourceType'] = request.resource_type
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tags(
        self,
        request: pvtz_20180101_models.DescribeTagsRequest,
    ) -> pvtz_20180101_models.DescribeTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    async def describe_tags_async(
        self,
        request: pvtz_20180101_models.DescribeTagsRequest,
    ) -> pvtz_20180101_models.DescribeTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tags_with_options_async(request, runtime)

    def describe_zone_info_with_options(
        self,
        request: pvtz_20180101_models.DescribeZoneInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeZoneInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeZoneInfo',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeZoneInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zone_info_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeZoneInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeZoneInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeZoneInfo',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeZoneInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Lang'] = request.lang
        query['Keyword'] = request.keyword
        query['ZoneId'] = request.zone_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['UserClientIp'] = request.user_client_ip
        query['Tag'] = request.tag
        query['SearchMode'] = request.search_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeZoneRecords',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeZoneRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zone_records_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeZoneRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeZoneRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['Keyword'] = request.keyword
        query['ZoneId'] = request.zone_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['UserClientIp'] = request.user_client_ip
        query['Tag'] = request.tag
        query['SearchMode'] = request.search_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeZoneRecords',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeZoneRecordsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Lang'] = request.lang
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Keyword'] = request.keyword
        query['SearchMode'] = request.search_mode
        query['QueryRegionId'] = request.query_region_id
        query['QueryVpcId'] = request.query_vpc_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ZoneType'] = request.zone_type
        query['ZoneTag'] = request.zone_tag
        query['ResourceTag'] = request.resource_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Keyword'] = request.keyword
        query['SearchMode'] = request.search_mode
        query['QueryRegionId'] = request.query_region_id
        query['QueryVpcId'] = request.query_vpc_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ZoneType'] = request.zone_type
        query['ZoneTag'] = request.zone_tag
        query['ResourceTag'] = request.resource_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeZoneVpcTree',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeZoneVpcTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zone_vpc_tree_with_options_async(
        self,
        request: pvtz_20180101_models.DescribeZoneVpcTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.DescribeZoneVpcTreeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeZoneVpcTree',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.DescribeZoneVpcTreeResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_tag_resources_with_options(
        self,
        request: pvtz_20180101_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ResourceType'] = request.resource_type
        query['NextToken'] = request.next_token
        query['Size'] = request.size
        query['ResourceId'] = request.resource_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: pvtz_20180101_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ResourceType'] = request.resource_type
        query['NextToken'] = request.next_token
        query['Size'] = request.size
        query['ResourceId'] = request.resource_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: pvtz_20180101_models.ListTagResourcesRequest,
    ) -> pvtz_20180101_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: pvtz_20180101_models.ListTagResourcesRequest,
    ) -> pvtz_20180101_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: pvtz_20180101_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ResourceId'] = request.resource_id
        query['NewResourceGroupId'] = request.new_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: pvtz_20180101_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ResourceId'] = request.resource_id
        query['NewResourceGroupId'] = request.new_resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Lang'] = request.lang
        query['ZoneId'] = request.zone_id
        query['ProxyPattern'] = request.proxy_pattern
        query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetProxyPattern',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.SetProxyPatternResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_proxy_pattern_with_options_async(
        self,
        request: pvtz_20180101_models.SetProxyPatternRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.SetProxyPatternResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ZoneId'] = request.zone_id
        query['ProxyPattern'] = request.proxy_pattern
        query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetProxyPattern',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.SetProxyPatternResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Lang'] = request.lang
        query['RecordId'] = request.record_id
        query['Status'] = request.status
        query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetZoneRecordStatus',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.SetZoneRecordStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_zone_record_status_with_options_async(
        self,
        request: pvtz_20180101_models.SetZoneRecordStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.SetZoneRecordStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['RecordId'] = request.record_id
        query['Status'] = request.status
        query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetZoneRecordStatus',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.SetZoneRecordStatusResponse(),
            await self.call_api_async(params, req, runtime)
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

    def tag_resources_with_options(
        self,
        request: pvtz_20180101_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ResourceType'] = request.resource_type
        query['OverWrite'] = request.over_write
        query['ResourceId'] = request.resource_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: pvtz_20180101_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ResourceType'] = request.resource_type
        query['OverWrite'] = request.over_write
        query['ResourceId'] = request.resource_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: pvtz_20180101_models.TagResourcesRequest,
    ) -> pvtz_20180101_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: pvtz_20180101_models.TagResourcesRequest,
    ) -> pvtz_20180101_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: pvtz_20180101_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ResourceType'] = request.resource_type
        query['All'] = request.all
        query['ResourceId'] = request.resource_id
        query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: pvtz_20180101_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ResourceType'] = request.resource_type
        query['All'] = request.all
        query['ResourceId'] = request.resource_id
        query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: pvtz_20180101_models.UntagResourcesRequest,
    ) -> pvtz_20180101_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: pvtz_20180101_models.UntagResourcesRequest,
    ) -> pvtz_20180101_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_record_remark_with_options(
        self,
        request: pvtz_20180101_models.UpdateRecordRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UpdateRecordRemarkResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['RecordId'] = request.record_id
        query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateRecordRemark',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.UpdateRecordRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_record_remark_with_options_async(
        self,
        request: pvtz_20180101_models.UpdateRecordRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UpdateRecordRemarkResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['RecordId'] = request.record_id
        query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateRecordRemark',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.UpdateRecordRemarkResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Rr'] = request.rr
        query['Lang'] = request.lang
        query['RecordId'] = request.record_id
        query['Type'] = request.type
        query['Ttl'] = request.ttl
        query['Priority'] = request.priority
        query['Value'] = request.value
        query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateZoneRecord',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.UpdateZoneRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_zone_record_with_options_async(
        self,
        request: pvtz_20180101_models.UpdateZoneRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UpdateZoneRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Rr'] = request.rr
        query['Lang'] = request.lang
        query['RecordId'] = request.record_id
        query['Type'] = request.type
        query['Ttl'] = request.ttl
        query['Priority'] = request.priority
        query['Value'] = request.value
        query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateZoneRecord',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.UpdateZoneRecordResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Lang'] = request.lang
        query['ZoneId'] = request.zone_id
        query['Remark'] = request.remark
        query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateZoneRemark',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.UpdateZoneRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_zone_remark_with_options_async(
        self,
        request: pvtz_20180101_models.UpdateZoneRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> pvtz_20180101_models.UpdateZoneRemarkResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ZoneId'] = request.zone_id
        query['Remark'] = request.remark
        query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateZoneRemark',
            version='2018-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pvtz_20180101_models.UpdateZoneRemarkResponse(),
            await self.call_api_async(params, req, runtime)
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
