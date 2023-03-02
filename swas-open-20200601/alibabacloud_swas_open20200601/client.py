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

    def allocate_public_connection_with_options(
        self,
        request: swas__open20200601_models.AllocatePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.AllocatePublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocatePublicConnection',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.AllocatePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_public_connection_with_options_async(
        self,
        request: swas__open20200601_models.AllocatePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.AllocatePublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocatePublicConnection',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.AllocatePublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_public_connection(
        self,
        request: swas__open20200601_models.AllocatePublicConnectionRequest,
    ) -> swas__open20200601_models.AllocatePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_public_connection_with_options(request, runtime)

    async def allocate_public_connection_async(
        self,
        request: swas__open20200601_models.AllocatePublicConnectionRequest,
    ) -> swas__open20200601_models.AllocatePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_public_connection_with_options_async(request, runtime)

    def create_custom_image_with_options(
        self,
        request: swas__open20200601_models.CreateCustomImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateCustomImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_snapshot_id):
            query['DataSnapshotId'] = request.data_snapshot_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.system_snapshot_id):
            query['SystemSnapshotId'] = request.system_snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomImage',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateCustomImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_image_with_options_async(
        self,
        request: swas__open20200601_models.CreateCustomImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateCustomImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_snapshot_id):
            query['DataSnapshotId'] = request.data_snapshot_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.system_snapshot_id):
            query['SystemSnapshotId'] = request.system_snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomImage',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateCustomImageResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.rule_protocol):
            query['RuleProtocol'] = request.rule_protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFirewallRule',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateFirewallRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_firewall_rule_with_options_async(
        self,
        request: swas__open20200601_models.CreateFirewallRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateFirewallRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.rule_protocol):
            query['RuleProtocol'] = request.rule_protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFirewallRule',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateFirewallRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_disk_size):
            query['DataDiskSize'] = request.data_disk_size
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstances',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instances_with_options_async(
        self,
        request: swas__open20200601_models.CreateInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_disk_size):
            query['DataDiskSize'] = request.data_disk_size
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstances',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateInstancesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSnapshot',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_snapshot_with_options_async(
        self,
        request: swas__open20200601_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSnapshot',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomImage',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteCustomImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_image_with_options_async(
        self,
        request: swas__open20200601_models.DeleteCustomImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteCustomImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomImage',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteCustomImageResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFirewallRule',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteFirewallRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_firewall_rule_with_options_async(
        self,
        request: swas__open20200601_models.DeleteFirewallRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteFirewallRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFirewallRule',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteFirewallRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_snapshot_with_options_async(
        self,
        request: swas__open20200601_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_cloud_assistant_status_with_options(
        self,
        tmp_req: swas__open20200601_models.DescribeCloudAssistantStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeCloudAssistantStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = swas__open20200601_models.DescribeCloudAssistantStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudAssistantStatus',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeCloudAssistantStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_assistant_status_with_options_async(
        self,
        tmp_req: swas__open20200601_models.DescribeCloudAssistantStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeCloudAssistantStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = swas__open20200601_models.DescribeCloudAssistantStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudAssistantStatus',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeCloudAssistantStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_assistant_status(
        self,
        request: swas__open20200601_models.DescribeCloudAssistantStatusRequest,
    ) -> swas__open20200601_models.DescribeCloudAssistantStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_assistant_status_with_options(request, runtime)

    async def describe_cloud_assistant_status_async(
        self,
        request: swas__open20200601_models.DescribeCloudAssistantStatusRequest,
    ) -> swas__open20200601_models.DescribeCloudAssistantStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_assistant_status_with_options_async(request, runtime)

    def describe_database_error_logs_with_options(
        self,
        request: swas__open20200601_models.DescribeDatabaseErrorLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseErrorLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabaseErrorLogs',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeDatabaseErrorLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_database_error_logs_with_options_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseErrorLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseErrorLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabaseErrorLogs',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeDatabaseErrorLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_database_error_logs(
        self,
        request: swas__open20200601_models.DescribeDatabaseErrorLogsRequest,
    ) -> swas__open20200601_models.DescribeDatabaseErrorLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_database_error_logs_with_options(request, runtime)

    async def describe_database_error_logs_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseErrorLogsRequest,
    ) -> swas__open20200601_models.DescribeDatabaseErrorLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_database_error_logs_with_options_async(request, runtime)

    def describe_database_instance_metric_data_with_options(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstanceMetricDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseInstanceMetricDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabaseInstanceMetricData',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeDatabaseInstanceMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_database_instance_metric_data_with_options_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstanceMetricDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseInstanceMetricDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabaseInstanceMetricData',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeDatabaseInstanceMetricDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_database_instance_metric_data(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstanceMetricDataRequest,
    ) -> swas__open20200601_models.DescribeDatabaseInstanceMetricDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_database_instance_metric_data_with_options(request, runtime)

    async def describe_database_instance_metric_data_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstanceMetricDataRequest,
    ) -> swas__open20200601_models.DescribeDatabaseInstanceMetricDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_database_instance_metric_data_with_options_async(request, runtime)

    def describe_database_instance_parameters_with_options(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstanceParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseInstanceParametersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabaseInstanceParameters',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeDatabaseInstanceParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_database_instance_parameters_with_options_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstanceParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseInstanceParametersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabaseInstanceParameters',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeDatabaseInstanceParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_database_instance_parameters(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstanceParametersRequest,
    ) -> swas__open20200601_models.DescribeDatabaseInstanceParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_database_instance_parameters_with_options(request, runtime)

    async def describe_database_instance_parameters_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstanceParametersRequest,
    ) -> swas__open20200601_models.DescribeDatabaseInstanceParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_database_instance_parameters_with_options_async(request, runtime)

    def describe_database_instances_with_options(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_instance_ids):
            query['DatabaseInstanceIds'] = request.database_instance_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabaseInstances',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeDatabaseInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_database_instances_with_options_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_instance_ids):
            query['DatabaseInstanceIds'] = request.database_instance_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabaseInstances',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeDatabaseInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_database_instances(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstancesRequest,
    ) -> swas__open20200601_models.DescribeDatabaseInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_database_instances_with_options(request, runtime)

    async def describe_database_instances_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstancesRequest,
    ) -> swas__open20200601_models.DescribeDatabaseInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_database_instances_with_options_async(request, runtime)

    def describe_database_slow_log_records_with_options(
        self,
        request: swas__open20200601_models.DescribeDatabaseSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseSlowLogRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabaseSlowLogRecords',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeDatabaseSlowLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_database_slow_log_records_with_options_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseSlowLogRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabaseSlowLogRecords',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeDatabaseSlowLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_database_slow_log_records(
        self,
        request: swas__open20200601_models.DescribeDatabaseSlowLogRecordsRequest,
    ) -> swas__open20200601_models.DescribeDatabaseSlowLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_database_slow_log_records_with_options(request, runtime)

    async def describe_database_slow_log_records_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseSlowLogRecordsRequest,
    ) -> swas__open20200601_models.DescribeDatabaseSlowLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_database_slow_log_records_with_options_async(request, runtime)

    def describe_invocation_result_with_options(
        self,
        request: swas__open20200601_models.DescribeInvocationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeInvocationResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInvocationResult',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeInvocationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_invocation_result_with_options_async(
        self,
        request: swas__open20200601_models.DescribeInvocationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeInvocationResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInvocationResult',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeInvocationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_invocation_result(
        self,
        request: swas__open20200601_models.DescribeInvocationResultRequest,
    ) -> swas__open20200601_models.DescribeInvocationResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_invocation_result_with_options(request, runtime)

    async def describe_invocation_result_async(
        self,
        request: swas__open20200601_models.DescribeInvocationResultRequest,
    ) -> swas__open20200601_models.DescribeInvocationResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_invocation_result_with_options_async(request, runtime)

    def describe_invocations_with_options(
        self,
        request: swas__open20200601_models.DescribeInvocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeInvocationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.invoke_status):
            query['InvokeStatus'] = request.invoke_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInvocations',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeInvocationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_invocations_with_options_async(
        self,
        request: swas__open20200601_models.DescribeInvocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeInvocationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.invoke_status):
            query['InvokeStatus'] = request.invoke_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInvocations',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeInvocationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_invocations(
        self,
        request: swas__open20200601_models.DescribeInvocationsRequest,
    ) -> swas__open20200601_models.DescribeInvocationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_invocations_with_options(request, runtime)

    async def describe_invocations_async(
        self,
        request: swas__open20200601_models.DescribeInvocationsRequest,
    ) -> swas__open20200601_models.DescribeInvocationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_invocations_with_options_async(request, runtime)

    def install_cloud_assistant_with_options(
        self,
        tmp_req: swas__open20200601_models.InstallCloudAssistantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.InstallCloudAssistantResponse:
        UtilClient.validate_model(tmp_req)
        request = swas__open20200601_models.InstallCloudAssistantShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallCloudAssistant',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.InstallCloudAssistantResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_cloud_assistant_with_options_async(
        self,
        tmp_req: swas__open20200601_models.InstallCloudAssistantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.InstallCloudAssistantResponse:
        UtilClient.validate_model(tmp_req)
        request = swas__open20200601_models.InstallCloudAssistantShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallCloudAssistant',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.InstallCloudAssistantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_cloud_assistant(
        self,
        request: swas__open20200601_models.InstallCloudAssistantRequest,
    ) -> swas__open20200601_models.InstallCloudAssistantResponse:
        runtime = util_models.RuntimeOptions()
        return self.install_cloud_assistant_with_options(request, runtime)

    async def install_cloud_assistant_async(
        self,
        request: swas__open20200601_models.InstallCloudAssistantRequest,
    ) -> swas__open20200601_models.InstallCloudAssistantResponse:
        runtime = util_models.RuntimeOptions()
        return await self.install_cloud_assistant_with_options_async(request, runtime)

    def list_disks_with_options(
        self,
        request: swas__open20200601_models.ListDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListDisksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDisks',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListDisksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_disks_with_options_async(
        self,
        request: swas__open20200601_models.ListDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListDisksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDisks',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListDisksResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFirewallRules',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListFirewallRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_firewall_rules_with_options_async(
        self,
        request: swas__open20200601_models.ListFirewallRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListFirewallRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFirewallRules',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListFirewallRulesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.image_ids):
            query['ImageIds'] = request.image_ids
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_images_with_options_async(
        self,
        request: swas__open20200601_models.ListImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_ids):
            query['ImageIds'] = request.image_ids
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListImagesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancePlansModification',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListInstancePlansModificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_plans_modification_with_options_async(
        self,
        request: swas__open20200601_models.ListInstancePlansModificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListInstancePlansModificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancePlansModification',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListInstancePlansModificationResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.public_ip_addresses):
            query['PublicIpAddresses'] = request.public_ip_addresses
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: swas__open20200601_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.public_ip_addresses):
            query['PublicIpAddresses'] = request.public_ip_addresses
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancesTrafficPackages',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListInstancesTrafficPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_traffic_packages_with_options_async(
        self,
        request: swas__open20200601_models.ListInstancesTrafficPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListInstancesTrafficPackagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancesTrafficPackages',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListInstancesTrafficPackagesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPlans',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_plans_with_options_async(
        self,
        request: swas__open20200601_models.ListPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListPlansResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPlans',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListPlansResponse(),
            await self.call_api_async(params, req, runtime)
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
        params = open_api_models.Params(
            action='ListRegions',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegions',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_ids):
            query['SnapshotIds'] = request.snapshot_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSnapshots',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_snapshots_with_options_async(
        self,
        request: swas__open20200601_models.ListSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListSnapshotsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_ids):
            query['SnapshotIds'] = request.snapshot_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSnapshots',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListSnapshotsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def login_instance_with_options(
        self,
        request: swas__open20200601_models.LoginInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.LoginInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LoginInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.LoginInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def login_instance_with_options_async(
        self,
        request: swas__open20200601_models.LoginInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.LoginInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LoginInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.LoginInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def login_instance(
        self,
        request: swas__open20200601_models.LoginInstanceRequest,
    ) -> swas__open20200601_models.LoginInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.login_instance_with_options(request, runtime)

    async def login_instance_async(
        self,
        request: swas__open20200601_models.LoginInstanceRequest,
    ) -> swas__open20200601_models.LoginInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.login_instance_with_options_async(request, runtime)

    def modify_database_instance_description_with_options(
        self,
        request: swas__open20200601_models.ModifyDatabaseInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ModifyDatabaseInstanceDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_description):
            query['DatabaseInstanceDescription'] = request.database_instance_description
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDatabaseInstanceDescription',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ModifyDatabaseInstanceDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_database_instance_description_with_options_async(
        self,
        request: swas__open20200601_models.ModifyDatabaseInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ModifyDatabaseInstanceDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_description):
            query['DatabaseInstanceDescription'] = request.database_instance_description
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDatabaseInstanceDescription',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ModifyDatabaseInstanceDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_database_instance_description(
        self,
        request: swas__open20200601_models.ModifyDatabaseInstanceDescriptionRequest,
    ) -> swas__open20200601_models.ModifyDatabaseInstanceDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_database_instance_description_with_options(request, runtime)

    async def modify_database_instance_description_async(
        self,
        request: swas__open20200601_models.ModifyDatabaseInstanceDescriptionRequest,
    ) -> swas__open20200601_models.ModifyDatabaseInstanceDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_database_instance_description_with_options_async(request, runtime)

    def modify_database_instance_parameter_with_options(
        self,
        request: swas__open20200601_models.ModifyDatabaseInstanceParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ModifyDatabaseInstanceParameterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.force_restart):
            query['ForceRestart'] = request.force_restart
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDatabaseInstanceParameter',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ModifyDatabaseInstanceParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_database_instance_parameter_with_options_async(
        self,
        request: swas__open20200601_models.ModifyDatabaseInstanceParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ModifyDatabaseInstanceParameterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.force_restart):
            query['ForceRestart'] = request.force_restart
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDatabaseInstanceParameter',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ModifyDatabaseInstanceParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_database_instance_parameter(
        self,
        request: swas__open20200601_models.ModifyDatabaseInstanceParameterRequest,
    ) -> swas__open20200601_models.ModifyDatabaseInstanceParameterResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_database_instance_parameter_with_options(request, runtime)

    async def modify_database_instance_parameter_async(
        self,
        request: swas__open20200601_models.ModifyDatabaseInstanceParameterRequest,
    ) -> swas__open20200601_models.ModifyDatabaseInstanceParameterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_database_instance_parameter_with_options_async(request, runtime)

    def modify_image_share_status_with_options(
        self,
        request: swas__open20200601_models.ModifyImageShareStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ModifyImageShareStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyImageShareStatus',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ModifyImageShareStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_image_share_status_with_options_async(
        self,
        request: swas__open20200601_models.ModifyImageShareStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ModifyImageShareStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyImageShareStatus',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ModifyImageShareStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.RebootInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_instance_with_options_async(
        self,
        request: swas__open20200601_models.RebootInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RebootInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.RebootInstanceResponse(),
            await self.call_api_async(params, req, runtime)
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

    def release_public_connection_with_options(
        self,
        request: swas__open20200601_models.ReleasePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ReleasePublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleasePublicConnection',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ReleasePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_public_connection_with_options_async(
        self,
        request: swas__open20200601_models.ReleasePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ReleasePublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleasePublicConnection',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ReleasePublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_public_connection(
        self,
        request: swas__open20200601_models.ReleasePublicConnectionRequest,
    ) -> swas__open20200601_models.ReleasePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_public_connection_with_options(request, runtime)

    async def release_public_connection_async(
        self,
        request: swas__open20200601_models.ReleasePublicConnectionRequest,
    ) -> swas__open20200601_models.ReleasePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_public_connection_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: swas__open20200601_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: swas__open20200601_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.RenewInstanceResponse(),
            await self.call_api_async(params, req, runtime)
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

    def reset_database_account_password_with_options(
        self,
        request: swas__open20200601_models.ResetDatabaseAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ResetDatabaseAccountPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDatabaseAccountPassword',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ResetDatabaseAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_database_account_password_with_options_async(
        self,
        request: swas__open20200601_models.ResetDatabaseAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ResetDatabaseAccountPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDatabaseAccountPassword',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ResetDatabaseAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_database_account_password(
        self,
        request: swas__open20200601_models.ResetDatabaseAccountPasswordRequest,
    ) -> swas__open20200601_models.ResetDatabaseAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_database_account_password_with_options(request, runtime)

    async def reset_database_account_password_async(
        self,
        request: swas__open20200601_models.ResetDatabaseAccountPasswordRequest,
    ) -> swas__open20200601_models.ResetDatabaseAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_database_account_password_with_options_async(request, runtime)

    def reset_disk_with_options(
        self,
        request: swas__open20200601_models.ResetDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ResetDiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDisk',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ResetDiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_disk_with_options_async(
        self,
        request: swas__open20200601_models.ResetDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ResetDiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDisk',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ResetDiskResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetSystem',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ResetSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_system_with_options_async(
        self,
        request: swas__open20200601_models.ResetSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ResetSystemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetSystem',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ResetSystemResponse(),
            await self.call_api_async(params, req, runtime)
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

    def restart_database_instance_with_options(
        self,
        request: swas__open20200601_models.RestartDatabaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RestartDatabaseInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDatabaseInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.RestartDatabaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_database_instance_with_options_async(
        self,
        request: swas__open20200601_models.RestartDatabaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RestartDatabaseInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDatabaseInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.RestartDatabaseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_database_instance(
        self,
        request: swas__open20200601_models.RestartDatabaseInstanceRequest,
    ) -> swas__open20200601_models.RestartDatabaseInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_database_instance_with_options(request, runtime)

    async def restart_database_instance_async(
        self,
        request: swas__open20200601_models.RestartDatabaseInstanceRequest,
    ) -> swas__open20200601_models.RestartDatabaseInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_database_instance_with_options_async(request, runtime)

    def run_command_with_options(
        self,
        tmp_req: swas__open20200601_models.RunCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RunCommandResponse:
        UtilClient.validate_model(tmp_req)
        request = swas__open20200601_models.RunCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.command_content):
            query['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.enable_parameter):
            query['EnableParameter'] = request.enable_parameter
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.windows_password_name):
            query['WindowsPasswordName'] = request.windows_password_name
        if not UtilClient.is_unset(request.working_dir):
            query['WorkingDir'] = request.working_dir
        if not UtilClient.is_unset(request.working_user):
            query['WorkingUser'] = request.working_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunCommand',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.RunCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_command_with_options_async(
        self,
        tmp_req: swas__open20200601_models.RunCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RunCommandResponse:
        UtilClient.validate_model(tmp_req)
        request = swas__open20200601_models.RunCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.command_content):
            query['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.enable_parameter):
            query['EnableParameter'] = request.enable_parameter
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.windows_password_name):
            query['WindowsPasswordName'] = request.windows_password_name
        if not UtilClient.is_unset(request.working_dir):
            query['WorkingDir'] = request.working_dir
        if not UtilClient.is_unset(request.working_user):
            query['WorkingUser'] = request.working_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunCommand',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.RunCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_command(
        self,
        request: swas__open20200601_models.RunCommandRequest,
    ) -> swas__open20200601_models.RunCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_command_with_options(request, runtime)

    async def run_command_async(
        self,
        request: swas__open20200601_models.RunCommandRequest,
    ) -> swas__open20200601_models.RunCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_command_with_options_async(request, runtime)

    def start_database_instance_with_options(
        self,
        request: swas__open20200601_models.StartDatabaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StartDatabaseInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDatabaseInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.StartDatabaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_database_instance_with_options_async(
        self,
        request: swas__open20200601_models.StartDatabaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StartDatabaseInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDatabaseInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.StartDatabaseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_database_instance(
        self,
        request: swas__open20200601_models.StartDatabaseInstanceRequest,
    ) -> swas__open20200601_models.StartDatabaseInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_database_instance_with_options(request, runtime)

    async def start_database_instance_async(
        self,
        request: swas__open20200601_models.StartDatabaseInstanceRequest,
    ) -> swas__open20200601_models.StartDatabaseInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_database_instance_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        request: swas__open20200601_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StartInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.StartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        request: swas__open20200601_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StartInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.StartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
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

    def stop_database_instance_with_options(
        self,
        request: swas__open20200601_models.StopDatabaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StopDatabaseInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDatabaseInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.StopDatabaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_database_instance_with_options_async(
        self,
        request: swas__open20200601_models.StopDatabaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StopDatabaseInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDatabaseInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.StopDatabaseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_database_instance(
        self,
        request: swas__open20200601_models.StopDatabaseInstanceRequest,
    ) -> swas__open20200601_models.StopDatabaseInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_database_instance_with_options(request, runtime)

    async def stop_database_instance_async(
        self,
        request: swas__open20200601_models.StopDatabaseInstanceRequest,
    ) -> swas__open20200601_models.StopDatabaseInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_database_instance_with_options_async(request, runtime)

    def stop_instance_with_options(
        self,
        request: swas__open20200601_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StopInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.StopInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_instance_with_options_async(
        self,
        request: swas__open20200601_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StopInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.StopInstanceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceAttribute',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.UpdateInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_attribute_with_options_async(
        self,
        request: swas__open20200601_models.UpdateInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.UpdateInstanceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceAttribute',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.UpdateInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.UpgradeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_instance_with_options_async(
        self,
        request: swas__open20200601_models.UpgradeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.UpgradeInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.UpgradeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
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
