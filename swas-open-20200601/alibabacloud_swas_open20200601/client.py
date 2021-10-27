# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_swas_open20200601 import models as swas__open20200601_models
from alibabacloud_tea_util import models as util_models


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
        self._endpoint = self.get_endpoint('swas-open', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_custom_image_with_options(
        self,
        request: swas__open20200601_models.CreateCustomImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateCustomImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateCustomImageResponse(),
            self.do_rpcrequest('CreateCustomImage', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_custom_image_with_options_async(
        self,
        request: swas__open20200601_models.CreateCustomImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateCustomImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateCustomImageResponse(),
            await self.do_rpcrequest_async('CreateCustomImage', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_custom_image(
        self,
        request: swas__open20200601_models.CreateCustomImageRequest,
    ) -> swas__open20200601_models.CreateCustomImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_custom_image_with_options(request, runtime)

    async def create_custom_image_async(
        self,
        request: swas__open20200601_models.CreateCustomImageRequest,
    ) -> swas__open20200601_models.CreateCustomImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_custom_image_with_options_async(request, runtime)

    def create_firewall_rule_with_options(
        self,
        request: swas__open20200601_models.CreateFirewallRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateFirewallRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateFirewallRuleResponse(),
            self.do_rpcrequest('CreateFirewallRule', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_firewall_rule_with_options_async(
        self,
        request: swas__open20200601_models.CreateFirewallRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateFirewallRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateFirewallRuleResponse(),
            await self.do_rpcrequest_async('CreateFirewallRule', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_firewall_rule(
        self,
        request: swas__open20200601_models.CreateFirewallRuleRequest,
    ) -> swas__open20200601_models.CreateFirewallRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_firewall_rule_with_options(request, runtime)

    async def create_firewall_rule_async(
        self,
        request: swas__open20200601_models.CreateFirewallRuleRequest,
    ) -> swas__open20200601_models.CreateFirewallRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_firewall_rule_with_options_async(request, runtime)

    def create_instances_with_options(
        self,
        request: swas__open20200601_models.CreateInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateInstancesResponse(),
            self.do_rpcrequest('CreateInstances', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_instances_with_options_async(
        self,
        request: swas__open20200601_models.CreateInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateInstancesResponse(),
            await self.do_rpcrequest_async('CreateInstances', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_instances(
        self,
        request: swas__open20200601_models.CreateInstancesRequest,
    ) -> swas__open20200601_models.CreateInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instances_with_options(request, runtime)

    async def create_instances_async(
        self,
        request: swas__open20200601_models.CreateInstancesRequest,
    ) -> swas__open20200601_models.CreateInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instances_with_options_async(request, runtime)

    def create_snapshot_with_options(
        self,
        request: swas__open20200601_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateSnapshotResponse(),
            self.do_rpcrequest('CreateSnapshot', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_snapshot_with_options_async(
        self,
        request: swas__open20200601_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateSnapshotResponse(),
            await self.do_rpcrequest_async('CreateSnapshot', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_snapshot(
        self,
        request: swas__open20200601_models.CreateSnapshotRequest,
    ) -> swas__open20200601_models.CreateSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_snapshot_with_options(request, runtime)

    async def create_snapshot_async(
        self,
        request: swas__open20200601_models.CreateSnapshotRequest,
    ) -> swas__open20200601_models.CreateSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_snapshot_with_options_async(request, runtime)

    def delete_custom_image_with_options(
        self,
        request: swas__open20200601_models.DeleteCustomImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteCustomImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteCustomImageResponse(),
            self.do_rpcrequest('DeleteCustomImage', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_custom_image_with_options_async(
        self,
        request: swas__open20200601_models.DeleteCustomImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteCustomImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteCustomImageResponse(),
            await self.do_rpcrequest_async('DeleteCustomImage', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_custom_image(
        self,
        request: swas__open20200601_models.DeleteCustomImageRequest,
    ) -> swas__open20200601_models.DeleteCustomImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_image_with_options(request, runtime)

    async def delete_custom_image_async(
        self,
        request: swas__open20200601_models.DeleteCustomImageRequest,
    ) -> swas__open20200601_models.DeleteCustomImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_image_with_options_async(request, runtime)

    def delete_firewall_rule_with_options(
        self,
        request: swas__open20200601_models.DeleteFirewallRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteFirewallRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteFirewallRuleResponse(),
            self.do_rpcrequest('DeleteFirewallRule', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_firewall_rule_with_options_async(
        self,
        request: swas__open20200601_models.DeleteFirewallRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteFirewallRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteFirewallRuleResponse(),
            await self.do_rpcrequest_async('DeleteFirewallRule', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_firewall_rule(
        self,
        request: swas__open20200601_models.DeleteFirewallRuleRequest,
    ) -> swas__open20200601_models.DeleteFirewallRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_firewall_rule_with_options(request, runtime)

    async def delete_firewall_rule_async(
        self,
        request: swas__open20200601_models.DeleteFirewallRuleRequest,
    ) -> swas__open20200601_models.DeleteFirewallRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_firewall_rule_with_options_async(request, runtime)

    def delete_snapshot_with_options(
        self,
        request: swas__open20200601_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteSnapshotResponse(),
            self.do_rpcrequest('DeleteSnapshot', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_snapshot_with_options_async(
        self,
        request: swas__open20200601_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteSnapshotResponse(),
            await self.do_rpcrequest_async('DeleteSnapshot', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_snapshot(
        self,
        request: swas__open20200601_models.DeleteSnapshotRequest,
    ) -> swas__open20200601_models.DeleteSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_with_options(request, runtime)

    async def delete_snapshot_async(
        self,
        request: swas__open20200601_models.DeleteSnapshotRequest,
    ) -> swas__open20200601_models.DeleteSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_snapshot_with_options_async(request, runtime)

    def list_disks_with_options(
        self,
        request: swas__open20200601_models.ListDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListDisksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListDisksResponse(),
            self.do_rpcrequest('ListDisks', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_disks_with_options_async(
        self,
        request: swas__open20200601_models.ListDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListDisksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListDisksResponse(),
            await self.do_rpcrequest_async('ListDisks', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_disks(
        self,
        request: swas__open20200601_models.ListDisksRequest,
    ) -> swas__open20200601_models.ListDisksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_disks_with_options(request, runtime)

    async def list_disks_async(
        self,
        request: swas__open20200601_models.ListDisksRequest,
    ) -> swas__open20200601_models.ListDisksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_disks_with_options_async(request, runtime)

    def list_firewall_rules_with_options(
        self,
        request: swas__open20200601_models.ListFirewallRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListFirewallRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListFirewallRulesResponse(),
            self.do_rpcrequest('ListFirewallRules', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_firewall_rules_with_options_async(
        self,
        request: swas__open20200601_models.ListFirewallRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListFirewallRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListFirewallRulesResponse(),
            await self.do_rpcrequest_async('ListFirewallRules', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_firewall_rules(
        self,
        request: swas__open20200601_models.ListFirewallRulesRequest,
    ) -> swas__open20200601_models.ListFirewallRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_firewall_rules_with_options(request, runtime)

    async def list_firewall_rules_async(
        self,
        request: swas__open20200601_models.ListFirewallRulesRequest,
    ) -> swas__open20200601_models.ListFirewallRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_firewall_rules_with_options_async(request, runtime)

    def list_images_with_options(
        self,
        request: swas__open20200601_models.ListImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListImagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListImagesResponse(),
            self.do_rpcrequest('ListImages', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_images_with_options_async(
        self,
        request: swas__open20200601_models.ListImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListImagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListImagesResponse(),
            await self.do_rpcrequest_async('ListImages', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_images(
        self,
        request: swas__open20200601_models.ListImagesRequest,
    ) -> swas__open20200601_models.ListImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_images_with_options(request, runtime)

    async def list_images_async(
        self,
        request: swas__open20200601_models.ListImagesRequest,
    ) -> swas__open20200601_models.ListImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_images_with_options_async(request, runtime)

    def list_instance_plans_modification_with_options(
        self,
        request: swas__open20200601_models.ListInstancePlansModificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListInstancePlansModificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListInstancePlansModificationResponse(),
            self.do_rpcrequest('ListInstancePlansModification', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_instance_plans_modification_with_options_async(
        self,
        request: swas__open20200601_models.ListInstancePlansModificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListInstancePlansModificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListInstancePlansModificationResponse(),
            await self.do_rpcrequest_async('ListInstancePlansModification', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_instance_plans_modification(
        self,
        request: swas__open20200601_models.ListInstancePlansModificationRequest,
    ) -> swas__open20200601_models.ListInstancePlansModificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instance_plans_modification_with_options(request, runtime)

    async def list_instance_plans_modification_async(
        self,
        request: swas__open20200601_models.ListInstancePlansModificationRequest,
    ) -> swas__open20200601_models.ListInstancePlansModificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_plans_modification_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: swas__open20200601_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListInstancesResponse(),
            self.do_rpcrequest('ListInstances', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: swas__open20200601_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListInstancesResponse(),
            await self.do_rpcrequest_async('ListInstances', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_instances(
        self,
        request: swas__open20200601_models.ListInstancesRequest,
    ) -> swas__open20200601_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: swas__open20200601_models.ListInstancesRequest,
    ) -> swas__open20200601_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def list_instances_traffic_packages_with_options(
        self,
        request: swas__open20200601_models.ListInstancesTrafficPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListInstancesTrafficPackagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListInstancesTrafficPackagesResponse(),
            self.do_rpcrequest('ListInstancesTrafficPackages', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_instances_traffic_packages_with_options_async(
        self,
        request: swas__open20200601_models.ListInstancesTrafficPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListInstancesTrafficPackagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListInstancesTrafficPackagesResponse(),
            await self.do_rpcrequest_async('ListInstancesTrafficPackages', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_instances_traffic_packages(
        self,
        request: swas__open20200601_models.ListInstancesTrafficPackagesRequest,
    ) -> swas__open20200601_models.ListInstancesTrafficPackagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instances_traffic_packages_with_options(request, runtime)

    async def list_instances_traffic_packages_async(
        self,
        request: swas__open20200601_models.ListInstancesTrafficPackagesRequest,
    ) -> swas__open20200601_models.ListInstancesTrafficPackagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_traffic_packages_with_options_async(request, runtime)

    def list_plans_with_options(
        self,
        request: swas__open20200601_models.ListPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListPlansResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListPlansResponse(),
            self.do_rpcrequest('ListPlans', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_plans_with_options_async(
        self,
        request: swas__open20200601_models.ListPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListPlansResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListPlansResponse(),
            await self.do_rpcrequest_async('ListPlans', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_plans(
        self,
        request: swas__open20200601_models.ListPlansRequest,
    ) -> swas__open20200601_models.ListPlansResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_plans_with_options(request, runtime)

    async def list_plans_async(
        self,
        request: swas__open20200601_models.ListPlansRequest,
    ) -> swas__open20200601_models.ListPlansResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_plans_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListRegionsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            swas__open20200601_models.ListRegionsResponse(),
            self.do_rpcrequest('ListRegions', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListRegionsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            swas__open20200601_models.ListRegionsResponse(),
            await self.do_rpcrequest_async('ListRegions', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_regions(self) -> swas__open20200601_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(runtime)

    async def list_regions_async(self) -> swas__open20200601_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_regions_with_options_async(runtime)

    def list_snapshots_with_options(
        self,
        request: swas__open20200601_models.ListSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListSnapshotsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListSnapshotsResponse(),
            self.do_rpcrequest('ListSnapshots', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_snapshots_with_options_async(
        self,
        request: swas__open20200601_models.ListSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListSnapshotsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListSnapshotsResponse(),
            await self.do_rpcrequest_async('ListSnapshots', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_snapshots(
        self,
        request: swas__open20200601_models.ListSnapshotsRequest,
    ) -> swas__open20200601_models.ListSnapshotsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_snapshots_with_options(request, runtime)

    async def list_snapshots_async(
        self,
        request: swas__open20200601_models.ListSnapshotsRequest,
    ) -> swas__open20200601_models.ListSnapshotsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_snapshots_with_options_async(request, runtime)

    def modify_image_share_status_with_options(
        self,
        request: swas__open20200601_models.ModifyImageShareStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ModifyImageShareStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ModifyImageShareStatusResponse(),
            self.do_rpcrequest('ModifyImageShareStatus', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_image_share_status_with_options_async(
        self,
        request: swas__open20200601_models.ModifyImageShareStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ModifyImageShareStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ModifyImageShareStatusResponse(),
            await self.do_rpcrequest_async('ModifyImageShareStatus', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_image_share_status(
        self,
        request: swas__open20200601_models.ModifyImageShareStatusRequest,
    ) -> swas__open20200601_models.ModifyImageShareStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_image_share_status_with_options(request, runtime)

    async def modify_image_share_status_async(
        self,
        request: swas__open20200601_models.ModifyImageShareStatusRequest,
    ) -> swas__open20200601_models.ModifyImageShareStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_image_share_status_with_options_async(request, runtime)

    def reboot_instance_with_options(
        self,
        request: swas__open20200601_models.RebootInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RebootInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.RebootInstanceResponse(),
            self.do_rpcrequest('RebootInstance', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reboot_instance_with_options_async(
        self,
        request: swas__open20200601_models.RebootInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RebootInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.RebootInstanceResponse(),
            await self.do_rpcrequest_async('RebootInstance', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reboot_instance(
        self,
        request: swas__open20200601_models.RebootInstanceRequest,
    ) -> swas__open20200601_models.RebootInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.reboot_instance_with_options(request, runtime)

    async def reboot_instance_async(
        self,
        request: swas__open20200601_models.RebootInstanceRequest,
    ) -> swas__open20200601_models.RebootInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reboot_instance_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: swas__open20200601_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.RenewInstanceResponse(),
            self.do_rpcrequest('RenewInstance', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: swas__open20200601_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.RenewInstanceResponse(),
            await self.do_rpcrequest_async('RenewInstance', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_instance(
        self,
        request: swas__open20200601_models.RenewInstanceRequest,
    ) -> swas__open20200601_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    async def renew_instance_async(
        self,
        request: swas__open20200601_models.RenewInstanceRequest,
    ) -> swas__open20200601_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_instance_with_options_async(request, runtime)

    def reset_disk_with_options(
        self,
        request: swas__open20200601_models.ResetDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ResetDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ResetDiskResponse(),
            self.do_rpcrequest('ResetDisk', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_disk_with_options_async(
        self,
        request: swas__open20200601_models.ResetDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ResetDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ResetDiskResponse(),
            await self.do_rpcrequest_async('ResetDisk', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_disk(
        self,
        request: swas__open20200601_models.ResetDiskRequest,
    ) -> swas__open20200601_models.ResetDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_disk_with_options(request, runtime)

    async def reset_disk_async(
        self,
        request: swas__open20200601_models.ResetDiskRequest,
    ) -> swas__open20200601_models.ResetDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_disk_with_options_async(request, runtime)

    def reset_system_with_options(
        self,
        request: swas__open20200601_models.ResetSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ResetSystemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ResetSystemResponse(),
            self.do_rpcrequest('ResetSystem', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_system_with_options_async(
        self,
        request: swas__open20200601_models.ResetSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ResetSystemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ResetSystemResponse(),
            await self.do_rpcrequest_async('ResetSystem', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_system(
        self,
        request: swas__open20200601_models.ResetSystemRequest,
    ) -> swas__open20200601_models.ResetSystemResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_system_with_options(request, runtime)

    async def reset_system_async(
        self,
        request: swas__open20200601_models.ResetSystemRequest,
    ) -> swas__open20200601_models.ResetSystemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_system_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        request: swas__open20200601_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StartInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.StartInstanceResponse(),
            self.do_rpcrequest('StartInstance', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        request: swas__open20200601_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StartInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.StartInstanceResponse(),
            await self.do_rpcrequest_async('StartInstance', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_instance(
        self,
        request: swas__open20200601_models.StartInstanceRequest,
    ) -> swas__open20200601_models.StartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    async def start_instance_async(
        self,
        request: swas__open20200601_models.StartInstanceRequest,
    ) -> swas__open20200601_models.StartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_instance_with_options_async(request, runtime)

    def stop_instance_with_options(
        self,
        request: swas__open20200601_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StopInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.StopInstanceResponse(),
            self.do_rpcrequest('StopInstance', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_instance_with_options_async(
        self,
        request: swas__open20200601_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StopInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.StopInstanceResponse(),
            await self.do_rpcrequest_async('StopInstance', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_instance(
        self,
        request: swas__open20200601_models.StopInstanceRequest,
    ) -> swas__open20200601_models.StopInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    async def stop_instance_async(
        self,
        request: swas__open20200601_models.StopInstanceRequest,
    ) -> swas__open20200601_models.StopInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_instance_with_options_async(request, runtime)

    def update_instance_attribute_with_options(
        self,
        request: swas__open20200601_models.UpdateInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.UpdateInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.UpdateInstanceAttributeResponse(),
            self.do_rpcrequest('UpdateInstanceAttribute', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_instance_attribute_with_options_async(
        self,
        request: swas__open20200601_models.UpdateInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.UpdateInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.UpdateInstanceAttributeResponse(),
            await self.do_rpcrequest_async('UpdateInstanceAttribute', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_instance_attribute(
        self,
        request: swas__open20200601_models.UpdateInstanceAttributeRequest,
    ) -> swas__open20200601_models.UpdateInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_instance_attribute_with_options(request, runtime)

    async def update_instance_attribute_async(
        self,
        request: swas__open20200601_models.UpdateInstanceAttributeRequest,
    ) -> swas__open20200601_models.UpdateInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_attribute_with_options_async(request, runtime)

    def upgrade_instance_with_options(
        self,
        request: swas__open20200601_models.UpgradeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.UpgradeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.UpgradeInstanceResponse(),
            self.do_rpcrequest('UpgradeInstance', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_instance_with_options_async(
        self,
        request: swas__open20200601_models.UpgradeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.UpgradeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.UpgradeInstanceResponse(),
            await self.do_rpcrequest_async('UpgradeInstance', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_instance(
        self,
        request: swas__open20200601_models.UpgradeInstanceRequest,
    ) -> swas__open20200601_models.UpgradeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_instance_with_options(request, runtime)

    async def upgrade_instance_async(
        self,
        request: swas__open20200601_models.UpgradeInstanceRequest,
    ) -> swas__open20200601_models.UpgradeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_instance_with_options_async(request, runtime)
