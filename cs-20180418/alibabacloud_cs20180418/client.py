# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_roa.client import Client as ROAClient
from alibabacloud_cs20180418 import models as cs20180418_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(ROAClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = "regional"
        self._endpoint_map = {
            "ap-northeast-2-pop": "cs.aliyuncs.com",
            "cn-beijing-finance-1": "cs.aliyuncs.com",
            "cn-beijing-finance-pop": "cs.aliyuncs.com",
            "cn-beijing-gov-1": "cs.aliyuncs.com",
            "cn-beijing-nu16-b01": "cs.aliyuncs.com",
            "cn-edge-1": "cs.aliyuncs.com",
            "cn-fujian": "cs.aliyuncs.com",
            "cn-haidian-cm12-c01": "cs.aliyuncs.com",
            "cn-hangzhou-bj-b01": "cs.aliyuncs.com",
            "cn-hangzhou-finance": "cs.aliyuncs.com",
            "cn-hangzhou-internal-prod-1": "cs.aliyuncs.com",
            "cn-hangzhou-internal-test-1": "cs.aliyuncs.com",
            "cn-hangzhou-internal-test-2": "cs.aliyuncs.com",
            "cn-hangzhou-internal-test-3": "cs.aliyuncs.com",
            "cn-hangzhou-test-306": "cs.aliyuncs.com",
            "cn-hongkong-finance-pop": "cs.aliyuncs.com",
            "cn-huhehaote-nebula-1": "cs.aliyuncs.com",
            "cn-qingdao-nebula": "cs.aliyuncs.com",
            "cn-shanghai-et15-b01": "cs.aliyuncs.com",
            "cn-shanghai-et2-b01": "cs.aliyuncs.com",
            "cn-shanghai-finance-1": "cs.aliyuncs.com",
            "cn-shanghai-inner": "cs.aliyuncs.com",
            "cn-shanghai-internal-test-1": "cs.aliyuncs.com",
            "cn-shenzhen-finance-1": "cs.aliyuncs.com",
            "cn-shenzhen-inner": "cs.aliyuncs.com",
            "cn-shenzhen-st4-d01": "cs.aliyuncs.com",
            "cn-shenzhen-su18-b01": "cs.aliyuncs.com",
            "cn-wuhan": "cs.aliyuncs.com",
            "cn-wulanchabu": "cs.aliyuncs.com",
            "cn-yushanfang": "cs.aliyuncs.com",
            "cn-zhangbei-na61-b01": "cs.aliyuncs.com",
            "cn-zhangjiakou-na62-a01": "cs.aliyuncs.com",
            "cn-zhengzhou-nebula-1": "cs.aliyuncs.com",
            "eu-west-1-oxs": "cs.aliyuncs.com",
            "rus-west-1-pop": "cs.aliyuncs.com"
        }
        self.check_config(config)
        self._endpoint_host = self.get_endpoint("cs", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint_host)

    def get_project_events_with_options(self, cluster_id, project_id, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.GetProjectEventsResponse().from_map(self.do_request_with_action("GetProjectEvents", "2018-04-18", "HTTPS", "GET", "AK", "/clusters/" + str(cluster_id) + "/projects/" + str(project_id) + "/events", None, request.headers, None, runtime))

    def get_project_events(self, cluster_id, project_id, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_project_events_with_options(cluster_id, project_id, request, runtime)

    def describe_kubernetes_template_with_options(self, cluster_id, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DescribeKubernetesTemplateResponse().from_map(self.do_request_with_action("DescribeKubernetesTemplate", "2018-04-18", "HTTPS", "GET", "AK", "/k8s/templates/" + str(cluster_id) + "", None, request.headers, None, runtime))

    def describe_kubernetes_template(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_kubernetes_template_with_options(cluster_id, request, runtime)

    def describe_agility_tunnel_certs_with_options(self, token, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DescribeAgilityTunnelCertsResponse().from_map(self.do_request_with_action("DescribeAgilityTunnelCerts", "2018-04-18", "HTTPS", "GET", "Anonymous", "/agility/" + str(token) + "/agent_certs", None, request.headers, None, runtime))

    def describe_agility_tunnel_certs(self, token, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_agility_tunnel_certs_with_options(token, request, runtime)

    def describe_cluster_tokens_with_options(self, cluster_id, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DescribeClusterTokensResponse().from_map(self.do_request_with_action("DescribeClusterTokens", "2018-04-18", "HTTPS", "GET", "AK", "/clusters/" + str(cluster_id) + "/tokens", None, request.headers, None, runtime))

    def describe_cluster_tokens(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_cluster_tokens_with_options(cluster_id, request, runtime)

    def download_cluster_node_certs_with_options(self, token, node_id, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DownloadClusterNodeCertsResponse().from_map(self.do_request_with_action("DownloadClusterNodeCerts", "2018-04-18", "HTTPS", "GET", "Anonymous", "/token/" + str(token) + "/nodes/" + str(node_id) + "/certs", None, request.headers, None, runtime))

    def download_cluster_node_certs(self, token, node_id, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.download_cluster_node_certs_with_options(token, node_id, request, runtime)

    def describe_service_containers_with_options(self, cluster_id, service_id, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DescribeServiceContainersResponse().from_map(self.do_request_with_action("DescribeServiceContainers", "2018-04-18", "HTTPS", "GET", "AK", "/clusters/" + str(cluster_id) + "/services/" + str(service_id) + "/containers", None, request.headers, None, runtime))

    def describe_service_containers(self, cluster_id, service_id, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_service_containers_with_options(cluster_id, service_id, request, runtime)

    def gather_logs_token_with_options(self, token, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.GatherLogsTokenResponse().from_map(self.do_request_with_action("GatherLogsToken", "2018-04-18", "HTTPS", "POST", "Anonymous", "/token/" + str(token) + "/gather_logs", None, request.headers, None, runtime))

    def gather_logs_token(self, token, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.gather_logs_token_with_options(token, request, runtime)

    def get_cluster_projects_with_options(self, cluster_id, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.GetClusterProjectsResponse().from_map(self.do_request_with_action("GetClusterProjects", "2018-04-18", "HTTPS", "GET", "AK", "/clusters/" + str(cluster_id) + "/projects", None, request.headers, None, runtime))

    def get_cluster_projects(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_cluster_projects_with_options(cluster_id, request, runtime)

    def describe_api_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DescribeApiVersionResponse().from_map(self.do_request_with_action("DescribeApiVersion", "2018-04-18", "HTTPS", "GET", "AK", "/version", None, request.headers, None, runtime))

    def describe_api_version(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_api_version_with_options(request, runtime)

    def describe_task_info_with_options(self, task_id, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DescribeTaskInfoResponse().from_map(self.do_request_with_action("DescribeTaskInfo", "2018-04-18", "HTTPS", "GET", "AK", "/tasks/" + str(task_id) + "", None, request.headers, None, runtime))

    def describe_task_info(self, task_id, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_task_info_with_options(task_id, request, runtime)

    def describe_cluster_nodes_with_options(self, cluster_id, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DescribeClusterNodesResponse().from_map(self.do_request_with_action("DescribeClusterNodes", "2018-04-18", "HTTPS", "GET", "AK", "/clusters/" + str(cluster_id) + "/nodes", UtilClient.stringify_map_value(request.query.to_map()), request.headers, None, runtime))

    def describe_cluster_nodes(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_cluster_nodes_with_options(cluster_id, request, runtime)

    def describe_agility_tunnel_agent_info_with_options(self, token, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DescribeAgilityTunnelAgentInfoResponse().from_map(self.do_request_with_action("DescribeAgilityTunnelAgentInfo", "2018-04-18", "HTTPS", "GET", "Anonymous", "/agility/" + str(token) + "/agent_info", None, request.headers, None, runtime))

    def describe_agility_tunnel_agent_info(self, token, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_agility_tunnel_agent_info_with_options(token, request, runtime)

    def delete_cluster_node_with_options(self, cluster_id, ip, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DeleteClusterNodeResponse().from_map(self.do_request_with_action("DeleteClusterNode", "2018-04-18", "HTTPS", "DELETE", "AK", "/clusters/" + str(cluster_id) + "/ip/" + str(ip) + "", UtilClient.stringify_map_value(request.query.to_map()), request.headers, None, runtime))

    def delete_cluster_node(self, cluster_id, ip, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_cluster_node_with_options(cluster_id, ip, request, runtime)

    def describe_cluster_node_info_with_instance_with_options(self, token, instance_id, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DescribeClusterNodeInfoWithInstanceResponse().from_map(self.do_request_with_action("DescribeClusterNodeInfoWithInstance", "2018-04-18", "HTTPS", "GET", "Anonymous", "/token/" + str(token) + "/instance/" + str(instance_id) + "/node_info", None, request.headers, None, runtime))

    def describe_cluster_node_info_with_instance(self, token, instance_id, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_cluster_node_info_with_instance_with_options(token, instance_id, request, runtime)

    def describe_user_containers_with_options(self, region_id, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DescribeUserContainersResponse().from_map(self.do_request_with_action("DescribeUserContainers", "2018-04-18", "HTTPS", "GET", "AK", "/region/" + str(region_id) + "/containers", UtilClient.stringify_map_value(request.query.to_map()), request.headers, None, runtime))

    def describe_user_containers(self, region_id, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_user_containers_with_options(region_id, request, runtime)

    def create_cluster_token_with_options(self, cluster_id, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.CreateClusterTokenResponse().from_map(self.do_request_with_action("CreateClusterToken", "2018-04-18", "HTTPS", "POST", "AK", "/clusters/" + str(cluster_id) + "/token", None, request.headers, None, runtime))

    def create_cluster_token(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_cluster_token_with_options(cluster_id, request, runtime)

    def describe_cluster_hosts_with_options(self, cluster_id, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DescribeClusterHostsResponse().from_map(self.do_request_with_action("DescribeClusterHosts", "2018-04-18", "HTTPS", "GET", "AK", "/clusters/" + str(cluster_id) + "/hosts", None, request.headers, None, runtime))

    def describe_cluster_hosts(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_cluster_hosts_with_options(cluster_id, request, runtime)

    def describe_kubernetes_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DescribeKubernetesTemplatesResponse().from_map(self.do_request_with_action("DescribeKubernetesTemplates", "2018-04-18", "HTTPS", "GET", "AK", "/k8s/templates", UtilClient.stringify_map_value(request.query.to_map()), request.headers, None, runtime))

    def describe_kubernetes_templates(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_kubernetes_templates_with_options(request, runtime)

    def describe_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DescribeTemplatesResponse().from_map(self.do_request_with_action("DescribeTemplates", "2018-04-18", "HTTPS", "GET", "AK", "/templates", None, request.headers, None, runtime))

    def describe_templates(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_templates_with_options(request, runtime)

    def describe_cluster_scaled_node_with_options(self, cluster_id, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DescribeClusterScaledNodeResponse().from_map(self.do_request_with_action("DescribeClusterScaledNode", "2018-04-18", "HTTPS", "GET", "AK", "/clusters/" + str(cluster_id) + "/scaled_nodes/", None, request.headers, None, runtime))

    def describe_cluster_scaled_node(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_cluster_scaled_node_with_options(cluster_id, request, runtime)

    def callback_cluster_token_with_options(self, token, req_once, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.CallbackClusterTokenResponse().from_map(self.do_request_with_action("CallbackClusterToken", "2018-04-18", "HTTPS", "POST", "Anonymous", "/token/" + str(token) + "/req_once/" + str(req_once) + "/callback", None, request.headers, None, runtime))

    def callback_cluster_token(self, token, req_once, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.callback_cluster_token_with_options(token, req_once, request, runtime)

    def describe_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DescribeImagesResponse().from_map(self.do_request_with_action("DescribeImages", "2018-04-18", "HTTPS", "GET", "AK", "/images", UtilClient.stringify_map_value(request.query.to_map()), request.headers, None, runtime))

    def describe_images(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_images_with_options(request, runtime)

    def describe_cluster_logs_with_options(self, cluster_id, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DescribeClusterLogsResponse().from_map(self.do_request_with_action("DescribeClusterLogs", "2018-04-18", "HTTPS", "GET", "AK", "/clusters/" + str(cluster_id) + "/logs", None, request.headers, None, runtime))

    def describe_cluster_logs(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_cluster_logs_with_options(cluster_id, request, runtime)

    def describe_cluster_services_with_options(self, cluster_id, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DescribeClusterServicesResponse().from_map(self.do_request_with_action("DescribeClusterServices", "2018-04-18", "HTTPS", "GET", "AK", "/clusters/" + str(cluster_id) + "/services", None, request.headers, None, runtime))

    def describe_cluster_services(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_cluster_services_with_options(cluster_id, request, runtime)

    def get_trigger_hook_with_options(self, cluster_id, project_id, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.GetTriggerHookResponse().from_map(self.do_request_with_action("GetTriggerHook", "2018-04-18", "HTTPS", "GET", "AK", "/hook/trigger/" + str(cluster_id) + "/" + str(project_id) + "", None, request.headers, None, runtime))

    def get_trigger_hook(self, cluster_id, project_id, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_trigger_hook_with_options(cluster_id, project_id, request, runtime)

    def describe_template_attribute_with_options(self, template_id, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DescribeTemplateAttributeResponse().from_map(self.do_request_with_action("DescribeTemplateAttribute", "2018-04-18", "HTTPS", "GET", "AK", "/templates/" + str(template_id) + "", None, request.headers, None, runtime))

    def describe_template_attribute(self, template_id, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_template_attribute_with_options(template_id, request, runtime)

    def describe_cluster_certs_with_options(self, cluster_id, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DescribeClusterCertsResponse().from_map(self.do_request_with_action("DescribeClusterCerts", "2018-04-18", "HTTPS", "GET", "AK", "/clusters/" + str(cluster_id) + "/certs", None, request.headers, None, runtime))

    def describe_cluster_certs(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_cluster_certs_with_options(cluster_id, request, runtime)

    def describe_cluster_node_info_with_options(self, token, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DescribeClusterNodeInfoResponse().from_map(self.do_request_with_action("DescribeClusterNodeInfo", "2018-04-18", "HTTPS", "GET", "Anonymous", "/token/" + str(token) + "/node_info", None, request.headers, None, runtime))

    def describe_cluster_node_info(self, token, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_cluster_node_info_with_options(token, request, runtime)

    def delete_cluster_with_options(self, cluster_id, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DeleteClusterResponse().from_map(self.do_request_with_action("DeleteCluster", "2018-04-18", "HTTPS", "DELETE", "AK", "/clusters/" + str(cluster_id) + "", None, request.headers, None, runtime))

    def delete_cluster(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_cluster_with_options(cluster_id, request, runtime)

    def create_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.CreateClusterResponse().from_map(self.do_request_with_action("CreateCluster", "2018-04-18", "HTTPS", "POST", "AK", "/clusters", None, request.headers, None, runtime))

    def create_cluster(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_cluster_with_options(request, runtime)

    def describe_cluster_detail_with_options(self, cluster_id, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DescribeClusterDetailResponse().from_map(self.do_request_with_action("DescribeClusterDetail", "2018-04-18", "HTTPS", "GET", "AK", "/clusters/" + str(cluster_id) + "", None, request.headers, None, runtime))

    def describe_cluster_detail(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_cluster_detail_with_options(cluster_id, request, runtime)

    def describe_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return cs20180418_models.DescribeClustersResponse().from_map(self.do_request_with_action("DescribeClusters", "2018-04-18", "HTTPS", "GET", "AK", "/clusters", UtilClient.stringify_map_value(request.query.to_map()), request.headers, None, runtime))

    def describe_clusters(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_clusters_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
