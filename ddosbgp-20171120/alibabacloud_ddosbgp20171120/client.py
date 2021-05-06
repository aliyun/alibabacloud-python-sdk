# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore
from typing import Dict

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_tea_rpc import models as rpc_models
from alibabacloud_ddosbgp20171120 import models as ddosbgp_20171120_models
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

    def describe_on_demand_instance_with_options(
        self,
        request: ddosbgp_20171120_models.DescribeOnDemandInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DescribeOnDemandInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DescribeOnDemandInstanceResponse(),
            self.do_request('DescribeOnDemandInstance', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_on_demand_instance_with_options_async(
        self,
        request: ddosbgp_20171120_models.DescribeOnDemandInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DescribeOnDemandInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DescribeOnDemandInstanceResponse(),
            await self.do_request_async('DescribeOnDemandInstance', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_on_demand_instance(
        self,
        request: ddosbgp_20171120_models.DescribeOnDemandInstanceRequest,
    ) -> ddosbgp_20171120_models.DescribeOnDemandInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_on_demand_instance_with_options(request, runtime)

    async def describe_on_demand_instance_async(
        self,
        request: ddosbgp_20171120_models.DescribeOnDemandInstanceRequest,
    ) -> ddosbgp_20171120_models.DescribeOnDemandInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_on_demand_instance_with_options_async(request, runtime)

    def modify_on_demaond_defense_status_with_options(
        self,
        request: ddosbgp_20171120_models.ModifyOnDemaondDefenseStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.ModifyOnDemaondDefenseStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.ModifyOnDemaondDefenseStatusResponse(),
            self.do_request('ModifyOnDemaondDefenseStatus', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def modify_on_demaond_defense_status_with_options_async(
        self,
        request: ddosbgp_20171120_models.ModifyOnDemaondDefenseStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.ModifyOnDemaondDefenseStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.ModifyOnDemaondDefenseStatusResponse(),
            await self.do_request_async('ModifyOnDemaondDefenseStatus', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def modify_on_demaond_defense_status(
        self,
        request: ddosbgp_20171120_models.ModifyOnDemaondDefenseStatusRequest,
    ) -> ddosbgp_20171120_models.ModifyOnDemaondDefenseStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_on_demaond_defense_status_with_options(request, runtime)

    async def modify_on_demaond_defense_status_async(
        self,
        request: ddosbgp_20171120_models.ModifyOnDemaondDefenseStatusRequest,
    ) -> ddosbgp_20171120_models.ModifyOnDemaondDefenseStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_on_demaond_defense_status_with_options_async(request, runtime)

    def describe_op_entities_with_options(
        self,
        request: ddosbgp_20171120_models.DescribeOpEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DescribeOpEntitiesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DescribeOpEntitiesResponse(),
            self.do_request('DescribeOpEntities', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_op_entities_with_options_async(
        self,
        request: ddosbgp_20171120_models.DescribeOpEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DescribeOpEntitiesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DescribeOpEntitiesResponse(),
            await self.do_request_async('DescribeOpEntities', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_op_entities(
        self,
        request: ddosbgp_20171120_models.DescribeOpEntitiesRequest,
    ) -> ddosbgp_20171120_models.DescribeOpEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_op_entities_with_options(request, runtime)

    async def describe_op_entities_async(
        self,
        request: ddosbgp_20171120_models.DescribeOpEntitiesRequest,
    ) -> ddosbgp_20171120_models.DescribeOpEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_op_entities_with_options_async(request, runtime)

    def describe_pack_paid_traffic_with_options(
        self,
        request: ddosbgp_20171120_models.DescribePackPaidTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DescribePackPaidTrafficResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DescribePackPaidTrafficResponse(),
            self.do_request('DescribePackPaidTraffic', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_pack_paid_traffic_with_options_async(
        self,
        request: ddosbgp_20171120_models.DescribePackPaidTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DescribePackPaidTrafficResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DescribePackPaidTrafficResponse(),
            await self.do_request_async('DescribePackPaidTraffic', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_pack_paid_traffic(
        self,
        request: ddosbgp_20171120_models.DescribePackPaidTrafficRequest,
    ) -> ddosbgp_20171120_models.DescribePackPaidTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pack_paid_traffic_with_options(request, runtime)

    async def describe_pack_paid_traffic_async(
        self,
        request: ddosbgp_20171120_models.DescribePackPaidTrafficRequest,
    ) -> ddosbgp_20171120_models.DescribePackPaidTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pack_paid_traffic_with_options_async(request, runtime)

    def describe_resource_pack_usage_with_options(
        self,
        request: ddosbgp_20171120_models.DescribeResourcePackUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DescribeResourcePackUsageResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DescribeResourcePackUsageResponse(),
            self.do_request('DescribeResourcePackUsage', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_resource_pack_usage_with_options_async(
        self,
        request: ddosbgp_20171120_models.DescribeResourcePackUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DescribeResourcePackUsageResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DescribeResourcePackUsageResponse(),
            await self.do_request_async('DescribeResourcePackUsage', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_resource_pack_usage(
        self,
        request: ddosbgp_20171120_models.DescribeResourcePackUsageRequest,
    ) -> ddosbgp_20171120_models.DescribeResourcePackUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_pack_usage_with_options(request, runtime)

    async def describe_resource_pack_usage_async(
        self,
        request: ddosbgp_20171120_models.DescribeResourcePackUsageRequest,
    ) -> ddosbgp_20171120_models.DescribeResourcePackUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_pack_usage_with_options_async(request, runtime)

    def describe_resource_pack_statistics_with_options(
        self,
        request: ddosbgp_20171120_models.DescribeResourcePackStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DescribeResourcePackStatisticsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DescribeResourcePackStatisticsResponse(),
            self.do_request('DescribeResourcePackStatistics', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_resource_pack_statistics_with_options_async(
        self,
        request: ddosbgp_20171120_models.DescribeResourcePackStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DescribeResourcePackStatisticsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DescribeResourcePackStatisticsResponse(),
            await self.do_request_async('DescribeResourcePackStatistics', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_resource_pack_statistics(
        self,
        request: ddosbgp_20171120_models.DescribeResourcePackStatisticsRequest,
    ) -> ddosbgp_20171120_models.DescribeResourcePackStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_pack_statistics_with_options(request, runtime)

    async def describe_resource_pack_statistics_async(
        self,
        request: ddosbgp_20171120_models.DescribeResourcePackStatisticsRequest,
    ) -> ddosbgp_20171120_models.DescribeResourcePackStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_pack_statistics_with_options_async(request, runtime)

    def describe_resource_pack_instances_with_options(
        self,
        request: ddosbgp_20171120_models.DescribeResourcePackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DescribeResourcePackInstancesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DescribeResourcePackInstancesResponse(),
            self.do_request('DescribeResourcePackInstances', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_resource_pack_instances_with_options_async(
        self,
        request: ddosbgp_20171120_models.DescribeResourcePackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DescribeResourcePackInstancesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DescribeResourcePackInstancesResponse(),
            await self.do_request_async('DescribeResourcePackInstances', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_resource_pack_instances(
        self,
        request: ddosbgp_20171120_models.DescribeResourcePackInstancesRequest,
    ) -> ddosbgp_20171120_models.DescribeResourcePackInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_pack_instances_with_options(request, runtime)

    async def describe_resource_pack_instances_async(
        self,
        request: ddosbgp_20171120_models.DescribeResourcePackInstancesRequest,
    ) -> ddosbgp_20171120_models.DescribeResourcePackInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_pack_instances_with_options_async(request, runtime)

    def delete_blackhole_with_options(
        self,
        request: ddosbgp_20171120_models.DeleteBlackholeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DeleteBlackholeResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DeleteBlackholeResponse(),
            self.do_request('DeleteBlackhole', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_blackhole_with_options_async(
        self,
        request: ddosbgp_20171120_models.DeleteBlackholeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DeleteBlackholeResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DeleteBlackholeResponse(),
            await self.do_request_async('DeleteBlackhole', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_blackhole(
        self,
        request: ddosbgp_20171120_models.DeleteBlackholeRequest,
    ) -> ddosbgp_20171120_models.DeleteBlackholeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_blackhole_with_options(request, runtime)

    async def delete_blackhole_async(
        self,
        request: ddosbgp_20171120_models.DeleteBlackholeRequest,
    ) -> ddosbgp_20171120_models.DeleteBlackholeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_blackhole_with_options_async(request, runtime)

    def check_grant_with_options(
        self,
        request: ddosbgp_20171120_models.CheckGrantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.CheckGrantResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.CheckGrantResponse(),
            self.do_request('CheckGrant', 'HTTPS', 'GET', '2017-11-20', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def check_grant_with_options_async(
        self,
        request: ddosbgp_20171120_models.CheckGrantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.CheckGrantResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.CheckGrantResponse(),
            await self.do_request_async('CheckGrant', 'HTTPS', 'GET', '2017-11-20', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def check_grant(
        self,
        request: ddosbgp_20171120_models.CheckGrantRequest,
    ) -> ddosbgp_20171120_models.CheckGrantResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_grant_with_options(request, runtime)

    async def check_grant_async(
        self,
        request: ddosbgp_20171120_models.CheckGrantRequest,
    ) -> ddosbgp_20171120_models.CheckGrantResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_grant_with_options_async(request, runtime)

    def delete_product_with_options(
        self,
        request: ddosbgp_20171120_models.DeleteProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DeleteProductResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DeleteProductResponse(),
            self.do_request('DeleteProduct', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_product_with_options_async(
        self,
        request: ddosbgp_20171120_models.DeleteProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DeleteProductResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DeleteProductResponse(),
            await self.do_request_async('DeleteProduct', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_product(
        self,
        request: ddosbgp_20171120_models.DeleteProductRequest,
    ) -> ddosbgp_20171120_models.DeleteProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_product_with_options(request, runtime)

    async def delete_product_async(
        self,
        request: ddosbgp_20171120_models.DeleteProductRequest,
    ) -> ddosbgp_20171120_models.DeleteProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_product_with_options_async(request, runtime)

    def add_product_with_options(
        self,
        request: ddosbgp_20171120_models.AddProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.AddProductResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.AddProductResponse(),
            self.do_request('AddProduct', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def add_product_with_options_async(
        self,
        request: ddosbgp_20171120_models.AddProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.AddProductResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.AddProductResponse(),
            await self.do_request_async('AddProduct', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def add_product(
        self,
        request: ddosbgp_20171120_models.AddProductRequest,
    ) -> ddosbgp_20171120_models.AddProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_product_with_options(request, runtime)

    async def add_product_async(
        self,
        request: ddosbgp_20171120_models.AddProductRequest,
    ) -> ddosbgp_20171120_models.AddProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_product_with_options_async(request, runtime)

    def add_ip_with_options(
        self,
        request: ddosbgp_20171120_models.AddIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.AddIpResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.AddIpResponse(),
            self.do_request('AddIp', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def add_ip_with_options_async(
        self,
        request: ddosbgp_20171120_models.AddIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.AddIpResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.AddIpResponse(),
            await self.do_request_async('AddIp', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def add_ip(
        self,
        request: ddosbgp_20171120_models.AddIpRequest,
    ) -> ddosbgp_20171120_models.AddIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_ip_with_options(request, runtime)

    async def add_ip_async(
        self,
        request: ddosbgp_20171120_models.AddIpRequest,
    ) -> ddosbgp_20171120_models.AddIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_ip_with_options_async(request, runtime)

    def describe_instance_list_with_options(
        self,
        request: ddosbgp_20171120_models.DescribeInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DescribeInstanceListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DescribeInstanceListResponse(),
            self.do_request('DescribeInstanceList', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_instance_list_with_options_async(
        self,
        request: ddosbgp_20171120_models.DescribeInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DescribeInstanceListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DescribeInstanceListResponse(),
            await self.do_request_async('DescribeInstanceList', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_instance_list(
        self,
        request: ddosbgp_20171120_models.DescribeInstanceListRequest,
    ) -> ddosbgp_20171120_models.DescribeInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_list_with_options(request, runtime)

    async def describe_instance_list_async(
        self,
        request: ddosbgp_20171120_models.DescribeInstanceListRequest,
    ) -> ddosbgp_20171120_models.DescribeInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_list_with_options_async(request, runtime)

    def describe_top_traffic_with_options(
        self,
        request: ddosbgp_20171120_models.DescribeTopTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DescribeTopTrafficResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DescribeTopTrafficResponse(),
            self.do_request('DescribeTopTraffic', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_top_traffic_with_options_async(
        self,
        request: ddosbgp_20171120_models.DescribeTopTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DescribeTopTrafficResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DescribeTopTrafficResponse(),
            await self.do_request_async('DescribeTopTraffic', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_top_traffic(
        self,
        request: ddosbgp_20171120_models.DescribeTopTrafficRequest,
    ) -> ddosbgp_20171120_models.DescribeTopTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_top_traffic_with_options(request, runtime)

    async def describe_top_traffic_async(
        self,
        request: ddosbgp_20171120_models.DescribeTopTrafficRequest,
    ) -> ddosbgp_20171120_models.DescribeTopTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_top_traffic_with_options_async(request, runtime)

    def describe_ddos_event_with_options(
        self,
        request: ddosbgp_20171120_models.DescribeDdosEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DescribeDdosEventResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DescribeDdosEventResponse(),
            self.do_request('DescribeDdosEvent', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_ddos_event_with_options_async(
        self,
        request: ddosbgp_20171120_models.DescribeDdosEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DescribeDdosEventResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DescribeDdosEventResponse(),
            await self.do_request_async('DescribeDdosEvent', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_ddos_event(
        self,
        request: ddosbgp_20171120_models.DescribeDdosEventRequest,
    ) -> ddosbgp_20171120_models.DescribeDdosEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_with_options(request, runtime)

    async def describe_ddos_event_async(
        self,
        request: ddosbgp_20171120_models.DescribeDdosEventRequest,
    ) -> ddosbgp_20171120_models.DescribeDdosEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_event_with_options_async(request, runtime)

    def describe_traffic_with_options(
        self,
        request: ddosbgp_20171120_models.DescribeTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DescribeTrafficResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DescribeTrafficResponse(),
            self.do_request('DescribeTraffic', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_traffic_with_options_async(
        self,
        request: ddosbgp_20171120_models.DescribeTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DescribeTrafficResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DescribeTrafficResponse(),
            await self.do_request_async('DescribeTraffic', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_traffic(
        self,
        request: ddosbgp_20171120_models.DescribeTrafficRequest,
    ) -> ddosbgp_20171120_models.DescribeTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_traffic_with_options(request, runtime)

    async def describe_traffic_async(
        self,
        request: ddosbgp_20171120_models.DescribeTrafficRequest,
    ) -> ddosbgp_20171120_models.DescribeTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_traffic_with_options_async(request, runtime)

    def delete_ip_with_options(
        self,
        request: ddosbgp_20171120_models.DeleteIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DeleteIpResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DeleteIpResponse(),
            self.do_request('DeleteIp', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_ip_with_options_async(
        self,
        request: ddosbgp_20171120_models.DeleteIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DeleteIpResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DeleteIpResponse(),
            await self.do_request_async('DeleteIp', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_ip(
        self,
        request: ddosbgp_20171120_models.DeleteIpRequest,
    ) -> ddosbgp_20171120_models.DeleteIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ip_with_options(request, runtime)

    async def delete_ip_async(
        self,
        request: ddosbgp_20171120_models.DeleteIpRequest,
    ) -> ddosbgp_20171120_models.DeleteIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ip_with_options_async(request, runtime)

    def describe_pack_with_options(
        self,
        request: ddosbgp_20171120_models.DescribePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DescribePackResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DescribePackResponse(),
            self.do_request('DescribePack', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_pack_with_options_async(
        self,
        request: ddosbgp_20171120_models.DescribePackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DescribePackResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DescribePackResponse(),
            await self.do_request_async('DescribePack', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_pack(
        self,
        request: ddosbgp_20171120_models.DescribePackRequest,
    ) -> ddosbgp_20171120_models.DescribePackResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pack_with_options(request, runtime)

    async def describe_pack_async(
        self,
        request: ddosbgp_20171120_models.DescribePackRequest,
    ) -> ddosbgp_20171120_models.DescribePackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pack_with_options_async(request, runtime)

    def describe_pack_list_with_options(
        self,
        request: ddosbgp_20171120_models.DescribePackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DescribePackListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DescribePackListResponse(),
            self.do_request('DescribePackList', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_pack_list_with_options_async(
        self,
        request: ddosbgp_20171120_models.DescribePackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20171120_models.DescribePackListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddosbgp_20171120_models.DescribePackListResponse(),
            await self.do_request_async('DescribePackList', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_pack_list(
        self,
        request: ddosbgp_20171120_models.DescribePackListRequest,
    ) -> ddosbgp_20171120_models.DescribePackListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pack_list_with_options(request, runtime)

    async def describe_pack_list_async(
        self,
        request: ddosbgp_20171120_models.DescribePackListRequest,
    ) -> ddosbgp_20171120_models.DescribePackListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pack_list_with_options_async(request, runtime)

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
