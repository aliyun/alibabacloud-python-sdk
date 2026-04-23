# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_starrocks20221019 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('starrocks', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_backup_policy_with_options(
        self,
        request: main_models.AddBackupPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddBackupPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.expire_days):
            body['ExpireDays'] = request.expire_days
        if not DaraCore.is_null(request.hour):
            body['Hour'] = request.hour
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.minute):
            body['Minute'] = request.minute
        if not DaraCore.is_null(request.recurrence_type):
            body['RecurrenceType'] = request.recurrence_type
        if not DaraCore.is_null(request.recurrence_values):
            body['RecurrenceValues'] = request.recurrence_values
        if not DaraCore.is_null(request.timeout_seconds):
            body['TimeoutSeconds'] = request.timeout_seconds
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddBackupPolicy',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/backupRestore/policy/add',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_backup_policy_with_options_async(
        self,
        request: main_models.AddBackupPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddBackupPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.expire_days):
            body['ExpireDays'] = request.expire_days
        if not DaraCore.is_null(request.hour):
            body['Hour'] = request.hour
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.minute):
            body['Minute'] = request.minute
        if not DaraCore.is_null(request.recurrence_type):
            body['RecurrenceType'] = request.recurrence_type
        if not DaraCore.is_null(request.recurrence_values):
            body['RecurrenceValues'] = request.recurrence_values
        if not DaraCore.is_null(request.timeout_seconds):
            body['TimeoutSeconds'] = request.timeout_seconds
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddBackupPolicy',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/backupRestore/policy/add',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_backup_policy(
        self,
        request: main_models.AddBackupPolicyRequest,
    ) -> main_models.AddBackupPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_backup_policy_with_options(request, headers, runtime)

    async def add_backup_policy_async(
        self,
        request: main_models.AddBackupPolicyRequest,
    ) -> main_models.AddBackupPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_backup_policy_with_options_async(request, headers, runtime)

    def add_gateway_with_options(
        self,
        request: main_models.AddGatewayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fe_node_number):
            query['FeNodeNumber'] = request.fe_node_number
        if not DaraCore.is_null(request.gateway_name):
            query['GatewayName'] = request.gateway_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGateway',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/gateway/add',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_gateway_with_options_async(
        self,
        request: main_models.AddGatewayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fe_node_number):
            query['FeNodeNumber'] = request.fe_node_number
        if not DaraCore.is_null(request.gateway_name):
            query['GatewayName'] = request.gateway_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGateway',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/gateway/add',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_gateway(
        self,
        request: main_models.AddGatewayRequest,
    ) -> main_models.AddGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_gateway_with_options(request, headers, runtime)

    async def add_gateway_async(
        self,
        request: main_models.AddGatewayRequest,
    ) -> main_models.AddGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_gateway_with_options_async(request, headers, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/resourceGroup/change',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/resourceGroup/change',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.change_resource_group_with_options(request, headers, runtime)

    async def change_resource_group_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.change_resource_group_with_options_async(request, headers, runtime)

    def check_inventory_with_options(
        self,
        request: main_models.CheckInventoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckInventoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_info):
            query['ClusterInfo'] = request.cluster_info
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckInventory',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/check/inventory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckInventoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_inventory_with_options_async(
        self,
        request: main_models.CheckInventoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckInventoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_info):
            query['ClusterInfo'] = request.cluster_info
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckInventory',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/check/inventory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckInventoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_inventory(
        self,
        request: main_models.CheckInventoryRequest,
    ) -> main_models.CheckInventoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.check_inventory_with_options(request, headers, runtime)

    async def check_inventory_async(
        self,
        request: main_models.CheckInventoryRequest,
    ) -> main_models.CheckInventoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.check_inventory_with_options_async(request, headers, runtime)

    def create_agent_resource_with_options(
        self,
        request: main_models.CreateAgentResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.cu):
            query['Cu'] = request.cu
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.spec_type):
            query['SpecType'] = request.spec_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentResource',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/lifecycle/createAgentNodeGroup',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_agent_resource_with_options_async(
        self,
        request: main_models.CreateAgentResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.cu):
            query['Cu'] = request.cu
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.spec_type):
            query['SpecType'] = request.spec_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgentResource',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/lifecycle/createAgentNodeGroup',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_agent_resource(
        self,
        request: main_models.CreateAgentResourceRequest,
    ) -> main_models.CreateAgentResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_agent_resource_with_options(request, headers, runtime)

    async def create_agent_resource_async(
        self,
        request: main_models.CreateAgentResourceRequest,
    ) -> main_models.CreateAgentResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_agent_resource_with_options_async(request, headers, runtime)

    def create_instance_v1with_options(
        self,
        request: main_models.CreateInstanceV1Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceV1Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.admin_password):
            body['AdminPassword'] = request.admin_password
        if not DaraCore.is_null(request.agent_node_group):
            body['AgentNodeGroup'] = request.agent_node_group
        if not DaraCore.is_null(request.auto_pay):
            body['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.backend_node_groups):
            body['BackendNodeGroups'] = request.backend_node_groups
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dlf_catalog_name):
            body['DlfCatalogName'] = request.dlf_catalog_name
        if not DaraCore.is_null(request.dlf_catalog_type):
            body['DlfCatalogType'] = request.dlf_catalog_type
        if not DaraCore.is_null(request.duration):
            body['Duration'] = request.duration
        if not DaraCore.is_null(request.enable_multi_az):
            body['EnableMultiAz'] = request.enable_multi_az
        if not DaraCore.is_null(request.encrypted):
            body['Encrypted'] = request.encrypted
        if not DaraCore.is_null(request.frontend_node_groups):
            body['FrontendNodeGroups'] = request.frontend_node_groups
        if not DaraCore.is_null(request.gateway_type):
            body['GatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.kms_key_id):
            body['KmsKeyId'] = request.kms_key_id
        if not DaraCore.is_null(request.linked_ram_user_name):
            body['LinkedRamUserName'] = request.linked_ram_user_name
        if not DaraCore.is_null(request.observer_node_groups):
            body['ObserverNodeGroups'] = request.observer_node_groups
        if not DaraCore.is_null(request.oss_accessing_role_name):
            body['OssAccessingRoleName'] = request.oss_accessing_role_name
        if not DaraCore.is_null(request.package_type):
            body['PackageType'] = request.package_type
        if not DaraCore.is_null(request.pay_type):
            body['PayType'] = request.pay_type
        if not DaraCore.is_null(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.principal_type):
            body['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.promotion_option_no):
            body['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.ram_user_id):
            body['RamUserId'] = request.ram_user_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.run_mode):
            body['RunMode'] = request.run_mode
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        if not DaraCore.is_null(request.v_switches):
            body['VSwitches'] = request.v_switches
        if not DaraCore.is_null(request.version):
            body['Version'] = request.version
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceV1',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/cluster/createV1',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceV1Response(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_v1with_options_async(
        self,
        request: main_models.CreateInstanceV1Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceV1Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.admin_password):
            body['AdminPassword'] = request.admin_password
        if not DaraCore.is_null(request.agent_node_group):
            body['AgentNodeGroup'] = request.agent_node_group
        if not DaraCore.is_null(request.auto_pay):
            body['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.backend_node_groups):
            body['BackendNodeGroups'] = request.backend_node_groups
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dlf_catalog_name):
            body['DlfCatalogName'] = request.dlf_catalog_name
        if not DaraCore.is_null(request.dlf_catalog_type):
            body['DlfCatalogType'] = request.dlf_catalog_type
        if not DaraCore.is_null(request.duration):
            body['Duration'] = request.duration
        if not DaraCore.is_null(request.enable_multi_az):
            body['EnableMultiAz'] = request.enable_multi_az
        if not DaraCore.is_null(request.encrypted):
            body['Encrypted'] = request.encrypted
        if not DaraCore.is_null(request.frontend_node_groups):
            body['FrontendNodeGroups'] = request.frontend_node_groups
        if not DaraCore.is_null(request.gateway_type):
            body['GatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.kms_key_id):
            body['KmsKeyId'] = request.kms_key_id
        if not DaraCore.is_null(request.linked_ram_user_name):
            body['LinkedRamUserName'] = request.linked_ram_user_name
        if not DaraCore.is_null(request.observer_node_groups):
            body['ObserverNodeGroups'] = request.observer_node_groups
        if not DaraCore.is_null(request.oss_accessing_role_name):
            body['OssAccessingRoleName'] = request.oss_accessing_role_name
        if not DaraCore.is_null(request.package_type):
            body['PackageType'] = request.package_type
        if not DaraCore.is_null(request.pay_type):
            body['PayType'] = request.pay_type
        if not DaraCore.is_null(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.principal_type):
            body['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.promotion_option_no):
            body['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.ram_user_id):
            body['RamUserId'] = request.ram_user_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.run_mode):
            body['RunMode'] = request.run_mode
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        if not DaraCore.is_null(request.v_switches):
            body['VSwitches'] = request.v_switches
        if not DaraCore.is_null(request.version):
            body['Version'] = request.version
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceV1',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/cluster/createV1',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceV1Response(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_v1(
        self,
        request: main_models.CreateInstanceV1Request,
    ) -> main_models.CreateInstanceV1Response:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_instance_v1with_options(request, headers, runtime)

    async def create_instance_v1_async(
        self,
        request: main_models.CreateInstanceV1Request,
    ) -> main_models.CreateInstanceV1Response:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_instance_v1with_options_async(request, headers, runtime)

    def create_scaling_rule_with_options(
        self,
        request: main_models.CreateScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.rule):
            query['Rule'] = request.rule
        if not DaraCore.is_null(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScalingRule',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/scalingRule/createScalingRule',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scaling_rule_with_options_async(
        self,
        request: main_models.CreateScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.rule):
            query['Rule'] = request.rule
        if not DaraCore.is_null(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScalingRule',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/scalingRule/createScalingRule',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scaling_rule(
        self,
        request: main_models.CreateScalingRuleRequest,
    ) -> main_models.CreateScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_scaling_rule_with_options(request, headers, runtime)

    async def create_scaling_rule_async(
        self,
        request: main_models.CreateScalingRuleRequest,
    ) -> main_models.CreateScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_scaling_rule_with_options_async(request, headers, runtime)

    def create_service_linked_role_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceLinkedRoleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceLinkedRole',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/user/create_default_role',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceLinkedRoleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceLinkedRole',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/user/create_default_role',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_linked_role(self) -> main_models.CreateServiceLinkedRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_service_linked_role_with_options(headers, runtime)

    async def create_service_linked_role_async(self) -> main_models.CreateServiceLinkedRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_service_linked_role_with_options_async(headers, runtime)

    def delete_backup_with_options(
        self,
        request: main_models.DeleteBackupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_task_id):
            query['BackupTaskId'] = request.backup_task_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBackup',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/backup/manage/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_backup_with_options_async(
        self,
        request: main_models.DeleteBackupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_task_id):
            query['BackupTaskId'] = request.backup_task_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBackup',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/backup/manage/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_backup(
        self,
        request: main_models.DeleteBackupRequest,
    ) -> main_models.DeleteBackupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_backup_with_options(request, headers, runtime)

    async def delete_backup_async(
        self,
        request: main_models.DeleteBackupRequest,
    ) -> main_models.DeleteBackupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_backup_with_options_async(request, headers, runtime)

    def delete_backup_policy_with_options(
        self,
        request: main_models.DeleteBackupPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackupPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBackupPolicy',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/backupRestore/policy/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_backup_policy_with_options_async(
        self,
        request: main_models.DeleteBackupPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackupPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBackupPolicy',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/backupRestore/policy/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_backup_policy(
        self,
        request: main_models.DeleteBackupPolicyRequest,
    ) -> main_models.DeleteBackupPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_backup_policy_with_options(request, headers, runtime)

    async def delete_backup_policy_async(
        self,
        request: main_models.DeleteBackupPolicyRequest,
    ) -> main_models.DeleteBackupPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_backup_policy_with_options_async(request, headers, runtime)

    def delete_gateway_with_options(
        self,
        request: main_models.DeleteGatewayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGateway',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/gateway/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_with_options_async(
        self,
        request: main_models.DeleteGatewayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGateway',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/gateway/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway(
        self,
        request: main_models.DeleteGatewayRequest,
    ) -> main_models.DeleteGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_gateway_with_options(request, headers, runtime)

    async def delete_gateway_async(
        self,
        request: main_models.DeleteGatewayRequest,
    ) -> main_models.DeleteGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_gateway_with_options_async(request, headers, runtime)

    def delete_inner_ip_whitelist_group_with_options(
        self,
        request: main_models.DeleteInnerIpWhitelistGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInnerIpWhitelistGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.inner_ip_whitelist_group_id):
            body['InnerIpWhitelistGroupId'] = request.inner_ip_whitelist_group_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInnerIpWhitelistGroup',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/securityGroup/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInnerIpWhitelistGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_inner_ip_whitelist_group_with_options_async(
        self,
        request: main_models.DeleteInnerIpWhitelistGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInnerIpWhitelistGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.inner_ip_whitelist_group_id):
            body['InnerIpWhitelistGroupId'] = request.inner_ip_whitelist_group_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInnerIpWhitelistGroup',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/securityGroup/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInnerIpWhitelistGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_inner_ip_whitelist_group(
        self,
        request: main_models.DeleteInnerIpWhitelistGroupRequest,
    ) -> main_models.DeleteInnerIpWhitelistGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_inner_ip_whitelist_group_with_options(request, headers, runtime)

    async def delete_inner_ip_whitelist_group_async(
        self,
        request: main_models.DeleteInnerIpWhitelistGroupRequest,
    ) -> main_models.DeleteInnerIpWhitelistGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_inner_ip_whitelist_group_with_options_async(request, headers, runtime)

    def delete_scaling_rule_with_options(
        self,
        request: main_models.DeleteScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        if not DaraCore.is_null(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScalingRule',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/scalingRule/deleteScalingRule',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scaling_rule_with_options_async(
        self,
        request: main_models.DeleteScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        if not DaraCore.is_null(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScalingRule',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/scalingRule/deleteScalingRule',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scaling_rule(
        self,
        request: main_models.DeleteScalingRuleRequest,
    ) -> main_models.DeleteScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_scaling_rule_with_options(request, headers, runtime)

    async def delete_scaling_rule_async(
        self,
        request: main_models.DeleteScalingRuleRequest,
    ) -> main_models.DeleteScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_scaling_rule_with_options_async(request, headers, runtime)

    def describe_available_zones_with_options(
        self,
        request: main_models.DescribeAvailableZonesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAvailableZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAvailableZones',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/zone/describeZones',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAvailableZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_zones_with_options_async(
        self,
        request: main_models.DescribeAvailableZonesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAvailableZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAvailableZones',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/zone/describeZones',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAvailableZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_zones(
        self,
        request: main_models.DescribeAvailableZonesRequest,
    ) -> main_models.DescribeAvailableZonesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_available_zones_with_options(request, headers, runtime)

    async def describe_available_zones_async(
        self,
        request: main_models.DescribeAvailableZonesRequest,
    ) -> main_models.DescribeAvailableZonesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_available_zones_with_options_async(request, headers, runtime)

    def describe_backup_policies_with_options(
        self,
        request: main_models.DescribeBackupPoliciesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupPolicies',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/backupRestore/policy/describe',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_policies_with_options_async(
        self,
        request: main_models.DescribeBackupPoliciesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupPolicies',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/backupRestore/policy/describe',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_policies(
        self,
        request: main_models.DescribeBackupPoliciesRequest,
    ) -> main_models.DescribeBackupPoliciesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_backup_policies_with_options(request, headers, runtime)

    async def describe_backup_policies_async(
        self,
        request: main_models.DescribeBackupPoliciesRequest,
    ) -> main_models.DescribeBackupPoliciesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_backup_policies_with_options_async(request, headers, runtime)

    def describe_backups_with_options(
        self,
        request: main_models.DescribeBackupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_task_id):
            query['BackupTaskId'] = request.backup_task_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.statuses):
            query['Statuses'] = request.statuses
        if not DaraCore.is_null(request.time_period_end_time):
            query['TimePeriodEndTime'] = request.time_period_end_time
        if not DaraCore.is_null(request.time_period_start_time):
            query['TimePeriodStartTime'] = request.time_period_start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackups',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/backup/manage/describe',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backups_with_options_async(
        self,
        request: main_models.DescribeBackupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_task_id):
            query['BackupTaskId'] = request.backup_task_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.statuses):
            query['Statuses'] = request.statuses
        if not DaraCore.is_null(request.time_period_end_time):
            query['TimePeriodEndTime'] = request.time_period_end_time
        if not DaraCore.is_null(request.time_period_start_time):
            query['TimePeriodStartTime'] = request.time_period_start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackups',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/backup/manage/describe',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backups(
        self,
        request: main_models.DescribeBackupsRequest,
    ) -> main_models.DescribeBackupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_backups_with_options(request, headers, runtime)

    async def describe_backups_async(
        self,
        request: main_models.DescribeBackupsRequest,
    ) -> main_models.DescribeBackupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_backups_with_options_async(request, headers, runtime)

    def describe_config_history_with_options(
        self,
        request: main_models.DescribeConfigHistoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConfigHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.effect_statuses):
            query['EffectStatuses'] = request.effect_statuses
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.need_total):
            query['NeedTotal'] = request.need_total
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConfigHistory',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/config/describeConfigHistory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConfigHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_config_history_with_options_async(
        self,
        request: main_models.DescribeConfigHistoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConfigHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.effect_statuses):
            query['EffectStatuses'] = request.effect_statuses
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.need_total):
            query['NeedTotal'] = request.need_total
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConfigHistory',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/config/describeConfigHistory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConfigHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_config_history(
        self,
        request: main_models.DescribeConfigHistoryRequest,
    ) -> main_models.DescribeConfigHistoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_config_history_with_options(request, headers, runtime)

    async def describe_config_history_async(
        self,
        request: main_models.DescribeConfigHistoryRequest,
    ) -> main_models.DescribeConfigHistoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_config_history_with_options_async(request, headers, runtime)

    def describe_event_names_with_options(
        self,
        request: main_models.DescribeEventNamesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventNamesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventNames',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/event/describeEventNames',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventNamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_names_with_options_async(
        self,
        request: main_models.DescribeEventNamesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventNamesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventNames',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/event/describeEventNames',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventNamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_names(
        self,
        request: main_models.DescribeEventNamesRequest,
    ) -> main_models.DescribeEventNamesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_event_names_with_options(request, headers, runtime)

    async def describe_event_names_async(
        self,
        request: main_models.DescribeEventNamesRequest,
    ) -> main_models.DescribeEventNamesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_event_names_with_options_async(request, headers, runtime)

    def describe_inner_ip_whitelist_groups_with_options(
        self,
        request: main_models.DescribeInnerIpWhitelistGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInnerIpWhitelistGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInnerIpWhitelistGroups',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/securityGroup/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInnerIpWhitelistGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_inner_ip_whitelist_groups_with_options_async(
        self,
        request: main_models.DescribeInnerIpWhitelistGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInnerIpWhitelistGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInnerIpWhitelistGroups',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/securityGroup/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInnerIpWhitelistGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_inner_ip_whitelist_groups(
        self,
        request: main_models.DescribeInnerIpWhitelistGroupsRequest,
    ) -> main_models.DescribeInnerIpWhitelistGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_inner_ip_whitelist_groups_with_options(request, headers, runtime)

    async def describe_inner_ip_whitelist_groups_async(
        self,
        request: main_models.DescribeInnerIpWhitelistGroupsRequest,
    ) -> main_models.DescribeInnerIpWhitelistGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_inner_ip_whitelist_groups_with_options_async(request, headers, runtime)

    def describe_instance_configs_with_options(
        self,
        request: main_models.DescribeInstanceConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_modify):
            query['AllowModify'] = request.allow_modify
        if not DaraCore.is_null(request.config_key):
            query['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.config_type):
            query['ConfigType'] = request.config_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.need_total):
            query['NeedTotal'] = request.need_total
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceConfigs',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/config/describeInstanceConfigs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_configs_with_options_async(
        self,
        request: main_models.DescribeInstanceConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_modify):
            query['AllowModify'] = request.allow_modify
        if not DaraCore.is_null(request.config_key):
            query['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.config_type):
            query['ConfigType'] = request.config_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.need_total):
            query['NeedTotal'] = request.need_total
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceConfigs',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/config/describeInstanceConfigs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_configs(
        self,
        request: main_models.DescribeInstanceConfigsRequest,
    ) -> main_models.DescribeInstanceConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_instance_configs_with_options(request, headers, runtime)

    async def describe_instance_configs_async(
        self,
        request: main_models.DescribeInstanceConfigsRequest,
    ) -> main_models.DescribeInstanceConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_instance_configs_with_options_async(request, headers, runtime)

    def describe_instance_diagnosis_result_with_options(
        self,
        request: main_models.DescribeInstanceDiagnosisResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceDiagnosisResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dimension):
            query['Dimension'] = request.dimension
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.report_date):
            query['ReportDate'] = request.report_date
        if not DaraCore.is_null(request.statuses):
            query['Statuses'] = request.statuses
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceDiagnosisResult',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/diagnosis/describe',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceDiagnosisResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_diagnosis_result_with_options_async(
        self,
        request: main_models.DescribeInstanceDiagnosisResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceDiagnosisResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dimension):
            query['Dimension'] = request.dimension
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.report_date):
            query['ReportDate'] = request.report_date
        if not DaraCore.is_null(request.statuses):
            query['Statuses'] = request.statuses
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceDiagnosisResult',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/diagnosis/describe',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceDiagnosisResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_diagnosis_result(
        self,
        request: main_models.DescribeInstanceDiagnosisResultRequest,
    ) -> main_models.DescribeInstanceDiagnosisResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_instance_diagnosis_result_with_options(request, headers, runtime)

    async def describe_instance_diagnosis_result_async(
        self,
        request: main_models.DescribeInstanceDiagnosisResultRequest,
    ) -> main_models.DescribeInstanceDiagnosisResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_instance_diagnosis_result_with_options_async(request, headers, runtime)

    def describe_instance_meta_token_with_options(
        self,
        request: main_models.DescribeInstanceMetaTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceMetaTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceMetaToken',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/migration/getMetaToken',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceMetaTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_meta_token_with_options_async(
        self,
        request: main_models.DescribeInstanceMetaTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceMetaTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceMetaToken',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/migration/getMetaToken',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceMetaTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_meta_token(
        self,
        request: main_models.DescribeInstanceMetaTokenRequest,
    ) -> main_models.DescribeInstanceMetaTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_instance_meta_token_with_options(request, headers, runtime)

    async def describe_instance_meta_token_async(
        self,
        request: main_models.DescribeInstanceMetaTokenRequest,
    ) -> main_models.DescribeInstanceMetaTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_instance_meta_token_with_options_async(request, headers, runtime)

    def describe_instances_with_options(
        self,
        tmp_req: main_models.DescribeInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstancesResponse:
        tmp_req.validate()
        request = main_models.DescribeInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstances',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/starrocks/describeInstances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        tmp_req: main_models.DescribeInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstancesResponse:
        tmp_req.validate()
        request = main_models.DescribeInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstances',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/starrocks/describeInstances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instances(
        self,
        request: main_models.DescribeInstancesRequest,
    ) -> main_models.DescribeInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_instances_with_options(request, headers, runtime)

    async def describe_instances_async(
        self,
        request: main_models.DescribeInstancesRequest,
    ) -> main_models.DescribeInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_instances_with_options_async(request, headers, runtime)

    def describe_node_groups_with_options(
        self,
        request: main_models.DescribeNodeGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNodeGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not DaraCore.is_null(request.component_type):
            body['componentType'] = request.component_type
        if not DaraCore.is_null(request.instance_id):
            body['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_ids):
            body['nodeGroupIds'] = request.node_group_ids
        if not DaraCore.is_null(request.node_group_name):
            body['nodeGroupName'] = request.node_group_name
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNodeGroups',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/nodegroup/describeNodeGroups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNodeGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_node_groups_with_options_async(
        self,
        request: main_models.DescribeNodeGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNodeGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not DaraCore.is_null(request.component_type):
            body['componentType'] = request.component_type
        if not DaraCore.is_null(request.instance_id):
            body['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_ids):
            body['nodeGroupIds'] = request.node_group_ids
        if not DaraCore.is_null(request.node_group_name):
            body['nodeGroupName'] = request.node_group_name
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNodeGroups',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/nodegroup/describeNodeGroups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNodeGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_node_groups(
        self,
        request: main_models.DescribeNodeGroupsRequest,
    ) -> main_models.DescribeNodeGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_node_groups_with_options(request, headers, runtime)

    async def describe_node_groups_async(
        self,
        request: main_models.DescribeNodeGroupsRequest,
    ) -> main_models.DescribeNodeGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_node_groups_with_options_async(request, headers, runtime)

    def describe_regions_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/region/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/region/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(self) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(headers, runtime)

    async def describe_regions_async(self) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(headers, runtime)

    def describe_resource_constraints_with_options(
        self,
        request: main_models.DescribeResourceConstraintsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceConstraintsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.architecture):
            query['Architecture'] = request.architecture
        if not DaraCore.is_null(request.package_type):
            query['PackageType'] = request.package_type
        if not DaraCore.is_null(request.run_mode):
            query['RunMode'] = request.run_mode
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceConstraints',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/starrocks/describeResourceConstraints',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceConstraintsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_constraints_with_options_async(
        self,
        request: main_models.DescribeResourceConstraintsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceConstraintsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.architecture):
            query['Architecture'] = request.architecture
        if not DaraCore.is_null(request.package_type):
            query['PackageType'] = request.package_type
        if not DaraCore.is_null(request.run_mode):
            query['RunMode'] = request.run_mode
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceConstraints',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/starrocks/describeResourceConstraints',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceConstraintsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_constraints(
        self,
        request: main_models.DescribeResourceConstraintsRequest,
    ) -> main_models.DescribeResourceConstraintsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_resource_constraints_with_options(request, headers, runtime)

    async def describe_resource_constraints_async(
        self,
        request: main_models.DescribeResourceConstraintsRequest,
    ) -> main_models.DescribeResourceConstraintsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_resource_constraints_with_options_async(request, headers, runtime)

    def describe_system_timezone_with_options(
        self,
        request: main_models.DescribeSystemTimezoneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSystemTimezoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSystemTimezone',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/timezone/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSystemTimezoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_system_timezone_with_options_async(
        self,
        request: main_models.DescribeSystemTimezoneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSystemTimezoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSystemTimezone',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/timezone/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSystemTimezoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_system_timezone(
        self,
        request: main_models.DescribeSystemTimezoneRequest,
    ) -> main_models.DescribeSystemTimezoneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_system_timezone_with_options(request, headers, runtime)

    async def describe_system_timezone_async(
        self,
        request: main_models.DescribeSystemTimezoneRequest,
    ) -> main_models.DescribeSystemTimezoneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_system_timezone_with_options_async(request, headers, runtime)

    def describe_time_trigger_scaling_rules_with_options(
        self,
        request: main_models.DescribeTimeTriggerScalingRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTimeTriggerScalingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTimeTriggerScalingRules',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/scalingRule/describeTimeTriggerScalingRules',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTimeTriggerScalingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_time_trigger_scaling_rules_with_options_async(
        self,
        request: main_models.DescribeTimeTriggerScalingRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTimeTriggerScalingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTimeTriggerScalingRules',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/scalingRule/describeTimeTriggerScalingRules',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTimeTriggerScalingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_time_trigger_scaling_rules(
        self,
        request: main_models.DescribeTimeTriggerScalingRulesRequest,
    ) -> main_models.DescribeTimeTriggerScalingRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_time_trigger_scaling_rules_with_options(request, headers, runtime)

    async def describe_time_trigger_scaling_rules_async(
        self,
        request: main_models.DescribeTimeTriggerScalingRulesRequest,
    ) -> main_models.DescribeTimeTriggerScalingRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_time_trigger_scaling_rules_with_options_async(request, headers, runtime)

    def disable_sslconnection_with_options(
        self,
        request: main_models.DisableSSLConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableSSLConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableSSLConnection',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/starrocks/disableSSLConnection',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSSLConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_sslconnection_with_options_async(
        self,
        request: main_models.DisableSSLConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableSSLConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableSSLConnection',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/starrocks/disableSSLConnection',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSSLConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_sslconnection(
        self,
        request: main_models.DisableSSLConnectionRequest,
    ) -> main_models.DisableSSLConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.disable_sslconnection_with_options(request, headers, runtime)

    async def disable_sslconnection_async(
        self,
        request: main_models.DisableSSLConnectionRequest,
    ) -> main_models.DisableSSLConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.disable_sslconnection_with_options_async(request, headers, runtime)

    def enable_internal_slb_with_options(
        self,
        request: main_models.EnableInternalSlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableInternalSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableInternalSlb',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/gateway/enableInternalSlb',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableInternalSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_internal_slb_with_options_async(
        self,
        request: main_models.EnableInternalSlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableInternalSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableInternalSlb',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/gateway/enableInternalSlb',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableInternalSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_internal_slb(
        self,
        request: main_models.EnableInternalSlbRequest,
    ) -> main_models.EnableInternalSlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.enable_internal_slb_with_options(request, headers, runtime)

    async def enable_internal_slb_async(
        self,
        request: main_models.EnableInternalSlbRequest,
    ) -> main_models.EnableInternalSlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.enable_internal_slb_with_options_async(request, headers, runtime)

    def enable_multi_az_with_options(
        self,
        request: main_models.EnableMultiAzRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableMultiAzResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.observers):
            body['observers'] = request.observers
        if not DaraCore.is_null(request.promotion_option_no):
            body['promotionOptionNo'] = request.promotion_option_no
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableMultiAz',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/lifecycle/enableMultiAz',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableMultiAzResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_multi_az_with_options_async(
        self,
        request: main_models.EnableMultiAzRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableMultiAzResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.observers):
            body['observers'] = request.observers
        if not DaraCore.is_null(request.promotion_option_no):
            body['promotionOptionNo'] = request.promotion_option_no
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableMultiAz',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/lifecycle/enableMultiAz',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableMultiAzResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_multi_az(
        self,
        request: main_models.EnableMultiAzRequest,
    ) -> main_models.EnableMultiAzResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.enable_multi_az_with_options(request, headers, runtime)

    async def enable_multi_az_async(
        self,
        request: main_models.EnableMultiAzRequest,
    ) -> main_models.EnableMultiAzResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.enable_multi_az_with_options_async(request, headers, runtime)

    def enable_sslconnection_with_options(
        self,
        request: main_models.EnableSSLConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableSSLConnectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.custom_sslcertificate):
            body['CustomSSLCertificate'] = request.custom_sslcertificate
        if not DaraCore.is_null(request.enable_custom):
            body['EnableCustom'] = request.enable_custom
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.renewal):
            body['Renewal'] = request.renewal
        if not DaraCore.is_null(request.ssl_key_password):
            body['SslKeyPassword'] = request.ssl_key_password
        if not DaraCore.is_null(request.ssl_keystore_password):
            body['SslKeystorePassword'] = request.ssl_keystore_password
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableSSLConnection',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/starrocks/enableSSLConnection',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSSLConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_sslconnection_with_options_async(
        self,
        request: main_models.EnableSSLConnectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableSSLConnectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.custom_sslcertificate):
            body['CustomSSLCertificate'] = request.custom_sslcertificate
        if not DaraCore.is_null(request.enable_custom):
            body['EnableCustom'] = request.enable_custom
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.renewal):
            body['Renewal'] = request.renewal
        if not DaraCore.is_null(request.ssl_key_password):
            body['SslKeyPassword'] = request.ssl_key_password
        if not DaraCore.is_null(request.ssl_keystore_password):
            body['SslKeystorePassword'] = request.ssl_keystore_password
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableSSLConnection',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/starrocks/enableSSLConnection',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSSLConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_sslconnection(
        self,
        request: main_models.EnableSSLConnectionRequest,
    ) -> main_models.EnableSSLConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.enable_sslconnection_with_options(request, headers, runtime)

    async def enable_sslconnection_async(
        self,
        request: main_models.EnableSSLConnectionRequest,
    ) -> main_models.EnableSSLConnectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.enable_sslconnection_with_options_async(request, headers, runtime)

    def get_instance_feature_gate_with_options(
        self,
        request: main_models.GetInstanceFeatureGateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceFeatureGateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceFeatureGate',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/features/featureGate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceFeatureGateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_feature_gate_with_options_async(
        self,
        request: main_models.GetInstanceFeatureGateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceFeatureGateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceFeatureGate',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/features/featureGate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceFeatureGateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_feature_gate(
        self,
        request: main_models.GetInstanceFeatureGateRequest,
    ) -> main_models.GetInstanceFeatureGateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_instance_feature_gate_with_options(request, headers, runtime)

    async def get_instance_feature_gate_async(
        self,
        request: main_models.GetInstanceFeatureGateRequest,
    ) -> main_models.GetInstanceFeatureGateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_instance_feature_gate_with_options_async(request, headers, runtime)

    def get_node_group_feature_gate_with_options(
        self,
        request: main_models.GetNodeGroupFeatureGateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetNodeGroupFeatureGateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNodeGroupFeatureGate',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/features/nodeGroupFeatureGate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNodeGroupFeatureGateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_node_group_feature_gate_with_options_async(
        self,
        request: main_models.GetNodeGroupFeatureGateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetNodeGroupFeatureGateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNodeGroupFeatureGate',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/features/nodeGroupFeatureGate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNodeGroupFeatureGateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_node_group_feature_gate(
        self,
        request: main_models.GetNodeGroupFeatureGateRequest,
    ) -> main_models.GetNodeGroupFeatureGateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_node_group_feature_gate_with_options(request, headers, runtime)

    async def get_node_group_feature_gate_async(
        self,
        request: main_models.GetNodeGroupFeatureGateRequest,
    ) -> main_models.GetNodeGroupFeatureGateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_node_group_feature_gate_with_options_async(request, headers, runtime)

    def isolate_leader_with_options(
        self,
        request: main_models.IsolateLeaderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.IsolateLeaderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.isolate_leader):
            query['IsolateLeader'] = request.isolate_leader
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IsolateLeader',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/gateway/isolateLeader',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IsolateLeaderResponse(),
            self.call_api(params, req, runtime)
        )

    async def isolate_leader_with_options_async(
        self,
        request: main_models.IsolateLeaderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.IsolateLeaderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.isolate_leader):
            query['IsolateLeader'] = request.isolate_leader
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IsolateLeader',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/gateway/isolateLeader',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IsolateLeaderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def isolate_leader(
        self,
        request: main_models.IsolateLeaderRequest,
    ) -> main_models.IsolateLeaderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.isolate_leader_with_options(request, headers, runtime)

    async def isolate_leader_async(
        self,
        request: main_models.IsolateLeaderRequest,
    ) -> main_models.IsolateLeaderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.isolate_leader_with_options_async(request, headers, runtime)

    def list_gateway_with_options(
        self,
        request: main_models.ListGatewayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGateway',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/gateway/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_with_options_async(
        self,
        request: main_models.ListGatewayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGateway',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/gateway/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway(
        self,
        request: main_models.ListGatewayRequest,
    ) -> main_models.ListGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_gateway_with_options(request, headers, runtime)

    async def list_gateway_async(
        self,
        request: main_models.ListGatewayRequest,
    ) -> main_models.ListGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_gateway_with_options_async(request, headers, runtime)

    def list_operation_activity_with_options(
        self,
        request: main_models.ListOperationActivityRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListOperationActivityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.operation_id):
            query['OperationId'] = request.operation_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOperationActivity',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/operation/listOperationActivity',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOperationActivityResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_operation_activity_with_options_async(
        self,
        request: main_models.ListOperationActivityRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListOperationActivityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.operation_id):
            query['OperationId'] = request.operation_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOperationActivity',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/operation/listOperationActivity',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOperationActivityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_operation_activity(
        self,
        request: main_models.ListOperationActivityRequest,
    ) -> main_models.ListOperationActivityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_operation_activity_with_options(request, headers, runtime)

    async def list_operation_activity_async(
        self,
        request: main_models.ListOperationActivityRequest,
    ) -> main_models.ListOperationActivityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_operation_activity_with_options_async(request, headers, runtime)

    def list_operation_history_with_options(
        self,
        request: main_models.ListOperationHistoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListOperationHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.operation_id):
            query['OperationId'] = request.operation_id
        if not DaraCore.is_null(request.operation_status):
            query['OperationStatus'] = request.operation_status
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOperationHistory',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/operation/listOperationHistory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOperationHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_operation_history_with_options_async(
        self,
        request: main_models.ListOperationHistoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListOperationHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.operation_id):
            query['OperationId'] = request.operation_id
        if not DaraCore.is_null(request.operation_status):
            query['OperationStatus'] = request.operation_status
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOperationHistory',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/operation/listOperationHistory',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOperationHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_operation_history(
        self,
        request: main_models.ListOperationHistoryRequest,
    ) -> main_models.ListOperationHistoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_operation_history_with_options(request, headers, runtime)

    async def list_operation_history_async(
        self,
        request: main_models.ListOperationHistoryRequest,
    ) -> main_models.ListOperationHistoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_operation_history_with_options_async(request, headers, runtime)

    def list_ssldetails_with_options(
        self,
        request: main_models.ListSSLDetailsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSSLDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSSLDetails',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/starrocks/listSSLDetails',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSSLDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ssldetails_with_options_async(
        self,
        request: main_models.ListSSLDetailsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSSLDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSSLDetails',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/starrocks/listSSLDetails',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSSLDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ssldetails(
        self,
        request: main_models.ListSSLDetailsRequest,
    ) -> main_models.ListSSLDetailsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_ssldetails_with_options(request, headers, runtime)

    async def list_ssldetails_async(
        self,
        request: main_models.ListSSLDetailsRequest,
    ) -> main_models.ListSSLDetailsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_ssldetails_with_options_async(request, headers, runtime)

    def modify_charge_type_with_options(
        self,
        request: main_models.ModifyChargeTypeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyChargeTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.billing_instance_ids):
            query['BillingInstanceIds'] = request.billing_instance_ids
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyChargeType',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/cluster/modifyChargeType',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_charge_type_with_options_async(
        self,
        request: main_models.ModifyChargeTypeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyChargeTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.billing_instance_ids):
            query['BillingInstanceIds'] = request.billing_instance_ids
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyChargeType',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/cluster/modifyChargeType',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyChargeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_charge_type(
        self,
        request: main_models.ModifyChargeTypeRequest,
    ) -> main_models.ModifyChargeTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_charge_type_with_options(request, headers, runtime)

    async def modify_charge_type_async(
        self,
        request: main_models.ModifyChargeTypeRequest,
    ) -> main_models.ModifyChargeTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_charge_type_with_options_async(request, headers, runtime)

    def modify_cu_with_options(
        self,
        request: main_models.ModifyCuRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCuResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fast_mode):
            query['FastMode'] = request.fast_mode
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCu',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/resourceChange/modifyCu',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCuResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cu_with_options_async(
        self,
        request: main_models.ModifyCuRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCuResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fast_mode):
            query['FastMode'] = request.fast_mode
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCu',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/resourceChange/modifyCu',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCuResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cu(
        self,
        request: main_models.ModifyCuRequest,
    ) -> main_models.ModifyCuResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_cu_with_options(request, headers, runtime)

    async def modify_cu_async(
        self,
        request: main_models.ModifyCuRequest,
    ) -> main_models.ModifyCuResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_cu_with_options_async(request, headers, runtime)

    def modify_cu_pre_check_with_options(
        self,
        request: main_models.ModifyCuPreCheckRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCuPreCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCuPreCheck',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/resourceChange/modifyCuPreCheck',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCuPreCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cu_pre_check_with_options_async(
        self,
        request: main_models.ModifyCuPreCheckRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCuPreCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCuPreCheck',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/resourceChange/modifyCuPreCheck',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCuPreCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cu_pre_check(
        self,
        request: main_models.ModifyCuPreCheckRequest,
    ) -> main_models.ModifyCuPreCheckResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_cu_pre_check_with_options(request, headers, runtime)

    async def modify_cu_pre_check_async(
        self,
        request: main_models.ModifyCuPreCheckRequest,
    ) -> main_models.ModifyCuPreCheckResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_cu_pre_check_with_options_async(request, headers, runtime)

    def modify_disk_number_with_options(
        self,
        request: main_models.ModifyDiskNumberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDiskNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fast_mode):
            query['FastMode'] = request.fast_mode
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDiskNumber',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/resourceChange/modifyDiskNumber',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDiskNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_disk_number_with_options_async(
        self,
        request: main_models.ModifyDiskNumberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDiskNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fast_mode):
            query['FastMode'] = request.fast_mode
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDiskNumber',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/resourceChange/modifyDiskNumber',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDiskNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_disk_number(
        self,
        request: main_models.ModifyDiskNumberRequest,
    ) -> main_models.ModifyDiskNumberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_disk_number_with_options(request, headers, runtime)

    async def modify_disk_number_async(
        self,
        request: main_models.ModifyDiskNumberRequest,
    ) -> main_models.ModifyDiskNumberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_disk_number_with_options_async(request, headers, runtime)

    def modify_disk_performance_level_with_options(
        self,
        request: main_models.ModifyDiskPerformanceLevelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDiskPerformanceLevelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDiskPerformanceLevel',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/resourceChange/modifyDiskPerformanceLevel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDiskPerformanceLevelResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_disk_performance_level_with_options_async(
        self,
        request: main_models.ModifyDiskPerformanceLevelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDiskPerformanceLevelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDiskPerformanceLevel',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/resourceChange/modifyDiskPerformanceLevel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDiskPerformanceLevelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_disk_performance_level(
        self,
        request: main_models.ModifyDiskPerformanceLevelRequest,
    ) -> main_models.ModifyDiskPerformanceLevelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_disk_performance_level_with_options(request, headers, runtime)

    async def modify_disk_performance_level_async(
        self,
        request: main_models.ModifyDiskPerformanceLevelRequest,
    ) -> main_models.ModifyDiskPerformanceLevelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_disk_performance_level_with_options_async(request, headers, runtime)

    def modify_disk_size_with_options(
        self,
        request: main_models.ModifyDiskSizeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDiskSizeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fast_mode):
            query['FastMode'] = request.fast_mode
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDiskSize',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/resourceChange/modifyDiskSize',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDiskSizeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_disk_size_with_options_async(
        self,
        request: main_models.ModifyDiskSizeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDiskSizeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fast_mode):
            query['FastMode'] = request.fast_mode
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDiskSize',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/resourceChange/modifyDiskSize',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDiskSizeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_disk_size(
        self,
        request: main_models.ModifyDiskSizeRequest,
    ) -> main_models.ModifyDiskSizeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_disk_size_with_options(request, headers, runtime)

    async def modify_disk_size_async(
        self,
        request: main_models.ModifyDiskSizeRequest,
    ) -> main_models.ModifyDiskSizeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_disk_size_with_options_async(request, headers, runtime)

    def modify_disk_type_with_options(
        self,
        request: main_models.ModifyDiskTypeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDiskTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target_disk_type):
            query['TargetDiskType'] = request.target_disk_type
        if not DaraCore.is_null(request.target_performance_level):
            query['TargetPerformanceLevel'] = request.target_performance_level
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDiskType',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/resourceChange/modifyDiskType',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDiskTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_disk_type_with_options_async(
        self,
        request: main_models.ModifyDiskTypeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDiskTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target_disk_type):
            query['TargetDiskType'] = request.target_disk_type
        if not DaraCore.is_null(request.target_performance_level):
            query['TargetPerformanceLevel'] = request.target_performance_level
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDiskType',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/resourceChange/modifyDiskType',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDiskTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_disk_type(
        self,
        request: main_models.ModifyDiskTypeRequest,
    ) -> main_models.ModifyDiskTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_disk_type_with_options(request, headers, runtime)

    async def modify_disk_type_async(
        self,
        request: main_models.ModifyDiskTypeRequest,
    ) -> main_models.ModifyDiskTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_disk_type_with_options_async(request, headers, runtime)

    def modify_host_alias_with_options(
        self,
        request: main_models.ModifyHostAliasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHostAliasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not DaraCore.is_null(request.host_aliases):
            body['hostAliases'] = request.host_aliases
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHostAlias',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/network/modifyHostAlias',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHostAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_host_alias_with_options_async(
        self,
        request: main_models.ModifyHostAliasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHostAliasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not DaraCore.is_null(request.host_aliases):
            body['hostAliases'] = request.host_aliases
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHostAlias',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/network/modifyHostAlias',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHostAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_host_alias(
        self,
        request: main_models.ModifyHostAliasRequest,
    ) -> main_models.ModifyHostAliasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_host_alias_with_options(request, headers, runtime)

    async def modify_host_alias_async(
        self,
        request: main_models.ModifyHostAliasRequest,
    ) -> main_models.ModifyHostAliasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_host_alias_with_options_async(request, headers, runtime)

    def modify_instance_config_with_options(
        self,
        request: main_models.ModifyInstanceConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_config_list):
            query['AddConfigList'] = request.add_config_list
        if not DaraCore.is_null(request.config_list):
            query['ConfigList'] = request.config_list
        if not DaraCore.is_null(request.delete_config_list):
            query['DeleteConfigList'] = request.delete_config_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.reason):
            query['Reason'] = request.reason
        body = {}
        if not DaraCore.is_null(request.configs_to_add):
            body['configsToAdd'] = request.configs_to_add
        if not DaraCore.is_null(request.configs_to_delete):
            body['configsToDelete'] = request.configs_to_delete
        if not DaraCore.is_null(request.configs_to_update):
            body['configsToUpdate'] = request.configs_to_update
        if not DaraCore.is_null(request.fast_mode):
            body['fastMode'] = request.fast_mode
        if not DaraCore.is_null(request.restart):
            body['restart'] = request.restart
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceConfig',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/config/modifyInstanceConfig',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_config_with_options_async(
        self,
        request: main_models.ModifyInstanceConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_config_list):
            query['AddConfigList'] = request.add_config_list
        if not DaraCore.is_null(request.config_list):
            query['ConfigList'] = request.config_list
        if not DaraCore.is_null(request.delete_config_list):
            query['DeleteConfigList'] = request.delete_config_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.reason):
            query['Reason'] = request.reason
        body = {}
        if not DaraCore.is_null(request.configs_to_add):
            body['configsToAdd'] = request.configs_to_add
        if not DaraCore.is_null(request.configs_to_delete):
            body['configsToDelete'] = request.configs_to_delete
        if not DaraCore.is_null(request.configs_to_update):
            body['configsToUpdate'] = request.configs_to_update
        if not DaraCore.is_null(request.fast_mode):
            body['fastMode'] = request.fast_mode
        if not DaraCore.is_null(request.restart):
            body['restart'] = request.restart
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceConfig',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/config/modifyInstanceConfig',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_config(
        self,
        request: main_models.ModifyInstanceConfigRequest,
    ) -> main_models.ModifyInstanceConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_instance_config_with_options(request, headers, runtime)

    async def modify_instance_config_async(
        self,
        request: main_models.ModifyInstanceConfigRequest,
    ) -> main_models.ModifyInstanceConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_instance_config_with_options_async(request, headers, runtime)

    def modify_instance_config_pre_check_with_options(
        self,
        request: main_models.ModifyInstanceConfigPreCheckRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceConfigPreCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not DaraCore.is_null(request.configs_to_add):
            body['configsToAdd'] = request.configs_to_add
        if not DaraCore.is_null(request.configs_to_delete):
            body['configsToDelete'] = request.configs_to_delete
        if not DaraCore.is_null(request.configs_to_update):
            body['configsToUpdate'] = request.configs_to_update
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceConfigPreCheck',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/config/modifyInstanceConfigPreCheck',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceConfigPreCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_config_pre_check_with_options_async(
        self,
        request: main_models.ModifyInstanceConfigPreCheckRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceConfigPreCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not DaraCore.is_null(request.configs_to_add):
            body['configsToAdd'] = request.configs_to_add
        if not DaraCore.is_null(request.configs_to_delete):
            body['configsToDelete'] = request.configs_to_delete
        if not DaraCore.is_null(request.configs_to_update):
            body['configsToUpdate'] = request.configs_to_update
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceConfigPreCheck',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/config/modifyInstanceConfigPreCheck',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceConfigPreCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_config_pre_check(
        self,
        request: main_models.ModifyInstanceConfigPreCheckRequest,
    ) -> main_models.ModifyInstanceConfigPreCheckResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_instance_config_pre_check_with_options(request, headers, runtime)

    async def modify_instance_config_pre_check_async(
        self,
        request: main_models.ModifyInstanceConfigPreCheckRequest,
    ) -> main_models.ModifyInstanceConfigPreCheckResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_instance_config_pre_check_with_options_async(request, headers, runtime)

    def modify_maintainable_time_with_options(
        self,
        request: main_models.ModifyMaintainableTimeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMaintainableTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.maintainable_time_period):
            query['MaintainableTimePeriod'] = request.maintainable_time_period
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMaintainableTime',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/starrocks/modifyMaintainableTime',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMaintainableTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_maintainable_time_with_options_async(
        self,
        request: main_models.ModifyMaintainableTimeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMaintainableTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.maintainable_time_period):
            query['MaintainableTimePeriod'] = request.maintainable_time_period
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMaintainableTime',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/starrocks/modifyMaintainableTime',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMaintainableTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_maintainable_time(
        self,
        request: main_models.ModifyMaintainableTimeRequest,
    ) -> main_models.ModifyMaintainableTimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_maintainable_time_with_options(request, headers, runtime)

    async def modify_maintainable_time_async(
        self,
        request: main_models.ModifyMaintainableTimeRequest,
    ) -> main_models.ModifyMaintainableTimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_maintainable_time_with_options_async(request, headers, runtime)

    def modify_node_number_with_options(
        self,
        request: main_models.ModifyNodeNumberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyNodeNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        if not DaraCore.is_null(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyNodeNumber',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/resourceChange/modifyNodeNumber',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyNodeNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_node_number_with_options_async(
        self,
        request: main_models.ModifyNodeNumberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyNodeNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        if not DaraCore.is_null(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyNodeNumber',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/resourceChange/modifyNodeNumber',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyNodeNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_node_number(
        self,
        request: main_models.ModifyNodeNumberRequest,
    ) -> main_models.ModifyNodeNumberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_node_number_with_options(request, headers, runtime)

    async def modify_node_number_async(
        self,
        request: main_models.ModifyNodeNumberRequest,
    ) -> main_models.ModifyNodeNumberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_node_number_with_options_async(request, headers, runtime)

    def modify_node_number_pre_check_with_options(
        self,
        request: main_models.ModifyNodeNumberPreCheckRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyNodeNumberPreCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyNodeNumberPreCheck',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/resourceChange/modifyNodeNumberPreCheck',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyNodeNumberPreCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_node_number_pre_check_with_options_async(
        self,
        request: main_models.ModifyNodeNumberPreCheckRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyNodeNumberPreCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyNodeNumberPreCheck',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/resourceChange/modifyNodeNumberPreCheck',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyNodeNumberPreCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_node_number_pre_check(
        self,
        request: main_models.ModifyNodeNumberPreCheckRequest,
    ) -> main_models.ModifyNodeNumberPreCheckResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_node_number_pre_check_with_options(request, headers, runtime)

    async def modify_node_number_pre_check_async(
        self,
        request: main_models.ModifyNodeNumberPreCheckRequest,
    ) -> main_models.ModifyNodeNumberPreCheckResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_node_number_pre_check_with_options_async(request, headers, runtime)

    def modify_scaling_rule_with_options(
        self,
        request: main_models.ModifyScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_trigger_type):
            query['NewTriggerType'] = request.new_trigger_type
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.old_trigger_type):
            query['OldTriggerType'] = request.old_trigger_type
        if not DaraCore.is_null(request.rule):
            query['Rule'] = request.rule
        if not DaraCore.is_null(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyScalingRule',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/scalingRule/modifyScalingRule',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scaling_rule_with_options_async(
        self,
        request: main_models.ModifyScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_trigger_type):
            query['NewTriggerType'] = request.new_trigger_type
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.old_trigger_type):
            query['OldTriggerType'] = request.old_trigger_type
        if not DaraCore.is_null(request.rule):
            query['Rule'] = request.rule
        if not DaraCore.is_null(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyScalingRule',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/scalingRule/modifyScalingRule',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scaling_rule(
        self,
        request: main_models.ModifyScalingRuleRequest,
    ) -> main_models.ModifyScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_scaling_rule_with_options(request, headers, runtime)

    async def modify_scaling_rule_async(
        self,
        request: main_models.ModifyScalingRuleRequest,
    ) -> main_models.ModifyScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_scaling_rule_with_options_async(request, headers, runtime)

    def modify_spec_type_with_options(
        self,
        request: main_models.ModifySpecTypeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifySpecTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fast_mode):
            query['FastMode'] = request.fast_mode
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target_spec_type):
            query['TargetSpecType'] = request.target_spec_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySpecType',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/resourceChange/modifySpecType',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySpecTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_spec_type_with_options_async(
        self,
        request: main_models.ModifySpecTypeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifySpecTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fast_mode):
            query['FastMode'] = request.fast_mode
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target_spec_type):
            query['TargetSpecType'] = request.target_spec_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySpecType',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/resourceChange/modifySpecType',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySpecTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_spec_type(
        self,
        request: main_models.ModifySpecTypeRequest,
    ) -> main_models.ModifySpecTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_spec_type_with_options(request, headers, runtime)

    async def modify_spec_type_async(
        self,
        request: main_models.ModifySpecTypeRequest,
    ) -> main_models.ModifySpecTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_spec_type_with_options_async(request, headers, runtime)

    def modify_spec_type_pre_check_with_options(
        self,
        request: main_models.ModifySpecTypePreCheckRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifySpecTypePreCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.target_spec_type):
            query['TargetSpecType'] = request.target_spec_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySpecTypePreCheck',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/resourceChange/modifySpecTypePreCheck',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySpecTypePreCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_spec_type_pre_check_with_options_async(
        self,
        request: main_models.ModifySpecTypePreCheckRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifySpecTypePreCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.target_spec_type):
            query['TargetSpecType'] = request.target_spec_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySpecTypePreCheck',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/resourceChange/modifySpecTypePreCheck',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySpecTypePreCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_spec_type_pre_check(
        self,
        request: main_models.ModifySpecTypePreCheckRequest,
    ) -> main_models.ModifySpecTypePreCheckResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_spec_type_pre_check_with_options(request, headers, runtime)

    async def modify_spec_type_pre_check_async(
        self,
        request: main_models.ModifySpecTypePreCheckRequest,
    ) -> main_models.ModifySpecTypePreCheckResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_spec_type_pre_check_with_options_async(request, headers, runtime)

    def modify_user_password_with_options(
        self,
        request: main_models.ModifyUserPasswordRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUserPassword',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/password/modify',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_password_with_options_async(
        self,
        request: main_models.ModifyUserPasswordRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUserPassword',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/password/modify',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user_password(
        self,
        request: main_models.ModifyUserPasswordRequest,
    ) -> main_models.ModifyUserPasswordResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_user_password_with_options(request, headers, runtime)

    async def modify_user_password_async(
        self,
        request: main_models.ModifyUserPasswordRequest,
    ) -> main_models.ModifyUserPasswordResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_user_password_with_options_async(request, headers, runtime)

    def query_enable_multi_az_price_with_options(
        self,
        request: main_models.QueryEnableMultiAzPriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryEnableMultiAzPriceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.observers):
            body['observers'] = request.observers
        if not DaraCore.is_null(request.promotion_option_no):
            body['promotionOptionNo'] = request.promotion_option_no
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryEnableMultiAzPrice',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/priceInquiry/enableMultiAz',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEnableMultiAzPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_enable_multi_az_price_with_options_async(
        self,
        request: main_models.QueryEnableMultiAzPriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryEnableMultiAzPriceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.observers):
            body['observers'] = request.observers
        if not DaraCore.is_null(request.promotion_option_no):
            body['promotionOptionNo'] = request.promotion_option_no
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryEnableMultiAzPrice',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/priceInquiry/enableMultiAz',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEnableMultiAzPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_enable_multi_az_price(
        self,
        request: main_models.QueryEnableMultiAzPriceRequest,
    ) -> main_models.QueryEnableMultiAzPriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_enable_multi_az_price_with_options(request, headers, runtime)

    async def query_enable_multi_az_price_async(
        self,
        request: main_models.QueryEnableMultiAzPriceRequest,
    ) -> main_models.QueryEnableMultiAzPriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_enable_multi_az_price_with_options_async(request, headers, runtime)

    def query_minor_version_with_options(
        self,
        request: main_models.QueryMinorVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryMinorVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMinorVersion',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/starrocks/queryAppDefineVersion',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMinorVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_minor_version_with_options_async(
        self,
        request: main_models.QueryMinorVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryMinorVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMinorVersion',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/starrocks/queryAppDefineVersion',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMinorVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_minor_version(
        self,
        request: main_models.QueryMinorVersionRequest,
    ) -> main_models.QueryMinorVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_minor_version_with_options(request, headers, runtime)

    async def query_minor_version_async(
        self,
        request: main_models.QueryMinorVersionRequest,
    ) -> main_models.QueryMinorVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_minor_version_with_options_async(request, headers, runtime)

    def query_modify_charge_type_price_with_options(
        self,
        request: main_models.QueryModifyChargeTypePriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryModifyChargeTypePriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.billing_instance_ids):
            query['BillingInstanceIds'] = request.billing_instance_ids
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryModifyChargeTypePrice',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/buy/query_modify_charge_type_price',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryModifyChargeTypePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_modify_charge_type_price_with_options_async(
        self,
        request: main_models.QueryModifyChargeTypePriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryModifyChargeTypePriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.billing_instance_ids):
            query['BillingInstanceIds'] = request.billing_instance_ids
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryModifyChargeTypePrice',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/buy/query_modify_charge_type_price',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryModifyChargeTypePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_modify_charge_type_price(
        self,
        request: main_models.QueryModifyChargeTypePriceRequest,
    ) -> main_models.QueryModifyChargeTypePriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_modify_charge_type_price_with_options(request, headers, runtime)

    async def query_modify_charge_type_price_async(
        self,
        request: main_models.QueryModifyChargeTypePriceRequest,
    ) -> main_models.QueryModifyChargeTypePriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_modify_charge_type_price_with_options_async(request, headers, runtime)

    def query_modify_cu_price_with_options(
        self,
        request: main_models.QueryModifyCuPriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryModifyCuPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryModifyCuPrice',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/priceInquiry/modifyCu',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryModifyCuPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_modify_cu_price_with_options_async(
        self,
        request: main_models.QueryModifyCuPriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryModifyCuPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryModifyCuPrice',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/priceInquiry/modifyCu',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryModifyCuPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_modify_cu_price(
        self,
        request: main_models.QueryModifyCuPriceRequest,
    ) -> main_models.QueryModifyCuPriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_modify_cu_price_with_options(request, headers, runtime)

    async def query_modify_cu_price_async(
        self,
        request: main_models.QueryModifyCuPriceRequest,
    ) -> main_models.QueryModifyCuPriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_modify_cu_price_with_options_async(request, headers, runtime)

    def query_modify_disk_number_price_with_options(
        self,
        request: main_models.QueryModifyDiskNumberPriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryModifyDiskNumberPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryModifyDiskNumberPrice',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/priceInquiry/modifyDiskNumber',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryModifyDiskNumberPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_modify_disk_number_price_with_options_async(
        self,
        request: main_models.QueryModifyDiskNumberPriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryModifyDiskNumberPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryModifyDiskNumberPrice',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/priceInquiry/modifyDiskNumber',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryModifyDiskNumberPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_modify_disk_number_price(
        self,
        request: main_models.QueryModifyDiskNumberPriceRequest,
    ) -> main_models.QueryModifyDiskNumberPriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_modify_disk_number_price_with_options(request, headers, runtime)

    async def query_modify_disk_number_price_async(
        self,
        request: main_models.QueryModifyDiskNumberPriceRequest,
    ) -> main_models.QueryModifyDiskNumberPriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_modify_disk_number_price_with_options_async(request, headers, runtime)

    def query_modify_disk_performance_level_price_with_options(
        self,
        request: main_models.QueryModifyDiskPerformanceLevelPriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryModifyDiskPerformanceLevelPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryModifyDiskPerformanceLevelPrice',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/priceInquiry/modifyDiskPerformanceLevel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryModifyDiskPerformanceLevelPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_modify_disk_performance_level_price_with_options_async(
        self,
        request: main_models.QueryModifyDiskPerformanceLevelPriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryModifyDiskPerformanceLevelPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryModifyDiskPerformanceLevelPrice',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/priceInquiry/modifyDiskPerformanceLevel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryModifyDiskPerformanceLevelPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_modify_disk_performance_level_price(
        self,
        request: main_models.QueryModifyDiskPerformanceLevelPriceRequest,
    ) -> main_models.QueryModifyDiskPerformanceLevelPriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_modify_disk_performance_level_price_with_options(request, headers, runtime)

    async def query_modify_disk_performance_level_price_async(
        self,
        request: main_models.QueryModifyDiskPerformanceLevelPriceRequest,
    ) -> main_models.QueryModifyDiskPerformanceLevelPriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_modify_disk_performance_level_price_with_options_async(request, headers, runtime)

    def query_modify_disk_size_price_with_options(
        self,
        request: main_models.QueryModifyDiskSizePriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryModifyDiskSizePriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryModifyDiskSizePrice',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/priceInquiry/modifyDiskSize',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryModifyDiskSizePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_modify_disk_size_price_with_options_async(
        self,
        request: main_models.QueryModifyDiskSizePriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryModifyDiskSizePriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryModifyDiskSizePrice',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/priceInquiry/modifyDiskSize',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryModifyDiskSizePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_modify_disk_size_price(
        self,
        request: main_models.QueryModifyDiskSizePriceRequest,
    ) -> main_models.QueryModifyDiskSizePriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_modify_disk_size_price_with_options(request, headers, runtime)

    async def query_modify_disk_size_price_async(
        self,
        request: main_models.QueryModifyDiskSizePriceRequest,
    ) -> main_models.QueryModifyDiskSizePriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_modify_disk_size_price_with_options_async(request, headers, runtime)

    def query_modify_disk_type_price_with_options(
        self,
        request: main_models.QueryModifyDiskTypePriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryModifyDiskTypePriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target_disk_type):
            query['TargetDiskType'] = request.target_disk_type
        if not DaraCore.is_null(request.target_performance_level):
            query['TargetPerformanceLevel'] = request.target_performance_level
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryModifyDiskTypePrice',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/priceInquiry/modifyDiskType',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryModifyDiskTypePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_modify_disk_type_price_with_options_async(
        self,
        request: main_models.QueryModifyDiskTypePriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryModifyDiskTypePriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target_disk_type):
            query['TargetDiskType'] = request.target_disk_type
        if not DaraCore.is_null(request.target_performance_level):
            query['TargetPerformanceLevel'] = request.target_performance_level
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryModifyDiskTypePrice',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/priceInquiry/modifyDiskType',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryModifyDiskTypePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_modify_disk_type_price(
        self,
        request: main_models.QueryModifyDiskTypePriceRequest,
    ) -> main_models.QueryModifyDiskTypePriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_modify_disk_type_price_with_options(request, headers, runtime)

    async def query_modify_disk_type_price_async(
        self,
        request: main_models.QueryModifyDiskTypePriceRequest,
    ) -> main_models.QueryModifyDiskTypePriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_modify_disk_type_price_with_options_async(request, headers, runtime)

    def query_modify_node_number_price_with_options(
        self,
        request: main_models.QueryModifyNodeNumberPriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryModifyNodeNumberPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryModifyNodeNumberPrice',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/priceInquiry/modifyNodeNumber',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryModifyNodeNumberPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_modify_node_number_price_with_options_async(
        self,
        request: main_models.QueryModifyNodeNumberPriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryModifyNodeNumberPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryModifyNodeNumberPrice',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/priceInquiry/modifyNodeNumber',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryModifyNodeNumberPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_modify_node_number_price(
        self,
        request: main_models.QueryModifyNodeNumberPriceRequest,
    ) -> main_models.QueryModifyNodeNumberPriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_modify_node_number_price_with_options(request, headers, runtime)

    async def query_modify_node_number_price_async(
        self,
        request: main_models.QueryModifyNodeNumberPriceRequest,
    ) -> main_models.QueryModifyNodeNumberPriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_modify_node_number_price_with_options_async(request, headers, runtime)

    def query_modify_spec_type_price_with_options(
        self,
        request: main_models.QueryModifySpecTypePriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryModifySpecTypePriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target_spec_type):
            query['TargetSpecType'] = request.target_spec_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryModifySpecTypePrice',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/priceInquiry/modifySpecType',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryModifySpecTypePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_modify_spec_type_price_with_options_async(
        self,
        request: main_models.QueryModifySpecTypePriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryModifySpecTypePriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.target_spec_type):
            query['TargetSpecType'] = request.target_spec_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryModifySpecTypePrice',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/priceInquiry/modifySpecType',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryModifySpecTypePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_modify_spec_type_price(
        self,
        request: main_models.QueryModifySpecTypePriceRequest,
    ) -> main_models.QueryModifySpecTypePriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_modify_spec_type_price_with_options(request, headers, runtime)

    async def query_modify_spec_type_price_async(
        self,
        request: main_models.QueryModifySpecTypePriceRequest,
    ) -> main_models.QueryModifySpecTypePriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_modify_spec_type_price_with_options_async(request, headers, runtime)

    def query_price_v1with_options(
        self,
        request: main_models.QueryPriceV1Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryPriceV1Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_node_group):
            body['AgentNodeGroup'] = request.agent_node_group
        if not DaraCore.is_null(request.backend_node_groups):
            body['BackendNodeGroups'] = request.backend_node_groups
        if not DaraCore.is_null(request.duration):
            body['Duration'] = request.duration
        if not DaraCore.is_null(request.frontend_node_groups):
            body['FrontendNodeGroups'] = request.frontend_node_groups
        if not DaraCore.is_null(request.observer_node_groups):
            body['ObserverNodeGroups'] = request.observer_node_groups
        if not DaraCore.is_null(request.package_type):
            body['PackageType'] = request.package_type
        if not DaraCore.is_null(request.pay_type):
            body['PayType'] = request.pay_type
        if not DaraCore.is_null(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.promotion_option_no):
            body['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.run_mode):
            body['RunMode'] = request.run_mode
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryPriceV1',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/price/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPriceV1Response(),
            self.call_api(params, req, runtime)
        )

    async def query_price_v1with_options_async(
        self,
        request: main_models.QueryPriceV1Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryPriceV1Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_node_group):
            body['AgentNodeGroup'] = request.agent_node_group
        if not DaraCore.is_null(request.backend_node_groups):
            body['BackendNodeGroups'] = request.backend_node_groups
        if not DaraCore.is_null(request.duration):
            body['Duration'] = request.duration
        if not DaraCore.is_null(request.frontend_node_groups):
            body['FrontendNodeGroups'] = request.frontend_node_groups
        if not DaraCore.is_null(request.observer_node_groups):
            body['ObserverNodeGroups'] = request.observer_node_groups
        if not DaraCore.is_null(request.package_type):
            body['PackageType'] = request.package_type
        if not DaraCore.is_null(request.pay_type):
            body['PayType'] = request.pay_type
        if not DaraCore.is_null(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.promotion_option_no):
            body['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.run_mode):
            body['RunMode'] = request.run_mode
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryPriceV1',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/price/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPriceV1Response(),
            await self.call_api_async(params, req, runtime)
        )

    def query_price_v1(
        self,
        request: main_models.QueryPriceV1Request,
    ) -> main_models.QueryPriceV1Response:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_price_v1with_options(request, headers, runtime)

    async def query_price_v1_async(
        self,
        request: main_models.QueryPriceV1Request,
    ) -> main_models.QueryPriceV1Response:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_price_v1with_options_async(request, headers, runtime)

    def query_refund_price_with_options(
        self,
        request: main_models.QueryRefundPriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryRefundPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.billing_instance_ids):
            query['billingInstanceIds'] = request.billing_instance_ids
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRefundPrice',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/buy/queryRefundPrice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRefundPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_refund_price_with_options_async(
        self,
        request: main_models.QueryRefundPriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryRefundPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.billing_instance_ids):
            query['billingInstanceIds'] = request.billing_instance_ids
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRefundPrice',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/buy/queryRefundPrice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRefundPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_refund_price(
        self,
        request: main_models.QueryRefundPriceRequest,
    ) -> main_models.QueryRefundPriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_refund_price_with_options(request, headers, runtime)

    async def query_refund_price_async(
        self,
        request: main_models.QueryRefundPriceRequest,
    ) -> main_models.QueryRefundPriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_refund_price_with_options_async(request, headers, runtime)

    def query_renew_price_with_options(
        self,
        request: main_models.QueryRenewPriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryRenewPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.billing_instance_ids):
            query['BillingInstanceIds'] = request.billing_instance_ids
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRenewPrice',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/price/renew',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRenewPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_renew_price_with_options_async(
        self,
        request: main_models.QueryRenewPriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryRenewPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.billing_instance_ids):
            query['BillingInstanceIds'] = request.billing_instance_ids
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRenewPrice',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/price/renew',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRenewPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_renew_price(
        self,
        request: main_models.QueryRenewPriceRequest,
    ) -> main_models.QueryRenewPriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_renew_price_with_options(request, headers, runtime)

    async def query_renew_price_async(
        self,
        request: main_models.QueryRenewPriceRequest,
    ) -> main_models.QueryRenewPriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_renew_price_with_options_async(request, headers, runtime)

    def query_unpaid_order_with_options(
        self,
        request: main_models.QueryUnpaidOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryUnpaidOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.billing_instance_id):
            query['BillingInstanceId'] = request.billing_instance_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUnpaidOrder',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/order/queryUnpaidOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUnpaidOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_unpaid_order_with_options_async(
        self,
        request: main_models.QueryUnpaidOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryUnpaidOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.billing_instance_id):
            query['BillingInstanceId'] = request.billing_instance_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUnpaidOrder',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/order/queryUnpaidOrder',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUnpaidOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_unpaid_order(
        self,
        request: main_models.QueryUnpaidOrderRequest,
    ) -> main_models.QueryUnpaidOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_unpaid_order_with_options(request, headers, runtime)

    async def query_unpaid_order_async(
        self,
        request: main_models.QueryUnpaidOrderRequest,
    ) -> main_models.QueryUnpaidOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_unpaid_order_with_options_async(request, headers, runtime)

    def query_upgradable_versions_with_options(
        self,
        request: main_models.QueryUpgradableVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryUpgradableVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.minor):
            query['Minor'] = request.minor
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUpgradableVersions',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/starrocks/queryUpgradableVersions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUpgradableVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_upgradable_versions_with_options_async(
        self,
        request: main_models.QueryUpgradableVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryUpgradableVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.minor):
            query['Minor'] = request.minor
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUpgradableVersions',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/starrocks/queryUpgradableVersions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUpgradableVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_upgradable_versions(
        self,
        request: main_models.QueryUpgradableVersionsRequest,
    ) -> main_models.QueryUpgradableVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_upgradable_versions_with_options(request, headers, runtime)

    async def query_upgradable_versions_async(
        self,
        request: main_models.QueryUpgradableVersionsRequest,
    ) -> main_models.QueryUpgradableVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_upgradable_versions_with_options_async(request, headers, runtime)

    def reboot_ecswith_options(
        self,
        request: main_models.RebootECSRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RebootECSResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.reboot_time):
            query['RebootTime'] = request.reboot_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RebootECS',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/event/rebootEcs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebootECSResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_ecswith_options_async(
        self,
        request: main_models.RebootECSRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RebootECSResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.reboot_time):
            query['RebootTime'] = request.reboot_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RebootECS',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/event/rebootEcs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebootECSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reboot_ecs(
        self,
        request: main_models.RebootECSRequest,
    ) -> main_models.RebootECSResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.reboot_ecswith_options(request, headers, runtime)

    async def reboot_ecs_async(
        self,
        request: main_models.RebootECSRequest,
    ) -> main_models.RebootECSResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.reboot_ecswith_options_async(request, headers, runtime)

    def release_instance_with_options(
        self,
        request: main_models.ReleaseInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseInstance',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/cluster/release',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_instance_with_options_async(
        self,
        request: main_models.ReleaseInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseInstance',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/cluster/release',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_instance(
        self,
        request: main_models.ReleaseInstanceRequest,
    ) -> main_models.ReleaseInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.release_instance_with_options(request, headers, runtime)

    async def release_instance_async(
        self,
        request: main_models.ReleaseInstanceRequest,
    ) -> main_models.ReleaseInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.release_instance_with_options_async(request, headers, runtime)

    def renew_instance_with_options(
        self,
        request: main_models.RenewInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RenewInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.billing_instance_ids):
            query['BillingInstanceIds'] = request.billing_instance_ids
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewInstance',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/order/renew_instance',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: main_models.RenewInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RenewInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.billing_instance_ids):
            query['BillingInstanceIds'] = request.billing_instance_ids
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewInstance',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/order/renew_instance',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_instance(
        self,
        request: main_models.RenewInstanceRequest,
    ) -> main_models.RenewInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.renew_instance_with_options(request, headers, runtime)

    async def renew_instance_async(
        self,
        request: main_models.RenewInstanceRequest,
    ) -> main_models.RenewInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.renew_instance_with_options_async(request, headers, runtime)

    def restart_instance_with_options(
        self,
        request: main_models.RestartInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fast_mode):
            query['FastMode'] = request.fast_mode
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartInstance',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/starrocks/restartCluster',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_instance_with_options_async(
        self,
        request: main_models.RestartInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fast_mode):
            query['FastMode'] = request.fast_mode
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartInstance',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/starrocks/restartCluster',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_instance(
        self,
        request: main_models.RestartInstanceRequest,
    ) -> main_models.RestartInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.restart_instance_with_options(request, headers, runtime)

    async def restart_instance_async(
        self,
        request: main_models.RestartInstanceRequest,
    ) -> main_models.RestartInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.restart_instance_with_options_async(request, headers, runtime)

    def restart_node_group_with_options(
        self,
        request: main_models.RestartNodeGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartNodeGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fast_mode):
            query['FastMode'] = request.fast_mode
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartNodeGroup',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/nodegroup/restart',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartNodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_node_group_with_options_async(
        self,
        request: main_models.RestartNodeGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartNodeGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fast_mode):
            query['FastMode'] = request.fast_mode
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartNodeGroup',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/nodegroup/restart',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartNodeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_node_group(
        self,
        request: main_models.RestartNodeGroupRequest,
    ) -> main_models.RestartNodeGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.restart_node_group_with_options(request, headers, runtime)

    async def restart_node_group_async(
        self,
        request: main_models.RestartNodeGroupRequest,
    ) -> main_models.RestartNodeGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.restart_node_group_with_options_async(request, headers, runtime)

    def restart_nodes_with_options(
        self,
        request: main_models.RestartNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not DaraCore.is_null(request.restart_node_groups):
            body['RestartNodeGroups'] = request.restart_node_groups
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RestartNodes',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/restart/restart',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_nodes_with_options_async(
        self,
        request: main_models.RestartNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not DaraCore.is_null(request.restart_node_groups):
            body['RestartNodeGroups'] = request.restart_node_groups
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RestartNodes',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/restart/restart',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_nodes(
        self,
        request: main_models.RestartNodesRequest,
    ) -> main_models.RestartNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.restart_nodes_with_options(request, headers, runtime)

    async def restart_nodes_async(
        self,
        request: main_models.RestartNodesRequest,
    ) -> main_models.RestartNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.restart_nodes_with_options_async(request, headers, runtime)

    def restore_instance_with_options(
        self,
        request: main_models.RestoreInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestoreInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.admin_password):
            body['AdminPassword'] = request.admin_password
        if not DaraCore.is_null(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.backup_task_id):
            body['BackupTaskId'] = request.backup_task_id
        if not DaraCore.is_null(request.duration):
            body['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.pay_type):
            body['PayType'] = request.pay_type
        if not DaraCore.is_null(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        if not DaraCore.is_null(request.v_switches):
            body['VSwitches'] = request.v_switches
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RestoreInstance',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/restore/restoreInstance',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestoreInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restore_instance_with_options_async(
        self,
        request: main_models.RestoreInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestoreInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.admin_password):
            body['AdminPassword'] = request.admin_password
        if not DaraCore.is_null(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.backup_task_id):
            body['BackupTaskId'] = request.backup_task_id
        if not DaraCore.is_null(request.duration):
            body['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.pay_type):
            body['PayType'] = request.pay_type
        if not DaraCore.is_null(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        if not DaraCore.is_null(request.v_switches):
            body['VSwitches'] = request.v_switches
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RestoreInstance',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/restore/restoreInstance',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestoreInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restore_instance(
        self,
        request: main_models.RestoreInstanceRequest,
    ) -> main_models.RestoreInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.restore_instance_with_options(request, headers, runtime)

    async def restore_instance_async(
        self,
        request: main_models.RestoreInstanceRequest,
    ) -> main_models.RestoreInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.restore_instance_with_options_async(request, headers, runtime)

    def resume_instance_with_options(
        self,
        request: main_models.ResumeInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResumeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeInstance',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/lifecycle/resumeInstance',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_instance_with_options_async(
        self,
        request: main_models.ResumeInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResumeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeInstance',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/lifecycle/resumeInstance',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_instance(
        self,
        request: main_models.ResumeInstanceRequest,
    ) -> main_models.ResumeInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.resume_instance_with_options(request, headers, runtime)

    async def resume_instance_async(
        self,
        request: main_models.ResumeInstanceRequest,
    ) -> main_models.ResumeInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.resume_instance_with_options_async(request, headers, runtime)

    def rollback_config_modification_with_options(
        self,
        request: main_models.RollbackConfigModificationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RollbackConfigModificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_history_id):
            query['ConfigHistoryId'] = request.config_history_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.restart):
            query['Restart'] = request.restart
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackConfigModification',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/config/rollbackConfigModification',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackConfigModificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_config_modification_with_options_async(
        self,
        request: main_models.RollbackConfigModificationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RollbackConfigModificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_history_id):
            query['ConfigHistoryId'] = request.config_history_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.restart):
            query['Restart'] = request.restart
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackConfigModification',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/config/rollbackConfigModification',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackConfigModificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_config_modification(
        self,
        request: main_models.RollbackConfigModificationRequest,
    ) -> main_models.RollbackConfigModificationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.rollback_config_modification_with_options(request, headers, runtime)

    async def rollback_config_modification_async(
        self,
        request: main_models.RollbackConfigModificationRequest,
    ) -> main_models.RollbackConfigModificationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.rollback_config_modification_with_options_async(request, headers, runtime)

    def switch_active_standby_zones_with_options(
        self,
        request: main_models.SwitchActiveStandbyZonesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SwitchActiveStandbyZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.target_zone_id):
            query['TargetZoneId'] = request.target_zone_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchActiveStandbyZones',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/recovery/switchZones',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchActiveStandbyZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_active_standby_zones_with_options_async(
        self,
        request: main_models.SwitchActiveStandbyZonesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SwitchActiveStandbyZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.target_zone_id):
            query['TargetZoneId'] = request.target_zone_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchActiveStandbyZones',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/recovery/switchZones',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchActiveStandbyZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_active_standby_zones(
        self,
        request: main_models.SwitchActiveStandbyZonesRequest,
    ) -> main_models.SwitchActiveStandbyZonesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.switch_active_standby_zones_with_options(request, headers, runtime)

    async def switch_active_standby_zones_async(
        self,
        request: main_models.SwitchActiveStandbyZonesRequest,
    ) -> main_models.SwitchActiveStandbyZonesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.switch_active_standby_zones_with_options_async(request, headers, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.tag_resources_with_options_async(request, headers, runtime)

    def toggle_auto_minor_version_upgrade_with_options(
        self,
        request: main_models.ToggleAutoMinorVersionUpgradeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ToggleAutoMinorVersionUpgradeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_upgrade):
            query['AutoUpgrade'] = request.auto_upgrade
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ToggleAutoMinorVersionUpgrade',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/starrocks/toggleAutoMinorVersionUpgrade',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ToggleAutoMinorVersionUpgradeResponse(),
            self.call_api(params, req, runtime)
        )

    async def toggle_auto_minor_version_upgrade_with_options_async(
        self,
        request: main_models.ToggleAutoMinorVersionUpgradeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ToggleAutoMinorVersionUpgradeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_upgrade):
            query['AutoUpgrade'] = request.auto_upgrade
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ToggleAutoMinorVersionUpgrade',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/starrocks/toggleAutoMinorVersionUpgrade',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ToggleAutoMinorVersionUpgradeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def toggle_auto_minor_version_upgrade(
        self,
        request: main_models.ToggleAutoMinorVersionUpgradeRequest,
    ) -> main_models.ToggleAutoMinorVersionUpgradeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.toggle_auto_minor_version_upgrade_with_options(request, headers, runtime)

    async def toggle_auto_minor_version_upgrade_async(
        self,
        request: main_models.ToggleAutoMinorVersionUpgradeRequest,
    ) -> main_models.ToggleAutoMinorVersionUpgradeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.toggle_auto_minor_version_upgrade_with_options_async(request, headers, runtime)

    def toggle_public_slb_with_options(
        self,
        request: main_models.TogglePublicSlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TogglePublicSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_public_slb):
            query['EnablePublicSlb'] = request.enable_public_slb
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TogglePublicSlb',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/gateway/togglePublicSlb',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TogglePublicSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def toggle_public_slb_with_options_async(
        self,
        request: main_models.TogglePublicSlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TogglePublicSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_public_slb):
            query['EnablePublicSlb'] = request.enable_public_slb
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TogglePublicSlb',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/gateway/togglePublicSlb',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TogglePublicSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def toggle_public_slb(
        self,
        request: main_models.TogglePublicSlbRequest,
    ) -> main_models.TogglePublicSlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.toggle_public_slb_with_options(request, headers, runtime)

    async def toggle_public_slb_async(
        self,
        request: main_models.TogglePublicSlbRequest,
    ) -> main_models.TogglePublicSlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.toggle_public_slb_with_options_async(request, headers, runtime)

    def un_tag_resources_with_options(
        self,
        tmp_req: main_models.UnTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnTagResourcesResponse:
        tmp_req.validate()
        request = main_models.UnTagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not DaraCore.is_null(tmp_req.tag_key):
            request.tag_key_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_key, 'TagKey', 'json')
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key_shrink):
            query['TagKey'] = request.tag_key_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnTagResources',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/tags',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_tag_resources_with_options_async(
        self,
        tmp_req: main_models.UnTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnTagResourcesResponse:
        tmp_req.validate()
        request = main_models.UnTagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not DaraCore.is_null(tmp_req.tag_key):
            request.tag_key_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_key, 'TagKey', 'json')
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key_shrink):
            query['TagKey'] = request.tag_key_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnTagResources',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/tags',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_tag_resources(
        self,
        request: main_models.UnTagResourcesRequest,
    ) -> main_models.UnTagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.un_tag_resources_with_options(request, headers, runtime)

    async def un_tag_resources_async(
        self,
        request: main_models.UnTagResourcesRequest,
    ) -> main_models.UnTagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.un_tag_resources_with_options_async(request, headers, runtime)

    def update_backup_with_options(
        self,
        request: main_models.UpdateBackupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.backup_task_id):
            body['backupTaskId'] = request.backup_task_id
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBackup',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/backup/manage/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_backup_with_options_async(
        self,
        request: main_models.UpdateBackupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.backup_task_id):
            body['backupTaskId'] = request.backup_task_id
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBackup',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/backup/manage/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_backup(
        self,
        request: main_models.UpdateBackupRequest,
    ) -> main_models.UpdateBackupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_backup_with_options(request, headers, runtime)

    async def update_backup_async(
        self,
        request: main_models.UpdateBackupRequest,
    ) -> main_models.UpdateBackupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_backup_with_options_async(request, headers, runtime)

    def update_backup_policy_with_options(
        self,
        request: main_models.UpdateBackupPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBackupPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.expire_days):
            body['ExpireDays'] = request.expire_days
        if not DaraCore.is_null(request.hour):
            body['Hour'] = request.hour
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.minute):
            body['Minute'] = request.minute
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.recurrence_values):
            body['RecurrenceValues'] = request.recurrence_values
        if not DaraCore.is_null(request.timeout_seconds):
            body['TimeoutSeconds'] = request.timeout_seconds
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBackupPolicy',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/backupRestore/policy/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_backup_policy_with_options_async(
        self,
        request: main_models.UpdateBackupPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBackupPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.expire_days):
            body['ExpireDays'] = request.expire_days
        if not DaraCore.is_null(request.hour):
            body['Hour'] = request.hour
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.minute):
            body['Minute'] = request.minute
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.recurrence_values):
            body['RecurrenceValues'] = request.recurrence_values
        if not DaraCore.is_null(request.timeout_seconds):
            body['TimeoutSeconds'] = request.timeout_seconds
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBackupPolicy',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/backupRestore/policy/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_backup_policy(
        self,
        request: main_models.UpdateBackupPolicyRequest,
    ) -> main_models.UpdateBackupPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_backup_policy_with_options(request, headers, runtime)

    async def update_backup_policy_async(
        self,
        request: main_models.UpdateBackupPolicyRequest,
    ) -> main_models.UpdateBackupPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_backup_policy_with_options_async(request, headers, runtime)

    def update_gateway_with_options(
        self,
        request: main_models.UpdateGatewayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fe_node_number):
            query['FeNodeNumber'] = request.fe_node_number
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_name):
            query['GatewayName'] = request.gateway_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGateway',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/gateway/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_with_options_async(
        self,
        request: main_models.UpdateGatewayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fe_node_number):
            query['FeNodeNumber'] = request.fe_node_number
        if not DaraCore.is_null(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_name):
            query['GatewayName'] = request.gateway_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGateway',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/gateway/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway(
        self,
        request: main_models.UpdateGatewayRequest,
    ) -> main_models.UpdateGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_gateway_with_options(request, headers, runtime)

    async def update_gateway_async(
        self,
        request: main_models.UpdateGatewayRequest,
    ) -> main_models.UpdateGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_gateway_with_options_async(request, headers, runtime)

    def update_inner_ip_whitelist_group_with_options(
        self,
        request: main_models.UpdateInnerIpWhitelistGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInnerIpWhitelistGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cidr_ip_list):
            body['CidrIpList'] = request.cidr_ip_list
        if not DaraCore.is_null(request.inner_ip_whitelist_group_id):
            body['InnerIpWhitelistGroupId'] = request.inner_ip_whitelist_group_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInnerIpWhitelistGroup',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/securityGroup/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInnerIpWhitelistGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_inner_ip_whitelist_group_with_options_async(
        self,
        request: main_models.UpdateInnerIpWhitelistGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInnerIpWhitelistGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cidr_ip_list):
            body['CidrIpList'] = request.cidr_ip_list
        if not DaraCore.is_null(request.inner_ip_whitelist_group_id):
            body['InnerIpWhitelistGroupId'] = request.inner_ip_whitelist_group_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInnerIpWhitelistGroup',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/securityGroup/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInnerIpWhitelistGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_inner_ip_whitelist_group(
        self,
        request: main_models.UpdateInnerIpWhitelistGroupRequest,
    ) -> main_models.UpdateInnerIpWhitelistGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_inner_ip_whitelist_group_with_options(request, headers, runtime)

    async def update_inner_ip_whitelist_group_async(
        self,
        request: main_models.UpdateInnerIpWhitelistGroupRequest,
    ) -> main_models.UpdateInnerIpWhitelistGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_inner_ip_whitelist_group_with_options_async(request, headers, runtime)

    def update_instance_name_with_options(
        self,
        request: main_models.UpdateInstanceNameRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceName',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/cluster/update_name',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_name_with_options_async(
        self,
        request: main_models.UpdateInstanceNameRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceName',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/cluster/update_name',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_name(
        self,
        request: main_models.UpdateInstanceNameRequest,
    ) -> main_models.UpdateInstanceNameResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_instance_name_with_options(request, headers, runtime)

    async def update_instance_name_async(
        self,
        request: main_models.UpdateInstanceNameRequest,
    ) -> main_models.UpdateInstanceNameResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_instance_name_with_options_async(request, headers, runtime)

    def update_node_group_description_with_options(
        self,
        request: main_models.UpdateNodeGroupDescriptionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNodeGroupDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.x_acs_ram_auth_context):
            query['X-Acs-Ram-Auth-Context'] = request.x_acs_ram_auth_context
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNodeGroupDescription',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/nodegroup/updateDescription',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNodeGroupDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_node_group_description_with_options_async(
        self,
        request: main_models.UpdateNodeGroupDescriptionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNodeGroupDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.x_acs_ram_auth_context):
            query['X-Acs-Ram-Auth-Context'] = request.x_acs_ram_auth_context
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNodeGroupDescription',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/nodegroup/updateDescription',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNodeGroupDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_node_group_description(
        self,
        request: main_models.UpdateNodeGroupDescriptionRequest,
    ) -> main_models.UpdateNodeGroupDescriptionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_node_group_description_with_options(request, headers, runtime)

    async def update_node_group_description_async(
        self,
        request: main_models.UpdateNodeGroupDescriptionRequest,
    ) -> main_models.UpdateNodeGroupDescriptionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_node_group_description_with_options_async(request, headers, runtime)

    def update_public_network_status_with_options(
        self,
        request: main_models.UpdatePublicNetworkStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePublicNetworkStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.component_type):
            query['ComponentType'] = request.component_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.public_network_enabled):
            query['PublicNetworkEnabled'] = request.public_network_enabled
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePublicNetworkStatus',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/network/updatePublicNetworkStatus',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePublicNetworkStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_public_network_status_with_options_async(
        self,
        request: main_models.UpdatePublicNetworkStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePublicNetworkStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.component_type):
            query['ComponentType'] = request.component_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.public_network_enabled):
            query['PublicNetworkEnabled'] = request.public_network_enabled
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePublicNetworkStatus',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/network/updatePublicNetworkStatus',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePublicNetworkStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_public_network_status(
        self,
        request: main_models.UpdatePublicNetworkStatusRequest,
    ) -> main_models.UpdatePublicNetworkStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_public_network_status_with_options(request, headers, runtime)

    async def update_public_network_status_async(
        self,
        request: main_models.UpdatePublicNetworkStatusRequest,
    ) -> main_models.UpdatePublicNetworkStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_public_network_status_with_options_async(request, headers, runtime)

    def upgrade_version_with_options(
        self,
        request: main_models.UpgradeVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fast_mode):
            query['FastMode'] = request.fast_mode
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.minor):
            query['Minor'] = request.minor
        if not DaraCore.is_null(request.target_version):
            query['TargetVersion'] = request.target_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeVersion',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/starrocks/upgradeVersion',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_version_with_options_async(
        self,
        request: main_models.UpgradeVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fast_mode):
            query['FastMode'] = request.fast_mode
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.minor):
            query['Minor'] = request.minor
        if not DaraCore.is_null(request.target_version):
            query['TargetVersion'] = request.target_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeVersion',
            version = '2022-10-19',
            protocol = 'HTTPS',
            pathname = f'/webapi/starrocks/upgradeVersion',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_version(
        self,
        request: main_models.UpgradeVersionRequest,
    ) -> main_models.UpgradeVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.upgrade_version_with_options(request, headers, runtime)

    async def upgrade_version_async(
        self,
        request: main_models.UpgradeVersionRequest,
    ) -> main_models.UpgradeVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.upgrade_version_with_options_async(request, headers, runtime)
