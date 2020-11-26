# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_ddosbgp20180720 import models as ddosbgp_20180720_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = "regional"
        self._endpoint_map = {
            "cn-qingdao": "ddosbgp.aliyuncs.com",
            "cn-beijing": "ddosbgp.aliyuncs.com",
            "cn-zhangjiakou": "ddosbgp.aliyuncs.com",
            "cn-huhehaote": "ddosbgp.aliyuncs.com",
            "cn-hangzhou": "ddosbgp.aliyuncs.com",
            "cn-shanghai": "ddosbgp.aliyuncs.com",
            "cn-shenzhen": "ddosbgp.aliyuncs.com",
            "ap-northeast-1": "ddosbgp.ap-southeast-1.aliyuncs.com",
            "ap-south-1": "ddosbgp.ap-southeast-1.aliyuncs.com",
            "ap-southeast-2": "ddosbgp.ap-southeast-1.aliyuncs.com",
            "ap-southeast-3": "ddosbgp.ap-southeast-1.aliyuncs.com",
            "ap-southeast-5": "ddosbgp.ap-southeast-1.aliyuncs.com",
            "cn-chengdu": "ddosbgp.aliyuncs.com",
            "eu-central-1": "ddosbgp.ap-southeast-1.aliyuncs.com",
            "eu-west-1": "ddosbgp.ap-southeast-1.aliyuncs.com",
            "me-east-1": "ddosbgp.ap-southeast-1.aliyuncs.com",
            "cn-hangzhou-finance": "ddosbgp.aliyuncs.com",
            "cn-shenzhen-finance-1": "ddosbgp.aliyuncs.com",
            "cn-shanghai-finance-1": "ddosbgp.aliyuncs.com",
            "cn-north-2-gov-1": "ddosbgp.aliyuncs.com"
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint("ddosbgp", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def describe_on_demand_instance_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeOnDemandInstanceStatusResponse().from_map(self.do_request("DescribeOnDemandInstanceStatus", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def describe_on_demand_instance_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_on_demand_instance_status_with_options(request, runtime)

    def set_instance_mode_on_demand_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.SetInstanceModeOnDemandResponse().from_map(self.do_request("SetInstanceModeOnDemand", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def set_instance_mode_on_demand(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_instance_mode_on_demand_with_options(request, runtime)

    def query_schedrule_on_demand_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.QuerySchedruleOnDemandResponse().from_map(self.do_request("QuerySchedruleOnDemand", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def query_schedrule_on_demand(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_schedrule_on_demand_with_options(request, runtime)

    def delete_schedrule_on_demand_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DeleteSchedruleOnDemandResponse().from_map(self.do_request("DeleteSchedruleOnDemand", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def delete_schedrule_on_demand(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_schedrule_on_demand_with_options(request, runtime)

    def config_schedrule_on_demand_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.ConfigSchedruleOnDemandResponse().from_map(self.do_request("ConfigSchedruleOnDemand", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def config_schedrule_on_demand(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_schedrule_on_demand_with_options(request, runtime)

    def create_schedrule_on_demand_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.CreateSchedruleOnDemandResponse().from_map(self.do_request("CreateSchedruleOnDemand", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def create_schedrule_on_demand(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_schedrule_on_demand_with_options(request, runtime)

    def describe_on_demand_ddos_event_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeOnDemandDdosEventResponse().from_map(self.do_request("DescribeOnDemandDdosEvent", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def describe_on_demand_ddos_event(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_on_demand_ddos_event_with_options(request, runtime)

    def list_tag_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.ListTagKeysResponse().from_map(self.do_request("ListTagKeys", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def list_tag_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.ListTagResourcesResponse().from_map(self.do_request("ListTagResources", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.UntagResourcesResponse().from_map(self.do_request("UntagResources", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.TagResourcesResponse().from_map(self.do_request("TagResources", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def describe_excpetion_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeExcpetionCountResponse().from_map(self.do_request("DescribeExcpetionCount", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def describe_excpetion_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_excpetion_count_with_options(request, runtime)

    def describe_pack_ip_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribePackIpListResponse().from_map(self.do_request("DescribePackIpList", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def describe_pack_ip_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pack_ip_list_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeRegionsResponse().from_map(self.do_request("DescribeRegions", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def modify_remark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.ModifyRemarkResponse().from_map(self.do_request("ModifyRemark", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def modify_remark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_remark_with_options(request, runtime)

    def describe_traffic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeTrafficResponse().from_map(self.do_request("DescribeTraffic", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def describe_traffic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_traffic_with_options(request, runtime)

    def describe_resource_pack_usage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeResourcePackUsageResponse().from_map(self.do_request("DescribeResourcePackUsage", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def describe_resource_pack_usage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_pack_usage_with_options(request, runtime)

    def describe_resource_pack_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeResourcePackStatisticsResponse().from_map(self.do_request("DescribeResourcePackStatistics", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def describe_resource_pack_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_pack_statistics_with_options(request, runtime)

    def describe_resource_pack_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeResourcePackInstancesResponse().from_map(self.do_request("DescribeResourcePackInstances", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def describe_resource_pack_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_pack_instances_with_options(request, runtime)

    def describe_pack_paid_traffic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribePackPaidTrafficResponse().from_map(self.do_request("DescribePackPaidTraffic", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def describe_pack_paid_traffic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pack_paid_traffic_with_options(request, runtime)

    def describe_op_entities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeOpEntitiesResponse().from_map(self.do_request("DescribeOpEntities", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def describe_op_entities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_op_entities_with_options(request, runtime)

    def describe_instance_specs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeInstanceSpecsResponse().from_map(self.do_request("DescribeInstanceSpecs", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def describe_instance_specs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_specs_with_options(request, runtime)

    def describe_instance_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeInstanceListResponse().from_map(self.do_request("DescribeInstanceList", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def describe_instance_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_list_with_options(request, runtime)

    def describe_ddos_event_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DescribeDdosEventResponse().from_map(self.do_request("DescribeDdosEvent", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def describe_ddos_event(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_with_options(request, runtime)

    def delete_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DeleteIpResponse().from_map(self.do_request("DeleteIp", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def delete_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_ip_with_options(request, runtime)

    def delete_blackhole_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.DeleteBlackholeResponse().from_map(self.do_request("DeleteBlackhole", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def delete_blackhole(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_blackhole_with_options(request, runtime)

    def check_grant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.CheckGrantResponse().from_map(self.do_request("CheckGrant", "HTTPS", "GET", "2018-07-20", "AK", request.to_map(), None, runtime))

    def check_grant(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_grant_with_options(request, runtime)

    def add_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ddosbgp_20180720_models.AddIpResponse().from_map(self.do_request("AddIp", "HTTPS", "POST", "2018-07-20", "AK", None, request.to_map(), runtime))

    def add_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_ip_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
