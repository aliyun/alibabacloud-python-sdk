# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_gws20190618 import models as gws_20190618_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = "regional"
        self._endpoint_map = {
            "ap-southeast-3": "gws.ap-northeast-3.aliyuncs.com",
            "cn-hangzhou-finance": "ecd.cn-hangzhou-finance.aliyuncs.com"
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint("gws", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def set_cluster_dnat_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.SetClusterDnatResponse().from_map(self.do_request("SetClusterDnat", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def set_cluster_dnat(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_cluster_dnat_with_options(request, runtime)

    def create_service_linked_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.CreateServiceLinkedRoleResponse().from_map(self.do_request("CreateServiceLinkedRole", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def create_service_linked_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    def describe_cluster_connections_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.DescribeClusterConnectionsResponse().from_map(self.do_request("DescribeClusterConnections", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def describe_cluster_connections(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_connections_with_options(request, runtime)

    def describe_cluster_addomain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.DescribeClusterADDomainResponse().from_map(self.do_request("DescribeClusterADDomain", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def describe_cluster_addomain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_addomain_with_options(request, runtime)

    def set_cluster_addomain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.SetClusterADDomainResponse().from_map(self.do_request("SetClusterADDomain", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def set_cluster_addomain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_cluster_addomain_with_options(request, runtime)

    def describe_instance_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.DescribeInstancePolicyResponse().from_map(self.do_request("DescribeInstancePolicy", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def describe_instance_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_policy_with_options(request, runtime)

    def set_instance_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.SetInstancePolicyResponse().from_map(self.do_request("SetInstancePolicy", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def set_instance_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_instance_policy_with_options(request, runtime)

    def describe_available_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.DescribeAvailableResourceResponse().from_map(self.do_request("DescribeAvailableResource", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def describe_available_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    def set_cluster_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.SetClusterPolicyResponse().from_map(self.do_request("SetClusterPolicy", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def set_cluster_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_cluster_policy_with_options(request, runtime)

    def describe_cluster_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.DescribeClusterPolicyResponse().from_map(self.do_request("DescribeClusterPolicy", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def describe_cluster_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_policy_with_options(request, runtime)

    def set_instance_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.SetInstanceNameResponse().from_map(self.do_request("SetInstanceName", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def set_instance_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_instance_name_with_options(request, runtime)

    def set_image_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.SetImageNameResponse().from_map(self.do_request("SetImageName", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def set_image_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_image_name_with_options(request, runtime)

    def set_cluster_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.SetClusterNameResponse().from_map(self.do_request("SetClusterName", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def set_cluster_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_cluster_name_with_options(request, runtime)

    def stop_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.StopInstanceResponse().from_map(self.do_request("StopInstance", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def stop_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    def start_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.StartInstanceResponse().from_map(self.do_request("StartInstance", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def start_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    def set_instance_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.SetInstanceUserResponse().from_map(self.do_request("SetInstanceUser", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def set_instance_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_instance_user_with_options(request, runtime)

    def restart_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.RestartInstanceResponse().from_map(self.do_request("RestartInstance", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def restart_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restart_instance_with_options(request, runtime)

    def is_user_admin_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.IsUserAdminResponse().from_map(self.do_request("IsUserAdmin", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def is_user_admin(self, request):
        runtime = util_models.RuntimeOptions()
        return self.is_user_admin_with_options(request, runtime)

    def get_connect_ticket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.GetConnectTicketResponse().from_map(self.do_request("GetConnectTicket", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def get_connect_ticket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_connect_ticket_with_options(request, runtime)

    def describe_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.DescribeInstancesResponse().from_map(self.do_request("DescribeInstances", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def describe_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    def describe_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.DescribeImagesResponse().from_map(self.do_request("DescribeImages", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def describe_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_images_with_options(request, runtime)

    def describe_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.DescribeClustersResponse().from_map(self.do_request("DescribeClusters", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def describe_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_clusters_with_options(request, runtime)

    def delete_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.DeleteInstanceResponse().from_map(self.do_request("DeleteInstance", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def delete_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    def delete_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.DeleteImageResponse().from_map(self.do_request("DeleteImage", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def delete_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_image_with_options(request, runtime)

    def delete_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.DeleteClusterResponse().from_map(self.do_request("DeleteCluster", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def delete_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    def create_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.CreateInstanceResponse().from_map(self.do_request("CreateInstance", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def create_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    def create_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.CreateImageResponse().from_map(self.do_request("CreateImage", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def create_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_image_with_options(request, runtime)

    def create_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return gws_20190618_models.CreateClusterResponse().from_map(self.do_request("CreateCluster", "HTTPS", "POST", "2019-06-18", "AK", None, request.to_map(), runtime))

    def create_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
