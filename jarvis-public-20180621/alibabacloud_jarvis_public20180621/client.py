# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_jarvis_public20180621 import models as jarvis_public_20180621_models
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
        self._endpoint = self.get_endpoint('jarvis-public', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_console_access_white_list_with_options(
        self,
        request: jarvis_public_20180621_models.CreateConsoleAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_public_20180621_models.CreateConsoleAccessWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_port):
            query['DstPort'] = request.dst_port
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.instance_info_list):
            query['InstanceInfoList'] = request.instance_info_list
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.live_time):
            query['LiveTime'] = request.live_time
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not UtilClient.is_unset(request.white_list_type):
            query['WhiteListType'] = request.white_list_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConsoleAccessWhiteList',
            version='2018-06-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_public_20180621_models.CreateConsoleAccessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_console_access_white_list_with_options_async(
        self,
        request: jarvis_public_20180621_models.CreateConsoleAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_public_20180621_models.CreateConsoleAccessWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_port):
            query['DstPort'] = request.dst_port
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.instance_info_list):
            query['InstanceInfoList'] = request.instance_info_list
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.live_time):
            query['LiveTime'] = request.live_time
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not UtilClient.is_unset(request.white_list_type):
            query['WhiteListType'] = request.white_list_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConsoleAccessWhiteList',
            version='2018-06-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_public_20180621_models.CreateConsoleAccessWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_console_access_white_list(
        self,
        request: jarvis_public_20180621_models.CreateConsoleAccessWhiteListRequest,
    ) -> jarvis_public_20180621_models.CreateConsoleAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_console_access_white_list_with_options(request, runtime)

    async def create_console_access_white_list_async(
        self,
        request: jarvis_public_20180621_models.CreateConsoleAccessWhiteListRequest,
    ) -> jarvis_public_20180621_models.CreateConsoleAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_console_access_white_list_with_options_async(request, runtime)

    def delete_console_access_white_list_with_options(
        self,
        request: jarvis_public_20180621_models.DeleteConsoleAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_public_20180621_models.DeleteConsoleAccessWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disable_whitelist):
            query['DisableWhitelist'] = request.disable_whitelist
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConsoleAccessWhiteList',
            version='2018-06-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_public_20180621_models.DeleteConsoleAccessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_console_access_white_list_with_options_async(
        self,
        request: jarvis_public_20180621_models.DeleteConsoleAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_public_20180621_models.DeleteConsoleAccessWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disable_whitelist):
            query['DisableWhitelist'] = request.disable_whitelist
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConsoleAccessWhiteList',
            version='2018-06-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_public_20180621_models.DeleteConsoleAccessWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_console_access_white_list(
        self,
        request: jarvis_public_20180621_models.DeleteConsoleAccessWhiteListRequest,
    ) -> jarvis_public_20180621_models.DeleteConsoleAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_console_access_white_list_with_options(request, runtime)

    async def delete_console_access_white_list_async(
        self,
        request: jarvis_public_20180621_models.DeleteConsoleAccessWhiteListRequest,
    ) -> jarvis_public_20180621_models.DeleteConsoleAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_console_access_white_list_with_options_async(request, runtime)

    def describe_access_white_list_slb_list_with_options(
        self,
        request: jarvis_public_20180621_models.DescribeAccessWhiteListSlbListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_public_20180621_models.DescribeAccessWhiteListSlbListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessWhiteListSlbList',
            version='2018-06-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_public_20180621_models.DescribeAccessWhiteListSlbListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_white_list_slb_list_with_options_async(
        self,
        request: jarvis_public_20180621_models.DescribeAccessWhiteListSlbListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_public_20180621_models.DescribeAccessWhiteListSlbListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessWhiteListSlbList',
            version='2018-06-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_public_20180621_models.DescribeAccessWhiteListSlbListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_white_list_slb_list(
        self,
        request: jarvis_public_20180621_models.DescribeAccessWhiteListSlbListRequest,
    ) -> jarvis_public_20180621_models.DescribeAccessWhiteListSlbListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_access_white_list_slb_list_with_options(request, runtime)

    async def describe_access_white_list_slb_list_async(
        self,
        request: jarvis_public_20180621_models.DescribeAccessWhiteListSlbListRequest,
    ) -> jarvis_public_20180621_models.DescribeAccessWhiteListSlbListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_access_white_list_slb_list_with_options_async(request, runtime)

    def describe_access_whitelist_ecs_list_with_options(
        self,
        request: jarvis_public_20180621_models.DescribeAccessWhitelistEcsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_public_20180621_models.DescribeAccessWhitelistEcsListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessWhitelistEcsList',
            version='2018-06-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_public_20180621_models.DescribeAccessWhitelistEcsListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_whitelist_ecs_list_with_options_async(
        self,
        request: jarvis_public_20180621_models.DescribeAccessWhitelistEcsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_public_20180621_models.DescribeAccessWhitelistEcsListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessWhitelistEcsList',
            version='2018-06-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_public_20180621_models.DescribeAccessWhitelistEcsListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_whitelist_ecs_list(
        self,
        request: jarvis_public_20180621_models.DescribeAccessWhitelistEcsListRequest,
    ) -> jarvis_public_20180621_models.DescribeAccessWhitelistEcsListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_access_whitelist_ecs_list_with_options(request, runtime)

    async def describe_access_whitelist_ecs_list_async(
        self,
        request: jarvis_public_20180621_models.DescribeAccessWhitelistEcsListRequest,
    ) -> jarvis_public_20180621_models.DescribeAccessWhitelistEcsListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_access_whitelist_ecs_list_with_options_async(request, runtime)

    def describe_attack_event_with_options(
        self,
        request: jarvis_public_20180621_models.DescribeAttackEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_public_20180621_models.DescribeAttackEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.server_ip_list):
            query['ServerIpList'] = request.server_ip_list
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAttackEvent',
            version='2018-06-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_public_20180621_models.DescribeAttackEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_attack_event_with_options_async(
        self,
        request: jarvis_public_20180621_models.DescribeAttackEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_public_20180621_models.DescribeAttackEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.server_ip_list):
            query['ServerIpList'] = request.server_ip_list
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAttackEvent',
            version='2018-06-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_public_20180621_models.DescribeAttackEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_attack_event(
        self,
        request: jarvis_public_20180621_models.DescribeAttackEventRequest,
    ) -> jarvis_public_20180621_models.DescribeAttackEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_attack_event_with_options(request, runtime)

    async def describe_attack_event_async(
        self,
        request: jarvis_public_20180621_models.DescribeAttackEventRequest,
    ) -> jarvis_public_20180621_models.DescribeAttackEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_attack_event_with_options_async(request, runtime)

    def describe_attacked_ip_with_options(
        self,
        request: jarvis_public_20180621_models.DescribeAttackedIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_public_20180621_models.DescribeAttackedIpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.server_ip_list):
            query['ServerIpList'] = request.server_ip_list
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAttackedIp',
            version='2018-06-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_public_20180621_models.DescribeAttackedIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_attacked_ip_with_options_async(
        self,
        request: jarvis_public_20180621_models.DescribeAttackedIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_public_20180621_models.DescribeAttackedIpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.server_ip_list):
            query['ServerIpList'] = request.server_ip_list
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAttackedIp',
            version='2018-06-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_public_20180621_models.DescribeAttackedIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_attacked_ip(
        self,
        request: jarvis_public_20180621_models.DescribeAttackedIpRequest,
    ) -> jarvis_public_20180621_models.DescribeAttackedIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_attacked_ip_with_options(request, runtime)

    async def describe_attacked_ip_async(
        self,
        request: jarvis_public_20180621_models.DescribeAttackedIpRequest,
    ) -> jarvis_public_20180621_models.DescribeAttackedIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_attacked_ip_with_options_async(request, runtime)

    def describe_console_access_white_list_with_options(
        self,
        request: jarvis_public_20180621_models.DescribeConsoleAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_public_20180621_models.DescribeConsoleAccessWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.white_list_type):
            query['WhiteListType'] = request.white_list_type
        if not UtilClient.is_unset(request.query_product):
            query['queryProduct'] = request.query_product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConsoleAccessWhiteList',
            version='2018-06-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_public_20180621_models.DescribeConsoleAccessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_console_access_white_list_with_options_async(
        self,
        request: jarvis_public_20180621_models.DescribeConsoleAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_public_20180621_models.DescribeConsoleAccessWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.white_list_type):
            query['WhiteListType'] = request.white_list_type
        if not UtilClient.is_unset(request.query_product):
            query['queryProduct'] = request.query_product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConsoleAccessWhiteList',
            version='2018-06-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_public_20180621_models.DescribeConsoleAccessWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_console_access_white_list(
        self,
        request: jarvis_public_20180621_models.DescribeConsoleAccessWhiteListRequest,
    ) -> jarvis_public_20180621_models.DescribeConsoleAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_console_access_white_list_with_options(request, runtime)

    async def describe_console_access_white_list_async(
        self,
        request: jarvis_public_20180621_models.DescribeConsoleAccessWhiteListRequest,
    ) -> jarvis_public_20180621_models.DescribeConsoleAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_console_access_white_list_with_options_async(request, runtime)

    def describe_count_attack_event_with_options(
        self,
        request: jarvis_public_20180621_models.DescribeCountAttackEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_public_20180621_models.DescribeCountAttackEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.server_ip_list):
            query['ServerIpList'] = request.server_ip_list
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCountAttackEvent',
            version='2018-06-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_public_20180621_models.DescribeCountAttackEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_count_attack_event_with_options_async(
        self,
        request: jarvis_public_20180621_models.DescribeCountAttackEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_public_20180621_models.DescribeCountAttackEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.server_ip_list):
            query['ServerIpList'] = request.server_ip_list
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCountAttackEvent',
            version='2018-06-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_public_20180621_models.DescribeCountAttackEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_count_attack_event(
        self,
        request: jarvis_public_20180621_models.DescribeCountAttackEventRequest,
    ) -> jarvis_public_20180621_models.DescribeCountAttackEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_count_attack_event_with_options(request, runtime)

    async def describe_count_attack_event_async(
        self,
        request: jarvis_public_20180621_models.DescribeCountAttackEventRequest,
    ) -> jarvis_public_20180621_models.DescribeCountAttackEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_count_attack_event_with_options_async(request, runtime)

    def describe_phone_info_with_options(
        self,
        request: jarvis_public_20180621_models.DescribePhoneInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_public_20180621_models.DescribePhoneInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.phone_num):
            query['phoneNum'] = request.phone_num
        if not UtilClient.is_unset(request.source_code):
            query['sourceCode'] = request.source_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePhoneInfo',
            version='2018-06-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_public_20180621_models.DescribePhoneInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_phone_info_with_options_async(
        self,
        request: jarvis_public_20180621_models.DescribePhoneInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_public_20180621_models.DescribePhoneInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.phone_num):
            query['phoneNum'] = request.phone_num
        if not UtilClient.is_unset(request.source_code):
            query['sourceCode'] = request.source_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePhoneInfo',
            version='2018-06-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_public_20180621_models.DescribePhoneInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_phone_info(
        self,
        request: jarvis_public_20180621_models.DescribePhoneInfoRequest,
    ) -> jarvis_public_20180621_models.DescribePhoneInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_phone_info_with_options(request, runtime)

    async def describe_phone_info_async(
        self,
        request: jarvis_public_20180621_models.DescribePhoneInfoRequest,
    ) -> jarvis_public_20180621_models.DescribePhoneInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_phone_info_with_options_async(request, runtime)
