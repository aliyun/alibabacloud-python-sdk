# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_jarvis20180206 import models as jarvis_20180206_models
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
        self._endpoint = self.get_endpoint('jarvis', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_access_white_list_group_with_options(
        self,
        request: jarvis_20180206_models.CreateAccessWhiteListGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.CreateAccessWhiteListGroupResponse:
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
            action='CreateAccessWhiteListGroup',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.CreateAccessWhiteListGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_white_list_group_with_options_async(
        self,
        request: jarvis_20180206_models.CreateAccessWhiteListGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.CreateAccessWhiteListGroupResponse:
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
            action='CreateAccessWhiteListGroup',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.CreateAccessWhiteListGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_access_white_list_group(
        self,
        request: jarvis_20180206_models.CreateAccessWhiteListGroupRequest,
    ) -> jarvis_20180206_models.CreateAccessWhiteListGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_access_white_list_group_with_options(request, runtime)

    async def create_access_white_list_group_async(
        self,
        request: jarvis_20180206_models.CreateAccessWhiteListGroupRequest,
    ) -> jarvis_20180206_models.CreateAccessWhiteListGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_access_white_list_group_with_options_async(request, runtime)

    def create_all_ecs_white_list_with_options(
        self,
        request: jarvis_20180206_models.CreateAllEcsWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.CreateAllEcsWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIP'] = request.src_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAllEcsWhiteList',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.CreateAllEcsWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_all_ecs_white_list_with_options_async(
        self,
        request: jarvis_20180206_models.CreateAllEcsWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.CreateAllEcsWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIP'] = request.src_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAllEcsWhiteList',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.CreateAllEcsWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_all_ecs_white_list(
        self,
        request: jarvis_20180206_models.CreateAllEcsWhiteListRequest,
    ) -> jarvis_20180206_models.CreateAllEcsWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_all_ecs_white_list_with_options(request, runtime)

    async def create_all_ecs_white_list_async(
        self,
        request: jarvis_20180206_models.CreateAllEcsWhiteListRequest,
    ) -> jarvis_20180206_models.CreateAllEcsWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_all_ecs_white_list_with_options_async(request, runtime)

    def create_cdn_ip_with_options(
        self,
        request: jarvis_20180206_models.CreateCdnIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.CreateCdnIpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdn_ip_list):
            query['CdnIpList'] = request.cdn_ip_list
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCdnIp',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.CreateCdnIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cdn_ip_with_options_async(
        self,
        request: jarvis_20180206_models.CreateCdnIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.CreateCdnIpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdn_ip_list):
            query['CdnIpList'] = request.cdn_ip_list
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCdnIp',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.CreateCdnIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cdn_ip(
        self,
        request: jarvis_20180206_models.CreateCdnIpRequest,
    ) -> jarvis_20180206_models.CreateCdnIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cdn_ip_with_options(request, runtime)

    async def create_cdn_ip_async(
        self,
        request: jarvis_20180206_models.CreateCdnIpRequest,
    ) -> jarvis_20180206_models.CreateCdnIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cdn_ip_with_options_async(request, runtime)

    def create_cdn_subscription_with_options(
        self,
        request: jarvis_20180206_models.CreateCdnSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.CreateCdnSubscriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdn_uid_list):
            query['CdnUidList'] = request.cdn_uid_list
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCdnSubscription',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.CreateCdnSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cdn_subscription_with_options_async(
        self,
        request: jarvis_20180206_models.CreateCdnSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.CreateCdnSubscriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdn_uid_list):
            query['CdnUidList'] = request.cdn_uid_list
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCdnSubscription',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.CreateCdnSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cdn_subscription(
        self,
        request: jarvis_20180206_models.CreateCdnSubscriptionRequest,
    ) -> jarvis_20180206_models.CreateCdnSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cdn_subscription_with_options(request, runtime)

    async def create_cdn_subscription_async(
        self,
        request: jarvis_20180206_models.CreateCdnSubscriptionRequest,
    ) -> jarvis_20180206_models.CreateCdnSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cdn_subscription_with_options_async(request, runtime)

    def create_console_access_white_list_with_options(
        self,
        request: jarvis_20180206_models.CreateConsoleAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.CreateConsoleAccessWhiteListResponse:
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
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.CreateConsoleAccessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_console_access_white_list_with_options_async(
        self,
        request: jarvis_20180206_models.CreateConsoleAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.CreateConsoleAccessWhiteListResponse:
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
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.CreateConsoleAccessWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_console_access_white_list(
        self,
        request: jarvis_20180206_models.CreateConsoleAccessWhiteListRequest,
    ) -> jarvis_20180206_models.CreateConsoleAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_console_access_white_list_with_options(request, runtime)

    async def create_console_access_white_list_async(
        self,
        request: jarvis_20180206_models.CreateConsoleAccessWhiteListRequest,
    ) -> jarvis_20180206_models.CreateConsoleAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_console_access_white_list_with_options_async(request, runtime)

    def create_cpmc_punish_feed_back_with_options(
        self,
        request: jarvis_20180206_models.CreateCpmcPunishFeedBackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.CreateCpmcPunishFeedBackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not UtilClient.is_unset(request.dst_port):
            query['DstPort'] = request.dst_port
        if not UtilClient.is_unset(request.feed_back):
            query['FeedBack'] = request.feed_back
        if not UtilClient.is_unset(request.gmt_create):
            query['GmtCreate'] = request.gmt_create
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not UtilClient.is_unset(request.punish_type):
            query['PunishType'] = request.punish_type
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not UtilClient.is_unset(request.src_port):
            query['SrcPort'] = request.src_port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCpmcPunishFeedBack',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.CreateCpmcPunishFeedBackResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cpmc_punish_feed_back_with_options_async(
        self,
        request: jarvis_20180206_models.CreateCpmcPunishFeedBackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.CreateCpmcPunishFeedBackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not UtilClient.is_unset(request.dst_port):
            query['DstPort'] = request.dst_port
        if not UtilClient.is_unset(request.feed_back):
            query['FeedBack'] = request.feed_back
        if not UtilClient.is_unset(request.gmt_create):
            query['GmtCreate'] = request.gmt_create
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not UtilClient.is_unset(request.punish_type):
            query['PunishType'] = request.punish_type
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not UtilClient.is_unset(request.src_port):
            query['SrcPort'] = request.src_port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCpmcPunishFeedBack',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.CreateCpmcPunishFeedBackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cpmc_punish_feed_back(
        self,
        request: jarvis_20180206_models.CreateCpmcPunishFeedBackRequest,
    ) -> jarvis_20180206_models.CreateCpmcPunishFeedBackResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cpmc_punish_feed_back_with_options(request, runtime)

    async def create_cpmc_punish_feed_back_async(
        self,
        request: jarvis_20180206_models.CreateCpmcPunishFeedBackRequest,
    ) -> jarvis_20180206_models.CreateCpmcPunishFeedBackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cpmc_punish_feed_back_with_options_async(request, runtime)

    def create_ip_white_baseline_with_options(
        self,
        request: jarvis_20180206_models.CreateIpWhiteBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.CreateIpWhiteBaselineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIp'] = request.src_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIpWhiteBaseline',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.CreateIpWhiteBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ip_white_baseline_with_options_async(
        self,
        request: jarvis_20180206_models.CreateIpWhiteBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.CreateIpWhiteBaselineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIp'] = request.src_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIpWhiteBaseline',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.CreateIpWhiteBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ip_white_baseline(
        self,
        request: jarvis_20180206_models.CreateIpWhiteBaselineRequest,
    ) -> jarvis_20180206_models.CreateIpWhiteBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ip_white_baseline_with_options(request, runtime)

    async def create_ip_white_baseline_async(
        self,
        request: jarvis_20180206_models.CreateIpWhiteBaselineRequest,
    ) -> jarvis_20180206_models.CreateIpWhiteBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ip_white_baseline_with_options_async(request, runtime)

    def create_mining_apply_with_options(
        self,
        request: jarvis_20180206_models.CreateMiningApplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.CreateMiningApplyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMiningApply',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.CreateMiningApplyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mining_apply_with_options_async(
        self,
        request: jarvis_20180206_models.CreateMiningApplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.CreateMiningApplyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMiningApply',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.CreateMiningApplyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mining_apply(
        self,
        request: jarvis_20180206_models.CreateMiningApplyRequest,
    ) -> jarvis_20180206_models.CreateMiningApplyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_mining_apply_with_options(request, runtime)

    async def create_mining_apply_async(
        self,
        request: jarvis_20180206_models.CreateMiningApplyRequest,
    ) -> jarvis_20180206_models.CreateMiningApplyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_mining_apply_with_options_async(request, runtime)

    def create_mining_report_with_options(
        self,
        request: jarvis_20180206_models.CreateMiningReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.CreateMiningReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMiningReport',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.CreateMiningReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mining_report_with_options_async(
        self,
        request: jarvis_20180206_models.CreateMiningReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.CreateMiningReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMiningReport',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.CreateMiningReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mining_report(
        self,
        request: jarvis_20180206_models.CreateMiningReportRequest,
    ) -> jarvis_20180206_models.CreateMiningReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_mining_report_with_options(request, runtime)

    async def create_mining_report_async(
        self,
        request: jarvis_20180206_models.CreateMiningReportRequest,
    ) -> jarvis_20180206_models.CreateMiningReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_mining_report_with_options_async(request, runtime)

    def create_mining_revoke_with_options(
        self,
        request: jarvis_20180206_models.CreateMiningRevokeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.CreateMiningRevokeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMiningRevoke',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.CreateMiningRevokeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mining_revoke_with_options_async(
        self,
        request: jarvis_20180206_models.CreateMiningRevokeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.CreateMiningRevokeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMiningRevoke',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.CreateMiningRevokeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mining_revoke(
        self,
        request: jarvis_20180206_models.CreateMiningRevokeRequest,
    ) -> jarvis_20180206_models.CreateMiningRevokeResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_mining_revoke_with_options(request, runtime)

    async def create_mining_revoke_async(
        self,
        request: jarvis_20180206_models.CreateMiningRevokeRequest,
    ) -> jarvis_20180206_models.CreateMiningRevokeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_mining_revoke_with_options_async(request, runtime)

    def create_uid_white_baseline_with_options(
        self,
        request: jarvis_20180206_models.CreateUidWhiteBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.CreateUidWhiteBaselineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_uid):
            query['SrcUid'] = request.src_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUidWhiteBaseline',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.CreateUidWhiteBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_uid_white_baseline_with_options_async(
        self,
        request: jarvis_20180206_models.CreateUidWhiteBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.CreateUidWhiteBaselineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_uid):
            query['SrcUid'] = request.src_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUidWhiteBaseline',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.CreateUidWhiteBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_uid_white_baseline(
        self,
        request: jarvis_20180206_models.CreateUidWhiteBaselineRequest,
    ) -> jarvis_20180206_models.CreateUidWhiteBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_uid_white_baseline_with_options(request, runtime)

    async def create_uid_white_baseline_async(
        self,
        request: jarvis_20180206_models.CreateUidWhiteBaselineRequest,
    ) -> jarvis_20180206_models.CreateUidWhiteBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_uid_white_baseline_with_options_async(request, runtime)

    def create_uid_white_list_group_with_options(
        self,
        request: jarvis_20180206_models.CreateUidWhiteListGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.CreateUidWhiteListGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_port):
            query['DstPort'] = request.dst_port
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
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
        if not UtilClient.is_unset(request.src_uid):
            query['SrcUid'] = request.src_uid
        if not UtilClient.is_unset(request.white_list_type):
            query['WhiteListType'] = request.white_list_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUidWhiteListGroup',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.CreateUidWhiteListGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_uid_white_list_group_with_options_async(
        self,
        request: jarvis_20180206_models.CreateUidWhiteListGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.CreateUidWhiteListGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_port):
            query['DstPort'] = request.dst_port
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
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
        if not UtilClient.is_unset(request.src_uid):
            query['SrcUid'] = request.src_uid
        if not UtilClient.is_unset(request.white_list_type):
            query['WhiteListType'] = request.white_list_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUidWhiteListGroup',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.CreateUidWhiteListGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_uid_white_list_group(
        self,
        request: jarvis_20180206_models.CreateUidWhiteListGroupRequest,
    ) -> jarvis_20180206_models.CreateUidWhiteListGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_uid_white_list_group_with_options(request, runtime)

    async def create_uid_white_list_group_async(
        self,
        request: jarvis_20180206_models.CreateUidWhiteListGroupRequest,
    ) -> jarvis_20180206_models.CreateUidWhiteListGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_uid_white_list_group_with_options_async(request, runtime)

    def delete_access_white_list_group_with_options(
        self,
        request: jarvis_20180206_models.DeleteAccessWhiteListGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DeleteAccessWhiteListGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id_list):
            query['GroupIdList'] = request.group_id_list
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
            action='DeleteAccessWhiteListGroup',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DeleteAccessWhiteListGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_white_list_group_with_options_async(
        self,
        request: jarvis_20180206_models.DeleteAccessWhiteListGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DeleteAccessWhiteListGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id_list):
            query['GroupIdList'] = request.group_id_list
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
            action='DeleteAccessWhiteListGroup',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DeleteAccessWhiteListGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_access_white_list_group(
        self,
        request: jarvis_20180206_models.DeleteAccessWhiteListGroupRequest,
    ) -> jarvis_20180206_models.DeleteAccessWhiteListGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_access_white_list_group_with_options(request, runtime)

    async def delete_access_white_list_group_async(
        self,
        request: jarvis_20180206_models.DeleteAccessWhiteListGroupRequest,
    ) -> jarvis_20180206_models.DeleteAccessWhiteListGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_access_white_list_group_with_options_async(request, runtime)

    def delete_cdn_ip_with_options(
        self,
        request: jarvis_20180206_models.DeleteCdnIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DeleteCdnIpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdn_ip):
            query['CdnIp'] = request.cdn_ip
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCdnIp',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DeleteCdnIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cdn_ip_with_options_async(
        self,
        request: jarvis_20180206_models.DeleteCdnIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DeleteCdnIpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdn_ip):
            query['CdnIp'] = request.cdn_ip
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCdnIp',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DeleteCdnIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cdn_ip(
        self,
        request: jarvis_20180206_models.DeleteCdnIpRequest,
    ) -> jarvis_20180206_models.DeleteCdnIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cdn_ip_with_options(request, runtime)

    async def delete_cdn_ip_async(
        self,
        request: jarvis_20180206_models.DeleteCdnIpRequest,
    ) -> jarvis_20180206_models.DeleteCdnIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cdn_ip_with_options_async(request, runtime)

    def delete_cdn_subscription_with_options(
        self,
        request: jarvis_20180206_models.DeleteCdnSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DeleteCdnSubscriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdn_uid_list):
            query['CdnUidList'] = request.cdn_uid_list
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
            action='DeleteCdnSubscription',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DeleteCdnSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cdn_subscription_with_options_async(
        self,
        request: jarvis_20180206_models.DeleteCdnSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DeleteCdnSubscriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdn_uid_list):
            query['CdnUidList'] = request.cdn_uid_list
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
            action='DeleteCdnSubscription',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DeleteCdnSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cdn_subscription(
        self,
        request: jarvis_20180206_models.DeleteCdnSubscriptionRequest,
    ) -> jarvis_20180206_models.DeleteCdnSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cdn_subscription_with_options(request, runtime)

    async def delete_cdn_subscription_async(
        self,
        request: jarvis_20180206_models.DeleteCdnSubscriptionRequest,
    ) -> jarvis_20180206_models.DeleteCdnSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cdn_subscription_with_options_async(request, runtime)

    def delete_console_access_white_list_with_options(
        self,
        request: jarvis_20180206_models.DeleteConsoleAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DeleteConsoleAccessWhiteListResponse:
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
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DeleteConsoleAccessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_console_access_white_list_with_options_async(
        self,
        request: jarvis_20180206_models.DeleteConsoleAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DeleteConsoleAccessWhiteListResponse:
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
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DeleteConsoleAccessWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_console_access_white_list(
        self,
        request: jarvis_20180206_models.DeleteConsoleAccessWhiteListRequest,
    ) -> jarvis_20180206_models.DeleteConsoleAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_console_access_white_list_with_options(request, runtime)

    async def delete_console_access_white_list_async(
        self,
        request: jarvis_20180206_models.DeleteConsoleAccessWhiteListRequest,
    ) -> jarvis_20180206_models.DeleteConsoleAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_console_access_white_list_with_options_async(request, runtime)

    def delete_cpmc_punish_with_options(
        self,
        request: jarvis_20180206_models.DeleteCpmcPunishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DeleteCpmcPunishResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ban_path):
            query['BanPath'] = request.ban_path
        if not UtilClient.is_unset(request.detect_id):
            query['DetectId'] = request.detect_id
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.dst_ip):
            query['DstIp'] = request.dst_ip
        if not UtilClient.is_unset(request.dst_port):
            query['DstPort'] = request.dst_port
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.evidence):
            query['Evidence'] = request.evidence
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.owner_ali_uid):
            query['OwnerAliUid'] = request.owner_ali_uid
        if not UtilClient.is_unset(request.punish_type):
            query['PunishType'] = request.punish_type
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.reg_name):
            query['RegName'] = request.reg_name
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.rule):
            query['Rule'] = request.rule
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.source_uid):
            query['SourceUid'] = request.source_uid
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIp'] = request.src_ip
        if not UtilClient.is_unset(request.src_port):
            query['SrcPort'] = request.src_port
        if not UtilClient.is_unset(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        if not UtilClient.is_unset(request.tunnel_id):
            query['TunnelId'] = request.tunnel_id
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCpmcPunish',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DeleteCpmcPunishResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cpmc_punish_with_options_async(
        self,
        request: jarvis_20180206_models.DeleteCpmcPunishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DeleteCpmcPunishResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ban_path):
            query['BanPath'] = request.ban_path
        if not UtilClient.is_unset(request.detect_id):
            query['DetectId'] = request.detect_id
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.dst_ip):
            query['DstIp'] = request.dst_ip
        if not UtilClient.is_unset(request.dst_port):
            query['DstPort'] = request.dst_port
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.evidence):
            query['Evidence'] = request.evidence
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.owner_ali_uid):
            query['OwnerAliUid'] = request.owner_ali_uid
        if not UtilClient.is_unset(request.punish_type):
            query['PunishType'] = request.punish_type
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.reg_name):
            query['RegName'] = request.reg_name
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.rule):
            query['Rule'] = request.rule
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.source_uid):
            query['SourceUid'] = request.source_uid
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIp'] = request.src_ip
        if not UtilClient.is_unset(request.src_port):
            query['SrcPort'] = request.src_port
        if not UtilClient.is_unset(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        if not UtilClient.is_unset(request.tunnel_id):
            query['TunnelId'] = request.tunnel_id
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCpmcPunish',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DeleteCpmcPunishResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cpmc_punish(
        self,
        request: jarvis_20180206_models.DeleteCpmcPunishRequest,
    ) -> jarvis_20180206_models.DeleteCpmcPunishResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cpmc_punish_with_options(request, runtime)

    async def delete_cpmc_punish_async(
        self,
        request: jarvis_20180206_models.DeleteCpmcPunishRequest,
    ) -> jarvis_20180206_models.DeleteCpmcPunishResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cpmc_punish_with_options_async(request, runtime)

    def delete_ip_white_baseline_with_options(
        self,
        request: jarvis_20180206_models.DeleteIpWhiteBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DeleteIpWhiteBaselineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.wbl_ip_list):
            query['WblIpList'] = request.wbl_ip_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIpWhiteBaseline',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DeleteIpWhiteBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ip_white_baseline_with_options_async(
        self,
        request: jarvis_20180206_models.DeleteIpWhiteBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DeleteIpWhiteBaselineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.wbl_ip_list):
            query['WblIpList'] = request.wbl_ip_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIpWhiteBaseline',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DeleteIpWhiteBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ip_white_baseline(
        self,
        request: jarvis_20180206_models.DeleteIpWhiteBaselineRequest,
    ) -> jarvis_20180206_models.DeleteIpWhiteBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ip_white_baseline_with_options(request, runtime)

    async def delete_ip_white_baseline_async(
        self,
        request: jarvis_20180206_models.DeleteIpWhiteBaselineRequest,
    ) -> jarvis_20180206_models.DeleteIpWhiteBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ip_white_baseline_with_options_async(request, runtime)

    def delete_uid_white_baseline_with_options(
        self,
        request: jarvis_20180206_models.DeleteUidWhiteBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DeleteUidWhiteBaselineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.wbl_uid_list):
            query['WblUidList'] = request.wbl_uid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUidWhiteBaseline',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DeleteUidWhiteBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_uid_white_baseline_with_options_async(
        self,
        request: jarvis_20180206_models.DeleteUidWhiteBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DeleteUidWhiteBaselineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.wbl_uid_list):
            query['WblUidList'] = request.wbl_uid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUidWhiteBaseline',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DeleteUidWhiteBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_uid_white_baseline(
        self,
        request: jarvis_20180206_models.DeleteUidWhiteBaselineRequest,
    ) -> jarvis_20180206_models.DeleteUidWhiteBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_uid_white_baseline_with_options(request, runtime)

    async def delete_uid_white_baseline_async(
        self,
        request: jarvis_20180206_models.DeleteUidWhiteBaselineRequest,
    ) -> jarvis_20180206_models.DeleteUidWhiteBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_uid_white_baseline_with_options_async(request, runtime)

    def delete_uid_white_list_group_with_options(
        self,
        request: jarvis_20180206_models.DeleteUidWhiteListGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DeleteUidWhiteListGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id_list):
            query['GroupIdList'] = request.group_id_list
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
            action='DeleteUidWhiteListGroup',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DeleteUidWhiteListGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_uid_white_list_group_with_options_async(
        self,
        request: jarvis_20180206_models.DeleteUidWhiteListGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DeleteUidWhiteListGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id_list):
            query['GroupIdList'] = request.group_id_list
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
            action='DeleteUidWhiteListGroup',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DeleteUidWhiteListGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_uid_white_list_group(
        self,
        request: jarvis_20180206_models.DeleteUidWhiteListGroupRequest,
    ) -> jarvis_20180206_models.DeleteUidWhiteListGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_uid_white_list_group_with_options(request, runtime)

    async def delete_uid_white_list_group_async(
        self,
        request: jarvis_20180206_models.DeleteUidWhiteListGroupRequest,
    ) -> jarvis_20180206_models.DeleteUidWhiteListGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_uid_white_list_group_with_options_async(request, runtime)

    def delete_white_list_conditional_with_options(
        self,
        request: jarvis_20180206_models.DeleteWhiteListConditionalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DeleteWhiteListConditionalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not UtilClient.is_unset(request.query_product):
            query['queryProduct'] = request.query_product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWhiteListConditional',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DeleteWhiteListConditionalResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_white_list_conditional_with_options_async(
        self,
        request: jarvis_20180206_models.DeleteWhiteListConditionalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DeleteWhiteListConditionalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not UtilClient.is_unset(request.query_product):
            query['queryProduct'] = request.query_product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWhiteListConditional',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DeleteWhiteListConditionalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_white_list_conditional(
        self,
        request: jarvis_20180206_models.DeleteWhiteListConditionalRequest,
    ) -> jarvis_20180206_models.DeleteWhiteListConditionalResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_white_list_conditional_with_options(request, runtime)

    async def delete_white_list_conditional_async(
        self,
        request: jarvis_20180206_models.DeleteWhiteListConditionalRequest,
    ) -> jarvis_20180206_models.DeleteWhiteListConditionalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_white_list_conditional_with_options_async(request, runtime)

    def delete_white_list_db_item_conditional_with_options(
        self,
        request: jarvis_20180206_models.DeleteWhiteListDbItemConditionalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DeleteWhiteListDbItemConditionalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not UtilClient.is_unset(request.query_product):
            query['queryProduct'] = request.query_product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWhiteListDbItemConditional',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DeleteWhiteListDbItemConditionalResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_white_list_db_item_conditional_with_options_async(
        self,
        request: jarvis_20180206_models.DeleteWhiteListDbItemConditionalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DeleteWhiteListDbItemConditionalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not UtilClient.is_unset(request.query_product):
            query['queryProduct'] = request.query_product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWhiteListDbItemConditional',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DeleteWhiteListDbItemConditionalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_white_list_db_item_conditional(
        self,
        request: jarvis_20180206_models.DeleteWhiteListDbItemConditionalRequest,
    ) -> jarvis_20180206_models.DeleteWhiteListDbItemConditionalResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_white_list_db_item_conditional_with_options(request, runtime)

    async def delete_white_list_db_item_conditional_async(
        self,
        request: jarvis_20180206_models.DeleteWhiteListDbItemConditionalRequest,
    ) -> jarvis_20180206_models.DeleteWhiteListDbItemConditionalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_white_list_db_item_conditional_with_options_async(request, runtime)

    def describe_access_white_list_eip_list_with_options(
        self,
        request: jarvis_20180206_models.DescribeAccessWhiteListEipListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeAccessWhiteListEipListResponse:
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
            action='DescribeAccessWhiteListEipList',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeAccessWhiteListEipListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_white_list_eip_list_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeAccessWhiteListEipListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeAccessWhiteListEipListResponse:
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
            action='DescribeAccessWhiteListEipList',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeAccessWhiteListEipListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_white_list_eip_list(
        self,
        request: jarvis_20180206_models.DescribeAccessWhiteListEipListRequest,
    ) -> jarvis_20180206_models.DescribeAccessWhiteListEipListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_access_white_list_eip_list_with_options(request, runtime)

    async def describe_access_white_list_eip_list_async(
        self,
        request: jarvis_20180206_models.DescribeAccessWhiteListEipListRequest,
    ) -> jarvis_20180206_models.DescribeAccessWhiteListEipListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_access_white_list_eip_list_with_options_async(request, runtime)

    def describe_access_white_list_group_with_options(
        self,
        request: jarvis_20180206_models.DescribeAccessWhiteListGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeAccessWhiteListGroupResponse:
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
            action='DescribeAccessWhiteListGroup',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeAccessWhiteListGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_white_list_group_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeAccessWhiteListGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeAccessWhiteListGroupResponse:
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
            action='DescribeAccessWhiteListGroup',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeAccessWhiteListGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_white_list_group(
        self,
        request: jarvis_20180206_models.DescribeAccessWhiteListGroupRequest,
    ) -> jarvis_20180206_models.DescribeAccessWhiteListGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_access_white_list_group_with_options(request, runtime)

    async def describe_access_white_list_group_async(
        self,
        request: jarvis_20180206_models.DescribeAccessWhiteListGroupRequest,
    ) -> jarvis_20180206_models.DescribeAccessWhiteListGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_access_white_list_group_with_options_async(request, runtime)

    def describe_access_white_list_rds_list_with_options(
        self,
        request: jarvis_20180206_models.DescribeAccessWhiteListRdsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeAccessWhiteListRdsListResponse:
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
            action='DescribeAccessWhiteListRdsList',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeAccessWhiteListRdsListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_white_list_rds_list_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeAccessWhiteListRdsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeAccessWhiteListRdsListResponse:
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
            action='DescribeAccessWhiteListRdsList',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeAccessWhiteListRdsListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_white_list_rds_list(
        self,
        request: jarvis_20180206_models.DescribeAccessWhiteListRdsListRequest,
    ) -> jarvis_20180206_models.DescribeAccessWhiteListRdsListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_access_white_list_rds_list_with_options(request, runtime)

    async def describe_access_white_list_rds_list_async(
        self,
        request: jarvis_20180206_models.DescribeAccessWhiteListRdsListRequest,
    ) -> jarvis_20180206_models.DescribeAccessWhiteListRdsListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_access_white_list_rds_list_with_options_async(request, runtime)

    def describe_access_white_list_slb_list_with_options(
        self,
        request: jarvis_20180206_models.DescribeAccessWhiteListSlbListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeAccessWhiteListSlbListResponse:
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
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeAccessWhiteListSlbListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_white_list_slb_list_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeAccessWhiteListSlbListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeAccessWhiteListSlbListResponse:
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
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeAccessWhiteListSlbListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_white_list_slb_list(
        self,
        request: jarvis_20180206_models.DescribeAccessWhiteListSlbListRequest,
    ) -> jarvis_20180206_models.DescribeAccessWhiteListSlbListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_access_white_list_slb_list_with_options(request, runtime)

    async def describe_access_white_list_slb_list_async(
        self,
        request: jarvis_20180206_models.DescribeAccessWhiteListSlbListRequest,
    ) -> jarvis_20180206_models.DescribeAccessWhiteListSlbListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_access_white_list_slb_list_with_options_async(request, runtime)

    def describe_access_white_list_swas_list_with_options(
        self,
        request: jarvis_20180206_models.DescribeAccessWhiteListSwasListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeAccessWhiteListSwasListResponse:
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
            action='DescribeAccessWhiteListSwasList',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeAccessWhiteListSwasListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_white_list_swas_list_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeAccessWhiteListSwasListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeAccessWhiteListSwasListResponse:
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
            action='DescribeAccessWhiteListSwasList',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeAccessWhiteListSwasListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_white_list_swas_list(
        self,
        request: jarvis_20180206_models.DescribeAccessWhiteListSwasListRequest,
    ) -> jarvis_20180206_models.DescribeAccessWhiteListSwasListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_access_white_list_swas_list_with_options(request, runtime)

    async def describe_access_white_list_swas_list_async(
        self,
        request: jarvis_20180206_models.DescribeAccessWhiteListSwasListRequest,
    ) -> jarvis_20180206_models.DescribeAccessWhiteListSwasListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_access_white_list_swas_list_with_options_async(request, runtime)

    def describe_access_whitelist_ecs_list_with_options(
        self,
        request: jarvis_20180206_models.DescribeAccessWhitelistEcsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeAccessWhitelistEcsListResponse:
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
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeAccessWhitelistEcsListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_whitelist_ecs_list_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeAccessWhitelistEcsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeAccessWhitelistEcsListResponse:
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
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeAccessWhitelistEcsListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_whitelist_ecs_list(
        self,
        request: jarvis_20180206_models.DescribeAccessWhitelistEcsListRequest,
    ) -> jarvis_20180206_models.DescribeAccessWhitelistEcsListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_access_whitelist_ecs_list_with_options(request, runtime)

    async def describe_access_whitelist_ecs_list_async(
        self,
        request: jarvis_20180206_models.DescribeAccessWhitelistEcsListRequest,
    ) -> jarvis_20180206_models.DescribeAccessWhitelistEcsListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_access_whitelist_ecs_list_with_options_async(request, runtime)

    def describe_cdn_certify_with_options(
        self,
        request: jarvis_20180206_models.DescribeCdnCertifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeCdnCertifyResponse:
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
            action='DescribeCdnCertify',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeCdnCertifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_certify_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeCdnCertifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeCdnCertifyResponse:
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
            action='DescribeCdnCertify',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeCdnCertifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_certify(
        self,
        request: jarvis_20180206_models.DescribeCdnCertifyRequest,
    ) -> jarvis_20180206_models.DescribeCdnCertifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_certify_with_options(request, runtime)

    async def describe_cdn_certify_async(
        self,
        request: jarvis_20180206_models.DescribeCdnCertifyRequest,
    ) -> jarvis_20180206_models.DescribeCdnCertifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_certify_with_options_async(request, runtime)

    def describe_cdn_ip_list_with_options(
        self,
        request: jarvis_20180206_models.DescribeCdnIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeCdnIpListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
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
        if not UtilClient.is_unset(request.wl_state):
            query['WlState'] = request.wl_state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnIpList',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeCdnIpListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_ip_list_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeCdnIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeCdnIpListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
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
        if not UtilClient.is_unset(request.wl_state):
            query['WlState'] = request.wl_state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnIpList',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeCdnIpListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_ip_list(
        self,
        request: jarvis_20180206_models.DescribeCdnIpListRequest,
    ) -> jarvis_20180206_models.DescribeCdnIpListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_ip_list_with_options(request, runtime)

    async def describe_cdn_ip_list_async(
        self,
        request: jarvis_20180206_models.DescribeCdnIpListRequest,
    ) -> jarvis_20180206_models.DescribeCdnIpListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_ip_list_with_options_async(request, runtime)

    def describe_cdn_subscription_with_options(
        self,
        request: jarvis_20180206_models.DescribeCdnSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeCdnSubscriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.subscription_state):
            query['SubscriptionState'] = request.subscription_state
        if not UtilClient.is_unset(request.vendor_name):
            query['VendorName'] = request.vendor_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnSubscription',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeCdnSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_subscription_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeCdnSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeCdnSubscriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.subscription_state):
            query['SubscriptionState'] = request.subscription_state
        if not UtilClient.is_unset(request.vendor_name):
            query['VendorName'] = request.vendor_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnSubscription',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeCdnSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_subscription(
        self,
        request: jarvis_20180206_models.DescribeCdnSubscriptionRequest,
    ) -> jarvis_20180206_models.DescribeCdnSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_subscription_with_options(request, runtime)

    async def describe_cdn_subscription_async(
        self,
        request: jarvis_20180206_models.DescribeCdnSubscriptionRequest,
    ) -> jarvis_20180206_models.DescribeCdnSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_subscription_with_options_async(request, runtime)

    def describe_cdn_vendor_with_options(
        self,
        request: jarvis_20180206_models.DescribeCdnVendorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeCdnVendorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnVendor',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeCdnVendorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_vendor_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeCdnVendorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeCdnVendorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnVendor',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeCdnVendorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_vendor(
        self,
        request: jarvis_20180206_models.DescribeCdnVendorRequest,
    ) -> jarvis_20180206_models.DescribeCdnVendorResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_vendor_with_options(request, runtime)

    async def describe_cdn_vendor_async(
        self,
        request: jarvis_20180206_models.DescribeCdnVendorRequest,
    ) -> jarvis_20180206_models.DescribeCdnVendorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_vendor_with_options_async(request, runtime)

    def describe_console_access_white_list_with_options(
        self,
        request: jarvis_20180206_models.DescribeConsoleAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeConsoleAccessWhiteListResponse:
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
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeConsoleAccessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_console_access_white_list_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeConsoleAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeConsoleAccessWhiteListResponse:
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
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeConsoleAccessWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_console_access_white_list(
        self,
        request: jarvis_20180206_models.DescribeConsoleAccessWhiteListRequest,
    ) -> jarvis_20180206_models.DescribeConsoleAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_console_access_white_list_with_options(request, runtime)

    async def describe_console_access_white_list_async(
        self,
        request: jarvis_20180206_models.DescribeConsoleAccessWhiteListRequest,
    ) -> jarvis_20180206_models.DescribeConsoleAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_console_access_white_list_with_options_async(request, runtime)

    def describe_cpmc_punish_list_with_options(
        self,
        request: jarvis_20180206_models.DescribeCpmcPunishListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeCpmcPunishListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.punish_status):
            query['PunishStatus'] = request.punish_status
        if not UtilClient.is_unset(request.punish_type):
            query['PunishType'] = request.punish_type
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCpmcPunishList',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeCpmcPunishListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cpmc_punish_list_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeCpmcPunishListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeCpmcPunishListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.punish_status):
            query['PunishStatus'] = request.punish_status
        if not UtilClient.is_unset(request.punish_type):
            query['PunishType'] = request.punish_type
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCpmcPunishList',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeCpmcPunishListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cpmc_punish_list(
        self,
        request: jarvis_20180206_models.DescribeCpmcPunishListRequest,
    ) -> jarvis_20180206_models.DescribeCpmcPunishListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cpmc_punish_list_with_options(request, runtime)

    async def describe_cpmc_punish_list_async(
        self,
        request: jarvis_20180206_models.DescribeCpmcPunishListRequest,
    ) -> jarvis_20180206_models.DescribeCpmcPunishListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cpmc_punish_list_with_options_async(request, runtime)

    def describe_ddos_defense_info_with_options(
        self,
        request: jarvis_20180206_models.DescribeDdosDefenseInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeDdosDefenseInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.source_code):
            query['sourceCode'] = request.source_code
        if not UtilClient.is_unset(request.src_uid):
            query['srcUid'] = request.src_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDdosDefenseInfo',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeDdosDefenseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_defense_info_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeDdosDefenseInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeDdosDefenseInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.source_code):
            query['sourceCode'] = request.source_code
        if not UtilClient.is_unset(request.src_uid):
            query['srcUid'] = request.src_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDdosDefenseInfo',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeDdosDefenseInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ddos_defense_info(
        self,
        request: jarvis_20180206_models.DescribeDdosDefenseInfoRequest,
    ) -> jarvis_20180206_models.DescribeDdosDefenseInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_defense_info_with_options(request, runtime)

    async def describe_ddos_defense_info_async(
        self,
        request: jarvis_20180206_models.DescribeDdosDefenseInfoRequest,
    ) -> jarvis_20180206_models.DescribeDdosDefenseInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_defense_info_with_options_async(request, runtime)

    def describe_ecs_list_page_with_options(
        self,
        request: jarvis_20180206_models.DescribeEcsListPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeEcsListPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEcsListPage',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeEcsListPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ecs_list_page_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeEcsListPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeEcsListPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEcsListPage',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeEcsListPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ecs_list_page(
        self,
        request: jarvis_20180206_models.DescribeEcsListPageRequest,
    ) -> jarvis_20180206_models.DescribeEcsListPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ecs_list_page_with_options(request, runtime)

    async def describe_ecs_list_page_async(
        self,
        request: jarvis_20180206_models.DescribeEcsListPageRequest,
    ) -> jarvis_20180206_models.DescribeEcsListPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ecs_list_page_with_options_async(request, runtime)

    def describe_ip_white_baseline_with_options(
        self,
        request: jarvis_20180206_models.DescribeIpWhiteBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeIpWhiteBaselineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIp'] = request.src_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpWhiteBaseline',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeIpWhiteBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ip_white_baseline_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeIpWhiteBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeIpWhiteBaselineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIp'] = request.src_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpWhiteBaseline',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeIpWhiteBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ip_white_baseline(
        self,
        request: jarvis_20180206_models.DescribeIpWhiteBaselineRequest,
    ) -> jarvis_20180206_models.DescribeIpWhiteBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_white_baseline_with_options(request, runtime)

    async def describe_ip_white_baseline_async(
        self,
        request: jarvis_20180206_models.DescribeIpWhiteBaselineRequest,
    ) -> jarvis_20180206_models.DescribeIpWhiteBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ip_white_baseline_with_options_async(request, runtime)

    def describe_mining_pre_apply_with_options(
        self,
        request: jarvis_20180206_models.DescribeMiningPreApplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeMiningPreApplyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_type):
            query['FileType'] = request.file_type
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMiningPreApply',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeMiningPreApplyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mining_pre_apply_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeMiningPreApplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeMiningPreApplyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_type):
            query['FileType'] = request.file_type
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMiningPreApply',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeMiningPreApplyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mining_pre_apply(
        self,
        request: jarvis_20180206_models.DescribeMiningPreApplyRequest,
    ) -> jarvis_20180206_models.DescribeMiningPreApplyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_mining_pre_apply_with_options(request, runtime)

    async def describe_mining_pre_apply_async(
        self,
        request: jarvis_20180206_models.DescribeMiningPreApplyRequest,
    ) -> jarvis_20180206_models.DescribeMiningPreApplyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_mining_pre_apply_with_options_async(request, runtime)

    def describe_mining_records_with_options(
        self,
        request: jarvis_20180206_models.DescribeMiningRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeMiningRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMiningRecords',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeMiningRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mining_records_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeMiningRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeMiningRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMiningRecords',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeMiningRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mining_records(
        self,
        request: jarvis_20180206_models.DescribeMiningRecordsRequest,
    ) -> jarvis_20180206_models.DescribeMiningRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_mining_records_with_options(request, runtime)

    async def describe_mining_records_async(
        self,
        request: jarvis_20180206_models.DescribeMiningRecordsRequest,
    ) -> jarvis_20180206_models.DescribeMiningRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_mining_records_with_options_async(request, runtime)

    def describe_mining_rejected_reason_with_options(
        self,
        request: jarvis_20180206_models.DescribeMiningRejectedReasonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeMiningRejectedReasonResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMiningRejectedReason',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeMiningRejectedReasonResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mining_rejected_reason_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeMiningRejectedReasonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeMiningRejectedReasonResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMiningRejectedReason',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeMiningRejectedReasonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mining_rejected_reason(
        self,
        request: jarvis_20180206_models.DescribeMiningRejectedReasonRequest,
    ) -> jarvis_20180206_models.DescribeMiningRejectedReasonResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_mining_rejected_reason_with_options(request, runtime)

    async def describe_mining_rejected_reason_async(
        self,
        request: jarvis_20180206_models.DescribeMiningRejectedReasonRequest,
    ) -> jarvis_20180206_models.DescribeMiningRejectedReasonResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_mining_rejected_reason_with_options_async(request, runtime)

    def describe_mining_report_content_with_options(
        self,
        request: jarvis_20180206_models.DescribeMiningReportContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeMiningReportContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMiningReportContent',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeMiningReportContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mining_report_content_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeMiningReportContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeMiningReportContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMiningReportContent',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeMiningReportContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mining_report_content(
        self,
        request: jarvis_20180206_models.DescribeMiningReportContentRequest,
    ) -> jarvis_20180206_models.DescribeMiningReportContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_mining_report_content_with_options(request, runtime)

    async def describe_mining_report_content_async(
        self,
        request: jarvis_20180206_models.DescribeMiningReportContentRequest,
    ) -> jarvis_20180206_models.DescribeMiningReportContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_mining_report_content_with_options_async(request, runtime)

    def describe_mining_report_file_with_options(
        self,
        request: jarvis_20180206_models.DescribeMiningReportFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeMiningReportFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMiningReportFile',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeMiningReportFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mining_report_file_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeMiningReportFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeMiningReportFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMiningReportFile',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeMiningReportFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mining_report_file(
        self,
        request: jarvis_20180206_models.DescribeMiningReportFileRequest,
    ) -> jarvis_20180206_models.DescribeMiningReportFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_mining_report_file_with_options(request, runtime)

    async def describe_mining_report_file_async(
        self,
        request: jarvis_20180206_models.DescribeMiningReportFileRequest,
    ) -> jarvis_20180206_models.DescribeMiningReportFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_mining_report_file_with_options_async(request, runtime)

    def describe_phone_info_with_options(
        self,
        request: jarvis_20180206_models.DescribePhoneInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribePhoneInfoResponse:
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
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribePhoneInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_phone_info_with_options_async(
        self,
        request: jarvis_20180206_models.DescribePhoneInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribePhoneInfoResponse:
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
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribePhoneInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_phone_info(
        self,
        request: jarvis_20180206_models.DescribePhoneInfoRequest,
    ) -> jarvis_20180206_models.DescribePhoneInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_phone_info_with_options(request, runtime)

    async def describe_phone_info_async(
        self,
        request: jarvis_20180206_models.DescribePhoneInfoRequest,
    ) -> jarvis_20180206_models.DescribePhoneInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_phone_info_with_options_async(request, runtime)

    def describe_punish_list_with_options(
        self,
        request: jarvis_20180206_models.DescribePunishListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribePunishListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.punish_status):
            query['PunishStatus'] = request.punish_status
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_code):
            query['sourceCode'] = request.source_code
        if not UtilClient.is_unset(request.src_uid):
            query['srcUid'] = request.src_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePunishList',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribePunishListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_punish_list_with_options_async(
        self,
        request: jarvis_20180206_models.DescribePunishListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribePunishListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.punish_status):
            query['PunishStatus'] = request.punish_status
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_code):
            query['sourceCode'] = request.source_code
        if not UtilClient.is_unset(request.src_uid):
            query['srcUid'] = request.src_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePunishList',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribePunishListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_punish_list(
        self,
        request: jarvis_20180206_models.DescribePunishListRequest,
    ) -> jarvis_20180206_models.DescribePunishListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_punish_list_with_options(request, runtime)

    async def describe_punish_list_async(
        self,
        request: jarvis_20180206_models.DescribePunishListRequest,
    ) -> jarvis_20180206_models.DescribePunishListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_punish_list_with_options_async(request, runtime)

    def describe_reset_record_list_with_options(
        self,
        request: jarvis_20180206_models.DescribeResetRecordListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeResetRecordListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResetRecordList',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeResetRecordListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_reset_record_list_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeResetRecordListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeResetRecordListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResetRecordList',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeResetRecordListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_reset_record_list(
        self,
        request: jarvis_20180206_models.DescribeResetRecordListRequest,
    ) -> jarvis_20180206_models.DescribeResetRecordListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_reset_record_list_with_options(request, runtime)

    async def describe_reset_record_list_async(
        self,
        request: jarvis_20180206_models.DescribeResetRecordListRequest,
    ) -> jarvis_20180206_models.DescribeResetRecordListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_reset_record_list_with_options_async(request, runtime)

    def describe_reset_record_query_count_with_options(
        self,
        request: jarvis_20180206_models.DescribeResetRecordQueryCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeResetRecordQueryCountResponse:
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
            action='DescribeResetRecordQueryCount',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeResetRecordQueryCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_reset_record_query_count_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeResetRecordQueryCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeResetRecordQueryCountResponse:
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
            action='DescribeResetRecordQueryCount',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeResetRecordQueryCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_reset_record_query_count(
        self,
        request: jarvis_20180206_models.DescribeResetRecordQueryCountRequest,
    ) -> jarvis_20180206_models.DescribeResetRecordQueryCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_reset_record_query_count_with_options(request, runtime)

    async def describe_reset_record_query_count_async(
        self,
        request: jarvis_20180206_models.DescribeResetRecordQueryCountRequest,
    ) -> jarvis_20180206_models.DescribeResetRecordQueryCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_reset_record_query_count_with_options_async(request, runtime)

    def describe_risk_list_detail_with_options(
        self,
        request: jarvis_20180206_models.DescribeRiskListDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeRiskListDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_product):
            query['queryProduct'] = request.query_product
        if not UtilClient.is_unset(request.query_region_id):
            query['queryRegionId'] = request.query_region_id
        if not UtilClient.is_unset(request.risk_describe):
            query['riskDescribe'] = request.risk_describe
        if not UtilClient.is_unset(request.risk_type):
            query['riskType'] = request.risk_type
        if not UtilClient.is_unset(request.source_code):
            query['sourceCode'] = request.source_code
        if not UtilClient.is_unset(request.src_uid):
            query['srcUid'] = request.src_uid
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskListDetail',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeRiskListDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_list_detail_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeRiskListDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeRiskListDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_product):
            query['queryProduct'] = request.query_product
        if not UtilClient.is_unset(request.query_region_id):
            query['queryRegionId'] = request.query_region_id
        if not UtilClient.is_unset(request.risk_describe):
            query['riskDescribe'] = request.risk_describe
        if not UtilClient.is_unset(request.risk_type):
            query['riskType'] = request.risk_type
        if not UtilClient.is_unset(request.source_code):
            query['sourceCode'] = request.source_code
        if not UtilClient.is_unset(request.src_uid):
            query['srcUid'] = request.src_uid
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskListDetail',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeRiskListDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_list_detail(
        self,
        request: jarvis_20180206_models.DescribeRiskListDetailRequest,
    ) -> jarvis_20180206_models.DescribeRiskListDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_list_detail_with_options(request, runtime)

    async def describe_risk_list_detail_async(
        self,
        request: jarvis_20180206_models.DescribeRiskListDetailRequest,
    ) -> jarvis_20180206_models.DescribeRiskListDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_risk_list_detail_with_options_async(request, runtime)

    def describe_risk_trend_with_options(
        self,
        request: jarvis_20180206_models.DescribeRiskTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeRiskTrendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.peroid):
            query['Peroid'] = request.peroid
        if not UtilClient.is_unset(request.query_product):
            query['QueryProduct'] = request.query_product
        if not UtilClient.is_unset(request.query_region_id):
            query['QueryRegionId'] = request.query_region_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskTrend',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeRiskTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_trend_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeRiskTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeRiskTrendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.peroid):
            query['Peroid'] = request.peroid
        if not UtilClient.is_unset(request.query_product):
            query['QueryProduct'] = request.query_product
        if not UtilClient.is_unset(request.query_region_id):
            query['QueryRegionId'] = request.query_region_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskTrend',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeRiskTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_trend(
        self,
        request: jarvis_20180206_models.DescribeRiskTrendRequest,
    ) -> jarvis_20180206_models.DescribeRiskTrendResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_trend_with_options(request, runtime)

    async def describe_risk_trend_async(
        self,
        request: jarvis_20180206_models.DescribeRiskTrendRequest,
    ) -> jarvis_20180206_models.DescribeRiskTrendResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_risk_trend_with_options_async(request, runtime)

    def describe_special_ecs_with_options(
        self,
        request: jarvis_20180206_models.DescribeSpecialEcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeSpecialEcsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.target_ip):
            query['TargetIp'] = request.target_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSpecialEcs',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeSpecialEcsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_special_ecs_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeSpecialEcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeSpecialEcsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.target_ip):
            query['TargetIp'] = request.target_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSpecialEcs',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeSpecialEcsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_special_ecs(
        self,
        request: jarvis_20180206_models.DescribeSpecialEcsRequest,
    ) -> jarvis_20180206_models.DescribeSpecialEcsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_special_ecs_with_options(request, runtime)

    async def describe_special_ecs_async(
        self,
        request: jarvis_20180206_models.DescribeSpecialEcsRequest,
    ) -> jarvis_20180206_models.DescribeSpecialEcsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_special_ecs_with_options_async(request, runtime)

    def describe_uid_gc_level_with_options(
        self,
        request: jarvis_20180206_models.DescribeUidGcLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeUidGcLevelResponse:
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
            action='DescribeUidGcLevel',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeUidGcLevelResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_uid_gc_level_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeUidGcLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeUidGcLevelResponse:
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
            action='DescribeUidGcLevel',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeUidGcLevelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_uid_gc_level(
        self,
        request: jarvis_20180206_models.DescribeUidGcLevelRequest,
    ) -> jarvis_20180206_models.DescribeUidGcLevelResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_uid_gc_level_with_options(request, runtime)

    async def describe_uid_gc_level_async(
        self,
        request: jarvis_20180206_models.DescribeUidGcLevelRequest,
    ) -> jarvis_20180206_models.DescribeUidGcLevelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_uid_gc_level_with_options_async(request, runtime)

    def describe_uid_white_baseline_with_options(
        self,
        request: jarvis_20180206_models.DescribeUidWhiteBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeUidWhiteBaselineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_uid):
            query['SrcUid'] = request.src_uid
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUidWhiteBaseline',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeUidWhiteBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_uid_white_baseline_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeUidWhiteBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeUidWhiteBaselineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_uid):
            query['SrcUid'] = request.src_uid
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUidWhiteBaseline',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeUidWhiteBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_uid_white_baseline(
        self,
        request: jarvis_20180206_models.DescribeUidWhiteBaselineRequest,
    ) -> jarvis_20180206_models.DescribeUidWhiteBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_uid_white_baseline_with_options(request, runtime)

    async def describe_uid_white_baseline_async(
        self,
        request: jarvis_20180206_models.DescribeUidWhiteBaselineRequest,
    ) -> jarvis_20180206_models.DescribeUidWhiteBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_uid_white_baseline_with_options_async(request, runtime)

    def describe_uid_white_list_group_with_options(
        self,
        request: jarvis_20180206_models.DescribeUidWhiteListGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeUidWhiteListGroupResponse:
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
        if not UtilClient.is_unset(request.src_uid):
            query['SrcUid'] = request.src_uid
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.white_list_type):
            query['WhiteListType'] = request.white_list_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUidWhiteListGroup',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeUidWhiteListGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_uid_white_list_group_with_options_async(
        self,
        request: jarvis_20180206_models.DescribeUidWhiteListGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.DescribeUidWhiteListGroupResponse:
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
        if not UtilClient.is_unset(request.src_uid):
            query['SrcUid'] = request.src_uid
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.white_list_type):
            query['WhiteListType'] = request.white_list_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUidWhiteListGroup',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.DescribeUidWhiteListGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_uid_white_list_group(
        self,
        request: jarvis_20180206_models.DescribeUidWhiteListGroupRequest,
    ) -> jarvis_20180206_models.DescribeUidWhiteListGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_uid_white_list_group_with_options(request, runtime)

    async def describe_uid_white_list_group_async(
        self,
        request: jarvis_20180206_models.DescribeUidWhiteListGroupRequest,
    ) -> jarvis_20180206_models.DescribeUidWhiteListGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_uid_white_list_group_with_options_async(request, runtime)

    def modify_access_white_list_auto_share_with_options(
        self,
        request: jarvis_20180206_models.ModifyAccessWhiteListAutoShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.ModifyAccessWhiteListAutoShareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_config):
            query['AutoConfig'] = request.auto_config
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
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
            action='ModifyAccessWhiteListAutoShare',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.ModifyAccessWhiteListAutoShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_access_white_list_auto_share_with_options_async(
        self,
        request: jarvis_20180206_models.ModifyAccessWhiteListAutoShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.ModifyAccessWhiteListAutoShareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_config):
            query['AutoConfig'] = request.auto_config
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
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
            action='ModifyAccessWhiteListAutoShare',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.ModifyAccessWhiteListAutoShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_access_white_list_auto_share(
        self,
        request: jarvis_20180206_models.ModifyAccessWhiteListAutoShareRequest,
    ) -> jarvis_20180206_models.ModifyAccessWhiteListAutoShareResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_access_white_list_auto_share_with_options(request, runtime)

    async def modify_access_white_list_auto_share_async(
        self,
        request: jarvis_20180206_models.ModifyAccessWhiteListAutoShareRequest,
    ) -> jarvis_20180206_models.ModifyAccessWhiteListAutoShareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_access_white_list_auto_share_with_options_async(request, runtime)

    def modify_ip_white_baseline_with_options(
        self,
        request: jarvis_20180206_models.ModifyIpWhiteBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.ModifyIpWhiteBaselineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIp'] = request.src_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyIpWhiteBaseline',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.ModifyIpWhiteBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ip_white_baseline_with_options_async(
        self,
        request: jarvis_20180206_models.ModifyIpWhiteBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.ModifyIpWhiteBaselineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIp'] = request.src_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyIpWhiteBaseline',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.ModifyIpWhiteBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_ip_white_baseline(
        self,
        request: jarvis_20180206_models.ModifyIpWhiteBaselineRequest,
    ) -> jarvis_20180206_models.ModifyIpWhiteBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ip_white_baseline_with_options(request, runtime)

    async def modify_ip_white_baseline_async(
        self,
        request: jarvis_20180206_models.ModifyIpWhiteBaselineRequest,
    ) -> jarvis_20180206_models.ModifyIpWhiteBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ip_white_baseline_with_options_async(request, runtime)

    def modify_uid_white_baseline_with_options(
        self,
        request: jarvis_20180206_models.ModifyUidWhiteBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.ModifyUidWhiteBaselineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_uid):
            query['SrcUid'] = request.src_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUidWhiteBaseline',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.ModifyUidWhiteBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_uid_white_baseline_with_options_async(
        self,
        request: jarvis_20180206_models.ModifyUidWhiteBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.ModifyUidWhiteBaselineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_uid):
            query['SrcUid'] = request.src_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUidWhiteBaseline',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.ModifyUidWhiteBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_uid_white_baseline(
        self,
        request: jarvis_20180206_models.ModifyUidWhiteBaselineRequest,
    ) -> jarvis_20180206_models.ModifyUidWhiteBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_uid_white_baseline_with_options(request, runtime)

    async def modify_uid_white_baseline_async(
        self,
        request: jarvis_20180206_models.ModifyUidWhiteBaselineRequest,
    ) -> jarvis_20180206_models.ModifyUidWhiteBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_uid_white_baseline_with_options_async(request, runtime)

    def modify_uid_white_list_auto_share_with_options(
        self,
        request: jarvis_20180206_models.ModifyUidWhiteListAutoShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.ModifyUidWhiteListAutoShareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_config):
            query['AutoConfig'] = request.auto_config
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_uid):
            query['SrcUid'] = request.src_uid
        if not UtilClient.is_unset(request.white_list_type):
            query['WhiteListType'] = request.white_list_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUidWhiteListAutoShare',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.ModifyUidWhiteListAutoShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_uid_white_list_auto_share_with_options_async(
        self,
        request: jarvis_20180206_models.ModifyUidWhiteListAutoShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> jarvis_20180206_models.ModifyUidWhiteListAutoShareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_config):
            query['AutoConfig'] = request.auto_config
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_uid):
            query['SrcUid'] = request.src_uid
        if not UtilClient.is_unset(request.white_list_type):
            query['WhiteListType'] = request.white_list_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUidWhiteListAutoShare',
            version='2018-02-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            jarvis_20180206_models.ModifyUidWhiteListAutoShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_uid_white_list_auto_share(
        self,
        request: jarvis_20180206_models.ModifyUidWhiteListAutoShareRequest,
    ) -> jarvis_20180206_models.ModifyUidWhiteListAutoShareResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_uid_white_list_auto_share_with_options(request, runtime)

    async def modify_uid_white_list_auto_share_async(
        self,
        request: jarvis_20180206_models.ModifyUidWhiteListAutoShareRequest,
    ) -> jarvis_20180206_models.ModifyUidWhiteListAutoShareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_uid_white_list_auto_share_with_options_async(request, runtime)
