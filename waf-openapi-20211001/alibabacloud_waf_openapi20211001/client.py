# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_waf_openapi20211001 import models as main_models
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
        self._endpoint_map = {
            'cn-qingdao': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-beijing': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-chengdu': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-zhangjiakou': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-huhehaote': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-hangzhou': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-shenzhen': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-heyuan': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-wulanchabu': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-hongkong': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'us-west-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'eu-central-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'cn-shanghai-finance-1': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-finance-1': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-north-2-gov-1': 'wafopenapi.cn-hangzhou.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('waf-openapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_address_with_options(
        self,
        request: main_models.AddAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_list):
            query['AddressList'] = request.address_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAddress',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_address_with_options_async(
        self,
        request: main_models.AddAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_list):
            query['AddressList'] = request.address_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAddress',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_address(
        self,
        request: main_models.AddAddressRequest,
    ) -> main_models.AddAddressResponse:
        runtime = RuntimeOptions()
        return self.add_address_with_options(request, runtime)

    async def add_address_async(
        self,
        request: main_models.AddAddressRequest,
    ) -> main_models.AddAddressResponse:
        runtime = RuntimeOptions()
        return await self.add_address_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
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
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def clear_address_with_options(
        self,
        request: main_models.ClearAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ClearAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ClearAddress',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClearAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_address_with_options_async(
        self,
        request: main_models.ClearAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ClearAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ClearAddress',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClearAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clear_address(
        self,
        request: main_models.ClearAddressRequest,
    ) -> main_models.ClearAddressResponse:
        runtime = RuntimeOptions()
        return self.clear_address_with_options(request, runtime)

    async def clear_address_async(
        self,
        request: main_models.ClearAddressRequest,
    ) -> main_models.ClearAddressResponse:
        runtime = RuntimeOptions()
        return await self.clear_address_with_options_async(request, runtime)

    def clear_major_protection_black_ip_with_options(
        self,
        request: main_models.ClearMajorProtectionBlackIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ClearMajorProtectionBlackIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ClearMajorProtectionBlackIp',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClearMajorProtectionBlackIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_major_protection_black_ip_with_options_async(
        self,
        request: main_models.ClearMajorProtectionBlackIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ClearMajorProtectionBlackIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ClearMajorProtectionBlackIp',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClearMajorProtectionBlackIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clear_major_protection_black_ip(
        self,
        request: main_models.ClearMajorProtectionBlackIpRequest,
    ) -> main_models.ClearMajorProtectionBlackIpResponse:
        runtime = RuntimeOptions()
        return self.clear_major_protection_black_ip_with_options(request, runtime)

    async def clear_major_protection_black_ip_async(
        self,
        request: main_models.ClearMajorProtectionBlackIpRequest,
    ) -> main_models.ClearMajorProtectionBlackIpResponse:
        runtime = RuntimeOptions()
        return await self.clear_major_protection_black_ip_with_options_async(request, runtime)

    def copy_defense_template_with_options(
        self,
        request: main_models.CopyDefenseTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopyDefenseTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CopyDefenseTemplate',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopyDefenseTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_defense_template_with_options_async(
        self,
        request: main_models.CopyDefenseTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopyDefenseTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CopyDefenseTemplate',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopyDefenseTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_defense_template(
        self,
        request: main_models.CopyDefenseTemplateRequest,
    ) -> main_models.CopyDefenseTemplateResponse:
        runtime = RuntimeOptions()
        return self.copy_defense_template_with_options(request, runtime)

    async def copy_defense_template_async(
        self,
        request: main_models.CopyDefenseTemplateRequest,
    ) -> main_models.CopyDefenseTemplateResponse:
        runtime = RuntimeOptions()
        return await self.copy_defense_template_with_options_async(request, runtime)

    def create_api_export_with_options(
        self,
        request: main_models.CreateApiExportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApiExportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.param):
            query['Param'] = request.param
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApiExport',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApiExportResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_api_export_with_options_async(
        self,
        request: main_models.CreateApiExportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApiExportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.param):
            query['Param'] = request.param
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApiExport',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApiExportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_api_export(
        self,
        request: main_models.CreateApiExportRequest,
    ) -> main_models.CreateApiExportResponse:
        runtime = RuntimeOptions()
        return self.create_api_export_with_options(request, runtime)

    async def create_api_export_async(
        self,
        request: main_models.CreateApiExportRequest,
    ) -> main_models.CreateApiExportResponse:
        runtime = RuntimeOptions()
        return await self.create_api_export_with_options_async(request, runtime)

    def create_certs_with_options(
        self,
        request: main_models.CreateCertsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCertsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_content):
            query['CertContent'] = request.cert_content
        if not DaraCore.is_null(request.cert_key):
            query['CertKey'] = request.cert_key
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCerts',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_certs_with_options_async(
        self,
        request: main_models.CreateCertsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCertsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_content):
            query['CertContent'] = request.cert_content
        if not DaraCore.is_null(request.cert_key):
            query['CertKey'] = request.cert_key
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCerts',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCertsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_certs(
        self,
        request: main_models.CreateCertsRequest,
    ) -> main_models.CreateCertsResponse:
        runtime = RuntimeOptions()
        return self.create_certs_with_options(request, runtime)

    async def create_certs_async(
        self,
        request: main_models.CreateCertsRequest,
    ) -> main_models.CreateCertsResponse:
        runtime = RuntimeOptions()
        return await self.create_certs_with_options_async(request, runtime)

    def create_cloud_resource_with_options(
        self,
        tmp_req: main_models.CreateCloudResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudResourceResponse:
        tmp_req.validate()
        request = main_models.CreateCloudResourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.listen):
            request.listen_shrink = Utils.array_to_string_with_specified_style(tmp_req.listen, 'Listen', 'json')
        if not DaraCore.is_null(tmp_req.redirect):
            request.redirect_shrink = Utils.array_to_string_with_specified_style(tmp_req.redirect, 'Redirect', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.listen_shrink):
            query['Listen'] = request.listen_shrink
        if not DaraCore.is_null(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        if not DaraCore.is_null(request.redirect_shrink):
            query['Redirect'] = request.redirect_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudResource',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_resource_with_options_async(
        self,
        tmp_req: main_models.CreateCloudResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudResourceResponse:
        tmp_req.validate()
        request = main_models.CreateCloudResourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.listen):
            request.listen_shrink = Utils.array_to_string_with_specified_style(tmp_req.listen, 'Listen', 'json')
        if not DaraCore.is_null(tmp_req.redirect):
            request.redirect_shrink = Utils.array_to_string_with_specified_style(tmp_req.redirect, 'Redirect', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.listen_shrink):
            query['Listen'] = request.listen_shrink
        if not DaraCore.is_null(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        if not DaraCore.is_null(request.redirect_shrink):
            query['Redirect'] = request.redirect_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudResource',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_resource(
        self,
        request: main_models.CreateCloudResourceRequest,
    ) -> main_models.CreateCloudResourceResponse:
        runtime = RuntimeOptions()
        return self.create_cloud_resource_with_options(request, runtime)

    async def create_cloud_resource_async(
        self,
        request: main_models.CreateCloudResourceRequest,
    ) -> main_models.CreateCloudResourceResponse:
        runtime = RuntimeOptions()
        return await self.create_cloud_resource_with_options_async(request, runtime)

    def create_defense_resource_with_options(
        self,
        tmp_req: main_models.CreateDefenseResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDefenseResourceResponse:
        tmp_req.validate()
        request = main_models.CreateDefenseResourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.custom_headers):
            request.custom_headers_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_headers, 'CustomHeaders', 'json')
        query = {}
        if not DaraCore.is_null(request.custom_headers_shrink):
            query['CustomHeaders'] = request.custom_headers_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.detail):
            query['Detail'] = request.detail
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        if not DaraCore.is_null(request.pattern):
            query['Pattern'] = request.pattern
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_group):
            query['ResourceGroup'] = request.resource_group
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_origin):
            query['ResourceOrigin'] = request.resource_origin
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.xff_status):
            query['XffStatus'] = request.xff_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDefenseResource',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDefenseResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_defense_resource_with_options_async(
        self,
        tmp_req: main_models.CreateDefenseResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDefenseResourceResponse:
        tmp_req.validate()
        request = main_models.CreateDefenseResourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.custom_headers):
            request.custom_headers_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_headers, 'CustomHeaders', 'json')
        query = {}
        if not DaraCore.is_null(request.custom_headers_shrink):
            query['CustomHeaders'] = request.custom_headers_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.detail):
            query['Detail'] = request.detail
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        if not DaraCore.is_null(request.pattern):
            query['Pattern'] = request.pattern
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_group):
            query['ResourceGroup'] = request.resource_group
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_origin):
            query['ResourceOrigin'] = request.resource_origin
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.xff_status):
            query['XffStatus'] = request.xff_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDefenseResource',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDefenseResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_defense_resource(
        self,
        request: main_models.CreateDefenseResourceRequest,
    ) -> main_models.CreateDefenseResourceResponse:
        runtime = RuntimeOptions()
        return self.create_defense_resource_with_options(request, runtime)

    async def create_defense_resource_async(
        self,
        request: main_models.CreateDefenseResourceRequest,
    ) -> main_models.CreateDefenseResourceResponse:
        runtime = RuntimeOptions()
        return await self.create_defense_resource_with_options_async(request, runtime)

    def create_defense_resource_group_with_options(
        self,
        request: main_models.CreateDefenseResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDefenseResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_list):
            query['AddList'] = request.add_list
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDefenseResourceGroup',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDefenseResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_defense_resource_group_with_options_async(
        self,
        request: main_models.CreateDefenseResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDefenseResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_list):
            query['AddList'] = request.add_list
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDefenseResourceGroup',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDefenseResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_defense_resource_group(
        self,
        request: main_models.CreateDefenseResourceGroupRequest,
    ) -> main_models.CreateDefenseResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.create_defense_resource_group_with_options(request, runtime)

    async def create_defense_resource_group_async(
        self,
        request: main_models.CreateDefenseResourceGroupRequest,
    ) -> main_models.CreateDefenseResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_defense_resource_group_with_options_async(request, runtime)

    def create_defense_rule_with_options(
        self,
        request: main_models.CreateDefenseRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDefenseRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not DaraCore.is_null(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        body = {}
        if not DaraCore.is_null(request.rules):
            body['Rules'] = request.rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDefenseRule',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDefenseRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_defense_rule_with_options_async(
        self,
        request: main_models.CreateDefenseRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDefenseRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not DaraCore.is_null(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        body = {}
        if not DaraCore.is_null(request.rules):
            body['Rules'] = request.rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDefenseRule',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDefenseRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_defense_rule(
        self,
        request: main_models.CreateDefenseRuleRequest,
    ) -> main_models.CreateDefenseRuleResponse:
        runtime = RuntimeOptions()
        return self.create_defense_rule_with_options(request, runtime)

    async def create_defense_rule_async(
        self,
        request: main_models.CreateDefenseRuleRequest,
    ) -> main_models.CreateDefenseRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_defense_rule_with_options_async(request, runtime)

    def create_defense_template_with_options(
        self,
        request: main_models.CreateDefenseTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDefenseTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_origin):
            query['TemplateOrigin'] = request.template_origin
        if not DaraCore.is_null(request.template_status):
            query['TemplateStatus'] = request.template_status
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        if not DaraCore.is_null(request.unbind_resource_groups):
            query['UnbindResourceGroups'] = request.unbind_resource_groups
        if not DaraCore.is_null(request.unbind_resources):
            query['UnbindResources'] = request.unbind_resources
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDefenseTemplate',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDefenseTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_defense_template_with_options_async(
        self,
        request: main_models.CreateDefenseTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDefenseTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_origin):
            query['TemplateOrigin'] = request.template_origin
        if not DaraCore.is_null(request.template_status):
            query['TemplateStatus'] = request.template_status
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        if not DaraCore.is_null(request.unbind_resource_groups):
            query['UnbindResourceGroups'] = request.unbind_resource_groups
        if not DaraCore.is_null(request.unbind_resources):
            query['UnbindResources'] = request.unbind_resources
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDefenseTemplate',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDefenseTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_defense_template(
        self,
        request: main_models.CreateDefenseTemplateRequest,
    ) -> main_models.CreateDefenseTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_defense_template_with_options(request, runtime)

    async def create_defense_template_async(
        self,
        request: main_models.CreateDefenseTemplateRequest,
    ) -> main_models.CreateDefenseTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_defense_template_with_options_async(request, runtime)

    def create_domain_with_options(
        self,
        tmp_req: main_models.CreateDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDomainResponse:
        tmp_req.validate()
        request = main_models.CreateDomainShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.listen):
            request.listen_shrink = Utils.array_to_string_with_specified_style(tmp_req.listen, 'Listen', 'json')
        if not DaraCore.is_null(tmp_req.redirect):
            request.redirect_shrink = Utils.array_to_string_with_specified_style(tmp_req.redirect, 'Redirect', 'json')
        query = {}
        if not DaraCore.is_null(request.access_type):
            query['AccessType'] = request.access_type
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.listen_shrink):
            query['Listen'] = request.listen_shrink
        if not DaraCore.is_null(request.redirect_shrink):
            query['Redirect'] = request.redirect_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDomain',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_domain_with_options_async(
        self,
        tmp_req: main_models.CreateDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDomainResponse:
        tmp_req.validate()
        request = main_models.CreateDomainShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.listen):
            request.listen_shrink = Utils.array_to_string_with_specified_style(tmp_req.listen, 'Listen', 'json')
        if not DaraCore.is_null(tmp_req.redirect):
            request.redirect_shrink = Utils.array_to_string_with_specified_style(tmp_req.redirect, 'Redirect', 'json')
        query = {}
        if not DaraCore.is_null(request.access_type):
            query['AccessType'] = request.access_type
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.listen_shrink):
            query['Listen'] = request.listen_shrink
        if not DaraCore.is_null(request.redirect_shrink):
            query['Redirect'] = request.redirect_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDomain',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_domain(
        self,
        request: main_models.CreateDomainRequest,
    ) -> main_models.CreateDomainResponse:
        runtime = RuntimeOptions()
        return self.create_domain_with_options(request, runtime)

    async def create_domain_async(
        self,
        request: main_models.CreateDomainRequest,
    ) -> main_models.CreateDomainResponse:
        runtime = RuntimeOptions()
        return await self.create_domain_with_options_async(request, runtime)

    def create_hybrid_cloud_cluster_with_options(
        self,
        request: main_models.CreateHybridCloudClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHybridCloudClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not DaraCore.is_null(request.access_region):
            query['AccessRegion'] = request.access_region
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.http_ports):
            query['HttpPorts'] = request.http_ports
        if not DaraCore.is_null(request.https_ports):
            query['HttpsPorts'] = request.https_ports
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.log_fields_not_returned):
            query['LogFieldsNotReturned'] = request.log_fields_not_returned
        if not DaraCore.is_null(request.protection_server_count):
            query['ProtectionServerCount'] = request.protection_server_count
        if not DaraCore.is_null(request.proxy_status):
            query['ProxyStatus'] = request.proxy_status
        if not DaraCore.is_null(request.proxy_type):
            query['ProxyType'] = request.proxy_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_config):
            query['RuleConfig'] = request.rule_config
        if not DaraCore.is_null(request.rule_status):
            query['RuleStatus'] = request.rule_status
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHybridCloudCluster',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHybridCloudClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hybrid_cloud_cluster_with_options_async(
        self,
        request: main_models.CreateHybridCloudClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHybridCloudClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not DaraCore.is_null(request.access_region):
            query['AccessRegion'] = request.access_region
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.http_ports):
            query['HttpPorts'] = request.http_ports
        if not DaraCore.is_null(request.https_ports):
            query['HttpsPorts'] = request.https_ports
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.log_fields_not_returned):
            query['LogFieldsNotReturned'] = request.log_fields_not_returned
        if not DaraCore.is_null(request.protection_server_count):
            query['ProtectionServerCount'] = request.protection_server_count
        if not DaraCore.is_null(request.proxy_status):
            query['ProxyStatus'] = request.proxy_status
        if not DaraCore.is_null(request.proxy_type):
            query['ProxyType'] = request.proxy_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_config):
            query['RuleConfig'] = request.rule_config
        if not DaraCore.is_null(request.rule_status):
            query['RuleStatus'] = request.rule_status
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHybridCloudCluster',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHybridCloudClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hybrid_cloud_cluster(
        self,
        request: main_models.CreateHybridCloudClusterRequest,
    ) -> main_models.CreateHybridCloudClusterResponse:
        runtime = RuntimeOptions()
        return self.create_hybrid_cloud_cluster_with_options(request, runtime)

    async def create_hybrid_cloud_cluster_async(
        self,
        request: main_models.CreateHybridCloudClusterRequest,
    ) -> main_models.CreateHybridCloudClusterResponse:
        runtime = RuntimeOptions()
        return await self.create_hybrid_cloud_cluster_with_options_async(request, runtime)

    def create_hybrid_cloud_cluster_rule_with_options(
        self,
        request: main_models.CreateHybridCloudClusterRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHybridCloudClusterRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_config):
            query['RuleConfig'] = request.rule_config
        if not DaraCore.is_null(request.rule_status):
            query['RuleStatus'] = request.rule_status
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHybridCloudClusterRule',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHybridCloudClusterRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hybrid_cloud_cluster_rule_with_options_async(
        self,
        request: main_models.CreateHybridCloudClusterRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHybridCloudClusterRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_config):
            query['RuleConfig'] = request.rule_config
        if not DaraCore.is_null(request.rule_status):
            query['RuleStatus'] = request.rule_status
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHybridCloudClusterRule',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHybridCloudClusterRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hybrid_cloud_cluster_rule(
        self,
        request: main_models.CreateHybridCloudClusterRuleRequest,
    ) -> main_models.CreateHybridCloudClusterRuleResponse:
        runtime = RuntimeOptions()
        return self.create_hybrid_cloud_cluster_rule_with_options(request, runtime)

    async def create_hybrid_cloud_cluster_rule_async(
        self,
        request: main_models.CreateHybridCloudClusterRuleRequest,
    ) -> main_models.CreateHybridCloudClusterRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_hybrid_cloud_cluster_rule_with_options_async(request, runtime)

    def create_hybrid_cloud_group_with_options(
        self,
        request: main_models.CreateHybridCloudGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHybridCloudGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.back_source_mark):
            query['BackSourceMark'] = request.back_source_mark
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.load_balance_ip):
            query['LoadBalanceIp'] = request.load_balance_ip
        if not DaraCore.is_null(request.location_code):
            query['LocationCode'] = request.location_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHybridCloudGroup',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHybridCloudGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hybrid_cloud_group_with_options_async(
        self,
        request: main_models.CreateHybridCloudGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHybridCloudGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.back_source_mark):
            query['BackSourceMark'] = request.back_source_mark
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.load_balance_ip):
            query['LoadBalanceIp'] = request.load_balance_ip
        if not DaraCore.is_null(request.location_code):
            query['LocationCode'] = request.location_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHybridCloudGroup',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHybridCloudGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hybrid_cloud_group(
        self,
        request: main_models.CreateHybridCloudGroupRequest,
    ) -> main_models.CreateHybridCloudGroupResponse:
        runtime = RuntimeOptions()
        return self.create_hybrid_cloud_group_with_options(request, runtime)

    async def create_hybrid_cloud_group_async(
        self,
        request: main_models.CreateHybridCloudGroupRequest,
    ) -> main_models.CreateHybridCloudGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_hybrid_cloud_group_with_options_async(request, runtime)

    def create_log_delivery_config_with_options(
        self,
        request: main_models.CreateLogDeliveryConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLogDeliveryConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_detail):
            query['DeliveryDetail'] = request.delivery_detail
        if not DaraCore.is_null(request.delivery_name):
            query['DeliveryName'] = request.delivery_name
        if not DaraCore.is_null(request.delivery_type):
            query['DeliveryType'] = request.delivery_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLogDeliveryConfig',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLogDeliveryConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_log_delivery_config_with_options_async(
        self,
        request: main_models.CreateLogDeliveryConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLogDeliveryConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_detail):
            query['DeliveryDetail'] = request.delivery_detail
        if not DaraCore.is_null(request.delivery_name):
            query['DeliveryName'] = request.delivery_name
        if not DaraCore.is_null(request.delivery_type):
            query['DeliveryType'] = request.delivery_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLogDeliveryConfig',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLogDeliveryConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_log_delivery_config(
        self,
        request: main_models.CreateLogDeliveryConfigRequest,
    ) -> main_models.CreateLogDeliveryConfigResponse:
        runtime = RuntimeOptions()
        return self.create_log_delivery_config_with_options(request, runtime)

    async def create_log_delivery_config_async(
        self,
        request: main_models.CreateLogDeliveryConfigRequest,
    ) -> main_models.CreateLogDeliveryConfigResponse:
        runtime = RuntimeOptions()
        return await self.create_log_delivery_config_with_options_async(request, runtime)

    def create_major_protection_black_ip_with_options(
        self,
        request: main_models.CreateMajorProtectionBlackIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMajorProtectionBlackIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip_list):
            query['IpList'] = request.ip_list
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMajorProtectionBlackIp',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMajorProtectionBlackIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_major_protection_black_ip_with_options_async(
        self,
        request: main_models.CreateMajorProtectionBlackIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMajorProtectionBlackIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip_list):
            query['IpList'] = request.ip_list
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMajorProtectionBlackIp',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMajorProtectionBlackIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_major_protection_black_ip(
        self,
        request: main_models.CreateMajorProtectionBlackIpRequest,
    ) -> main_models.CreateMajorProtectionBlackIpResponse:
        runtime = RuntimeOptions()
        return self.create_major_protection_black_ip_with_options(request, runtime)

    async def create_major_protection_black_ip_async(
        self,
        request: main_models.CreateMajorProtectionBlackIpRequest,
    ) -> main_models.CreateMajorProtectionBlackIpResponse:
        runtime = RuntimeOptions()
        return await self.create_major_protection_black_ip_with_options_async(request, runtime)

    def create_member_accounts_with_options(
        self,
        request: main_models.CreateMemberAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMemberAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.member_account_ids):
            query['MemberAccountIds'] = request.member_account_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMemberAccounts',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMemberAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_member_accounts_with_options_async(
        self,
        request: main_models.CreateMemberAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMemberAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.member_account_ids):
            query['MemberAccountIds'] = request.member_account_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMemberAccounts',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMemberAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_member_accounts(
        self,
        request: main_models.CreateMemberAccountsRequest,
    ) -> main_models.CreateMemberAccountsResponse:
        runtime = RuntimeOptions()
        return self.create_member_accounts_with_options(request, runtime)

    async def create_member_accounts_async(
        self,
        request: main_models.CreateMemberAccountsRequest,
    ) -> main_models.CreateMemberAccountsResponse:
        runtime = RuntimeOptions()
        return await self.create_member_accounts_with_options_async(request, runtime)

    def create_poc_function_with_options(
        self,
        request: main_models.CreatePocFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePocFunctionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePocFunction',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePocFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_poc_function_with_options_async(
        self,
        request: main_models.CreatePocFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePocFunctionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePocFunction',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePocFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_poc_function(
        self,
        request: main_models.CreatePocFunctionRequest,
    ) -> main_models.CreatePocFunctionResponse:
        runtime = RuntimeOptions()
        return self.create_poc_function_with_options(request, runtime)

    async def create_poc_function_async(
        self,
        request: main_models.CreatePocFunctionRequest,
    ) -> main_models.CreatePocFunctionResponse:
        runtime = RuntimeOptions()
        return await self.create_poc_function_with_options_async(request, runtime)

    def create_postpaid_instance_with_options(
        self,
        request: main_models.CreatePostpaidInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePostpaidInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePostpaidInstance',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePostpaidInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_postpaid_instance_with_options_async(
        self,
        request: main_models.CreatePostpaidInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePostpaidInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePostpaidInstance',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePostpaidInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_postpaid_instance(
        self,
        request: main_models.CreatePostpaidInstanceRequest,
    ) -> main_models.CreatePostpaidInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_postpaid_instance_with_options(request, runtime)

    async def create_postpaid_instance_async(
        self,
        request: main_models.CreatePostpaidInstanceRequest,
    ) -> main_models.CreatePostpaidInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_postpaid_instance_with_options_async(request, runtime)

    def create_sm2cert_with_options(
        self,
        request: main_models.CreateSM2CertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSM2CertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.encrypt_certificate):
            query['EncryptCertificate'] = request.encrypt_certificate
        if not DaraCore.is_null(request.encrypt_private_key):
            query['EncryptPrivateKey'] = request.encrypt_private_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.sign_certificate):
            query['SignCertificate'] = request.sign_certificate
        if not DaraCore.is_null(request.sign_private_key):
            query['SignPrivateKey'] = request.sign_private_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSM2Cert',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSM2CertResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sm2cert_with_options_async(
        self,
        request: main_models.CreateSM2CertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSM2CertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.encrypt_certificate):
            query['EncryptCertificate'] = request.encrypt_certificate
        if not DaraCore.is_null(request.encrypt_private_key):
            query['EncryptPrivateKey'] = request.encrypt_private_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.sign_certificate):
            query['SignCertificate'] = request.sign_certificate
        if not DaraCore.is_null(request.sign_private_key):
            query['SignPrivateKey'] = request.sign_private_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSM2Cert',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSM2CertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sm2cert(
        self,
        request: main_models.CreateSM2CertRequest,
    ) -> main_models.CreateSM2CertResponse:
        runtime = RuntimeOptions()
        return self.create_sm2cert_with_options(request, runtime)

    async def create_sm2cert_async(
        self,
        request: main_models.CreateSM2CertRequest,
    ) -> main_models.CreateSM2CertResponse:
        runtime = RuntimeOptions()
        return await self.create_sm2cert_with_options_async(request, runtime)

    def delete_address_with_options(
        self,
        request: main_models.DeleteAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_list):
            query['AddressList'] = request.address_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAddress',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_address_with_options_async(
        self,
        request: main_models.DeleteAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_list):
            query['AddressList'] = request.address_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAddress',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_address(
        self,
        request: main_models.DeleteAddressRequest,
    ) -> main_models.DeleteAddressResponse:
        runtime = RuntimeOptions()
        return self.delete_address_with_options(request, runtime)

    async def delete_address_async(
        self,
        request: main_models.DeleteAddressRequest,
    ) -> main_models.DeleteAddressResponse:
        runtime = RuntimeOptions()
        return await self.delete_address_with_options_async(request, runtime)

    def delete_apisec_abnormals_with_options(
        self,
        request: main_models.DeleteApisecAbnormalsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApisecAbnormalsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.abnormal_ids):
            query['AbnormalIds'] = request.abnormal_ids
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApisecAbnormals',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApisecAbnormalsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_apisec_abnormals_with_options_async(
        self,
        request: main_models.DeleteApisecAbnormalsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApisecAbnormalsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.abnormal_ids):
            query['AbnormalIds'] = request.abnormal_ids
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApisecAbnormals',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApisecAbnormalsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_apisec_abnormals(
        self,
        request: main_models.DeleteApisecAbnormalsRequest,
    ) -> main_models.DeleteApisecAbnormalsResponse:
        runtime = RuntimeOptions()
        return self.delete_apisec_abnormals_with_options(request, runtime)

    async def delete_apisec_abnormals_async(
        self,
        request: main_models.DeleteApisecAbnormalsRequest,
    ) -> main_models.DeleteApisecAbnormalsResponse:
        runtime = RuntimeOptions()
        return await self.delete_apisec_abnormals_with_options_async(request, runtime)

    def delete_apisec_events_with_options(
        self,
        request: main_models.DeleteApisecEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApisecEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.event_ids):
            query['EventIds'] = request.event_ids
        if not DaraCore.is_null(request.event_scope):
            query['EventScope'] = request.event_scope
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApisecEvents',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApisecEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_apisec_events_with_options_async(
        self,
        request: main_models.DeleteApisecEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApisecEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.event_ids):
            query['EventIds'] = request.event_ids
        if not DaraCore.is_null(request.event_scope):
            query['EventScope'] = request.event_scope
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApisecEvents',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApisecEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_apisec_events(
        self,
        request: main_models.DeleteApisecEventsRequest,
    ) -> main_models.DeleteApisecEventsResponse:
        runtime = RuntimeOptions()
        return self.delete_apisec_events_with_options(request, runtime)

    async def delete_apisec_events_async(
        self,
        request: main_models.DeleteApisecEventsRequest,
    ) -> main_models.DeleteApisecEventsResponse:
        runtime = RuntimeOptions()
        return await self.delete_apisec_events_with_options_async(request, runtime)

    def delete_cloud_resource_with_options(
        self,
        request: main_models.DeleteCloudResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cloud_resource_id):
            query['CloudResourceId'] = request.cloud_resource_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_product):
            query['ResourceProduct'] = request.resource_product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudResource',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloud_resource_with_options_async(
        self,
        request: main_models.DeleteCloudResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cloud_resource_id):
            query['CloudResourceId'] = request.cloud_resource_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_product):
            query['ResourceProduct'] = request.resource_product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudResource',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cloud_resource(
        self,
        request: main_models.DeleteCloudResourceRequest,
    ) -> main_models.DeleteCloudResourceResponse:
        runtime = RuntimeOptions()
        return self.delete_cloud_resource_with_options(request, runtime)

    async def delete_cloud_resource_async(
        self,
        request: main_models.DeleteCloudResourceRequest,
    ) -> main_models.DeleteCloudResourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_cloud_resource_with_options_async(request, runtime)

    def delete_defense_resource_with_options(
        self,
        request: main_models.DeleteDefenseResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDefenseResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDefenseResource',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDefenseResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_defense_resource_with_options_async(
        self,
        request: main_models.DeleteDefenseResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDefenseResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDefenseResource',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDefenseResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_defense_resource(
        self,
        request: main_models.DeleteDefenseResourceRequest,
    ) -> main_models.DeleteDefenseResourceResponse:
        runtime = RuntimeOptions()
        return self.delete_defense_resource_with_options(request, runtime)

    async def delete_defense_resource_async(
        self,
        request: main_models.DeleteDefenseResourceRequest,
    ) -> main_models.DeleteDefenseResourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_defense_resource_with_options_async(request, runtime)

    def delete_defense_resource_group_with_options(
        self,
        request: main_models.DeleteDefenseResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDefenseResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDefenseResourceGroup',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDefenseResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_defense_resource_group_with_options_async(
        self,
        request: main_models.DeleteDefenseResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDefenseResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDefenseResourceGroup',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDefenseResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_defense_resource_group(
        self,
        request: main_models.DeleteDefenseResourceGroupRequest,
    ) -> main_models.DeleteDefenseResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_defense_resource_group_with_options(request, runtime)

    async def delete_defense_resource_group_async(
        self,
        request: main_models.DeleteDefenseResourceGroupRequest,
    ) -> main_models.DeleteDefenseResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_defense_resource_group_with_options_async(request, runtime)

    def delete_defense_rule_with_options(
        self,
        request: main_models.DeleteDefenseRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDefenseRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDefenseRule',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDefenseRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_defense_rule_with_options_async(
        self,
        request: main_models.DeleteDefenseRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDefenseRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDefenseRule',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDefenseRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_defense_rule(
        self,
        request: main_models.DeleteDefenseRuleRequest,
    ) -> main_models.DeleteDefenseRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_defense_rule_with_options(request, runtime)

    async def delete_defense_rule_async(
        self,
        request: main_models.DeleteDefenseRuleRequest,
    ) -> main_models.DeleteDefenseRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_defense_rule_with_options_async(request, runtime)

    def delete_defense_rule_block_ip_with_options(
        self,
        request: main_models.DeleteDefenseRuleBlockIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDefenseRuleBlockIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDefenseRuleBlockIp',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDefenseRuleBlockIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_defense_rule_block_ip_with_options_async(
        self,
        request: main_models.DeleteDefenseRuleBlockIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDefenseRuleBlockIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDefenseRuleBlockIp',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDefenseRuleBlockIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_defense_rule_block_ip(
        self,
        request: main_models.DeleteDefenseRuleBlockIpRequest,
    ) -> main_models.DeleteDefenseRuleBlockIpResponse:
        runtime = RuntimeOptions()
        return self.delete_defense_rule_block_ip_with_options(request, runtime)

    async def delete_defense_rule_block_ip_async(
        self,
        request: main_models.DeleteDefenseRuleBlockIpRequest,
    ) -> main_models.DeleteDefenseRuleBlockIpResponse:
        runtime = RuntimeOptions()
        return await self.delete_defense_rule_block_ip_with_options_async(request, runtime)

    def delete_defense_template_with_options(
        self,
        request: main_models.DeleteDefenseTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDefenseTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDefenseTemplate',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDefenseTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_defense_template_with_options_async(
        self,
        request: main_models.DeleteDefenseTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDefenseTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDefenseTemplate',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDefenseTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_defense_template(
        self,
        request: main_models.DeleteDefenseTemplateRequest,
    ) -> main_models.DeleteDefenseTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_defense_template_with_options(request, runtime)

    async def delete_defense_template_async(
        self,
        request: main_models.DeleteDefenseTemplateRequest,
    ) -> main_models.DeleteDefenseTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_defense_template_with_options_async(request, runtime)

    def delete_domain_with_options(
        self,
        request: main_models.DeleteDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_type):
            query['AccessType'] = request.access_type
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomain',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        request: main_models.DeleteDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_type):
            query['AccessType'] = request.access_type
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomain',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain(
        self,
        request: main_models.DeleteDomainRequest,
    ) -> main_models.DeleteDomainResponse:
        runtime = RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    async def delete_domain_async(
        self,
        request: main_models.DeleteDomainRequest,
    ) -> main_models.DeleteDomainResponse:
        runtime = RuntimeOptions()
        return await self.delete_domain_with_options_async(request, runtime)

    def delete_hybrid_cloud_cluster_rule_with_options(
        self,
        request: main_models.DeleteHybridCloudClusterRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHybridCloudClusterRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_rule_resource_id):
            query['ClusterRuleResourceId'] = request.cluster_rule_resource_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHybridCloudClusterRule',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHybridCloudClusterRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hybrid_cloud_cluster_rule_with_options_async(
        self,
        request: main_models.DeleteHybridCloudClusterRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHybridCloudClusterRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_rule_resource_id):
            query['ClusterRuleResourceId'] = request.cluster_rule_resource_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHybridCloudClusterRule',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHybridCloudClusterRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hybrid_cloud_cluster_rule(
        self,
        request: main_models.DeleteHybridCloudClusterRuleRequest,
    ) -> main_models.DeleteHybridCloudClusterRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_hybrid_cloud_cluster_rule_with_options(request, runtime)

    async def delete_hybrid_cloud_cluster_rule_async(
        self,
        request: main_models.DeleteHybridCloudClusterRuleRequest,
    ) -> main_models.DeleteHybridCloudClusterRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_hybrid_cloud_cluster_rule_with_options_async(request, runtime)

    def delete_hybrid_cloud_group_with_options(
        self,
        request: main_models.DeleteHybridCloudGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHybridCloudGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHybridCloudGroup',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHybridCloudGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hybrid_cloud_group_with_options_async(
        self,
        request: main_models.DeleteHybridCloudGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHybridCloudGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHybridCloudGroup',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHybridCloudGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hybrid_cloud_group(
        self,
        request: main_models.DeleteHybridCloudGroupRequest,
    ) -> main_models.DeleteHybridCloudGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_hybrid_cloud_group_with_options(request, runtime)

    async def delete_hybrid_cloud_group_async(
        self,
        request: main_models.DeleteHybridCloudGroupRequest,
    ) -> main_models.DeleteHybridCloudGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_hybrid_cloud_group_with_options_async(request, runtime)

    def delete_log_delivery_config_with_options(
        self,
        request: main_models.DeleteLogDeliveryConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLogDeliveryConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_name):
            query['DeliveryName'] = request.delivery_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLogDeliveryConfig',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLogDeliveryConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_log_delivery_config_with_options_async(
        self,
        request: main_models.DeleteLogDeliveryConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLogDeliveryConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_name):
            query['DeliveryName'] = request.delivery_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLogDeliveryConfig',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLogDeliveryConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_log_delivery_config(
        self,
        request: main_models.DeleteLogDeliveryConfigRequest,
    ) -> main_models.DeleteLogDeliveryConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_log_delivery_config_with_options(request, runtime)

    async def delete_log_delivery_config_async(
        self,
        request: main_models.DeleteLogDeliveryConfigRequest,
    ) -> main_models.DeleteLogDeliveryConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_log_delivery_config_with_options_async(request, runtime)

    def delete_major_protection_black_ip_with_options(
        self,
        request: main_models.DeleteMajorProtectionBlackIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMajorProtectionBlackIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip_list):
            query['IpList'] = request.ip_list
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMajorProtectionBlackIp',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMajorProtectionBlackIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_major_protection_black_ip_with_options_async(
        self,
        request: main_models.DeleteMajorProtectionBlackIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMajorProtectionBlackIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip_list):
            query['IpList'] = request.ip_list
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMajorProtectionBlackIp',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMajorProtectionBlackIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_major_protection_black_ip(
        self,
        request: main_models.DeleteMajorProtectionBlackIpRequest,
    ) -> main_models.DeleteMajorProtectionBlackIpResponse:
        runtime = RuntimeOptions()
        return self.delete_major_protection_black_ip_with_options(request, runtime)

    async def delete_major_protection_black_ip_async(
        self,
        request: main_models.DeleteMajorProtectionBlackIpRequest,
    ) -> main_models.DeleteMajorProtectionBlackIpResponse:
        runtime = RuntimeOptions()
        return await self.delete_major_protection_black_ip_with_options_async(request, runtime)

    def delete_member_account_with_options(
        self,
        request: main_models.DeleteMemberAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMemberAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.member_account_id):
            query['MemberAccountId'] = request.member_account_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMemberAccount',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMemberAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_member_account_with_options_async(
        self,
        request: main_models.DeleteMemberAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMemberAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.member_account_id):
            query['MemberAccountId'] = request.member_account_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMemberAccount',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMemberAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_member_account(
        self,
        request: main_models.DeleteMemberAccountRequest,
    ) -> main_models.DeleteMemberAccountResponse:
        runtime = RuntimeOptions()
        return self.delete_member_account_with_options(request, runtime)

    async def delete_member_account_async(
        self,
        request: main_models.DeleteMemberAccountRequest,
    ) -> main_models.DeleteMemberAccountResponse:
        runtime = RuntimeOptions()
        return await self.delete_member_account_with_options_async(request, runtime)

    def describe_abnormal_cloud_resources_with_options(
        self,
        request: main_models.DescribeAbnormalCloudResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAbnormalCloudResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAbnormalCloudResources',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAbnormalCloudResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_abnormal_cloud_resources_with_options_async(
        self,
        request: main_models.DescribeAbnormalCloudResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAbnormalCloudResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAbnormalCloudResources',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAbnormalCloudResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_abnormal_cloud_resources(
        self,
        request: main_models.DescribeAbnormalCloudResourcesRequest,
    ) -> main_models.DescribeAbnormalCloudResourcesResponse:
        runtime = RuntimeOptions()
        return self.describe_abnormal_cloud_resources_with_options(request, runtime)

    async def describe_abnormal_cloud_resources_async(
        self,
        request: main_models.DescribeAbnormalCloudResourcesRequest,
    ) -> main_models.DescribeAbnormalCloudResourcesResponse:
        runtime = RuntimeOptions()
        return await self.describe_abnormal_cloud_resources_with_options_async(request, runtime)

    def describe_account_delegated_status_with_options(
        self,
        request: main_models.DescribeAccountDelegatedStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountDelegatedStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccountDelegatedStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccountDelegatedStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_delegated_status_with_options_async(
        self,
        request: main_models.DescribeAccountDelegatedStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountDelegatedStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccountDelegatedStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccountDelegatedStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_delegated_status(
        self,
        request: main_models.DescribeAccountDelegatedStatusRequest,
    ) -> main_models.DescribeAccountDelegatedStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_account_delegated_status_with_options(request, runtime)

    async def describe_account_delegated_status_async(
        self,
        request: main_models.DescribeAccountDelegatedStatusRequest,
    ) -> main_models.DescribeAccountDelegatedStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_account_delegated_status_with_options_async(request, runtime)

    def describe_addresses_with_options(
        self,
        request: main_models.DescribeAddressesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAddressesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_like):
            query['AddressLike'] = request.address_like
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAddresses',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAddressesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_addresses_with_options_async(
        self,
        request: main_models.DescribeAddressesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAddressesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_like):
            query['AddressLike'] = request.address_like
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAddresses',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAddressesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_addresses(
        self,
        request: main_models.DescribeAddressesRequest,
    ) -> main_models.DescribeAddressesResponse:
        runtime = RuntimeOptions()
        return self.describe_addresses_with_options(request, runtime)

    async def describe_addresses_async(
        self,
        request: main_models.DescribeAddressesRequest,
    ) -> main_models.DescribeAddressesResponse:
        runtime = RuntimeOptions()
        return await self.describe_addresses_with_options_async(request, runtime)

    def describe_alarm_banner_with_options(
        self,
        request: main_models.DescribeAlarmBannerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlarmBannerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlarmBanner',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlarmBannerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alarm_banner_with_options_async(
        self,
        request: main_models.DescribeAlarmBannerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlarmBannerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlarmBanner',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlarmBannerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alarm_banner(
        self,
        request: main_models.DescribeAlarmBannerRequest,
    ) -> main_models.DescribeAlarmBannerResponse:
        runtime = RuntimeOptions()
        return self.describe_alarm_banner_with_options(request, runtime)

    async def describe_alarm_banner_async(
        self,
        request: main_models.DescribeAlarmBannerRequest,
    ) -> main_models.DescribeAlarmBannerResponse:
        runtime = RuntimeOptions()
        return await self.describe_alarm_banner_with_options_async(request, runtime)

    def describe_alarm_list_with_options(
        self,
        request: main_models.DescribeAlarmListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlarmListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlarmList',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlarmListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alarm_list_with_options_async(
        self,
        request: main_models.DescribeAlarmListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlarmListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlarmList',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlarmListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alarm_list(
        self,
        request: main_models.DescribeAlarmListRequest,
    ) -> main_models.DescribeAlarmListResponse:
        runtime = RuntimeOptions()
        return self.describe_alarm_list_with_options(request, runtime)

    async def describe_alarm_list_async(
        self,
        request: main_models.DescribeAlarmListRequest,
    ) -> main_models.DescribeAlarmListResponse:
        runtime = RuntimeOptions()
        return await self.describe_alarm_list_with_options_async(request, runtime)

    def describe_api_exports_with_options(
        self,
        request: main_models.DescribeApiExportsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiExportsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiExports',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiExportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_exports_with_options_async(
        self,
        request: main_models.DescribeApiExportsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiExportsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiExports',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiExportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_exports(
        self,
        request: main_models.DescribeApiExportsRequest,
    ) -> main_models.DescribeApiExportsResponse:
        runtime = RuntimeOptions()
        return self.describe_api_exports_with_options(request, runtime)

    async def describe_api_exports_async(
        self,
        request: main_models.DescribeApiExportsRequest,
    ) -> main_models.DescribeApiExportsResponse:
        runtime = RuntimeOptions()
        return await self.describe_api_exports_with_options_async(request, runtime)

    def describe_apisec_abnormal_domain_statistic_with_options(
        self,
        request: main_models.DescribeApisecAbnormalDomainStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecAbnormalDomainStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_way):
            query['OrderWay'] = request.order_way
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecAbnormalDomainStatistic',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecAbnormalDomainStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_abnormal_domain_statistic_with_options_async(
        self,
        request: main_models.DescribeApisecAbnormalDomainStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecAbnormalDomainStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_way):
            query['OrderWay'] = request.order_way
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecAbnormalDomainStatistic',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecAbnormalDomainStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_abnormal_domain_statistic(
        self,
        request: main_models.DescribeApisecAbnormalDomainStatisticRequest,
    ) -> main_models.DescribeApisecAbnormalDomainStatisticResponse:
        runtime = RuntimeOptions()
        return self.describe_apisec_abnormal_domain_statistic_with_options(request, runtime)

    async def describe_apisec_abnormal_domain_statistic_async(
        self,
        request: main_models.DescribeApisecAbnormalDomainStatisticRequest,
    ) -> main_models.DescribeApisecAbnormalDomainStatisticResponse:
        runtime = RuntimeOptions()
        return await self.describe_apisec_abnormal_domain_statistic_with_options_async(request, runtime)

    def describe_apisec_abnormals_with_options(
        self,
        request: main_models.DescribeApisecAbnormalsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecAbnormalsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.abnormal_id):
            query['AbnormalId'] = request.abnormal_id
        if not DaraCore.is_null(request.abnormal_level):
            query['AbnormalLevel'] = request.abnormal_level
        if not DaraCore.is_null(request.abnormal_tag):
            query['AbnormalTag'] = request.abnormal_tag
        if not DaraCore.is_null(request.api_format):
            query['ApiFormat'] = request.api_format
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.api_tag):
            query['ApiTag'] = request.api_tag
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.matched_host):
            query['MatchedHost'] = request.matched_host
        if not DaraCore.is_null(request.order_key):
            query['OrderKey'] = request.order_key
        if not DaraCore.is_null(request.order_way):
            query['OrderWay'] = request.order_way
        if not DaraCore.is_null(request.origin):
            query['Origin'] = request.origin
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user_status):
            query['UserStatus'] = request.user_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecAbnormals',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecAbnormalsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_abnormals_with_options_async(
        self,
        request: main_models.DescribeApisecAbnormalsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecAbnormalsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.abnormal_id):
            query['AbnormalId'] = request.abnormal_id
        if not DaraCore.is_null(request.abnormal_level):
            query['AbnormalLevel'] = request.abnormal_level
        if not DaraCore.is_null(request.abnormal_tag):
            query['AbnormalTag'] = request.abnormal_tag
        if not DaraCore.is_null(request.api_format):
            query['ApiFormat'] = request.api_format
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.api_tag):
            query['ApiTag'] = request.api_tag
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.matched_host):
            query['MatchedHost'] = request.matched_host
        if not DaraCore.is_null(request.order_key):
            query['OrderKey'] = request.order_key
        if not DaraCore.is_null(request.order_way):
            query['OrderWay'] = request.order_way
        if not DaraCore.is_null(request.origin):
            query['Origin'] = request.origin
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user_status):
            query['UserStatus'] = request.user_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecAbnormals',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecAbnormalsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_abnormals(
        self,
        request: main_models.DescribeApisecAbnormalsRequest,
    ) -> main_models.DescribeApisecAbnormalsResponse:
        runtime = RuntimeOptions()
        return self.describe_apisec_abnormals_with_options(request, runtime)

    async def describe_apisec_abnormals_async(
        self,
        request: main_models.DescribeApisecAbnormalsRequest,
    ) -> main_models.DescribeApisecAbnormalsResponse:
        runtime = RuntimeOptions()
        return await self.describe_apisec_abnormals_with_options_async(request, runtime)

    def describe_apisec_api_resources_with_options(
        self,
        request: main_models.DescribeApisecApiResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecApiResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_format):
            query['ApiFormat'] = request.api_format
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.api_method):
            query['ApiMethod'] = request.api_method
        if not DaraCore.is_null(request.api_status):
            query['ApiStatus'] = request.api_status
        if not DaraCore.is_null(request.api_tag):
            query['ApiTag'] = request.api_tag
        if not DaraCore.is_null(request.api_type):
            query['ApiType'] = request.api_type
        if not DaraCore.is_null(request.auth_flag):
            query['AuthFlag'] = request.auth_flag
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.follow):
            query['Follow'] = request.follow
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.matched_host):
            query['MatchedHost'] = request.matched_host
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        if not DaraCore.is_null(request.order_key):
            query['OrderKey'] = request.order_key
        if not DaraCore.is_null(request.order_way):
            query['OrderWay'] = request.order_way
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_sensitive_type):
            query['RequestSensitiveType'] = request.request_sensitive_type
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.sensitive_level):
            query['SensitiveLevel'] = request.sensitive_level
        if not DaraCore.is_null(request.sensitive_type):
            query['SensitiveType'] = request.sensitive_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecApiResources',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecApiResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_api_resources_with_options_async(
        self,
        request: main_models.DescribeApisecApiResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecApiResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_format):
            query['ApiFormat'] = request.api_format
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.api_method):
            query['ApiMethod'] = request.api_method
        if not DaraCore.is_null(request.api_status):
            query['ApiStatus'] = request.api_status
        if not DaraCore.is_null(request.api_tag):
            query['ApiTag'] = request.api_tag
        if not DaraCore.is_null(request.api_type):
            query['ApiType'] = request.api_type
        if not DaraCore.is_null(request.auth_flag):
            query['AuthFlag'] = request.auth_flag
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.follow):
            query['Follow'] = request.follow
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.matched_host):
            query['MatchedHost'] = request.matched_host
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        if not DaraCore.is_null(request.order_key):
            query['OrderKey'] = request.order_key
        if not DaraCore.is_null(request.order_way):
            query['OrderWay'] = request.order_way
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_sensitive_type):
            query['RequestSensitiveType'] = request.request_sensitive_type
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.sensitive_level):
            query['SensitiveLevel'] = request.sensitive_level
        if not DaraCore.is_null(request.sensitive_type):
            query['SensitiveType'] = request.sensitive_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecApiResources',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecApiResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_api_resources(
        self,
        request: main_models.DescribeApisecApiResourcesRequest,
    ) -> main_models.DescribeApisecApiResourcesResponse:
        runtime = RuntimeOptions()
        return self.describe_apisec_api_resources_with_options(request, runtime)

    async def describe_apisec_api_resources_async(
        self,
        request: main_models.DescribeApisecApiResourcesRequest,
    ) -> main_models.DescribeApisecApiResourcesResponse:
        runtime = RuntimeOptions()
        return await self.describe_apisec_api_resources_with_options_async(request, runtime)

    def describe_apisec_asset_trend_with_options(
        self,
        request: main_models.DescribeApisecAssetTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecAssetTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecAssetTrend',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecAssetTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_asset_trend_with_options_async(
        self,
        request: main_models.DescribeApisecAssetTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecAssetTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecAssetTrend',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecAssetTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_asset_trend(
        self,
        request: main_models.DescribeApisecAssetTrendRequest,
    ) -> main_models.DescribeApisecAssetTrendResponse:
        runtime = RuntimeOptions()
        return self.describe_apisec_asset_trend_with_options(request, runtime)

    async def describe_apisec_asset_trend_async(
        self,
        request: main_models.DescribeApisecAssetTrendRequest,
    ) -> main_models.DescribeApisecAssetTrendResponse:
        runtime = RuntimeOptions()
        return await self.describe_apisec_asset_trend_with_options_async(request, runtime)

    def describe_apisec_event_detail_with_options(
        self,
        request: main_models.DescribeApisecEventDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecEventDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.detail_type):
            query['DetailType'] = request.detail_type
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.event_scope):
            query['EventScope'] = request.event_scope
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecEventDetail',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecEventDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_event_detail_with_options_async(
        self,
        request: main_models.DescribeApisecEventDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecEventDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.detail_type):
            query['DetailType'] = request.detail_type
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.event_scope):
            query['EventScope'] = request.event_scope
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecEventDetail',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecEventDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_event_detail(
        self,
        request: main_models.DescribeApisecEventDetailRequest,
    ) -> main_models.DescribeApisecEventDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_apisec_event_detail_with_options(request, runtime)

    async def describe_apisec_event_detail_async(
        self,
        request: main_models.DescribeApisecEventDetailRequest,
    ) -> main_models.DescribeApisecEventDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_apisec_event_detail_with_options_async(request, runtime)

    def describe_apisec_event_domain_statistic_with_options(
        self,
        request: main_models.DescribeApisecEventDomainStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecEventDomainStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_way):
            query['OrderWay'] = request.order_way
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecEventDomainStatistic',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecEventDomainStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_event_domain_statistic_with_options_async(
        self,
        request: main_models.DescribeApisecEventDomainStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecEventDomainStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_way):
            query['OrderWay'] = request.order_way
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecEventDomainStatistic',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecEventDomainStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_event_domain_statistic(
        self,
        request: main_models.DescribeApisecEventDomainStatisticRequest,
    ) -> main_models.DescribeApisecEventDomainStatisticResponse:
        runtime = RuntimeOptions()
        return self.describe_apisec_event_domain_statistic_with_options(request, runtime)

    async def describe_apisec_event_domain_statistic_async(
        self,
        request: main_models.DescribeApisecEventDomainStatisticRequest,
    ) -> main_models.DescribeApisecEventDomainStatisticResponse:
        runtime = RuntimeOptions()
        return await self.describe_apisec_event_domain_statistic_with_options_async(request, runtime)

    def describe_apisec_events_with_options(
        self,
        request: main_models.DescribeApisecEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.api_format):
            query['ApiFormat'] = request.api_format
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.api_tag):
            query['ApiTag'] = request.api_tag
        if not DaraCore.is_null(request.attack_ip):
            query['AttackIp'] = request.attack_ip
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_ts):
            query['EndTs'] = request.end_ts
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.event_level):
            query['EventLevel'] = request.event_level
        if not DaraCore.is_null(request.event_scope):
            query['EventScope'] = request.event_scope
        if not DaraCore.is_null(request.event_tag):
            query['EventTag'] = request.event_tag
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.matched_host):
            query['MatchedHost'] = request.matched_host
        if not DaraCore.is_null(request.order_key):
            query['OrderKey'] = request.order_key
        if not DaraCore.is_null(request.order_way):
            query['OrderWay'] = request.order_way
        if not DaraCore.is_null(request.origin):
            query['Origin'] = request.origin
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_ts):
            query['StartTs'] = request.start_ts
        if not DaraCore.is_null(request.user_status):
            query['UserStatus'] = request.user_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecEvents',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_events_with_options_async(
        self,
        request: main_models.DescribeApisecEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.api_format):
            query['ApiFormat'] = request.api_format
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.api_tag):
            query['ApiTag'] = request.api_tag
        if not DaraCore.is_null(request.attack_ip):
            query['AttackIp'] = request.attack_ip
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_ts):
            query['EndTs'] = request.end_ts
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.event_level):
            query['EventLevel'] = request.event_level
        if not DaraCore.is_null(request.event_scope):
            query['EventScope'] = request.event_scope
        if not DaraCore.is_null(request.event_tag):
            query['EventTag'] = request.event_tag
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.matched_host):
            query['MatchedHost'] = request.matched_host
        if not DaraCore.is_null(request.order_key):
            query['OrderKey'] = request.order_key
        if not DaraCore.is_null(request.order_way):
            query['OrderWay'] = request.order_way
        if not DaraCore.is_null(request.origin):
            query['Origin'] = request.origin
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_ts):
            query['StartTs'] = request.start_ts
        if not DaraCore.is_null(request.user_status):
            query['UserStatus'] = request.user_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecEvents',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_events(
        self,
        request: main_models.DescribeApisecEventsRequest,
    ) -> main_models.DescribeApisecEventsResponse:
        runtime = RuntimeOptions()
        return self.describe_apisec_events_with_options(request, runtime)

    async def describe_apisec_events_async(
        self,
        request: main_models.DescribeApisecEventsRequest,
    ) -> main_models.DescribeApisecEventsResponse:
        runtime = RuntimeOptions()
        return await self.describe_apisec_events_with_options_async(request, runtime)

    def describe_apisec_examples_with_options(
        self,
        request: main_models.DescribeApisecExamplesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecExamplesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.abnormal_tag):
            query['AbnormalTag'] = request.abnormal_tag
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.example_type):
            query['ExampleType'] = request.example_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_sensitive_type_list):
            query['RequestSensitiveTypeList'] = request.request_sensitive_type_list
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.response_sensitive_type_list):
            query['ResponseSensitiveTypeList'] = request.response_sensitive_type_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecExamples',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecExamplesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_examples_with_options_async(
        self,
        request: main_models.DescribeApisecExamplesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecExamplesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.abnormal_tag):
            query['AbnormalTag'] = request.abnormal_tag
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.example_type):
            query['ExampleType'] = request.example_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_sensitive_type_list):
            query['RequestSensitiveTypeList'] = request.request_sensitive_type_list
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.response_sensitive_type_list):
            query['ResponseSensitiveTypeList'] = request.response_sensitive_type_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecExamples',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecExamplesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_examples(
        self,
        request: main_models.DescribeApisecExamplesRequest,
    ) -> main_models.DescribeApisecExamplesResponse:
        runtime = RuntimeOptions()
        return self.describe_apisec_examples_with_options(request, runtime)

    async def describe_apisec_examples_async(
        self,
        request: main_models.DescribeApisecExamplesRequest,
    ) -> main_models.DescribeApisecExamplesResponse:
        runtime = RuntimeOptions()
        return await self.describe_apisec_examples_with_options_async(request, runtime)

    def describe_apisec_log_deliveries_with_options(
        self,
        request: main_models.DescribeApisecLogDeliveriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecLogDeliveriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecLogDeliveries',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecLogDeliveriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_log_deliveries_with_options_async(
        self,
        request: main_models.DescribeApisecLogDeliveriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecLogDeliveriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecLogDeliveries',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecLogDeliveriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_log_deliveries(
        self,
        request: main_models.DescribeApisecLogDeliveriesRequest,
    ) -> main_models.DescribeApisecLogDeliveriesResponse:
        runtime = RuntimeOptions()
        return self.describe_apisec_log_deliveries_with_options(request, runtime)

    async def describe_apisec_log_deliveries_async(
        self,
        request: main_models.DescribeApisecLogDeliveriesRequest,
    ) -> main_models.DescribeApisecLogDeliveriesResponse:
        runtime = RuntimeOptions()
        return await self.describe_apisec_log_deliveries_with_options_async(request, runtime)

    def describe_apisec_matched_hosts_with_options(
        self,
        request: main_models.DescribeApisecMatchedHostsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecMatchedHostsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.matched_host):
            query['MatchedHost'] = request.matched_host
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecMatchedHosts',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecMatchedHostsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_matched_hosts_with_options_async(
        self,
        request: main_models.DescribeApisecMatchedHostsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecMatchedHostsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.matched_host):
            query['MatchedHost'] = request.matched_host
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecMatchedHosts',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecMatchedHostsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_matched_hosts(
        self,
        request: main_models.DescribeApisecMatchedHostsRequest,
    ) -> main_models.DescribeApisecMatchedHostsResponse:
        runtime = RuntimeOptions()
        return self.describe_apisec_matched_hosts_with_options(request, runtime)

    async def describe_apisec_matched_hosts_async(
        self,
        request: main_models.DescribeApisecMatchedHostsRequest,
    ) -> main_models.DescribeApisecMatchedHostsResponse:
        runtime = RuntimeOptions()
        return await self.describe_apisec_matched_hosts_with_options_async(request, runtime)

    def describe_apisec_protection_groups_with_options(
        self,
        request: main_models.DescribeApisecProtectionGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecProtectionGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apisec_status):
            query['ApisecStatus'] = request.apisec_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group):
            query['ResourceGroup'] = request.resource_group
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecProtectionGroups',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecProtectionGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_protection_groups_with_options_async(
        self,
        request: main_models.DescribeApisecProtectionGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecProtectionGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apisec_status):
            query['ApisecStatus'] = request.apisec_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group):
            query['ResourceGroup'] = request.resource_group
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecProtectionGroups',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecProtectionGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_protection_groups(
        self,
        request: main_models.DescribeApisecProtectionGroupsRequest,
    ) -> main_models.DescribeApisecProtectionGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_apisec_protection_groups_with_options(request, runtime)

    async def describe_apisec_protection_groups_async(
        self,
        request: main_models.DescribeApisecProtectionGroupsRequest,
    ) -> main_models.DescribeApisecProtectionGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_apisec_protection_groups_with_options_async(request, runtime)

    def describe_apisec_protection_resources_with_options(
        self,
        request: main_models.DescribeApisecProtectionResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecProtectionResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apisec_status):
            query['ApisecStatus'] = request.apisec_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecProtectionResources',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecProtectionResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_protection_resources_with_options_async(
        self,
        request: main_models.DescribeApisecProtectionResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecProtectionResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apisec_status):
            query['ApisecStatus'] = request.apisec_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecProtectionResources',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecProtectionResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_protection_resources(
        self,
        request: main_models.DescribeApisecProtectionResourcesRequest,
    ) -> main_models.DescribeApisecProtectionResourcesResponse:
        runtime = RuntimeOptions()
        return self.describe_apisec_protection_resources_with_options(request, runtime)

    async def describe_apisec_protection_resources_async(
        self,
        request: main_models.DescribeApisecProtectionResourcesRequest,
    ) -> main_models.DescribeApisecProtectionResourcesResponse:
        runtime = RuntimeOptions()
        return await self.describe_apisec_protection_resources_with_options_async(request, runtime)

    def describe_apisec_rules_with_options(
        self,
        request: main_models.DescribeApisecRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.origin):
            query['Origin'] = request.origin
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecRules',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_rules_with_options_async(
        self,
        request: main_models.DescribeApisecRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.origin):
            query['Origin'] = request.origin
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecRules',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_rules(
        self,
        request: main_models.DescribeApisecRulesRequest,
    ) -> main_models.DescribeApisecRulesResponse:
        runtime = RuntimeOptions()
        return self.describe_apisec_rules_with_options(request, runtime)

    async def describe_apisec_rules_async(
        self,
        request: main_models.DescribeApisecRulesRequest,
    ) -> main_models.DescribeApisecRulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_apisec_rules_with_options_async(request, runtime)

    def describe_apisec_sensitive_domain_statistic_with_options(
        self,
        request: main_models.DescribeApisecSensitiveDomainStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecSensitiveDomainStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_way):
            query['OrderWay'] = request.order_way
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecSensitiveDomainStatistic',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecSensitiveDomainStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_sensitive_domain_statistic_with_options_async(
        self,
        request: main_models.DescribeApisecSensitiveDomainStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecSensitiveDomainStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_way):
            query['OrderWay'] = request.order_way
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecSensitiveDomainStatistic',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecSensitiveDomainStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_sensitive_domain_statistic(
        self,
        request: main_models.DescribeApisecSensitiveDomainStatisticRequest,
    ) -> main_models.DescribeApisecSensitiveDomainStatisticResponse:
        runtime = RuntimeOptions()
        return self.describe_apisec_sensitive_domain_statistic_with_options(request, runtime)

    async def describe_apisec_sensitive_domain_statistic_async(
        self,
        request: main_models.DescribeApisecSensitiveDomainStatisticRequest,
    ) -> main_models.DescribeApisecSensitiveDomainStatisticResponse:
        runtime = RuntimeOptions()
        return await self.describe_apisec_sensitive_domain_statistic_with_options_async(request, runtime)

    def describe_apisec_sls_log_stores_with_options(
        self,
        request: main_models.DescribeApisecSlsLogStoresRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecSlsLogStoresResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.log_region_id):
            query['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecSlsLogStores',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecSlsLogStoresResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_sls_log_stores_with_options_async(
        self,
        request: main_models.DescribeApisecSlsLogStoresRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecSlsLogStoresResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.log_region_id):
            query['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecSlsLogStores',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecSlsLogStoresResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_sls_log_stores(
        self,
        request: main_models.DescribeApisecSlsLogStoresRequest,
    ) -> main_models.DescribeApisecSlsLogStoresResponse:
        runtime = RuntimeOptions()
        return self.describe_apisec_sls_log_stores_with_options(request, runtime)

    async def describe_apisec_sls_log_stores_async(
        self,
        request: main_models.DescribeApisecSlsLogStoresRequest,
    ) -> main_models.DescribeApisecSlsLogStoresResponse:
        runtime = RuntimeOptions()
        return await self.describe_apisec_sls_log_stores_with_options_async(request, runtime)

    def describe_apisec_sls_projects_with_options(
        self,
        request: main_models.DescribeApisecSlsProjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecSlsProjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.log_region_id):
            query['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecSlsProjects',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecSlsProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_sls_projects_with_options_async(
        self,
        request: main_models.DescribeApisecSlsProjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecSlsProjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.log_region_id):
            query['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecSlsProjects',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecSlsProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_sls_projects(
        self,
        request: main_models.DescribeApisecSlsProjectsRequest,
    ) -> main_models.DescribeApisecSlsProjectsResponse:
        runtime = RuntimeOptions()
        return self.describe_apisec_sls_projects_with_options(request, runtime)

    async def describe_apisec_sls_projects_async(
        self,
        request: main_models.DescribeApisecSlsProjectsRequest,
    ) -> main_models.DescribeApisecSlsProjectsResponse:
        runtime = RuntimeOptions()
        return await self.describe_apisec_sls_projects_with_options_async(request, runtime)

    def describe_apisec_statistics_with_options(
        self,
        request: main_models.DescribeApisecStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_status_list):
            query['UserStatusList'] = request.user_status_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecStatistics',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_statistics_with_options_async(
        self,
        request: main_models.DescribeApisecStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_status_list):
            query['UserStatusList'] = request.user_status_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecStatistics',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_statistics(
        self,
        request: main_models.DescribeApisecStatisticsRequest,
    ) -> main_models.DescribeApisecStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_apisec_statistics_with_options(request, runtime)

    async def describe_apisec_statistics_async(
        self,
        request: main_models.DescribeApisecStatisticsRequest,
    ) -> main_models.DescribeApisecStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_apisec_statistics_with_options_async(request, runtime)

    def describe_apisec_suggestions_with_options(
        self,
        request: main_models.DescribeApisecSuggestionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecSuggestionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecSuggestions',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecSuggestionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_suggestions_with_options_async(
        self,
        request: main_models.DescribeApisecSuggestionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecSuggestionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecSuggestions',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecSuggestionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_suggestions(
        self,
        request: main_models.DescribeApisecSuggestionsRequest,
    ) -> main_models.DescribeApisecSuggestionsResponse:
        runtime = RuntimeOptions()
        return self.describe_apisec_suggestions_with_options(request, runtime)

    async def describe_apisec_suggestions_async(
        self,
        request: main_models.DescribeApisecSuggestionsRequest,
    ) -> main_models.DescribeApisecSuggestionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_apisec_suggestions_with_options_async(request, runtime)

    def describe_apisec_user_operations_with_options(
        self,
        request: main_models.DescribeApisecUserOperationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecUserOperationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.object_id):
            query['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecUserOperations',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecUserOperationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apisec_user_operations_with_options_async(
        self,
        request: main_models.DescribeApisecUserOperationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApisecUserOperationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.object_id):
            query['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApisecUserOperations',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApisecUserOperationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apisec_user_operations(
        self,
        request: main_models.DescribeApisecUserOperationsRequest,
    ) -> main_models.DescribeApisecUserOperationsResponse:
        runtime = RuntimeOptions()
        return self.describe_apisec_user_operations_with_options(request, runtime)

    async def describe_apisec_user_operations_async(
        self,
        request: main_models.DescribeApisecUserOperationsRequest,
    ) -> main_models.DescribeApisecUserOperationsResponse:
        runtime = RuntimeOptions()
        return await self.describe_apisec_user_operations_with_options_async(request, runtime)

    def describe_base_system_rules_with_options(
        self,
        request: main_models.DescribeBaseSystemRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBaseSystemRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.detect_type):
            query['DetectType'] = request.detect_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.rule_action):
            query['RuleAction'] = request.rule_action
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_status):
            query['RuleStatus'] = request.rule_status
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBaseSystemRules',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBaseSystemRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_base_system_rules_with_options_async(
        self,
        request: main_models.DescribeBaseSystemRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBaseSystemRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.detect_type):
            query['DetectType'] = request.detect_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.rule_action):
            query['RuleAction'] = request.rule_action
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_status):
            query['RuleStatus'] = request.rule_status
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBaseSystemRules',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBaseSystemRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_base_system_rules(
        self,
        request: main_models.DescribeBaseSystemRulesRequest,
    ) -> main_models.DescribeBaseSystemRulesResponse:
        runtime = RuntimeOptions()
        return self.describe_base_system_rules_with_options(request, runtime)

    async def describe_base_system_rules_async(
        self,
        request: main_models.DescribeBaseSystemRulesRequest,
    ) -> main_models.DescribeBaseSystemRulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_base_system_rules_with_options_async(request, runtime)

    def describe_bot_app_key_with_options(
        self,
        request: main_models.DescribeBotAppKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBotAppKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.key_version):
            query['KeyVersion'] = request.key_version
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBotAppKey',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBotAppKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_bot_app_key_with_options_async(
        self,
        request: main_models.DescribeBotAppKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBotAppKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.key_version):
            query['KeyVersion'] = request.key_version
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBotAppKey',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBotAppKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_bot_app_key(
        self,
        request: main_models.DescribeBotAppKeyRequest,
    ) -> main_models.DescribeBotAppKeyResponse:
        runtime = RuntimeOptions()
        return self.describe_bot_app_key_with_options(request, runtime)

    async def describe_bot_app_key_async(
        self,
        request: main_models.DescribeBotAppKeyRequest,
    ) -> main_models.DescribeBotAppKeyResponse:
        runtime = RuntimeOptions()
        return await self.describe_bot_app_key_with_options_async(request, runtime)

    def describe_bot_rule_labels_with_options(
        self,
        request: main_models.DescribeBotRuleLabelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBotRuleLabelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.label_type):
            query['LabelType'] = request.label_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.sub_scene):
            query['SubScene'] = request.sub_scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBotRuleLabels',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBotRuleLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_bot_rule_labels_with_options_async(
        self,
        request: main_models.DescribeBotRuleLabelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBotRuleLabelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.label_type):
            query['LabelType'] = request.label_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.sub_scene):
            query['SubScene'] = request.sub_scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBotRuleLabels',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBotRuleLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_bot_rule_labels(
        self,
        request: main_models.DescribeBotRuleLabelsRequest,
    ) -> main_models.DescribeBotRuleLabelsResponse:
        runtime = RuntimeOptions()
        return self.describe_bot_rule_labels_with_options(request, runtime)

    async def describe_bot_rule_labels_async(
        self,
        request: main_models.DescribeBotRuleLabelsRequest,
    ) -> main_models.DescribeBotRuleLabelsResponse:
        runtime = RuntimeOptions()
        return await self.describe_bot_rule_labels_with_options_async(request, runtime)

    def describe_cert_detail_with_options(
        self,
        request: main_models.DescribeCertDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCertDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCertDetail',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCertDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cert_detail_with_options_async(
        self,
        request: main_models.DescribeCertDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCertDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCertDetail',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCertDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cert_detail(
        self,
        request: main_models.DescribeCertDetailRequest,
    ) -> main_models.DescribeCertDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_cert_detail_with_options(request, runtime)

    async def describe_cert_detail_async(
        self,
        request: main_models.DescribeCertDetailRequest,
    ) -> main_models.DescribeCertDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_cert_detail_with_options_async(request, runtime)

    def describe_certs_with_options(
        self,
        request: main_models.DescribeCertsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCertsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCerts',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_certs_with_options_async(
        self,
        request: main_models.DescribeCertsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCertsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCerts',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCertsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_certs(
        self,
        request: main_models.DescribeCertsRequest,
    ) -> main_models.DescribeCertsResponse:
        runtime = RuntimeOptions()
        return self.describe_certs_with_options(request, runtime)

    async def describe_certs_async(
        self,
        request: main_models.DescribeCertsRequest,
    ) -> main_models.DescribeCertsResponse:
        runtime = RuntimeOptions()
        return await self.describe_certs_with_options_async(request, runtime)

    def describe_charge_module_with_options(
        self,
        request: main_models.DescribeChargeModuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChargeModuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChargeModule',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChargeModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_charge_module_with_options_async(
        self,
        request: main_models.DescribeChargeModuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChargeModuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChargeModule',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChargeModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_charge_module(
        self,
        request: main_models.DescribeChargeModuleRequest,
    ) -> main_models.DescribeChargeModuleResponse:
        runtime = RuntimeOptions()
        return self.describe_charge_module_with_options(request, runtime)

    async def describe_charge_module_async(
        self,
        request: main_models.DescribeChargeModuleRequest,
    ) -> main_models.DescribeChargeModuleResponse:
        runtime = RuntimeOptions()
        return await self.describe_charge_module_with_options_async(request, runtime)

    def describe_charge_result_with_options(
        self,
        request: main_models.DescribeChargeResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChargeResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.charge_cycle):
            query['ChargeCycle'] = request.charge_cycle
        if not DaraCore.is_null(request.charge_modules):
            query['ChargeModules'] = request.charge_modules
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChargeResult',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChargeResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_charge_result_with_options_async(
        self,
        request: main_models.DescribeChargeResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChargeResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.charge_cycle):
            query['ChargeCycle'] = request.charge_cycle
        if not DaraCore.is_null(request.charge_modules):
            query['ChargeModules'] = request.charge_modules
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChargeResult',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChargeResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_charge_result(
        self,
        request: main_models.DescribeChargeResultRequest,
    ) -> main_models.DescribeChargeResultResponse:
        runtime = RuntimeOptions()
        return self.describe_charge_result_with_options(request, runtime)

    async def describe_charge_result_async(
        self,
        request: main_models.DescribeChargeResultRequest,
    ) -> main_models.DescribeChargeResultResponse:
        runtime = RuntimeOptions()
        return await self.describe_charge_result_with_options_async(request, runtime)

    def describe_cloud_resource_access_port_details_with_options(
        self,
        request: main_models.DescribeCloudResourceAccessPortDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudResourceAccessPortDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_product):
            query['ResourceProduct'] = request.resource_product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudResourceAccessPortDetails',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudResourceAccessPortDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_resource_access_port_details_with_options_async(
        self,
        request: main_models.DescribeCloudResourceAccessPortDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudResourceAccessPortDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_product):
            query['ResourceProduct'] = request.resource_product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudResourceAccessPortDetails',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudResourceAccessPortDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_resource_access_port_details(
        self,
        request: main_models.DescribeCloudResourceAccessPortDetailsRequest,
    ) -> main_models.DescribeCloudResourceAccessPortDetailsResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_resource_access_port_details_with_options(request, runtime)

    async def describe_cloud_resource_access_port_details_async(
        self,
        request: main_models.DescribeCloudResourceAccessPortDetailsRequest,
    ) -> main_models.DescribeCloudResourceAccessPortDetailsResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_resource_access_port_details_with_options_async(request, runtime)

    def describe_cloud_resource_accessed_ports_with_options(
        self,
        request: main_models.DescribeCloudResourceAccessedPortsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudResourceAccessedPortsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudResourceAccessedPorts',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudResourceAccessedPortsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_resource_accessed_ports_with_options_async(
        self,
        request: main_models.DescribeCloudResourceAccessedPortsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudResourceAccessedPortsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudResourceAccessedPorts',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudResourceAccessedPortsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_resource_accessed_ports(
        self,
        request: main_models.DescribeCloudResourceAccessedPortsRequest,
    ) -> main_models.DescribeCloudResourceAccessedPortsResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_resource_accessed_ports_with_options(request, runtime)

    async def describe_cloud_resource_accessed_ports_async(
        self,
        request: main_models.DescribeCloudResourceAccessedPortsRequest,
    ) -> main_models.DescribeCloudResourceAccessedPortsResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_resource_accessed_ports_with_options_async(request, runtime)

    def describe_cloud_resources_with_options(
        self,
        request: main_models.DescribeCloudResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_domain):
            query['ResourceDomain'] = request.resource_domain
        if not DaraCore.is_null(request.resource_function):
            query['ResourceFunction'] = request.resource_function
        if not DaraCore.is_null(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not DaraCore.is_null(request.resource_instance_name):
            query['ResourceInstanceName'] = request.resource_instance_name
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_product):
            query['ResourceProduct'] = request.resource_product
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_route_name):
            query['ResourceRouteName'] = request.resource_route_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudResources',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_resources_with_options_async(
        self,
        request: main_models.DescribeCloudResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_domain):
            query['ResourceDomain'] = request.resource_domain
        if not DaraCore.is_null(request.resource_function):
            query['ResourceFunction'] = request.resource_function
        if not DaraCore.is_null(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not DaraCore.is_null(request.resource_instance_name):
            query['ResourceInstanceName'] = request.resource_instance_name
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_product):
            query['ResourceProduct'] = request.resource_product
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_route_name):
            query['ResourceRouteName'] = request.resource_route_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudResources',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_resources(
        self,
        request: main_models.DescribeCloudResourcesRequest,
    ) -> main_models.DescribeCloudResourcesResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_resources_with_options(request, runtime)

    async def describe_cloud_resources_async(
        self,
        request: main_models.DescribeCloudResourcesRequest,
    ) -> main_models.DescribeCloudResourcesResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_resources_with_options_async(request, runtime)

    def describe_cname_count_with_options(
        self,
        request: main_models.DescribeCnameCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCnameCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCnameCount',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCnameCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cname_count_with_options_async(
        self,
        request: main_models.DescribeCnameCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCnameCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCnameCount',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCnameCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cname_count(
        self,
        request: main_models.DescribeCnameCountRequest,
    ) -> main_models.DescribeCnameCountResponse:
        runtime = RuntimeOptions()
        return self.describe_cname_count_with_options(request, runtime)

    async def describe_cname_count_async(
        self,
        request: main_models.DescribeCnameCountRequest,
    ) -> main_models.DescribeCnameCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_cname_count_with_options_async(request, runtime)

    def describe_common_log_fields_with_options(
        self,
        tmp_req: main_models.DescribeCommonLogFieldsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCommonLogFieldsResponse:
        tmp_req.validate()
        request = main_models.DescribeCommonLogFieldsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.log_key_list):
            request.log_key_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.log_key_list, 'LogKeyList', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_default):
            query['IsDefault'] = request.is_default
        if not DaraCore.is_null(request.is_required):
            query['IsRequired'] = request.is_required
        if not DaraCore.is_null(request.log_key_list_shrink):
            query['LogKeyList'] = request.log_key_list_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCommonLogFields',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCommonLogFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_common_log_fields_with_options_async(
        self,
        tmp_req: main_models.DescribeCommonLogFieldsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCommonLogFieldsResponse:
        tmp_req.validate()
        request = main_models.DescribeCommonLogFieldsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.log_key_list):
            request.log_key_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.log_key_list, 'LogKeyList', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_default):
            query['IsDefault'] = request.is_default
        if not DaraCore.is_null(request.is_required):
            query['IsRequired'] = request.is_required
        if not DaraCore.is_null(request.log_key_list_shrink):
            query['LogKeyList'] = request.log_key_list_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCommonLogFields',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCommonLogFieldsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_common_log_fields(
        self,
        request: main_models.DescribeCommonLogFieldsRequest,
    ) -> main_models.DescribeCommonLogFieldsResponse:
        runtime = RuntimeOptions()
        return self.describe_common_log_fields_with_options(request, runtime)

    async def describe_common_log_fields_async(
        self,
        request: main_models.DescribeCommonLogFieldsRequest,
    ) -> main_models.DescribeCommonLogFieldsResponse:
        runtime = RuntimeOptions()
        return await self.describe_common_log_fields_with_options_async(request, runtime)

    def describe_custom_base_rule_compile_result_with_options(
        self,
        request: main_models.DescribeCustomBaseRuleCompileResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomBaseRuleCompileResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomBaseRuleCompileResult',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomBaseRuleCompileResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_base_rule_compile_result_with_options_async(
        self,
        request: main_models.DescribeCustomBaseRuleCompileResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomBaseRuleCompileResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomBaseRuleCompileResult',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomBaseRuleCompileResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_base_rule_compile_result(
        self,
        request: main_models.DescribeCustomBaseRuleCompileResultRequest,
    ) -> main_models.DescribeCustomBaseRuleCompileResultResponse:
        runtime = RuntimeOptions()
        return self.describe_custom_base_rule_compile_result_with_options(request, runtime)

    async def describe_custom_base_rule_compile_result_async(
        self,
        request: main_models.DescribeCustomBaseRuleCompileResultRequest,
    ) -> main_models.DescribeCustomBaseRuleCompileResultResponse:
        runtime = RuntimeOptions()
        return await self.describe_custom_base_rule_compile_result_with_options_async(request, runtime)

    def describe_ddo_sstatus_with_options(
        self,
        request: main_models.DescribeDDoSStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDDoSStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDDoSStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDDoSStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddo_sstatus_with_options_async(
        self,
        request: main_models.DescribeDDoSStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDDoSStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDDoSStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDDoSStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ddo_sstatus(
        self,
        request: main_models.DescribeDDoSStatusRequest,
    ) -> main_models.DescribeDDoSStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_ddo_sstatus_with_options(request, runtime)

    async def describe_ddo_sstatus_async(
        self,
        request: main_models.DescribeDDoSStatusRequest,
    ) -> main_models.DescribeDDoSStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_ddo_sstatus_with_options_async(request, runtime)

    def describe_default_https_with_options(
        self,
        request: main_models.DescribeDefaultHttpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefaultHttpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefaultHttps',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefaultHttpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_default_https_with_options_async(
        self,
        request: main_models.DescribeDefaultHttpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefaultHttpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefaultHttps',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefaultHttpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_default_https(
        self,
        request: main_models.DescribeDefaultHttpsRequest,
    ) -> main_models.DescribeDefaultHttpsResponse:
        runtime = RuntimeOptions()
        return self.describe_default_https_with_options(request, runtime)

    async def describe_default_https_async(
        self,
        request: main_models.DescribeDefaultHttpsRequest,
    ) -> main_models.DescribeDefaultHttpsResponse:
        runtime = RuntimeOptions()
        return await self.describe_default_https_with_options_async(request, runtime)

    def describe_defense_group_valid_resources_with_options(
        self,
        request: main_models.DescribeDefenseGroupValidResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseGroupValidResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseGroupValidResources',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseGroupValidResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_group_valid_resources_with_options_async(
        self,
        request: main_models.DescribeDefenseGroupValidResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseGroupValidResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseGroupValidResources',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseGroupValidResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_group_valid_resources(
        self,
        request: main_models.DescribeDefenseGroupValidResourcesRequest,
    ) -> main_models.DescribeDefenseGroupValidResourcesResponse:
        runtime = RuntimeOptions()
        return self.describe_defense_group_valid_resources_with_options(request, runtime)

    async def describe_defense_group_valid_resources_async(
        self,
        request: main_models.DescribeDefenseGroupValidResourcesRequest,
    ) -> main_models.DescribeDefenseGroupValidResourcesResponse:
        runtime = RuntimeOptions()
        return await self.describe_defense_group_valid_resources_with_options_async(request, runtime)

    def describe_defense_resource_with_options(
        self,
        request: main_models.DescribeDefenseResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseResource',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_resource_with_options_async(
        self,
        request: main_models.DescribeDefenseResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseResource',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_resource(
        self,
        request: main_models.DescribeDefenseResourceRequest,
    ) -> main_models.DescribeDefenseResourceResponse:
        runtime = RuntimeOptions()
        return self.describe_defense_resource_with_options(request, runtime)

    async def describe_defense_resource_async(
        self,
        request: main_models.DescribeDefenseResourceRequest,
    ) -> main_models.DescribeDefenseResourceResponse:
        runtime = RuntimeOptions()
        return await self.describe_defense_resource_with_options_async(request, runtime)

    def describe_defense_resource_group_with_options(
        self,
        request: main_models.DescribeDefenseResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseResourceGroup',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_resource_group_with_options_async(
        self,
        request: main_models.DescribeDefenseResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseResourceGroup',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_resource_group(
        self,
        request: main_models.DescribeDefenseResourceGroupRequest,
    ) -> main_models.DescribeDefenseResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.describe_defense_resource_group_with_options(request, runtime)

    async def describe_defense_resource_group_async(
        self,
        request: main_models.DescribeDefenseResourceGroupRequest,
    ) -> main_models.DescribeDefenseResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.describe_defense_resource_group_with_options_async(request, runtime)

    def describe_defense_resource_group_names_with_options(
        self,
        request: main_models.DescribeDefenseResourceGroupNamesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseResourceGroupNamesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name_like):
            query['GroupNameLike'] = request.group_name_like
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseResourceGroupNames',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseResourceGroupNamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_resource_group_names_with_options_async(
        self,
        request: main_models.DescribeDefenseResourceGroupNamesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseResourceGroupNamesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name_like):
            query['GroupNameLike'] = request.group_name_like
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseResourceGroupNames',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseResourceGroupNamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_resource_group_names(
        self,
        request: main_models.DescribeDefenseResourceGroupNamesRequest,
    ) -> main_models.DescribeDefenseResourceGroupNamesResponse:
        runtime = RuntimeOptions()
        return self.describe_defense_resource_group_names_with_options(request, runtime)

    async def describe_defense_resource_group_names_async(
        self,
        request: main_models.DescribeDefenseResourceGroupNamesRequest,
    ) -> main_models.DescribeDefenseResourceGroupNamesResponse:
        runtime = RuntimeOptions()
        return await self.describe_defense_resource_group_names_with_options_async(request, runtime)

    def describe_defense_resource_groups_with_options(
        self,
        request: main_models.DescribeDefenseResourceGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseResourceGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name_like):
            query['GroupNameLike'] = request.group_name_like
        if not DaraCore.is_null(request.group_names):
            query['GroupNames'] = request.group_names
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseResourceGroups',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseResourceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_resource_groups_with_options_async(
        self,
        request: main_models.DescribeDefenseResourceGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseResourceGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name_like):
            query['GroupNameLike'] = request.group_name_like
        if not DaraCore.is_null(request.group_names):
            query['GroupNames'] = request.group_names
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseResourceGroups',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseResourceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_resource_groups(
        self,
        request: main_models.DescribeDefenseResourceGroupsRequest,
    ) -> main_models.DescribeDefenseResourceGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_defense_resource_groups_with_options(request, runtime)

    async def describe_defense_resource_groups_async(
        self,
        request: main_models.DescribeDefenseResourceGroupsRequest,
    ) -> main_models.DescribeDefenseResourceGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_defense_resource_groups_with_options_async(request, runtime)

    def describe_defense_resource_names_with_options(
        self,
        request: main_models.DescribeDefenseResourceNamesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseResourceNamesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseResourceNames',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseResourceNamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_resource_names_with_options_async(
        self,
        request: main_models.DescribeDefenseResourceNamesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseResourceNamesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseResourceNames',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseResourceNamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_resource_names(
        self,
        request: main_models.DescribeDefenseResourceNamesRequest,
    ) -> main_models.DescribeDefenseResourceNamesResponse:
        runtime = RuntimeOptions()
        return self.describe_defense_resource_names_with_options(request, runtime)

    async def describe_defense_resource_names_async(
        self,
        request: main_models.DescribeDefenseResourceNamesRequest,
    ) -> main_models.DescribeDefenseResourceNamesResponse:
        runtime = RuntimeOptions()
        return await self.describe_defense_resource_names_with_options_async(request, runtime)

    def describe_defense_resource_owner_uid_with_options(
        self,
        request: main_models.DescribeDefenseResourceOwnerUidRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseResourceOwnerUidResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_names):
            query['ResourceNames'] = request.resource_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseResourceOwnerUid',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseResourceOwnerUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_resource_owner_uid_with_options_async(
        self,
        request: main_models.DescribeDefenseResourceOwnerUidRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseResourceOwnerUidResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_names):
            query['ResourceNames'] = request.resource_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseResourceOwnerUid',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseResourceOwnerUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_resource_owner_uid(
        self,
        request: main_models.DescribeDefenseResourceOwnerUidRequest,
    ) -> main_models.DescribeDefenseResourceOwnerUidResponse:
        runtime = RuntimeOptions()
        return self.describe_defense_resource_owner_uid_with_options(request, runtime)

    async def describe_defense_resource_owner_uid_async(
        self,
        request: main_models.DescribeDefenseResourceOwnerUidRequest,
    ) -> main_models.DescribeDefenseResourceOwnerUidResponse:
        runtime = RuntimeOptions()
        return await self.describe_defense_resource_owner_uid_with_options_async(request, runtime)

    def describe_defense_resource_templates_with_options(
        self,
        request: main_models.DescribeDefenseResourceTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseResourceTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseResourceTemplates',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseResourceTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_resource_templates_with_options_async(
        self,
        request: main_models.DescribeDefenseResourceTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseResourceTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseResourceTemplates',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseResourceTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_resource_templates(
        self,
        request: main_models.DescribeDefenseResourceTemplatesRequest,
    ) -> main_models.DescribeDefenseResourceTemplatesResponse:
        runtime = RuntimeOptions()
        return self.describe_defense_resource_templates_with_options(request, runtime)

    async def describe_defense_resource_templates_async(
        self,
        request: main_models.DescribeDefenseResourceTemplatesRequest,
    ) -> main_models.DescribeDefenseResourceTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.describe_defense_resource_templates_with_options_async(request, runtime)

    def describe_defense_resources_with_options(
        self,
        request: main_models.DescribeDefenseResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseResources',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_resources_with_options_async(
        self,
        request: main_models.DescribeDefenseResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseResources',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_resources(
        self,
        request: main_models.DescribeDefenseResourcesRequest,
    ) -> main_models.DescribeDefenseResourcesResponse:
        runtime = RuntimeOptions()
        return self.describe_defense_resources_with_options(request, runtime)

    async def describe_defense_resources_async(
        self,
        request: main_models.DescribeDefenseResourcesRequest,
    ) -> main_models.DescribeDefenseResourcesResponse:
        runtime = RuntimeOptions()
        return await self.describe_defense_resources_with_options_async(request, runtime)

    def describe_defense_rule_with_options(
        self,
        request: main_models.DescribeDefenseRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseRule',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_rule_with_options_async(
        self,
        request: main_models.DescribeDefenseRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseRule',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_rule(
        self,
        request: main_models.DescribeDefenseRuleRequest,
    ) -> main_models.DescribeDefenseRuleResponse:
        runtime = RuntimeOptions()
        return self.describe_defense_rule_with_options(request, runtime)

    async def describe_defense_rule_async(
        self,
        request: main_models.DescribeDefenseRuleRequest,
    ) -> main_models.DescribeDefenseRuleResponse:
        runtime = RuntimeOptions()
        return await self.describe_defense_rule_with_options_async(request, runtime)

    def describe_defense_rule_statistics_with_options(
        self,
        request: main_models.DescribeDefenseRuleStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseRuleStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fourth_key):
            query['FourthKey'] = request.fourth_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.primary_key):
            query['PrimaryKey'] = request.primary_key
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.secondary_key):
            query['SecondaryKey'] = request.secondary_key
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.third_key):
            query['ThirdKey'] = request.third_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseRuleStatistics',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseRuleStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_rule_statistics_with_options_async(
        self,
        request: main_models.DescribeDefenseRuleStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseRuleStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fourth_key):
            query['FourthKey'] = request.fourth_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.primary_key):
            query['PrimaryKey'] = request.primary_key
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.secondary_key):
            query['SecondaryKey'] = request.secondary_key
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.third_key):
            query['ThirdKey'] = request.third_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseRuleStatistics',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseRuleStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_rule_statistics(
        self,
        request: main_models.DescribeDefenseRuleStatisticsRequest,
    ) -> main_models.DescribeDefenseRuleStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_defense_rule_statistics_with_options(request, runtime)

    async def describe_defense_rule_statistics_async(
        self,
        request: main_models.DescribeDefenseRuleStatisticsRequest,
    ) -> main_models.DescribeDefenseRuleStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_defense_rule_statistics_with_options_async(request, runtime)

    def describe_defense_rules_with_options(
        self,
        request: main_models.DescribeDefenseRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseRules',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_rules_with_options_async(
        self,
        request: main_models.DescribeDefenseRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseRules',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_rules(
        self,
        request: main_models.DescribeDefenseRulesRequest,
    ) -> main_models.DescribeDefenseRulesResponse:
        runtime = RuntimeOptions()
        return self.describe_defense_rules_with_options(request, runtime)

    async def describe_defense_rules_async(
        self,
        request: main_models.DescribeDefenseRulesRequest,
    ) -> main_models.DescribeDefenseRulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_defense_rules_with_options_async(request, runtime)

    def describe_defense_scene_config_with_options(
        self,
        request: main_models.DescribeDefenseSceneConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseSceneConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_key):
            query['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseSceneConfig',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseSceneConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_scene_config_with_options_async(
        self,
        request: main_models.DescribeDefenseSceneConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseSceneConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_key):
            query['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseSceneConfig',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseSceneConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_scene_config(
        self,
        request: main_models.DescribeDefenseSceneConfigRequest,
    ) -> main_models.DescribeDefenseSceneConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_defense_scene_config_with_options(request, runtime)

    async def describe_defense_scene_config_async(
        self,
        request: main_models.DescribeDefenseSceneConfigRequest,
    ) -> main_models.DescribeDefenseSceneConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_defense_scene_config_with_options_async(request, runtime)

    def describe_defense_template_with_options(
        self,
        request: main_models.DescribeDefenseTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseTemplate',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_template_with_options_async(
        self,
        request: main_models.DescribeDefenseTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseTemplate',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_template(
        self,
        request: main_models.DescribeDefenseTemplateRequest,
    ) -> main_models.DescribeDefenseTemplateResponse:
        runtime = RuntimeOptions()
        return self.describe_defense_template_with_options(request, runtime)

    async def describe_defense_template_async(
        self,
        request: main_models.DescribeDefenseTemplateRequest,
    ) -> main_models.DescribeDefenseTemplateResponse:
        runtime = RuntimeOptions()
        return await self.describe_defense_template_with_options_async(request, runtime)

    def describe_defense_template_valid_groups_with_options(
        self,
        request: main_models.DescribeDefenseTemplateValidGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseTemplateValidGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseTemplateValidGroups',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseTemplateValidGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_template_valid_groups_with_options_async(
        self,
        request: main_models.DescribeDefenseTemplateValidGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseTemplateValidGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseTemplateValidGroups',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseTemplateValidGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_template_valid_groups(
        self,
        request: main_models.DescribeDefenseTemplateValidGroupsRequest,
    ) -> main_models.DescribeDefenseTemplateValidGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_defense_template_valid_groups_with_options(request, runtime)

    async def describe_defense_template_valid_groups_async(
        self,
        request: main_models.DescribeDefenseTemplateValidGroupsRequest,
    ) -> main_models.DescribeDefenseTemplateValidGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_defense_template_valid_groups_with_options_async(request, runtime)

    def describe_defense_template_valid_resources_with_options(
        self,
        request: main_models.DescribeDefenseTemplateValidResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseTemplateValidResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseTemplateValidResources',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseTemplateValidResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_template_valid_resources_with_options_async(
        self,
        request: main_models.DescribeDefenseTemplateValidResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseTemplateValidResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseTemplateValidResources',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseTemplateValidResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_template_valid_resources(
        self,
        request: main_models.DescribeDefenseTemplateValidResourcesRequest,
    ) -> main_models.DescribeDefenseTemplateValidResourcesResponse:
        runtime = RuntimeOptions()
        return self.describe_defense_template_valid_resources_with_options(request, runtime)

    async def describe_defense_template_valid_resources_async(
        self,
        request: main_models.DescribeDefenseTemplateValidResourcesRequest,
    ) -> main_models.DescribeDefenseTemplateValidResourcesResponse:
        runtime = RuntimeOptions()
        return await self.describe_defense_template_valid_resources_with_options_async(request, runtime)

    def describe_defense_templates_with_options(
        self,
        request: main_models.DescribeDefenseTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not DaraCore.is_null(request.defense_sub_scene):
            query['DefenseSubScene'] = request.defense_sub_scene
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_ids):
            query['TemplateIds'] = request.template_ids
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseTemplates',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_defense_templates_with_options_async(
        self,
        request: main_models.DescribeDefenseTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefenseTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not DaraCore.is_null(request.defense_sub_scene):
            query['DefenseSubScene'] = request.defense_sub_scene
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_ids):
            query['TemplateIds'] = request.template_ids
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefenseTemplates',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefenseTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_defense_templates(
        self,
        request: main_models.DescribeDefenseTemplatesRequest,
    ) -> main_models.DescribeDefenseTemplatesResponse:
        runtime = RuntimeOptions()
        return self.describe_defense_templates_with_options(request, runtime)

    async def describe_defense_templates_async(
        self,
        request: main_models.DescribeDefenseTemplatesRequest,
    ) -> main_models.DescribeDefenseTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.describe_defense_templates_with_options_async(request, runtime)

    def describe_domain_dnsrecord_with_options(
        self,
        request: main_models.DescribeDomainDNSRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainDNSRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainDNSRecord',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainDNSRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_dnsrecord_with_options_async(
        self,
        request: main_models.DescribeDomainDNSRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainDNSRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainDNSRecord',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainDNSRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_dnsrecord(
        self,
        request: main_models.DescribeDomainDNSRecordRequest,
    ) -> main_models.DescribeDomainDNSRecordResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_dnsrecord_with_options(request, runtime)

    async def describe_domain_dnsrecord_async(
        self,
        request: main_models.DescribeDomainDNSRecordRequest,
    ) -> main_models.DescribeDomainDNSRecordResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_dnsrecord_with_options_async(request, runtime)

    def describe_domain_detail_with_options(
        self,
        request: main_models.DescribeDomainDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainDetail',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_detail_with_options_async(
        self,
        request: main_models.DescribeDomainDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainDetail',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_detail(
        self,
        request: main_models.DescribeDomainDetailRequest,
    ) -> main_models.DescribeDomainDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_detail_with_options(request, runtime)

    async def describe_domain_detail_async(
        self,
        request: main_models.DescribeDomainDetailRequest,
    ) -> main_models.DescribeDomainDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_detail_with_options_async(request, runtime)

    def describe_domain_used_ports_with_options(
        self,
        request: main_models.DescribeDomainUsedPortsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainUsedPortsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainUsedPorts',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainUsedPortsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_used_ports_with_options_async(
        self,
        request: main_models.DescribeDomainUsedPortsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainUsedPortsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainUsedPorts',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainUsedPortsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_used_ports(
        self,
        request: main_models.DescribeDomainUsedPortsRequest,
    ) -> main_models.DescribeDomainUsedPortsResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_used_ports_with_options(request, runtime)

    async def describe_domain_used_ports_async(
        self,
        request: main_models.DescribeDomainUsedPortsRequest,
    ) -> main_models.DescribeDomainUsedPortsResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_used_ports_with_options_async(request, runtime)

    def describe_domains_with_options(
        self,
        request: main_models.DescribeDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend):
            query['Backend'] = request.backend
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomains',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domains_with_options_async(
        self,
        request: main_models.DescribeDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend):
            query['Backend'] = request.backend
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomains',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domains(
        self,
        request: main_models.DescribeDomainsRequest,
    ) -> main_models.DescribeDomainsResponse:
        runtime = RuntimeOptions()
        return self.describe_domains_with_options(request, runtime)

    async def describe_domains_async(
        self,
        request: main_models.DescribeDomainsRequest,
    ) -> main_models.DescribeDomainsResponse:
        runtime = RuntimeOptions()
        return await self.describe_domains_with_options_async(request, runtime)

    def describe_flow_chart_with_options(
        self,
        request: main_models.DescribeFlowChartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFlowChartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFlowChart',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFlowChartResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_chart_with_options_async(
        self,
        request: main_models.DescribeFlowChartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFlowChartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFlowChart',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFlowChartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_flow_chart(
        self,
        request: main_models.DescribeFlowChartRequest,
    ) -> main_models.DescribeFlowChartResponse:
        runtime = RuntimeOptions()
        return self.describe_flow_chart_with_options(request, runtime)

    async def describe_flow_chart_async(
        self,
        request: main_models.DescribeFlowChartRequest,
    ) -> main_models.DescribeFlowChartResponse:
        runtime = RuntimeOptions()
        return await self.describe_flow_chart_with_options_async(request, runtime)

    def describe_flow_top_resource_with_options(
        self,
        request: main_models.DescribeFlowTopResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFlowTopResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFlowTopResource',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFlowTopResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_top_resource_with_options_async(
        self,
        request: main_models.DescribeFlowTopResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFlowTopResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFlowTopResource',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFlowTopResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_flow_top_resource(
        self,
        request: main_models.DescribeFlowTopResourceRequest,
    ) -> main_models.DescribeFlowTopResourceResponse:
        runtime = RuntimeOptions()
        return self.describe_flow_top_resource_with_options(request, runtime)

    async def describe_flow_top_resource_async(
        self,
        request: main_models.DescribeFlowTopResourceRequest,
    ) -> main_models.DescribeFlowTopResourceResponse:
        runtime = RuntimeOptions()
        return await self.describe_flow_top_resource_with_options_async(request, runtime)

    def describe_flow_top_url_with_options(
        self,
        request: main_models.DescribeFlowTopUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFlowTopUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFlowTopUrl',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFlowTopUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_top_url_with_options_async(
        self,
        request: main_models.DescribeFlowTopUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFlowTopUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFlowTopUrl',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFlowTopUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_flow_top_url(
        self,
        request: main_models.DescribeFlowTopUrlRequest,
    ) -> main_models.DescribeFlowTopUrlResponse:
        runtime = RuntimeOptions()
        return self.describe_flow_top_url_with_options(request, runtime)

    async def describe_flow_top_url_async(
        self,
        request: main_models.DescribeFlowTopUrlRequest,
    ) -> main_models.DescribeFlowTopUrlResponse:
        runtime = RuntimeOptions()
        return await self.describe_flow_top_url_with_options_async(request, runtime)

    def describe_free_user_asset_count_with_options(
        self,
        request: main_models.DescribeFreeUserAssetCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFreeUserAssetCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFreeUserAssetCount',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFreeUserAssetCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_free_user_asset_count_with_options_async(
        self,
        request: main_models.DescribeFreeUserAssetCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFreeUserAssetCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFreeUserAssetCount',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFreeUserAssetCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_free_user_asset_count(
        self,
        request: main_models.DescribeFreeUserAssetCountRequest,
    ) -> main_models.DescribeFreeUserAssetCountResponse:
        runtime = RuntimeOptions()
        return self.describe_free_user_asset_count_with_options(request, runtime)

    async def describe_free_user_asset_count_async(
        self,
        request: main_models.DescribeFreeUserAssetCountRequest,
    ) -> main_models.DescribeFreeUserAssetCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_free_user_asset_count_with_options_async(request, runtime)

    def describe_free_user_event_count_with_options(
        self,
        request: main_models.DescribeFreeUserEventCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFreeUserEventCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFreeUserEventCount',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFreeUserEventCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_free_user_event_count_with_options_async(
        self,
        request: main_models.DescribeFreeUserEventCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFreeUserEventCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFreeUserEventCount',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFreeUserEventCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_free_user_event_count(
        self,
        request: main_models.DescribeFreeUserEventCountRequest,
    ) -> main_models.DescribeFreeUserEventCountResponse:
        runtime = RuntimeOptions()
        return self.describe_free_user_event_count_with_options(request, runtime)

    async def describe_free_user_event_count_async(
        self,
        request: main_models.DescribeFreeUserEventCountRequest,
    ) -> main_models.DescribeFreeUserEventCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_free_user_event_count_with_options_async(request, runtime)

    def describe_free_user_event_types_with_options(
        self,
        request: main_models.DescribeFreeUserEventTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFreeUserEventTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFreeUserEventTypes',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFreeUserEventTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_free_user_event_types_with_options_async(
        self,
        request: main_models.DescribeFreeUserEventTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFreeUserEventTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFreeUserEventTypes',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFreeUserEventTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_free_user_event_types(
        self,
        request: main_models.DescribeFreeUserEventTypesRequest,
    ) -> main_models.DescribeFreeUserEventTypesResponse:
        runtime = RuntimeOptions()
        return self.describe_free_user_event_types_with_options(request, runtime)

    async def describe_free_user_event_types_async(
        self,
        request: main_models.DescribeFreeUserEventTypesRequest,
    ) -> main_models.DescribeFreeUserEventTypesResponse:
        runtime = RuntimeOptions()
        return await self.describe_free_user_event_types_with_options_async(request, runtime)

    def describe_free_user_events_with_options(
        self,
        request: main_models.DescribeFreeUserEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFreeUserEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFreeUserEvents',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFreeUserEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_free_user_events_with_options_async(
        self,
        request: main_models.DescribeFreeUserEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFreeUserEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFreeUserEvents',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFreeUserEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_free_user_events(
        self,
        request: main_models.DescribeFreeUserEventsRequest,
    ) -> main_models.DescribeFreeUserEventsResponse:
        runtime = RuntimeOptions()
        return self.describe_free_user_events_with_options(request, runtime)

    async def describe_free_user_events_async(
        self,
        request: main_models.DescribeFreeUserEventsRequest,
    ) -> main_models.DescribeFreeUserEventsResponse:
        runtime = RuntimeOptions()
        return await self.describe_free_user_events_with_options_async(request, runtime)

    def describe_hybrid_cloud_basic_monitor_with_options(
        self,
        request: main_models.DescribeHybridCloudBasicMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudBasicMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mid):
            query['Mid'] = request.mid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudBasicMonitor',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudBasicMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_cloud_basic_monitor_with_options_async(
        self,
        request: main_models.DescribeHybridCloudBasicMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudBasicMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mid):
            query['Mid'] = request.mid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudBasicMonitor',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudBasicMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_cloud_basic_monitor(
        self,
        request: main_models.DescribeHybridCloudBasicMonitorRequest,
    ) -> main_models.DescribeHybridCloudBasicMonitorResponse:
        runtime = RuntimeOptions()
        return self.describe_hybrid_cloud_basic_monitor_with_options(request, runtime)

    async def describe_hybrid_cloud_basic_monitor_async(
        self,
        request: main_models.DescribeHybridCloudBasicMonitorRequest,
    ) -> main_models.DescribeHybridCloudBasicMonitorResponse:
        runtime = RuntimeOptions()
        return await self.describe_hybrid_cloud_basic_monitor_with_options_async(request, runtime)

    def describe_hybrid_cloud_cluster_rule_with_options(
        self,
        request: main_models.DescribeHybridCloudClusterRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudClusterRuleResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudClusterRule',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudClusterRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_cloud_cluster_rule_with_options_async(
        self,
        request: main_models.DescribeHybridCloudClusterRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudClusterRuleResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudClusterRule',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudClusterRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_cloud_cluster_rule(
        self,
        request: main_models.DescribeHybridCloudClusterRuleRequest,
    ) -> main_models.DescribeHybridCloudClusterRuleResponse:
        runtime = RuntimeOptions()
        return self.describe_hybrid_cloud_cluster_rule_with_options(request, runtime)

    async def describe_hybrid_cloud_cluster_rule_async(
        self,
        request: main_models.DescribeHybridCloudClusterRuleRequest,
    ) -> main_models.DescribeHybridCloudClusterRuleResponse:
        runtime = RuntimeOptions()
        return await self.describe_hybrid_cloud_cluster_rule_with_options_async(request, runtime)

    def describe_hybrid_cloud_cluster_rules_with_options(
        self,
        request: main_models.DescribeHybridCloudClusterRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudClusterRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_content):
            query['RuleContent'] = request.rule_content
        if not DaraCore.is_null(request.rule_match_type):
            query['RuleMatchType'] = request.rule_match_type
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudClusterRules',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudClusterRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_cloud_cluster_rules_with_options_async(
        self,
        request: main_models.DescribeHybridCloudClusterRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudClusterRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_content):
            query['RuleContent'] = request.rule_content
        if not DaraCore.is_null(request.rule_match_type):
            query['RuleMatchType'] = request.rule_match_type
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudClusterRules',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudClusterRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_cloud_cluster_rules(
        self,
        request: main_models.DescribeHybridCloudClusterRulesRequest,
    ) -> main_models.DescribeHybridCloudClusterRulesResponse:
        runtime = RuntimeOptions()
        return self.describe_hybrid_cloud_cluster_rules_with_options(request, runtime)

    async def describe_hybrid_cloud_cluster_rules_async(
        self,
        request: main_models.DescribeHybridCloudClusterRulesRequest,
    ) -> main_models.DescribeHybridCloudClusterRulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_hybrid_cloud_cluster_rules_with_options_async(request, runtime)

    def describe_hybrid_cloud_cluster_servers_with_options(
        self,
        request: main_models.DescribeHybridCloudClusterServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudClusterServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudClusterServers',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudClusterServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_cloud_cluster_servers_with_options_async(
        self,
        request: main_models.DescribeHybridCloudClusterServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudClusterServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudClusterServers',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudClusterServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_cloud_cluster_servers(
        self,
        request: main_models.DescribeHybridCloudClusterServersRequest,
    ) -> main_models.DescribeHybridCloudClusterServersResponse:
        runtime = RuntimeOptions()
        return self.describe_hybrid_cloud_cluster_servers_with_options(request, runtime)

    async def describe_hybrid_cloud_cluster_servers_async(
        self,
        request: main_models.DescribeHybridCloudClusterServersRequest,
    ) -> main_models.DescribeHybridCloudClusterServersResponse:
        runtime = RuntimeOptions()
        return await self.describe_hybrid_cloud_cluster_servers_with_options_async(request, runtime)

    def describe_hybrid_cloud_clusters_with_options(
        self,
        request: main_models.DescribeHybridCloudClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudClusters',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_cloud_clusters_with_options_async(
        self,
        request: main_models.DescribeHybridCloudClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudClusters',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_cloud_clusters(
        self,
        request: main_models.DescribeHybridCloudClustersRequest,
    ) -> main_models.DescribeHybridCloudClustersResponse:
        runtime = RuntimeOptions()
        return self.describe_hybrid_cloud_clusters_with_options(request, runtime)

    async def describe_hybrid_cloud_clusters_async(
        self,
        request: main_models.DescribeHybridCloudClustersRequest,
    ) -> main_models.DescribeHybridCloudClustersResponse:
        runtime = RuntimeOptions()
        return await self.describe_hybrid_cloud_clusters_with_options_async(request, runtime)

    def describe_hybrid_cloud_groups_with_options(
        self,
        request: main_models.DescribeHybridCloudGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_proxy_type):
            query['ClusterProxyType'] = request.cluster_proxy_type
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudGroups',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_cloud_groups_with_options_async(
        self,
        request: main_models.DescribeHybridCloudGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_proxy_type):
            query['ClusterProxyType'] = request.cluster_proxy_type
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudGroups',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_cloud_groups(
        self,
        request: main_models.DescribeHybridCloudGroupsRequest,
    ) -> main_models.DescribeHybridCloudGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_hybrid_cloud_groups_with_options(request, runtime)

    async def describe_hybrid_cloud_groups_async(
        self,
        request: main_models.DescribeHybridCloudGroupsRequest,
    ) -> main_models.DescribeHybridCloudGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_hybrid_cloud_groups_with_options_async(request, runtime)

    def describe_hybrid_cloud_process_monitor_with_options(
        self,
        request: main_models.DescribeHybridCloudProcessMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudProcessMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mid):
            query['Mid'] = request.mid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudProcessMonitor',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudProcessMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_cloud_process_monitor_with_options_async(
        self,
        request: main_models.DescribeHybridCloudProcessMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudProcessMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mid):
            query['Mid'] = request.mid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudProcessMonitor',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudProcessMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_cloud_process_monitor(
        self,
        request: main_models.DescribeHybridCloudProcessMonitorRequest,
    ) -> main_models.DescribeHybridCloudProcessMonitorResponse:
        runtime = RuntimeOptions()
        return self.describe_hybrid_cloud_process_monitor_with_options(request, runtime)

    async def describe_hybrid_cloud_process_monitor_async(
        self,
        request: main_models.DescribeHybridCloudProcessMonitorRequest,
    ) -> main_models.DescribeHybridCloudProcessMonitorResponse:
        runtime = RuntimeOptions()
        return await self.describe_hybrid_cloud_process_monitor_with_options_async(request, runtime)

    def describe_hybrid_cloud_protectable_count_with_options(
        self,
        request: main_models.DescribeHybridCloudProtectableCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudProtectableCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudProtectableCount',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudProtectableCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_cloud_protectable_count_with_options_async(
        self,
        request: main_models.DescribeHybridCloudProtectableCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudProtectableCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudProtectableCount',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudProtectableCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_cloud_protectable_count(
        self,
        request: main_models.DescribeHybridCloudProtectableCountRequest,
    ) -> main_models.DescribeHybridCloudProtectableCountResponse:
        runtime = RuntimeOptions()
        return self.describe_hybrid_cloud_protectable_count_with_options(request, runtime)

    async def describe_hybrid_cloud_protectable_count_async(
        self,
        request: main_models.DescribeHybridCloudProtectableCountRequest,
    ) -> main_models.DescribeHybridCloudProtectableCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_hybrid_cloud_protectable_count_with_options_async(request, runtime)

    def describe_hybrid_cloud_resource_detail_with_options(
        self,
        request: main_models.DescribeHybridCloudResourceDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudResourceDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend):
            query['Backend'] = request.backend
        if not DaraCore.is_null(request.cname_enabled):
            query['CnameEnabled'] = request.cname_enabled
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudResourceDetail',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudResourceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_cloud_resource_detail_with_options_async(
        self,
        request: main_models.DescribeHybridCloudResourceDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudResourceDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend):
            query['Backend'] = request.backend
        if not DaraCore.is_null(request.cname_enabled):
            query['CnameEnabled'] = request.cname_enabled
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudResourceDetail',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudResourceDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_cloud_resource_detail(
        self,
        request: main_models.DescribeHybridCloudResourceDetailRequest,
    ) -> main_models.DescribeHybridCloudResourceDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_hybrid_cloud_resource_detail_with_options(request, runtime)

    async def describe_hybrid_cloud_resource_detail_async(
        self,
        request: main_models.DescribeHybridCloudResourceDetailRequest,
    ) -> main_models.DescribeHybridCloudResourceDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_hybrid_cloud_resource_detail_with_options_async(request, runtime)

    def describe_hybrid_cloud_resources_with_options(
        self,
        request: main_models.DescribeHybridCloudResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend):
            query['Backend'] = request.backend
        if not DaraCore.is_null(request.cname_enabled):
            query['CnameEnabled'] = request.cname_enabled
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudResources',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_cloud_resources_with_options_async(
        self,
        request: main_models.DescribeHybridCloudResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend):
            query['Backend'] = request.backend
        if not DaraCore.is_null(request.cname_enabled):
            query['CnameEnabled'] = request.cname_enabled
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudResources',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_cloud_resources(
        self,
        request: main_models.DescribeHybridCloudResourcesRequest,
    ) -> main_models.DescribeHybridCloudResourcesResponse:
        runtime = RuntimeOptions()
        return self.describe_hybrid_cloud_resources_with_options(request, runtime)

    async def describe_hybrid_cloud_resources_async(
        self,
        request: main_models.DescribeHybridCloudResourcesRequest,
    ) -> main_models.DescribeHybridCloudResourcesResponse:
        runtime = RuntimeOptions()
        return await self.describe_hybrid_cloud_resources_with_options_async(request, runtime)

    def describe_hybrid_cloud_sdk_servers_with_options(
        self,
        request: main_models.DescribeHybridCloudSdkServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudSdkServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudSdkServers',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudSdkServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_cloud_sdk_servers_with_options_async(
        self,
        request: main_models.DescribeHybridCloudSdkServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudSdkServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudSdkServers',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudSdkServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_cloud_sdk_servers(
        self,
        request: main_models.DescribeHybridCloudSdkServersRequest,
    ) -> main_models.DescribeHybridCloudSdkServersResponse:
        runtime = RuntimeOptions()
        return self.describe_hybrid_cloud_sdk_servers_with_options(request, runtime)

    async def describe_hybrid_cloud_sdk_servers_async(
        self,
        request: main_models.DescribeHybridCloudSdkServersRequest,
    ) -> main_models.DescribeHybridCloudSdkServersResponse:
        runtime = RuntimeOptions()
        return await self.describe_hybrid_cloud_sdk_servers_with_options_async(request, runtime)

    def describe_hybrid_cloud_server_regions_with_options(
        self,
        request: main_models.DescribeHybridCloudServerRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudServerRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_type):
            query['RegionType'] = request.region_type
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudServerRegions',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudServerRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_cloud_server_regions_with_options_async(
        self,
        request: main_models.DescribeHybridCloudServerRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudServerRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_type):
            query['RegionType'] = request.region_type
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudServerRegions',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudServerRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_cloud_server_regions(
        self,
        request: main_models.DescribeHybridCloudServerRegionsRequest,
    ) -> main_models.DescribeHybridCloudServerRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_hybrid_cloud_server_regions_with_options(request, runtime)

    async def describe_hybrid_cloud_server_regions_async(
        self,
        request: main_models.DescribeHybridCloudServerRegionsRequest,
    ) -> main_models.DescribeHybridCloudServerRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_hybrid_cloud_server_regions_with_options_async(request, runtime)

    def describe_hybrid_cloud_support_regions_with_options(
        self,
        request: main_models.DescribeHybridCloudSupportRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudSupportRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudSupportRegions',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudSupportRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_cloud_support_regions_with_options_async(
        self,
        request: main_models.DescribeHybridCloudSupportRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudSupportRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudSupportRegions',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudSupportRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_cloud_support_regions(
        self,
        request: main_models.DescribeHybridCloudSupportRegionsRequest,
    ) -> main_models.DescribeHybridCloudSupportRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_hybrid_cloud_support_regions_with_options(request, runtime)

    async def describe_hybrid_cloud_support_regions_async(
        self,
        request: main_models.DescribeHybridCloudSupportRegionsRequest,
    ) -> main_models.DescribeHybridCloudSupportRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_hybrid_cloud_support_regions_with_options_async(request, runtime)

    def describe_hybrid_cloud_unassigned_machines_with_options(
        self,
        request: main_models.DescribeHybridCloudUnassignedMachinesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudUnassignedMachinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudUnassignedMachines',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudUnassignedMachinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_cloud_unassigned_machines_with_options_async(
        self,
        request: main_models.DescribeHybridCloudUnassignedMachinesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudUnassignedMachinesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudUnassignedMachines',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudUnassignedMachinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_cloud_unassigned_machines(
        self,
        request: main_models.DescribeHybridCloudUnassignedMachinesRequest,
    ) -> main_models.DescribeHybridCloudUnassignedMachinesResponse:
        runtime = RuntimeOptions()
        return self.describe_hybrid_cloud_unassigned_machines_with_options(request, runtime)

    async def describe_hybrid_cloud_unassigned_machines_async(
        self,
        request: main_models.DescribeHybridCloudUnassignedMachinesRequest,
    ) -> main_models.DescribeHybridCloudUnassignedMachinesResponse:
        runtime = RuntimeOptions()
        return await self.describe_hybrid_cloud_unassigned_machines_with_options_async(request, runtime)

    def describe_hybrid_cloud_unsupport_ports_with_options(
        self,
        request: main_models.DescribeHybridCloudUnsupportPortsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudUnsupportPortsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudUnsupportPorts',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudUnsupportPortsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_cloud_unsupport_ports_with_options_async(
        self,
        request: main_models.DescribeHybridCloudUnsupportPortsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudUnsupportPortsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudUnsupportPorts',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudUnsupportPortsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_cloud_unsupport_ports(
        self,
        request: main_models.DescribeHybridCloudUnsupportPortsRequest,
    ) -> main_models.DescribeHybridCloudUnsupportPortsResponse:
        runtime = RuntimeOptions()
        return self.describe_hybrid_cloud_unsupport_ports_with_options(request, runtime)

    async def describe_hybrid_cloud_unsupport_ports_async(
        self,
        request: main_models.DescribeHybridCloudUnsupportPortsRequest,
    ) -> main_models.DescribeHybridCloudUnsupportPortsResponse:
        runtime = RuntimeOptions()
        return await self.describe_hybrid_cloud_unsupport_ports_with_options_async(request, runtime)

    def describe_hybrid_cloud_user_with_options(
        self,
        request: main_models.DescribeHybridCloudUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudUser',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_cloud_user_with_options_async(
        self,
        request: main_models.DescribeHybridCloudUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridCloudUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridCloudUser',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridCloudUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_cloud_user(
        self,
        request: main_models.DescribeHybridCloudUserRequest,
    ) -> main_models.DescribeHybridCloudUserResponse:
        runtime = RuntimeOptions()
        return self.describe_hybrid_cloud_user_with_options(request, runtime)

    async def describe_hybrid_cloud_user_async(
        self,
        request: main_models.DescribeHybridCloudUserRequest,
    ) -> main_models.DescribeHybridCloudUserResponse:
        runtime = RuntimeOptions()
        return await self.describe_hybrid_cloud_user_with_options_async(request, runtime)

    def describe_instance_with_options(
        self,
        request: main_models.DescribeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstance',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        request: main_models.DescribeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstance',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance(
        self,
        request: main_models.DescribeInstanceRequest,
    ) -> main_models.DescribeInstanceResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    async def describe_instance_async(
        self,
        request: main_models.DescribeInstanceRequest,
    ) -> main_models.DescribeInstanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_with_options_async(request, runtime)

    def describe_ip_abroad_country_infos_with_options(
        self,
        request: main_models.DescribeIpAbroadCountryInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIpAbroadCountryInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.abroad_region):
            query['AbroadRegion'] = request.abroad_region
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIpAbroadCountryInfos',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIpAbroadCountryInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ip_abroad_country_infos_with_options_async(
        self,
        request: main_models.DescribeIpAbroadCountryInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIpAbroadCountryInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.abroad_region):
            query['AbroadRegion'] = request.abroad_region
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIpAbroadCountryInfos',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIpAbroadCountryInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ip_abroad_country_infos(
        self,
        request: main_models.DescribeIpAbroadCountryInfosRequest,
    ) -> main_models.DescribeIpAbroadCountryInfosResponse:
        runtime = RuntimeOptions()
        return self.describe_ip_abroad_country_infos_with_options(request, runtime)

    async def describe_ip_abroad_country_infos_async(
        self,
        request: main_models.DescribeIpAbroadCountryInfosRequest,
    ) -> main_models.DescribeIpAbroadCountryInfosResponse:
        runtime = RuntimeOptions()
        return await self.describe_ip_abroad_country_infos_with_options_async(request, runtime)

    def describe_log_delivery_config_with_options(
        self,
        request: main_models.DescribeLogDeliveryConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogDeliveryConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_name):
            query['DeliveryName'] = request.delivery_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogDeliveryConfig',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogDeliveryConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_delivery_config_with_options_async(
        self,
        request: main_models.DescribeLogDeliveryConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogDeliveryConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_name):
            query['DeliveryName'] = request.delivery_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogDeliveryConfig',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogDeliveryConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_delivery_config(
        self,
        request: main_models.DescribeLogDeliveryConfigRequest,
    ) -> main_models.DescribeLogDeliveryConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_log_delivery_config_with_options(request, runtime)

    async def describe_log_delivery_config_async(
        self,
        request: main_models.DescribeLogDeliveryConfigRequest,
    ) -> main_models.DescribeLogDeliveryConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_log_delivery_config_with_options_async(request, runtime)

    def describe_log_delivery_configs_with_options(
        self,
        request: main_models.DescribeLogDeliveryConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogDeliveryConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_name_like):
            query['DeliveryNameLike'] = request.delivery_name_like
        if not DaraCore.is_null(request.delivery_type):
            query['DeliveryType'] = request.delivery_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogDeliveryConfigs',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogDeliveryConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_delivery_configs_with_options_async(
        self,
        request: main_models.DescribeLogDeliveryConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogDeliveryConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_name_like):
            query['DeliveryNameLike'] = request.delivery_name_like
        if not DaraCore.is_null(request.delivery_type):
            query['DeliveryType'] = request.delivery_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogDeliveryConfigs',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogDeliveryConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_delivery_configs(
        self,
        request: main_models.DescribeLogDeliveryConfigsRequest,
    ) -> main_models.DescribeLogDeliveryConfigsResponse:
        runtime = RuntimeOptions()
        return self.describe_log_delivery_configs_with_options(request, runtime)

    async def describe_log_delivery_configs_async(
        self,
        request: main_models.DescribeLogDeliveryConfigsRequest,
    ) -> main_models.DescribeLogDeliveryConfigsResponse:
        runtime = RuntimeOptions()
        return await self.describe_log_delivery_configs_with_options_async(request, runtime)

    def describe_major_protection_black_ips_with_options(
        self,
        request: main_models.DescribeMajorProtectionBlackIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMajorProtectionBlackIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip_like):
            query['IpLike'] = request.ip_like
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMajorProtectionBlackIps',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMajorProtectionBlackIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_major_protection_black_ips_with_options_async(
        self,
        request: main_models.DescribeMajorProtectionBlackIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMajorProtectionBlackIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip_like):
            query['IpLike'] = request.ip_like
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMajorProtectionBlackIps',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMajorProtectionBlackIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_major_protection_black_ips(
        self,
        request: main_models.DescribeMajorProtectionBlackIpsRequest,
    ) -> main_models.DescribeMajorProtectionBlackIpsResponse:
        runtime = RuntimeOptions()
        return self.describe_major_protection_black_ips_with_options(request, runtime)

    async def describe_major_protection_black_ips_async(
        self,
        request: main_models.DescribeMajorProtectionBlackIpsRequest,
    ) -> main_models.DescribeMajorProtectionBlackIpsResponse:
        runtime = RuntimeOptions()
        return await self.describe_major_protection_black_ips_with_options_async(request, runtime)

    def describe_member_accounts_with_options(
        self,
        request: main_models.DescribeMemberAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMemberAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_status):
            query['AccountStatus'] = request.account_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMemberAccounts',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMemberAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_member_accounts_with_options_async(
        self,
        request: main_models.DescribeMemberAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMemberAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_status):
            query['AccountStatus'] = request.account_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMemberAccounts',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMemberAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_member_accounts(
        self,
        request: main_models.DescribeMemberAccountsRequest,
    ) -> main_models.DescribeMemberAccountsResponse:
        runtime = RuntimeOptions()
        return self.describe_member_accounts_with_options(request, runtime)

    async def describe_member_accounts_async(
        self,
        request: main_models.DescribeMemberAccountsRequest,
    ) -> main_models.DescribeMemberAccountsResponse:
        runtime = RuntimeOptions()
        return await self.describe_member_accounts_with_options_async(request, runtime)

    def describe_network_flow_time_series_metric_with_options(
        self,
        tmp_req: main_models.DescribeNetworkFlowTimeSeriesMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNetworkFlowTimeSeriesMetricResponse:
        tmp_req.validate()
        request = main_models.DescribeNetworkFlowTimeSeriesMetricShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.metric):
            query['Metric'] = request.metric
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNetworkFlowTimeSeriesMetric',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNetworkFlowTimeSeriesMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_network_flow_time_series_metric_with_options_async(
        self,
        tmp_req: main_models.DescribeNetworkFlowTimeSeriesMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNetworkFlowTimeSeriesMetricResponse:
        tmp_req.validate()
        request = main_models.DescribeNetworkFlowTimeSeriesMetricShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.metric):
            query['Metric'] = request.metric
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNetworkFlowTimeSeriesMetric',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNetworkFlowTimeSeriesMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_network_flow_time_series_metric(
        self,
        request: main_models.DescribeNetworkFlowTimeSeriesMetricRequest,
    ) -> main_models.DescribeNetworkFlowTimeSeriesMetricResponse:
        runtime = RuntimeOptions()
        return self.describe_network_flow_time_series_metric_with_options(request, runtime)

    async def describe_network_flow_time_series_metric_async(
        self,
        request: main_models.DescribeNetworkFlowTimeSeriesMetricRequest,
    ) -> main_models.DescribeNetworkFlowTimeSeriesMetricResponse:
        runtime = RuntimeOptions()
        return await self.describe_network_flow_time_series_metric_with_options_async(request, runtime)

    def describe_network_flow_top_nmetric_with_options(
        self,
        tmp_req: main_models.DescribeNetworkFlowTopNMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNetworkFlowTopNMetricResponse:
        tmp_req.validate()
        request = main_models.DescribeNetworkFlowTopNMetricShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.metric):
            query['Metric'] = request.metric
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNetworkFlowTopNMetric',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNetworkFlowTopNMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_network_flow_top_nmetric_with_options_async(
        self,
        tmp_req: main_models.DescribeNetworkFlowTopNMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNetworkFlowTopNMetricResponse:
        tmp_req.validate()
        request = main_models.DescribeNetworkFlowTopNMetricShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.metric):
            query['Metric'] = request.metric
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNetworkFlowTopNMetric',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNetworkFlowTopNMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_network_flow_top_nmetric(
        self,
        request: main_models.DescribeNetworkFlowTopNMetricRequest,
    ) -> main_models.DescribeNetworkFlowTopNMetricResponse:
        runtime = RuntimeOptions()
        return self.describe_network_flow_top_nmetric_with_options(request, runtime)

    async def describe_network_flow_top_nmetric_async(
        self,
        request: main_models.DescribeNetworkFlowTopNMetricRequest,
    ) -> main_models.DescribeNetworkFlowTopNMetricResponse:
        runtime = RuntimeOptions()
        return await self.describe_network_flow_top_nmetric_with_options_async(request, runtime)

    def describe_pause_protection_status_with_options(
        self,
        request: main_models.DescribePauseProtectionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePauseProtectionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePauseProtectionStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePauseProtectionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pause_protection_status_with_options_async(
        self,
        request: main_models.DescribePauseProtectionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePauseProtectionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePauseProtectionStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePauseProtectionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pause_protection_status(
        self,
        request: main_models.DescribePauseProtectionStatusRequest,
    ) -> main_models.DescribePauseProtectionStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_pause_protection_status_with_options(request, runtime)

    async def describe_pause_protection_status_async(
        self,
        request: main_models.DescribePauseProtectionStatusRequest,
    ) -> main_models.DescribePauseProtectionStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_pause_protection_status_with_options_async(request, runtime)

    def describe_peak_trend_with_options(
        self,
        request: main_models.DescribePeakTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePeakTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePeakTrend',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePeakTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_peak_trend_with_options_async(
        self,
        request: main_models.DescribePeakTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePeakTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePeakTrend',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePeakTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_peak_trend(
        self,
        request: main_models.DescribePeakTrendRequest,
    ) -> main_models.DescribePeakTrendResponse:
        runtime = RuntimeOptions()
        return self.describe_peak_trend_with_options(request, runtime)

    async def describe_peak_trend_async(
        self,
        request: main_models.DescribePeakTrendRequest,
    ) -> main_models.DescribePeakTrendResponse:
        runtime = RuntimeOptions()
        return await self.describe_peak_trend_with_options_async(request, runtime)

    def describe_poc_functions_with_options(
        self,
        request: main_models.DescribePocFunctionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePocFunctionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePocFunctions',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePocFunctionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_poc_functions_with_options_async(
        self,
        request: main_models.DescribePocFunctionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePocFunctionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePocFunctions',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePocFunctionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_poc_functions(
        self,
        request: main_models.DescribePocFunctionsRequest,
    ) -> main_models.DescribePocFunctionsResponse:
        runtime = RuntimeOptions()
        return self.describe_poc_functions_with_options(request, runtime)

    async def describe_poc_functions_async(
        self,
        request: main_models.DescribePocFunctionsRequest,
    ) -> main_models.DescribePocFunctionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_poc_functions_with_options_async(request, runtime)

    def describe_product_instances_with_options(
        self,
        request: main_models.DescribeProductInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProductInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_instance_access_status):
            query['ResourceInstanceAccessStatus'] = request.resource_instance_access_status
        if not DaraCore.is_null(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not DaraCore.is_null(request.resource_instance_ip):
            query['ResourceInstanceIp'] = request.resource_instance_ip
        if not DaraCore.is_null(request.resource_instance_name):
            query['ResourceInstanceName'] = request.resource_instance_name
        if not DaraCore.is_null(request.resource_ip):
            query['ResourceIp'] = request.resource_ip
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_product):
            query['ResourceProduct'] = request.resource_product
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProductInstances',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProductInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_product_instances_with_options_async(
        self,
        request: main_models.DescribeProductInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProductInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_instance_access_status):
            query['ResourceInstanceAccessStatus'] = request.resource_instance_access_status
        if not DaraCore.is_null(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not DaraCore.is_null(request.resource_instance_ip):
            query['ResourceInstanceIp'] = request.resource_instance_ip
        if not DaraCore.is_null(request.resource_instance_name):
            query['ResourceInstanceName'] = request.resource_instance_name
        if not DaraCore.is_null(request.resource_ip):
            query['ResourceIp'] = request.resource_ip
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_product):
            query['ResourceProduct'] = request.resource_product
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProductInstances',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProductInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_product_instances(
        self,
        request: main_models.DescribeProductInstancesRequest,
    ) -> main_models.DescribeProductInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_product_instances_with_options(request, runtime)

    async def describe_product_instances_async(
        self,
        request: main_models.DescribeProductInstancesRequest,
    ) -> main_models.DescribeProductInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_product_instances_with_options_async(request, runtime)

    def describe_punished_domains_with_options(
        self,
        request: main_models.DescribePunishedDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePunishedDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domains):
            query['Domains'] = request.domains
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.punish_type):
            query['PunishType'] = request.punish_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePunishedDomains',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePunishedDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_punished_domains_with_options_async(
        self,
        request: main_models.DescribePunishedDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePunishedDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domains):
            query['Domains'] = request.domains
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.punish_type):
            query['PunishType'] = request.punish_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePunishedDomains',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePunishedDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_punished_domains(
        self,
        request: main_models.DescribePunishedDomainsRequest,
    ) -> main_models.DescribePunishedDomainsResponse:
        runtime = RuntimeOptions()
        return self.describe_punished_domains_with_options(request, runtime)

    async def describe_punished_domains_async(
        self,
        request: main_models.DescribePunishedDomainsRequest,
    ) -> main_models.DescribePunishedDomainsResponse:
        runtime = RuntimeOptions()
        return await self.describe_punished_domains_with_options_async(request, runtime)

    def describe_related_defense_rules_with_options(
        self,
        request: main_models.DescribeRelatedDefenseRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRelatedDefenseRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not DaraCore.is_null(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRelatedDefenseRules',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRelatedDefenseRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_related_defense_rules_with_options_async(
        self,
        request: main_models.DescribeRelatedDefenseRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRelatedDefenseRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not DaraCore.is_null(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRelatedDefenseRules',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRelatedDefenseRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_related_defense_rules(
        self,
        request: main_models.DescribeRelatedDefenseRulesRequest,
    ) -> main_models.DescribeRelatedDefenseRulesResponse:
        runtime = RuntimeOptions()
        return self.describe_related_defense_rules_with_options(request, runtime)

    async def describe_related_defense_rules_async(
        self,
        request: main_models.DescribeRelatedDefenseRulesRequest,
    ) -> main_models.DescribeRelatedDefenseRulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_related_defense_rules_with_options_async(request, runtime)

    def describe_resource_instance_certs_with_options(
        self,
        request: main_models.DescribeResourceInstanceCertsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceInstanceCertsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceInstanceCerts',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceInstanceCertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_instance_certs_with_options_async(
        self,
        request: main_models.DescribeResourceInstanceCertsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceInstanceCertsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceInstanceCerts',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceInstanceCertsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_instance_certs(
        self,
        request: main_models.DescribeResourceInstanceCertsRequest,
    ) -> main_models.DescribeResourceInstanceCertsResponse:
        runtime = RuntimeOptions()
        return self.describe_resource_instance_certs_with_options(request, runtime)

    async def describe_resource_instance_certs_async(
        self,
        request: main_models.DescribeResourceInstanceCertsRequest,
    ) -> main_models.DescribeResourceInstanceCertsResponse:
        runtime = RuntimeOptions()
        return await self.describe_resource_instance_certs_with_options_async(request, runtime)

    def describe_resource_log_delivery_status_with_options(
        self,
        request: main_models.DescribeResourceLogDeliveryStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceLogDeliveryStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceLogDeliveryStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceLogDeliveryStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_log_delivery_status_with_options_async(
        self,
        request: main_models.DescribeResourceLogDeliveryStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceLogDeliveryStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceLogDeliveryStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceLogDeliveryStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_log_delivery_status(
        self,
        request: main_models.DescribeResourceLogDeliveryStatusRequest,
    ) -> main_models.DescribeResourceLogDeliveryStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_resource_log_delivery_status_with_options(request, runtime)

    async def describe_resource_log_delivery_status_async(
        self,
        request: main_models.DescribeResourceLogDeliveryStatusRequest,
    ) -> main_models.DescribeResourceLogDeliveryStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_resource_log_delivery_status_with_options_async(request, runtime)

    def describe_resource_log_field_config_with_options(
        self,
        request: main_models.DescribeResourceLogFieldConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceLogFieldConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_type):
            query['DeliveryType'] = request.delivery_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceLogFieldConfig',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceLogFieldConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_log_field_config_with_options_async(
        self,
        request: main_models.DescribeResourceLogFieldConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceLogFieldConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_type):
            query['DeliveryType'] = request.delivery_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceLogFieldConfig',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceLogFieldConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_log_field_config(
        self,
        request: main_models.DescribeResourceLogFieldConfigRequest,
    ) -> main_models.DescribeResourceLogFieldConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_resource_log_field_config_with_options(request, runtime)

    async def describe_resource_log_field_config_async(
        self,
        request: main_models.DescribeResourceLogFieldConfigRequest,
    ) -> main_models.DescribeResourceLogFieldConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_resource_log_field_config_with_options_async(request, runtime)

    def describe_resource_log_status_with_options(
        self,
        request: main_models.DescribeResourceLogStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceLogStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceLogStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceLogStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_log_status_with_options_async(
        self,
        request: main_models.DescribeResourceLogStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceLogStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceLogStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceLogStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_log_status(
        self,
        request: main_models.DescribeResourceLogStatusRequest,
    ) -> main_models.DescribeResourceLogStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_resource_log_status_with_options(request, runtime)

    async def describe_resource_log_status_async(
        self,
        request: main_models.DescribeResourceLogStatusRequest,
    ) -> main_models.DescribeResourceLogStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_resource_log_status_with_options_async(request, runtime)

    def describe_resource_port_with_options(
        self,
        request: main_models.DescribeResourcePortRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourcePortResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourcePort',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourcePortResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_port_with_options_async(
        self,
        request: main_models.DescribeResourcePortRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourcePortResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourcePort',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourcePortResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_port(
        self,
        request: main_models.DescribeResourcePortRequest,
    ) -> main_models.DescribeResourcePortResponse:
        runtime = RuntimeOptions()
        return self.describe_resource_port_with_options(request, runtime)

    async def describe_resource_port_async(
        self,
        request: main_models.DescribeResourcePortRequest,
    ) -> main_models.DescribeResourcePortResponse:
        runtime = RuntimeOptions()
        return await self.describe_resource_port_with_options_async(request, runtime)

    def describe_resource_region_id_with_options(
        self,
        request: main_models.DescribeResourceRegionIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceRegionIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceRegionId',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceRegionIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_region_id_with_options_async(
        self,
        request: main_models.DescribeResourceRegionIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceRegionIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceRegionId',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceRegionIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_region_id(
        self,
        request: main_models.DescribeResourceRegionIdRequest,
    ) -> main_models.DescribeResourceRegionIdResponse:
        runtime = RuntimeOptions()
        return self.describe_resource_region_id_with_options(request, runtime)

    async def describe_resource_region_id_async(
        self,
        request: main_models.DescribeResourceRegionIdRequest,
    ) -> main_models.DescribeResourceRegionIdResponse:
        runtime = RuntimeOptions()
        return await self.describe_resource_region_id_with_options_async(request, runtime)

    def describe_resource_support_regions_with_options(
        self,
        request: main_models.DescribeResourceSupportRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceSupportRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_product):
            query['ResourceProduct'] = request.resource_product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceSupportRegions',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceSupportRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_support_regions_with_options_async(
        self,
        request: main_models.DescribeResourceSupportRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceSupportRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_product):
            query['ResourceProduct'] = request.resource_product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceSupportRegions',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceSupportRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_support_regions(
        self,
        request: main_models.DescribeResourceSupportRegionsRequest,
    ) -> main_models.DescribeResourceSupportRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_resource_support_regions_with_options(request, runtime)

    async def describe_resource_support_regions_async(
        self,
        request: main_models.DescribeResourceSupportRegionsRequest,
    ) -> main_models.DescribeResourceSupportRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_resource_support_regions_with_options_async(request, runtime)

    def describe_response_code_trend_graph_with_options(
        self,
        request: main_models.DescribeResponseCodeTrendGraphRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResponseCodeTrendGraphResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResponseCodeTrendGraph',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResponseCodeTrendGraphResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_response_code_trend_graph_with_options_async(
        self,
        request: main_models.DescribeResponseCodeTrendGraphRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResponseCodeTrendGraphResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResponseCodeTrendGraph',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResponseCodeTrendGraphResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_response_code_trend_graph(
        self,
        request: main_models.DescribeResponseCodeTrendGraphRequest,
    ) -> main_models.DescribeResponseCodeTrendGraphResponse:
        runtime = RuntimeOptions()
        return self.describe_response_code_trend_graph_with_options(request, runtime)

    async def describe_response_code_trend_graph_async(
        self,
        request: main_models.DescribeResponseCodeTrendGraphRequest,
    ) -> main_models.DescribeResponseCodeTrendGraphResponse:
        runtime = RuntimeOptions()
        return await self.describe_response_code_trend_graph_with_options_async(request, runtime)

    def describe_role_auth_status_with_options(
        self,
        request: main_models.DescribeRoleAuthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRoleAuthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRoleAuthStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRoleAuthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_role_auth_status_with_options_async(
        self,
        request: main_models.DescribeRoleAuthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRoleAuthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRoleAuthStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRoleAuthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_role_auth_status(
        self,
        request: main_models.DescribeRoleAuthStatusRequest,
    ) -> main_models.DescribeRoleAuthStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_role_auth_status_with_options(request, runtime)

    async def describe_role_auth_status_async(
        self,
        request: main_models.DescribeRoleAuthStatusRequest,
    ) -> main_models.DescribeRoleAuthStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_role_auth_status_with_options_async(request, runtime)

    def describe_rule_groups_with_options(
        self,
        request: main_models.DescribeRuleGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.search_type):
            query['SearchType'] = request.search_type
        if not DaraCore.is_null(request.search_value):
            query['SearchValue'] = request.search_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleGroups',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_groups_with_options_async(
        self,
        request: main_models.DescribeRuleGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.search_type):
            query['SearchType'] = request.search_type
        if not DaraCore.is_null(request.search_value):
            query['SearchValue'] = request.search_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleGroups',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_groups(
        self,
        request: main_models.DescribeRuleGroupsRequest,
    ) -> main_models.DescribeRuleGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_rule_groups_with_options(request, runtime)

    async def describe_rule_groups_async(
        self,
        request: main_models.DescribeRuleGroupsRequest,
    ) -> main_models.DescribeRuleGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_rule_groups_with_options_async(request, runtime)

    def describe_rule_hits_top_client_ip_with_options(
        self,
        request: main_models.DescribeRuleHitsTopClientIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleHitsTopClientIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleHitsTopClientIp',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleHitsTopClientIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_hits_top_client_ip_with_options_async(
        self,
        request: main_models.DescribeRuleHitsTopClientIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleHitsTopClientIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleHitsTopClientIp',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleHitsTopClientIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_hits_top_client_ip(
        self,
        request: main_models.DescribeRuleHitsTopClientIpRequest,
    ) -> main_models.DescribeRuleHitsTopClientIpResponse:
        runtime = RuntimeOptions()
        return self.describe_rule_hits_top_client_ip_with_options(request, runtime)

    async def describe_rule_hits_top_client_ip_async(
        self,
        request: main_models.DescribeRuleHitsTopClientIpRequest,
    ) -> main_models.DescribeRuleHitsTopClientIpResponse:
        runtime = RuntimeOptions()
        return await self.describe_rule_hits_top_client_ip_with_options_async(request, runtime)

    def describe_rule_hits_top_resource_with_options(
        self,
        request: main_models.DescribeRuleHitsTopResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleHitsTopResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleHitsTopResource',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleHitsTopResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_hits_top_resource_with_options_async(
        self,
        request: main_models.DescribeRuleHitsTopResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleHitsTopResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleHitsTopResource',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleHitsTopResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_hits_top_resource(
        self,
        request: main_models.DescribeRuleHitsTopResourceRequest,
    ) -> main_models.DescribeRuleHitsTopResourceResponse:
        runtime = RuntimeOptions()
        return self.describe_rule_hits_top_resource_with_options(request, runtime)

    async def describe_rule_hits_top_resource_async(
        self,
        request: main_models.DescribeRuleHitsTopResourceRequest,
    ) -> main_models.DescribeRuleHitsTopResourceResponse:
        runtime = RuntimeOptions()
        return await self.describe_rule_hits_top_resource_with_options_async(request, runtime)

    def describe_rule_hits_top_rule_id_with_options(
        self,
        request: main_models.DescribeRuleHitsTopRuleIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleHitsTopRuleIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_group_resource):
            query['IsGroupResource'] = request.is_group_resource
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleHitsTopRuleId',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleHitsTopRuleIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_hits_top_rule_id_with_options_async(
        self,
        request: main_models.DescribeRuleHitsTopRuleIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleHitsTopRuleIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_group_resource):
            query['IsGroupResource'] = request.is_group_resource
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleHitsTopRuleId',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleHitsTopRuleIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_hits_top_rule_id(
        self,
        request: main_models.DescribeRuleHitsTopRuleIdRequest,
    ) -> main_models.DescribeRuleHitsTopRuleIdResponse:
        runtime = RuntimeOptions()
        return self.describe_rule_hits_top_rule_id_with_options(request, runtime)

    async def describe_rule_hits_top_rule_id_async(
        self,
        request: main_models.DescribeRuleHitsTopRuleIdRequest,
    ) -> main_models.DescribeRuleHitsTopRuleIdResponse:
        runtime = RuntimeOptions()
        return await self.describe_rule_hits_top_rule_id_with_options_async(request, runtime)

    def describe_rule_hits_top_tule_type_with_options(
        self,
        request: main_models.DescribeRuleHitsTopTuleTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleHitsTopTuleTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleHitsTopTuleType',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleHitsTopTuleTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_hits_top_tule_type_with_options_async(
        self,
        request: main_models.DescribeRuleHitsTopTuleTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleHitsTopTuleTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleHitsTopTuleType',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleHitsTopTuleTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_hits_top_tule_type(
        self,
        request: main_models.DescribeRuleHitsTopTuleTypeRequest,
    ) -> main_models.DescribeRuleHitsTopTuleTypeResponse:
        runtime = RuntimeOptions()
        return self.describe_rule_hits_top_tule_type_with_options(request, runtime)

    async def describe_rule_hits_top_tule_type_async(
        self,
        request: main_models.DescribeRuleHitsTopTuleTypeRequest,
    ) -> main_models.DescribeRuleHitsTopTuleTypeResponse:
        runtime = RuntimeOptions()
        return await self.describe_rule_hits_top_tule_type_with_options_async(request, runtime)

    def describe_rule_hits_top_ua_with_options(
        self,
        request: main_models.DescribeRuleHitsTopUaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleHitsTopUaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleHitsTopUa',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleHitsTopUaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_hits_top_ua_with_options_async(
        self,
        request: main_models.DescribeRuleHitsTopUaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleHitsTopUaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleHitsTopUa',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleHitsTopUaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_hits_top_ua(
        self,
        request: main_models.DescribeRuleHitsTopUaRequest,
    ) -> main_models.DescribeRuleHitsTopUaResponse:
        runtime = RuntimeOptions()
        return self.describe_rule_hits_top_ua_with_options(request, runtime)

    async def describe_rule_hits_top_ua_async(
        self,
        request: main_models.DescribeRuleHitsTopUaRequest,
    ) -> main_models.DescribeRuleHitsTopUaResponse:
        runtime = RuntimeOptions()
        return await self.describe_rule_hits_top_ua_with_options_async(request, runtime)

    def describe_rule_hits_top_url_with_options(
        self,
        request: main_models.DescribeRuleHitsTopUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleHitsTopUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleHitsTopUrl',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleHitsTopUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_hits_top_url_with_options_async(
        self,
        request: main_models.DescribeRuleHitsTopUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRuleHitsTopUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRuleHitsTopUrl',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRuleHitsTopUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_hits_top_url(
        self,
        request: main_models.DescribeRuleHitsTopUrlRequest,
    ) -> main_models.DescribeRuleHitsTopUrlResponse:
        runtime = RuntimeOptions()
        return self.describe_rule_hits_top_url_with_options(request, runtime)

    async def describe_rule_hits_top_url_async(
        self,
        request: main_models.DescribeRuleHitsTopUrlRequest,
    ) -> main_models.DescribeRuleHitsTopUrlResponse:
        runtime = RuntimeOptions()
        return await self.describe_rule_hits_top_url_with_options_async(request, runtime)

    def describe_security_event_logs_with_options(
        self,
        tmp_req: main_models.DescribeSecurityEventLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityEventLogsResponse:
        tmp_req.validate()
        request = main_models.DescribeSecurityEventLogsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityEventLogs',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityEventLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_event_logs_with_options_async(
        self,
        tmp_req: main_models.DescribeSecurityEventLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityEventLogsResponse:
        tmp_req.validate()
        request = main_models.DescribeSecurityEventLogsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityEventLogs',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityEventLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_event_logs(
        self,
        request: main_models.DescribeSecurityEventLogsRequest,
    ) -> main_models.DescribeSecurityEventLogsResponse:
        runtime = RuntimeOptions()
        return self.describe_security_event_logs_with_options(request, runtime)

    async def describe_security_event_logs_async(
        self,
        request: main_models.DescribeSecurityEventLogsRequest,
    ) -> main_models.DescribeSecurityEventLogsResponse:
        runtime = RuntimeOptions()
        return await self.describe_security_event_logs_with_options_async(request, runtime)

    def describe_security_event_time_series_metric_with_options(
        self,
        tmp_req: main_models.DescribeSecurityEventTimeSeriesMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityEventTimeSeriesMetricResponse:
        tmp_req.validate()
        request = main_models.DescribeSecurityEventTimeSeriesMetricShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.metric):
            query['Metric'] = request.metric
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityEventTimeSeriesMetric',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityEventTimeSeriesMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_event_time_series_metric_with_options_async(
        self,
        tmp_req: main_models.DescribeSecurityEventTimeSeriesMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityEventTimeSeriesMetricResponse:
        tmp_req.validate()
        request = main_models.DescribeSecurityEventTimeSeriesMetricShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.metric):
            query['Metric'] = request.metric
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityEventTimeSeriesMetric',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityEventTimeSeriesMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_event_time_series_metric(
        self,
        request: main_models.DescribeSecurityEventTimeSeriesMetricRequest,
    ) -> main_models.DescribeSecurityEventTimeSeriesMetricResponse:
        runtime = RuntimeOptions()
        return self.describe_security_event_time_series_metric_with_options(request, runtime)

    async def describe_security_event_time_series_metric_async(
        self,
        request: main_models.DescribeSecurityEventTimeSeriesMetricRequest,
    ) -> main_models.DescribeSecurityEventTimeSeriesMetricResponse:
        runtime = RuntimeOptions()
        return await self.describe_security_event_time_series_metric_with_options_async(request, runtime)

    def describe_security_event_top_nmetric_with_options(
        self,
        tmp_req: main_models.DescribeSecurityEventTopNMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityEventTopNMetricResponse:
        tmp_req.validate()
        request = main_models.DescribeSecurityEventTopNMetricShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.metric):
            query['Metric'] = request.metric
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityEventTopNMetric',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityEventTopNMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_event_top_nmetric_with_options_async(
        self,
        tmp_req: main_models.DescribeSecurityEventTopNMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityEventTopNMetricResponse:
        tmp_req.validate()
        request = main_models.DescribeSecurityEventTopNMetricShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.metric):
            query['Metric'] = request.metric
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityEventTopNMetric',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityEventTopNMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_event_top_nmetric(
        self,
        request: main_models.DescribeSecurityEventTopNMetricRequest,
    ) -> main_models.DescribeSecurityEventTopNMetricResponse:
        runtime = RuntimeOptions()
        return self.describe_security_event_top_nmetric_with_options(request, runtime)

    async def describe_security_event_top_nmetric_async(
        self,
        request: main_models.DescribeSecurityEventTopNMetricRequest,
    ) -> main_models.DescribeSecurityEventTopNMetricResponse:
        runtime = RuntimeOptions()
        return await self.describe_security_event_top_nmetric_with_options_async(request, runtime)

    def describe_sensitive_api_statistic_with_options(
        self,
        request: main_models.DescribeSensitiveApiStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSensitiveApiStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.matched_host):
            query['MatchedHost'] = request.matched_host
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSensitiveApiStatistic',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSensitiveApiStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sensitive_api_statistic_with_options_async(
        self,
        request: main_models.DescribeSensitiveApiStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSensitiveApiStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.matched_host):
            query['MatchedHost'] = request.matched_host
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSensitiveApiStatistic',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSensitiveApiStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sensitive_api_statistic(
        self,
        request: main_models.DescribeSensitiveApiStatisticRequest,
    ) -> main_models.DescribeSensitiveApiStatisticResponse:
        runtime = RuntimeOptions()
        return self.describe_sensitive_api_statistic_with_options(request, runtime)

    async def describe_sensitive_api_statistic_async(
        self,
        request: main_models.DescribeSensitiveApiStatisticRequest,
    ) -> main_models.DescribeSensitiveApiStatisticResponse:
        runtime = RuntimeOptions()
        return await self.describe_sensitive_api_statistic_with_options_async(request, runtime)

    def describe_sensitive_detection_result_with_options(
        self,
        request: main_models.DescribeSensitiveDetectionResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSensitiveDetectionResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSensitiveDetectionResult',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSensitiveDetectionResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sensitive_detection_result_with_options_async(
        self,
        request: main_models.DescribeSensitiveDetectionResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSensitiveDetectionResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSensitiveDetectionResult',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSensitiveDetectionResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sensitive_detection_result(
        self,
        request: main_models.DescribeSensitiveDetectionResultRequest,
    ) -> main_models.DescribeSensitiveDetectionResultResponse:
        runtime = RuntimeOptions()
        return self.describe_sensitive_detection_result_with_options(request, runtime)

    async def describe_sensitive_detection_result_async(
        self,
        request: main_models.DescribeSensitiveDetectionResultRequest,
    ) -> main_models.DescribeSensitiveDetectionResultResponse:
        runtime = RuntimeOptions()
        return await self.describe_sensitive_detection_result_with_options_async(request, runtime)

    def describe_sensitive_outbound_distribution_with_options(
        self,
        request: main_models.DescribeSensitiveOutboundDistributionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSensitiveOutboundDistributionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSensitiveOutboundDistribution',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSensitiveOutboundDistributionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sensitive_outbound_distribution_with_options_async(
        self,
        request: main_models.DescribeSensitiveOutboundDistributionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSensitiveOutboundDistributionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSensitiveOutboundDistribution',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSensitiveOutboundDistributionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sensitive_outbound_distribution(
        self,
        request: main_models.DescribeSensitiveOutboundDistributionRequest,
    ) -> main_models.DescribeSensitiveOutboundDistributionResponse:
        runtime = RuntimeOptions()
        return self.describe_sensitive_outbound_distribution_with_options(request, runtime)

    async def describe_sensitive_outbound_distribution_async(
        self,
        request: main_models.DescribeSensitiveOutboundDistributionRequest,
    ) -> main_models.DescribeSensitiveOutboundDistributionResponse:
        runtime = RuntimeOptions()
        return await self.describe_sensitive_outbound_distribution_with_options_async(request, runtime)

    def describe_sensitive_outbound_statistic_with_options(
        self,
        request: main_models.DescribeSensitiveOutboundStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSensitiveOutboundStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.detection_result):
            query['DetectionResult'] = request.detection_result
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_key):
            query['OrderKey'] = request.order_key
        if not DaraCore.is_null(request.order_way):
            query['OrderWay'] = request.order_way
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.sensitive_code):
            query['SensitiveCode'] = request.sensitive_code
        if not DaraCore.is_null(request.sensitive_level):
            query['SensitiveLevel'] = request.sensitive_level
        if not DaraCore.is_null(request.sensitive_type):
            query['SensitiveType'] = request.sensitive_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSensitiveOutboundStatistic',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSensitiveOutboundStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sensitive_outbound_statistic_with_options_async(
        self,
        request: main_models.DescribeSensitiveOutboundStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSensitiveOutboundStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.detection_result):
            query['DetectionResult'] = request.detection_result
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_key):
            query['OrderKey'] = request.order_key
        if not DaraCore.is_null(request.order_way):
            query['OrderWay'] = request.order_way
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.sensitive_code):
            query['SensitiveCode'] = request.sensitive_code
        if not DaraCore.is_null(request.sensitive_level):
            query['SensitiveLevel'] = request.sensitive_level
        if not DaraCore.is_null(request.sensitive_type):
            query['SensitiveType'] = request.sensitive_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSensitiveOutboundStatistic',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSensitiveOutboundStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sensitive_outbound_statistic(
        self,
        request: main_models.DescribeSensitiveOutboundStatisticRequest,
    ) -> main_models.DescribeSensitiveOutboundStatisticResponse:
        runtime = RuntimeOptions()
        return self.describe_sensitive_outbound_statistic_with_options(request, runtime)

    async def describe_sensitive_outbound_statistic_async(
        self,
        request: main_models.DescribeSensitiveOutboundStatisticRequest,
    ) -> main_models.DescribeSensitiveOutboundStatisticResponse:
        runtime = RuntimeOptions()
        return await self.describe_sensitive_outbound_statistic_with_options_async(request, runtime)

    def describe_sensitive_outbound_trend_with_options(
        self,
        request: main_models.DescribeSensitiveOutboundTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSensitiveOutboundTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSensitiveOutboundTrend',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSensitiveOutboundTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sensitive_outbound_trend_with_options_async(
        self,
        request: main_models.DescribeSensitiveOutboundTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSensitiveOutboundTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSensitiveOutboundTrend',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSensitiveOutboundTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sensitive_outbound_trend(
        self,
        request: main_models.DescribeSensitiveOutboundTrendRequest,
    ) -> main_models.DescribeSensitiveOutboundTrendResponse:
        runtime = RuntimeOptions()
        return self.describe_sensitive_outbound_trend_with_options(request, runtime)

    async def describe_sensitive_outbound_trend_async(
        self,
        request: main_models.DescribeSensitiveOutboundTrendRequest,
    ) -> main_models.DescribeSensitiveOutboundTrendResponse:
        runtime = RuntimeOptions()
        return await self.describe_sensitive_outbound_trend_with_options_async(request, runtime)

    def describe_sensitive_request_log_with_options(
        self,
        request: main_models.DescribeSensitiveRequestLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSensitiveRequestLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.api_format):
            query['ApiFormat'] = request.api_format
        if not DaraCore.is_null(request.client_ip):
            query['ClientIP'] = request.client_ip
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.matched_host):
            query['MatchedHost'] = request.matched_host
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.sensitive_code):
            query['SensitiveCode'] = request.sensitive_code
        if not DaraCore.is_null(request.sensitive_data):
            query['SensitiveData'] = request.sensitive_data
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSensitiveRequestLog',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSensitiveRequestLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sensitive_request_log_with_options_async(
        self,
        request: main_models.DescribeSensitiveRequestLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSensitiveRequestLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.api_format):
            query['ApiFormat'] = request.api_format
        if not DaraCore.is_null(request.client_ip):
            query['ClientIP'] = request.client_ip
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.matched_host):
            query['MatchedHost'] = request.matched_host
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.sensitive_code):
            query['SensitiveCode'] = request.sensitive_code
        if not DaraCore.is_null(request.sensitive_data):
            query['SensitiveData'] = request.sensitive_data
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSensitiveRequestLog',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSensitiveRequestLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sensitive_request_log(
        self,
        request: main_models.DescribeSensitiveRequestLogRequest,
    ) -> main_models.DescribeSensitiveRequestLogResponse:
        runtime = RuntimeOptions()
        return self.describe_sensitive_request_log_with_options(request, runtime)

    async def describe_sensitive_request_log_async(
        self,
        request: main_models.DescribeSensitiveRequestLogRequest,
    ) -> main_models.DescribeSensitiveRequestLogResponse:
        runtime = RuntimeOptions()
        return await self.describe_sensitive_request_log_with_options_async(request, runtime)

    def describe_sensitive_requests_with_options(
        self,
        request: main_models.DescribeSensitiveRequestsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSensitiveRequestsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.sensitive_code):
            query['SensitiveCode'] = request.sensitive_code
        if not DaraCore.is_null(request.sensitive_data):
            query['SensitiveData'] = request.sensitive_data
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSensitiveRequests',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSensitiveRequestsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sensitive_requests_with_options_async(
        self,
        request: main_models.DescribeSensitiveRequestsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSensitiveRequestsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.sensitive_code):
            query['SensitiveCode'] = request.sensitive_code
        if not DaraCore.is_null(request.sensitive_data):
            query['SensitiveData'] = request.sensitive_data
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSensitiveRequests',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSensitiveRequestsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sensitive_requests(
        self,
        request: main_models.DescribeSensitiveRequestsRequest,
    ) -> main_models.DescribeSensitiveRequestsResponse:
        runtime = RuntimeOptions()
        return self.describe_sensitive_requests_with_options(request, runtime)

    async def describe_sensitive_requests_async(
        self,
        request: main_models.DescribeSensitiveRequestsRequest,
    ) -> main_models.DescribeSensitiveRequestsResponse:
        runtime = RuntimeOptions()
        return await self.describe_sensitive_requests_with_options_async(request, runtime)

    def describe_sensitive_statistic_with_options(
        self,
        request: main_models.DescribeSensitiveStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSensitiveStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.statistic_type):
            query['StatisticType'] = request.statistic_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSensitiveStatistic',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSensitiveStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sensitive_statistic_with_options_async(
        self,
        request: main_models.DescribeSensitiveStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSensitiveStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.statistic_type):
            query['StatisticType'] = request.statistic_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSensitiveStatistic',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSensitiveStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sensitive_statistic(
        self,
        request: main_models.DescribeSensitiveStatisticRequest,
    ) -> main_models.DescribeSensitiveStatisticResponse:
        runtime = RuntimeOptions()
        return self.describe_sensitive_statistic_with_options(request, runtime)

    async def describe_sensitive_statistic_async(
        self,
        request: main_models.DescribeSensitiveStatisticRequest,
    ) -> main_models.DescribeSensitiveStatisticResponse:
        runtime = RuntimeOptions()
        return await self.describe_sensitive_statistic_with_options_async(request, runtime)

    def describe_sls_auth_status_with_options(
        self,
        request: main_models.DescribeSlsAuthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlsAuthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlsAuthStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlsAuthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sls_auth_status_with_options_async(
        self,
        request: main_models.DescribeSlsAuthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlsAuthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlsAuthStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlsAuthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sls_auth_status(
        self,
        request: main_models.DescribeSlsAuthStatusRequest,
    ) -> main_models.DescribeSlsAuthStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_sls_auth_status_with_options(request, runtime)

    async def describe_sls_auth_status_async(
        self,
        request: main_models.DescribeSlsAuthStatusRequest,
    ) -> main_models.DescribeSlsAuthStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_sls_auth_status_with_options_async(request, runtime)

    def describe_sls_log_store_with_options(
        self,
        request: main_models.DescribeSlsLogStoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlsLogStoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlsLogStore',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlsLogStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sls_log_store_with_options_async(
        self,
        request: main_models.DescribeSlsLogStoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlsLogStoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlsLogStore',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlsLogStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sls_log_store(
        self,
        request: main_models.DescribeSlsLogStoreRequest,
    ) -> main_models.DescribeSlsLogStoreResponse:
        runtime = RuntimeOptions()
        return self.describe_sls_log_store_with_options(request, runtime)

    async def describe_sls_log_store_async(
        self,
        request: main_models.DescribeSlsLogStoreRequest,
    ) -> main_models.DescribeSlsLogStoreResponse:
        runtime = RuntimeOptions()
        return await self.describe_sls_log_store_with_options_async(request, runtime)

    def describe_sls_log_store_status_with_options(
        self,
        request: main_models.DescribeSlsLogStoreStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlsLogStoreStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlsLogStoreStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlsLogStoreStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sls_log_store_status_with_options_async(
        self,
        request: main_models.DescribeSlsLogStoreStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlsLogStoreStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlsLogStoreStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlsLogStoreStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sls_log_store_status(
        self,
        request: main_models.DescribeSlsLogStoreStatusRequest,
    ) -> main_models.DescribeSlsLogStoreStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_sls_log_store_status_with_options(request, runtime)

    async def describe_sls_log_store_status_async(
        self,
        request: main_models.DescribeSlsLogStoreStatusRequest,
    ) -> main_models.DescribeSlsLogStoreStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_sls_log_store_status_with_options_async(request, runtime)

    def describe_template_resource_count_with_options(
        self,
        request: main_models.DescribeTemplateResourceCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTemplateResourceCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.template_ids):
            query['TemplateIds'] = request.template_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTemplateResourceCount',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTemplateResourceCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_template_resource_count_with_options_async(
        self,
        request: main_models.DescribeTemplateResourceCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTemplateResourceCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.template_ids):
            query['TemplateIds'] = request.template_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTemplateResourceCount',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTemplateResourceCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_template_resource_count(
        self,
        request: main_models.DescribeTemplateResourceCountRequest,
    ) -> main_models.DescribeTemplateResourceCountResponse:
        runtime = RuntimeOptions()
        return self.describe_template_resource_count_with_options(request, runtime)

    async def describe_template_resource_count_async(
        self,
        request: main_models.DescribeTemplateResourceCountRequest,
    ) -> main_models.DescribeTemplateResourceCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_template_resource_count_with_options_async(request, runtime)

    def describe_template_resources_with_options(
        self,
        request: main_models.DescribeTemplateResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTemplateResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asset_api):
            query['AssetApi'] = request.asset_api
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTemplateResources',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTemplateResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_template_resources_with_options_async(
        self,
        request: main_models.DescribeTemplateResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTemplateResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asset_api):
            query['AssetApi'] = request.asset_api
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTemplateResources',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTemplateResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_template_resources(
        self,
        request: main_models.DescribeTemplateResourcesRequest,
    ) -> main_models.DescribeTemplateResourcesResponse:
        runtime = RuntimeOptions()
        return self.describe_template_resources_with_options(request, runtime)

    async def describe_template_resources_async(
        self,
        request: main_models.DescribeTemplateResourcesRequest,
    ) -> main_models.DescribeTemplateResourcesResponse:
        runtime = RuntimeOptions()
        return await self.describe_template_resources_with_options_async(request, runtime)

    def describe_threat_event_with_options(
        self,
        request: main_models.DescribeThreatEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeThreatEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeThreatEvent',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeThreatEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_threat_event_with_options_async(
        self,
        request: main_models.DescribeThreatEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeThreatEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeThreatEvent',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeThreatEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_threat_event(
        self,
        request: main_models.DescribeThreatEventRequest,
    ) -> main_models.DescribeThreatEventResponse:
        runtime = RuntimeOptions()
        return self.describe_threat_event_with_options(request, runtime)

    async def describe_threat_event_async(
        self,
        request: main_models.DescribeThreatEventRequest,
    ) -> main_models.DescribeThreatEventResponse:
        runtime = RuntimeOptions()
        return await self.describe_threat_event_with_options_async(request, runtime)

    def describe_threat_event_detail_with_options(
        self,
        request: main_models.DescribeThreatEventDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeThreatEventDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeThreatEventDetail',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeThreatEventDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_threat_event_detail_with_options_async(
        self,
        request: main_models.DescribeThreatEventDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeThreatEventDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeThreatEventDetail',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeThreatEventDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_threat_event_detail(
        self,
        request: main_models.DescribeThreatEventDetailRequest,
    ) -> main_models.DescribeThreatEventDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_threat_event_detail_with_options(request, runtime)

    async def describe_threat_event_detail_async(
        self,
        request: main_models.DescribeThreatEventDetailRequest,
    ) -> main_models.DescribeThreatEventDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_threat_event_detail_with_options_async(request, runtime)

    def describe_user_abnormal_trend_with_options(
        self,
        request: main_models.DescribeUserAbnormalTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserAbnormalTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserAbnormalTrend',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserAbnormalTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_abnormal_trend_with_options_async(
        self,
        request: main_models.DescribeUserAbnormalTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserAbnormalTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserAbnormalTrend',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserAbnormalTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_abnormal_trend(
        self,
        request: main_models.DescribeUserAbnormalTrendRequest,
    ) -> main_models.DescribeUserAbnormalTrendResponse:
        runtime = RuntimeOptions()
        return self.describe_user_abnormal_trend_with_options(request, runtime)

    async def describe_user_abnormal_trend_async(
        self,
        request: main_models.DescribeUserAbnormalTrendRequest,
    ) -> main_models.DescribeUserAbnormalTrendResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_abnormal_trend_with_options_async(request, runtime)

    def describe_user_abnormal_type_with_options(
        self,
        request: main_models.DescribeUserAbnormalTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserAbnormalTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user_status_list):
            query['UserStatusList'] = request.user_status_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserAbnormalType',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserAbnormalTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_abnormal_type_with_options_async(
        self,
        request: main_models.DescribeUserAbnormalTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserAbnormalTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user_status_list):
            query['UserStatusList'] = request.user_status_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserAbnormalType',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserAbnormalTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_abnormal_type(
        self,
        request: main_models.DescribeUserAbnormalTypeRequest,
    ) -> main_models.DescribeUserAbnormalTypeResponse:
        runtime = RuntimeOptions()
        return self.describe_user_abnormal_type_with_options(request, runtime)

    async def describe_user_abnormal_type_async(
        self,
        request: main_models.DescribeUserAbnormalTypeRequest,
    ) -> main_models.DescribeUserAbnormalTypeResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_abnormal_type_with_options_async(request, runtime)

    def describe_user_api_request_with_options(
        self,
        request: main_models.DescribeUserApiRequestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserApiRequestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_format):
            query['ApiFormat'] = request.api_format
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserApiRequest',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserApiRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_api_request_with_options_async(
        self,
        request: main_models.DescribeUserApiRequestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserApiRequestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_format):
            query['ApiFormat'] = request.api_format
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserApiRequest',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserApiRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_api_request(
        self,
        request: main_models.DescribeUserApiRequestRequest,
    ) -> main_models.DescribeUserApiRequestResponse:
        runtime = RuntimeOptions()
        return self.describe_user_api_request_with_options(request, runtime)

    async def describe_user_api_request_async(
        self,
        request: main_models.DescribeUserApiRequestRequest,
    ) -> main_models.DescribeUserApiRequestResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_api_request_with_options_async(request, runtime)

    def describe_user_asset_with_options(
        self,
        request: main_models.DescribeUserAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserAssetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.days):
            query['Days'] = request.days
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserAsset',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_asset_with_options_async(
        self,
        request: main_models.DescribeUserAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserAssetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.days):
            query['Days'] = request.days
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserAsset',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_asset(
        self,
        request: main_models.DescribeUserAssetRequest,
    ) -> main_models.DescribeUserAssetResponse:
        runtime = RuntimeOptions()
        return self.describe_user_asset_with_options(request, runtime)

    async def describe_user_asset_async(
        self,
        request: main_models.DescribeUserAssetRequest,
    ) -> main_models.DescribeUserAssetResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_asset_with_options_async(request, runtime)

    def describe_user_event_trend_with_options(
        self,
        request: main_models.DescribeUserEventTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserEventTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.event_scope):
            query['EventScope'] = request.event_scope
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserEventTrend',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserEventTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_event_trend_with_options_async(
        self,
        request: main_models.DescribeUserEventTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserEventTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.event_scope):
            query['EventScope'] = request.event_scope
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserEventTrend',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserEventTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_event_trend(
        self,
        request: main_models.DescribeUserEventTrendRequest,
    ) -> main_models.DescribeUserEventTrendResponse:
        runtime = RuntimeOptions()
        return self.describe_user_event_trend_with_options(request, runtime)

    async def describe_user_event_trend_async(
        self,
        request: main_models.DescribeUserEventTrendRequest,
    ) -> main_models.DescribeUserEventTrendResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_event_trend_with_options_async(request, runtime)

    def describe_user_event_type_with_options(
        self,
        request: main_models.DescribeUserEventTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserEventTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_scope):
            query['EventScope'] = request.event_scope
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user_status_list):
            query['UserStatusList'] = request.user_status_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserEventType',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserEventTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_event_type_with_options_async(
        self,
        request: main_models.DescribeUserEventTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserEventTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_scope):
            query['EventScope'] = request.event_scope
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user_status_list):
            query['UserStatusList'] = request.user_status_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserEventType',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserEventTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_event_type(
        self,
        request: main_models.DescribeUserEventTypeRequest,
    ) -> main_models.DescribeUserEventTypeResponse:
        runtime = RuntimeOptions()
        return self.describe_user_event_type_with_options(request, runtime)

    async def describe_user_event_type_async(
        self,
        request: main_models.DescribeUserEventTypeRequest,
    ) -> main_models.DescribeUserEventTypeResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_event_type_with_options_async(request, runtime)

    def describe_user_log_field_config_with_options(
        self,
        request: main_models.DescribeUserLogFieldConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserLogFieldConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_type):
            query['DeliveryType'] = request.delivery_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserLogFieldConfig',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserLogFieldConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_log_field_config_with_options_async(
        self,
        request: main_models.DescribeUserLogFieldConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserLogFieldConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_type):
            query['DeliveryType'] = request.delivery_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserLogFieldConfig',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserLogFieldConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_log_field_config(
        self,
        request: main_models.DescribeUserLogFieldConfigRequest,
    ) -> main_models.DescribeUserLogFieldConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_user_log_field_config_with_options(request, runtime)

    async def describe_user_log_field_config_async(
        self,
        request: main_models.DescribeUserLogFieldConfigRequest,
    ) -> main_models.DescribeUserLogFieldConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_log_field_config_with_options_async(request, runtime)

    def describe_user_sls_log_regions_with_options(
        self,
        request: main_models.DescribeUserSlsLogRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserSlsLogRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserSlsLogRegions',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserSlsLogRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_sls_log_regions_with_options_async(
        self,
        request: main_models.DescribeUserSlsLogRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserSlsLogRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserSlsLogRegions',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserSlsLogRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_sls_log_regions(
        self,
        request: main_models.DescribeUserSlsLogRegionsRequest,
    ) -> main_models.DescribeUserSlsLogRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_user_sls_log_regions_with_options(request, runtime)

    async def describe_user_sls_log_regions_async(
        self,
        request: main_models.DescribeUserSlsLogRegionsRequest,
    ) -> main_models.DescribeUserSlsLogRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_sls_log_regions_with_options_async(request, runtime)

    def describe_user_waf_log_status_with_options(
        self,
        request: main_models.DescribeUserWafLogStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserWafLogStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserWafLogStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserWafLogStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_waf_log_status_with_options_async(
        self,
        request: main_models.DescribeUserWafLogStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserWafLogStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserWafLogStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserWafLogStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_waf_log_status(
        self,
        request: main_models.DescribeUserWafLogStatusRequest,
    ) -> main_models.DescribeUserWafLogStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_user_waf_log_status_with_options(request, runtime)

    async def describe_user_waf_log_status_async(
        self,
        request: main_models.DescribeUserWafLogStatusRequest,
    ) -> main_models.DescribeUserWafLogStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_waf_log_status_with_options_async(request, runtime)

    def describe_verify_content_with_options(
        self,
        request: main_models.DescribeVerifyContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifyContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_origin):
            query['AccessOrigin'] = request.access_origin
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifyContent',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifyContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_verify_content_with_options_async(
        self,
        request: main_models.DescribeVerifyContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVerifyContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_origin):
            query['AccessOrigin'] = request.access_origin
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVerifyContent',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVerifyContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_verify_content(
        self,
        request: main_models.DescribeVerifyContentRequest,
    ) -> main_models.DescribeVerifyContentResponse:
        runtime = RuntimeOptions()
        return self.describe_verify_content_with_options(request, runtime)

    async def describe_verify_content_async(
        self,
        request: main_models.DescribeVerifyContentRequest,
    ) -> main_models.DescribeVerifyContentResponse:
        runtime = RuntimeOptions()
        return await self.describe_verify_content_with_options_async(request, runtime)

    def describe_visit_top_ip_with_options(
        self,
        request: main_models.DescribeVisitTopIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVisitTopIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVisitTopIp',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVisitTopIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_visit_top_ip_with_options_async(
        self,
        request: main_models.DescribeVisitTopIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVisitTopIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVisitTopIp',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVisitTopIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_visit_top_ip(
        self,
        request: main_models.DescribeVisitTopIpRequest,
    ) -> main_models.DescribeVisitTopIpResponse:
        runtime = RuntimeOptions()
        return self.describe_visit_top_ip_with_options(request, runtime)

    async def describe_visit_top_ip_async(
        self,
        request: main_models.DescribeVisitTopIpRequest,
    ) -> main_models.DescribeVisitTopIpResponse:
        runtime = RuntimeOptions()
        return await self.describe_visit_top_ip_with_options_async(request, runtime)

    def describe_visit_uas_with_options(
        self,
        request: main_models.DescribeVisitUasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVisitUasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVisitUas',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVisitUasResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_visit_uas_with_options_async(
        self,
        request: main_models.DescribeVisitUasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVisitUasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVisitUas',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVisitUasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_visit_uas(
        self,
        request: main_models.DescribeVisitUasRequest,
    ) -> main_models.DescribeVisitUasResponse:
        runtime = RuntimeOptions()
        return self.describe_visit_uas_with_options(request, runtime)

    async def describe_visit_uas_async(
        self,
        request: main_models.DescribeVisitUasRequest,
    ) -> main_models.DescribeVisitUasResponse:
        runtime = RuntimeOptions()
        return await self.describe_visit_uas_with_options_async(request, runtime)

    def describe_waf_source_ip_segment_with_options(
        self,
        request: main_models.DescribeWafSourceIpSegmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWafSourceIpSegmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWafSourceIpSegment',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWafSourceIpSegmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_waf_source_ip_segment_with_options_async(
        self,
        request: main_models.DescribeWafSourceIpSegmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWafSourceIpSegmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWafSourceIpSegment',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWafSourceIpSegmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_waf_source_ip_segment(
        self,
        request: main_models.DescribeWafSourceIpSegmentRequest,
    ) -> main_models.DescribeWafSourceIpSegmentResponse:
        runtime = RuntimeOptions()
        return self.describe_waf_source_ip_segment_with_options(request, runtime)

    async def describe_waf_source_ip_segment_async(
        self,
        request: main_models.DescribeWafSourceIpSegmentRequest,
    ) -> main_models.DescribeWafSourceIpSegmentResponse:
        runtime = RuntimeOptions()
        return await self.describe_waf_source_ip_segment_with_options_async(request, runtime)

    def initialize_waf_operation_role_with_options(
        self,
        request: main_models.InitializeWafOperationRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitializeWafOperationRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InitializeWafOperationRole',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitializeWafOperationRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def initialize_waf_operation_role_with_options_async(
        self,
        request: main_models.InitializeWafOperationRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitializeWafOperationRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InitializeWafOperationRole',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitializeWafOperationRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def initialize_waf_operation_role(
        self,
        request: main_models.InitializeWafOperationRoleRequest,
    ) -> main_models.InitializeWafOperationRoleResponse:
        runtime = RuntimeOptions()
        return self.initialize_waf_operation_role_with_options(request, runtime)

    async def initialize_waf_operation_role_async(
        self,
        request: main_models.InitializeWafOperationRoleRequest,
    ) -> main_models.InitializeWafOperationRoleResponse:
        runtime = RuntimeOptions()
        return await self.initialize_waf_operation_role_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: main_models.ListTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagKeys',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: main_models.ListTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagKeys',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: main_models.ListTagKeysRequest,
    ) -> main_models.ListTagKeysResponse:
        runtime = RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: main_models.ListTagKeysRequest,
    ) -> main_models.ListTagKeysResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2021-10-01',
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
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2021-10-01',
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

    def list_tag_values_with_options(
        self,
        request: main_models.ListTagValuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagValuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagValues',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: main_models.ListTagValuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagValuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagValues',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_values(
        self,
        request: main_models.ListTagValuesRequest,
    ) -> main_models.ListTagValuesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: main_models.ListTagValuesRequest,
    ) -> main_models.ListTagValuesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def modify_apisec_abnormals_with_options(
        self,
        request: main_models.ModifyApisecAbnormalsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApisecAbnormalsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.abnormal_ids):
            query['AbnormalIds'] = request.abnormal_ids
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.user_status):
            query['UserStatus'] = request.user_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApisecAbnormals',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApisecAbnormalsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_apisec_abnormals_with_options_async(
        self,
        request: main_models.ModifyApisecAbnormalsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApisecAbnormalsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.abnormal_ids):
            query['AbnormalIds'] = request.abnormal_ids
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.user_status):
            query['UserStatus'] = request.user_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApisecAbnormals',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApisecAbnormalsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_apisec_abnormals(
        self,
        request: main_models.ModifyApisecAbnormalsRequest,
    ) -> main_models.ModifyApisecAbnormalsResponse:
        runtime = RuntimeOptions()
        return self.modify_apisec_abnormals_with_options(request, runtime)

    async def modify_apisec_abnormals_async(
        self,
        request: main_models.ModifyApisecAbnormalsRequest,
    ) -> main_models.ModifyApisecAbnormalsResponse:
        runtime = RuntimeOptions()
        return await self.modify_apisec_abnormals_with_options_async(request, runtime)

    def modify_apisec_api_resource_with_options(
        self,
        request: main_models.ModifyApisecApiResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApisecApiResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.follow):
            query['Follow'] = request.follow
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApisecApiResource',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApisecApiResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_apisec_api_resource_with_options_async(
        self,
        request: main_models.ModifyApisecApiResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApisecApiResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.follow):
            query['Follow'] = request.follow
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApisecApiResource',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApisecApiResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_apisec_api_resource(
        self,
        request: main_models.ModifyApisecApiResourceRequest,
    ) -> main_models.ModifyApisecApiResourceResponse:
        runtime = RuntimeOptions()
        return self.modify_apisec_api_resource_with_options(request, runtime)

    async def modify_apisec_api_resource_async(
        self,
        request: main_models.ModifyApisecApiResourceRequest,
    ) -> main_models.ModifyApisecApiResourceResponse:
        runtime = RuntimeOptions()
        return await self.modify_apisec_api_resource_with_options_async(request, runtime)

    def modify_apisec_events_with_options(
        self,
        request: main_models.ModifyApisecEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApisecEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.event_ids):
            query['EventIds'] = request.event_ids
        if not DaraCore.is_null(request.event_scope):
            query['EventScope'] = request.event_scope
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.user_status):
            query['UserStatus'] = request.user_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApisecEvents',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApisecEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_apisec_events_with_options_async(
        self,
        request: main_models.ModifyApisecEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApisecEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.event_ids):
            query['EventIds'] = request.event_ids
        if not DaraCore.is_null(request.event_scope):
            query['EventScope'] = request.event_scope
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.note):
            query['Note'] = request.note
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.user_status):
            query['UserStatus'] = request.user_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApisecEvents',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApisecEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_apisec_events(
        self,
        request: main_models.ModifyApisecEventsRequest,
    ) -> main_models.ModifyApisecEventsResponse:
        runtime = RuntimeOptions()
        return self.modify_apisec_events_with_options(request, runtime)

    async def modify_apisec_events_async(
        self,
        request: main_models.ModifyApisecEventsRequest,
    ) -> main_models.ModifyApisecEventsResponse:
        runtime = RuntimeOptions()
        return await self.modify_apisec_events_with_options_async(request, runtime)

    def modify_apisec_log_delivery_with_options(
        self,
        request: main_models.ModifyApisecLogDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApisecLogDeliveryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assert_key):
            query['AssertKey'] = request.assert_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.log_region_id):
            query['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApisecLogDelivery',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApisecLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_apisec_log_delivery_with_options_async(
        self,
        request: main_models.ModifyApisecLogDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApisecLogDeliveryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assert_key):
            query['AssertKey'] = request.assert_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.log_region_id):
            query['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApisecLogDelivery',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApisecLogDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_apisec_log_delivery(
        self,
        request: main_models.ModifyApisecLogDeliveryRequest,
    ) -> main_models.ModifyApisecLogDeliveryResponse:
        runtime = RuntimeOptions()
        return self.modify_apisec_log_delivery_with_options(request, runtime)

    async def modify_apisec_log_delivery_async(
        self,
        request: main_models.ModifyApisecLogDeliveryRequest,
    ) -> main_models.ModifyApisecLogDeliveryResponse:
        runtime = RuntimeOptions()
        return await self.modify_apisec_log_delivery_with_options_async(request, runtime)

    def modify_apisec_log_delivery_status_with_options(
        self,
        request: main_models.ModifyApisecLogDeliveryStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApisecLogDeliveryStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assert_key):
            query['AssertKey'] = request.assert_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApisecLogDeliveryStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApisecLogDeliveryStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_apisec_log_delivery_status_with_options_async(
        self,
        request: main_models.ModifyApisecLogDeliveryStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApisecLogDeliveryStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assert_key):
            query['AssertKey'] = request.assert_key
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApisecLogDeliveryStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApisecLogDeliveryStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_apisec_log_delivery_status(
        self,
        request: main_models.ModifyApisecLogDeliveryStatusRequest,
    ) -> main_models.ModifyApisecLogDeliveryStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_apisec_log_delivery_status_with_options(request, runtime)

    async def modify_apisec_log_delivery_status_async(
        self,
        request: main_models.ModifyApisecLogDeliveryStatusRequest,
    ) -> main_models.ModifyApisecLogDeliveryStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_apisec_log_delivery_status_with_options_async(request, runtime)

    def modify_apisec_module_status_with_options(
        self,
        request: main_models.ModifyApisecModuleStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApisecModuleStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.report_status):
            query['ReportStatus'] = request.report_status
        if not DaraCore.is_null(request.resource_groups):
            query['ResourceGroups'] = request.resource_groups
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        if not DaraCore.is_null(request.trace_status):
            query['TraceStatus'] = request.trace_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApisecModuleStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApisecModuleStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_apisec_module_status_with_options_async(
        self,
        request: main_models.ModifyApisecModuleStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApisecModuleStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.report_status):
            query['ReportStatus'] = request.report_status
        if not DaraCore.is_null(request.resource_groups):
            query['ResourceGroups'] = request.resource_groups
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        if not DaraCore.is_null(request.trace_status):
            query['TraceStatus'] = request.trace_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApisecModuleStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApisecModuleStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_apisec_module_status(
        self,
        request: main_models.ModifyApisecModuleStatusRequest,
    ) -> main_models.ModifyApisecModuleStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_apisec_module_status_with_options(request, runtime)

    async def modify_apisec_module_status_async(
        self,
        request: main_models.ModifyApisecModuleStatusRequest,
    ) -> main_models.ModifyApisecModuleStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_apisec_module_status_with_options_async(request, runtime)

    def modify_apisec_status_with_options(
        self,
        request: main_models.ModifyApisecStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApisecStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apisec_status):
            query['ApisecStatus'] = request.apisec_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_groups):
            query['ResourceGroups'] = request.resource_groups
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApisecStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApisecStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_apisec_status_with_options_async(
        self,
        request: main_models.ModifyApisecStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApisecStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apisec_status):
            query['ApisecStatus'] = request.apisec_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_groups):
            query['ResourceGroups'] = request.resource_groups
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApisecStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApisecStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_apisec_status(
        self,
        request: main_models.ModifyApisecStatusRequest,
    ) -> main_models.ModifyApisecStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_apisec_status_with_options(request, runtime)

    async def modify_apisec_status_async(
        self,
        request: main_models.ModifyApisecStatusRequest,
    ) -> main_models.ModifyApisecStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_apisec_status_with_options_async(request, runtime)

    def modify_cloud_resource_with_options(
        self,
        tmp_req: main_models.ModifyCloudResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCloudResourceResponse:
        tmp_req.validate()
        request = main_models.ModifyCloudResourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.listen):
            request.listen_shrink = Utils.array_to_string_with_specified_style(tmp_req.listen, 'Listen', 'json')
        if not DaraCore.is_null(tmp_req.redirect):
            request.redirect_shrink = Utils.array_to_string_with_specified_style(tmp_req.redirect, 'Redirect', 'json')
        query = {}
        if not DaraCore.is_null(request.cloud_resource_id):
            query['CloudResourceId'] = request.cloud_resource_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.listen_shrink):
            query['Listen'] = request.listen_shrink
        if not DaraCore.is_null(request.redirect_shrink):
            query['Redirect'] = request.redirect_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCloudResource',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCloudResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cloud_resource_with_options_async(
        self,
        tmp_req: main_models.ModifyCloudResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCloudResourceResponse:
        tmp_req.validate()
        request = main_models.ModifyCloudResourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.listen):
            request.listen_shrink = Utils.array_to_string_with_specified_style(tmp_req.listen, 'Listen', 'json')
        if not DaraCore.is_null(tmp_req.redirect):
            request.redirect_shrink = Utils.array_to_string_with_specified_style(tmp_req.redirect, 'Redirect', 'json')
        query = {}
        if not DaraCore.is_null(request.cloud_resource_id):
            query['CloudResourceId'] = request.cloud_resource_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.listen_shrink):
            query['Listen'] = request.listen_shrink
        if not DaraCore.is_null(request.redirect_shrink):
            query['Redirect'] = request.redirect_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCloudResource',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCloudResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cloud_resource(
        self,
        request: main_models.ModifyCloudResourceRequest,
    ) -> main_models.ModifyCloudResourceResponse:
        runtime = RuntimeOptions()
        return self.modify_cloud_resource_with_options(request, runtime)

    async def modify_cloud_resource_async(
        self,
        request: main_models.ModifyCloudResourceRequest,
    ) -> main_models.ModifyCloudResourceResponse:
        runtime = RuntimeOptions()
        return await self.modify_cloud_resource_with_options_async(request, runtime)

    def modify_cloud_resource_cert_with_options(
        self,
        request: main_models.ModifyCloudResourceCertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCloudResourceCertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certificates):
            query['Certificates'] = request.certificates
        if not DaraCore.is_null(request.cloud_resource_id):
            query['CloudResourceId'] = request.cloud_resource_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not DaraCore.is_null(request.resource_product):
            query['ResourceProduct'] = request.resource_product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCloudResourceCert',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCloudResourceCertResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cloud_resource_cert_with_options_async(
        self,
        request: main_models.ModifyCloudResourceCertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCloudResourceCertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certificates):
            query['Certificates'] = request.certificates
        if not DaraCore.is_null(request.cloud_resource_id):
            query['CloudResourceId'] = request.cloud_resource_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not DaraCore.is_null(request.resource_product):
            query['ResourceProduct'] = request.resource_product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCloudResourceCert',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCloudResourceCertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cloud_resource_cert(
        self,
        request: main_models.ModifyCloudResourceCertRequest,
    ) -> main_models.ModifyCloudResourceCertResponse:
        runtime = RuntimeOptions()
        return self.modify_cloud_resource_cert_with_options(request, runtime)

    async def modify_cloud_resource_cert_async(
        self,
        request: main_models.ModifyCloudResourceCertRequest,
    ) -> main_models.ModifyCloudResourceCertResponse:
        runtime = RuntimeOptions()
        return await self.modify_cloud_resource_cert_with_options_async(request, runtime)

    def modify_default_https_with_options(
        self,
        request: main_models.ModifyDefaultHttpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDefaultHttpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_id):
            query['CertId'] = request.cert_id
        if not DaraCore.is_null(request.cipher_suite):
            query['CipherSuite'] = request.cipher_suite
        if not DaraCore.is_null(request.custom_ciphers):
            query['CustomCiphers'] = request.custom_ciphers
        if not DaraCore.is_null(request.enable_tlsv_3):
            query['EnableTLSv3'] = request.enable_tlsv_3
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.tlsversion):
            query['TLSVersion'] = request.tlsversion
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDefaultHttps',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDefaultHttpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_default_https_with_options_async(
        self,
        request: main_models.ModifyDefaultHttpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDefaultHttpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_id):
            query['CertId'] = request.cert_id
        if not DaraCore.is_null(request.cipher_suite):
            query['CipherSuite'] = request.cipher_suite
        if not DaraCore.is_null(request.custom_ciphers):
            query['CustomCiphers'] = request.custom_ciphers
        if not DaraCore.is_null(request.enable_tlsv_3):
            query['EnableTLSv3'] = request.enable_tlsv_3
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.tlsversion):
            query['TLSVersion'] = request.tlsversion
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDefaultHttps',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDefaultHttpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_default_https(
        self,
        request: main_models.ModifyDefaultHttpsRequest,
    ) -> main_models.ModifyDefaultHttpsResponse:
        runtime = RuntimeOptions()
        return self.modify_default_https_with_options(request, runtime)

    async def modify_default_https_async(
        self,
        request: main_models.ModifyDefaultHttpsRequest,
    ) -> main_models.ModifyDefaultHttpsResponse:
        runtime = RuntimeOptions()
        return await self.modify_default_https_with_options_async(request, runtime)

    def modify_defense_resource_group_with_options(
        self,
        request: main_models.ModifyDefenseResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDefenseResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_list):
            query['AddList'] = request.add_list
        if not DaraCore.is_null(request.delete_list):
            query['DeleteList'] = request.delete_list
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDefenseResourceGroup',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDefenseResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_defense_resource_group_with_options_async(
        self,
        request: main_models.ModifyDefenseResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDefenseResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_list):
            query['AddList'] = request.add_list
        if not DaraCore.is_null(request.delete_list):
            query['DeleteList'] = request.delete_list
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDefenseResourceGroup',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDefenseResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_defense_resource_group(
        self,
        request: main_models.ModifyDefenseResourceGroupRequest,
    ) -> main_models.ModifyDefenseResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_defense_resource_group_with_options(request, runtime)

    async def modify_defense_resource_group_async(
        self,
        request: main_models.ModifyDefenseResourceGroupRequest,
    ) -> main_models.ModifyDefenseResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_defense_resource_group_with_options_async(request, runtime)

    def modify_defense_resource_xff_with_options(
        self,
        request: main_models.ModifyDefenseResourceXffRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDefenseResourceXffResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acw_cookie_status):
            query['AcwCookieStatus'] = request.acw_cookie_status
        if not DaraCore.is_null(request.acw_secure_status):
            query['AcwSecureStatus'] = request.acw_secure_status
        if not DaraCore.is_null(request.acw_v3secure_status):
            query['AcwV3SecureStatus'] = request.acw_v3secure_status
        if not DaraCore.is_null(request.custom_headers):
            query['CustomHeaders'] = request.custom_headers
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.response_headers):
            query['ResponseHeaders'] = request.response_headers
        if not DaraCore.is_null(request.xff_status):
            query['XffStatus'] = request.xff_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDefenseResourceXff',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDefenseResourceXffResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_defense_resource_xff_with_options_async(
        self,
        request: main_models.ModifyDefenseResourceXffRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDefenseResourceXffResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acw_cookie_status):
            query['AcwCookieStatus'] = request.acw_cookie_status
        if not DaraCore.is_null(request.acw_secure_status):
            query['AcwSecureStatus'] = request.acw_secure_status
        if not DaraCore.is_null(request.acw_v3secure_status):
            query['AcwV3SecureStatus'] = request.acw_v3secure_status
        if not DaraCore.is_null(request.custom_headers):
            query['CustomHeaders'] = request.custom_headers
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.response_headers):
            query['ResponseHeaders'] = request.response_headers
        if not DaraCore.is_null(request.xff_status):
            query['XffStatus'] = request.xff_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDefenseResourceXff',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDefenseResourceXffResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_defense_resource_xff(
        self,
        request: main_models.ModifyDefenseResourceXffRequest,
    ) -> main_models.ModifyDefenseResourceXffResponse:
        runtime = RuntimeOptions()
        return self.modify_defense_resource_xff_with_options(request, runtime)

    async def modify_defense_resource_xff_async(
        self,
        request: main_models.ModifyDefenseResourceXffRequest,
    ) -> main_models.ModifyDefenseResourceXffResponse:
        runtime = RuntimeOptions()
        return await self.modify_defense_resource_xff_with_options_async(request, runtime)

    def modify_defense_rule_with_options(
        self,
        request: main_models.ModifyDefenseRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDefenseRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not DaraCore.is_null(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        body = {}
        if not DaraCore.is_null(request.rules):
            body['Rules'] = request.rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDefenseRule',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDefenseRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_defense_rule_with_options_async(
        self,
        request: main_models.ModifyDefenseRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDefenseRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not DaraCore.is_null(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        body = {}
        if not DaraCore.is_null(request.rules):
            body['Rules'] = request.rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDefenseRule',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDefenseRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_defense_rule(
        self,
        request: main_models.ModifyDefenseRuleRequest,
    ) -> main_models.ModifyDefenseRuleResponse:
        runtime = RuntimeOptions()
        return self.modify_defense_rule_with_options(request, runtime)

    async def modify_defense_rule_async(
        self,
        request: main_models.ModifyDefenseRuleRequest,
    ) -> main_models.ModifyDefenseRuleResponse:
        runtime = RuntimeOptions()
        return await self.modify_defense_rule_with_options_async(request, runtime)

    def modify_defense_rule_cache_with_options(
        self,
        request: main_models.ModifyDefenseRuleCacheRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDefenseRuleCacheResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDefenseRuleCache',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDefenseRuleCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_defense_rule_cache_with_options_async(
        self,
        request: main_models.ModifyDefenseRuleCacheRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDefenseRuleCacheResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDefenseRuleCache',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDefenseRuleCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_defense_rule_cache(
        self,
        request: main_models.ModifyDefenseRuleCacheRequest,
    ) -> main_models.ModifyDefenseRuleCacheResponse:
        runtime = RuntimeOptions()
        return self.modify_defense_rule_cache_with_options(request, runtime)

    async def modify_defense_rule_cache_async(
        self,
        request: main_models.ModifyDefenseRuleCacheRequest,
    ) -> main_models.ModifyDefenseRuleCacheResponse:
        runtime = RuntimeOptions()
        return await self.modify_defense_rule_cache_with_options_async(request, runtime)

    def modify_defense_rule_status_with_options(
        self,
        request: main_models.ModifyDefenseRuleStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDefenseRuleStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_status):
            query['RuleStatus'] = request.rule_status
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDefenseRuleStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDefenseRuleStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_defense_rule_status_with_options_async(
        self,
        request: main_models.ModifyDefenseRuleStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDefenseRuleStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_status):
            query['RuleStatus'] = request.rule_status
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDefenseRuleStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDefenseRuleStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_defense_rule_status(
        self,
        request: main_models.ModifyDefenseRuleStatusRequest,
    ) -> main_models.ModifyDefenseRuleStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_defense_rule_status_with_options(request, runtime)

    async def modify_defense_rule_status_async(
        self,
        request: main_models.ModifyDefenseRuleStatusRequest,
    ) -> main_models.ModifyDefenseRuleStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_defense_rule_status_with_options_async(request, runtime)

    def modify_defense_scene_config_with_options(
        self,
        request: main_models.ModifyDefenseSceneConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDefenseSceneConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_key):
            query['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.config_value):
            query['ConfigValue'] = request.config_value
        if not DaraCore.is_null(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDefenseSceneConfig',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDefenseSceneConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_defense_scene_config_with_options_async(
        self,
        request: main_models.ModifyDefenseSceneConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDefenseSceneConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_key):
            query['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.config_value):
            query['ConfigValue'] = request.config_value
        if not DaraCore.is_null(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDefenseSceneConfig',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDefenseSceneConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_defense_scene_config(
        self,
        request: main_models.ModifyDefenseSceneConfigRequest,
    ) -> main_models.ModifyDefenseSceneConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_defense_scene_config_with_options(request, runtime)

    async def modify_defense_scene_config_async(
        self,
        request: main_models.ModifyDefenseSceneConfigRequest,
    ) -> main_models.ModifyDefenseSceneConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_defense_scene_config_with_options_async(request, runtime)

    def modify_defense_template_with_options(
        self,
        request: main_models.ModifyDefenseTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDefenseTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDefenseTemplate',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDefenseTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_defense_template_with_options_async(
        self,
        request: main_models.ModifyDefenseTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDefenseTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDefenseTemplate',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDefenseTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_defense_template(
        self,
        request: main_models.ModifyDefenseTemplateRequest,
    ) -> main_models.ModifyDefenseTemplateResponse:
        runtime = RuntimeOptions()
        return self.modify_defense_template_with_options(request, runtime)

    async def modify_defense_template_async(
        self,
        request: main_models.ModifyDefenseTemplateRequest,
    ) -> main_models.ModifyDefenseTemplateResponse:
        runtime = RuntimeOptions()
        return await self.modify_defense_template_with_options_async(request, runtime)

    def modify_defense_template_status_with_options(
        self,
        request: main_models.ModifyDefenseTemplateStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDefenseTemplateStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_status):
            query['TemplateStatus'] = request.template_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDefenseTemplateStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDefenseTemplateStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_defense_template_status_with_options_async(
        self,
        request: main_models.ModifyDefenseTemplateStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDefenseTemplateStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_status):
            query['TemplateStatus'] = request.template_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDefenseTemplateStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDefenseTemplateStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_defense_template_status(
        self,
        request: main_models.ModifyDefenseTemplateStatusRequest,
    ) -> main_models.ModifyDefenseTemplateStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_defense_template_status_with_options(request, runtime)

    async def modify_defense_template_status_async(
        self,
        request: main_models.ModifyDefenseTemplateStatusRequest,
    ) -> main_models.ModifyDefenseTemplateStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_defense_template_status_with_options_async(request, runtime)

    def modify_domain_with_options(
        self,
        tmp_req: main_models.ModifyDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDomainResponse:
        tmp_req.validate()
        request = main_models.ModifyDomainShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.listen):
            request.listen_shrink = Utils.array_to_string_with_specified_style(tmp_req.listen, 'Listen', 'json')
        if not DaraCore.is_null(tmp_req.redirect):
            request.redirect_shrink = Utils.array_to_string_with_specified_style(tmp_req.redirect, 'Redirect', 'json')
        query = {}
        if not DaraCore.is_null(request.access_type):
            query['AccessType'] = request.access_type
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.listen_shrink):
            query['Listen'] = request.listen_shrink
        if not DaraCore.is_null(request.redirect_shrink):
            query['Redirect'] = request.redirect_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDomain',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_domain_with_options_async(
        self,
        tmp_req: main_models.ModifyDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDomainResponse:
        tmp_req.validate()
        request = main_models.ModifyDomainShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.listen):
            request.listen_shrink = Utils.array_to_string_with_specified_style(tmp_req.listen, 'Listen', 'json')
        if not DaraCore.is_null(tmp_req.redirect):
            request.redirect_shrink = Utils.array_to_string_with_specified_style(tmp_req.redirect, 'Redirect', 'json')
        query = {}
        if not DaraCore.is_null(request.access_type):
            query['AccessType'] = request.access_type
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.listen_shrink):
            query['Listen'] = request.listen_shrink
        if not DaraCore.is_null(request.redirect_shrink):
            query['Redirect'] = request.redirect_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDomain',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_domain(
        self,
        request: main_models.ModifyDomainRequest,
    ) -> main_models.ModifyDomainResponse:
        runtime = RuntimeOptions()
        return self.modify_domain_with_options(request, runtime)

    async def modify_domain_async(
        self,
        request: main_models.ModifyDomainRequest,
    ) -> main_models.ModifyDomainResponse:
        runtime = RuntimeOptions()
        return await self.modify_domain_with_options_async(request, runtime)

    def modify_domain_cert_with_options(
        self,
        request: main_models.ModifyDomainCertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDomainCertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_id):
            query['CertId'] = request.cert_id
        if not DaraCore.is_null(request.cipher_suite):
            query['CipherSuite'] = request.cipher_suite
        if not DaraCore.is_null(request.custom_ciphers):
            query['CustomCiphers'] = request.custom_ciphers
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enable_tlsv_3):
            query['EnableTLSv3'] = request.enable_tlsv_3
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tlsversion):
            query['TLSVersion'] = request.tlsversion
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDomainCert',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDomainCertResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_domain_cert_with_options_async(
        self,
        request: main_models.ModifyDomainCertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDomainCertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_id):
            query['CertId'] = request.cert_id
        if not DaraCore.is_null(request.cipher_suite):
            query['CipherSuite'] = request.cipher_suite
        if not DaraCore.is_null(request.custom_ciphers):
            query['CustomCiphers'] = request.custom_ciphers
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enable_tlsv_3):
            query['EnableTLSv3'] = request.enable_tlsv_3
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tlsversion):
            query['TLSVersion'] = request.tlsversion
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDomainCert',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDomainCertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_domain_cert(
        self,
        request: main_models.ModifyDomainCertRequest,
    ) -> main_models.ModifyDomainCertResponse:
        runtime = RuntimeOptions()
        return self.modify_domain_cert_with_options(request, runtime)

    async def modify_domain_cert_async(
        self,
        request: main_models.ModifyDomainCertRequest,
    ) -> main_models.ModifyDomainCertResponse:
        runtime = RuntimeOptions()
        return await self.modify_domain_cert_with_options_async(request, runtime)

    def modify_domain_punish_status_with_options(
        self,
        request: main_models.ModifyDomainPunishStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDomainPunishStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDomainPunishStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDomainPunishStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_domain_punish_status_with_options_async(
        self,
        request: main_models.ModifyDomainPunishStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDomainPunishStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDomainPunishStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDomainPunishStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_domain_punish_status(
        self,
        request: main_models.ModifyDomainPunishStatusRequest,
    ) -> main_models.ModifyDomainPunishStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_domain_punish_status_with_options(request, runtime)

    async def modify_domain_punish_status_async(
        self,
        request: main_models.ModifyDomainPunishStatusRequest,
    ) -> main_models.ModifyDomainPunishStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_domain_punish_status_with_options_async(request, runtime)

    def modify_hybrid_cloud_cluster_with_options(
        self,
        request: main_models.ModifyHybridCloudClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHybridCloudClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not DaraCore.is_null(request.access_region):
            query['AccessRegion'] = request.access_region
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.http_ports):
            query['HttpPorts'] = request.http_ports
        if not DaraCore.is_null(request.https_ports):
            query['HttpsPorts'] = request.https_ports
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.log_fields_not_returned):
            query['LogFieldsNotReturned'] = request.log_fields_not_returned
        if not DaraCore.is_null(request.protection_server_count):
            query['ProtectionServerCount'] = request.protection_server_count
        if not DaraCore.is_null(request.proxy_status):
            query['ProxyStatus'] = request.proxy_status
        if not DaraCore.is_null(request.proxy_type):
            query['ProxyType'] = request.proxy_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_config):
            query['RuleConfig'] = request.rule_config
        if not DaraCore.is_null(request.rule_status):
            query['RuleStatus'] = request.rule_status
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHybridCloudCluster',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHybridCloudClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hybrid_cloud_cluster_with_options_async(
        self,
        request: main_models.ModifyHybridCloudClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHybridCloudClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not DaraCore.is_null(request.access_region):
            query['AccessRegion'] = request.access_region
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.http_ports):
            query['HttpPorts'] = request.http_ports
        if not DaraCore.is_null(request.https_ports):
            query['HttpsPorts'] = request.https_ports
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.log_fields_not_returned):
            query['LogFieldsNotReturned'] = request.log_fields_not_returned
        if not DaraCore.is_null(request.protection_server_count):
            query['ProtectionServerCount'] = request.protection_server_count
        if not DaraCore.is_null(request.proxy_status):
            query['ProxyStatus'] = request.proxy_status
        if not DaraCore.is_null(request.proxy_type):
            query['ProxyType'] = request.proxy_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_config):
            query['RuleConfig'] = request.rule_config
        if not DaraCore.is_null(request.rule_status):
            query['RuleStatus'] = request.rule_status
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHybridCloudCluster',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHybridCloudClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hybrid_cloud_cluster(
        self,
        request: main_models.ModifyHybridCloudClusterRequest,
    ) -> main_models.ModifyHybridCloudClusterResponse:
        runtime = RuntimeOptions()
        return self.modify_hybrid_cloud_cluster_with_options(request, runtime)

    async def modify_hybrid_cloud_cluster_async(
        self,
        request: main_models.ModifyHybridCloudClusterRequest,
    ) -> main_models.ModifyHybridCloudClusterResponse:
        runtime = RuntimeOptions()
        return await self.modify_hybrid_cloud_cluster_with_options_async(request, runtime)

    def modify_hybrid_cloud_cluster_bypass_status_with_options(
        self,
        request: main_models.ModifyHybridCloudClusterBypassStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHybridCloudClusterBypassStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_resource_id):
            query['ClusterResourceId'] = request.cluster_resource_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_status):
            query['RuleStatus'] = request.rule_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHybridCloudClusterBypassStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHybridCloudClusterBypassStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hybrid_cloud_cluster_bypass_status_with_options_async(
        self,
        request: main_models.ModifyHybridCloudClusterBypassStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHybridCloudClusterBypassStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_resource_id):
            query['ClusterResourceId'] = request.cluster_resource_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_status):
            query['RuleStatus'] = request.rule_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHybridCloudClusterBypassStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHybridCloudClusterBypassStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hybrid_cloud_cluster_bypass_status(
        self,
        request: main_models.ModifyHybridCloudClusterBypassStatusRequest,
    ) -> main_models.ModifyHybridCloudClusterBypassStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_hybrid_cloud_cluster_bypass_status_with_options(request, runtime)

    async def modify_hybrid_cloud_cluster_bypass_status_async(
        self,
        request: main_models.ModifyHybridCloudClusterBypassStatusRequest,
    ) -> main_models.ModifyHybridCloudClusterBypassStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_hybrid_cloud_cluster_bypass_status_with_options_async(request, runtime)

    def modify_hybrid_cloud_cluster_rule_with_options(
        self,
        request: main_models.ModifyHybridCloudClusterRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHybridCloudClusterRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_rule_resource_id):
            query['ClusterRuleResourceId'] = request.cluster_rule_resource_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_config):
            query['RuleConfig'] = request.rule_config
        if not DaraCore.is_null(request.rule_status):
            query['RuleStatus'] = request.rule_status
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHybridCloudClusterRule',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHybridCloudClusterRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hybrid_cloud_cluster_rule_with_options_async(
        self,
        request: main_models.ModifyHybridCloudClusterRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHybridCloudClusterRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_rule_resource_id):
            query['ClusterRuleResourceId'] = request.cluster_rule_resource_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_config):
            query['RuleConfig'] = request.rule_config
        if not DaraCore.is_null(request.rule_status):
            query['RuleStatus'] = request.rule_status
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHybridCloudClusterRule',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHybridCloudClusterRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hybrid_cloud_cluster_rule(
        self,
        request: main_models.ModifyHybridCloudClusterRuleRequest,
    ) -> main_models.ModifyHybridCloudClusterRuleResponse:
        runtime = RuntimeOptions()
        return self.modify_hybrid_cloud_cluster_rule_with_options(request, runtime)

    async def modify_hybrid_cloud_cluster_rule_async(
        self,
        request: main_models.ModifyHybridCloudClusterRuleRequest,
    ) -> main_models.ModifyHybridCloudClusterRuleResponse:
        runtime = RuntimeOptions()
        return await self.modify_hybrid_cloud_cluster_rule_with_options_async(request, runtime)

    def modify_hybrid_cloud_group_with_options(
        self,
        request: main_models.ModifyHybridCloudGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHybridCloudGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHybridCloudGroup',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHybridCloudGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hybrid_cloud_group_with_options_async(
        self,
        request: main_models.ModifyHybridCloudGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHybridCloudGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHybridCloudGroup',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHybridCloudGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hybrid_cloud_group(
        self,
        request: main_models.ModifyHybridCloudGroupRequest,
    ) -> main_models.ModifyHybridCloudGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_hybrid_cloud_group_with_options(request, runtime)

    async def modify_hybrid_cloud_group_async(
        self,
        request: main_models.ModifyHybridCloudGroupRequest,
    ) -> main_models.ModifyHybridCloudGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_hybrid_cloud_group_with_options_async(request, runtime)

    def modify_hybrid_cloud_group_expansion_server_with_options(
        self,
        request: main_models.ModifyHybridCloudGroupExpansionServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHybridCloudGroupExpansionServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mids):
            query['Mids'] = request.mids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHybridCloudGroupExpansionServer',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHybridCloudGroupExpansionServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hybrid_cloud_group_expansion_server_with_options_async(
        self,
        request: main_models.ModifyHybridCloudGroupExpansionServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHybridCloudGroupExpansionServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mids):
            query['Mids'] = request.mids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHybridCloudGroupExpansionServer',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHybridCloudGroupExpansionServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hybrid_cloud_group_expansion_server(
        self,
        request: main_models.ModifyHybridCloudGroupExpansionServerRequest,
    ) -> main_models.ModifyHybridCloudGroupExpansionServerResponse:
        runtime = RuntimeOptions()
        return self.modify_hybrid_cloud_group_expansion_server_with_options(request, runtime)

    async def modify_hybrid_cloud_group_expansion_server_async(
        self,
        request: main_models.ModifyHybridCloudGroupExpansionServerRequest,
    ) -> main_models.ModifyHybridCloudGroupExpansionServerResponse:
        runtime = RuntimeOptions()
        return await self.modify_hybrid_cloud_group_expansion_server_with_options_async(request, runtime)

    def modify_hybrid_cloud_group_shrink_server_with_options(
        self,
        request: main_models.ModifyHybridCloudGroupShrinkServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHybridCloudGroupShrinkServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mids):
            query['Mids'] = request.mids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHybridCloudGroupShrinkServer',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHybridCloudGroupShrinkServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hybrid_cloud_group_shrink_server_with_options_async(
        self,
        request: main_models.ModifyHybridCloudGroupShrinkServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHybridCloudGroupShrinkServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mids):
            query['Mids'] = request.mids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHybridCloudGroupShrinkServer',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHybridCloudGroupShrinkServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hybrid_cloud_group_shrink_server(
        self,
        request: main_models.ModifyHybridCloudGroupShrinkServerRequest,
    ) -> main_models.ModifyHybridCloudGroupShrinkServerResponse:
        runtime = RuntimeOptions()
        return self.modify_hybrid_cloud_group_shrink_server_with_options(request, runtime)

    async def modify_hybrid_cloud_group_shrink_server_async(
        self,
        request: main_models.ModifyHybridCloudGroupShrinkServerRequest,
    ) -> main_models.ModifyHybridCloudGroupShrinkServerResponse:
        runtime = RuntimeOptions()
        return await self.modify_hybrid_cloud_group_shrink_server_with_options_async(request, runtime)

    def modify_hybrid_cloud_sdk_pullin_status_with_options(
        self,
        request: main_models.ModifyHybridCloudSdkPullinStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHybridCloudSdkPullinStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mid):
            query['Mid'] = request.mid
        if not DaraCore.is_null(request.pullin_status):
            query['PullinStatus'] = request.pullin_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHybridCloudSdkPullinStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHybridCloudSdkPullinStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hybrid_cloud_sdk_pullin_status_with_options_async(
        self,
        request: main_models.ModifyHybridCloudSdkPullinStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHybridCloudSdkPullinStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mid):
            query['Mid'] = request.mid
        if not DaraCore.is_null(request.pullin_status):
            query['PullinStatus'] = request.pullin_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHybridCloudSdkPullinStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHybridCloudSdkPullinStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hybrid_cloud_sdk_pullin_status(
        self,
        request: main_models.ModifyHybridCloudSdkPullinStatusRequest,
    ) -> main_models.ModifyHybridCloudSdkPullinStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_hybrid_cloud_sdk_pullin_status_with_options(request, runtime)

    async def modify_hybrid_cloud_sdk_pullin_status_async(
        self,
        request: main_models.ModifyHybridCloudSdkPullinStatusRequest,
    ) -> main_models.ModifyHybridCloudSdkPullinStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_hybrid_cloud_sdk_pullin_status_with_options_async(request, runtime)

    def modify_hybrid_cloud_server_with_options(
        self,
        request: main_models.ModifyHybridCloudServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHybridCloudServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.continents):
            query['Continents'] = request.continents
        if not DaraCore.is_null(request.custom_name):
            query['CustomName'] = request.custom_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mid):
            query['Mid'] = request.mid
        if not DaraCore.is_null(request.operator):
            query['Operator'] = request.operator
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHybridCloudServer',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHybridCloudServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hybrid_cloud_server_with_options_async(
        self,
        request: main_models.ModifyHybridCloudServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHybridCloudServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.continents):
            query['Continents'] = request.continents
        if not DaraCore.is_null(request.custom_name):
            query['CustomName'] = request.custom_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mid):
            query['Mid'] = request.mid
        if not DaraCore.is_null(request.operator):
            query['Operator'] = request.operator
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHybridCloudServer',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHybridCloudServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hybrid_cloud_server(
        self,
        request: main_models.ModifyHybridCloudServerRequest,
    ) -> main_models.ModifyHybridCloudServerResponse:
        runtime = RuntimeOptions()
        return self.modify_hybrid_cloud_server_with_options(request, runtime)

    async def modify_hybrid_cloud_server_async(
        self,
        request: main_models.ModifyHybridCloudServerRequest,
    ) -> main_models.ModifyHybridCloudServerResponse:
        runtime = RuntimeOptions()
        return await self.modify_hybrid_cloud_server_with_options_async(request, runtime)

    def modify_log_delivery_config_with_options(
        self,
        request: main_models.ModifyLogDeliveryConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLogDeliveryConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_detail):
            query['DeliveryDetail'] = request.delivery_detail
        if not DaraCore.is_null(request.delivery_name):
            query['DeliveryName'] = request.delivery_name
        if not DaraCore.is_null(request.delivery_type):
            query['DeliveryType'] = request.delivery_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLogDeliveryConfig',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLogDeliveryConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_log_delivery_config_with_options_async(
        self,
        request: main_models.ModifyLogDeliveryConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLogDeliveryConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_detail):
            query['DeliveryDetail'] = request.delivery_detail
        if not DaraCore.is_null(request.delivery_name):
            query['DeliveryName'] = request.delivery_name
        if not DaraCore.is_null(request.delivery_type):
            query['DeliveryType'] = request.delivery_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLogDeliveryConfig',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLogDeliveryConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_log_delivery_config(
        self,
        request: main_models.ModifyLogDeliveryConfigRequest,
    ) -> main_models.ModifyLogDeliveryConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_log_delivery_config_with_options(request, runtime)

    async def modify_log_delivery_config_async(
        self,
        request: main_models.ModifyLogDeliveryConfigRequest,
    ) -> main_models.ModifyLogDeliveryConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_log_delivery_config_with_options_async(request, runtime)

    def modify_major_protection_black_ip_with_options(
        self,
        request: main_models.ModifyMajorProtectionBlackIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMajorProtectionBlackIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip_list):
            query['IpList'] = request.ip_list
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMajorProtectionBlackIp',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMajorProtectionBlackIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_major_protection_black_ip_with_options_async(
        self,
        request: main_models.ModifyMajorProtectionBlackIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMajorProtectionBlackIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ip_list):
            query['IpList'] = request.ip_list
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMajorProtectionBlackIp',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMajorProtectionBlackIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_major_protection_black_ip(
        self,
        request: main_models.ModifyMajorProtectionBlackIpRequest,
    ) -> main_models.ModifyMajorProtectionBlackIpResponse:
        runtime = RuntimeOptions()
        return self.modify_major_protection_black_ip_with_options(request, runtime)

    async def modify_major_protection_black_ip_async(
        self,
        request: main_models.ModifyMajorProtectionBlackIpRequest,
    ) -> main_models.ModifyMajorProtectionBlackIpResponse:
        runtime = RuntimeOptions()
        return await self.modify_major_protection_black_ip_with_options_async(request, runtime)

    def modify_member_account_with_options(
        self,
        request: main_models.ModifyMemberAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMemberAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.member_account_id):
            query['MemberAccountId'] = request.member_account_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMemberAccount',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMemberAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_member_account_with_options_async(
        self,
        request: main_models.ModifyMemberAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMemberAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.member_account_id):
            query['MemberAccountId'] = request.member_account_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMemberAccount',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMemberAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_member_account(
        self,
        request: main_models.ModifyMemberAccountRequest,
    ) -> main_models.ModifyMemberAccountResponse:
        runtime = RuntimeOptions()
        return self.modify_member_account_with_options(request, runtime)

    async def modify_member_account_async(
        self,
        request: main_models.ModifyMemberAccountRequest,
    ) -> main_models.ModifyMemberAccountResponse:
        runtime = RuntimeOptions()
        return await self.modify_member_account_with_options_async(request, runtime)

    def modify_pause_protection_status_with_options(
        self,
        request: main_models.ModifyPauseProtectionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPauseProtectionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.pause_status):
            query['PauseStatus'] = request.pause_status
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPauseProtectionStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPauseProtectionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_pause_protection_status_with_options_async(
        self,
        request: main_models.ModifyPauseProtectionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPauseProtectionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.pause_status):
            query['PauseStatus'] = request.pause_status
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPauseProtectionStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPauseProtectionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_pause_protection_status(
        self,
        request: main_models.ModifyPauseProtectionStatusRequest,
    ) -> main_models.ModifyPauseProtectionStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_pause_protection_status_with_options(request, runtime)

    async def modify_pause_protection_status_async(
        self,
        request: main_models.ModifyPauseProtectionStatusRequest,
    ) -> main_models.ModifyPauseProtectionStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_pause_protection_status_with_options_async(request, runtime)

    def modify_resource_log_delivery_status_with_options(
        self,
        request: main_models.ModifyResourceLogDeliveryStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyResourceLogDeliveryStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_name):
            query['DeliveryName'] = request.delivery_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyResourceLogDeliveryStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyResourceLogDeliveryStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_resource_log_delivery_status_with_options_async(
        self,
        request: main_models.ModifyResourceLogDeliveryStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyResourceLogDeliveryStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_name):
            query['DeliveryName'] = request.delivery_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyResourceLogDeliveryStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyResourceLogDeliveryStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_resource_log_delivery_status(
        self,
        request: main_models.ModifyResourceLogDeliveryStatusRequest,
    ) -> main_models.ModifyResourceLogDeliveryStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_resource_log_delivery_status_with_options(request, runtime)

    async def modify_resource_log_delivery_status_async(
        self,
        request: main_models.ModifyResourceLogDeliveryStatusRequest,
    ) -> main_models.ModifyResourceLogDeliveryStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_resource_log_delivery_status_with_options_async(request, runtime)

    def modify_resource_log_field_config_with_options(
        self,
        request: main_models.ModifyResourceLogFieldConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyResourceLogFieldConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_type):
            query['DeliveryType'] = request.delivery_type
        if not DaraCore.is_null(request.extend_config):
            query['ExtendConfig'] = request.extend_config
        if not DaraCore.is_null(request.field_list):
            query['FieldList'] = request.field_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.log_delivery_strategy):
            query['LogDeliveryStrategy'] = request.log_delivery_strategy
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyResourceLogFieldConfig',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyResourceLogFieldConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_resource_log_field_config_with_options_async(
        self,
        request: main_models.ModifyResourceLogFieldConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyResourceLogFieldConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_type):
            query['DeliveryType'] = request.delivery_type
        if not DaraCore.is_null(request.extend_config):
            query['ExtendConfig'] = request.extend_config
        if not DaraCore.is_null(request.field_list):
            query['FieldList'] = request.field_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.log_delivery_strategy):
            query['LogDeliveryStrategy'] = request.log_delivery_strategy
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyResourceLogFieldConfig',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyResourceLogFieldConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_resource_log_field_config(
        self,
        request: main_models.ModifyResourceLogFieldConfigRequest,
    ) -> main_models.ModifyResourceLogFieldConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_resource_log_field_config_with_options(request, runtime)

    async def modify_resource_log_field_config_async(
        self,
        request: main_models.ModifyResourceLogFieldConfigRequest,
    ) -> main_models.ModifyResourceLogFieldConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_resource_log_field_config_with_options_async(request, runtime)

    def modify_resource_log_status_with_options(
        self,
        request: main_models.ModifyResourceLogStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyResourceLogStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyResourceLogStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyResourceLogStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_resource_log_status_with_options_async(
        self,
        request: main_models.ModifyResourceLogStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyResourceLogStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyResourceLogStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyResourceLogStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_resource_log_status(
        self,
        request: main_models.ModifyResourceLogStatusRequest,
    ) -> main_models.ModifyResourceLogStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_resource_log_status_with_options(request, runtime)

    async def modify_resource_log_status_async(
        self,
        request: main_models.ModifyResourceLogStatusRequest,
    ) -> main_models.ModifyResourceLogStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_resource_log_status_with_options_async(request, runtime)

    def modify_template_resources_with_options(
        self,
        request: main_models.ModifyTemplateResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTemplateResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bind_assets):
            query['BindAssets'] = request.bind_assets
        if not DaraCore.is_null(request.bind_resource_groups):
            query['BindResourceGroups'] = request.bind_resource_groups
        if not DaraCore.is_null(request.bind_resources):
            query['BindResources'] = request.bind_resources
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.unbind_assets):
            query['UnbindAssets'] = request.unbind_assets
        if not DaraCore.is_null(request.unbind_resource_groups):
            query['UnbindResourceGroups'] = request.unbind_resource_groups
        if not DaraCore.is_null(request.unbind_resources):
            query['UnbindResources'] = request.unbind_resources
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTemplateResources',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTemplateResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_template_resources_with_options_async(
        self,
        request: main_models.ModifyTemplateResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTemplateResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bind_assets):
            query['BindAssets'] = request.bind_assets
        if not DaraCore.is_null(request.bind_resource_groups):
            query['BindResourceGroups'] = request.bind_resource_groups
        if not DaraCore.is_null(request.bind_resources):
            query['BindResources'] = request.bind_resources
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.unbind_assets):
            query['UnbindAssets'] = request.unbind_assets
        if not DaraCore.is_null(request.unbind_resource_groups):
            query['UnbindResourceGroups'] = request.unbind_resource_groups
        if not DaraCore.is_null(request.unbind_resources):
            query['UnbindResources'] = request.unbind_resources
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTemplateResources',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTemplateResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_template_resources(
        self,
        request: main_models.ModifyTemplateResourcesRequest,
    ) -> main_models.ModifyTemplateResourcesResponse:
        runtime = RuntimeOptions()
        return self.modify_template_resources_with_options(request, runtime)

    async def modify_template_resources_async(
        self,
        request: main_models.ModifyTemplateResourcesRequest,
    ) -> main_models.ModifyTemplateResourcesResponse:
        runtime = RuntimeOptions()
        return await self.modify_template_resources_with_options_async(request, runtime)

    def modify_user_log_field_config_with_options(
        self,
        request: main_models.ModifyUserLogFieldConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserLogFieldConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_type):
            query['DeliveryType'] = request.delivery_type
        if not DaraCore.is_null(request.extend_config):
            query['ExtendConfig'] = request.extend_config
        if not DaraCore.is_null(request.field_list):
            query['FieldList'] = request.field_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.log_delivery_strategy):
            query['LogDeliveryStrategy'] = request.log_delivery_strategy
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUserLogFieldConfig',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserLogFieldConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_log_field_config_with_options_async(
        self,
        request: main_models.ModifyUserLogFieldConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserLogFieldConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_type):
            query['DeliveryType'] = request.delivery_type
        if not DaraCore.is_null(request.extend_config):
            query['ExtendConfig'] = request.extend_config
        if not DaraCore.is_null(request.field_list):
            query['FieldList'] = request.field_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.log_delivery_strategy):
            query['LogDeliveryStrategy'] = request.log_delivery_strategy
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUserLogFieldConfig',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserLogFieldConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user_log_field_config(
        self,
        request: main_models.ModifyUserLogFieldConfigRequest,
    ) -> main_models.ModifyUserLogFieldConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_user_log_field_config_with_options(request, runtime)

    async def modify_user_log_field_config_async(
        self,
        request: main_models.ModifyUserLogFieldConfigRequest,
    ) -> main_models.ModifyUserLogFieldConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_user_log_field_config_with_options_async(request, runtime)

    def modify_user_waf_log_status_with_options(
        self,
        request: main_models.ModifyUserWafLogStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserWafLogStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.log_region_id):
            query['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.log_status):
            query['LogStatus'] = request.log_status
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUserWafLogStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserWafLogStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_waf_log_status_with_options_async(
        self,
        request: main_models.ModifyUserWafLogStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserWafLogStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.log_region_id):
            query['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.log_status):
            query['LogStatus'] = request.log_status
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUserWafLogStatus',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserWafLogStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user_waf_log_status(
        self,
        request: main_models.ModifyUserWafLogStatusRequest,
    ) -> main_models.ModifyUserWafLogStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_user_waf_log_status_with_options(request, runtime)

    async def modify_user_waf_log_status_async(
        self,
        request: main_models.ModifyUserWafLogStatusRequest,
    ) -> main_models.ModifyUserWafLogStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_user_waf_log_status_with_options_async(request, runtime)

    def re_create_cloud_resource_with_options(
        self,
        request: main_models.ReCreateCloudResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReCreateCloudResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cloud_resource_id):
            query['CloudResourceId'] = request.cloud_resource_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_product):
            query['ResourceProduct'] = request.resource_product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReCreateCloudResource',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReCreateCloudResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def re_create_cloud_resource_with_options_async(
        self,
        request: main_models.ReCreateCloudResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReCreateCloudResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cloud_resource_id):
            query['CloudResourceId'] = request.cloud_resource_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        if not DaraCore.is_null(request.resource_product):
            query['ResourceProduct'] = request.resource_product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReCreateCloudResource',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReCreateCloudResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def re_create_cloud_resource(
        self,
        request: main_models.ReCreateCloudResourceRequest,
    ) -> main_models.ReCreateCloudResourceResponse:
        runtime = RuntimeOptions()
        return self.re_create_cloud_resource_with_options(request, runtime)

    async def re_create_cloud_resource_async(
        self,
        request: main_models.ReCreateCloudResourceRequest,
    ) -> main_models.ReCreateCloudResourceResponse:
        runtime = RuntimeOptions()
        return await self.re_create_cloud_resource_with_options_async(request, runtime)

    def release_instance_with_options(
        self,
        request: main_models.ReleaseInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseInstance',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_instance_with_options_async(
        self,
        request: main_models.ReleaseInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseInstance',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
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
        return self.release_instance_with_options(request, runtime)

    async def release_instance_async(
        self,
        request: main_models.ReleaseInstanceRequest,
    ) -> main_models.ReleaseInstanceResponse:
        runtime = RuntimeOptions()
        return await self.release_instance_with_options_async(request, runtime)

    def sync_product_instance_with_options(
        self,
        request: main_models.SyncProductInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncProductInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SyncProductInstance',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncProductInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_product_instance_with_options_async(
        self,
        request: main_models.SyncProductInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncProductInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_manager_resource_group_id):
            query['ResourceManagerResourceGroupId'] = request.resource_manager_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SyncProductInstance',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncProductInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_product_instance(
        self,
        request: main_models.SyncProductInstanceRequest,
    ) -> main_models.SyncProductInstanceResponse:
        runtime = RuntimeOptions()
        return self.sync_product_instance_with_options(request, runtime)

    async def sync_product_instance_async(
        self,
        request: main_models.SyncProductInstanceRequest,
    ) -> main_models.SyncProductInstanceResponse:
        runtime = RuntimeOptions()
        return await self.sync_product_instance_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2021-10-01',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2021-10-01',
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
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2021-10-01',
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
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2021-10-01',
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

    def verify_domain_owner_with_options(
        self,
        request: main_models.VerifyDomainOwnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyDomainOwnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyDomainOwner',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyDomainOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_domain_owner_with_options_async(
        self,
        request: main_models.VerifyDomainOwnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyDomainOwnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyDomainOwner',
            version = '2021-10-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyDomainOwnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_domain_owner(
        self,
        request: main_models.VerifyDomainOwnerRequest,
    ) -> main_models.VerifyDomainOwnerResponse:
        runtime = RuntimeOptions()
        return self.verify_domain_owner_with_options(request, runtime)

    async def verify_domain_owner_async(
        self,
        request: main_models.VerifyDomainOwnerRequest,
    ) -> main_models.VerifyDomainOwnerResponse:
        runtime = RuntimeOptions()
        return await self.verify_domain_owner_with_options_async(request, runtime)
