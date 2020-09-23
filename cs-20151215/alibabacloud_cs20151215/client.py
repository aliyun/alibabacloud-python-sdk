# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cs20151215 import models as cs20151215_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *
    """
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
        self._endpoint = self.get_endpoint("cs", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def attach_instances(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.attach_instances_with_options(cluster_id, request, headers, runtime)

    def attach_instances_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        body["instances"] = request.instances
        body["runtime"] = request.runtime
        body["image_id"] = request.image_id
        body["format_disk"] = request.format_disk
        body["keep_instance_name"] = request.keep_instance_name
        body["cpu_policy"] = request.cpu_policy
        body["key_pair"] = request.key_pair
        body["password"] = request.password
        body["is_edge_worker"] = request.is_edge_worker
        body["user_data"] = request.user_data
        body["nodepool_id"] = request.nodepool_id
        body["rds_instances"] = request.rds_instances
        body["tags"] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=body
        )
        return cs20151215_models.AttachInstancesResponse().from_map(self.do_roarequest_with_form("AttachInstances", "2015-12-15", "HTTPS", "POST", "AK", "/clusters/" + str(cluster_id) + "/attach", "json", req, runtime))

    def cancel_cluster_upgrade(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.cancel_cluster_upgrade_with_options(cluster_id, request, headers, runtime)

    def cancel_cluster_upgrade_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cs20151215_models.CancelClusterUpgradeResponse().from_map(self.do_roarequest("CancelClusterUpgrade", "2015-12-15", "HTTPS", "POST", "AK", "/api/v2/clusters/" + str(cluster_id) + "/upgrade/cancel", "none", req, runtime))

    def cancel_component_upgrade(self, clusterid, componentid, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.cancel_component_upgrade_with_options(clusterid, componentid, request, headers, runtime)

    def cancel_component_upgrade_with_options(self, clusterid, componentid, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cs20151215_models.CancelComponentUpgradeResponse().from_map(self.do_roarequest("CancelComponentUpgrade", "2015-12-15", "HTTPS", "POST", "AK", "/clusters/" + str(clusterid) + "/components/{componentid}/cancel", "none", req, runtime))

    def create_cluster(self, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.create_cluster_with_options(request, headers, runtime)

    def create_cluster_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        body["name"] = request.name
        body["cluster_type"] = request.cluster_type
        body["region_id"] = request.region_id
        body["zone_id"] = request.zone_id
        body["kubernetes_version"] = request.kubernetes_version
        body["deletion_protection"] = request.deletion_protection
        body["runtime"] = request.runtime
        body["vpcid"] = request.vpcid
        body["worker_vswitch_ids"] = request.worker_vswitch_ids
        body["container_cidr"] = request.container_cidr
        body["service_cidr"] = request.service_cidr
        body["node_cidr_mask"] = request.node_cidr_mask
        body["snat_entry"] = request.snat_entry
        body["endpoint_public_access"] = request.endpoint_public_access
        body["ssh_flags"] = request.ssh_flags
        body["rds_instances"] = request.rds_instances
        body["security_group_id"] = request.security_group_id
        body["is_enterprise_security_group"] = request.is_enterprise_security_group
        body["proxy_mode"] = request.proxy_mode
        body["tags"] = request.tags
        body["images_id"] = request.images_id
        body["master_instance_charge_type"] = request.master_instance_charge_type
        body["master_period"] = request.master_period
        body["master_period_unit"] = request.master_period_unit
        body["master_auto_renew"] = request.master_auto_renew
        body["master_auto_renew_period"] = request.master_auto_renew_period
        body["master_count"] = request.master_count
        body["master_vswitch_ids"] = request.master_vswitch_ids
        body["master_instance_types"] = request.master_instance_types
        body["master_system_disk_category"] = request.master_system_disk_category
        body["master_system_disk_size"] = request.master_system_disk_size
        body["worker_instance_charge_type"] = request.worker_instance_charge_type
        body["worker_period"] = request.worker_period
        body["worker_period_unit"] = request.worker_period_unit
        body["worker_auto_renew"] = request.worker_auto_renew
        body["worker_auto_renew_period"] = request.worker_auto_renew_period
        body["num_of_nodes"] = request.num_of_nodes
        body["worker_instance_types"] = request.worker_instance_types
        body["worker_system_disk_category"] = request.worker_system_disk_category
        body["worker_system_disk_size"] = request.worker_system_disk_size
        body["worker_data_disks"] = request.worker_data_disks
        body["os_type"] = request.os_type
        body["key_pair"] = request.key_pair
        body["login_password"] = request.login_password
        body["user_data"] = request.user_data
        body["node_port_range"] = request.node_port_range
        body["cpu_policy"] = request.cpu_policy
        body["taints"] = request.taints
        body["cloud_monitor_flags"] = request.cloud_monitor_flags
        body["addons"] = request.addons
        body["platform"] = request.platform
        body["vswitch_ids"] = request.vswitch_ids
        body["private_zone"] = request.private_zone
        body["profile"] = request.profile
        body["pod_vswitch_ids"] = request.pod_vswitch_ids
        body["disable_rollback"] = request.disable_rollback
        body["timeout_mins"] = request.timeout_mins
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=body
        )
        return cs20151215_models.CreateClusterResponse().from_map(self.do_roarequest_with_form("CreateCluster", "2015-12-15", "HTTPS", "POST", "AK", "/clusters", "json", req, runtime))

    def create_kubernetes_trigger(self, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.create_kubernetes_trigger_with_options(request, headers, runtime)

    def create_kubernetes_trigger_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        body["RegionId"] = request.region_id
        body["ClusterId"] = request.cluster_id
        body["ProjectId"] = request.project_id
        body["Type"] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=body
        )
        return cs20151215_models.CreateKubernetesTriggerResponse().from_map(self.do_roarequest_with_form("CreateKubernetesTrigger", "2015-12-15", "HTTPS", "POST", "AK", "/triggers", "json", req, runtime))

    def delete_cluster(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.delete_cluster_with_options(cluster_id, request, headers, runtime)

    def delete_cluster_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        query["retain_resources"] = request.retain_resources
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cs20151215_models.DeleteClusterResponse().from_map(self.do_roarequest("DeleteCluster", "2015-12-15", "HTTPS", "DELETE", "AK", "/clusters/" + str(cluster_id) + "", "none", req, runtime))

    def delete_kubernetes_trigger(self, id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.delete_kubernetes_trigger_with_options(id, request, headers, runtime)

    def delete_kubernetes_trigger_with_options(self, id, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cs20151215_models.DeleteKubernetesTriggerResponse().from_map(self.do_roarequest("DeleteKubernetesTrigger", "2015-12-15", "HTTPS", "DELETE", "AK", "/triggers/revoke/" + str(id) + "", "none", req, runtime))

    def describe_addons(self, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.describe_addons_with_options(request, headers, runtime)

    def describe_addons_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        query["region"] = request.region
        query["cluster_type"] = request.cluster_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cs20151215_models.DescribeAddonsResponse().from_map(self.do_roarequest("DescribeAddons", "2015-12-15", "HTTPS", "GET", "AK", "/clusters/components/metadata", "json", req, runtime))

    def describe_cluster_addon_upgrade_status(self, cluster_id, component_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.describe_cluster_addon_upgrade_status_with_options(cluster_id, component_id, request, headers, runtime)

    def describe_cluster_addon_upgrade_status_with_options(self, cluster_id, component_id, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cs20151215_models.DescribeClusterAddonUpgradeStatusResponse().from_map(self.do_roarequest("DescribeClusterAddonUpgradeStatus", "2015-12-15", "HTTPS", "GET", "AK", "/clusters/" + str(cluster_id) + "/components/{ComponentId}/upgradestatus", "json", req, runtime))

    def describe_cluster_addons_upgrade_status(self, cluster_id, request):
        """
        批量查询集群Addon升级状态
        """
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.describe_cluster_addons_upgrade_status_with_options(cluster_id, request, headers, runtime)

    def describe_cluster_addons_upgrade_status_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        query["componentIds"] = request.component_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cs20151215_models.DescribeClusterAddonsUpgradeStatusResponse().from_map(self.do_roarequest("DescribeClusterAddonsUpgradeStatus", "2015-12-15", "HTTPS", "GET", "AK", "/clusters/[ClusterId]/components/upgradestatus", "none", req, runtime))

    def describe_cluster_addons_version(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.describe_cluster_addons_version_with_options(cluster_id, request, headers, runtime)

    def describe_cluster_addons_version_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cs20151215_models.DescribeClusterAddonsVersionResponse().from_map(self.do_roarequest("DescribeClusterAddonsVersion", "2015-12-15", "HTTPS", "GET", "AK", "/clusters/" + str(cluster_id) + "/components/version", "json", req, runtime))

    def describe_cluster_attach_scripts(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.describe_cluster_attach_scripts_with_options(cluster_id, request, headers, runtime)

    def describe_cluster_attach_scripts_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        body["arch"] = request.arch
        body["options"] = request.options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=body
        )
        return cs20151215_models.DescribeClusterAttachScriptsResponse().from_map(self.do_roarequest_with_form("DescribeClusterAttachScripts", "2015-12-15", "HTTPS", "POST", "AK", "/clusters/" + str(cluster_id) + "/attachscript", "string", req, runtime))

    def describe_cluster_detail(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.describe_cluster_detail_with_options(cluster_id, request, headers, runtime)

    def describe_cluster_detail_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cs20151215_models.DescribeClusterDetailResponse().from_map(self.do_roarequest("DescribeClusterDetail", "2015-12-15", "HTTPS", "GET", "AK", "/clusters/" + str(cluster_id) + "", "json", req, runtime))

    def describe_cluster_logs(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.describe_cluster_logs_with_options(cluster_id, request, headers, runtime)

    def describe_cluster_logs_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cs20151215_models.DescribeClusterLogsResponse().from_map(self.do_roarequest("DescribeClusterLogs", "2015-12-15", "HTTPS", "GET", "AK", "/clusters/" + str(cluster_id) + "/logs", "json", req, runtime))

    def describe_cluster_nodes(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.describe_cluster_nodes_with_options(cluster_id, request, headers, runtime)

    def describe_cluster_nodes_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        query["pageSize"] = request.page_size
        query["pageNumber"] = request.page_number
        query["nodepool_id"] = request.nodepool_id
        query["state"] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cs20151215_models.DescribeClusterNodesResponse().from_map(self.do_roarequest("DescribeClusterNodes", "2015-12-15", "HTTPS", "GET", "AK", "/clusters/" + str(cluster_id) + "/nodes", "json", req, runtime))

    def describe_cluster_resources(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.describe_cluster_resources_with_options(cluster_id, request, headers, runtime)

    def describe_cluster_resources_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cs20151215_models.DescribeClusterResourcesResponse().from_map(self.do_roarequest("DescribeClusterResources", "2015-12-15", "HTTPS", "GET", "AK", "/clusters/" + str(cluster_id) + "/resources", "array", req, runtime))

    def describe_cluster_user_kubeconfig(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.describe_cluster_user_kubeconfig_with_options(cluster_id, request, headers, runtime)

    def describe_cluster_user_kubeconfig_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        query["PrivateIpAddress"] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cs20151215_models.DescribeClusterUserKubeconfigResponse().from_map(self.do_roarequest("DescribeClusterUserKubeconfig", "2015-12-15", "HTTPS", "GET", "AK", "/k8s/" + str(cluster_id) + "/user_config", "json", req, runtime))

    def describe_cluster_v2user_kubeconfig(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.describe_cluster_v2user_kubeconfig_with_options(cluster_id, request, headers, runtime)

    def describe_cluster_v2user_kubeconfig_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        query["PrivateIpAddress"] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cs20151215_models.DescribeClusterV2UserKubeconfigResponse().from_map(self.do_roarequest("DescribeClusterV2UserKubeconfig", "2015-12-15", "HTTPS", "GET", "AK", "/api/v2/k8s/" + str(cluster_id) + "/user_config", "json", req, runtime))

    def describe_clusters(self, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.describe_clusters_with_options(request, headers, runtime)

    def describe_clusters_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        query["name"] = request.name
        query["clusterType"] = request.cluster_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cs20151215_models.DescribeClustersResponse().from_map(self.do_roarequest("DescribeClusters", "2015-12-15", "HTTPS", "GET", "AK", "/clusters", "array", req, runtime))

    def describe_clusters_v1(self, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.describe_clusters_v1with_options(request, headers, runtime)

    def describe_clusters_v1with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        query["Name"] = request.name
        query["ClusterType"] = request.cluster_type
        query["page_size"] = request.page_size
        query["page_number"] = request.page_number
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cs20151215_models.DescribeClustersV1Response().from_map(self.do_roarequest("DescribeClustersV1", "2015-12-15", "HTTPS", "GET", "AK", "/api/v1/clusters", "json", req, runtime))

    def describe_external_agent(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.describe_external_agent_with_options(cluster_id, request, headers, runtime)

    def describe_external_agent_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cs20151215_models.DescribeExternalAgentResponse().from_map(self.do_roarequest("DescribeExternalAgent", "2015-12-15", "HTTPS", "GET", "AK", "/k8s/" + str(cluster_id) + "/external/agent/deployment", "json", req, runtime))

    def describe_templates(self, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.describe_templates_with_options(request, headers, runtime)

    def describe_templates_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        query["template_type"] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cs20151215_models.DescribeTemplatesResponse().from_map(self.do_roarequest("DescribeTemplates", "2015-12-15", "HTTPS", "GET", "AK", "/templates", "json", req, runtime))

    def describe_user_quota(self):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.describe_user_quota_with_options(headers, runtime)

    def describe_user_quota_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cs20151215_models.DescribeUserQuotaResponse().from_map(self.do_roarequest("DescribeUserQuota", "2015-12-15", "HTTPS", "GET", "AK", "/quota", "json", req, runtime))

    def get_kubernetes_trigger(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.get_kubernetes_trigger_with_options(cluster_id, request, headers, runtime)

    def get_kubernetes_trigger_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        query["Namespace"] = request.namespace
        query["Type"] = request.type
        query["Name"] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return cs20151215_models.GetKubernetesTriggerResponse().from_map(self.do_roarequest("GetKubernetesTrigger", "2015-12-15", "HTTPS", "GET", "AK", "/triggers/" + str(cluster_id) + "", "json", req, runtime))

    def get_upgrade_status(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.get_upgrade_status_with_options(cluster_id, request, headers, runtime)

    def get_upgrade_status_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cs20151215_models.GetUpgradeStatusResponse().from_map(self.do_roarequest("GetUpgradeStatus", "2015-12-15", "HTTPS", "GET", "AK", "/api/v2/clusters/" + str(cluster_id) + "/upgrade/status", "json", req, runtime))

    def install_cluster_addons(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.install_cluster_addons_with_options(cluster_id, request, headers, runtime)

    def install_cluster_addons_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        return cs20151215_models.InstallClusterAddonsResponse().from_map(self.do_roarequest("InstallClusterAddons", "2015-12-15", "HTTPS", "POST", "AK", "/clusters/" + str(cluster_id) + "/components/install", "none", req, runtime))

    def modify_cluster(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.modify_cluster_with_options(cluster_id, request, headers, runtime)

    def modify_cluster_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        body["deletion_protection"] = request.deletion_protection
        body["ingress_loadbalancer_id"] = request.ingress_loadbalancer_id
        body["api_server_eip"] = request.api_server_eip
        body["api_server_eip_id"] = request.api_server_eip_id
        body["resource_group_id"] = request.resource_group_id
        body["ingress_domain_rebinding"] = request.ingress_domain_rebinding
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=body
        )
        return cs20151215_models.ModifyClusterResponse().from_map(self.do_roarequest_with_form("ModifyCluster", "2015-12-15", "HTTPS", "PUT", "AK", "/api/v2/clusters/" + str(cluster_id) + "", "json", req, runtime))

    def modify_cluster_configuration(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.modify_cluster_configuration_with_options(cluster_id, request, headers, runtime)

    def modify_cluster_configuration_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        body["customize_config"] = request.customize_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=body
        )
        return cs20151215_models.ModifyClusterConfigurationResponse().from_map(self.do_roarequest_with_form("ModifyClusterConfiguration", "2015-12-15", "HTTPS", "PUT", "AK", "/clusters/" + str(cluster_id) + "/configuration", "none", req, runtime))

    def modify_cluster_tags(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.modify_cluster_tags_with_options(cluster_id, request, headers, runtime)

    def modify_cluster_tags_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        return cs20151215_models.ModifyClusterTagsResponse().from_map(self.do_roarequest("ModifyClusterTags", "2015-12-15", "HTTPS", "POST", "AK", "/clusters/" + str(cluster_id) + "/tags", "none", req, runtime))

    def pause_component_upgrade(self, clusterid, componentid, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.pause_component_upgrade_with_options(clusterid, componentid, request, headers, runtime)

    def pause_component_upgrade_with_options(self, clusterid, componentid, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cs20151215_models.PauseComponentUpgradeResponse().from_map(self.do_roarequest("PauseComponentUpgrade", "2015-12-15", "HTTPS", "POST", "AK", "/clusters/" + str(clusterid) + "/components/{componentid}/pause", "none", req, runtime))

    def remove_cluster_nodes(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.remove_cluster_nodes_with_options(cluster_id, request, headers, runtime)

    def remove_cluster_nodes_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        body["release_node"] = request.release_node
        body["drain_node"] = request.drain_node
        body["nodes"] = request.nodes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=body
        )
        return cs20151215_models.RemoveClusterNodesResponse().from_map(self.do_roarequest_with_form("RemoveClusterNodes", "2015-12-15", "HTTPS", "POST", "AK", "/api/v2/clusters/" + str(cluster_id) + "/nodes/remove", "none", req, runtime))

    def resume_component_upgrade(self, clusterid, componentid, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.resume_component_upgrade_with_options(clusterid, componentid, request, headers, runtime)

    def resume_component_upgrade_with_options(self, clusterid, componentid, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return cs20151215_models.ResumeComponentUpgradeResponse().from_map(self.do_roarequest("ResumeComponentUpgrade", "2015-12-15", "HTTPS", "POST", "AK", "/clusters/" + str(clusterid) + "/components/{componentid}/resume", "none", req, runtime))

    def scale_cluster(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.scale_cluster_with_options(cluster_id, request, headers, runtime)

    def scale_cluster_with_options(self, cluster_id, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = cs20151215_models.ScaleClusterShrinkRequest(

        )
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.taints):
            request.taints_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.taints, "taints", "json")
        body = {}
        body["count"] = request.count
        body["key_pair"] = request.key_pair
        body["login_password"] = request.login_password
        body["worker_data_disk"] = request.worker_data_disk
        body["worker_instance_types"] = request.worker_instance_types
        body["worker_instance_charge_type"] = request.worker_instance_charge_type
        body["worker_period"] = request.worker_period
        body["worker_period_unit"] = request.worker_period_unit
        body["worker_auto_renew"] = request.worker_auto_renew
        body["worker_auto_renew_period"] = request.worker_auto_renew_period
        body["worker_system_disk_category"] = request.worker_system_disk_category
        body["worker_system_disk_size"] = request.worker_system_disk_size
        body["cloud_monitor_flags"] = request.cloud_monitor_flags
        body["cpu_policy"] = request.cpu_policy
        body["disable_rollback"] = request.disable_rollback
        body["vswitch_ids"] = request.vswitch_ids
        body["worker_data_disks"] = request.worker_data_disks
        body["tags"] = request.tags
        body["taints"] = request.taints_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=body
        )
        return cs20151215_models.ScaleClusterResponse().from_map(self.do_roarequest_with_form("ScaleCluster", "2015-12-15", "HTTPS", "PUT", "AK", "/clusters/" + str(cluster_id) + "", "json", req, runtime))

    def scale_out_cluster(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.scale_out_cluster_with_options(cluster_id, request, headers, runtime)

    def scale_out_cluster_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        body["count"] = request.count
        body["worker_instance_charge_type"] = request.worker_instance_charge_type
        body["worker_period"] = request.worker_period
        body["worker_period_unit"] = request.worker_period_unit
        body["worker_auto_renew"] = request.worker_auto_renew
        body["worker_auto_renew_period"] = request.worker_auto_renew_period
        body["worker_system_disk_category"] = request.worker_system_disk_category
        body["worker_system_disk_size"] = request.worker_system_disk_size
        body["worker_data_disk"] = request.worker_data_disk
        body["key_pair"] = request.key_pair
        body["login_password"] = request.login_password
        body["cloud_monitor_flags"] = request.cloud_monitor_flags
        body["cpu_policy"] = request.cpu_policy
        body["disable_rollback"] = request.disable_rollback
        body["image_id"] = request.image_id
        body["user_data"] = request.user_data
        body["runtime"] = request.runtime
        body["vswitch_ids"] = request.vswitch_ids
        body["worker_instance_types"] = request.worker_instance_types
        body["rds_instances"] = request.rds_instances
        body["worker_data_disks"] = request.worker_data_disks
        body["tags"] = request.tags
        body["taints"] = request.taints
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=body
        )
        return cs20151215_models.ScaleOutClusterResponse().from_map(self.do_roarequest_with_form("ScaleOutCluster", "2015-12-15", "HTTPS", "POST", "AK", "/api/v2/clusters/" + str(cluster_id) + "", "json", req, runtime))

    def un_install_cluster_addons(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.un_install_cluster_addons_with_options(cluster_id, request, headers, runtime)

    def un_install_cluster_addons_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        body["addons"] = request.addons
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=body
        )
        return cs20151215_models.UnInstallClusterAddonsResponse().from_map(self.do_roarequest_with_form("UnInstallClusterAddons", "2015-12-15", "HTTPS", "POST", "AK", "/clusters/" + str(cluster_id) + "/components/uninstall", "none", req, runtime))

    def update_template(self, template_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.update_template_with_options(template_id, request, headers, runtime)

    def update_template_with_options(self, template_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        body["name"] = request.name
        body["template"] = request.template
        body["tags"] = request.tags
        body["description"] = request.description
        body["template_type"] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=body
        )
        return cs20151215_models.UpdateTemplateResponse().from_map(self.do_roarequest_with_form("UpdateTemplate", "2015-12-15", "HTTPS", "PUT", "AK", "/templates/" + str(template_id) + "", "none", req, runtime))

    def upgrade_cluster(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.upgrade_cluster_with_options(cluster_id, request, headers, runtime)

    def upgrade_cluster_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        body["component_name"] = request.component_name
        body["version"] = request.version
        body["next_version"] = request.next_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=body
        )
        return cs20151215_models.UpgradeClusterResponse().from_map(self.do_roarequest_with_form("UpgradeCluster", "2015-12-15", "HTTPS", "POST", "AK", "/api/v2/clusters/" + str(cluster_id) + "/upgrade", "none", req, runtime))

    def upgrade_cluster_addons(self, cluster_id, request):
        runtime = util_models.RuntimeOptions(

        )
        headers = {}
        return self.upgrade_cluster_addons_with_options(cluster_id, request, headers, runtime)

    def upgrade_cluster_addons_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        return cs20151215_models.UpgradeClusterAddonsResponse().from_map(self.do_roarequest("UpgradeClusterAddons", "2015-12-15", "HTTPS", "POST", "AK", "/clusters/" + str(cluster_id) + "/components/upgrade", "none", req, runtime))
