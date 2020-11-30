# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_ddosbgp20171120 import models as ddosbgp_20171120_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
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

    def describe_on_demand_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20171120_models.DescribeOnDemandInstanceResponse().from_map(self.do_request('DescribeOnDemandInstance', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_on_demand_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_on_demand_instance_with_options(request, runtime)

    def modify_on_demaond_defense_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20171120_models.ModifyOnDemaondDefenseStatusResponse().from_map(self.do_request('ModifyOnDemaondDefenseStatus', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime))

    def modify_on_demaond_defense_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_on_demaond_defense_status_with_options(request, runtime)

    def describe_op_entities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20171120_models.DescribeOpEntitiesResponse().from_map(self.do_request('DescribeOpEntities', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_op_entities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_op_entities_with_options(request, runtime)

    def describe_pack_paid_traffic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20171120_models.DescribePackPaidTrafficResponse().from_map(self.do_request('DescribePackPaidTraffic', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_pack_paid_traffic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pack_paid_traffic_with_options(request, runtime)

    def describe_resource_pack_usage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20171120_models.DescribeResourcePackUsageResponse().from_map(self.do_request('DescribeResourcePackUsage', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_resource_pack_usage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_pack_usage_with_options(request, runtime)

    def describe_resource_pack_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20171120_models.DescribeResourcePackStatisticsResponse().from_map(self.do_request('DescribeResourcePackStatistics', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_resource_pack_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_pack_statistics_with_options(request, runtime)

    def describe_resource_pack_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20171120_models.DescribeResourcePackInstancesResponse().from_map(self.do_request('DescribeResourcePackInstances', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_resource_pack_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_pack_instances_with_options(request, runtime)

    def delete_blackhole_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20171120_models.DeleteBlackholeResponse().from_map(self.do_request('DeleteBlackhole', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime))

    def delete_blackhole(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_blackhole_with_options(request, runtime)

    def check_grant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20171120_models.CheckGrantResponse().from_map(self.do_request('CheckGrant', 'HTTPS', 'GET', '2017-11-20', 'AK', TeaCore.to_map(request), None, runtime))

    def check_grant(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_grant_with_options(request, runtime)

    def delete_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20171120_models.DeleteProductResponse().from_map(self.do_request('DeleteProduct', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime))

    def delete_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_product_with_options(request, runtime)

    def add_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20171120_models.AddProductResponse().from_map(self.do_request('AddProduct', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime))

    def add_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_product_with_options(request, runtime)

    def add_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20171120_models.AddIpResponse().from_map(self.do_request('AddIp', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime))

    def add_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_ip_with_options(request, runtime)

    def describe_instance_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20171120_models.DescribeInstanceListResponse().from_map(self.do_request('DescribeInstanceList', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_instance_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_list_with_options(request, runtime)

    def describe_top_traffic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20171120_models.DescribeTopTrafficResponse().from_map(self.do_request('DescribeTopTraffic', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_top_traffic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_top_traffic_with_options(request, runtime)

    def describe_ddos_event_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20171120_models.DescribeDdosEventResponse().from_map(self.do_request('DescribeDdosEvent', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_ddos_event(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_with_options(request, runtime)

    def describe_traffic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20171120_models.DescribeTrafficResponse().from_map(self.do_request('DescribeTraffic', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_traffic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_traffic_with_options(request, runtime)

    def delete_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20171120_models.DeleteIpResponse().from_map(self.do_request('DeleteIp', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime))

    def delete_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_ip_with_options(request, runtime)

    def describe_pack_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20171120_models.DescribePackResponse().from_map(self.do_request('DescribePack', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_pack(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pack_with_options(request, runtime)

    def describe_pack_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20171120_models.DescribePackListResponse().from_map(self.do_request('DescribePackList', 'HTTPS', 'POST', '2017-11-20', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_pack_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pack_list_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
