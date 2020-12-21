# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore
from typing import Dict

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_tea_rpc import models as rpc_models
from alibabacloud_ddosbgp20180720 import models as ddosbgp_20180720_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(
        self, 
        config: rpc_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'ddosbgp.aliyuncs.com',
            'cn-beijing': 'ddosbgp.aliyuncs.com',
            'cn-zhangjiakou': 'ddosbgp.aliyuncs.com',
            'cn-huhehaote': 'ddosbgp.aliyuncs.com',
            'cn-hangzhou': 'ddosbgp.aliyuncs.com',
            'cn-shanghai': 'ddosbgp.aliyuncs.com',
            'cn-shenzhen': 'ddosbgp.aliyuncs.com',
            'ap-northeast-1': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'cn-chengdu': 'ddosbgp.aliyuncs.com',
            'eu-central-1': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'cn-hangzhou-finance': 'ddosbgp.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ddosbgp.aliyuncs.com',
            'cn-shanghai-finance-1': 'ddosbgp.aliyuncs.com',
            'cn-north-2-gov-1': 'ddosbgp.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ddosbgp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def describe_on_demand_instance_status_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeOnDemandInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeOnDemandInstanceStatusResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeOnDemandInstanceStatusResponse().from_map(
            self.do_request('DescribeOnDemandInstanceStatus', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_on_demand_instance_status_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeOnDemandInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeOnDemandInstanceStatusResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeOnDemandInstanceStatusResponse().from_map(
            await self.do_request_async('DescribeOnDemandInstanceStatus', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_on_demand_instance_status(
        self,
        request: ddosbgp_20180720_models.DescribeOnDemandInstanceStatusRequest,
    ) -> ddosbgp_20180720_models.DescribeOnDemandInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_on_demand_instance_status_with_options(request, runtime)

    async def describe_on_demand_instance_status_async(
        self,
        request: ddosbgp_20180720_models.DescribeOnDemandInstanceStatusRequest,
    ) -> ddosbgp_20180720_models.DescribeOnDemandInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_on_demand_instance_status_with_options_async(request, runtime)

    def set_instance_mode_on_demand_with_options(
        self,
        request: ddosbgp_20180720_models.SetInstanceModeOnDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.SetInstanceModeOnDemandResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.SetInstanceModeOnDemandResponse().from_map(
            self.do_request('SetInstanceModeOnDemand', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_instance_mode_on_demand_with_options_async(
        self,
        request: ddosbgp_20180720_models.SetInstanceModeOnDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.SetInstanceModeOnDemandResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.SetInstanceModeOnDemandResponse().from_map(
            await self.do_request_async('SetInstanceModeOnDemand', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_instance_mode_on_demand(
        self,
        request: ddosbgp_20180720_models.SetInstanceModeOnDemandRequest,
    ) -> ddosbgp_20180720_models.SetInstanceModeOnDemandResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_instance_mode_on_demand_with_options(request, runtime)

    async def set_instance_mode_on_demand_async(
        self,
        request: ddosbgp_20180720_models.SetInstanceModeOnDemandRequest,
    ) -> ddosbgp_20180720_models.SetInstanceModeOnDemandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_instance_mode_on_demand_with_options_async(request, runtime)

    def query_schedrule_on_demand_with_options(
        self,
        request: ddosbgp_20180720_models.QuerySchedruleOnDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.QuerySchedruleOnDemandResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.QuerySchedruleOnDemandResponse().from_map(
            self.do_request('QuerySchedruleOnDemand', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_schedrule_on_demand_with_options_async(
        self,
        request: ddosbgp_20180720_models.QuerySchedruleOnDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.QuerySchedruleOnDemandResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.QuerySchedruleOnDemandResponse().from_map(
            await self.do_request_async('QuerySchedruleOnDemand', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_schedrule_on_demand(
        self,
        request: ddosbgp_20180720_models.QuerySchedruleOnDemandRequest,
    ) -> ddosbgp_20180720_models.QuerySchedruleOnDemandResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_schedrule_on_demand_with_options(request, runtime)

    async def query_schedrule_on_demand_async(
        self,
        request: ddosbgp_20180720_models.QuerySchedruleOnDemandRequest,
    ) -> ddosbgp_20180720_models.QuerySchedruleOnDemandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_schedrule_on_demand_with_options_async(request, runtime)

    def delete_schedrule_on_demand_with_options(
        self,
        request: ddosbgp_20180720_models.DeleteSchedruleOnDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DeleteSchedruleOnDemandResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DeleteSchedruleOnDemandResponse().from_map(
            self.do_request('DeleteSchedruleOnDemand', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_schedrule_on_demand_with_options_async(
        self,
        request: ddosbgp_20180720_models.DeleteSchedruleOnDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DeleteSchedruleOnDemandResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DeleteSchedruleOnDemandResponse().from_map(
            await self.do_request_async('DeleteSchedruleOnDemand', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_schedrule_on_demand(
        self,
        request: ddosbgp_20180720_models.DeleteSchedruleOnDemandRequest,
    ) -> ddosbgp_20180720_models.DeleteSchedruleOnDemandResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_schedrule_on_demand_with_options(request, runtime)

    async def delete_schedrule_on_demand_async(
        self,
        request: ddosbgp_20180720_models.DeleteSchedruleOnDemandRequest,
    ) -> ddosbgp_20180720_models.DeleteSchedruleOnDemandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_schedrule_on_demand_with_options_async(request, runtime)

    def config_schedrule_on_demand_with_options(
        self,
        request: ddosbgp_20180720_models.ConfigSchedruleOnDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ConfigSchedruleOnDemandResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.ConfigSchedruleOnDemandResponse().from_map(
            self.do_request('ConfigSchedruleOnDemand', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def config_schedrule_on_demand_with_options_async(
        self,
        request: ddosbgp_20180720_models.ConfigSchedruleOnDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ConfigSchedruleOnDemandResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.ConfigSchedruleOnDemandResponse().from_map(
            await self.do_request_async('ConfigSchedruleOnDemand', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def config_schedrule_on_demand(
        self,
        request: ddosbgp_20180720_models.ConfigSchedruleOnDemandRequest,
    ) -> ddosbgp_20180720_models.ConfigSchedruleOnDemandResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_schedrule_on_demand_with_options(request, runtime)

    async def config_schedrule_on_demand_async(
        self,
        request: ddosbgp_20180720_models.ConfigSchedruleOnDemandRequest,
    ) -> ddosbgp_20180720_models.ConfigSchedruleOnDemandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_schedrule_on_demand_with_options_async(request, runtime)

    def create_schedrule_on_demand_with_options(
        self,
        request: ddosbgp_20180720_models.CreateSchedruleOnDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.CreateSchedruleOnDemandResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.CreateSchedruleOnDemandResponse().from_map(
            self.do_request('CreateSchedruleOnDemand', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_schedrule_on_demand_with_options_async(
        self,
        request: ddosbgp_20180720_models.CreateSchedruleOnDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.CreateSchedruleOnDemandResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.CreateSchedruleOnDemandResponse().from_map(
            await self.do_request_async('CreateSchedruleOnDemand', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_schedrule_on_demand(
        self,
        request: ddosbgp_20180720_models.CreateSchedruleOnDemandRequest,
    ) -> ddosbgp_20180720_models.CreateSchedruleOnDemandResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_schedrule_on_demand_with_options(request, runtime)

    async def create_schedrule_on_demand_async(
        self,
        request: ddosbgp_20180720_models.CreateSchedruleOnDemandRequest,
    ) -> ddosbgp_20180720_models.CreateSchedruleOnDemandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_schedrule_on_demand_with_options_async(request, runtime)

    def describe_on_demand_ddos_event_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeOnDemandDdosEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeOnDemandDdosEventResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeOnDemandDdosEventResponse().from_map(
            self.do_request('DescribeOnDemandDdosEvent', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_on_demand_ddos_event_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeOnDemandDdosEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeOnDemandDdosEventResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeOnDemandDdosEventResponse().from_map(
            await self.do_request_async('DescribeOnDemandDdosEvent', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_on_demand_ddos_event(
        self,
        request: ddosbgp_20180720_models.DescribeOnDemandDdosEventRequest,
    ) -> ddosbgp_20180720_models.DescribeOnDemandDdosEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_on_demand_ddos_event_with_options(request, runtime)

    async def describe_on_demand_ddos_event_async(
        self,
        request: ddosbgp_20180720_models.DescribeOnDemandDdosEventRequest,
    ) -> ddosbgp_20180720_models.DescribeOnDemandDdosEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_on_demand_ddos_event_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: ddosbgp_20180720_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.ListTagKeysResponse().from_map(
            self.do_request('ListTagKeys', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: ddosbgp_20180720_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.ListTagKeysResponse().from_map(
            await self.do_request_async('ListTagKeys', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_tag_keys(
        self,
        request: ddosbgp_20180720_models.ListTagKeysRequest,
    ) -> ddosbgp_20180720_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: ddosbgp_20180720_models.ListTagKeysRequest,
    ) -> ddosbgp_20180720_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: ddosbgp_20180720_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.ListTagResourcesResponse().from_map(
            self.do_request('ListTagResources', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: ddosbgp_20180720_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.ListTagResourcesResponse().from_map(
            await self.do_request_async('ListTagResources', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_tag_resources(
        self,
        request: ddosbgp_20180720_models.ListTagResourcesRequest,
    ) -> ddosbgp_20180720_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ddosbgp_20180720_models.ListTagResourcesRequest,
    ) -> ddosbgp_20180720_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: ddosbgp_20180720_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.UntagResourcesResponse().from_map(
            self.do_request('UntagResources', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: ddosbgp_20180720_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.UntagResourcesResponse().from_map(
            await self.do_request_async('UntagResources', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def untag_resources(
        self,
        request: ddosbgp_20180720_models.UntagResourcesRequest,
    ) -> ddosbgp_20180720_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: ddosbgp_20180720_models.UntagResourcesRequest,
    ) -> ddosbgp_20180720_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: ddosbgp_20180720_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.TagResourcesResponse().from_map(
            self.do_request('TagResources', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ddosbgp_20180720_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.TagResourcesResponse().from_map(
            await self.do_request_async('TagResources', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def tag_resources(
        self,
        request: ddosbgp_20180720_models.TagResourcesRequest,
    ) -> ddosbgp_20180720_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ddosbgp_20180720_models.TagResourcesRequest,
    ) -> ddosbgp_20180720_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def describe_excpetion_count_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeExcpetionCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeExcpetionCountResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeExcpetionCountResponse().from_map(
            self.do_request('DescribeExcpetionCount', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_excpetion_count_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeExcpetionCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeExcpetionCountResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeExcpetionCountResponse().from_map(
            await self.do_request_async('DescribeExcpetionCount', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_excpetion_count(
        self,
        request: ddosbgp_20180720_models.DescribeExcpetionCountRequest,
    ) -> ddosbgp_20180720_models.DescribeExcpetionCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_excpetion_count_with_options(request, runtime)

    async def describe_excpetion_count_async(
        self,
        request: ddosbgp_20180720_models.DescribeExcpetionCountRequest,
    ) -> ddosbgp_20180720_models.DescribeExcpetionCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_excpetion_count_with_options_async(request, runtime)

    def describe_pack_ip_list_with_options(
        self,
        request: ddosbgp_20180720_models.DescribePackIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribePackIpListResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribePackIpListResponse().from_map(
            self.do_request('DescribePackIpList', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_pack_ip_list_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribePackIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribePackIpListResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribePackIpListResponse().from_map(
            await self.do_request_async('DescribePackIpList', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_pack_ip_list(
        self,
        request: ddosbgp_20180720_models.DescribePackIpListRequest,
    ) -> ddosbgp_20180720_models.DescribePackIpListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pack_ip_list_with_options(request, runtime)

    async def describe_pack_ip_list_async(
        self,
        request: ddosbgp_20180720_models.DescribePackIpListRequest,
    ) -> ddosbgp_20180720_models.DescribePackIpListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pack_ip_list_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeRegionsResponse().from_map(
            self.do_request('DescribeRegions', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeRegionsResponse().from_map(
            await self.do_request_async('DescribeRegions', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_regions(
        self,
        request: ddosbgp_20180720_models.DescribeRegionsRequest,
    ) -> ddosbgp_20180720_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: ddosbgp_20180720_models.DescribeRegionsRequest,
    ) -> ddosbgp_20180720_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def modify_remark_with_options(
        self,
        request: ddosbgp_20180720_models.ModifyRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ModifyRemarkResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.ModifyRemarkResponse().from_map(
            self.do_request('ModifyRemark', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def modify_remark_with_options_async(
        self,
        request: ddosbgp_20180720_models.ModifyRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ModifyRemarkResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.ModifyRemarkResponse().from_map(
            await self.do_request_async('ModifyRemark', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def modify_remark(
        self,
        request: ddosbgp_20180720_models.ModifyRemarkRequest,
    ) -> ddosbgp_20180720_models.ModifyRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_remark_with_options(request, runtime)

    async def modify_remark_async(
        self,
        request: ddosbgp_20180720_models.ModifyRemarkRequest,
    ) -> ddosbgp_20180720_models.ModifyRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_remark_with_options_async(request, runtime)

    def describe_traffic_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeTrafficResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeTrafficResponse().from_map(
            self.do_request('DescribeTraffic', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_traffic_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeTrafficResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeTrafficResponse().from_map(
            await self.do_request_async('DescribeTraffic', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_traffic(
        self,
        request: ddosbgp_20180720_models.DescribeTrafficRequest,
    ) -> ddosbgp_20180720_models.DescribeTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_traffic_with_options(request, runtime)

    async def describe_traffic_async(
        self,
        request: ddosbgp_20180720_models.DescribeTrafficRequest,
    ) -> ddosbgp_20180720_models.DescribeTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_traffic_with_options_async(request, runtime)

    def describe_resource_pack_usage_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeResourcePackUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeResourcePackUsageResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeResourcePackUsageResponse().from_map(
            self.do_request('DescribeResourcePackUsage', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_resource_pack_usage_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeResourcePackUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeResourcePackUsageResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeResourcePackUsageResponse().from_map(
            await self.do_request_async('DescribeResourcePackUsage', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_resource_pack_usage(
        self,
        request: ddosbgp_20180720_models.DescribeResourcePackUsageRequest,
    ) -> ddosbgp_20180720_models.DescribeResourcePackUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_pack_usage_with_options(request, runtime)

    async def describe_resource_pack_usage_async(
        self,
        request: ddosbgp_20180720_models.DescribeResourcePackUsageRequest,
    ) -> ddosbgp_20180720_models.DescribeResourcePackUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_pack_usage_with_options_async(request, runtime)

    def describe_resource_pack_statistics_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeResourcePackStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeResourcePackStatisticsResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeResourcePackStatisticsResponse().from_map(
            self.do_request('DescribeResourcePackStatistics', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_resource_pack_statistics_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeResourcePackStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeResourcePackStatisticsResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeResourcePackStatisticsResponse().from_map(
            await self.do_request_async('DescribeResourcePackStatistics', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_resource_pack_statistics(
        self,
        request: ddosbgp_20180720_models.DescribeResourcePackStatisticsRequest,
    ) -> ddosbgp_20180720_models.DescribeResourcePackStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_pack_statistics_with_options(request, runtime)

    async def describe_resource_pack_statistics_async(
        self,
        request: ddosbgp_20180720_models.DescribeResourcePackStatisticsRequest,
    ) -> ddosbgp_20180720_models.DescribeResourcePackStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_pack_statistics_with_options_async(request, runtime)

    def describe_resource_pack_instances_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeResourcePackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeResourcePackInstancesResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeResourcePackInstancesResponse().from_map(
            self.do_request('DescribeResourcePackInstances', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_resource_pack_instances_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeResourcePackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeResourcePackInstancesResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeResourcePackInstancesResponse().from_map(
            await self.do_request_async('DescribeResourcePackInstances', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_resource_pack_instances(
        self,
        request: ddosbgp_20180720_models.DescribeResourcePackInstancesRequest,
    ) -> ddosbgp_20180720_models.DescribeResourcePackInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_pack_instances_with_options(request, runtime)

    async def describe_resource_pack_instances_async(
        self,
        request: ddosbgp_20180720_models.DescribeResourcePackInstancesRequest,
    ) -> ddosbgp_20180720_models.DescribeResourcePackInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_pack_instances_with_options_async(request, runtime)

    def describe_pack_paid_traffic_with_options(
        self,
        request: ddosbgp_20180720_models.DescribePackPaidTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribePackPaidTrafficResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribePackPaidTrafficResponse().from_map(
            self.do_request('DescribePackPaidTraffic', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_pack_paid_traffic_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribePackPaidTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribePackPaidTrafficResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribePackPaidTrafficResponse().from_map(
            await self.do_request_async('DescribePackPaidTraffic', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_pack_paid_traffic(
        self,
        request: ddosbgp_20180720_models.DescribePackPaidTrafficRequest,
    ) -> ddosbgp_20180720_models.DescribePackPaidTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pack_paid_traffic_with_options(request, runtime)

    async def describe_pack_paid_traffic_async(
        self,
        request: ddosbgp_20180720_models.DescribePackPaidTrafficRequest,
    ) -> ddosbgp_20180720_models.DescribePackPaidTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pack_paid_traffic_with_options_async(request, runtime)

    def describe_op_entities_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeOpEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeOpEntitiesResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeOpEntitiesResponse().from_map(
            self.do_request('DescribeOpEntities', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_op_entities_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeOpEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeOpEntitiesResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeOpEntitiesResponse().from_map(
            await self.do_request_async('DescribeOpEntities', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_op_entities(
        self,
        request: ddosbgp_20180720_models.DescribeOpEntitiesRequest,
    ) -> ddosbgp_20180720_models.DescribeOpEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_op_entities_with_options(request, runtime)

    async def describe_op_entities_async(
        self,
        request: ddosbgp_20180720_models.DescribeOpEntitiesRequest,
    ) -> ddosbgp_20180720_models.DescribeOpEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_op_entities_with_options_async(request, runtime)

    def describe_instance_specs_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeInstanceSpecsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeInstanceSpecsResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeInstanceSpecsResponse().from_map(
            self.do_request('DescribeInstanceSpecs', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_instance_specs_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeInstanceSpecsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeInstanceSpecsResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeInstanceSpecsResponse().from_map(
            await self.do_request_async('DescribeInstanceSpecs', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_instance_specs(
        self,
        request: ddosbgp_20180720_models.DescribeInstanceSpecsRequest,
    ) -> ddosbgp_20180720_models.DescribeInstanceSpecsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_specs_with_options(request, runtime)

    async def describe_instance_specs_async(
        self,
        request: ddosbgp_20180720_models.DescribeInstanceSpecsRequest,
    ) -> ddosbgp_20180720_models.DescribeInstanceSpecsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_specs_with_options_async(request, runtime)

    def describe_instance_list_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeInstanceListResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeInstanceListResponse().from_map(
            self.do_request('DescribeInstanceList', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_instance_list_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeInstanceListResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeInstanceListResponse().from_map(
            await self.do_request_async('DescribeInstanceList', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_instance_list(
        self,
        request: ddosbgp_20180720_models.DescribeInstanceListRequest,
    ) -> ddosbgp_20180720_models.DescribeInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_list_with_options(request, runtime)

    async def describe_instance_list_async(
        self,
        request: ddosbgp_20180720_models.DescribeInstanceListRequest,
    ) -> ddosbgp_20180720_models.DescribeInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_list_with_options_async(request, runtime)

    def describe_ddos_event_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeDdosEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeDdosEventResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeDdosEventResponse().from_map(
            self.do_request('DescribeDdosEvent', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_ddos_event_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeDdosEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeDdosEventResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeDdosEventResponse().from_map(
            await self.do_request_async('DescribeDdosEvent', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_ddos_event(
        self,
        request: ddosbgp_20180720_models.DescribeDdosEventRequest,
    ) -> ddosbgp_20180720_models.DescribeDdosEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_with_options(request, runtime)

    async def describe_ddos_event_async(
        self,
        request: ddosbgp_20180720_models.DescribeDdosEventRequest,
    ) -> ddosbgp_20180720_models.DescribeDdosEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_event_with_options_async(request, runtime)

    def delete_ip_with_options(
        self,
        request: ddosbgp_20180720_models.DeleteIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DeleteIpResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DeleteIpResponse().from_map(
            self.do_request('DeleteIp', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_ip_with_options_async(
        self,
        request: ddosbgp_20180720_models.DeleteIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DeleteIpResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DeleteIpResponse().from_map(
            await self.do_request_async('DeleteIp', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_ip(
        self,
        request: ddosbgp_20180720_models.DeleteIpRequest,
    ) -> ddosbgp_20180720_models.DeleteIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ip_with_options(request, runtime)

    async def delete_ip_async(
        self,
        request: ddosbgp_20180720_models.DeleteIpRequest,
    ) -> ddosbgp_20180720_models.DeleteIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ip_with_options_async(request, runtime)

    def delete_blackhole_with_options(
        self,
        request: ddosbgp_20180720_models.DeleteBlackholeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DeleteBlackholeResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DeleteBlackholeResponse().from_map(
            self.do_request('DeleteBlackhole', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_blackhole_with_options_async(
        self,
        request: ddosbgp_20180720_models.DeleteBlackholeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DeleteBlackholeResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DeleteBlackholeResponse().from_map(
            await self.do_request_async('DeleteBlackhole', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_blackhole(
        self,
        request: ddosbgp_20180720_models.DeleteBlackholeRequest,
    ) -> ddosbgp_20180720_models.DeleteBlackholeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_blackhole_with_options(request, runtime)

    async def delete_blackhole_async(
        self,
        request: ddosbgp_20180720_models.DeleteBlackholeRequest,
    ) -> ddosbgp_20180720_models.DeleteBlackholeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_blackhole_with_options_async(request, runtime)

    def check_grant_with_options(
        self,
        request: ddosbgp_20180720_models.CheckGrantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.CheckGrantResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.CheckGrantResponse().from_map(
            self.do_request('CheckGrant', 'HTTPS', 'GET', '2018-07-20', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def check_grant_with_options_async(
        self,
        request: ddosbgp_20180720_models.CheckGrantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.CheckGrantResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.CheckGrantResponse().from_map(
            await self.do_request_async('CheckGrant', 'HTTPS', 'GET', '2018-07-20', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def check_grant(
        self,
        request: ddosbgp_20180720_models.CheckGrantRequest,
    ) -> ddosbgp_20180720_models.CheckGrantResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_grant_with_options(request, runtime)

    async def check_grant_async(
        self,
        request: ddosbgp_20180720_models.CheckGrantRequest,
    ) -> ddosbgp_20180720_models.CheckGrantResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_grant_with_options_async(request, runtime)

    def add_ip_with_options(
        self,
        request: ddosbgp_20180720_models.AddIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.AddIpResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.AddIpResponse().from_map(
            self.do_request('AddIp', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def add_ip_with_options_async(
        self,
        request: ddosbgp_20180720_models.AddIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.AddIpResponse:
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.AddIpResponse().from_map(
            await self.do_request_async('AddIp', 'HTTPS', 'POST', '2018-07-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def add_ip(
        self,
        request: ddosbgp_20180720_models.AddIpRequest,
    ) -> ddosbgp_20180720_models.AddIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_ip_with_options(request, runtime)

    async def add_ip_async(
        self,
        request: ddosbgp_20180720_models.AddIpRequest,
    ) -> ddosbgp_20180720_models.AddIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_ip_with_options_async(request, runtime)

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
