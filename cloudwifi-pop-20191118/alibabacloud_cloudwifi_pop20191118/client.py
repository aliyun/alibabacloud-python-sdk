# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cloudwifi_pop20191118 import models as main_models
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
        self._endpoint_map = {
            'cn-hangzhou': 'cloudwf.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('cloudwifi-pop', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_ap_list_to_apgroup_with_options(
        self,
        tmp_req: main_models.AddApListToApgroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddApListToApgroupResponse:
        tmp_req.validate()
        request = main_models.AddApListToApgroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ap_mac_list):
            request.ap_mac_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.ap_mac_list, 'ApMacList', 'json')
        query = {}
        if not DaraCore.is_null(request.ap_group_id):
            query['ApGroupId'] = request.ap_group_id
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        body = {}
        if not DaraCore.is_null(request.ap_mac_list_shrink):
            body['ApMacList'] = request.ap_mac_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddApListToApgroup',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddApListToApgroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_ap_list_to_apgroup_with_options_async(
        self,
        tmp_req: main_models.AddApListToApgroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddApListToApgroupResponse:
        tmp_req.validate()
        request = main_models.AddApListToApgroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ap_mac_list):
            request.ap_mac_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.ap_mac_list, 'ApMacList', 'json')
        query = {}
        if not DaraCore.is_null(request.ap_group_id):
            query['ApGroupId'] = request.ap_group_id
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        body = {}
        if not DaraCore.is_null(request.ap_mac_list_shrink):
            body['ApMacList'] = request.ap_mac_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddApListToApgroup',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddApListToApgroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_ap_list_to_apgroup(
        self,
        request: main_models.AddApListToApgroupRequest,
    ) -> main_models.AddApListToApgroupResponse:
        runtime = RuntimeOptions()
        return self.add_ap_list_to_apgroup_with_options(request, runtime)

    async def add_ap_list_to_apgroup_async(
        self,
        request: main_models.AddApListToApgroupRequest,
    ) -> main_models.AddApListToApgroupResponse:
        runtime = RuntimeOptions()
        return await self.add_ap_list_to_apgroup_with_options_async(request, runtime)

    def del_ap_third_app_with_options(
        self,
        request: main_models.DelApThirdAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DelApThirdAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_asset_id):
            query['ApAssetId'] = request.ap_asset_id
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.mac):
            query['Mac'] = request.mac
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DelApThirdApp',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DelApThirdAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def del_ap_third_app_with_options_async(
        self,
        request: main_models.DelApThirdAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DelApThirdAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_asset_id):
            query['ApAssetId'] = request.ap_asset_id
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.mac):
            query['Mac'] = request.mac
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DelApThirdApp',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DelApThirdAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def del_ap_third_app(
        self,
        request: main_models.DelApThirdAppRequest,
    ) -> main_models.DelApThirdAppResponse:
        runtime = RuntimeOptions()
        return self.del_ap_third_app_with_options(request, runtime)

    async def del_ap_third_app_async(
        self,
        request: main_models.DelApThirdAppRequest,
    ) -> main_models.DelApThirdAppResponse:
        runtime = RuntimeOptions()
        return await self.del_ap_third_app_with_options_async(request, runtime)

    def delete_ap_ssid_config_with_options(
        self,
        request: main_models.DeleteApSsidConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApSsidConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.radio_index):
            query['RadioIndex'] = request.radio_index
        if not DaraCore.is_null(request.ssid):
            query['Ssid'] = request.ssid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApSsidConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApSsidConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ap_ssid_config_with_options_async(
        self,
        request: main_models.DeleteApSsidConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApSsidConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.radio_index):
            query['RadioIndex'] = request.radio_index
        if not DaraCore.is_null(request.ssid):
            query['Ssid'] = request.ssid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApSsidConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApSsidConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ap_ssid_config(
        self,
        request: main_models.DeleteApSsidConfigRequest,
    ) -> main_models.DeleteApSsidConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_ap_ssid_config_with_options(request, runtime)

    async def delete_ap_ssid_config_async(
        self,
        request: main_models.DeleteApSsidConfigRequest,
    ) -> main_models.DeleteApSsidConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_ap_ssid_config_with_options_async(request, runtime)

    def delete_apgroup_config_with_options(
        self,
        request: main_models.DeleteApgroupConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApgroupConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_group_uuid):
            query['ApGroupUUId'] = request.ap_group_uuid
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApgroupConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApgroupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_apgroup_config_with_options_async(
        self,
        request: main_models.DeleteApgroupConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApgroupConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_group_uuid):
            query['ApGroupUUId'] = request.ap_group_uuid
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApgroupConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApgroupConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_apgroup_config(
        self,
        request: main_models.DeleteApgroupConfigRequest,
    ) -> main_models.DeleteApgroupConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_apgroup_config_with_options(request, runtime)

    async def delete_apgroup_config_async(
        self,
        request: main_models.DeleteApgroupConfigRequest,
    ) -> main_models.DeleteApgroupConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_apgroup_config_with_options_async(request, runtime)

    def delete_apgroup_ssid_config_with_options(
        self,
        request: main_models.DeleteApgroupSsidConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApgroupSsidConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApgroupSsidConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApgroupSsidConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_apgroup_ssid_config_with_options_async(
        self,
        request: main_models.DeleteApgroupSsidConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApgroupSsidConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApgroupSsidConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApgroupSsidConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_apgroup_ssid_config(
        self,
        request: main_models.DeleteApgroupSsidConfigRequest,
    ) -> main_models.DeleteApgroupSsidConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_apgroup_ssid_config_with_options(request, runtime)

    async def delete_apgroup_ssid_config_async(
        self,
        request: main_models.DeleteApgroupSsidConfigRequest,
    ) -> main_models.DeleteApgroupSsidConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_apgroup_ssid_config_with_options_async(request, runtime)

    def delete_apgroup_third_app_with_options(
        self,
        request: main_models.DeleteApgroupThirdAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApgroupThirdAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApgroupThirdApp',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApgroupThirdAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_apgroup_third_app_with_options_async(
        self,
        request: main_models.DeleteApgroupThirdAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApgroupThirdAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApgroupThirdApp',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApgroupThirdAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_apgroup_third_app(
        self,
        request: main_models.DeleteApgroupThirdAppRequest,
    ) -> main_models.DeleteApgroupThirdAppResponse:
        runtime = RuntimeOptions()
        return self.delete_apgroup_third_app_with_options(request, runtime)

    async def delete_apgroup_third_app_async(
        self,
        request: main_models.DeleteApgroupThirdAppRequest,
    ) -> main_models.DeleteApgroupThirdAppResponse:
        runtime = RuntimeOptions()
        return await self.delete_apgroup_third_app_with_options_async(request, runtime)

    def delete_net_device_info_with_options(
        self,
        request: main_models.DeleteNetDeviceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNetDeviceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNetDeviceInfo',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNetDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_net_device_info_with_options_async(
        self,
        request: main_models.DeleteNetDeviceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNetDeviceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNetDeviceInfo',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNetDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_net_device_info(
        self,
        request: main_models.DeleteNetDeviceInfoRequest,
    ) -> main_models.DeleteNetDeviceInfoResponse:
        runtime = RuntimeOptions()
        return self.delete_net_device_info_with_options(request, runtime)

    async def delete_net_device_info_async(
        self,
        request: main_models.DeleteNetDeviceInfoRequest,
    ) -> main_models.DeleteNetDeviceInfoResponse:
        runtime = RuntimeOptions()
        return await self.delete_net_device_info_with_options_async(request, runtime)

    def edit_apgroup_third_app_with_options(
        self,
        request: main_models.EditApgroupThirdAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditApgroupThirdAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_data):
            query['AppData'] = request.app_data
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.apply_to_sub_group):
            query['ApplyToSubGroup'] = request.apply_to_sub_group
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.config_type):
            query['ConfigType'] = request.config_type
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.inherit_parent_group):
            query['InheritParentGroup'] = request.inherit_parent_group
        if not DaraCore.is_null(request.third_app_name):
            query['ThirdAppName'] = request.third_app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EditApgroupThirdApp',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditApgroupThirdAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_apgroup_third_app_with_options_async(
        self,
        request: main_models.EditApgroupThirdAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditApgroupThirdAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_data):
            query['AppData'] = request.app_data
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.apply_to_sub_group):
            query['ApplyToSubGroup'] = request.apply_to_sub_group
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.config_type):
            query['ConfigType'] = request.config_type
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.inherit_parent_group):
            query['InheritParentGroup'] = request.inherit_parent_group
        if not DaraCore.is_null(request.third_app_name):
            query['ThirdAppName'] = request.third_app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EditApgroupThirdApp',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditApgroupThirdAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_apgroup_third_app(
        self,
        request: main_models.EditApgroupThirdAppRequest,
    ) -> main_models.EditApgroupThirdAppResponse:
        runtime = RuntimeOptions()
        return self.edit_apgroup_third_app_with_options(request, runtime)

    async def edit_apgroup_third_app_async(
        self,
        request: main_models.EditApgroupThirdAppRequest,
    ) -> main_models.EditApgroupThirdAppResponse:
        runtime = RuntimeOptions()
        return await self.edit_apgroup_third_app_with_options_async(request, runtime)

    def effect_ap_config_with_options(
        self,
        request: main_models.EffectApConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EffectApConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EffectApConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EffectApConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def effect_ap_config_with_options_async(
        self,
        request: main_models.EffectApConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EffectApConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EffectApConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EffectApConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def effect_ap_config(
        self,
        request: main_models.EffectApConfigRequest,
    ) -> main_models.EffectApConfigResponse:
        runtime = RuntimeOptions()
        return self.effect_ap_config_with_options(request, runtime)

    async def effect_ap_config_async(
        self,
        request: main_models.EffectApConfigRequest,
    ) -> main_models.EffectApConfigResponse:
        runtime = RuntimeOptions()
        return await self.effect_ap_config_with_options_async(request, runtime)

    def effect_apgroup_config_with_options(
        self,
        request: main_models.EffectApgroupConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EffectApgroupConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_group_uuid):
            query['ApGroupUUId'] = request.ap_group_uuid
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EffectApgroupConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EffectApgroupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def effect_apgroup_config_with_options_async(
        self,
        request: main_models.EffectApgroupConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EffectApgroupConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_group_uuid):
            query['ApGroupUUId'] = request.ap_group_uuid
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EffectApgroupConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EffectApgroupConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def effect_apgroup_config(
        self,
        request: main_models.EffectApgroupConfigRequest,
    ) -> main_models.EffectApgroupConfigResponse:
        runtime = RuntimeOptions()
        return self.effect_apgroup_config_with_options(request, runtime)

    async def effect_apgroup_config_async(
        self,
        request: main_models.EffectApgroupConfigRequest,
    ) -> main_models.EffectApgroupConfigResponse:
        runtime = RuntimeOptions()
        return await self.effect_apgroup_config_with_options_async(request, runtime)

    def get_ant_sta_status_by_mac_with_options(
        self,
        request: main_models.GetAntStaStatusByMacRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAntStaStatusByMacResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.sta_mac):
            query['StaMac'] = request.sta_mac
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAntStaStatusByMac',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAntStaStatusByMacResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ant_sta_status_by_mac_with_options_async(
        self,
        request: main_models.GetAntStaStatusByMacRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAntStaStatusByMacResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.sta_mac):
            query['StaMac'] = request.sta_mac
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAntStaStatusByMac',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAntStaStatusByMacResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ant_sta_status_by_mac(
        self,
        request: main_models.GetAntStaStatusByMacRequest,
    ) -> main_models.GetAntStaStatusByMacResponse:
        runtime = RuntimeOptions()
        return self.get_ant_sta_status_by_mac_with_options(request, runtime)

    async def get_ant_sta_status_by_mac_async(
        self,
        request: main_models.GetAntStaStatusByMacRequest,
    ) -> main_models.GetAntStaStatusByMacResponse:
        runtime = RuntimeOptions()
        return await self.get_ant_sta_status_by_mac_with_options_async(request, runtime)

    def get_ap_address_by_mac_with_options(
        self,
        request: main_models.GetApAddressByMacRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApAddressByMacResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.mac):
            query['Mac'] = request.mac
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApAddressByMac',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApAddressByMacResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ap_address_by_mac_with_options_async(
        self,
        request: main_models.GetApAddressByMacRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApAddressByMacResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.mac):
            query['Mac'] = request.mac
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApAddressByMac',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApAddressByMacResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ap_address_by_mac(
        self,
        request: main_models.GetApAddressByMacRequest,
    ) -> main_models.GetApAddressByMacResponse:
        runtime = RuntimeOptions()
        return self.get_ap_address_by_mac_with_options(request, runtime)

    async def get_ap_address_by_mac_async(
        self,
        request: main_models.GetApAddressByMacRequest,
    ) -> main_models.GetApAddressByMacResponse:
        runtime = RuntimeOptions()
        return await self.get_ap_address_by_mac_with_options_async(request, runtime)

    def get_ap_asset_with_options(
        self,
        request: main_models.GetApAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApAssetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApAsset',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ap_asset_with_options_async(
        self,
        request: main_models.GetApAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApAssetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApAsset',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ap_asset(
        self,
        request: main_models.GetApAssetRequest,
    ) -> main_models.GetApAssetResponse:
        runtime = RuntimeOptions()
        return self.get_ap_asset_with_options(request, runtime)

    async def get_ap_asset_async(
        self,
        request: main_models.GetApAssetRequest,
    ) -> main_models.GetApAssetResponse:
        runtime = RuntimeOptions()
        return await self.get_ap_asset_with_options_async(request, runtime)

    def get_ap_detail_status_with_options(
        self,
        request: main_models.GetApDetailStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApDetailStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mac):
            query['Mac'] = request.mac
        if not DaraCore.is_null(request.need_apgroup_info):
            query['NeedApgroupInfo'] = request.need_apgroup_info
        if not DaraCore.is_null(request.need_radio_status):
            query['NeedRadioStatus'] = request.need_radio_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApDetailStatus',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApDetailStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ap_detail_status_with_options_async(
        self,
        request: main_models.GetApDetailStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApDetailStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.mac):
            query['Mac'] = request.mac
        if not DaraCore.is_null(request.need_apgroup_info):
            query['NeedApgroupInfo'] = request.need_apgroup_info
        if not DaraCore.is_null(request.need_radio_status):
            query['NeedRadioStatus'] = request.need_radio_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApDetailStatus',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApDetailStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ap_detail_status(
        self,
        request: main_models.GetApDetailStatusRequest,
    ) -> main_models.GetApDetailStatusResponse:
        runtime = RuntimeOptions()
        return self.get_ap_detail_status_with_options(request, runtime)

    async def get_ap_detail_status_async(
        self,
        request: main_models.GetApDetailStatusRequest,
    ) -> main_models.GetApDetailStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_ap_detail_status_with_options_async(request, runtime)

    def get_ap_detailed_config_with_options(
        self,
        request: main_models.GetApDetailedConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApDetailedConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApDetailedConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApDetailedConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ap_detailed_config_with_options_async(
        self,
        request: main_models.GetApDetailedConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApDetailedConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApDetailedConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApDetailedConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ap_detailed_config(
        self,
        request: main_models.GetApDetailedConfigRequest,
    ) -> main_models.GetApDetailedConfigResponse:
        runtime = RuntimeOptions()
        return self.get_ap_detailed_config_with_options(request, runtime)

    async def get_ap_detailed_config_async(
        self,
        request: main_models.GetApDetailedConfigRequest,
    ) -> main_models.GetApDetailedConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_ap_detailed_config_with_options_async(request, runtime)

    def get_ap_info_from_pool_with_options(
        self,
        request: main_models.GetApInfoFromPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApInfoFromPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApInfoFromPool',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApInfoFromPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ap_info_from_pool_with_options_async(
        self,
        request: main_models.GetApInfoFromPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApInfoFromPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApInfoFromPool',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApInfoFromPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ap_info_from_pool(
        self,
        request: main_models.GetApInfoFromPoolRequest,
    ) -> main_models.GetApInfoFromPoolResponse:
        runtime = RuntimeOptions()
        return self.get_ap_info_from_pool_with_options(request, runtime)

    async def get_ap_info_from_pool_async(
        self,
        request: main_models.GetApInfoFromPoolRequest,
    ) -> main_models.GetApInfoFromPoolResponse:
        runtime = RuntimeOptions()
        return await self.get_ap_info_from_pool_with_options_async(request, runtime)

    def get_ap_run_history_time_ser_with_options(
        self,
        request: main_models.GetApRunHistoryTimeSerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApRunHistoryTimeSerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.end):
            query['End'] = request.end
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApRunHistoryTimeSer',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApRunHistoryTimeSerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ap_run_history_time_ser_with_options_async(
        self,
        request: main_models.GetApRunHistoryTimeSerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApRunHistoryTimeSerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.end):
            query['End'] = request.end
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApRunHistoryTimeSer',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApRunHistoryTimeSerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ap_run_history_time_ser(
        self,
        request: main_models.GetApRunHistoryTimeSerRequest,
    ) -> main_models.GetApRunHistoryTimeSerResponse:
        runtime = RuntimeOptions()
        return self.get_ap_run_history_time_ser_with_options(request, runtime)

    async def get_ap_run_history_time_ser_async(
        self,
        request: main_models.GetApRunHistoryTimeSerRequest,
    ) -> main_models.GetApRunHistoryTimeSerResponse:
        runtime = RuntimeOptions()
        return await self.get_ap_run_history_time_ser_with_options_async(request, runtime)

    def get_ap_status_by_group_id_with_options(
        self,
        request: main_models.GetApStatusByGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApStatusByGroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cursor):
            query['Cursor'] = request.cursor
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApStatusByGroupId',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApStatusByGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ap_status_by_group_id_with_options_async(
        self,
        request: main_models.GetApStatusByGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApStatusByGroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cursor):
            query['Cursor'] = request.cursor
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApStatusByGroupId',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApStatusByGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ap_status_by_group_id(
        self,
        request: main_models.GetApStatusByGroupIdRequest,
    ) -> main_models.GetApStatusByGroupIdResponse:
        runtime = RuntimeOptions()
        return self.get_ap_status_by_group_id_with_options(request, runtime)

    async def get_ap_status_by_group_id_async(
        self,
        request: main_models.GetApStatusByGroupIdRequest,
    ) -> main_models.GetApStatusByGroupIdResponse:
        runtime = RuntimeOptions()
        return await self.get_ap_status_by_group_id_with_options_async(request, runtime)

    def get_apgroup_config_by_identity_with_options(
        self,
        request: main_models.GetApgroupConfigByIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApgroupConfigByIdentityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not DaraCore.is_null(request.apgroup_uuid):
            query['ApgroupUuid'] = request.apgroup_uuid
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApgroupConfigByIdentity',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApgroupConfigByIdentityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_apgroup_config_by_identity_with_options_async(
        self,
        request: main_models.GetApgroupConfigByIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApgroupConfigByIdentityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not DaraCore.is_null(request.apgroup_uuid):
            query['ApgroupUuid'] = request.apgroup_uuid
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApgroupConfigByIdentity',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApgroupConfigByIdentityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_apgroup_config_by_identity(
        self,
        request: main_models.GetApgroupConfigByIdentityRequest,
    ) -> main_models.GetApgroupConfigByIdentityResponse:
        runtime = RuntimeOptions()
        return self.get_apgroup_config_by_identity_with_options(request, runtime)

    async def get_apgroup_config_by_identity_async(
        self,
        request: main_models.GetApgroupConfigByIdentityRequest,
    ) -> main_models.GetApgroupConfigByIdentityResponse:
        runtime = RuntimeOptions()
        return await self.get_apgroup_config_by_identity_with_options_async(request, runtime)

    def get_apgroup_detailed_config_with_options(
        self,
        request: main_models.GetApgroupDetailedConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApgroupDetailedConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not DaraCore.is_null(request.apgroup_uuid):
            query['ApgroupUuid'] = request.apgroup_uuid
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApgroupDetailedConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApgroupDetailedConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_apgroup_detailed_config_with_options_async(
        self,
        request: main_models.GetApgroupDetailedConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApgroupDetailedConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not DaraCore.is_null(request.apgroup_uuid):
            query['ApgroupUuid'] = request.apgroup_uuid
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApgroupDetailedConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApgroupDetailedConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_apgroup_detailed_config(
        self,
        request: main_models.GetApgroupDetailedConfigRequest,
    ) -> main_models.GetApgroupDetailedConfigResponse:
        runtime = RuntimeOptions()
        return self.get_apgroup_detailed_config_with_options(request, runtime)

    async def get_apgroup_detailed_config_async(
        self,
        request: main_models.GetApgroupDetailedConfigRequest,
    ) -> main_models.GetApgroupDetailedConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_apgroup_detailed_config_with_options_async(request, runtime)

    def get_apgroup_id_with_options(
        self,
        request: main_models.GetApgroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApgroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApgroupId',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApgroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_apgroup_id_with_options_async(
        self,
        request: main_models.GetApgroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApgroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApgroupId',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApgroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_apgroup_id(
        self,
        request: main_models.GetApgroupIdRequest,
    ) -> main_models.GetApgroupIdResponse:
        runtime = RuntimeOptions()
        return self.get_apgroup_id_with_options(request, runtime)

    async def get_apgroup_id_async(
        self,
        request: main_models.GetApgroupIdRequest,
    ) -> main_models.GetApgroupIdResponse:
        runtime = RuntimeOptions()
        return await self.get_apgroup_id_with_options_async(request, runtime)

    def get_apgroup_ssid_config_with_options(
        self,
        request: main_models.GetApgroupSsidConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApgroupSsidConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_group_uuid):
            query['ApGroupUUId'] = request.ap_group_uuid
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApgroupSsidConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApgroupSsidConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_apgroup_ssid_config_with_options_async(
        self,
        request: main_models.GetApgroupSsidConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApgroupSsidConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_group_uuid):
            query['ApGroupUUId'] = request.ap_group_uuid
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApgroupSsidConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApgroupSsidConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_apgroup_ssid_config(
        self,
        request: main_models.GetApgroupSsidConfigRequest,
    ) -> main_models.GetApgroupSsidConfigResponse:
        runtime = RuntimeOptions()
        return self.get_apgroup_ssid_config_with_options(request, runtime)

    async def get_apgroup_ssid_config_async(
        self,
        request: main_models.GetApgroupSsidConfigRequest,
    ) -> main_models.GetApgroupSsidConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_apgroup_ssid_config_with_options_async(request, runtime)

    def get_batch_task_progress_with_options(
        self,
        request: main_models.GetBatchTaskProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBatchTaskProgressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBatchTaskProgress',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBatchTaskProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_batch_task_progress_with_options_async(
        self,
        request: main_models.GetBatchTaskProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBatchTaskProgressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBatchTaskProgress',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBatchTaskProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_batch_task_progress(
        self,
        request: main_models.GetBatchTaskProgressRequest,
    ) -> main_models.GetBatchTaskProgressResponse:
        runtime = RuntimeOptions()
        return self.get_batch_task_progress_with_options(request, runtime)

    async def get_batch_task_progress_async(
        self,
        request: main_models.GetBatchTaskProgressRequest,
    ) -> main_models.GetBatchTaskProgressResponse:
        runtime = RuntimeOptions()
        return await self.get_batch_task_progress_with_options_async(request, runtime)

    def get_group_misc_agg_time_ser_with_options(
        self,
        request: main_models.GetGroupMiscAggTimeSerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGroupMiscAggTimeSerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apgroup_uuid):
            query['ApgroupUuid'] = request.apgroup_uuid
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.end):
            query['End'] = request.end
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGroupMiscAggTimeSer',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGroupMiscAggTimeSerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_group_misc_agg_time_ser_with_options_async(
        self,
        request: main_models.GetGroupMiscAggTimeSerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGroupMiscAggTimeSerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apgroup_uuid):
            query['ApgroupUuid'] = request.apgroup_uuid
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.end):
            query['End'] = request.end
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGroupMiscAggTimeSer',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGroupMiscAggTimeSerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_group_misc_agg_time_ser(
        self,
        request: main_models.GetGroupMiscAggTimeSerRequest,
    ) -> main_models.GetGroupMiscAggTimeSerResponse:
        runtime = RuntimeOptions()
        return self.get_group_misc_agg_time_ser_with_options(request, runtime)

    async def get_group_misc_agg_time_ser_async(
        self,
        request: main_models.GetGroupMiscAggTimeSerRequest,
    ) -> main_models.GetGroupMiscAggTimeSerResponse:
        runtime = RuntimeOptions()
        return await self.get_group_misc_agg_time_ser_with_options_async(request, runtime)

    def get_net_device_info_with_options(
        self,
        request: main_models.GetNetDeviceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNetDeviceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cursor):
            query['Cursor'] = request.cursor
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.idc):
            query['Idc'] = request.idc
        if not DaraCore.is_null(request.logic_net_pod):
            query['LogicNetPod'] = request.logic_net_pod
        if not DaraCore.is_null(request.manufacturer):
            query['Manufacturer'] = request.manufacturer
        if not DaraCore.is_null(request.mgn_ip):
            query['MgnIp'] = request.mgn_ip
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.net_pod):
            query['NetPod'] = request.net_pod
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        if not DaraCore.is_null(request.service_tag):
            query['ServiceTag'] = request.service_tag
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNetDeviceInfo',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNetDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_net_device_info_with_options_async(
        self,
        request: main_models.GetNetDeviceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNetDeviceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cursor):
            query['Cursor'] = request.cursor
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.idc):
            query['Idc'] = request.idc
        if not DaraCore.is_null(request.logic_net_pod):
            query['LogicNetPod'] = request.logic_net_pod
        if not DaraCore.is_null(request.manufacturer):
            query['Manufacturer'] = request.manufacturer
        if not DaraCore.is_null(request.mgn_ip):
            query['MgnIp'] = request.mgn_ip
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.net_pod):
            query['NetPod'] = request.net_pod
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        if not DaraCore.is_null(request.service_tag):
            query['ServiceTag'] = request.service_tag
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNetDeviceInfo',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNetDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_net_device_info(
        self,
        request: main_models.GetNetDeviceInfoRequest,
    ) -> main_models.GetNetDeviceInfoResponse:
        runtime = RuntimeOptions()
        return self.get_net_device_info_with_options(request, runtime)

    async def get_net_device_info_async(
        self,
        request: main_models.GetNetDeviceInfoRequest,
    ) -> main_models.GetNetDeviceInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_net_device_info_with_options_async(request, runtime)

    def get_net_device_info_with_size_with_options(
        self,
        request: main_models.GetNetDeviceInfoWithSizeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNetDeviceInfoWithSizeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cursor):
            query['Cursor'] = request.cursor
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.idc):
            query['Idc'] = request.idc
        if not DaraCore.is_null(request.logic_net_pod):
            query['LogicNetPod'] = request.logic_net_pod
        if not DaraCore.is_null(request.manufacturer):
            query['Manufacturer'] = request.manufacturer
        if not DaraCore.is_null(request.mgn_ip):
            query['MgnIp'] = request.mgn_ip
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.net_pod):
            query['NetPod'] = request.net_pod
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        if not DaraCore.is_null(request.service_tag):
            query['ServiceTag'] = request.service_tag
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNetDeviceInfoWithSize',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNetDeviceInfoWithSizeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_net_device_info_with_size_with_options_async(
        self,
        request: main_models.GetNetDeviceInfoWithSizeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNetDeviceInfoWithSizeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cursor):
            query['Cursor'] = request.cursor
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.idc):
            query['Idc'] = request.idc
        if not DaraCore.is_null(request.logic_net_pod):
            query['LogicNetPod'] = request.logic_net_pod
        if not DaraCore.is_null(request.manufacturer):
            query['Manufacturer'] = request.manufacturer
        if not DaraCore.is_null(request.mgn_ip):
            query['MgnIp'] = request.mgn_ip
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.net_pod):
            query['NetPod'] = request.net_pod
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        if not DaraCore.is_null(request.service_tag):
            query['ServiceTag'] = request.service_tag
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNetDeviceInfoWithSize',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNetDeviceInfoWithSizeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_net_device_info_with_size(
        self,
        request: main_models.GetNetDeviceInfoWithSizeRequest,
    ) -> main_models.GetNetDeviceInfoWithSizeResponse:
        runtime = RuntimeOptions()
        return self.get_net_device_info_with_size_with_options(request, runtime)

    async def get_net_device_info_with_size_async(
        self,
        request: main_models.GetNetDeviceInfoWithSizeRequest,
    ) -> main_models.GetNetDeviceInfoWithSizeResponse:
        runtime = RuntimeOptions()
        return await self.get_net_device_info_with_size_with_options_async(request, runtime)

    def get_page_visit_data_with_options(
        self,
        request: main_models.GetPageVisitDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPageVisitDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPageVisitData',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPageVisitDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_page_visit_data_with_options_async(
        self,
        request: main_models.GetPageVisitDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPageVisitDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPageVisitData',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPageVisitDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_page_visit_data(
        self,
        request: main_models.GetPageVisitDataRequest,
    ) -> main_models.GetPageVisitDataResponse:
        runtime = RuntimeOptions()
        return self.get_page_visit_data_with_options(request, runtime)

    async def get_page_visit_data_async(
        self,
        request: main_models.GetPageVisitDataRequest,
    ) -> main_models.GetPageVisitDataResponse:
        runtime = RuntimeOptions()
        return await self.get_page_visit_data_with_options_async(request, runtime)

    def get_radio_run_history_time_ser_with_options(
        self,
        request: main_models.GetRadioRunHistoryTimeSerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRadioRunHistoryTimeSerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.end):
            query['End'] = request.end
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRadioRunHistoryTimeSer',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRadioRunHistoryTimeSerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_radio_run_history_time_ser_with_options_async(
        self,
        request: main_models.GetRadioRunHistoryTimeSerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRadioRunHistoryTimeSerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.end):
            query['End'] = request.end
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRadioRunHistoryTimeSer',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRadioRunHistoryTimeSerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_radio_run_history_time_ser(
        self,
        request: main_models.GetRadioRunHistoryTimeSerRequest,
    ) -> main_models.GetRadioRunHistoryTimeSerResponse:
        runtime = RuntimeOptions()
        return self.get_radio_run_history_time_ser_with_options(request, runtime)

    async def get_radio_run_history_time_ser_async(
        self,
        request: main_models.GetRadioRunHistoryTimeSerRequest,
    ) -> main_models.GetRadioRunHistoryTimeSerResponse:
        runtime = RuntimeOptions()
        return await self.get_radio_run_history_time_ser_with_options_async(request, runtime)

    def get_sta_detailed_status_by_mac_with_options(
        self,
        request: main_models.GetStaDetailedStatusByMacRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStaDetailedStatusByMacResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.sta_mac):
            query['StaMac'] = request.sta_mac
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStaDetailedStatusByMac',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStaDetailedStatusByMacResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sta_detailed_status_by_mac_with_options_async(
        self,
        request: main_models.GetStaDetailedStatusByMacRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStaDetailedStatusByMacResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.sta_mac):
            query['StaMac'] = request.sta_mac
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStaDetailedStatusByMac',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStaDetailedStatusByMacResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sta_detailed_status_by_mac(
        self,
        request: main_models.GetStaDetailedStatusByMacRequest,
    ) -> main_models.GetStaDetailedStatusByMacResponse:
        runtime = RuntimeOptions()
        return self.get_sta_detailed_status_by_mac_with_options(request, runtime)

    async def get_sta_detailed_status_by_mac_async(
        self,
        request: main_models.GetStaDetailedStatusByMacRequest,
    ) -> main_models.GetStaDetailedStatusByMacResponse:
        runtime = RuntimeOptions()
        return await self.get_sta_detailed_status_by_mac_with_options_async(request, runtime)

    def get_sta_status_list_by_ap_with_options(
        self,
        request: main_models.GetStaStatusListByApRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStaStatusListByApResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cursor):
            query['Cursor'] = request.cursor
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStaStatusListByAp',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStaStatusListByApResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sta_status_list_by_ap_with_options_async(
        self,
        request: main_models.GetStaStatusListByApRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStaStatusListByApResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cursor):
            query['Cursor'] = request.cursor
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStaStatusListByAp',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStaStatusListByApResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sta_status_list_by_ap(
        self,
        request: main_models.GetStaStatusListByApRequest,
    ) -> main_models.GetStaStatusListByApResponse:
        runtime = RuntimeOptions()
        return self.get_sta_status_list_by_ap_with_options(request, runtime)

    async def get_sta_status_list_by_ap_async(
        self,
        request: main_models.GetStaStatusListByApRequest,
    ) -> main_models.GetStaStatusListByApResponse:
        runtime = RuntimeOptions()
        return await self.get_sta_status_list_by_ap_with_options_async(request, runtime)

    def judge_xing_tian_business_with_options(
        self,
        request: main_models.JudgeXingTianBusinessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.JudgeXingTianBusinessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.realm_id):
            query['RealmId'] = request.realm_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'JudgeXingTianBusiness',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.JudgeXingTianBusinessResponse(),
            self.call_api(params, req, runtime)
        )

    async def judge_xing_tian_business_with_options_async(
        self,
        request: main_models.JudgeXingTianBusinessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.JudgeXingTianBusinessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.realm_id):
            query['RealmId'] = request.realm_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'JudgeXingTianBusiness',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.JudgeXingTianBusinessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def judge_xing_tian_business(
        self,
        request: main_models.JudgeXingTianBusinessRequest,
    ) -> main_models.JudgeXingTianBusinessResponse:
        runtime = RuntimeOptions()
        return self.judge_xing_tian_business_with_options(request, runtime)

    async def judge_xing_tian_business_async(
        self,
        request: main_models.JudgeXingTianBusinessRequest,
    ) -> main_models.JudgeXingTianBusinessResponse:
        runtime = RuntimeOptions()
        return await self.judge_xing_tian_business_with_options_async(request, runtime)

    def kick_ant_sta_with_options(
        self,
        request: main_models.KickAntStaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KickAntStaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.sta_mac):
            query['StaMac'] = request.sta_mac
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KickAntSta',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KickAntStaResponse(),
            self.call_api(params, req, runtime)
        )

    async def kick_ant_sta_with_options_async(
        self,
        request: main_models.KickAntStaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KickAntStaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.sta_mac):
            query['StaMac'] = request.sta_mac
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KickAntSta',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KickAntStaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kick_ant_sta(
        self,
        request: main_models.KickAntStaRequest,
    ) -> main_models.KickAntStaResponse:
        runtime = RuntimeOptions()
        return self.kick_ant_sta_with_options(request, runtime)

    async def kick_ant_sta_async(
        self,
        request: main_models.KickAntStaRequest,
    ) -> main_models.KickAntStaResponse:
        runtime = RuntimeOptions()
        return await self.kick_ant_sta_with_options_async(request, runtime)

    def kick_sta_with_options(
        self,
        request: main_models.KickStaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KickStaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.sta_mac):
            query['StaMac'] = request.sta_mac
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KickSta',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KickStaResponse(),
            self.call_api(params, req, runtime)
        )

    async def kick_sta_with_options_async(
        self,
        request: main_models.KickStaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KickStaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.sta_mac):
            query['StaMac'] = request.sta_mac
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KickSta',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KickStaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kick_sta(
        self,
        request: main_models.KickStaRequest,
    ) -> main_models.KickStaResponse:
        runtime = RuntimeOptions()
        return self.kick_sta_with_options(request, runtime)

    async def kick_sta_async(
        self,
        request: main_models.KickStaRequest,
    ) -> main_models.KickStaResponse:
        runtime = RuntimeOptions()
        return await self.kick_sta_with_options_async(request, runtime)

    def list_apgroup_descendant_with_options(
        self,
        request: main_models.ListApgroupDescendantRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApgroupDescendantResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not DaraCore.is_null(request.apgroup_uuid):
            query['ApgroupUuid'] = request.apgroup_uuid
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cursor):
            query['Cursor'] = request.cursor
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApgroupDescendant',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApgroupDescendantResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_apgroup_descendant_with_options_async(
        self,
        request: main_models.ListApgroupDescendantRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApgroupDescendantResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not DaraCore.is_null(request.apgroup_uuid):
            query['ApgroupUuid'] = request.apgroup_uuid
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cursor):
            query['Cursor'] = request.cursor
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApgroupDescendant',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApgroupDescendantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_apgroup_descendant(
        self,
        request: main_models.ListApgroupDescendantRequest,
    ) -> main_models.ListApgroupDescendantResponse:
        runtime = RuntimeOptions()
        return self.list_apgroup_descendant_with_options(request, runtime)

    async def list_apgroup_descendant_async(
        self,
        request: main_models.ListApgroupDescendantRequest,
    ) -> main_models.ListApgroupDescendantResponse:
        runtime = RuntimeOptions()
        return await self.list_apgroup_descendant_with_options_async(request, runtime)

    def list_job_orders_with_options(
        self,
        request: main_models.ListJobOrdersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobOrdersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.changing_type):
            query['ChangingType'] = request.changing_type
        if not DaraCore.is_null(request.client_system):
            query['ClientSystem'] = request.client_system
        if not DaraCore.is_null(request.client_unique_id):
            query['ClientUniqueId'] = request.client_unique_id
        if not DaraCore.is_null(request.cursor):
            query['Cursor'] = request.cursor
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.handler):
            query['Handler'] = request.handler
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.order_status):
            query['OrderStatus'] = request.order_status
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobOrders',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_orders_with_options_async(
        self,
        request: main_models.ListJobOrdersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobOrdersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.changing_type):
            query['ChangingType'] = request.changing_type
        if not DaraCore.is_null(request.client_system):
            query['ClientSystem'] = request.client_system
        if not DaraCore.is_null(request.client_unique_id):
            query['ClientUniqueId'] = request.client_unique_id
        if not DaraCore.is_null(request.cursor):
            query['Cursor'] = request.cursor
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.handler):
            query['Handler'] = request.handler
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.order_status):
            query['OrderStatus'] = request.order_status
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobOrders',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_orders(
        self,
        request: main_models.ListJobOrdersRequest,
    ) -> main_models.ListJobOrdersResponse:
        runtime = RuntimeOptions()
        return self.list_job_orders_with_options(request, runtime)

    async def list_job_orders_async(
        self,
        request: main_models.ListJobOrdersRequest,
    ) -> main_models.ListJobOrdersResponse:
        runtime = RuntimeOptions()
        return await self.list_job_orders_with_options_async(request, runtime)

    def list_job_orders_with_size_with_options(
        self,
        request: main_models.ListJobOrdersWithSizeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobOrdersWithSizeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.changing_type):
            query['ChangingType'] = request.changing_type
        if not DaraCore.is_null(request.client_system):
            query['ClientSystem'] = request.client_system
        if not DaraCore.is_null(request.client_unique_id):
            query['ClientUniqueId'] = request.client_unique_id
        if not DaraCore.is_null(request.cursor):
            query['Cursor'] = request.cursor
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.handler):
            query['Handler'] = request.handler
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.order_status):
            query['OrderStatus'] = request.order_status
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobOrdersWithSize',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobOrdersWithSizeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_orders_with_size_with_options_async(
        self,
        request: main_models.ListJobOrdersWithSizeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobOrdersWithSizeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.changing_type):
            query['ChangingType'] = request.changing_type
        if not DaraCore.is_null(request.client_system):
            query['ClientSystem'] = request.client_system
        if not DaraCore.is_null(request.client_unique_id):
            query['ClientUniqueId'] = request.client_unique_id
        if not DaraCore.is_null(request.cursor):
            query['Cursor'] = request.cursor
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.handler):
            query['Handler'] = request.handler
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.order_status):
            query['OrderStatus'] = request.order_status
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobOrdersWithSize',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobOrdersWithSizeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_orders_with_size(
        self,
        request: main_models.ListJobOrdersWithSizeRequest,
    ) -> main_models.ListJobOrdersWithSizeResponse:
        runtime = RuntimeOptions()
        return self.list_job_orders_with_size_with_options(request, runtime)

    async def list_job_orders_with_size_async(
        self,
        request: main_models.ListJobOrdersWithSizeRequest,
    ) -> main_models.ListJobOrdersWithSizeResponse:
        runtime = RuntimeOptions()
        return await self.list_job_orders_with_size_with_options_async(request, runtime)

    def new_apgroup_config_with_options(
        self,
        request: main_models.NewApgroupConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.NewApgroupConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.parent_apgroup_id):
            query['ParentApgroupId'] = request.parent_apgroup_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'NewApgroupConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.NewApgroupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def new_apgroup_config_with_options_async(
        self,
        request: main_models.NewApgroupConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.NewApgroupConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.parent_apgroup_id):
            query['ParentApgroupId'] = request.parent_apgroup_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'NewApgroupConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.NewApgroupConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def new_apgroup_config(
        self,
        request: main_models.NewApgroupConfigRequest,
    ) -> main_models.NewApgroupConfigResponse:
        runtime = RuntimeOptions()
        return self.new_apgroup_config_with_options(request, runtime)

    async def new_apgroup_config_async(
        self,
        request: main_models.NewApgroupConfigRequest,
    ) -> main_models.NewApgroupConfigResponse:
        runtime = RuntimeOptions()
        return await self.new_apgroup_config_with_options_async(request, runtime)

    def new_job_order_with_options(
        self,
        tmp_req: main_models.NewJobOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.NewJobOrderResponse:
        tmp_req.validate()
        request = main_models.NewJobOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not DaraCore.is_null(request.change_type):
            query['ChangeType'] = request.change_type
        if not DaraCore.is_null(request.client_system):
            query['ClientSystem'] = request.client_system
        if not DaraCore.is_null(request.client_unique_id):
            query['ClientUniqueId'] = request.client_unique_id
        if not DaraCore.is_null(request.creator):
            query['Creator'] = request.creator
        if not DaraCore.is_null(request.refer_url):
            query['ReferUrl'] = request.refer_url
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        body = {}
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'NewJobOrder',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.NewJobOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def new_job_order_with_options_async(
        self,
        tmp_req: main_models.NewJobOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.NewJobOrderResponse:
        tmp_req.validate()
        request = main_models.NewJobOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.params):
            request.params_shrink = Utils.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not DaraCore.is_null(request.change_type):
            query['ChangeType'] = request.change_type
        if not DaraCore.is_null(request.client_system):
            query['ClientSystem'] = request.client_system
        if not DaraCore.is_null(request.client_unique_id):
            query['ClientUniqueId'] = request.client_unique_id
        if not DaraCore.is_null(request.creator):
            query['Creator'] = request.creator
        if not DaraCore.is_null(request.refer_url):
            query['ReferUrl'] = request.refer_url
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        body = {}
        if not DaraCore.is_null(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'NewJobOrder',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.NewJobOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def new_job_order(
        self,
        request: main_models.NewJobOrderRequest,
    ) -> main_models.NewJobOrderResponse:
        runtime = RuntimeOptions()
        return self.new_job_order_with_options(request, runtime)

    async def new_job_order_async(
        self,
        request: main_models.NewJobOrderRequest,
    ) -> main_models.NewJobOrderResponse:
        runtime = RuntimeOptions()
        return await self.new_job_order_with_options_async(request, runtime)

    def new_net_device_info_with_options(
        self,
        request: main_models.NewNetDeviceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.NewNetDeviceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not DaraCore.is_null(request.devices):
            body['Devices'] = request.devices
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'NewNetDeviceInfo',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.NewNetDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def new_net_device_info_with_options_async(
        self,
        request: main_models.NewNetDeviceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.NewNetDeviceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not DaraCore.is_null(request.devices):
            body['Devices'] = request.devices
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'NewNetDeviceInfo',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.NewNetDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def new_net_device_info(
        self,
        request: main_models.NewNetDeviceInfoRequest,
    ) -> main_models.NewNetDeviceInfoResponse:
        runtime = RuntimeOptions()
        return self.new_net_device_info_with_options(request, runtime)

    async def new_net_device_info_async(
        self,
        request: main_models.NewNetDeviceInfoRequest,
    ) -> main_models.NewNetDeviceInfoResponse:
        runtime = RuntimeOptions()
        return await self.new_net_device_info_with_options_async(request, runtime)

    def put_app_config_and_save_with_options(
        self,
        request: main_models.PutAppConfigAndSaveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutAppConfigAndSaveResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.configure_type):
            query['ConfigureType'] = request.configure_type
        if not DaraCore.is_null(request.current_time):
            query['CurrentTime'] = request.current_time
        if not DaraCore.is_null(request.data):
            query['Data'] = request.data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutAppConfigAndSave',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutAppConfigAndSaveResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_app_config_and_save_with_options_async(
        self,
        request: main_models.PutAppConfigAndSaveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutAppConfigAndSaveResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.configure_type):
            query['ConfigureType'] = request.configure_type
        if not DaraCore.is_null(request.current_time):
            query['CurrentTime'] = request.current_time
        if not DaraCore.is_null(request.data):
            query['Data'] = request.data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutAppConfigAndSave',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutAppConfigAndSaveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_app_config_and_save(
        self,
        request: main_models.PutAppConfigAndSaveRequest,
    ) -> main_models.PutAppConfigAndSaveResponse:
        runtime = RuntimeOptions()
        return self.put_app_config_and_save_with_options(request, runtime)

    async def put_app_config_and_save_async(
        self,
        request: main_models.PutAppConfigAndSaveRequest,
    ) -> main_models.PutAppConfigAndSaveResponse:
        runtime = RuntimeOptions()
        return await self.put_app_config_and_save_with_options_async(request, runtime)

    def query_job_order_with_options(
        self,
        request: main_models.QueryJobOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryJobOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryJobOrder',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryJobOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_job_order_with_options_async(
        self,
        request: main_models.QueryJobOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryJobOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryJobOrder',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryJobOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_job_order(
        self,
        request: main_models.QueryJobOrderRequest,
    ) -> main_models.QueryJobOrderResponse:
        runtime = RuntimeOptions()
        return self.query_job_order_with_options(request, runtime)

    async def query_job_order_async(
        self,
        request: main_models.QueryJobOrderRequest,
    ) -> main_models.QueryJobOrderResponse:
        runtime = RuntimeOptions()
        return await self.query_job_order_with_options_async(request, runtime)

    def reboot_ap_with_options(
        self,
        request: main_models.RebootApRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RebootApResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RebootAp',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebootApResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_ap_with_options_async(
        self,
        request: main_models.RebootApRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RebootApResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RebootAp',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebootApResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reboot_ap(
        self,
        request: main_models.RebootApRequest,
    ) -> main_models.RebootApResponse:
        runtime = RuntimeOptions()
        return self.reboot_ap_with_options(request, runtime)

    async def reboot_ap_async(
        self,
        request: main_models.RebootApRequest,
    ) -> main_models.RebootApResponse:
        runtime = RuntimeOptions()
        return await self.reboot_ap_with_options_async(request, runtime)

    def register_ap_asset_with_options(
        self,
        request: main_models.RegisterApAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterApAssetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_group_uuid):
            query['ApGroupUUId'] = request.ap_group_uuid
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.mac):
            query['Mac'] = request.mac
        if not DaraCore.is_null(request.serial_no):
            query['SerialNo'] = request.serial_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterApAsset',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterApAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_ap_asset_with_options_async(
        self,
        request: main_models.RegisterApAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterApAssetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_group_uuid):
            query['ApGroupUUId'] = request.ap_group_uuid
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.mac):
            query['Mac'] = request.mac
        if not DaraCore.is_null(request.serial_no):
            query['SerialNo'] = request.serial_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterApAsset',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterApAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_ap_asset(
        self,
        request: main_models.RegisterApAssetRequest,
    ) -> main_models.RegisterApAssetResponse:
        runtime = RuntimeOptions()
        return self.register_ap_asset_with_options(request, runtime)

    async def register_ap_asset_async(
        self,
        request: main_models.RegisterApAssetRequest,
    ) -> main_models.RegisterApAssetResponse:
        runtime = RuntimeOptions()
        return await self.register_ap_asset_with_options_async(request, runtime)

    def repair_ap_radio_with_options(
        self,
        request: main_models.RepairApRadioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RepairApRadioResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.radio_index):
            query['RadioIndex'] = request.radio_index
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RepairApRadio',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RepairApRadioResponse(),
            self.call_api(params, req, runtime)
        )

    async def repair_ap_radio_with_options_async(
        self,
        request: main_models.RepairApRadioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RepairApRadioResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.radio_index):
            query['RadioIndex'] = request.radio_index
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RepairApRadio',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RepairApRadioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def repair_ap_radio(
        self,
        request: main_models.RepairApRadioRequest,
    ) -> main_models.RepairApRadioResponse:
        runtime = RuntimeOptions()
        return self.repair_ap_radio_with_options(request, runtime)

    async def repair_ap_radio_async(
        self,
        request: main_models.RepairApRadioRequest,
    ) -> main_models.RepairApRadioResponse:
        runtime = RuntimeOptions()
        return await self.repair_ap_radio_with_options_async(request, runtime)

    def save_ap_basic_config_with_options(
        self,
        request: main_models.SaveApBasicConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveApBasicConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.dai):
            query['Dai'] = request.dai
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.echo_int):
            query['EchoInt'] = request.echo_int
        if not DaraCore.is_null(request.failover):
            query['Failover'] = request.failover
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.insecure_allowed):
            query['InsecureAllowed'] = request.insecure_allowed
        if not DaraCore.is_null(request.lan_ip):
            query['LanIp'] = request.lan_ip
        if not DaraCore.is_null(request.lan_mask):
            query['LanMask'] = request.lan_mask
        if not DaraCore.is_null(request.lan_status):
            query['LanStatus'] = request.lan_status
        if not DaraCore.is_null(request.log_ip):
            query['LogIp'] = request.log_ip
        if not DaraCore.is_null(request.log_level):
            query['LogLevel'] = request.log_level
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.passwd):
            query['Passwd'] = request.passwd
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.route):
            query['Route'] = request.route
        if not DaraCore.is_null(request.scan):
            query['Scan'] = request.scan
        if not DaraCore.is_null(request.token_server):
            query['TokenServer'] = request.token_server
        if not DaraCore.is_null(request.vpn):
            query['Vpn'] = request.vpn
        if not DaraCore.is_null(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveApBasicConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveApBasicConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_ap_basic_config_with_options_async(
        self,
        request: main_models.SaveApBasicConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveApBasicConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.dai):
            query['Dai'] = request.dai
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.echo_int):
            query['EchoInt'] = request.echo_int
        if not DaraCore.is_null(request.failover):
            query['Failover'] = request.failover
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.insecure_allowed):
            query['InsecureAllowed'] = request.insecure_allowed
        if not DaraCore.is_null(request.lan_ip):
            query['LanIp'] = request.lan_ip
        if not DaraCore.is_null(request.lan_mask):
            query['LanMask'] = request.lan_mask
        if not DaraCore.is_null(request.lan_status):
            query['LanStatus'] = request.lan_status
        if not DaraCore.is_null(request.log_ip):
            query['LogIp'] = request.log_ip
        if not DaraCore.is_null(request.log_level):
            query['LogLevel'] = request.log_level
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.passwd):
            query['Passwd'] = request.passwd
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.route):
            query['Route'] = request.route
        if not DaraCore.is_null(request.scan):
            query['Scan'] = request.scan
        if not DaraCore.is_null(request.token_server):
            query['TokenServer'] = request.token_server
        if not DaraCore.is_null(request.vpn):
            query['Vpn'] = request.vpn
        if not DaraCore.is_null(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveApBasicConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveApBasicConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_ap_basic_config(
        self,
        request: main_models.SaveApBasicConfigRequest,
    ) -> main_models.SaveApBasicConfigResponse:
        runtime = RuntimeOptions()
        return self.save_ap_basic_config_with_options(request, runtime)

    async def save_ap_basic_config_async(
        self,
        request: main_models.SaveApBasicConfigRequest,
    ) -> main_models.SaveApBasicConfigResponse:
        runtime = RuntimeOptions()
        return await self.save_ap_basic_config_with_options_async(request, runtime)

    def save_ap_portal_config_with_options(
        self,
        tmp_req: main_models.SaveApPortalConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveApPortalConfigResponse:
        tmp_req.validate()
        request = main_models.SaveApPortalConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.portal_types):
            request.portal_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.portal_types, 'PortalTypes', 'simple')
        query = {}
        if not DaraCore.is_null(request.ap_config_id):
            query['ApConfigId'] = request.ap_config_id
        if not DaraCore.is_null(request.app_auth_url):
            query['AppAuthUrl'] = request.app_auth_url
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not DaraCore.is_null(request.auth_secret):
            query['AuthSecret'] = request.auth_secret
        if not DaraCore.is_null(request.check_url):
            query['CheckUrl'] = request.check_url
        if not DaraCore.is_null(request.client_download):
            query['ClientDownload'] = request.client_download
        if not DaraCore.is_null(request.client_upload):
            query['ClientUpload'] = request.client_upload
        if not DaraCore.is_null(request.countdown):
            query['Countdown'] = request.countdown
        if not DaraCore.is_null(request.network):
            query['Network'] = request.network
        if not DaraCore.is_null(request.portal_types_shrink):
            query['PortalTypes'] = request.portal_types_shrink
        if not DaraCore.is_null(request.portal_url):
            query['PortalUrl'] = request.portal_url
        if not DaraCore.is_null(request.time_stamp):
            query['TimeStamp'] = request.time_stamp
        if not DaraCore.is_null(request.total_download):
            query['TotalDownload'] = request.total_download
        if not DaraCore.is_null(request.total_upload):
            query['TotalUpload'] = request.total_upload
        if not DaraCore.is_null(request.web_auth_url):
            query['WebAuthUrl'] = request.web_auth_url
        if not DaraCore.is_null(request.whitelist):
            query['Whitelist'] = request.whitelist
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveApPortalConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveApPortalConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_ap_portal_config_with_options_async(
        self,
        tmp_req: main_models.SaveApPortalConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveApPortalConfigResponse:
        tmp_req.validate()
        request = main_models.SaveApPortalConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.portal_types):
            request.portal_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.portal_types, 'PortalTypes', 'simple')
        query = {}
        if not DaraCore.is_null(request.ap_config_id):
            query['ApConfigId'] = request.ap_config_id
        if not DaraCore.is_null(request.app_auth_url):
            query['AppAuthUrl'] = request.app_auth_url
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not DaraCore.is_null(request.auth_secret):
            query['AuthSecret'] = request.auth_secret
        if not DaraCore.is_null(request.check_url):
            query['CheckUrl'] = request.check_url
        if not DaraCore.is_null(request.client_download):
            query['ClientDownload'] = request.client_download
        if not DaraCore.is_null(request.client_upload):
            query['ClientUpload'] = request.client_upload
        if not DaraCore.is_null(request.countdown):
            query['Countdown'] = request.countdown
        if not DaraCore.is_null(request.network):
            query['Network'] = request.network
        if not DaraCore.is_null(request.portal_types_shrink):
            query['PortalTypes'] = request.portal_types_shrink
        if not DaraCore.is_null(request.portal_url):
            query['PortalUrl'] = request.portal_url
        if not DaraCore.is_null(request.time_stamp):
            query['TimeStamp'] = request.time_stamp
        if not DaraCore.is_null(request.total_download):
            query['TotalDownload'] = request.total_download
        if not DaraCore.is_null(request.total_upload):
            query['TotalUpload'] = request.total_upload
        if not DaraCore.is_null(request.web_auth_url):
            query['WebAuthUrl'] = request.web_auth_url
        if not DaraCore.is_null(request.whitelist):
            query['Whitelist'] = request.whitelist
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveApPortalConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveApPortalConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_ap_portal_config(
        self,
        request: main_models.SaveApPortalConfigRequest,
    ) -> main_models.SaveApPortalConfigResponse:
        runtime = RuntimeOptions()
        return self.save_ap_portal_config_with_options(request, runtime)

    async def save_ap_portal_config_async(
        self,
        request: main_models.SaveApPortalConfigRequest,
    ) -> main_models.SaveApPortalConfigResponse:
        runtime = RuntimeOptions()
        return await self.save_ap_portal_config_with_options_async(request, runtime)

    def save_ap_radio_config_with_options(
        self,
        request: main_models.SaveApRadioConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveApRadioConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.bcast_rate):
            query['BcastRate'] = request.bcast_rate
        if not DaraCore.is_null(request.beacon_int):
            query['BeaconInt'] = request.beacon_int
        if not DaraCore.is_null(request.channel):
            query['Channel'] = request.channel
        if not DaraCore.is_null(request.disabled):
            query['Disabled'] = request.disabled
        if not DaraCore.is_null(request.frag):
            query['Frag'] = request.frag
        if not DaraCore.is_null(request.htmode):
            query['Htmode'] = request.htmode
        if not DaraCore.is_null(request.hwmode):
            query['Hwmode'] = request.hwmode
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.mcast_rate):
            query['McastRate'] = request.mcast_rate
        if not DaraCore.is_null(request.mgmt_rate):
            query['MgmtRate'] = request.mgmt_rate
        if not DaraCore.is_null(request.minrate):
            query['Minrate'] = request.minrate
        if not DaraCore.is_null(request.noscan):
            query['Noscan'] = request.noscan
        if not DaraCore.is_null(request.probereq):
            query['Probereq'] = request.probereq
        if not DaraCore.is_null(request.require_mode):
            query['RequireMode'] = request.require_mode
        if not DaraCore.is_null(request.rts):
            query['Rts'] = request.rts
        if not DaraCore.is_null(request.shortgi):
            query['Shortgi'] = request.shortgi
        if not DaraCore.is_null(request.txpower):
            query['Txpower'] = request.txpower
        if not DaraCore.is_null(request.uapsd):
            query['Uapsd'] = request.uapsd
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveApRadioConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveApRadioConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_ap_radio_config_with_options_async(
        self,
        request: main_models.SaveApRadioConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveApRadioConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.bcast_rate):
            query['BcastRate'] = request.bcast_rate
        if not DaraCore.is_null(request.beacon_int):
            query['BeaconInt'] = request.beacon_int
        if not DaraCore.is_null(request.channel):
            query['Channel'] = request.channel
        if not DaraCore.is_null(request.disabled):
            query['Disabled'] = request.disabled
        if not DaraCore.is_null(request.frag):
            query['Frag'] = request.frag
        if not DaraCore.is_null(request.htmode):
            query['Htmode'] = request.htmode
        if not DaraCore.is_null(request.hwmode):
            query['Hwmode'] = request.hwmode
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.mcast_rate):
            query['McastRate'] = request.mcast_rate
        if not DaraCore.is_null(request.mgmt_rate):
            query['MgmtRate'] = request.mgmt_rate
        if not DaraCore.is_null(request.minrate):
            query['Minrate'] = request.minrate
        if not DaraCore.is_null(request.noscan):
            query['Noscan'] = request.noscan
        if not DaraCore.is_null(request.probereq):
            query['Probereq'] = request.probereq
        if not DaraCore.is_null(request.require_mode):
            query['RequireMode'] = request.require_mode
        if not DaraCore.is_null(request.rts):
            query['Rts'] = request.rts
        if not DaraCore.is_null(request.shortgi):
            query['Shortgi'] = request.shortgi
        if not DaraCore.is_null(request.txpower):
            query['Txpower'] = request.txpower
        if not DaraCore.is_null(request.uapsd):
            query['Uapsd'] = request.uapsd
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveApRadioConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveApRadioConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_ap_radio_config(
        self,
        request: main_models.SaveApRadioConfigRequest,
    ) -> main_models.SaveApRadioConfigResponse:
        runtime = RuntimeOptions()
        return self.save_ap_radio_config_with_options(request, runtime)

    async def save_ap_radio_config_async(
        self,
        request: main_models.SaveApRadioConfigRequest,
    ) -> main_models.SaveApRadioConfigResponse:
        runtime = RuntimeOptions()
        return await self.save_ap_radio_config_with_options_async(request, runtime)

    def save_ap_ssid_config_with_options(
        self,
        request: main_models.SaveApSsidConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveApSsidConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acct_port):
            query['AcctPort'] = request.acct_port
        if not DaraCore.is_null(request.acct_secret):
            query['AcctSecret'] = request.acct_secret
        if not DaraCore.is_null(request.acct_server):
            query['AcctServer'] = request.acct_server
        if not DaraCore.is_null(request.acct_status_server_work):
            query['AcctStatusServerWork'] = request.acct_status_server_work
        if not DaraCore.is_null(request.ap_asset_id):
            query['ApAssetId'] = request.ap_asset_id
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.arp_proxy_enable):
            query['ArpProxyEnable'] = request.arp_proxy_enable
        if not DaraCore.is_null(request.auth_cache):
            query['AuthCache'] = request.auth_cache
        if not DaraCore.is_null(request.auth_port):
            query['AuthPort'] = request.auth_port
        if not DaraCore.is_null(request.auth_secret):
            query['AuthSecret'] = request.auth_secret
        if not DaraCore.is_null(request.auth_server):
            query['AuthServer'] = request.auth_server
        if not DaraCore.is_null(request.auth_status_server_work):
            query['AuthStatusServerWork'] = request.auth_status_server_work
        if not DaraCore.is_null(request.cir):
            query['Cir'] = request.cir
        if not DaraCore.is_null(request.cir_step):
            query['CirStep'] = request.cir_step
        if not DaraCore.is_null(request.cir_type):
            query['CirType'] = request.cir_type
        if not DaraCore.is_null(request.cir_ul):
            query['CirUl'] = request.cir_ul
        if not DaraCore.is_null(request.dae_client):
            query['DaeClient'] = request.dae_client
        if not DaraCore.is_null(request.dae_port):
            query['DaePort'] = request.dae_port
        if not DaraCore.is_null(request.dae_secret):
            query['DaeSecret'] = request.dae_secret
        if not DaraCore.is_null(request.disabled):
            query['Disabled'] = request.disabled
        if not DaraCore.is_null(request.disassoc_low_ack):
            query['DisassocLowAck'] = request.disassoc_low_ack
        if not DaraCore.is_null(request.disassoc_weak_rssi):
            query['DisassocWeakRssi'] = request.disassoc_weak_rssi
        if not DaraCore.is_null(request.dynamic_vlan):
            query['DynamicVlan'] = request.dynamic_vlan
        if not DaraCore.is_null(request.enc_key):
            query['EncKey'] = request.enc_key
        if not DaraCore.is_null(request.encryption):
            query['Encryption'] = request.encryption
        if not DaraCore.is_null(request.fourth_auth_port):
            query['FourthAuthPort'] = request.fourth_auth_port
        if not DaraCore.is_null(request.fourth_auth_secret):
            query['FourthAuthSecret'] = request.fourth_auth_secret
        if not DaraCore.is_null(request.fourth_auth_server):
            query['FourthAuthServer'] = request.fourth_auth_server
        if not DaraCore.is_null(request.ft_over_ds):
            query['FtOverDs'] = request.ft_over_ds
        if not DaraCore.is_null(request.hidden):
            query['Hidden'] = request.hidden
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.ieee_80211r):
            query['Ieee80211r'] = request.ieee_80211r
        if not DaraCore.is_null(request.ieee_80211w):
            query['Ieee80211w'] = request.ieee_80211w
        if not DaraCore.is_null(request.ignore_weak_probe):
            query['IgnoreWeakProbe'] = request.ignore_weak_probe
        if not DaraCore.is_null(request.isolate):
            query['Isolate'] = request.isolate
        if not DaraCore.is_null(request.lite_effect):
            query['LiteEffect'] = request.lite_effect
        if not DaraCore.is_null(request.mac):
            query['Mac'] = request.mac
        if not DaraCore.is_null(request.max_inactivity):
            query['MaxInactivity'] = request.max_inactivity
        if not DaraCore.is_null(request.maxassoc):
            query['Maxassoc'] = request.maxassoc
        if not DaraCore.is_null(request.mobility_domain):
            query['MobilityDomain'] = request.mobility_domain
        if not DaraCore.is_null(request.multicast_forward):
            query['MulticastForward'] = request.multicast_forward
        if not DaraCore.is_null(request.nasid):
            query['Nasid'] = request.nasid
        if not DaraCore.is_null(request.nd_proxy_work):
            query['NdProxyWork'] = request.nd_proxy_work
        if not DaraCore.is_null(request.network):
            query['Network'] = request.network
        if not DaraCore.is_null(request.ownip):
            query['Ownip'] = request.ownip
        if not DaraCore.is_null(request.radio_index):
            query['RadioIndex'] = request.radio_index
        if not DaraCore.is_null(request.secondary_acct_port):
            query['SecondaryAcctPort'] = request.secondary_acct_port
        if not DaraCore.is_null(request.secondary_acct_secret):
            query['SecondaryAcctSecret'] = request.secondary_acct_secret
        if not DaraCore.is_null(request.secondary_acct_server):
            query['SecondaryAcctServer'] = request.secondary_acct_server
        if not DaraCore.is_null(request.secondary_auth_port):
            query['SecondaryAuthPort'] = request.secondary_auth_port
        if not DaraCore.is_null(request.secondary_auth_secret):
            query['SecondaryAuthSecret'] = request.secondary_auth_secret
        if not DaraCore.is_null(request.secondary_auth_server):
            query['SecondaryAuthServer'] = request.secondary_auth_server
        if not DaraCore.is_null(request.send_config_to_ap):
            query['SendConfigToAp'] = request.send_config_to_ap
        if not DaraCore.is_null(request.short_preamble):
            query['ShortPreamble'] = request.short_preamble
        if not DaraCore.is_null(request.ssid):
            query['Ssid'] = request.ssid
        if not DaraCore.is_null(request.ssid_lb):
            query['SsidLb'] = request.ssid_lb
        if not DaraCore.is_null(request.third_auth_port):
            query['ThirdAuthPort'] = request.third_auth_port
        if not DaraCore.is_null(request.third_auth_secret):
            query['ThirdAuthSecret'] = request.third_auth_secret
        if not DaraCore.is_null(request.third_auth_server):
            query['ThirdAuthServer'] = request.third_auth_server
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.vlan_dhcp):
            query['VlanDhcp'] = request.vlan_dhcp
        if not DaraCore.is_null(request.wmm):
            query['Wmm'] = request.wmm
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveApSsidConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveApSsidConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_ap_ssid_config_with_options_async(
        self,
        request: main_models.SaveApSsidConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveApSsidConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acct_port):
            query['AcctPort'] = request.acct_port
        if not DaraCore.is_null(request.acct_secret):
            query['AcctSecret'] = request.acct_secret
        if not DaraCore.is_null(request.acct_server):
            query['AcctServer'] = request.acct_server
        if not DaraCore.is_null(request.acct_status_server_work):
            query['AcctStatusServerWork'] = request.acct_status_server_work
        if not DaraCore.is_null(request.ap_asset_id):
            query['ApAssetId'] = request.ap_asset_id
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.arp_proxy_enable):
            query['ArpProxyEnable'] = request.arp_proxy_enable
        if not DaraCore.is_null(request.auth_cache):
            query['AuthCache'] = request.auth_cache
        if not DaraCore.is_null(request.auth_port):
            query['AuthPort'] = request.auth_port
        if not DaraCore.is_null(request.auth_secret):
            query['AuthSecret'] = request.auth_secret
        if not DaraCore.is_null(request.auth_server):
            query['AuthServer'] = request.auth_server
        if not DaraCore.is_null(request.auth_status_server_work):
            query['AuthStatusServerWork'] = request.auth_status_server_work
        if not DaraCore.is_null(request.cir):
            query['Cir'] = request.cir
        if not DaraCore.is_null(request.cir_step):
            query['CirStep'] = request.cir_step
        if not DaraCore.is_null(request.cir_type):
            query['CirType'] = request.cir_type
        if not DaraCore.is_null(request.cir_ul):
            query['CirUl'] = request.cir_ul
        if not DaraCore.is_null(request.dae_client):
            query['DaeClient'] = request.dae_client
        if not DaraCore.is_null(request.dae_port):
            query['DaePort'] = request.dae_port
        if not DaraCore.is_null(request.dae_secret):
            query['DaeSecret'] = request.dae_secret
        if not DaraCore.is_null(request.disabled):
            query['Disabled'] = request.disabled
        if not DaraCore.is_null(request.disassoc_low_ack):
            query['DisassocLowAck'] = request.disassoc_low_ack
        if not DaraCore.is_null(request.disassoc_weak_rssi):
            query['DisassocWeakRssi'] = request.disassoc_weak_rssi
        if not DaraCore.is_null(request.dynamic_vlan):
            query['DynamicVlan'] = request.dynamic_vlan
        if not DaraCore.is_null(request.enc_key):
            query['EncKey'] = request.enc_key
        if not DaraCore.is_null(request.encryption):
            query['Encryption'] = request.encryption
        if not DaraCore.is_null(request.fourth_auth_port):
            query['FourthAuthPort'] = request.fourth_auth_port
        if not DaraCore.is_null(request.fourth_auth_secret):
            query['FourthAuthSecret'] = request.fourth_auth_secret
        if not DaraCore.is_null(request.fourth_auth_server):
            query['FourthAuthServer'] = request.fourth_auth_server
        if not DaraCore.is_null(request.ft_over_ds):
            query['FtOverDs'] = request.ft_over_ds
        if not DaraCore.is_null(request.hidden):
            query['Hidden'] = request.hidden
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.ieee_80211r):
            query['Ieee80211r'] = request.ieee_80211r
        if not DaraCore.is_null(request.ieee_80211w):
            query['Ieee80211w'] = request.ieee_80211w
        if not DaraCore.is_null(request.ignore_weak_probe):
            query['IgnoreWeakProbe'] = request.ignore_weak_probe
        if not DaraCore.is_null(request.isolate):
            query['Isolate'] = request.isolate
        if not DaraCore.is_null(request.lite_effect):
            query['LiteEffect'] = request.lite_effect
        if not DaraCore.is_null(request.mac):
            query['Mac'] = request.mac
        if not DaraCore.is_null(request.max_inactivity):
            query['MaxInactivity'] = request.max_inactivity
        if not DaraCore.is_null(request.maxassoc):
            query['Maxassoc'] = request.maxassoc
        if not DaraCore.is_null(request.mobility_domain):
            query['MobilityDomain'] = request.mobility_domain
        if not DaraCore.is_null(request.multicast_forward):
            query['MulticastForward'] = request.multicast_forward
        if not DaraCore.is_null(request.nasid):
            query['Nasid'] = request.nasid
        if not DaraCore.is_null(request.nd_proxy_work):
            query['NdProxyWork'] = request.nd_proxy_work
        if not DaraCore.is_null(request.network):
            query['Network'] = request.network
        if not DaraCore.is_null(request.ownip):
            query['Ownip'] = request.ownip
        if not DaraCore.is_null(request.radio_index):
            query['RadioIndex'] = request.radio_index
        if not DaraCore.is_null(request.secondary_acct_port):
            query['SecondaryAcctPort'] = request.secondary_acct_port
        if not DaraCore.is_null(request.secondary_acct_secret):
            query['SecondaryAcctSecret'] = request.secondary_acct_secret
        if not DaraCore.is_null(request.secondary_acct_server):
            query['SecondaryAcctServer'] = request.secondary_acct_server
        if not DaraCore.is_null(request.secondary_auth_port):
            query['SecondaryAuthPort'] = request.secondary_auth_port
        if not DaraCore.is_null(request.secondary_auth_secret):
            query['SecondaryAuthSecret'] = request.secondary_auth_secret
        if not DaraCore.is_null(request.secondary_auth_server):
            query['SecondaryAuthServer'] = request.secondary_auth_server
        if not DaraCore.is_null(request.send_config_to_ap):
            query['SendConfigToAp'] = request.send_config_to_ap
        if not DaraCore.is_null(request.short_preamble):
            query['ShortPreamble'] = request.short_preamble
        if not DaraCore.is_null(request.ssid):
            query['Ssid'] = request.ssid
        if not DaraCore.is_null(request.ssid_lb):
            query['SsidLb'] = request.ssid_lb
        if not DaraCore.is_null(request.third_auth_port):
            query['ThirdAuthPort'] = request.third_auth_port
        if not DaraCore.is_null(request.third_auth_secret):
            query['ThirdAuthSecret'] = request.third_auth_secret
        if not DaraCore.is_null(request.third_auth_server):
            query['ThirdAuthServer'] = request.third_auth_server
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.vlan_dhcp):
            query['VlanDhcp'] = request.vlan_dhcp
        if not DaraCore.is_null(request.wmm):
            query['Wmm'] = request.wmm
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveApSsidConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveApSsidConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_ap_ssid_config(
        self,
        request: main_models.SaveApSsidConfigRequest,
    ) -> main_models.SaveApSsidConfigResponse:
        runtime = RuntimeOptions()
        return self.save_ap_ssid_config_with_options(request, runtime)

    async def save_ap_ssid_config_async(
        self,
        request: main_models.SaveApSsidConfigRequest,
    ) -> main_models.SaveApSsidConfigResponse:
        runtime = RuntimeOptions()
        return await self.save_ap_ssid_config_with_options_async(request, runtime)

    def save_ap_third_app_with_options(
        self,
        request: main_models.SaveApThirdAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveApThirdAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_style):
            query['AddStyle'] = request.add_style
        if not DaraCore.is_null(request.ap_asset_id):
            query['ApAssetId'] = request.ap_asset_id
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_data):
            query['AppData'] = request.app_data
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.mac):
            query['Mac'] = request.mac
        if not DaraCore.is_null(request.third_app_name):
            query['ThirdAppName'] = request.third_app_name
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveApThirdApp',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveApThirdAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_ap_third_app_with_options_async(
        self,
        request: main_models.SaveApThirdAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveApThirdAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_style):
            query['AddStyle'] = request.add_style
        if not DaraCore.is_null(request.ap_asset_id):
            query['ApAssetId'] = request.ap_asset_id
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_data):
            query['AppData'] = request.app_data
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.mac):
            query['Mac'] = request.mac
        if not DaraCore.is_null(request.third_app_name):
            query['ThirdAppName'] = request.third_app_name
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveApThirdApp',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveApThirdAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_ap_third_app(
        self,
        request: main_models.SaveApThirdAppRequest,
    ) -> main_models.SaveApThirdAppResponse:
        runtime = RuntimeOptions()
        return self.save_ap_third_app_with_options(request, runtime)

    async def save_ap_third_app_async(
        self,
        request: main_models.SaveApThirdAppRequest,
    ) -> main_models.SaveApThirdAppResponse:
        runtime = RuntimeOptions()
        return await self.save_ap_third_app_with_options_async(request, runtime)

    def save_apgroup_basic_config_with_options(
        self,
        request: main_models.SaveApgroupBasicConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveApgroupBasicConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.dai):
            query['Dai'] = request.dai
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.echo_int):
            query['EchoInt'] = request.echo_int
        if not DaraCore.is_null(request.failover):
            query['Failover'] = request.failover
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.insecure_allowed):
            query['InsecureAllowed'] = request.insecure_allowed
        if not DaraCore.is_null(request.is_config_strong_consistency):
            query['IsConfigStrongConsistency'] = request.is_config_strong_consistency
        if not DaraCore.is_null(request.lan_ip):
            query['LanIp'] = request.lan_ip
        if not DaraCore.is_null(request.lan_mask):
            query['LanMask'] = request.lan_mask
        if not DaraCore.is_null(request.lan_status):
            query['LanStatus'] = request.lan_status
        if not DaraCore.is_null(request.log_ip):
            query['LogIp'] = request.log_ip
        if not DaraCore.is_null(request.log_level):
            query['LogLevel'] = request.log_level
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.parent_apgroup_id):
            query['ParentApgroupId'] = request.parent_apgroup_id
        if not DaraCore.is_null(request.passwd):
            query['Passwd'] = request.passwd
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.route):
            query['Route'] = request.route
        if not DaraCore.is_null(request.scan):
            query['Scan'] = request.scan
        if not DaraCore.is_null(request.token_server):
            query['TokenServer'] = request.token_server
        if not DaraCore.is_null(request.vpn):
            query['Vpn'] = request.vpn
        if not DaraCore.is_null(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveApgroupBasicConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveApgroupBasicConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_apgroup_basic_config_with_options_async(
        self,
        request: main_models.SaveApgroupBasicConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveApgroupBasicConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.dai):
            query['Dai'] = request.dai
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.echo_int):
            query['EchoInt'] = request.echo_int
        if not DaraCore.is_null(request.failover):
            query['Failover'] = request.failover
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.insecure_allowed):
            query['InsecureAllowed'] = request.insecure_allowed
        if not DaraCore.is_null(request.is_config_strong_consistency):
            query['IsConfigStrongConsistency'] = request.is_config_strong_consistency
        if not DaraCore.is_null(request.lan_ip):
            query['LanIp'] = request.lan_ip
        if not DaraCore.is_null(request.lan_mask):
            query['LanMask'] = request.lan_mask
        if not DaraCore.is_null(request.lan_status):
            query['LanStatus'] = request.lan_status
        if not DaraCore.is_null(request.log_ip):
            query['LogIp'] = request.log_ip
        if not DaraCore.is_null(request.log_level):
            query['LogLevel'] = request.log_level
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.parent_apgroup_id):
            query['ParentApgroupId'] = request.parent_apgroup_id
        if not DaraCore.is_null(request.passwd):
            query['Passwd'] = request.passwd
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.route):
            query['Route'] = request.route
        if not DaraCore.is_null(request.scan):
            query['Scan'] = request.scan
        if not DaraCore.is_null(request.token_server):
            query['TokenServer'] = request.token_server
        if not DaraCore.is_null(request.vpn):
            query['Vpn'] = request.vpn
        if not DaraCore.is_null(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveApgroupBasicConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveApgroupBasicConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_apgroup_basic_config(
        self,
        request: main_models.SaveApgroupBasicConfigRequest,
    ) -> main_models.SaveApgroupBasicConfigResponse:
        runtime = RuntimeOptions()
        return self.save_apgroup_basic_config_with_options(request, runtime)

    async def save_apgroup_basic_config_async(
        self,
        request: main_models.SaveApgroupBasicConfigRequest,
    ) -> main_models.SaveApgroupBasicConfigResponse:
        runtime = RuntimeOptions()
        return await self.save_apgroup_basic_config_with_options_async(request, runtime)

    def save_apgroup_portal_config_with_options(
        self,
        tmp_req: main_models.SaveApgroupPortalConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveApgroupPortalConfigResponse:
        tmp_req.validate()
        request = main_models.SaveApgroupPortalConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.portal_types):
            request.portal_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.portal_types, 'PortalTypes', 'simple')
        query = {}
        if not DaraCore.is_null(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not DaraCore.is_null(request.app_auth_url):
            query['AppAuthUrl'] = request.app_auth_url
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not DaraCore.is_null(request.auth_secret):
            query['AuthSecret'] = request.auth_secret
        if not DaraCore.is_null(request.check_url):
            query['CheckUrl'] = request.check_url
        if not DaraCore.is_null(request.client_download):
            query['ClientDownload'] = request.client_download
        if not DaraCore.is_null(request.client_upload):
            query['ClientUpload'] = request.client_upload
        if not DaraCore.is_null(request.countdown):
            query['Countdown'] = request.countdown
        if not DaraCore.is_null(request.network):
            query['Network'] = request.network
        if not DaraCore.is_null(request.portal_types_shrink):
            query['PortalTypes'] = request.portal_types_shrink
        if not DaraCore.is_null(request.portal_url):
            query['PortalUrl'] = request.portal_url
        if not DaraCore.is_null(request.time_stamp):
            query['TimeStamp'] = request.time_stamp
        if not DaraCore.is_null(request.total_download):
            query['TotalDownload'] = request.total_download
        if not DaraCore.is_null(request.total_upload):
            query['TotalUpload'] = request.total_upload
        if not DaraCore.is_null(request.web_auth_url):
            query['WebAuthUrl'] = request.web_auth_url
        if not DaraCore.is_null(request.whitelist):
            query['Whitelist'] = request.whitelist
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveApgroupPortalConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveApgroupPortalConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_apgroup_portal_config_with_options_async(
        self,
        tmp_req: main_models.SaveApgroupPortalConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveApgroupPortalConfigResponse:
        tmp_req.validate()
        request = main_models.SaveApgroupPortalConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.portal_types):
            request.portal_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.portal_types, 'PortalTypes', 'simple')
        query = {}
        if not DaraCore.is_null(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not DaraCore.is_null(request.app_auth_url):
            query['AppAuthUrl'] = request.app_auth_url
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not DaraCore.is_null(request.auth_secret):
            query['AuthSecret'] = request.auth_secret
        if not DaraCore.is_null(request.check_url):
            query['CheckUrl'] = request.check_url
        if not DaraCore.is_null(request.client_download):
            query['ClientDownload'] = request.client_download
        if not DaraCore.is_null(request.client_upload):
            query['ClientUpload'] = request.client_upload
        if not DaraCore.is_null(request.countdown):
            query['Countdown'] = request.countdown
        if not DaraCore.is_null(request.network):
            query['Network'] = request.network
        if not DaraCore.is_null(request.portal_types_shrink):
            query['PortalTypes'] = request.portal_types_shrink
        if not DaraCore.is_null(request.portal_url):
            query['PortalUrl'] = request.portal_url
        if not DaraCore.is_null(request.time_stamp):
            query['TimeStamp'] = request.time_stamp
        if not DaraCore.is_null(request.total_download):
            query['TotalDownload'] = request.total_download
        if not DaraCore.is_null(request.total_upload):
            query['TotalUpload'] = request.total_upload
        if not DaraCore.is_null(request.web_auth_url):
            query['WebAuthUrl'] = request.web_auth_url
        if not DaraCore.is_null(request.whitelist):
            query['Whitelist'] = request.whitelist
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveApgroupPortalConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveApgroupPortalConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_apgroup_portal_config(
        self,
        request: main_models.SaveApgroupPortalConfigRequest,
    ) -> main_models.SaveApgroupPortalConfigResponse:
        runtime = RuntimeOptions()
        return self.save_apgroup_portal_config_with_options(request, runtime)

    async def save_apgroup_portal_config_async(
        self,
        request: main_models.SaveApgroupPortalConfigRequest,
    ) -> main_models.SaveApgroupPortalConfigResponse:
        runtime = RuntimeOptions()
        return await self.save_apgroup_portal_config_with_options_async(request, runtime)

    def save_apgroup_ssid_config_with_options(
        self,
        request: main_models.SaveApgroupSsidConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveApgroupSsidConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acct_port):
            query['AcctPort'] = request.acct_port
        if not DaraCore.is_null(request.acct_secret):
            query['AcctSecret'] = request.acct_secret
        if not DaraCore.is_null(request.acct_server):
            query['AcctServer'] = request.acct_server
        if not DaraCore.is_null(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.auth_cache):
            query['AuthCache'] = request.auth_cache
        if not DaraCore.is_null(request.auth_port):
            query['AuthPort'] = request.auth_port
        if not DaraCore.is_null(request.auth_secret):
            query['AuthSecret'] = request.auth_secret
        if not DaraCore.is_null(request.auth_server):
            query['AuthServer'] = request.auth_server
        if not DaraCore.is_null(request.binding):
            query['Binding'] = request.binding
        if not DaraCore.is_null(request.cir):
            query['Cir'] = request.cir
        if not DaraCore.is_null(request.dae_client):
            query['DaeClient'] = request.dae_client
        if not DaraCore.is_null(request.dae_port):
            query['DaePort'] = request.dae_port
        if not DaraCore.is_null(request.dae_secret):
            query['DaeSecret'] = request.dae_secret
        if not DaraCore.is_null(request.disabled):
            query['Disabled'] = request.disabled
        if not DaraCore.is_null(request.disassoc_low_ack):
            query['DisassocLowAck'] = request.disassoc_low_ack
        if not DaraCore.is_null(request.disassoc_weak_rssi):
            query['DisassocWeakRssi'] = request.disassoc_weak_rssi
        if not DaraCore.is_null(request.dynamic_vlan):
            query['DynamicVlan'] = request.dynamic_vlan
        if not DaraCore.is_null(request.effect):
            query['Effect'] = request.effect
        if not DaraCore.is_null(request.enc_key):
            query['EncKey'] = request.enc_key
        if not DaraCore.is_null(request.encryption):
            query['Encryption'] = request.encryption
        if not DaraCore.is_null(request.hidden):
            query['Hidden'] = request.hidden
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.ieee_80211w):
            query['Ieee80211w'] = request.ieee_80211w
        if not DaraCore.is_null(request.ignore_weak_probe):
            query['IgnoreWeakProbe'] = request.ignore_weak_probe
        if not DaraCore.is_null(request.isolate):
            query['Isolate'] = request.isolate
        if not DaraCore.is_null(request.lite_effect):
            query['LiteEffect'] = request.lite_effect
        if not DaraCore.is_null(request.max_inactivity):
            query['MaxInactivity'] = request.max_inactivity
        if not DaraCore.is_null(request.maxassoc):
            query['Maxassoc'] = request.maxassoc
        if not DaraCore.is_null(request.multicast_forward):
            query['MulticastForward'] = request.multicast_forward
        if not DaraCore.is_null(request.nasid):
            query['Nasid'] = request.nasid
        if not DaraCore.is_null(request.network):
            query['Network'] = request.network
        if not DaraCore.is_null(request.new_ssid):
            query['NewSsid'] = request.new_ssid
        if not DaraCore.is_null(request.ownip):
            query['Ownip'] = request.ownip
        if not DaraCore.is_null(request.secondary_acct_port):
            query['SecondaryAcctPort'] = request.secondary_acct_port
        if not DaraCore.is_null(request.secondary_acct_secret):
            query['SecondaryAcctSecret'] = request.secondary_acct_secret
        if not DaraCore.is_null(request.secondary_acct_server):
            query['SecondaryAcctServer'] = request.secondary_acct_server
        if not DaraCore.is_null(request.secondary_auth_port):
            query['SecondaryAuthPort'] = request.secondary_auth_port
        if not DaraCore.is_null(request.secondary_auth_secret):
            query['SecondaryAuthSecret'] = request.secondary_auth_secret
        if not DaraCore.is_null(request.secondary_auth_server):
            query['SecondaryAuthServer'] = request.secondary_auth_server
        if not DaraCore.is_null(request.short_preamble):
            query['ShortPreamble'] = request.short_preamble
        if not DaraCore.is_null(request.ssid):
            query['Ssid'] = request.ssid
        if not DaraCore.is_null(request.ssid_lb):
            query['SsidLb'] = request.ssid_lb
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.vlan_dhcp):
            query['VlanDhcp'] = request.vlan_dhcp
        if not DaraCore.is_null(request.wmm):
            query['Wmm'] = request.wmm
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveApgroupSsidConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveApgroupSsidConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_apgroup_ssid_config_with_options_async(
        self,
        request: main_models.SaveApgroupSsidConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveApgroupSsidConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acct_port):
            query['AcctPort'] = request.acct_port
        if not DaraCore.is_null(request.acct_secret):
            query['AcctSecret'] = request.acct_secret
        if not DaraCore.is_null(request.acct_server):
            query['AcctServer'] = request.acct_server
        if not DaraCore.is_null(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.auth_cache):
            query['AuthCache'] = request.auth_cache
        if not DaraCore.is_null(request.auth_port):
            query['AuthPort'] = request.auth_port
        if not DaraCore.is_null(request.auth_secret):
            query['AuthSecret'] = request.auth_secret
        if not DaraCore.is_null(request.auth_server):
            query['AuthServer'] = request.auth_server
        if not DaraCore.is_null(request.binding):
            query['Binding'] = request.binding
        if not DaraCore.is_null(request.cir):
            query['Cir'] = request.cir
        if not DaraCore.is_null(request.dae_client):
            query['DaeClient'] = request.dae_client
        if not DaraCore.is_null(request.dae_port):
            query['DaePort'] = request.dae_port
        if not DaraCore.is_null(request.dae_secret):
            query['DaeSecret'] = request.dae_secret
        if not DaraCore.is_null(request.disabled):
            query['Disabled'] = request.disabled
        if not DaraCore.is_null(request.disassoc_low_ack):
            query['DisassocLowAck'] = request.disassoc_low_ack
        if not DaraCore.is_null(request.disassoc_weak_rssi):
            query['DisassocWeakRssi'] = request.disassoc_weak_rssi
        if not DaraCore.is_null(request.dynamic_vlan):
            query['DynamicVlan'] = request.dynamic_vlan
        if not DaraCore.is_null(request.effect):
            query['Effect'] = request.effect
        if not DaraCore.is_null(request.enc_key):
            query['EncKey'] = request.enc_key
        if not DaraCore.is_null(request.encryption):
            query['Encryption'] = request.encryption
        if not DaraCore.is_null(request.hidden):
            query['Hidden'] = request.hidden
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.ieee_80211w):
            query['Ieee80211w'] = request.ieee_80211w
        if not DaraCore.is_null(request.ignore_weak_probe):
            query['IgnoreWeakProbe'] = request.ignore_weak_probe
        if not DaraCore.is_null(request.isolate):
            query['Isolate'] = request.isolate
        if not DaraCore.is_null(request.lite_effect):
            query['LiteEffect'] = request.lite_effect
        if not DaraCore.is_null(request.max_inactivity):
            query['MaxInactivity'] = request.max_inactivity
        if not DaraCore.is_null(request.maxassoc):
            query['Maxassoc'] = request.maxassoc
        if not DaraCore.is_null(request.multicast_forward):
            query['MulticastForward'] = request.multicast_forward
        if not DaraCore.is_null(request.nasid):
            query['Nasid'] = request.nasid
        if not DaraCore.is_null(request.network):
            query['Network'] = request.network
        if not DaraCore.is_null(request.new_ssid):
            query['NewSsid'] = request.new_ssid
        if not DaraCore.is_null(request.ownip):
            query['Ownip'] = request.ownip
        if not DaraCore.is_null(request.secondary_acct_port):
            query['SecondaryAcctPort'] = request.secondary_acct_port
        if not DaraCore.is_null(request.secondary_acct_secret):
            query['SecondaryAcctSecret'] = request.secondary_acct_secret
        if not DaraCore.is_null(request.secondary_acct_server):
            query['SecondaryAcctServer'] = request.secondary_acct_server
        if not DaraCore.is_null(request.secondary_auth_port):
            query['SecondaryAuthPort'] = request.secondary_auth_port
        if not DaraCore.is_null(request.secondary_auth_secret):
            query['SecondaryAuthSecret'] = request.secondary_auth_secret
        if not DaraCore.is_null(request.secondary_auth_server):
            query['SecondaryAuthServer'] = request.secondary_auth_server
        if not DaraCore.is_null(request.short_preamble):
            query['ShortPreamble'] = request.short_preamble
        if not DaraCore.is_null(request.ssid):
            query['Ssid'] = request.ssid
        if not DaraCore.is_null(request.ssid_lb):
            query['SsidLb'] = request.ssid_lb
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.vlan_dhcp):
            query['VlanDhcp'] = request.vlan_dhcp
        if not DaraCore.is_null(request.wmm):
            query['Wmm'] = request.wmm
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveApgroupSsidConfig',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveApgroupSsidConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_apgroup_ssid_config(
        self,
        request: main_models.SaveApgroupSsidConfigRequest,
    ) -> main_models.SaveApgroupSsidConfigResponse:
        runtime = RuntimeOptions()
        return self.save_apgroup_ssid_config_with_options(request, runtime)

    async def save_apgroup_ssid_config_async(
        self,
        request: main_models.SaveApgroupSsidConfigRequest,
    ) -> main_models.SaveApgroupSsidConfigResponse:
        runtime = RuntimeOptions()
        return await self.save_apgroup_ssid_config_with_options_async(request, runtime)

    def set_ap_address_with_options(
        self,
        request: main_models.SetApAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetApAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_area_name):
            query['ApAreaName'] = request.ap_area_name
        if not DaraCore.is_null(request.ap_building_name):
            query['ApBuildingName'] = request.ap_building_name
        if not DaraCore.is_null(request.ap_campus_name):
            query['ApCampusName'] = request.ap_campus_name
        if not DaraCore.is_null(request.ap_city_name):
            query['ApCityName'] = request.ap_city_name
        if not DaraCore.is_null(request.ap_floor):
            query['ApFloor'] = request.ap_floor
        if not DaraCore.is_null(request.ap_group):
            query['ApGroup'] = request.ap_group
        if not DaraCore.is_null(request.ap_name):
            query['ApName'] = request.ap_name
        if not DaraCore.is_null(request.ap_nation_name):
            query['ApNationName'] = request.ap_nation_name
        if not DaraCore.is_null(request.ap_province_name):
            query['ApProvinceName'] = request.ap_province_name
        if not DaraCore.is_null(request.ap_unit_id):
            query['ApUnitId'] = request.ap_unit_id
        if not DaraCore.is_null(request.ap_unit_name):
            query['ApUnitName'] = request.ap_unit_name
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.lat):
            query['Lat'] = request.lat
        if not DaraCore.is_null(request.lng):
            query['Lng'] = request.lng
        if not DaraCore.is_null(request.mac):
            query['Mac'] = request.mac
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetApAddress',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetApAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_ap_address_with_options_async(
        self,
        request: main_models.SetApAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetApAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_area_name):
            query['ApAreaName'] = request.ap_area_name
        if not DaraCore.is_null(request.ap_building_name):
            query['ApBuildingName'] = request.ap_building_name
        if not DaraCore.is_null(request.ap_campus_name):
            query['ApCampusName'] = request.ap_campus_name
        if not DaraCore.is_null(request.ap_city_name):
            query['ApCityName'] = request.ap_city_name
        if not DaraCore.is_null(request.ap_floor):
            query['ApFloor'] = request.ap_floor
        if not DaraCore.is_null(request.ap_group):
            query['ApGroup'] = request.ap_group
        if not DaraCore.is_null(request.ap_name):
            query['ApName'] = request.ap_name
        if not DaraCore.is_null(request.ap_nation_name):
            query['ApNationName'] = request.ap_nation_name
        if not DaraCore.is_null(request.ap_province_name):
            query['ApProvinceName'] = request.ap_province_name
        if not DaraCore.is_null(request.ap_unit_id):
            query['ApUnitId'] = request.ap_unit_id
        if not DaraCore.is_null(request.ap_unit_name):
            query['ApUnitName'] = request.ap_unit_name
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.lat):
            query['Lat'] = request.lat
        if not DaraCore.is_null(request.lng):
            query['Lng'] = request.lng
        if not DaraCore.is_null(request.mac):
            query['Mac'] = request.mac
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetApAddress',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetApAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_ap_address(
        self,
        request: main_models.SetApAddressRequest,
    ) -> main_models.SetApAddressResponse:
        runtime = RuntimeOptions()
        return self.set_ap_address_with_options(request, runtime)

    async def set_ap_address_async(
        self,
        request: main_models.SetApAddressRequest,
    ) -> main_models.SetApAddressResponse:
        runtime = RuntimeOptions()
        return await self.set_ap_address_with_options_async(request, runtime)

    def set_ap_name_with_options(
        self,
        request: main_models.SetApNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetApNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetApName',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetApNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_ap_name_with_options_async(
        self,
        request: main_models.SetApNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetApNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetApName',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetApNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_ap_name(
        self,
        request: main_models.SetApNameRequest,
    ) -> main_models.SetApNameResponse:
        runtime = RuntimeOptions()
        return self.set_ap_name_with_options(request, runtime)

    async def set_ap_name_async(
        self,
        request: main_models.SetApNameRequest,
    ) -> main_models.SetApNameResponse:
        runtime = RuntimeOptions()
        return await self.set_ap_name_with_options_async(request, runtime)

    def un_register_ap_asset_with_options(
        self,
        request: main_models.UnRegisterApAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnRegisterApAssetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.asset_apgroup_id):
            query['AssetApgroupId'] = request.asset_apgroup_id
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.mac):
            query['Mac'] = request.mac
        if not DaraCore.is_null(request.serial_no):
            query['SerialNo'] = request.serial_no
        if not DaraCore.is_null(request.use_for):
            query['UseFor'] = request.use_for
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnRegisterApAsset',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnRegisterApAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_register_ap_asset_with_options_async(
        self,
        request: main_models.UnRegisterApAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnRegisterApAssetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.asset_apgroup_id):
            query['AssetApgroupId'] = request.asset_apgroup_id
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.mac):
            query['Mac'] = request.mac
        if not DaraCore.is_null(request.serial_no):
            query['SerialNo'] = request.serial_no
        if not DaraCore.is_null(request.use_for):
            query['UseFor'] = request.use_for
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnRegisterApAsset',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnRegisterApAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_register_ap_asset(
        self,
        request: main_models.UnRegisterApAssetRequest,
    ) -> main_models.UnRegisterApAssetResponse:
        runtime = RuntimeOptions()
        return self.un_register_ap_asset_with_options(request, runtime)

    async def un_register_ap_asset_async(
        self,
        request: main_models.UnRegisterApAssetRequest,
    ) -> main_models.UnRegisterApAssetResponse:
        runtime = RuntimeOptions()
        return await self.un_register_ap_asset_with_options_async(request, runtime)

    def update_net_device_info_with_options(
        self,
        request: main_models.UpdateNetDeviceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNetDeviceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not DaraCore.is_null(request.devices):
            body['Devices'] = request.devices
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNetDeviceInfo',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNetDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_net_device_info_with_options_async(
        self,
        request: main_models.UpdateNetDeviceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNetDeviceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_code):
            query['AppCode'] = request.app_code
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not DaraCore.is_null(request.devices):
            body['Devices'] = request.devices
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNetDeviceInfo',
            version = '2019-11-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNetDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_net_device_info(
        self,
        request: main_models.UpdateNetDeviceInfoRequest,
    ) -> main_models.UpdateNetDeviceInfoResponse:
        runtime = RuntimeOptions()
        return self.update_net_device_info_with_options(request, runtime)

    async def update_net_device_info_async(
        self,
        request: main_models.UpdateNetDeviceInfoRequest,
    ) -> main_models.UpdateNetDeviceInfoResponse:
        runtime = RuntimeOptions()
        return await self.update_net_device_info_with_options_async(request, runtime)
