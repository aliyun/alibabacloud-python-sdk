# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_expressconnectrouter20230901 import models as main_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('expressconnectrouter', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def activate_flow_log_with_options(
        self,
        request: main_models.ActivateFlowLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ActivateFlowLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.flow_log_id):
            body['FlowLogId'] = request.flow_log_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ActivateFlowLog',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActivateFlowLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_flow_log_with_options_async(
        self,
        request: main_models.ActivateFlowLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ActivateFlowLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.flow_log_id):
            body['FlowLogId'] = request.flow_log_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ActivateFlowLog',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActivateFlowLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def activate_flow_log(
        self,
        request: main_models.ActivateFlowLogRequest,
    ) -> main_models.ActivateFlowLogResponse:
        runtime = RuntimeOptions()
        return self.activate_flow_log_with_options(request, runtime)

    async def activate_flow_log_async(
        self,
        request: main_models.ActivateFlowLogRequest,
    ) -> main_models.ActivateFlowLogResponse:
        runtime = RuntimeOptions()
        return await self.activate_flow_log_with_options_async(request, runtime)

    def attach_express_connect_router_child_instance_with_options(
        self,
        request: main_models.AttachExpressConnectRouterChildInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachExpressConnectRouterChildInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.child_instance_id):
            body['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_owner_id):
            body['ChildInstanceOwnerId'] = request.child_instance_owner_id
        if not DaraCore.is_null(request.child_instance_region_id):
            body['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_type):
            body['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AttachExpressConnectRouterChildInstance',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachExpressConnectRouterChildInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_express_connect_router_child_instance_with_options_async(
        self,
        request: main_models.AttachExpressConnectRouterChildInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachExpressConnectRouterChildInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.child_instance_id):
            body['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_owner_id):
            body['ChildInstanceOwnerId'] = request.child_instance_owner_id
        if not DaraCore.is_null(request.child_instance_region_id):
            body['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_type):
            body['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AttachExpressConnectRouterChildInstance',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachExpressConnectRouterChildInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_express_connect_router_child_instance(
        self,
        request: main_models.AttachExpressConnectRouterChildInstanceRequest,
    ) -> main_models.AttachExpressConnectRouterChildInstanceResponse:
        runtime = RuntimeOptions()
        return self.attach_express_connect_router_child_instance_with_options(request, runtime)

    async def attach_express_connect_router_child_instance_async(
        self,
        request: main_models.AttachExpressConnectRouterChildInstanceRequest,
    ) -> main_models.AttachExpressConnectRouterChildInstanceResponse:
        runtime = RuntimeOptions()
        return await self.attach_express_connect_router_child_instance_with_options_async(request, runtime)

    def check_add_region_to_express_connect_router_with_options(
        self,
        request: main_models.CheckAddRegionToExpressConnectRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckAddRegionToExpressConnectRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.fresh_region_id):
            body['FreshRegionId'] = request.fresh_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckAddRegionToExpressConnectRouter',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckAddRegionToExpressConnectRouterResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_add_region_to_express_connect_router_with_options_async(
        self,
        request: main_models.CheckAddRegionToExpressConnectRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckAddRegionToExpressConnectRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.fresh_region_id):
            body['FreshRegionId'] = request.fresh_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckAddRegionToExpressConnectRouter',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckAddRegionToExpressConnectRouterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_add_region_to_express_connect_router(
        self,
        request: main_models.CheckAddRegionToExpressConnectRouterRequest,
    ) -> main_models.CheckAddRegionToExpressConnectRouterResponse:
        runtime = RuntimeOptions()
        return self.check_add_region_to_express_connect_router_with_options(request, runtime)

    async def check_add_region_to_express_connect_router_async(
        self,
        request: main_models.CheckAddRegionToExpressConnectRouterRequest,
    ) -> main_models.CheckAddRegionToExpressConnectRouterResponse:
        runtime = RuntimeOptions()
        return await self.check_add_region_to_express_connect_router_with_options_async(request, runtime)

    def create_express_connect_router_with_options(
        self,
        request: main_models.CreateExpressConnectRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateExpressConnectRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.alibaba_side_asn):
            body['AlibabaSideAsn'] = request.alibaba_side_asn
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExpressConnectRouter',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExpressConnectRouterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_express_connect_router_with_options_async(
        self,
        request: main_models.CreateExpressConnectRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateExpressConnectRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.alibaba_side_asn):
            body['AlibabaSideAsn'] = request.alibaba_side_asn
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExpressConnectRouter',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExpressConnectRouterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_express_connect_router(
        self,
        request: main_models.CreateExpressConnectRouterRequest,
    ) -> main_models.CreateExpressConnectRouterResponse:
        runtime = RuntimeOptions()
        return self.create_express_connect_router_with_options(request, runtime)

    async def create_express_connect_router_async(
        self,
        request: main_models.CreateExpressConnectRouterRequest,
    ) -> main_models.CreateExpressConnectRouterResponse:
        runtime = RuntimeOptions()
        return await self.create_express_connect_router_with_options_async(request, runtime)

    def create_express_connect_router_association_with_options(
        self,
        request: main_models.CreateExpressConnectRouterAssociationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateExpressConnectRouterAssociationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.allowed_prefixes):
            body['AllowedPrefixes'] = request.allowed_prefixes
        if not DaraCore.is_null(request.allowed_prefixes_mode):
            body['AllowedPrefixesMode'] = request.allowed_prefixes_mode
        if not DaraCore.is_null(request.association_region_id):
            body['AssociationRegionId'] = request.association_region_id
        if not DaraCore.is_null(request.cen_id):
            body['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.create_attachment):
            body['CreateAttachment'] = request.create_attachment
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.transit_router_id):
            body['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.transit_router_owner_id):
            body['TransitRouterOwnerId'] = request.transit_router_owner_id
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpc_owner_id):
            body['VpcOwnerId'] = request.vpc_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExpressConnectRouterAssociation',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExpressConnectRouterAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_express_connect_router_association_with_options_async(
        self,
        request: main_models.CreateExpressConnectRouterAssociationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateExpressConnectRouterAssociationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.allowed_prefixes):
            body['AllowedPrefixes'] = request.allowed_prefixes
        if not DaraCore.is_null(request.allowed_prefixes_mode):
            body['AllowedPrefixesMode'] = request.allowed_prefixes_mode
        if not DaraCore.is_null(request.association_region_id):
            body['AssociationRegionId'] = request.association_region_id
        if not DaraCore.is_null(request.cen_id):
            body['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.create_attachment):
            body['CreateAttachment'] = request.create_attachment
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.transit_router_id):
            body['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.transit_router_owner_id):
            body['TransitRouterOwnerId'] = request.transit_router_owner_id
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpc_owner_id):
            body['VpcOwnerId'] = request.vpc_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExpressConnectRouterAssociation',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExpressConnectRouterAssociationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_express_connect_router_association(
        self,
        request: main_models.CreateExpressConnectRouterAssociationRequest,
    ) -> main_models.CreateExpressConnectRouterAssociationResponse:
        runtime = RuntimeOptions()
        return self.create_express_connect_router_association_with_options(request, runtime)

    async def create_express_connect_router_association_async(
        self,
        request: main_models.CreateExpressConnectRouterAssociationRequest,
    ) -> main_models.CreateExpressConnectRouterAssociationResponse:
        runtime = RuntimeOptions()
        return await self.create_express_connect_router_association_with_options_async(request, runtime)

    def create_flow_log_with_options(
        self,
        request: main_models.CreateFlowLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFlowLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.sampling_rate):
            query['SamplingRate'] = request.sampling_rate
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.target_sls_region_id):
            query['TargetSlsRegionId'] = request.target_sls_region_id
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.flow_log_name):
            body['FlowLogName'] = request.flow_log_name
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFlowLog',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFlowLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_log_with_options_async(
        self,
        request: main_models.CreateFlowLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFlowLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.sampling_rate):
            query['SamplingRate'] = request.sampling_rate
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.target_sls_region_id):
            query['TargetSlsRegionId'] = request.target_sls_region_id
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.flow_log_name):
            body['FlowLogName'] = request.flow_log_name
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFlowLog',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFlowLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_flow_log(
        self,
        request: main_models.CreateFlowLogRequest,
    ) -> main_models.CreateFlowLogResponse:
        runtime = RuntimeOptions()
        return self.create_flow_log_with_options(request, runtime)

    async def create_flow_log_async(
        self,
        request: main_models.CreateFlowLogRequest,
    ) -> main_models.CreateFlowLogResponse:
        runtime = RuntimeOptions()
        return await self.create_flow_log_with_options_async(request, runtime)

    def deactivate_flow_log_with_options(
        self,
        request: main_models.DeactivateFlowLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeactivateFlowLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.flow_log_id):
            body['FlowLogId'] = request.flow_log_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeactivateFlowLog',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeactivateFlowLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def deactivate_flow_log_with_options_async(
        self,
        request: main_models.DeactivateFlowLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeactivateFlowLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.flow_log_id):
            body['FlowLogId'] = request.flow_log_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeactivateFlowLog',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeactivateFlowLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deactivate_flow_log(
        self,
        request: main_models.DeactivateFlowLogRequest,
    ) -> main_models.DeactivateFlowLogResponse:
        runtime = RuntimeOptions()
        return self.deactivate_flow_log_with_options(request, runtime)

    async def deactivate_flow_log_async(
        self,
        request: main_models.DeactivateFlowLogRequest,
    ) -> main_models.DeactivateFlowLogResponse:
        runtime = RuntimeOptions()
        return await self.deactivate_flow_log_with_options_async(request, runtime)

    def delete_express_connect_router_with_options(
        self,
        request: main_models.DeleteExpressConnectRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExpressConnectRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExpressConnectRouter',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExpressConnectRouterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_express_connect_router_with_options_async(
        self,
        request: main_models.DeleteExpressConnectRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExpressConnectRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExpressConnectRouter',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExpressConnectRouterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_express_connect_router(
        self,
        request: main_models.DeleteExpressConnectRouterRequest,
    ) -> main_models.DeleteExpressConnectRouterResponse:
        runtime = RuntimeOptions()
        return self.delete_express_connect_router_with_options(request, runtime)

    async def delete_express_connect_router_async(
        self,
        request: main_models.DeleteExpressConnectRouterRequest,
    ) -> main_models.DeleteExpressConnectRouterResponse:
        runtime = RuntimeOptions()
        return await self.delete_express_connect_router_with_options_async(request, runtime)

    def delete_express_connect_router_association_with_options(
        self,
        request: main_models.DeleteExpressConnectRouterAssociationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExpressConnectRouterAssociationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.association_id):
            body['AssociationId'] = request.association_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.delete_attachment):
            body['DeleteAttachment'] = request.delete_attachment
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExpressConnectRouterAssociation',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExpressConnectRouterAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_express_connect_router_association_with_options_async(
        self,
        request: main_models.DeleteExpressConnectRouterAssociationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExpressConnectRouterAssociationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.association_id):
            body['AssociationId'] = request.association_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.delete_attachment):
            body['DeleteAttachment'] = request.delete_attachment
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExpressConnectRouterAssociation',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExpressConnectRouterAssociationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_express_connect_router_association(
        self,
        request: main_models.DeleteExpressConnectRouterAssociationRequest,
    ) -> main_models.DeleteExpressConnectRouterAssociationResponse:
        runtime = RuntimeOptions()
        return self.delete_express_connect_router_association_with_options(request, runtime)

    async def delete_express_connect_router_association_async(
        self,
        request: main_models.DeleteExpressConnectRouterAssociationRequest,
    ) -> main_models.DeleteExpressConnectRouterAssociationResponse:
        runtime = RuntimeOptions()
        return await self.delete_express_connect_router_association_with_options_async(request, runtime)

    def delete_flowlog_with_options(
        self,
        request: main_models.DeleteFlowlogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFlowlogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFlowlog',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFlowlogResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flowlog_with_options_async(
        self,
        request: main_models.DeleteFlowlogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFlowlogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFlowlog',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFlowlogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flowlog(
        self,
        request: main_models.DeleteFlowlogRequest,
    ) -> main_models.DeleteFlowlogResponse:
        runtime = RuntimeOptions()
        return self.delete_flowlog_with_options(request, runtime)

    async def delete_flowlog_async(
        self,
        request: main_models.DeleteFlowlogRequest,
    ) -> main_models.DeleteFlowlogResponse:
        runtime = RuntimeOptions()
        return await self.delete_flowlog_with_options_async(request, runtime)

    def describe_disabled_express_connect_router_route_entries_with_options(
        self,
        request: main_models.DescribeDisabledExpressConnectRouterRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDisabledExpressConnectRouterRouteEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDisabledExpressConnectRouterRouteEntries',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDisabledExpressConnectRouterRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_disabled_express_connect_router_route_entries_with_options_async(
        self,
        request: main_models.DescribeDisabledExpressConnectRouterRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDisabledExpressConnectRouterRouteEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDisabledExpressConnectRouterRouteEntries',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDisabledExpressConnectRouterRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_disabled_express_connect_router_route_entries(
        self,
        request: main_models.DescribeDisabledExpressConnectRouterRouteEntriesRequest,
    ) -> main_models.DescribeDisabledExpressConnectRouterRouteEntriesResponse:
        runtime = RuntimeOptions()
        return self.describe_disabled_express_connect_router_route_entries_with_options(request, runtime)

    async def describe_disabled_express_connect_router_route_entries_async(
        self,
        request: main_models.DescribeDisabledExpressConnectRouterRouteEntriesRequest,
    ) -> main_models.DescribeDisabledExpressConnectRouterRouteEntriesResponse:
        runtime = RuntimeOptions()
        return await self.describe_disabled_express_connect_router_route_entries_with_options_async(request, runtime)

    def describe_express_connect_router_with_options(
        self,
        request: main_models.DescribeExpressConnectRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExpressConnectRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExpressConnectRouter',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExpressConnectRouterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_express_connect_router_with_options_async(
        self,
        request: main_models.DescribeExpressConnectRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExpressConnectRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExpressConnectRouter',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExpressConnectRouterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_express_connect_router(
        self,
        request: main_models.DescribeExpressConnectRouterRequest,
    ) -> main_models.DescribeExpressConnectRouterResponse:
        runtime = RuntimeOptions()
        return self.describe_express_connect_router_with_options(request, runtime)

    async def describe_express_connect_router_async(
        self,
        request: main_models.DescribeExpressConnectRouterRequest,
    ) -> main_models.DescribeExpressConnectRouterResponse:
        runtime = RuntimeOptions()
        return await self.describe_express_connect_router_with_options_async(request, runtime)

    def describe_express_connect_router_allowed_prefix_history_with_options(
        self,
        request: main_models.DescribeExpressConnectRouterAllowedPrefixHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExpressConnectRouterAllowedPrefixHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.association_id):
            body['AssociationId'] = request.association_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExpressConnectRouterAllowedPrefixHistory',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExpressConnectRouterAllowedPrefixHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_express_connect_router_allowed_prefix_history_with_options_async(
        self,
        request: main_models.DescribeExpressConnectRouterAllowedPrefixHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExpressConnectRouterAllowedPrefixHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.association_id):
            body['AssociationId'] = request.association_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExpressConnectRouterAllowedPrefixHistory',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExpressConnectRouterAllowedPrefixHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_express_connect_router_allowed_prefix_history(
        self,
        request: main_models.DescribeExpressConnectRouterAllowedPrefixHistoryRequest,
    ) -> main_models.DescribeExpressConnectRouterAllowedPrefixHistoryResponse:
        runtime = RuntimeOptions()
        return self.describe_express_connect_router_allowed_prefix_history_with_options(request, runtime)

    async def describe_express_connect_router_allowed_prefix_history_async(
        self,
        request: main_models.DescribeExpressConnectRouterAllowedPrefixHistoryRequest,
    ) -> main_models.DescribeExpressConnectRouterAllowedPrefixHistoryResponse:
        runtime = RuntimeOptions()
        return await self.describe_express_connect_router_allowed_prefix_history_with_options_async(request, runtime)

    def describe_express_connect_router_association_with_options(
        self,
        request: main_models.DescribeExpressConnectRouterAssociationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExpressConnectRouterAssociationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.association_id):
            body['AssociationId'] = request.association_id
        if not DaraCore.is_null(request.association_node_type):
            body['AssociationNodeType'] = request.association_node_type
        if not DaraCore.is_null(request.association_region_id):
            body['AssociationRegionId'] = request.association_region_id
        if not DaraCore.is_null(request.cen_id):
            body['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.transit_router_id):
            body['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExpressConnectRouterAssociation',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExpressConnectRouterAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_express_connect_router_association_with_options_async(
        self,
        request: main_models.DescribeExpressConnectRouterAssociationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExpressConnectRouterAssociationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.association_id):
            body['AssociationId'] = request.association_id
        if not DaraCore.is_null(request.association_node_type):
            body['AssociationNodeType'] = request.association_node_type
        if not DaraCore.is_null(request.association_region_id):
            body['AssociationRegionId'] = request.association_region_id
        if not DaraCore.is_null(request.cen_id):
            body['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.transit_router_id):
            body['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExpressConnectRouterAssociation',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExpressConnectRouterAssociationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_express_connect_router_association(
        self,
        request: main_models.DescribeExpressConnectRouterAssociationRequest,
    ) -> main_models.DescribeExpressConnectRouterAssociationResponse:
        runtime = RuntimeOptions()
        return self.describe_express_connect_router_association_with_options(request, runtime)

    async def describe_express_connect_router_association_async(
        self,
        request: main_models.DescribeExpressConnectRouterAssociationRequest,
    ) -> main_models.DescribeExpressConnectRouterAssociationResponse:
        runtime = RuntimeOptions()
        return await self.describe_express_connect_router_association_with_options_async(request, runtime)

    def describe_express_connect_router_child_instance_with_options(
        self,
        request: main_models.DescribeExpressConnectRouterChildInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExpressConnectRouterChildInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.association_id):
            body['AssociationId'] = request.association_id
        if not DaraCore.is_null(request.child_instance_id):
            body['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_region_id):
            body['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_type):
            body['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExpressConnectRouterChildInstance',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExpressConnectRouterChildInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_express_connect_router_child_instance_with_options_async(
        self,
        request: main_models.DescribeExpressConnectRouterChildInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExpressConnectRouterChildInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.association_id):
            body['AssociationId'] = request.association_id
        if not DaraCore.is_null(request.child_instance_id):
            body['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_region_id):
            body['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_type):
            body['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExpressConnectRouterChildInstance',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExpressConnectRouterChildInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_express_connect_router_child_instance(
        self,
        request: main_models.DescribeExpressConnectRouterChildInstanceRequest,
    ) -> main_models.DescribeExpressConnectRouterChildInstanceResponse:
        runtime = RuntimeOptions()
        return self.describe_express_connect_router_child_instance_with_options(request, runtime)

    async def describe_express_connect_router_child_instance_async(
        self,
        request: main_models.DescribeExpressConnectRouterChildInstanceRequest,
    ) -> main_models.DescribeExpressConnectRouterChildInstanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_express_connect_router_child_instance_with_options_async(request, runtime)

    def describe_express_connect_router_inter_region_transit_mode_with_options(
        self,
        request: main_models.DescribeExpressConnectRouterInterRegionTransitModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExpressConnectRouterInterRegionTransitModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExpressConnectRouterInterRegionTransitMode',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExpressConnectRouterInterRegionTransitModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_express_connect_router_inter_region_transit_mode_with_options_async(
        self,
        request: main_models.DescribeExpressConnectRouterInterRegionTransitModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExpressConnectRouterInterRegionTransitModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExpressConnectRouterInterRegionTransitMode',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExpressConnectRouterInterRegionTransitModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_express_connect_router_inter_region_transit_mode(
        self,
        request: main_models.DescribeExpressConnectRouterInterRegionTransitModeRequest,
    ) -> main_models.DescribeExpressConnectRouterInterRegionTransitModeResponse:
        runtime = RuntimeOptions()
        return self.describe_express_connect_router_inter_region_transit_mode_with_options(request, runtime)

    async def describe_express_connect_router_inter_region_transit_mode_async(
        self,
        request: main_models.DescribeExpressConnectRouterInterRegionTransitModeRequest,
    ) -> main_models.DescribeExpressConnectRouterInterRegionTransitModeResponse:
        runtime = RuntimeOptions()
        return await self.describe_express_connect_router_inter_region_transit_mode_with_options_async(request, runtime)

    def describe_express_connect_router_region_with_options(
        self,
        request: main_models.DescribeExpressConnectRouterRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExpressConnectRouterRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExpressConnectRouterRegion',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExpressConnectRouterRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_express_connect_router_region_with_options_async(
        self,
        request: main_models.DescribeExpressConnectRouterRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExpressConnectRouterRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExpressConnectRouterRegion',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExpressConnectRouterRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_express_connect_router_region(
        self,
        request: main_models.DescribeExpressConnectRouterRegionRequest,
    ) -> main_models.DescribeExpressConnectRouterRegionResponse:
        runtime = RuntimeOptions()
        return self.describe_express_connect_router_region_with_options(request, runtime)

    async def describe_express_connect_router_region_async(
        self,
        request: main_models.DescribeExpressConnectRouterRegionRequest,
    ) -> main_models.DescribeExpressConnectRouterRegionResponse:
        runtime = RuntimeOptions()
        return await self.describe_express_connect_router_region_with_options_async(request, runtime)

    def describe_express_connect_router_route_entries_with_options(
        self,
        request: main_models.DescribeExpressConnectRouterRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExpressConnectRouterRouteEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.as_path):
            body['AsPath'] = request.as_path
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.community):
            body['Community'] = request.community
        if not DaraCore.is_null(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.nexthop_instance_id):
            body['NexthopInstanceId'] = request.nexthop_instance_id
        if not DaraCore.is_null(request.query_region_id):
            body['QueryRegionId'] = request.query_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExpressConnectRouterRouteEntries',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExpressConnectRouterRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_express_connect_router_route_entries_with_options_async(
        self,
        request: main_models.DescribeExpressConnectRouterRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExpressConnectRouterRouteEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.as_path):
            body['AsPath'] = request.as_path
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.community):
            body['Community'] = request.community
        if not DaraCore.is_null(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.nexthop_instance_id):
            body['NexthopInstanceId'] = request.nexthop_instance_id
        if not DaraCore.is_null(request.query_region_id):
            body['QueryRegionId'] = request.query_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExpressConnectRouterRouteEntries',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExpressConnectRouterRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_express_connect_router_route_entries(
        self,
        request: main_models.DescribeExpressConnectRouterRouteEntriesRequest,
    ) -> main_models.DescribeExpressConnectRouterRouteEntriesResponse:
        runtime = RuntimeOptions()
        return self.describe_express_connect_router_route_entries_with_options(request, runtime)

    async def describe_express_connect_router_route_entries_async(
        self,
        request: main_models.DescribeExpressConnectRouterRouteEntriesRequest,
    ) -> main_models.DescribeExpressConnectRouterRouteEntriesResponse:
        runtime = RuntimeOptions()
        return await self.describe_express_connect_router_route_entries_with_options_async(request, runtime)

    def describe_flow_logs_with_options(
        self,
        request: main_models.DescribeFlowLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFlowLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.flow_log_name):
            query['FlowLogName'] = request.flow_log_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFlowLogs',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFlowLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_logs_with_options_async(
        self,
        request: main_models.DescribeFlowLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFlowLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.flow_log_name):
            query['FlowLogName'] = request.flow_log_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFlowLogs',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFlowLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_flow_logs(
        self,
        request: main_models.DescribeFlowLogsRequest,
    ) -> main_models.DescribeFlowLogsResponse:
        runtime = RuntimeOptions()
        return self.describe_flow_logs_with_options(request, runtime)

    async def describe_flow_logs_async(
        self,
        request: main_models.DescribeFlowLogsRequest,
    ) -> main_models.DescribeFlowLogsResponse:
        runtime = RuntimeOptions()
        return await self.describe_flow_logs_with_options_async(request, runtime)

    def describe_instance_granted_to_express_connect_router_with_options(
        self,
        request: main_models.DescribeInstanceGrantedToExpressConnectRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceGrantedToExpressConnectRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.caller_type):
            body['CallerType'] = request.caller_type
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_owner_id):
            body['InstanceOwnerId'] = request.instance_owner_id
        if not DaraCore.is_null(request.instance_region_id):
            body['InstanceRegionId'] = request.instance_region_id
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag_models):
            body['TagModels'] = request.tag_models
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceGrantedToExpressConnectRouter',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceGrantedToExpressConnectRouterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_granted_to_express_connect_router_with_options_async(
        self,
        request: main_models.DescribeInstanceGrantedToExpressConnectRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceGrantedToExpressConnectRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.caller_type):
            body['CallerType'] = request.caller_type
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_owner_id):
            body['InstanceOwnerId'] = request.instance_owner_id
        if not DaraCore.is_null(request.instance_region_id):
            body['InstanceRegionId'] = request.instance_region_id
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag_models):
            body['TagModels'] = request.tag_models
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceGrantedToExpressConnectRouter',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceGrantedToExpressConnectRouterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_granted_to_express_connect_router(
        self,
        request: main_models.DescribeInstanceGrantedToExpressConnectRouterRequest,
    ) -> main_models.DescribeInstanceGrantedToExpressConnectRouterResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_granted_to_express_connect_router_with_options(request, runtime)

    async def describe_instance_granted_to_express_connect_router_async(
        self,
        request: main_models.DescribeInstanceGrantedToExpressConnectRouterRequest,
    ) -> main_models.DescribeInstanceGrantedToExpressConnectRouterResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_granted_to_express_connect_router_with_options_async(request, runtime)

    def detach_express_connect_router_child_instance_with_options(
        self,
        request: main_models.DetachExpressConnectRouterChildInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachExpressConnectRouterChildInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.child_instance_id):
            body['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_type):
            body['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DetachExpressConnectRouterChildInstance',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachExpressConnectRouterChildInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_express_connect_router_child_instance_with_options_async(
        self,
        request: main_models.DetachExpressConnectRouterChildInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachExpressConnectRouterChildInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.child_instance_id):
            body['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_type):
            body['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DetachExpressConnectRouterChildInstance',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachExpressConnectRouterChildInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_express_connect_router_child_instance(
        self,
        request: main_models.DetachExpressConnectRouterChildInstanceRequest,
    ) -> main_models.DetachExpressConnectRouterChildInstanceResponse:
        runtime = RuntimeOptions()
        return self.detach_express_connect_router_child_instance_with_options(request, runtime)

    async def detach_express_connect_router_child_instance_async(
        self,
        request: main_models.DetachExpressConnectRouterChildInstanceRequest,
    ) -> main_models.DetachExpressConnectRouterChildInstanceResponse:
        runtime = RuntimeOptions()
        return await self.detach_express_connect_router_child_instance_with_options_async(request, runtime)

    def disable_express_connect_router_route_entries_with_options(
        self,
        request: main_models.DisableExpressConnectRouterRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableExpressConnectRouterRouteEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.nexthop_instance_id):
            body['NexthopInstanceId'] = request.nexthop_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisableExpressConnectRouterRouteEntries',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableExpressConnectRouterRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_express_connect_router_route_entries_with_options_async(
        self,
        request: main_models.DisableExpressConnectRouterRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableExpressConnectRouterRouteEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.nexthop_instance_id):
            body['NexthopInstanceId'] = request.nexthop_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisableExpressConnectRouterRouteEntries',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableExpressConnectRouterRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_express_connect_router_route_entries(
        self,
        request: main_models.DisableExpressConnectRouterRouteEntriesRequest,
    ) -> main_models.DisableExpressConnectRouterRouteEntriesResponse:
        runtime = RuntimeOptions()
        return self.disable_express_connect_router_route_entries_with_options(request, runtime)

    async def disable_express_connect_router_route_entries_async(
        self,
        request: main_models.DisableExpressConnectRouterRouteEntriesRequest,
    ) -> main_models.DisableExpressConnectRouterRouteEntriesResponse:
        runtime = RuntimeOptions()
        return await self.disable_express_connect_router_route_entries_with_options_async(request, runtime)

    def enable_express_connect_router_route_entries_with_options(
        self,
        request: main_models.EnableExpressConnectRouterRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableExpressConnectRouterRouteEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.nexthop_instance_id):
            body['NexthopInstanceId'] = request.nexthop_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableExpressConnectRouterRouteEntries',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableExpressConnectRouterRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_express_connect_router_route_entries_with_options_async(
        self,
        request: main_models.EnableExpressConnectRouterRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableExpressConnectRouterRouteEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.nexthop_instance_id):
            body['NexthopInstanceId'] = request.nexthop_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableExpressConnectRouterRouteEntries',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableExpressConnectRouterRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_express_connect_router_route_entries(
        self,
        request: main_models.EnableExpressConnectRouterRouteEntriesRequest,
    ) -> main_models.EnableExpressConnectRouterRouteEntriesResponse:
        runtime = RuntimeOptions()
        return self.enable_express_connect_router_route_entries_with_options(request, runtime)

    async def enable_express_connect_router_route_entries_async(
        self,
        request: main_models.EnableExpressConnectRouterRouteEntriesRequest,
    ) -> main_models.EnableExpressConnectRouterRouteEntriesResponse:
        runtime = RuntimeOptions()
        return await self.enable_express_connect_router_route_entries_with_options_async(request, runtime)

    def force_delete_express_connect_router_with_options(
        self,
        request: main_models.ForceDeleteExpressConnectRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ForceDeleteExpressConnectRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ForceDeleteExpressConnectRouter',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ForceDeleteExpressConnectRouterResponse(),
            self.call_api(params, req, runtime)
        )

    async def force_delete_express_connect_router_with_options_async(
        self,
        request: main_models.ForceDeleteExpressConnectRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ForceDeleteExpressConnectRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ForceDeleteExpressConnectRouter',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ForceDeleteExpressConnectRouterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def force_delete_express_connect_router(
        self,
        request: main_models.ForceDeleteExpressConnectRouterRequest,
    ) -> main_models.ForceDeleteExpressConnectRouterResponse:
        runtime = RuntimeOptions()
        return self.force_delete_express_connect_router_with_options(request, runtime)

    async def force_delete_express_connect_router_async(
        self,
        request: main_models.ForceDeleteExpressConnectRouterRequest,
    ) -> main_models.ForceDeleteExpressConnectRouterResponse:
        runtime = RuntimeOptions()
        return await self.force_delete_express_connect_router_with_options_async(request, runtime)

    def grant_instance_to_express_connect_router_with_options(
        self,
        request: main_models.GrantInstanceToExpressConnectRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantInstanceToExpressConnectRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.ecr_owner_ali_uid):
            body['EcrOwnerAliUid'] = request.ecr_owner_ali_uid
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_region_id):
            body['InstanceRegionId'] = request.instance_region_id
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GrantInstanceToExpressConnectRouter',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantInstanceToExpressConnectRouterResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_instance_to_express_connect_router_with_options_async(
        self,
        request: main_models.GrantInstanceToExpressConnectRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantInstanceToExpressConnectRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.ecr_owner_ali_uid):
            body['EcrOwnerAliUid'] = request.ecr_owner_ali_uid
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_region_id):
            body['InstanceRegionId'] = request.instance_region_id
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GrantInstanceToExpressConnectRouter',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantInstanceToExpressConnectRouterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_instance_to_express_connect_router(
        self,
        request: main_models.GrantInstanceToExpressConnectRouterRequest,
    ) -> main_models.GrantInstanceToExpressConnectRouterResponse:
        runtime = RuntimeOptions()
        return self.grant_instance_to_express_connect_router_with_options(request, runtime)

    async def grant_instance_to_express_connect_router_async(
        self,
        request: main_models.GrantInstanceToExpressConnectRouterRequest,
    ) -> main_models.GrantInstanceToExpressConnectRouterResponse:
        runtime = RuntimeOptions()
        return await self.grant_instance_to_express_connect_router_with_options_async(request, runtime)

    def list_express_connect_router_supported_region_with_options(
        self,
        request: main_models.ListExpressConnectRouterSupportedRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExpressConnectRouterSupportedRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.node_type):
            body['NodeType'] = request.node_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListExpressConnectRouterSupportedRegion',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExpressConnectRouterSupportedRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_express_connect_router_supported_region_with_options_async(
        self,
        request: main_models.ListExpressConnectRouterSupportedRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExpressConnectRouterSupportedRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.node_type):
            body['NodeType'] = request.node_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListExpressConnectRouterSupportedRegion',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExpressConnectRouterSupportedRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_express_connect_router_supported_region(
        self,
        request: main_models.ListExpressConnectRouterSupportedRegionRequest,
    ) -> main_models.ListExpressConnectRouterSupportedRegionResponse:
        runtime = RuntimeOptions()
        return self.list_express_connect_router_supported_region_with_options(request, runtime)

    async def list_express_connect_router_supported_region_async(
        self,
        request: main_models.ListExpressConnectRouterSupportedRegionRequest,
    ) -> main_models.ListExpressConnectRouterSupportedRegionResponse:
        runtime = RuntimeOptions()
        return await self.list_express_connect_router_supported_region_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_express_connect_router_with_options(
        self,
        request: main_models.ModifyExpressConnectRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyExpressConnectRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyExpressConnectRouter',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyExpressConnectRouterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_express_connect_router_with_options_async(
        self,
        request: main_models.ModifyExpressConnectRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyExpressConnectRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyExpressConnectRouter',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyExpressConnectRouterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_express_connect_router(
        self,
        request: main_models.ModifyExpressConnectRouterRequest,
    ) -> main_models.ModifyExpressConnectRouterResponse:
        runtime = RuntimeOptions()
        return self.modify_express_connect_router_with_options(request, runtime)

    async def modify_express_connect_router_async(
        self,
        request: main_models.ModifyExpressConnectRouterRequest,
    ) -> main_models.ModifyExpressConnectRouterResponse:
        runtime = RuntimeOptions()
        return await self.modify_express_connect_router_with_options_async(request, runtime)

    def modify_express_connect_router_association_with_options(
        self,
        request: main_models.ModifyExpressConnectRouterAssociationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyExpressConnectRouterAssociationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.association_id):
            body['AssociationId'] = request.association_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyExpressConnectRouterAssociation',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyExpressConnectRouterAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_express_connect_router_association_with_options_async(
        self,
        request: main_models.ModifyExpressConnectRouterAssociationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyExpressConnectRouterAssociationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.association_id):
            body['AssociationId'] = request.association_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyExpressConnectRouterAssociation',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyExpressConnectRouterAssociationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_express_connect_router_association(
        self,
        request: main_models.ModifyExpressConnectRouterAssociationRequest,
    ) -> main_models.ModifyExpressConnectRouterAssociationResponse:
        runtime = RuntimeOptions()
        return self.modify_express_connect_router_association_with_options(request, runtime)

    async def modify_express_connect_router_association_async(
        self,
        request: main_models.ModifyExpressConnectRouterAssociationRequest,
    ) -> main_models.ModifyExpressConnectRouterAssociationResponse:
        runtime = RuntimeOptions()
        return await self.modify_express_connect_router_association_with_options_async(request, runtime)

    def modify_express_connect_router_association_allowed_prefix_with_options(
        self,
        request: main_models.ModifyExpressConnectRouterAssociationAllowedPrefixRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyExpressConnectRouterAssociationAllowedPrefixResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.allowed_prefixes):
            body['AllowedPrefixes'] = request.allowed_prefixes
        if not DaraCore.is_null(request.allowed_prefixes_mode):
            body['AllowedPrefixesMode'] = request.allowed_prefixes_mode
        if not DaraCore.is_null(request.association_id):
            body['AssociationId'] = request.association_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyExpressConnectRouterAssociationAllowedPrefix',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyExpressConnectRouterAssociationAllowedPrefixResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_express_connect_router_association_allowed_prefix_with_options_async(
        self,
        request: main_models.ModifyExpressConnectRouterAssociationAllowedPrefixRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyExpressConnectRouterAssociationAllowedPrefixResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.allowed_prefixes):
            body['AllowedPrefixes'] = request.allowed_prefixes
        if not DaraCore.is_null(request.allowed_prefixes_mode):
            body['AllowedPrefixesMode'] = request.allowed_prefixes_mode
        if not DaraCore.is_null(request.association_id):
            body['AssociationId'] = request.association_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyExpressConnectRouterAssociationAllowedPrefix',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyExpressConnectRouterAssociationAllowedPrefixResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_express_connect_router_association_allowed_prefix(
        self,
        request: main_models.ModifyExpressConnectRouterAssociationAllowedPrefixRequest,
    ) -> main_models.ModifyExpressConnectRouterAssociationAllowedPrefixResponse:
        runtime = RuntimeOptions()
        return self.modify_express_connect_router_association_allowed_prefix_with_options(request, runtime)

    async def modify_express_connect_router_association_allowed_prefix_async(
        self,
        request: main_models.ModifyExpressConnectRouterAssociationAllowedPrefixRequest,
    ) -> main_models.ModifyExpressConnectRouterAssociationAllowedPrefixResponse:
        runtime = RuntimeOptions()
        return await self.modify_express_connect_router_association_allowed_prefix_with_options_async(request, runtime)

    def modify_express_connect_router_child_instance_with_options(
        self,
        request: main_models.ModifyExpressConnectRouterChildInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyExpressConnectRouterChildInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.child_instance_id):
            body['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_type):
            body['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyExpressConnectRouterChildInstance',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyExpressConnectRouterChildInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_express_connect_router_child_instance_with_options_async(
        self,
        request: main_models.ModifyExpressConnectRouterChildInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyExpressConnectRouterChildInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.child_instance_id):
            body['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_type):
            body['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyExpressConnectRouterChildInstance',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyExpressConnectRouterChildInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_express_connect_router_child_instance(
        self,
        request: main_models.ModifyExpressConnectRouterChildInstanceRequest,
    ) -> main_models.ModifyExpressConnectRouterChildInstanceResponse:
        runtime = RuntimeOptions()
        return self.modify_express_connect_router_child_instance_with_options(request, runtime)

    async def modify_express_connect_router_child_instance_async(
        self,
        request: main_models.ModifyExpressConnectRouterChildInstanceRequest,
    ) -> main_models.ModifyExpressConnectRouterChildInstanceResponse:
        runtime = RuntimeOptions()
        return await self.modify_express_connect_router_child_instance_with_options_async(request, runtime)

    def modify_express_connect_router_inter_region_transit_mode_with_options(
        self,
        request: main_models.ModifyExpressConnectRouterInterRegionTransitModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyExpressConnectRouterInterRegionTransitModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.transit_mode_list):
            body['TransitModeList'] = request.transit_mode_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyExpressConnectRouterInterRegionTransitMode',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyExpressConnectRouterInterRegionTransitModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_express_connect_router_inter_region_transit_mode_with_options_async(
        self,
        request: main_models.ModifyExpressConnectRouterInterRegionTransitModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyExpressConnectRouterInterRegionTransitModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.transit_mode_list):
            body['TransitModeList'] = request.transit_mode_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyExpressConnectRouterInterRegionTransitMode',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyExpressConnectRouterInterRegionTransitModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_express_connect_router_inter_region_transit_mode(
        self,
        request: main_models.ModifyExpressConnectRouterInterRegionTransitModeRequest,
    ) -> main_models.ModifyExpressConnectRouterInterRegionTransitModeResponse:
        runtime = RuntimeOptions()
        return self.modify_express_connect_router_inter_region_transit_mode_with_options(request, runtime)

    async def modify_express_connect_router_inter_region_transit_mode_async(
        self,
        request: main_models.ModifyExpressConnectRouterInterRegionTransitModeRequest,
    ) -> main_models.ModifyExpressConnectRouterInterRegionTransitModeResponse:
        runtime = RuntimeOptions()
        return await self.modify_express_connect_router_inter_region_transit_mode_with_options_async(request, runtime)

    def modify_flow_log_attribute_with_options(
        self,
        request: main_models.ModifyFlowLogAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFlowLogAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.sampling_rate):
            query['SamplingRate'] = request.sampling_rate
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.flow_log_name):
            body['FlowLogName'] = request.flow_log_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFlowLogAttribute',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFlowLogAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_flow_log_attribute_with_options_async(
        self,
        request: main_models.ModifyFlowLogAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFlowLogAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.sampling_rate):
            query['SamplingRate'] = request.sampling_rate
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.flow_log_name):
            body['FlowLogName'] = request.flow_log_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFlowLogAttribute',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFlowLogAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_flow_log_attribute(
        self,
        request: main_models.ModifyFlowLogAttributeRequest,
    ) -> main_models.ModifyFlowLogAttributeResponse:
        runtime = RuntimeOptions()
        return self.modify_flow_log_attribute_with_options(request, runtime)

    async def modify_flow_log_attribute_async(
        self,
        request: main_models.ModifyFlowLogAttributeRequest,
    ) -> main_models.ModifyFlowLogAttributeResponse:
        runtime = RuntimeOptions()
        return await self.modify_flow_log_attribute_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: main_models.MoveResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: main_models.MoveResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource_group(
        self,
        request: main_models.MoveResourceGroupRequest,
    ) -> main_models.MoveResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: main_models.MoveResourceGroupRequest,
    ) -> main_models.MoveResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def revoke_instance_from_express_connect_router_with_options(
        self,
        request: main_models.RevokeInstanceFromExpressConnectRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeInstanceFromExpressConnectRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.ecr_owner_ali_uid):
            body['EcrOwnerAliUid'] = request.ecr_owner_ali_uid
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_region_id):
            body['InstanceRegionId'] = request.instance_region_id
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevokeInstanceFromExpressConnectRouter',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeInstanceFromExpressConnectRouterResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_instance_from_express_connect_router_with_options_async(
        self,
        request: main_models.RevokeInstanceFromExpressConnectRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeInstanceFromExpressConnectRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.ecr_owner_ali_uid):
            body['EcrOwnerAliUid'] = request.ecr_owner_ali_uid
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_region_id):
            body['InstanceRegionId'] = request.instance_region_id
        if not DaraCore.is_null(request.instance_type):
            body['InstanceType'] = request.instance_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevokeInstanceFromExpressConnectRouter',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeInstanceFromExpressConnectRouterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_instance_from_express_connect_router(
        self,
        request: main_models.RevokeInstanceFromExpressConnectRouterRequest,
    ) -> main_models.RevokeInstanceFromExpressConnectRouterResponse:
        runtime = RuntimeOptions()
        return self.revoke_instance_from_express_connect_router_with_options(request, runtime)

    async def revoke_instance_from_express_connect_router_async(
        self,
        request: main_models.RevokeInstanceFromExpressConnectRouterRequest,
    ) -> main_models.RevokeInstanceFromExpressConnectRouterResponse:
        runtime = RuntimeOptions()
        return await self.revoke_instance_from_express_connect_router_with_options_async(request, runtime)

    def synchronize_express_connect_router_inter_region_bandwidth_with_options(
        self,
        request: main_models.SynchronizeExpressConnectRouterInterRegionBandwidthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SynchronizeExpressConnectRouterInterRegionBandwidthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SynchronizeExpressConnectRouterInterRegionBandwidth',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SynchronizeExpressConnectRouterInterRegionBandwidthResponse(),
            self.call_api(params, req, runtime)
        )

    async def synchronize_express_connect_router_inter_region_bandwidth_with_options_async(
        self,
        request: main_models.SynchronizeExpressConnectRouterInterRegionBandwidthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SynchronizeExpressConnectRouterInterRegionBandwidthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SynchronizeExpressConnectRouterInterRegionBandwidth',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SynchronizeExpressConnectRouterInterRegionBandwidthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def synchronize_express_connect_router_inter_region_bandwidth(
        self,
        request: main_models.SynchronizeExpressConnectRouterInterRegionBandwidthRequest,
    ) -> main_models.SynchronizeExpressConnectRouterInterRegionBandwidthResponse:
        runtime = RuntimeOptions()
        return self.synchronize_express_connect_router_inter_region_bandwidth_with_options(request, runtime)

    async def synchronize_express_connect_router_inter_region_bandwidth_async(
        self,
        request: main_models.SynchronizeExpressConnectRouterInterRegionBandwidthRequest,
    ) -> main_models.SynchronizeExpressConnectRouterInterRegionBandwidthResponse:
        runtime = RuntimeOptions()
        return await self.synchronize_express_connect_router_inter_region_bandwidth_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
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
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.all):
            body['All'] = request.all
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            body['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.all):
            body['All'] = request.all
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            body['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2023-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
