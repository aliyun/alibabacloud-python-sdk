# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudwifi_pop20191118 import models as cloudwifi_pop_20191118_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_ap_list_to_apgroup_with_options(
        self,
        tmp_req: cloudwifi_pop_20191118_models.AddApListToApgroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.AddApListToApgroupResponse:
        UtilClient.validate_model(tmp_req)
        request = cloudwifi_pop_20191118_models.AddApListToApgroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ap_mac_list):
            request.ap_mac_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ap_mac_list, 'ApMacList', 'json')
        query = {}
        if not UtilClient.is_unset(request.ap_group_id):
            query['ApGroupId'] = request.ap_group_id
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        body = {}
        if not UtilClient.is_unset(request.ap_mac_list_shrink):
            body['ApMacList'] = request.ap_mac_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddApListToApgroup',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.AddApListToApgroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_ap_list_to_apgroup_with_options_async(
        self,
        tmp_req: cloudwifi_pop_20191118_models.AddApListToApgroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.AddApListToApgroupResponse:
        UtilClient.validate_model(tmp_req)
        request = cloudwifi_pop_20191118_models.AddApListToApgroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ap_mac_list):
            request.ap_mac_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ap_mac_list, 'ApMacList', 'json')
        query = {}
        if not UtilClient.is_unset(request.ap_group_id):
            query['ApGroupId'] = request.ap_group_id
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        body = {}
        if not UtilClient.is_unset(request.ap_mac_list_shrink):
            body['ApMacList'] = request.ap_mac_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddApListToApgroup',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.AddApListToApgroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_ap_list_to_apgroup(
        self,
        request: cloudwifi_pop_20191118_models.AddApListToApgroupRequest,
    ) -> cloudwifi_pop_20191118_models.AddApListToApgroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_ap_list_to_apgroup_with_options(request, runtime)

    async def add_ap_list_to_apgroup_async(
        self,
        request: cloudwifi_pop_20191118_models.AddApListToApgroupRequest,
    ) -> cloudwifi_pop_20191118_models.AddApListToApgroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_ap_list_to_apgroup_with_options_async(request, runtime)

    def del_ap_third_app_with_options(
        self,
        request: cloudwifi_pop_20191118_models.DelApThirdAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.DelApThirdAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_asset_id):
            query['ApAssetId'] = request.ap_asset_id
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.mac):
            query['Mac'] = request.mac
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelApThirdApp',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.DelApThirdAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def del_ap_third_app_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.DelApThirdAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.DelApThirdAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_asset_id):
            query['ApAssetId'] = request.ap_asset_id
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.mac):
            query['Mac'] = request.mac
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelApThirdApp',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.DelApThirdAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def del_ap_third_app(
        self,
        request: cloudwifi_pop_20191118_models.DelApThirdAppRequest,
    ) -> cloudwifi_pop_20191118_models.DelApThirdAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.del_ap_third_app_with_options(request, runtime)

    async def del_ap_third_app_async(
        self,
        request: cloudwifi_pop_20191118_models.DelApThirdAppRequest,
    ) -> cloudwifi_pop_20191118_models.DelApThirdAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.del_ap_third_app_with_options_async(request, runtime)

    def delete_ap_ssid_config_with_options(
        self,
        request: cloudwifi_pop_20191118_models.DeleteApSsidConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.DeleteApSsidConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.radio_index):
            query['RadioIndex'] = request.radio_index
        if not UtilClient.is_unset(request.ssid):
            query['Ssid'] = request.ssid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApSsidConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.DeleteApSsidConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ap_ssid_config_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.DeleteApSsidConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.DeleteApSsidConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.radio_index):
            query['RadioIndex'] = request.radio_index
        if not UtilClient.is_unset(request.ssid):
            query['Ssid'] = request.ssid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApSsidConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.DeleteApSsidConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ap_ssid_config(
        self,
        request: cloudwifi_pop_20191118_models.DeleteApSsidConfigRequest,
    ) -> cloudwifi_pop_20191118_models.DeleteApSsidConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ap_ssid_config_with_options(request, runtime)

    async def delete_ap_ssid_config_async(
        self,
        request: cloudwifi_pop_20191118_models.DeleteApSsidConfigRequest,
    ) -> cloudwifi_pop_20191118_models.DeleteApSsidConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ap_ssid_config_with_options_async(request, runtime)

    def delete_apgroup_config_with_options(
        self,
        request: cloudwifi_pop_20191118_models.DeleteApgroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.DeleteApgroupConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_group_uuid):
            query['ApGroupUUId'] = request.ap_group_uuid
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApgroupConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.DeleteApgroupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_apgroup_config_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.DeleteApgroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.DeleteApgroupConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_group_uuid):
            query['ApGroupUUId'] = request.ap_group_uuid
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApgroupConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.DeleteApgroupConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_apgroup_config(
        self,
        request: cloudwifi_pop_20191118_models.DeleteApgroupConfigRequest,
    ) -> cloudwifi_pop_20191118_models.DeleteApgroupConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_apgroup_config_with_options(request, runtime)

    async def delete_apgroup_config_async(
        self,
        request: cloudwifi_pop_20191118_models.DeleteApgroupConfigRequest,
    ) -> cloudwifi_pop_20191118_models.DeleteApgroupConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_apgroup_config_with_options_async(request, runtime)

    def delete_apgroup_ssid_config_with_options(
        self,
        request: cloudwifi_pop_20191118_models.DeleteApgroupSsidConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.DeleteApgroupSsidConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApgroupSsidConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.DeleteApgroupSsidConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_apgroup_ssid_config_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.DeleteApgroupSsidConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.DeleteApgroupSsidConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApgroupSsidConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.DeleteApgroupSsidConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_apgroup_ssid_config(
        self,
        request: cloudwifi_pop_20191118_models.DeleteApgroupSsidConfigRequest,
    ) -> cloudwifi_pop_20191118_models.DeleteApgroupSsidConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_apgroup_ssid_config_with_options(request, runtime)

    async def delete_apgroup_ssid_config_async(
        self,
        request: cloudwifi_pop_20191118_models.DeleteApgroupSsidConfigRequest,
    ) -> cloudwifi_pop_20191118_models.DeleteApgroupSsidConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_apgroup_ssid_config_with_options_async(request, runtime)

    def delete_apgroup_third_app_with_options(
        self,
        request: cloudwifi_pop_20191118_models.DeleteApgroupThirdAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.DeleteApgroupThirdAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApgroupThirdApp',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.DeleteApgroupThirdAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_apgroup_third_app_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.DeleteApgroupThirdAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.DeleteApgroupThirdAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApgroupThirdApp',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.DeleteApgroupThirdAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_apgroup_third_app(
        self,
        request: cloudwifi_pop_20191118_models.DeleteApgroupThirdAppRequest,
    ) -> cloudwifi_pop_20191118_models.DeleteApgroupThirdAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_apgroup_third_app_with_options(request, runtime)

    async def delete_apgroup_third_app_async(
        self,
        request: cloudwifi_pop_20191118_models.DeleteApgroupThirdAppRequest,
    ) -> cloudwifi_pop_20191118_models.DeleteApgroupThirdAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_apgroup_third_app_with_options_async(request, runtime)

    def delete_net_device_info_with_options(
        self,
        request: cloudwifi_pop_20191118_models.DeleteNetDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.DeleteNetDeviceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetDeviceInfo',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.DeleteNetDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_net_device_info_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.DeleteNetDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.DeleteNetDeviceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetDeviceInfo',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.DeleteNetDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_net_device_info(
        self,
        request: cloudwifi_pop_20191118_models.DeleteNetDeviceInfoRequest,
    ) -> cloudwifi_pop_20191118_models.DeleteNetDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_net_device_info_with_options(request, runtime)

    async def delete_net_device_info_async(
        self,
        request: cloudwifi_pop_20191118_models.DeleteNetDeviceInfoRequest,
    ) -> cloudwifi_pop_20191118_models.DeleteNetDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_net_device_info_with_options_async(request, runtime)

    def edit_apgroup_third_app_with_options(
        self,
        request: cloudwifi_pop_20191118_models.EditApgroupThirdAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.EditApgroupThirdAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_data):
            query['AppData'] = request.app_data
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.apply_to_sub_group):
            query['ApplyToSubGroup'] = request.apply_to_sub_group
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.config_type):
            query['ConfigType'] = request.config_type
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.inherit_parent_group):
            query['InheritParentGroup'] = request.inherit_parent_group
        if not UtilClient.is_unset(request.third_app_name):
            query['ThirdAppName'] = request.third_app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditApgroupThirdApp',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.EditApgroupThirdAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_apgroup_third_app_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.EditApgroupThirdAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.EditApgroupThirdAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_data):
            query['AppData'] = request.app_data
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.apply_to_sub_group):
            query['ApplyToSubGroup'] = request.apply_to_sub_group
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.config_type):
            query['ConfigType'] = request.config_type
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.inherit_parent_group):
            query['InheritParentGroup'] = request.inherit_parent_group
        if not UtilClient.is_unset(request.third_app_name):
            query['ThirdAppName'] = request.third_app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditApgroupThirdApp',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.EditApgroupThirdAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_apgroup_third_app(
        self,
        request: cloudwifi_pop_20191118_models.EditApgroupThirdAppRequest,
    ) -> cloudwifi_pop_20191118_models.EditApgroupThirdAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.edit_apgroup_third_app_with_options(request, runtime)

    async def edit_apgroup_third_app_async(
        self,
        request: cloudwifi_pop_20191118_models.EditApgroupThirdAppRequest,
    ) -> cloudwifi_pop_20191118_models.EditApgroupThirdAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.edit_apgroup_third_app_with_options_async(request, runtime)

    def effect_ap_config_with_options(
        self,
        request: cloudwifi_pop_20191118_models.EffectApConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.EffectApConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EffectApConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.EffectApConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def effect_ap_config_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.EffectApConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.EffectApConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EffectApConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.EffectApConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def effect_ap_config(
        self,
        request: cloudwifi_pop_20191118_models.EffectApConfigRequest,
    ) -> cloudwifi_pop_20191118_models.EffectApConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.effect_ap_config_with_options(request, runtime)

    async def effect_ap_config_async(
        self,
        request: cloudwifi_pop_20191118_models.EffectApConfigRequest,
    ) -> cloudwifi_pop_20191118_models.EffectApConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.effect_ap_config_with_options_async(request, runtime)

    def effect_apgroup_config_with_options(
        self,
        request: cloudwifi_pop_20191118_models.EffectApgroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.EffectApgroupConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_group_uuid):
            query['ApGroupUUId'] = request.ap_group_uuid
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EffectApgroupConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.EffectApgroupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def effect_apgroup_config_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.EffectApgroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.EffectApgroupConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_group_uuid):
            query['ApGroupUUId'] = request.ap_group_uuid
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EffectApgroupConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.EffectApgroupConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def effect_apgroup_config(
        self,
        request: cloudwifi_pop_20191118_models.EffectApgroupConfigRequest,
    ) -> cloudwifi_pop_20191118_models.EffectApgroupConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.effect_apgroup_config_with_options(request, runtime)

    async def effect_apgroup_config_async(
        self,
        request: cloudwifi_pop_20191118_models.EffectApgroupConfigRequest,
    ) -> cloudwifi_pop_20191118_models.EffectApgroupConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.effect_apgroup_config_with_options_async(request, runtime)

    def get_ap_address_by_mac_with_options(
        self,
        request: cloudwifi_pop_20191118_models.GetApAddressByMacRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetApAddressByMacResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.mac):
            query['Mac'] = request.mac
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApAddressByMac',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetApAddressByMacResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ap_address_by_mac_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.GetApAddressByMacRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetApAddressByMacResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.mac):
            query['Mac'] = request.mac
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApAddressByMac',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetApAddressByMacResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ap_address_by_mac(
        self,
        request: cloudwifi_pop_20191118_models.GetApAddressByMacRequest,
    ) -> cloudwifi_pop_20191118_models.GetApAddressByMacResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ap_address_by_mac_with_options(request, runtime)

    async def get_ap_address_by_mac_async(
        self,
        request: cloudwifi_pop_20191118_models.GetApAddressByMacRequest,
    ) -> cloudwifi_pop_20191118_models.GetApAddressByMacResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ap_address_by_mac_with_options_async(request, runtime)

    def get_ap_asset_with_options(
        self,
        request: cloudwifi_pop_20191118_models.GetApAssetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetApAssetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApAsset',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetApAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ap_asset_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.GetApAssetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetApAssetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApAsset',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetApAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ap_asset(
        self,
        request: cloudwifi_pop_20191118_models.GetApAssetRequest,
    ) -> cloudwifi_pop_20191118_models.GetApAssetResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ap_asset_with_options(request, runtime)

    async def get_ap_asset_async(
        self,
        request: cloudwifi_pop_20191118_models.GetApAssetRequest,
    ) -> cloudwifi_pop_20191118_models.GetApAssetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ap_asset_with_options_async(request, runtime)

    def get_ap_detail_status_with_options(
        self,
        request: cloudwifi_pop_20191118_models.GetApDetailStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetApDetailStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.mac):
            query['Mac'] = request.mac
        if not UtilClient.is_unset(request.need_apgroup_info):
            query['NeedApgroupInfo'] = request.need_apgroup_info
        if not UtilClient.is_unset(request.need_radio_status):
            query['NeedRadioStatus'] = request.need_radio_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApDetailStatus',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetApDetailStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ap_detail_status_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.GetApDetailStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetApDetailStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.mac):
            query['Mac'] = request.mac
        if not UtilClient.is_unset(request.need_apgroup_info):
            query['NeedApgroupInfo'] = request.need_apgroup_info
        if not UtilClient.is_unset(request.need_radio_status):
            query['NeedRadioStatus'] = request.need_radio_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApDetailStatus',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetApDetailStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ap_detail_status(
        self,
        request: cloudwifi_pop_20191118_models.GetApDetailStatusRequest,
    ) -> cloudwifi_pop_20191118_models.GetApDetailStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ap_detail_status_with_options(request, runtime)

    async def get_ap_detail_status_async(
        self,
        request: cloudwifi_pop_20191118_models.GetApDetailStatusRequest,
    ) -> cloudwifi_pop_20191118_models.GetApDetailStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ap_detail_status_with_options_async(request, runtime)

    def get_ap_detailed_config_with_options(
        self,
        request: cloudwifi_pop_20191118_models.GetApDetailedConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetApDetailedConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApDetailedConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetApDetailedConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ap_detailed_config_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.GetApDetailedConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetApDetailedConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApDetailedConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetApDetailedConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ap_detailed_config(
        self,
        request: cloudwifi_pop_20191118_models.GetApDetailedConfigRequest,
    ) -> cloudwifi_pop_20191118_models.GetApDetailedConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ap_detailed_config_with_options(request, runtime)

    async def get_ap_detailed_config_async(
        self,
        request: cloudwifi_pop_20191118_models.GetApDetailedConfigRequest,
    ) -> cloudwifi_pop_20191118_models.GetApDetailedConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ap_detailed_config_with_options_async(request, runtime)

    def get_ap_info_from_pool_with_options(
        self,
        request: cloudwifi_pop_20191118_models.GetApInfoFromPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetApInfoFromPoolResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApInfoFromPool',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetApInfoFromPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ap_info_from_pool_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.GetApInfoFromPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetApInfoFromPoolResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApInfoFromPool',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetApInfoFromPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ap_info_from_pool(
        self,
        request: cloudwifi_pop_20191118_models.GetApInfoFromPoolRequest,
    ) -> cloudwifi_pop_20191118_models.GetApInfoFromPoolResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ap_info_from_pool_with_options(request, runtime)

    async def get_ap_info_from_pool_async(
        self,
        request: cloudwifi_pop_20191118_models.GetApInfoFromPoolRequest,
    ) -> cloudwifi_pop_20191118_models.GetApInfoFromPoolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ap_info_from_pool_with_options_async(request, runtime)

    def get_ap_run_history_time_ser_with_options(
        self,
        request: cloudwifi_pop_20191118_models.GetApRunHistoryTimeSerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetApRunHistoryTimeSerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApRunHistoryTimeSer',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetApRunHistoryTimeSerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ap_run_history_time_ser_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.GetApRunHistoryTimeSerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetApRunHistoryTimeSerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApRunHistoryTimeSer',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetApRunHistoryTimeSerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ap_run_history_time_ser(
        self,
        request: cloudwifi_pop_20191118_models.GetApRunHistoryTimeSerRequest,
    ) -> cloudwifi_pop_20191118_models.GetApRunHistoryTimeSerResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ap_run_history_time_ser_with_options(request, runtime)

    async def get_ap_run_history_time_ser_async(
        self,
        request: cloudwifi_pop_20191118_models.GetApRunHistoryTimeSerRequest,
    ) -> cloudwifi_pop_20191118_models.GetApRunHistoryTimeSerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ap_run_history_time_ser_with_options_async(request, runtime)

    def get_ap_status_by_group_id_with_options(
        self,
        request: cloudwifi_pop_20191118_models.GetApStatusByGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetApStatusByGroupIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cursor):
            query['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApStatusByGroupId',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetApStatusByGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ap_status_by_group_id_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.GetApStatusByGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetApStatusByGroupIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cursor):
            query['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApStatusByGroupId',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetApStatusByGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ap_status_by_group_id(
        self,
        request: cloudwifi_pop_20191118_models.GetApStatusByGroupIdRequest,
    ) -> cloudwifi_pop_20191118_models.GetApStatusByGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ap_status_by_group_id_with_options(request, runtime)

    async def get_ap_status_by_group_id_async(
        self,
        request: cloudwifi_pop_20191118_models.GetApStatusByGroupIdRequest,
    ) -> cloudwifi_pop_20191118_models.GetApStatusByGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ap_status_by_group_id_with_options_async(request, runtime)

    def get_apgroup_config_by_identity_with_options(
        self,
        request: cloudwifi_pop_20191118_models.GetApgroupConfigByIdentityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetApgroupConfigByIdentityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not UtilClient.is_unset(request.apgroup_uuid):
            query['ApgroupUuid'] = request.apgroup_uuid
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApgroupConfigByIdentity',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetApgroupConfigByIdentityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_apgroup_config_by_identity_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.GetApgroupConfigByIdentityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetApgroupConfigByIdentityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not UtilClient.is_unset(request.apgroup_uuid):
            query['ApgroupUuid'] = request.apgroup_uuid
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApgroupConfigByIdentity',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetApgroupConfigByIdentityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_apgroup_config_by_identity(
        self,
        request: cloudwifi_pop_20191118_models.GetApgroupConfigByIdentityRequest,
    ) -> cloudwifi_pop_20191118_models.GetApgroupConfigByIdentityResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_apgroup_config_by_identity_with_options(request, runtime)

    async def get_apgroup_config_by_identity_async(
        self,
        request: cloudwifi_pop_20191118_models.GetApgroupConfigByIdentityRequest,
    ) -> cloudwifi_pop_20191118_models.GetApgroupConfigByIdentityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_apgroup_config_by_identity_with_options_async(request, runtime)

    def get_apgroup_detailed_config_with_options(
        self,
        request: cloudwifi_pop_20191118_models.GetApgroupDetailedConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetApgroupDetailedConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not UtilClient.is_unset(request.apgroup_uuid):
            query['ApgroupUuid'] = request.apgroup_uuid
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApgroupDetailedConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetApgroupDetailedConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_apgroup_detailed_config_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.GetApgroupDetailedConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetApgroupDetailedConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not UtilClient.is_unset(request.apgroup_uuid):
            query['ApgroupUuid'] = request.apgroup_uuid
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApgroupDetailedConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetApgroupDetailedConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_apgroup_detailed_config(
        self,
        request: cloudwifi_pop_20191118_models.GetApgroupDetailedConfigRequest,
    ) -> cloudwifi_pop_20191118_models.GetApgroupDetailedConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_apgroup_detailed_config_with_options(request, runtime)

    async def get_apgroup_detailed_config_async(
        self,
        request: cloudwifi_pop_20191118_models.GetApgroupDetailedConfigRequest,
    ) -> cloudwifi_pop_20191118_models.GetApgroupDetailedConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_apgroup_detailed_config_with_options_async(request, runtime)

    def get_apgroup_id_with_options(
        self,
        request: cloudwifi_pop_20191118_models.GetApgroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetApgroupIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApgroupId',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetApgroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_apgroup_id_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.GetApgroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetApgroupIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApgroupId',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetApgroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_apgroup_id(
        self,
        request: cloudwifi_pop_20191118_models.GetApgroupIdRequest,
    ) -> cloudwifi_pop_20191118_models.GetApgroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_apgroup_id_with_options(request, runtime)

    async def get_apgroup_id_async(
        self,
        request: cloudwifi_pop_20191118_models.GetApgroupIdRequest,
    ) -> cloudwifi_pop_20191118_models.GetApgroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_apgroup_id_with_options_async(request, runtime)

    def get_apgroup_ssid_config_with_options(
        self,
        request: cloudwifi_pop_20191118_models.GetApgroupSsidConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetApgroupSsidConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_group_uuid):
            query['ApGroupUUId'] = request.ap_group_uuid
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApgroupSsidConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetApgroupSsidConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_apgroup_ssid_config_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.GetApgroupSsidConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetApgroupSsidConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_group_uuid):
            query['ApGroupUUId'] = request.ap_group_uuid
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApgroupSsidConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetApgroupSsidConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_apgroup_ssid_config(
        self,
        request: cloudwifi_pop_20191118_models.GetApgroupSsidConfigRequest,
    ) -> cloudwifi_pop_20191118_models.GetApgroupSsidConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_apgroup_ssid_config_with_options(request, runtime)

    async def get_apgroup_ssid_config_async(
        self,
        request: cloudwifi_pop_20191118_models.GetApgroupSsidConfigRequest,
    ) -> cloudwifi_pop_20191118_models.GetApgroupSsidConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_apgroup_ssid_config_with_options_async(request, runtime)

    def get_batch_task_progress_with_options(
        self,
        request: cloudwifi_pop_20191118_models.GetBatchTaskProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetBatchTaskProgressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBatchTaskProgress',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetBatchTaskProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_batch_task_progress_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.GetBatchTaskProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetBatchTaskProgressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBatchTaskProgress',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetBatchTaskProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_batch_task_progress(
        self,
        request: cloudwifi_pop_20191118_models.GetBatchTaskProgressRequest,
    ) -> cloudwifi_pop_20191118_models.GetBatchTaskProgressResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_batch_task_progress_with_options(request, runtime)

    async def get_batch_task_progress_async(
        self,
        request: cloudwifi_pop_20191118_models.GetBatchTaskProgressRequest,
    ) -> cloudwifi_pop_20191118_models.GetBatchTaskProgressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_batch_task_progress_with_options_async(request, runtime)

    def get_group_misc_agg_time_ser_with_options(
        self,
        request: cloudwifi_pop_20191118_models.GetGroupMiscAggTimeSerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetGroupMiscAggTimeSerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apgroup_uuid):
            query['ApgroupUuid'] = request.apgroup_uuid
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroupMiscAggTimeSer',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetGroupMiscAggTimeSerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_group_misc_agg_time_ser_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.GetGroupMiscAggTimeSerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetGroupMiscAggTimeSerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apgroup_uuid):
            query['ApgroupUuid'] = request.apgroup_uuid
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroupMiscAggTimeSer',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetGroupMiscAggTimeSerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_group_misc_agg_time_ser(
        self,
        request: cloudwifi_pop_20191118_models.GetGroupMiscAggTimeSerRequest,
    ) -> cloudwifi_pop_20191118_models.GetGroupMiscAggTimeSerResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_group_misc_agg_time_ser_with_options(request, runtime)

    async def get_group_misc_agg_time_ser_async(
        self,
        request: cloudwifi_pop_20191118_models.GetGroupMiscAggTimeSerRequest,
    ) -> cloudwifi_pop_20191118_models.GetGroupMiscAggTimeSerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_group_misc_agg_time_ser_with_options_async(request, runtime)

    def get_net_device_info_with_options(
        self,
        request: cloudwifi_pop_20191118_models.GetNetDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetNetDeviceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cursor):
            query['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.idc):
            query['Idc'] = request.idc
        if not UtilClient.is_unset(request.logic_net_pod):
            query['LogicNetPod'] = request.logic_net_pod
        if not UtilClient.is_unset(request.manufacturer):
            query['Manufacturer'] = request.manufacturer
        if not UtilClient.is_unset(request.mgn_ip):
            query['MgnIp'] = request.mgn_ip
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        if not UtilClient.is_unset(request.net_pod):
            query['NetPod'] = request.net_pod
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.service_tag):
            query['ServiceTag'] = request.service_tag
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNetDeviceInfo',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetNetDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_net_device_info_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.GetNetDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetNetDeviceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cursor):
            query['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.idc):
            query['Idc'] = request.idc
        if not UtilClient.is_unset(request.logic_net_pod):
            query['LogicNetPod'] = request.logic_net_pod
        if not UtilClient.is_unset(request.manufacturer):
            query['Manufacturer'] = request.manufacturer
        if not UtilClient.is_unset(request.mgn_ip):
            query['MgnIp'] = request.mgn_ip
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        if not UtilClient.is_unset(request.net_pod):
            query['NetPod'] = request.net_pod
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.service_tag):
            query['ServiceTag'] = request.service_tag
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNetDeviceInfo',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetNetDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_net_device_info(
        self,
        request: cloudwifi_pop_20191118_models.GetNetDeviceInfoRequest,
    ) -> cloudwifi_pop_20191118_models.GetNetDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_net_device_info_with_options(request, runtime)

    async def get_net_device_info_async(
        self,
        request: cloudwifi_pop_20191118_models.GetNetDeviceInfoRequest,
    ) -> cloudwifi_pop_20191118_models.GetNetDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_net_device_info_with_options_async(request, runtime)

    def get_net_device_info_with_size_with_options(
        self,
        request: cloudwifi_pop_20191118_models.GetNetDeviceInfoWithSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetNetDeviceInfoWithSizeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cursor):
            query['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.idc):
            query['Idc'] = request.idc
        if not UtilClient.is_unset(request.logic_net_pod):
            query['LogicNetPod'] = request.logic_net_pod
        if not UtilClient.is_unset(request.manufacturer):
            query['Manufacturer'] = request.manufacturer
        if not UtilClient.is_unset(request.mgn_ip):
            query['MgnIp'] = request.mgn_ip
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        if not UtilClient.is_unset(request.net_pod):
            query['NetPod'] = request.net_pod
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.service_tag):
            query['ServiceTag'] = request.service_tag
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNetDeviceInfoWithSize',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetNetDeviceInfoWithSizeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_net_device_info_with_size_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.GetNetDeviceInfoWithSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetNetDeviceInfoWithSizeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cursor):
            query['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.idc):
            query['Idc'] = request.idc
        if not UtilClient.is_unset(request.logic_net_pod):
            query['LogicNetPod'] = request.logic_net_pod
        if not UtilClient.is_unset(request.manufacturer):
            query['Manufacturer'] = request.manufacturer
        if not UtilClient.is_unset(request.mgn_ip):
            query['MgnIp'] = request.mgn_ip
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        if not UtilClient.is_unset(request.net_pod):
            query['NetPod'] = request.net_pod
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.service_tag):
            query['ServiceTag'] = request.service_tag
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNetDeviceInfoWithSize',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetNetDeviceInfoWithSizeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_net_device_info_with_size(
        self,
        request: cloudwifi_pop_20191118_models.GetNetDeviceInfoWithSizeRequest,
    ) -> cloudwifi_pop_20191118_models.GetNetDeviceInfoWithSizeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_net_device_info_with_size_with_options(request, runtime)

    async def get_net_device_info_with_size_async(
        self,
        request: cloudwifi_pop_20191118_models.GetNetDeviceInfoWithSizeRequest,
    ) -> cloudwifi_pop_20191118_models.GetNetDeviceInfoWithSizeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_net_device_info_with_size_with_options_async(request, runtime)

    def get_page_visit_data_with_options(
        self,
        request: cloudwifi_pop_20191118_models.GetPageVisitDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetPageVisitDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPageVisitData',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetPageVisitDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_page_visit_data_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.GetPageVisitDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetPageVisitDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPageVisitData',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetPageVisitDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_page_visit_data(
        self,
        request: cloudwifi_pop_20191118_models.GetPageVisitDataRequest,
    ) -> cloudwifi_pop_20191118_models.GetPageVisitDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_page_visit_data_with_options(request, runtime)

    async def get_page_visit_data_async(
        self,
        request: cloudwifi_pop_20191118_models.GetPageVisitDataRequest,
    ) -> cloudwifi_pop_20191118_models.GetPageVisitDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_page_visit_data_with_options_async(request, runtime)

    def get_radio_run_history_time_ser_with_options(
        self,
        request: cloudwifi_pop_20191118_models.GetRadioRunHistoryTimeSerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetRadioRunHistoryTimeSerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRadioRunHistoryTimeSer',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetRadioRunHistoryTimeSerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_radio_run_history_time_ser_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.GetRadioRunHistoryTimeSerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetRadioRunHistoryTimeSerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRadioRunHistoryTimeSer',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetRadioRunHistoryTimeSerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_radio_run_history_time_ser(
        self,
        request: cloudwifi_pop_20191118_models.GetRadioRunHistoryTimeSerRequest,
    ) -> cloudwifi_pop_20191118_models.GetRadioRunHistoryTimeSerResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_radio_run_history_time_ser_with_options(request, runtime)

    async def get_radio_run_history_time_ser_async(
        self,
        request: cloudwifi_pop_20191118_models.GetRadioRunHistoryTimeSerRequest,
    ) -> cloudwifi_pop_20191118_models.GetRadioRunHistoryTimeSerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_radio_run_history_time_ser_with_options_async(request, runtime)

    def get_sta_detailed_status_by_mac_with_options(
        self,
        request: cloudwifi_pop_20191118_models.GetStaDetailedStatusByMacRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetStaDetailedStatusByMacResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.sta_mac):
            query['StaMac'] = request.sta_mac
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStaDetailedStatusByMac',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetStaDetailedStatusByMacResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sta_detailed_status_by_mac_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.GetStaDetailedStatusByMacRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetStaDetailedStatusByMacResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.sta_mac):
            query['StaMac'] = request.sta_mac
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStaDetailedStatusByMac',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetStaDetailedStatusByMacResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sta_detailed_status_by_mac(
        self,
        request: cloudwifi_pop_20191118_models.GetStaDetailedStatusByMacRequest,
    ) -> cloudwifi_pop_20191118_models.GetStaDetailedStatusByMacResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sta_detailed_status_by_mac_with_options(request, runtime)

    async def get_sta_detailed_status_by_mac_async(
        self,
        request: cloudwifi_pop_20191118_models.GetStaDetailedStatusByMacRequest,
    ) -> cloudwifi_pop_20191118_models.GetStaDetailedStatusByMacResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sta_detailed_status_by_mac_with_options_async(request, runtime)

    def get_sta_status_list_by_ap_with_options(
        self,
        request: cloudwifi_pop_20191118_models.GetStaStatusListByApRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetStaStatusListByApResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cursor):
            query['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStaStatusListByAp',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetStaStatusListByApResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sta_status_list_by_ap_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.GetStaStatusListByApRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.GetStaStatusListByApResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cursor):
            query['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStaStatusListByAp',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.GetStaStatusListByApResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sta_status_list_by_ap(
        self,
        request: cloudwifi_pop_20191118_models.GetStaStatusListByApRequest,
    ) -> cloudwifi_pop_20191118_models.GetStaStatusListByApResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sta_status_list_by_ap_with_options(request, runtime)

    async def get_sta_status_list_by_ap_async(
        self,
        request: cloudwifi_pop_20191118_models.GetStaStatusListByApRequest,
    ) -> cloudwifi_pop_20191118_models.GetStaStatusListByApResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sta_status_list_by_ap_with_options_async(request, runtime)

    def judge_xing_tian_business_with_options(
        self,
        request: cloudwifi_pop_20191118_models.JudgeXingTianBusinessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.JudgeXingTianBusinessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.realm_id):
            query['RealmId'] = request.realm_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='JudgeXingTianBusiness',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.JudgeXingTianBusinessResponse(),
            self.call_api(params, req, runtime)
        )

    async def judge_xing_tian_business_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.JudgeXingTianBusinessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.JudgeXingTianBusinessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.realm_id):
            query['RealmId'] = request.realm_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='JudgeXingTianBusiness',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.JudgeXingTianBusinessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def judge_xing_tian_business(
        self,
        request: cloudwifi_pop_20191118_models.JudgeXingTianBusinessRequest,
    ) -> cloudwifi_pop_20191118_models.JudgeXingTianBusinessResponse:
        runtime = util_models.RuntimeOptions()
        return self.judge_xing_tian_business_with_options(request, runtime)

    async def judge_xing_tian_business_async(
        self,
        request: cloudwifi_pop_20191118_models.JudgeXingTianBusinessRequest,
    ) -> cloudwifi_pop_20191118_models.JudgeXingTianBusinessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.judge_xing_tian_business_with_options_async(request, runtime)

    def kick_sta_with_options(
        self,
        request: cloudwifi_pop_20191118_models.KickStaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.KickStaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.sta_mac):
            query['StaMac'] = request.sta_mac
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='KickSta',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.KickStaResponse(),
            self.call_api(params, req, runtime)
        )

    async def kick_sta_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.KickStaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.KickStaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.sta_mac):
            query['StaMac'] = request.sta_mac
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='KickSta',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.KickStaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kick_sta(
        self,
        request: cloudwifi_pop_20191118_models.KickStaRequest,
    ) -> cloudwifi_pop_20191118_models.KickStaResponse:
        runtime = util_models.RuntimeOptions()
        return self.kick_sta_with_options(request, runtime)

    async def kick_sta_async(
        self,
        request: cloudwifi_pop_20191118_models.KickStaRequest,
    ) -> cloudwifi_pop_20191118_models.KickStaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.kick_sta_with_options_async(request, runtime)

    def list_apgroup_descendant_with_options(
        self,
        request: cloudwifi_pop_20191118_models.ListApgroupDescendantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.ListApgroupDescendantResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not UtilClient.is_unset(request.apgroup_uuid):
            query['ApgroupUuid'] = request.apgroup_uuid
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cursor):
            query['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApgroupDescendant',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.ListApgroupDescendantResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_apgroup_descendant_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.ListApgroupDescendantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.ListApgroupDescendantResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not UtilClient.is_unset(request.apgroup_uuid):
            query['ApgroupUuid'] = request.apgroup_uuid
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cursor):
            query['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApgroupDescendant',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.ListApgroupDescendantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_apgroup_descendant(
        self,
        request: cloudwifi_pop_20191118_models.ListApgroupDescendantRequest,
    ) -> cloudwifi_pop_20191118_models.ListApgroupDescendantResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_apgroup_descendant_with_options(request, runtime)

    async def list_apgroup_descendant_async(
        self,
        request: cloudwifi_pop_20191118_models.ListApgroupDescendantRequest,
    ) -> cloudwifi_pop_20191118_models.ListApgroupDescendantResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_apgroup_descendant_with_options_async(request, runtime)

    def list_job_orders_with_options(
        self,
        request: cloudwifi_pop_20191118_models.ListJobOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.ListJobOrdersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.changing_type):
            query['ChangingType'] = request.changing_type
        if not UtilClient.is_unset(request.client_system):
            query['ClientSystem'] = request.client_system
        if not UtilClient.is_unset(request.client_unique_id):
            query['ClientUniqueId'] = request.client_unique_id
        if not UtilClient.is_unset(request.cursor):
            query['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.handler):
            query['Handler'] = request.handler
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.order_status):
            query['OrderStatus'] = request.order_status
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobOrders',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.ListJobOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_orders_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.ListJobOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.ListJobOrdersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.changing_type):
            query['ChangingType'] = request.changing_type
        if not UtilClient.is_unset(request.client_system):
            query['ClientSystem'] = request.client_system
        if not UtilClient.is_unset(request.client_unique_id):
            query['ClientUniqueId'] = request.client_unique_id
        if not UtilClient.is_unset(request.cursor):
            query['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.handler):
            query['Handler'] = request.handler
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.order_status):
            query['OrderStatus'] = request.order_status
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobOrders',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.ListJobOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_orders(
        self,
        request: cloudwifi_pop_20191118_models.ListJobOrdersRequest,
    ) -> cloudwifi_pop_20191118_models.ListJobOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_job_orders_with_options(request, runtime)

    async def list_job_orders_async(
        self,
        request: cloudwifi_pop_20191118_models.ListJobOrdersRequest,
    ) -> cloudwifi_pop_20191118_models.ListJobOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_job_orders_with_options_async(request, runtime)

    def list_job_orders_with_size_with_options(
        self,
        request: cloudwifi_pop_20191118_models.ListJobOrdersWithSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.ListJobOrdersWithSizeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.changing_type):
            query['ChangingType'] = request.changing_type
        if not UtilClient.is_unset(request.client_system):
            query['ClientSystem'] = request.client_system
        if not UtilClient.is_unset(request.client_unique_id):
            query['ClientUniqueId'] = request.client_unique_id
        if not UtilClient.is_unset(request.cursor):
            query['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.handler):
            query['Handler'] = request.handler
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.order_status):
            query['OrderStatus'] = request.order_status
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobOrdersWithSize',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.ListJobOrdersWithSizeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_orders_with_size_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.ListJobOrdersWithSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.ListJobOrdersWithSizeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.changing_type):
            query['ChangingType'] = request.changing_type
        if not UtilClient.is_unset(request.client_system):
            query['ClientSystem'] = request.client_system
        if not UtilClient.is_unset(request.client_unique_id):
            query['ClientUniqueId'] = request.client_unique_id
        if not UtilClient.is_unset(request.cursor):
            query['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.handler):
            query['Handler'] = request.handler
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.order_status):
            query['OrderStatus'] = request.order_status
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobOrdersWithSize',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.ListJobOrdersWithSizeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_orders_with_size(
        self,
        request: cloudwifi_pop_20191118_models.ListJobOrdersWithSizeRequest,
    ) -> cloudwifi_pop_20191118_models.ListJobOrdersWithSizeResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_job_orders_with_size_with_options(request, runtime)

    async def list_job_orders_with_size_async(
        self,
        request: cloudwifi_pop_20191118_models.ListJobOrdersWithSizeRequest,
    ) -> cloudwifi_pop_20191118_models.ListJobOrdersWithSizeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_job_orders_with_size_with_options_async(request, runtime)

    def new_apgroup_config_with_options(
        self,
        request: cloudwifi_pop_20191118_models.NewApgroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.NewApgroupConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parent_apgroup_id):
            query['ParentApgroupId'] = request.parent_apgroup_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NewApgroupConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.NewApgroupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def new_apgroup_config_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.NewApgroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.NewApgroupConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parent_apgroup_id):
            query['ParentApgroupId'] = request.parent_apgroup_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NewApgroupConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.NewApgroupConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def new_apgroup_config(
        self,
        request: cloudwifi_pop_20191118_models.NewApgroupConfigRequest,
    ) -> cloudwifi_pop_20191118_models.NewApgroupConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.new_apgroup_config_with_options(request, runtime)

    async def new_apgroup_config_async(
        self,
        request: cloudwifi_pop_20191118_models.NewApgroupConfigRequest,
    ) -> cloudwifi_pop_20191118_models.NewApgroupConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.new_apgroup_config_with_options_async(request, runtime)

    def new_job_order_with_options(
        self,
        tmp_req: cloudwifi_pop_20191118_models.NewJobOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.NewJobOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = cloudwifi_pop_20191118_models.NewJobOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.params):
            request.params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.change_type):
            query['ChangeType'] = request.change_type
        if not UtilClient.is_unset(request.client_system):
            query['ClientSystem'] = request.client_system
        if not UtilClient.is_unset(request.client_unique_id):
            query['ClientUniqueId'] = request.client_unique_id
        if not UtilClient.is_unset(request.creator):
            query['Creator'] = request.creator
        if not UtilClient.is_unset(request.refer_url):
            query['ReferUrl'] = request.refer_url
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        body = {}
        if not UtilClient.is_unset(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='NewJobOrder',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.NewJobOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def new_job_order_with_options_async(
        self,
        tmp_req: cloudwifi_pop_20191118_models.NewJobOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.NewJobOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = cloudwifi_pop_20191118_models.NewJobOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.params):
            request.params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.params, 'Params', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.change_type):
            query['ChangeType'] = request.change_type
        if not UtilClient.is_unset(request.client_system):
            query['ClientSystem'] = request.client_system
        if not UtilClient.is_unset(request.client_unique_id):
            query['ClientUniqueId'] = request.client_unique_id
        if not UtilClient.is_unset(request.creator):
            query['Creator'] = request.creator
        if not UtilClient.is_unset(request.refer_url):
            query['ReferUrl'] = request.refer_url
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        body = {}
        if not UtilClient.is_unset(request.params_shrink):
            body['Params'] = request.params_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='NewJobOrder',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.NewJobOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def new_job_order(
        self,
        request: cloudwifi_pop_20191118_models.NewJobOrderRequest,
    ) -> cloudwifi_pop_20191118_models.NewJobOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.new_job_order_with_options(request, runtime)

    async def new_job_order_async(
        self,
        request: cloudwifi_pop_20191118_models.NewJobOrderRequest,
    ) -> cloudwifi_pop_20191118_models.NewJobOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.new_job_order_with_options_async(request, runtime)

    def new_net_device_info_with_options(
        self,
        request: cloudwifi_pop_20191118_models.NewNetDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.NewNetDeviceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.devices):
            body['Devices'] = request.devices
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='NewNetDeviceInfo',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.NewNetDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def new_net_device_info_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.NewNetDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.NewNetDeviceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.devices):
            body['Devices'] = request.devices
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='NewNetDeviceInfo',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.NewNetDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def new_net_device_info(
        self,
        request: cloudwifi_pop_20191118_models.NewNetDeviceInfoRequest,
    ) -> cloudwifi_pop_20191118_models.NewNetDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.new_net_device_info_with_options(request, runtime)

    async def new_net_device_info_async(
        self,
        request: cloudwifi_pop_20191118_models.NewNetDeviceInfoRequest,
    ) -> cloudwifi_pop_20191118_models.NewNetDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.new_net_device_info_with_options_async(request, runtime)

    def put_app_config_and_save_with_options(
        self,
        request: cloudwifi_pop_20191118_models.PutAppConfigAndSaveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.PutAppConfigAndSaveResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.configure_type):
            query['ConfigureType'] = request.configure_type
        if not UtilClient.is_unset(request.current_time):
            query['CurrentTime'] = request.current_time
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutAppConfigAndSave',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.PutAppConfigAndSaveResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_app_config_and_save_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.PutAppConfigAndSaveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.PutAppConfigAndSaveResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.configure_type):
            query['ConfigureType'] = request.configure_type
        if not UtilClient.is_unset(request.current_time):
            query['CurrentTime'] = request.current_time
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutAppConfigAndSave',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.PutAppConfigAndSaveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_app_config_and_save(
        self,
        request: cloudwifi_pop_20191118_models.PutAppConfigAndSaveRequest,
    ) -> cloudwifi_pop_20191118_models.PutAppConfigAndSaveResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_app_config_and_save_with_options(request, runtime)

    async def put_app_config_and_save_async(
        self,
        request: cloudwifi_pop_20191118_models.PutAppConfigAndSaveRequest,
    ) -> cloudwifi_pop_20191118_models.PutAppConfigAndSaveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_app_config_and_save_with_options_async(request, runtime)

    def query_job_order_with_options(
        self,
        request: cloudwifi_pop_20191118_models.QueryJobOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.QueryJobOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryJobOrder',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.QueryJobOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_job_order_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.QueryJobOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.QueryJobOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryJobOrder',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.QueryJobOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_job_order(
        self,
        request: cloudwifi_pop_20191118_models.QueryJobOrderRequest,
    ) -> cloudwifi_pop_20191118_models.QueryJobOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_job_order_with_options(request, runtime)

    async def query_job_order_async(
        self,
        request: cloudwifi_pop_20191118_models.QueryJobOrderRequest,
    ) -> cloudwifi_pop_20191118_models.QueryJobOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_job_order_with_options_async(request, runtime)

    def reboot_ap_with_options(
        self,
        request: cloudwifi_pop_20191118_models.RebootApRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.RebootApResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootAp',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.RebootApResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_ap_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.RebootApRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.RebootApResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootAp',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.RebootApResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reboot_ap(
        self,
        request: cloudwifi_pop_20191118_models.RebootApRequest,
    ) -> cloudwifi_pop_20191118_models.RebootApResponse:
        runtime = util_models.RuntimeOptions()
        return self.reboot_ap_with_options(request, runtime)

    async def reboot_ap_async(
        self,
        request: cloudwifi_pop_20191118_models.RebootApRequest,
    ) -> cloudwifi_pop_20191118_models.RebootApResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reboot_ap_with_options_async(request, runtime)

    def register_ap_asset_with_options(
        self,
        request: cloudwifi_pop_20191118_models.RegisterApAssetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.RegisterApAssetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_group_uuid):
            query['ApGroupUUId'] = request.ap_group_uuid
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.mac):
            query['Mac'] = request.mac
        if not UtilClient.is_unset(request.serial_no):
            query['SerialNo'] = request.serial_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterApAsset',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.RegisterApAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_ap_asset_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.RegisterApAssetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.RegisterApAssetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_group_uuid):
            query['ApGroupUUId'] = request.ap_group_uuid
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.mac):
            query['Mac'] = request.mac
        if not UtilClient.is_unset(request.serial_no):
            query['SerialNo'] = request.serial_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterApAsset',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.RegisterApAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_ap_asset(
        self,
        request: cloudwifi_pop_20191118_models.RegisterApAssetRequest,
    ) -> cloudwifi_pop_20191118_models.RegisterApAssetResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_ap_asset_with_options(request, runtime)

    async def register_ap_asset_async(
        self,
        request: cloudwifi_pop_20191118_models.RegisterApAssetRequest,
    ) -> cloudwifi_pop_20191118_models.RegisterApAssetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_ap_asset_with_options_async(request, runtime)

    def repair_ap_radio_with_options(
        self,
        request: cloudwifi_pop_20191118_models.RepairApRadioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.RepairApRadioResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.radio_index):
            query['RadioIndex'] = request.radio_index
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RepairApRadio',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.RepairApRadioResponse(),
            self.call_api(params, req, runtime)
        )

    async def repair_ap_radio_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.RepairApRadioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.RepairApRadioResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.radio_index):
            query['RadioIndex'] = request.radio_index
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RepairApRadio',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.RepairApRadioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def repair_ap_radio(
        self,
        request: cloudwifi_pop_20191118_models.RepairApRadioRequest,
    ) -> cloudwifi_pop_20191118_models.RepairApRadioResponse:
        runtime = util_models.RuntimeOptions()
        return self.repair_ap_radio_with_options(request, runtime)

    async def repair_ap_radio_async(
        self,
        request: cloudwifi_pop_20191118_models.RepairApRadioRequest,
    ) -> cloudwifi_pop_20191118_models.RepairApRadioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.repair_ap_radio_with_options_async(request, runtime)

    def save_ap_basic_config_with_options(
        self,
        request: cloudwifi_pop_20191118_models.SaveApBasicConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.SaveApBasicConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.dai):
            query['Dai'] = request.dai
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.echo_int):
            query['EchoInt'] = request.echo_int
        if not UtilClient.is_unset(request.failover):
            query['Failover'] = request.failover
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.insecure_allowed):
            query['InsecureAllowed'] = request.insecure_allowed
        if not UtilClient.is_unset(request.lan_ip):
            query['LanIp'] = request.lan_ip
        if not UtilClient.is_unset(request.lan_mask):
            query['LanMask'] = request.lan_mask
        if not UtilClient.is_unset(request.lan_status):
            query['LanStatus'] = request.lan_status
        if not UtilClient.is_unset(request.log_ip):
            query['LogIp'] = request.log_ip
        if not UtilClient.is_unset(request.log_level):
            query['LogLevel'] = request.log_level
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.passwd):
            query['Passwd'] = request.passwd
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.route):
            query['Route'] = request.route
        if not UtilClient.is_unset(request.scan):
            query['Scan'] = request.scan
        if not UtilClient.is_unset(request.token_server):
            query['TokenServer'] = request.token_server
        if not UtilClient.is_unset(request.vpn):
            query['Vpn'] = request.vpn
        if not UtilClient.is_unset(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveApBasicConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.SaveApBasicConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_ap_basic_config_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.SaveApBasicConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.SaveApBasicConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.dai):
            query['Dai'] = request.dai
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.echo_int):
            query['EchoInt'] = request.echo_int
        if not UtilClient.is_unset(request.failover):
            query['Failover'] = request.failover
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.insecure_allowed):
            query['InsecureAllowed'] = request.insecure_allowed
        if not UtilClient.is_unset(request.lan_ip):
            query['LanIp'] = request.lan_ip
        if not UtilClient.is_unset(request.lan_mask):
            query['LanMask'] = request.lan_mask
        if not UtilClient.is_unset(request.lan_status):
            query['LanStatus'] = request.lan_status
        if not UtilClient.is_unset(request.log_ip):
            query['LogIp'] = request.log_ip
        if not UtilClient.is_unset(request.log_level):
            query['LogLevel'] = request.log_level
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.passwd):
            query['Passwd'] = request.passwd
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.route):
            query['Route'] = request.route
        if not UtilClient.is_unset(request.scan):
            query['Scan'] = request.scan
        if not UtilClient.is_unset(request.token_server):
            query['TokenServer'] = request.token_server
        if not UtilClient.is_unset(request.vpn):
            query['Vpn'] = request.vpn
        if not UtilClient.is_unset(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveApBasicConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.SaveApBasicConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_ap_basic_config(
        self,
        request: cloudwifi_pop_20191118_models.SaveApBasicConfigRequest,
    ) -> cloudwifi_pop_20191118_models.SaveApBasicConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_ap_basic_config_with_options(request, runtime)

    async def save_ap_basic_config_async(
        self,
        request: cloudwifi_pop_20191118_models.SaveApBasicConfigRequest,
    ) -> cloudwifi_pop_20191118_models.SaveApBasicConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_ap_basic_config_with_options_async(request, runtime)

    def save_ap_portal_config_with_options(
        self,
        tmp_req: cloudwifi_pop_20191118_models.SaveApPortalConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.SaveApPortalConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = cloudwifi_pop_20191118_models.SaveApPortalConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.portal_types):
            request.portal_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.portal_types, 'PortalTypes', 'simple')
        query = {}
        if not UtilClient.is_unset(request.ap_config_id):
            query['ApConfigId'] = request.ap_config_id
        if not UtilClient.is_unset(request.app_auth_url):
            query['AppAuthUrl'] = request.app_auth_url
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_secret):
            query['AuthSecret'] = request.auth_secret
        if not UtilClient.is_unset(request.check_url):
            query['CheckUrl'] = request.check_url
        if not UtilClient.is_unset(request.client_download):
            query['ClientDownload'] = request.client_download
        if not UtilClient.is_unset(request.client_upload):
            query['ClientUpload'] = request.client_upload
        if not UtilClient.is_unset(request.countdown):
            query['Countdown'] = request.countdown
        if not UtilClient.is_unset(request.network):
            query['Network'] = request.network
        if not UtilClient.is_unset(request.portal_types_shrink):
            query['PortalTypes'] = request.portal_types_shrink
        if not UtilClient.is_unset(request.portal_url):
            query['PortalUrl'] = request.portal_url
        if not UtilClient.is_unset(request.time_stamp):
            query['TimeStamp'] = request.time_stamp
        if not UtilClient.is_unset(request.total_download):
            query['TotalDownload'] = request.total_download
        if not UtilClient.is_unset(request.total_upload):
            query['TotalUpload'] = request.total_upload
        if not UtilClient.is_unset(request.web_auth_url):
            query['WebAuthUrl'] = request.web_auth_url
        if not UtilClient.is_unset(request.whitelist):
            query['Whitelist'] = request.whitelist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveApPortalConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.SaveApPortalConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_ap_portal_config_with_options_async(
        self,
        tmp_req: cloudwifi_pop_20191118_models.SaveApPortalConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.SaveApPortalConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = cloudwifi_pop_20191118_models.SaveApPortalConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.portal_types):
            request.portal_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.portal_types, 'PortalTypes', 'simple')
        query = {}
        if not UtilClient.is_unset(request.ap_config_id):
            query['ApConfigId'] = request.ap_config_id
        if not UtilClient.is_unset(request.app_auth_url):
            query['AppAuthUrl'] = request.app_auth_url
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_secret):
            query['AuthSecret'] = request.auth_secret
        if not UtilClient.is_unset(request.check_url):
            query['CheckUrl'] = request.check_url
        if not UtilClient.is_unset(request.client_download):
            query['ClientDownload'] = request.client_download
        if not UtilClient.is_unset(request.client_upload):
            query['ClientUpload'] = request.client_upload
        if not UtilClient.is_unset(request.countdown):
            query['Countdown'] = request.countdown
        if not UtilClient.is_unset(request.network):
            query['Network'] = request.network
        if not UtilClient.is_unset(request.portal_types_shrink):
            query['PortalTypes'] = request.portal_types_shrink
        if not UtilClient.is_unset(request.portal_url):
            query['PortalUrl'] = request.portal_url
        if not UtilClient.is_unset(request.time_stamp):
            query['TimeStamp'] = request.time_stamp
        if not UtilClient.is_unset(request.total_download):
            query['TotalDownload'] = request.total_download
        if not UtilClient.is_unset(request.total_upload):
            query['TotalUpload'] = request.total_upload
        if not UtilClient.is_unset(request.web_auth_url):
            query['WebAuthUrl'] = request.web_auth_url
        if not UtilClient.is_unset(request.whitelist):
            query['Whitelist'] = request.whitelist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveApPortalConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.SaveApPortalConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_ap_portal_config(
        self,
        request: cloudwifi_pop_20191118_models.SaveApPortalConfigRequest,
    ) -> cloudwifi_pop_20191118_models.SaveApPortalConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_ap_portal_config_with_options(request, runtime)

    async def save_ap_portal_config_async(
        self,
        request: cloudwifi_pop_20191118_models.SaveApPortalConfigRequest,
    ) -> cloudwifi_pop_20191118_models.SaveApPortalConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_ap_portal_config_with_options_async(request, runtime)

    def save_ap_radio_config_with_options(
        self,
        request: cloudwifi_pop_20191118_models.SaveApRadioConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.SaveApRadioConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.bcast_rate):
            query['BcastRate'] = request.bcast_rate
        if not UtilClient.is_unset(request.beacon_int):
            query['BeaconInt'] = request.beacon_int
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.disabled):
            query['Disabled'] = request.disabled
        if not UtilClient.is_unset(request.frag):
            query['Frag'] = request.frag
        if not UtilClient.is_unset(request.htmode):
            query['Htmode'] = request.htmode
        if not UtilClient.is_unset(request.hwmode):
            query['Hwmode'] = request.hwmode
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.mcast_rate):
            query['McastRate'] = request.mcast_rate
        if not UtilClient.is_unset(request.mgmt_rate):
            query['MgmtRate'] = request.mgmt_rate
        if not UtilClient.is_unset(request.minrate):
            query['Minrate'] = request.minrate
        if not UtilClient.is_unset(request.noscan):
            query['Noscan'] = request.noscan
        if not UtilClient.is_unset(request.probereq):
            query['Probereq'] = request.probereq
        if not UtilClient.is_unset(request.require_mode):
            query['RequireMode'] = request.require_mode
        if not UtilClient.is_unset(request.rts):
            query['Rts'] = request.rts
        if not UtilClient.is_unset(request.shortgi):
            query['Shortgi'] = request.shortgi
        if not UtilClient.is_unset(request.txpower):
            query['Txpower'] = request.txpower
        if not UtilClient.is_unset(request.uapsd):
            query['Uapsd'] = request.uapsd
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveApRadioConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.SaveApRadioConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_ap_radio_config_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.SaveApRadioConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.SaveApRadioConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.bcast_rate):
            query['BcastRate'] = request.bcast_rate
        if not UtilClient.is_unset(request.beacon_int):
            query['BeaconInt'] = request.beacon_int
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.disabled):
            query['Disabled'] = request.disabled
        if not UtilClient.is_unset(request.frag):
            query['Frag'] = request.frag
        if not UtilClient.is_unset(request.htmode):
            query['Htmode'] = request.htmode
        if not UtilClient.is_unset(request.hwmode):
            query['Hwmode'] = request.hwmode
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.mcast_rate):
            query['McastRate'] = request.mcast_rate
        if not UtilClient.is_unset(request.mgmt_rate):
            query['MgmtRate'] = request.mgmt_rate
        if not UtilClient.is_unset(request.minrate):
            query['Minrate'] = request.minrate
        if not UtilClient.is_unset(request.noscan):
            query['Noscan'] = request.noscan
        if not UtilClient.is_unset(request.probereq):
            query['Probereq'] = request.probereq
        if not UtilClient.is_unset(request.require_mode):
            query['RequireMode'] = request.require_mode
        if not UtilClient.is_unset(request.rts):
            query['Rts'] = request.rts
        if not UtilClient.is_unset(request.shortgi):
            query['Shortgi'] = request.shortgi
        if not UtilClient.is_unset(request.txpower):
            query['Txpower'] = request.txpower
        if not UtilClient.is_unset(request.uapsd):
            query['Uapsd'] = request.uapsd
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveApRadioConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.SaveApRadioConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_ap_radio_config(
        self,
        request: cloudwifi_pop_20191118_models.SaveApRadioConfigRequest,
    ) -> cloudwifi_pop_20191118_models.SaveApRadioConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_ap_radio_config_with_options(request, runtime)

    async def save_ap_radio_config_async(
        self,
        request: cloudwifi_pop_20191118_models.SaveApRadioConfigRequest,
    ) -> cloudwifi_pop_20191118_models.SaveApRadioConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_ap_radio_config_with_options_async(request, runtime)

    def save_ap_ssid_config_with_options(
        self,
        request: cloudwifi_pop_20191118_models.SaveApSsidConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.SaveApSsidConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acct_port):
            query['AcctPort'] = request.acct_port
        if not UtilClient.is_unset(request.acct_secret):
            query['AcctSecret'] = request.acct_secret
        if not UtilClient.is_unset(request.acct_server):
            query['AcctServer'] = request.acct_server
        if not UtilClient.is_unset(request.acct_status_server_work):
            query['AcctStatusServerWork'] = request.acct_status_server_work
        if not UtilClient.is_unset(request.ap_asset_id):
            query['ApAssetId'] = request.ap_asset_id
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.arp_proxy_enable):
            query['ArpProxyEnable'] = request.arp_proxy_enable
        if not UtilClient.is_unset(request.auth_cache):
            query['AuthCache'] = request.auth_cache
        if not UtilClient.is_unset(request.auth_port):
            query['AuthPort'] = request.auth_port
        if not UtilClient.is_unset(request.auth_secret):
            query['AuthSecret'] = request.auth_secret
        if not UtilClient.is_unset(request.auth_server):
            query['AuthServer'] = request.auth_server
        if not UtilClient.is_unset(request.auth_status_server_work):
            query['AuthStatusServerWork'] = request.auth_status_server_work
        if not UtilClient.is_unset(request.cir):
            query['Cir'] = request.cir
        if not UtilClient.is_unset(request.cir_step):
            query['CirStep'] = request.cir_step
        if not UtilClient.is_unset(request.cir_type):
            query['CirType'] = request.cir_type
        if not UtilClient.is_unset(request.cir_ul):
            query['CirUl'] = request.cir_ul
        if not UtilClient.is_unset(request.dae_client):
            query['DaeClient'] = request.dae_client
        if not UtilClient.is_unset(request.dae_port):
            query['DaePort'] = request.dae_port
        if not UtilClient.is_unset(request.dae_secret):
            query['DaeSecret'] = request.dae_secret
        if not UtilClient.is_unset(request.disabled):
            query['Disabled'] = request.disabled
        if not UtilClient.is_unset(request.disassoc_low_ack):
            query['DisassocLowAck'] = request.disassoc_low_ack
        if not UtilClient.is_unset(request.disassoc_weak_rssi):
            query['DisassocWeakRssi'] = request.disassoc_weak_rssi
        if not UtilClient.is_unset(request.dynamic_vlan):
            query['DynamicVlan'] = request.dynamic_vlan
        if not UtilClient.is_unset(request.enc_key):
            query['EncKey'] = request.enc_key
        if not UtilClient.is_unset(request.encryption):
            query['Encryption'] = request.encryption
        if not UtilClient.is_unset(request.fourth_auth_port):
            query['FourthAuthPort'] = request.fourth_auth_port
        if not UtilClient.is_unset(request.fourth_auth_secret):
            query['FourthAuthSecret'] = request.fourth_auth_secret
        if not UtilClient.is_unset(request.fourth_auth_server):
            query['FourthAuthServer'] = request.fourth_auth_server
        if not UtilClient.is_unset(request.ft_over_ds):
            query['FtOverDs'] = request.ft_over_ds
        if not UtilClient.is_unset(request.hidden):
            query['Hidden'] = request.hidden
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ieee_80211r):
            query['Ieee80211r'] = request.ieee_80211r
        if not UtilClient.is_unset(request.ieee_80211w):
            query['Ieee80211w'] = request.ieee_80211w
        if not UtilClient.is_unset(request.ignore_weak_probe):
            query['IgnoreWeakProbe'] = request.ignore_weak_probe
        if not UtilClient.is_unset(request.isolate):
            query['Isolate'] = request.isolate
        if not UtilClient.is_unset(request.lite_effect):
            query['LiteEffect'] = request.lite_effect
        if not UtilClient.is_unset(request.mac):
            query['Mac'] = request.mac
        if not UtilClient.is_unset(request.max_inactivity):
            query['MaxInactivity'] = request.max_inactivity
        if not UtilClient.is_unset(request.maxassoc):
            query['Maxassoc'] = request.maxassoc
        if not UtilClient.is_unset(request.mobility_domain):
            query['MobilityDomain'] = request.mobility_domain
        if not UtilClient.is_unset(request.multicast_forward):
            query['MulticastForward'] = request.multicast_forward
        if not UtilClient.is_unset(request.nasid):
            query['Nasid'] = request.nasid
        if not UtilClient.is_unset(request.nd_proxy_work):
            query['NdProxyWork'] = request.nd_proxy_work
        if not UtilClient.is_unset(request.network):
            query['Network'] = request.network
        if not UtilClient.is_unset(request.ownip):
            query['Ownip'] = request.ownip
        if not UtilClient.is_unset(request.radio_index):
            query['RadioIndex'] = request.radio_index
        if not UtilClient.is_unset(request.secondary_acct_port):
            query['SecondaryAcctPort'] = request.secondary_acct_port
        if not UtilClient.is_unset(request.secondary_acct_secret):
            query['SecondaryAcctSecret'] = request.secondary_acct_secret
        if not UtilClient.is_unset(request.secondary_acct_server):
            query['SecondaryAcctServer'] = request.secondary_acct_server
        if not UtilClient.is_unset(request.secondary_auth_port):
            query['SecondaryAuthPort'] = request.secondary_auth_port
        if not UtilClient.is_unset(request.secondary_auth_secret):
            query['SecondaryAuthSecret'] = request.secondary_auth_secret
        if not UtilClient.is_unset(request.secondary_auth_server):
            query['SecondaryAuthServer'] = request.secondary_auth_server
        if not UtilClient.is_unset(request.send_config_to_ap):
            query['SendConfigToAp'] = request.send_config_to_ap
        if not UtilClient.is_unset(request.short_preamble):
            query['ShortPreamble'] = request.short_preamble
        if not UtilClient.is_unset(request.ssid):
            query['Ssid'] = request.ssid
        if not UtilClient.is_unset(request.ssid_lb):
            query['SsidLb'] = request.ssid_lb
        if not UtilClient.is_unset(request.third_auth_port):
            query['ThirdAuthPort'] = request.third_auth_port
        if not UtilClient.is_unset(request.third_auth_secret):
            query['ThirdAuthSecret'] = request.third_auth_secret
        if not UtilClient.is_unset(request.third_auth_server):
            query['ThirdAuthServer'] = request.third_auth_server
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vlan_dhcp):
            query['VlanDhcp'] = request.vlan_dhcp
        if not UtilClient.is_unset(request.wmm):
            query['Wmm'] = request.wmm
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveApSsidConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.SaveApSsidConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_ap_ssid_config_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.SaveApSsidConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.SaveApSsidConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acct_port):
            query['AcctPort'] = request.acct_port
        if not UtilClient.is_unset(request.acct_secret):
            query['AcctSecret'] = request.acct_secret
        if not UtilClient.is_unset(request.acct_server):
            query['AcctServer'] = request.acct_server
        if not UtilClient.is_unset(request.acct_status_server_work):
            query['AcctStatusServerWork'] = request.acct_status_server_work
        if not UtilClient.is_unset(request.ap_asset_id):
            query['ApAssetId'] = request.ap_asset_id
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.arp_proxy_enable):
            query['ArpProxyEnable'] = request.arp_proxy_enable
        if not UtilClient.is_unset(request.auth_cache):
            query['AuthCache'] = request.auth_cache
        if not UtilClient.is_unset(request.auth_port):
            query['AuthPort'] = request.auth_port
        if not UtilClient.is_unset(request.auth_secret):
            query['AuthSecret'] = request.auth_secret
        if not UtilClient.is_unset(request.auth_server):
            query['AuthServer'] = request.auth_server
        if not UtilClient.is_unset(request.auth_status_server_work):
            query['AuthStatusServerWork'] = request.auth_status_server_work
        if not UtilClient.is_unset(request.cir):
            query['Cir'] = request.cir
        if not UtilClient.is_unset(request.cir_step):
            query['CirStep'] = request.cir_step
        if not UtilClient.is_unset(request.cir_type):
            query['CirType'] = request.cir_type
        if not UtilClient.is_unset(request.cir_ul):
            query['CirUl'] = request.cir_ul
        if not UtilClient.is_unset(request.dae_client):
            query['DaeClient'] = request.dae_client
        if not UtilClient.is_unset(request.dae_port):
            query['DaePort'] = request.dae_port
        if not UtilClient.is_unset(request.dae_secret):
            query['DaeSecret'] = request.dae_secret
        if not UtilClient.is_unset(request.disabled):
            query['Disabled'] = request.disabled
        if not UtilClient.is_unset(request.disassoc_low_ack):
            query['DisassocLowAck'] = request.disassoc_low_ack
        if not UtilClient.is_unset(request.disassoc_weak_rssi):
            query['DisassocWeakRssi'] = request.disassoc_weak_rssi
        if not UtilClient.is_unset(request.dynamic_vlan):
            query['DynamicVlan'] = request.dynamic_vlan
        if not UtilClient.is_unset(request.enc_key):
            query['EncKey'] = request.enc_key
        if not UtilClient.is_unset(request.encryption):
            query['Encryption'] = request.encryption
        if not UtilClient.is_unset(request.fourth_auth_port):
            query['FourthAuthPort'] = request.fourth_auth_port
        if not UtilClient.is_unset(request.fourth_auth_secret):
            query['FourthAuthSecret'] = request.fourth_auth_secret
        if not UtilClient.is_unset(request.fourth_auth_server):
            query['FourthAuthServer'] = request.fourth_auth_server
        if not UtilClient.is_unset(request.ft_over_ds):
            query['FtOverDs'] = request.ft_over_ds
        if not UtilClient.is_unset(request.hidden):
            query['Hidden'] = request.hidden
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ieee_80211r):
            query['Ieee80211r'] = request.ieee_80211r
        if not UtilClient.is_unset(request.ieee_80211w):
            query['Ieee80211w'] = request.ieee_80211w
        if not UtilClient.is_unset(request.ignore_weak_probe):
            query['IgnoreWeakProbe'] = request.ignore_weak_probe
        if not UtilClient.is_unset(request.isolate):
            query['Isolate'] = request.isolate
        if not UtilClient.is_unset(request.lite_effect):
            query['LiteEffect'] = request.lite_effect
        if not UtilClient.is_unset(request.mac):
            query['Mac'] = request.mac
        if not UtilClient.is_unset(request.max_inactivity):
            query['MaxInactivity'] = request.max_inactivity
        if not UtilClient.is_unset(request.maxassoc):
            query['Maxassoc'] = request.maxassoc
        if not UtilClient.is_unset(request.mobility_domain):
            query['MobilityDomain'] = request.mobility_domain
        if not UtilClient.is_unset(request.multicast_forward):
            query['MulticastForward'] = request.multicast_forward
        if not UtilClient.is_unset(request.nasid):
            query['Nasid'] = request.nasid
        if not UtilClient.is_unset(request.nd_proxy_work):
            query['NdProxyWork'] = request.nd_proxy_work
        if not UtilClient.is_unset(request.network):
            query['Network'] = request.network
        if not UtilClient.is_unset(request.ownip):
            query['Ownip'] = request.ownip
        if not UtilClient.is_unset(request.radio_index):
            query['RadioIndex'] = request.radio_index
        if not UtilClient.is_unset(request.secondary_acct_port):
            query['SecondaryAcctPort'] = request.secondary_acct_port
        if not UtilClient.is_unset(request.secondary_acct_secret):
            query['SecondaryAcctSecret'] = request.secondary_acct_secret
        if not UtilClient.is_unset(request.secondary_acct_server):
            query['SecondaryAcctServer'] = request.secondary_acct_server
        if not UtilClient.is_unset(request.secondary_auth_port):
            query['SecondaryAuthPort'] = request.secondary_auth_port
        if not UtilClient.is_unset(request.secondary_auth_secret):
            query['SecondaryAuthSecret'] = request.secondary_auth_secret
        if not UtilClient.is_unset(request.secondary_auth_server):
            query['SecondaryAuthServer'] = request.secondary_auth_server
        if not UtilClient.is_unset(request.send_config_to_ap):
            query['SendConfigToAp'] = request.send_config_to_ap
        if not UtilClient.is_unset(request.short_preamble):
            query['ShortPreamble'] = request.short_preamble
        if not UtilClient.is_unset(request.ssid):
            query['Ssid'] = request.ssid
        if not UtilClient.is_unset(request.ssid_lb):
            query['SsidLb'] = request.ssid_lb
        if not UtilClient.is_unset(request.third_auth_port):
            query['ThirdAuthPort'] = request.third_auth_port
        if not UtilClient.is_unset(request.third_auth_secret):
            query['ThirdAuthSecret'] = request.third_auth_secret
        if not UtilClient.is_unset(request.third_auth_server):
            query['ThirdAuthServer'] = request.third_auth_server
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vlan_dhcp):
            query['VlanDhcp'] = request.vlan_dhcp
        if not UtilClient.is_unset(request.wmm):
            query['Wmm'] = request.wmm
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveApSsidConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.SaveApSsidConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_ap_ssid_config(
        self,
        request: cloudwifi_pop_20191118_models.SaveApSsidConfigRequest,
    ) -> cloudwifi_pop_20191118_models.SaveApSsidConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_ap_ssid_config_with_options(request, runtime)

    async def save_ap_ssid_config_async(
        self,
        request: cloudwifi_pop_20191118_models.SaveApSsidConfigRequest,
    ) -> cloudwifi_pop_20191118_models.SaveApSsidConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_ap_ssid_config_with_options_async(request, runtime)

    def save_ap_third_app_with_options(
        self,
        request: cloudwifi_pop_20191118_models.SaveApThirdAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.SaveApThirdAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_style):
            query['AddStyle'] = request.add_style
        if not UtilClient.is_unset(request.ap_asset_id):
            query['ApAssetId'] = request.ap_asset_id
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_data):
            query['AppData'] = request.app_data
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.mac):
            query['Mac'] = request.mac
        if not UtilClient.is_unset(request.third_app_name):
            query['ThirdAppName'] = request.third_app_name
        if not UtilClient.is_unset(request.version):
            query['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveApThirdApp',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.SaveApThirdAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_ap_third_app_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.SaveApThirdAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.SaveApThirdAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_style):
            query['AddStyle'] = request.add_style
        if not UtilClient.is_unset(request.ap_asset_id):
            query['ApAssetId'] = request.ap_asset_id
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_data):
            query['AppData'] = request.app_data
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.mac):
            query['Mac'] = request.mac
        if not UtilClient.is_unset(request.third_app_name):
            query['ThirdAppName'] = request.third_app_name
        if not UtilClient.is_unset(request.version):
            query['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveApThirdApp',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.SaveApThirdAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_ap_third_app(
        self,
        request: cloudwifi_pop_20191118_models.SaveApThirdAppRequest,
    ) -> cloudwifi_pop_20191118_models.SaveApThirdAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_ap_third_app_with_options(request, runtime)

    async def save_ap_third_app_async(
        self,
        request: cloudwifi_pop_20191118_models.SaveApThirdAppRequest,
    ) -> cloudwifi_pop_20191118_models.SaveApThirdAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_ap_third_app_with_options_async(request, runtime)

    def save_apgroup_basic_config_with_options(
        self,
        request: cloudwifi_pop_20191118_models.SaveApgroupBasicConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.SaveApgroupBasicConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.dai):
            query['Dai'] = request.dai
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.echo_int):
            query['EchoInt'] = request.echo_int
        if not UtilClient.is_unset(request.failover):
            query['Failover'] = request.failover
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.insecure_allowed):
            query['InsecureAllowed'] = request.insecure_allowed
        if not UtilClient.is_unset(request.is_config_strong_consistency):
            query['IsConfigStrongConsistency'] = request.is_config_strong_consistency
        if not UtilClient.is_unset(request.lan_ip):
            query['LanIp'] = request.lan_ip
        if not UtilClient.is_unset(request.lan_mask):
            query['LanMask'] = request.lan_mask
        if not UtilClient.is_unset(request.lan_status):
            query['LanStatus'] = request.lan_status
        if not UtilClient.is_unset(request.log_ip):
            query['LogIp'] = request.log_ip
        if not UtilClient.is_unset(request.log_level):
            query['LogLevel'] = request.log_level
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parent_apgroup_id):
            query['ParentApgroupId'] = request.parent_apgroup_id
        if not UtilClient.is_unset(request.passwd):
            query['Passwd'] = request.passwd
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.route):
            query['Route'] = request.route
        if not UtilClient.is_unset(request.scan):
            query['Scan'] = request.scan
        if not UtilClient.is_unset(request.token_server):
            query['TokenServer'] = request.token_server
        if not UtilClient.is_unset(request.vpn):
            query['Vpn'] = request.vpn
        if not UtilClient.is_unset(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveApgroupBasicConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.SaveApgroupBasicConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_apgroup_basic_config_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.SaveApgroupBasicConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.SaveApgroupBasicConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.dai):
            query['Dai'] = request.dai
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.echo_int):
            query['EchoInt'] = request.echo_int
        if not UtilClient.is_unset(request.failover):
            query['Failover'] = request.failover
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.insecure_allowed):
            query['InsecureAllowed'] = request.insecure_allowed
        if not UtilClient.is_unset(request.is_config_strong_consistency):
            query['IsConfigStrongConsistency'] = request.is_config_strong_consistency
        if not UtilClient.is_unset(request.lan_ip):
            query['LanIp'] = request.lan_ip
        if not UtilClient.is_unset(request.lan_mask):
            query['LanMask'] = request.lan_mask
        if not UtilClient.is_unset(request.lan_status):
            query['LanStatus'] = request.lan_status
        if not UtilClient.is_unset(request.log_ip):
            query['LogIp'] = request.log_ip
        if not UtilClient.is_unset(request.log_level):
            query['LogLevel'] = request.log_level
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parent_apgroup_id):
            query['ParentApgroupId'] = request.parent_apgroup_id
        if not UtilClient.is_unset(request.passwd):
            query['Passwd'] = request.passwd
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.route):
            query['Route'] = request.route
        if not UtilClient.is_unset(request.scan):
            query['Scan'] = request.scan
        if not UtilClient.is_unset(request.token_server):
            query['TokenServer'] = request.token_server
        if not UtilClient.is_unset(request.vpn):
            query['Vpn'] = request.vpn
        if not UtilClient.is_unset(request.work_mode):
            query['WorkMode'] = request.work_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveApgroupBasicConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.SaveApgroupBasicConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_apgroup_basic_config(
        self,
        request: cloudwifi_pop_20191118_models.SaveApgroupBasicConfigRequest,
    ) -> cloudwifi_pop_20191118_models.SaveApgroupBasicConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_apgroup_basic_config_with_options(request, runtime)

    async def save_apgroup_basic_config_async(
        self,
        request: cloudwifi_pop_20191118_models.SaveApgroupBasicConfigRequest,
    ) -> cloudwifi_pop_20191118_models.SaveApgroupBasicConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_apgroup_basic_config_with_options_async(request, runtime)

    def save_apgroup_portal_config_with_options(
        self,
        tmp_req: cloudwifi_pop_20191118_models.SaveApgroupPortalConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.SaveApgroupPortalConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = cloudwifi_pop_20191118_models.SaveApgroupPortalConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.portal_types):
            request.portal_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.portal_types, 'PortalTypes', 'simple')
        query = {}
        if not UtilClient.is_unset(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not UtilClient.is_unset(request.app_auth_url):
            query['AppAuthUrl'] = request.app_auth_url
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_secret):
            query['AuthSecret'] = request.auth_secret
        if not UtilClient.is_unset(request.check_url):
            query['CheckUrl'] = request.check_url
        if not UtilClient.is_unset(request.client_download):
            query['ClientDownload'] = request.client_download
        if not UtilClient.is_unset(request.client_upload):
            query['ClientUpload'] = request.client_upload
        if not UtilClient.is_unset(request.countdown):
            query['Countdown'] = request.countdown
        if not UtilClient.is_unset(request.network):
            query['Network'] = request.network
        if not UtilClient.is_unset(request.portal_types_shrink):
            query['PortalTypes'] = request.portal_types_shrink
        if not UtilClient.is_unset(request.portal_url):
            query['PortalUrl'] = request.portal_url
        if not UtilClient.is_unset(request.time_stamp):
            query['TimeStamp'] = request.time_stamp
        if not UtilClient.is_unset(request.total_download):
            query['TotalDownload'] = request.total_download
        if not UtilClient.is_unset(request.total_upload):
            query['TotalUpload'] = request.total_upload
        if not UtilClient.is_unset(request.web_auth_url):
            query['WebAuthUrl'] = request.web_auth_url
        if not UtilClient.is_unset(request.whitelist):
            query['Whitelist'] = request.whitelist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveApgroupPortalConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.SaveApgroupPortalConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_apgroup_portal_config_with_options_async(
        self,
        tmp_req: cloudwifi_pop_20191118_models.SaveApgroupPortalConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.SaveApgroupPortalConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = cloudwifi_pop_20191118_models.SaveApgroupPortalConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.portal_types):
            request.portal_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.portal_types, 'PortalTypes', 'simple')
        query = {}
        if not UtilClient.is_unset(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not UtilClient.is_unset(request.app_auth_url):
            query['AppAuthUrl'] = request.app_auth_url
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_secret):
            query['AuthSecret'] = request.auth_secret
        if not UtilClient.is_unset(request.check_url):
            query['CheckUrl'] = request.check_url
        if not UtilClient.is_unset(request.client_download):
            query['ClientDownload'] = request.client_download
        if not UtilClient.is_unset(request.client_upload):
            query['ClientUpload'] = request.client_upload
        if not UtilClient.is_unset(request.countdown):
            query['Countdown'] = request.countdown
        if not UtilClient.is_unset(request.network):
            query['Network'] = request.network
        if not UtilClient.is_unset(request.portal_types_shrink):
            query['PortalTypes'] = request.portal_types_shrink
        if not UtilClient.is_unset(request.portal_url):
            query['PortalUrl'] = request.portal_url
        if not UtilClient.is_unset(request.time_stamp):
            query['TimeStamp'] = request.time_stamp
        if not UtilClient.is_unset(request.total_download):
            query['TotalDownload'] = request.total_download
        if not UtilClient.is_unset(request.total_upload):
            query['TotalUpload'] = request.total_upload
        if not UtilClient.is_unset(request.web_auth_url):
            query['WebAuthUrl'] = request.web_auth_url
        if not UtilClient.is_unset(request.whitelist):
            query['Whitelist'] = request.whitelist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveApgroupPortalConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.SaveApgroupPortalConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_apgroup_portal_config(
        self,
        request: cloudwifi_pop_20191118_models.SaveApgroupPortalConfigRequest,
    ) -> cloudwifi_pop_20191118_models.SaveApgroupPortalConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_apgroup_portal_config_with_options(request, runtime)

    async def save_apgroup_portal_config_async(
        self,
        request: cloudwifi_pop_20191118_models.SaveApgroupPortalConfigRequest,
    ) -> cloudwifi_pop_20191118_models.SaveApgroupPortalConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_apgroup_portal_config_with_options_async(request, runtime)

    def save_apgroup_ssid_config_with_options(
        self,
        request: cloudwifi_pop_20191118_models.SaveApgroupSsidConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.SaveApgroupSsidConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acct_port):
            query['AcctPort'] = request.acct_port
        if not UtilClient.is_unset(request.acct_secret):
            query['AcctSecret'] = request.acct_secret
        if not UtilClient.is_unset(request.acct_server):
            query['AcctServer'] = request.acct_server
        if not UtilClient.is_unset(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.auth_cache):
            query['AuthCache'] = request.auth_cache
        if not UtilClient.is_unset(request.auth_port):
            query['AuthPort'] = request.auth_port
        if not UtilClient.is_unset(request.auth_secret):
            query['AuthSecret'] = request.auth_secret
        if not UtilClient.is_unset(request.auth_server):
            query['AuthServer'] = request.auth_server
        if not UtilClient.is_unset(request.binding):
            query['Binding'] = request.binding
        if not UtilClient.is_unset(request.cir):
            query['Cir'] = request.cir
        if not UtilClient.is_unset(request.dae_client):
            query['DaeClient'] = request.dae_client
        if not UtilClient.is_unset(request.dae_port):
            query['DaePort'] = request.dae_port
        if not UtilClient.is_unset(request.dae_secret):
            query['DaeSecret'] = request.dae_secret
        if not UtilClient.is_unset(request.disabled):
            query['Disabled'] = request.disabled
        if not UtilClient.is_unset(request.disassoc_low_ack):
            query['DisassocLowAck'] = request.disassoc_low_ack
        if not UtilClient.is_unset(request.disassoc_weak_rssi):
            query['DisassocWeakRssi'] = request.disassoc_weak_rssi
        if not UtilClient.is_unset(request.dynamic_vlan):
            query['DynamicVlan'] = request.dynamic_vlan
        if not UtilClient.is_unset(request.effect):
            query['Effect'] = request.effect
        if not UtilClient.is_unset(request.enc_key):
            query['EncKey'] = request.enc_key
        if not UtilClient.is_unset(request.encryption):
            query['Encryption'] = request.encryption
        if not UtilClient.is_unset(request.hidden):
            query['Hidden'] = request.hidden
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ieee_80211w):
            query['Ieee80211w'] = request.ieee_80211w
        if not UtilClient.is_unset(request.ignore_weak_probe):
            query['IgnoreWeakProbe'] = request.ignore_weak_probe
        if not UtilClient.is_unset(request.isolate):
            query['Isolate'] = request.isolate
        if not UtilClient.is_unset(request.lite_effect):
            query['LiteEffect'] = request.lite_effect
        if not UtilClient.is_unset(request.max_inactivity):
            query['MaxInactivity'] = request.max_inactivity
        if not UtilClient.is_unset(request.maxassoc):
            query['Maxassoc'] = request.maxassoc
        if not UtilClient.is_unset(request.multicast_forward):
            query['MulticastForward'] = request.multicast_forward
        if not UtilClient.is_unset(request.nasid):
            query['Nasid'] = request.nasid
        if not UtilClient.is_unset(request.network):
            query['Network'] = request.network
        if not UtilClient.is_unset(request.new_ssid):
            query['NewSsid'] = request.new_ssid
        if not UtilClient.is_unset(request.ownip):
            query['Ownip'] = request.ownip
        if not UtilClient.is_unset(request.secondary_acct_port):
            query['SecondaryAcctPort'] = request.secondary_acct_port
        if not UtilClient.is_unset(request.secondary_acct_secret):
            query['SecondaryAcctSecret'] = request.secondary_acct_secret
        if not UtilClient.is_unset(request.secondary_acct_server):
            query['SecondaryAcctServer'] = request.secondary_acct_server
        if not UtilClient.is_unset(request.secondary_auth_port):
            query['SecondaryAuthPort'] = request.secondary_auth_port
        if not UtilClient.is_unset(request.secondary_auth_secret):
            query['SecondaryAuthSecret'] = request.secondary_auth_secret
        if not UtilClient.is_unset(request.secondary_auth_server):
            query['SecondaryAuthServer'] = request.secondary_auth_server
        if not UtilClient.is_unset(request.short_preamble):
            query['ShortPreamble'] = request.short_preamble
        if not UtilClient.is_unset(request.ssid):
            query['Ssid'] = request.ssid
        if not UtilClient.is_unset(request.ssid_lb):
            query['SsidLb'] = request.ssid_lb
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vlan_dhcp):
            query['VlanDhcp'] = request.vlan_dhcp
        if not UtilClient.is_unset(request.wmm):
            query['Wmm'] = request.wmm
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveApgroupSsidConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.SaveApgroupSsidConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_apgroup_ssid_config_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.SaveApgroupSsidConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.SaveApgroupSsidConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acct_port):
            query['AcctPort'] = request.acct_port
        if not UtilClient.is_unset(request.acct_secret):
            query['AcctSecret'] = request.acct_secret
        if not UtilClient.is_unset(request.acct_server):
            query['AcctServer'] = request.acct_server
        if not UtilClient.is_unset(request.apgroup_id):
            query['ApgroupId'] = request.apgroup_id
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.auth_cache):
            query['AuthCache'] = request.auth_cache
        if not UtilClient.is_unset(request.auth_port):
            query['AuthPort'] = request.auth_port
        if not UtilClient.is_unset(request.auth_secret):
            query['AuthSecret'] = request.auth_secret
        if not UtilClient.is_unset(request.auth_server):
            query['AuthServer'] = request.auth_server
        if not UtilClient.is_unset(request.binding):
            query['Binding'] = request.binding
        if not UtilClient.is_unset(request.cir):
            query['Cir'] = request.cir
        if not UtilClient.is_unset(request.dae_client):
            query['DaeClient'] = request.dae_client
        if not UtilClient.is_unset(request.dae_port):
            query['DaePort'] = request.dae_port
        if not UtilClient.is_unset(request.dae_secret):
            query['DaeSecret'] = request.dae_secret
        if not UtilClient.is_unset(request.disabled):
            query['Disabled'] = request.disabled
        if not UtilClient.is_unset(request.disassoc_low_ack):
            query['DisassocLowAck'] = request.disassoc_low_ack
        if not UtilClient.is_unset(request.disassoc_weak_rssi):
            query['DisassocWeakRssi'] = request.disassoc_weak_rssi
        if not UtilClient.is_unset(request.dynamic_vlan):
            query['DynamicVlan'] = request.dynamic_vlan
        if not UtilClient.is_unset(request.effect):
            query['Effect'] = request.effect
        if not UtilClient.is_unset(request.enc_key):
            query['EncKey'] = request.enc_key
        if not UtilClient.is_unset(request.encryption):
            query['Encryption'] = request.encryption
        if not UtilClient.is_unset(request.hidden):
            query['Hidden'] = request.hidden
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ieee_80211w):
            query['Ieee80211w'] = request.ieee_80211w
        if not UtilClient.is_unset(request.ignore_weak_probe):
            query['IgnoreWeakProbe'] = request.ignore_weak_probe
        if not UtilClient.is_unset(request.isolate):
            query['Isolate'] = request.isolate
        if not UtilClient.is_unset(request.lite_effect):
            query['LiteEffect'] = request.lite_effect
        if not UtilClient.is_unset(request.max_inactivity):
            query['MaxInactivity'] = request.max_inactivity
        if not UtilClient.is_unset(request.maxassoc):
            query['Maxassoc'] = request.maxassoc
        if not UtilClient.is_unset(request.multicast_forward):
            query['MulticastForward'] = request.multicast_forward
        if not UtilClient.is_unset(request.nasid):
            query['Nasid'] = request.nasid
        if not UtilClient.is_unset(request.network):
            query['Network'] = request.network
        if not UtilClient.is_unset(request.new_ssid):
            query['NewSsid'] = request.new_ssid
        if not UtilClient.is_unset(request.ownip):
            query['Ownip'] = request.ownip
        if not UtilClient.is_unset(request.secondary_acct_port):
            query['SecondaryAcctPort'] = request.secondary_acct_port
        if not UtilClient.is_unset(request.secondary_acct_secret):
            query['SecondaryAcctSecret'] = request.secondary_acct_secret
        if not UtilClient.is_unset(request.secondary_acct_server):
            query['SecondaryAcctServer'] = request.secondary_acct_server
        if not UtilClient.is_unset(request.secondary_auth_port):
            query['SecondaryAuthPort'] = request.secondary_auth_port
        if not UtilClient.is_unset(request.secondary_auth_secret):
            query['SecondaryAuthSecret'] = request.secondary_auth_secret
        if not UtilClient.is_unset(request.secondary_auth_server):
            query['SecondaryAuthServer'] = request.secondary_auth_server
        if not UtilClient.is_unset(request.short_preamble):
            query['ShortPreamble'] = request.short_preamble
        if not UtilClient.is_unset(request.ssid):
            query['Ssid'] = request.ssid
        if not UtilClient.is_unset(request.ssid_lb):
            query['SsidLb'] = request.ssid_lb
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vlan_dhcp):
            query['VlanDhcp'] = request.vlan_dhcp
        if not UtilClient.is_unset(request.wmm):
            query['Wmm'] = request.wmm
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveApgroupSsidConfig',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.SaveApgroupSsidConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_apgroup_ssid_config(
        self,
        request: cloudwifi_pop_20191118_models.SaveApgroupSsidConfigRequest,
    ) -> cloudwifi_pop_20191118_models.SaveApgroupSsidConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_apgroup_ssid_config_with_options(request, runtime)

    async def save_apgroup_ssid_config_async(
        self,
        request: cloudwifi_pop_20191118_models.SaveApgroupSsidConfigRequest,
    ) -> cloudwifi_pop_20191118_models.SaveApgroupSsidConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_apgroup_ssid_config_with_options_async(request, runtime)

    def set_ap_address_with_options(
        self,
        request: cloudwifi_pop_20191118_models.SetApAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.SetApAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_area_name):
            query['ApAreaName'] = request.ap_area_name
        if not UtilClient.is_unset(request.ap_building_name):
            query['ApBuildingName'] = request.ap_building_name
        if not UtilClient.is_unset(request.ap_campus_name):
            query['ApCampusName'] = request.ap_campus_name
        if not UtilClient.is_unset(request.ap_city_name):
            query['ApCityName'] = request.ap_city_name
        if not UtilClient.is_unset(request.ap_floor):
            query['ApFloor'] = request.ap_floor
        if not UtilClient.is_unset(request.ap_group):
            query['ApGroup'] = request.ap_group
        if not UtilClient.is_unset(request.ap_name):
            query['ApName'] = request.ap_name
        if not UtilClient.is_unset(request.ap_nation_name):
            query['ApNationName'] = request.ap_nation_name
        if not UtilClient.is_unset(request.ap_province_name):
            query['ApProvinceName'] = request.ap_province_name
        if not UtilClient.is_unset(request.ap_unit_id):
            query['ApUnitId'] = request.ap_unit_id
        if not UtilClient.is_unset(request.ap_unit_name):
            query['ApUnitName'] = request.ap_unit_name
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.lat):
            query['Lat'] = request.lat
        if not UtilClient.is_unset(request.lng):
            query['Lng'] = request.lng
        if not UtilClient.is_unset(request.mac):
            query['Mac'] = request.mac
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetApAddress',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.SetApAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_ap_address_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.SetApAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.SetApAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_area_name):
            query['ApAreaName'] = request.ap_area_name
        if not UtilClient.is_unset(request.ap_building_name):
            query['ApBuildingName'] = request.ap_building_name
        if not UtilClient.is_unset(request.ap_campus_name):
            query['ApCampusName'] = request.ap_campus_name
        if not UtilClient.is_unset(request.ap_city_name):
            query['ApCityName'] = request.ap_city_name
        if not UtilClient.is_unset(request.ap_floor):
            query['ApFloor'] = request.ap_floor
        if not UtilClient.is_unset(request.ap_group):
            query['ApGroup'] = request.ap_group
        if not UtilClient.is_unset(request.ap_name):
            query['ApName'] = request.ap_name
        if not UtilClient.is_unset(request.ap_nation_name):
            query['ApNationName'] = request.ap_nation_name
        if not UtilClient.is_unset(request.ap_province_name):
            query['ApProvinceName'] = request.ap_province_name
        if not UtilClient.is_unset(request.ap_unit_id):
            query['ApUnitId'] = request.ap_unit_id
        if not UtilClient.is_unset(request.ap_unit_name):
            query['ApUnitName'] = request.ap_unit_name
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.lat):
            query['Lat'] = request.lat
        if not UtilClient.is_unset(request.lng):
            query['Lng'] = request.lng
        if not UtilClient.is_unset(request.mac):
            query['Mac'] = request.mac
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetApAddress',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.SetApAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_ap_address(
        self,
        request: cloudwifi_pop_20191118_models.SetApAddressRequest,
    ) -> cloudwifi_pop_20191118_models.SetApAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_ap_address_with_options(request, runtime)

    async def set_ap_address_async(
        self,
        request: cloudwifi_pop_20191118_models.SetApAddressRequest,
    ) -> cloudwifi_pop_20191118_models.SetApAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_ap_address_with_options_async(request, runtime)

    def set_ap_name_with_options(
        self,
        request: cloudwifi_pop_20191118_models.SetApNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.SetApNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetApName',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.SetApNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_ap_name_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.SetApNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.SetApNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ap_mac):
            query['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetApName',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.SetApNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_ap_name(
        self,
        request: cloudwifi_pop_20191118_models.SetApNameRequest,
    ) -> cloudwifi_pop_20191118_models.SetApNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_ap_name_with_options(request, runtime)

    async def set_ap_name_async(
        self,
        request: cloudwifi_pop_20191118_models.SetApNameRequest,
    ) -> cloudwifi_pop_20191118_models.SetApNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_ap_name_with_options_async(request, runtime)

    def un_register_ap_asset_with_options(
        self,
        request: cloudwifi_pop_20191118_models.UnRegisterApAssetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.UnRegisterApAssetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.asset_apgroup_id):
            query['AssetApgroupId'] = request.asset_apgroup_id
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.mac):
            query['Mac'] = request.mac
        if not UtilClient.is_unset(request.serial_no):
            query['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.use_for):
            query['UseFor'] = request.use_for
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnRegisterApAsset',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.UnRegisterApAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_register_ap_asset_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.UnRegisterApAssetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.UnRegisterApAssetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.asset_apgroup_id):
            query['AssetApgroupId'] = request.asset_apgroup_id
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.mac):
            query['Mac'] = request.mac
        if not UtilClient.is_unset(request.serial_no):
            query['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.use_for):
            query['UseFor'] = request.use_for
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnRegisterApAsset',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.UnRegisterApAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_register_ap_asset(
        self,
        request: cloudwifi_pop_20191118_models.UnRegisterApAssetRequest,
    ) -> cloudwifi_pop_20191118_models.UnRegisterApAssetResponse:
        runtime = util_models.RuntimeOptions()
        return self.un_register_ap_asset_with_options(request, runtime)

    async def un_register_ap_asset_async(
        self,
        request: cloudwifi_pop_20191118_models.UnRegisterApAssetRequest,
    ) -> cloudwifi_pop_20191118_models.UnRegisterApAssetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.un_register_ap_asset_with_options_async(request, runtime)

    def update_net_device_info_with_options(
        self,
        request: cloudwifi_pop_20191118_models.UpdateNetDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.UpdateNetDeviceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.devices):
            body['Devices'] = request.devices
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateNetDeviceInfo',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.UpdateNetDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_net_device_info_with_options_async(
        self,
        request: cloudwifi_pop_20191118_models.UpdateNetDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudwifi_pop_20191118_models.UpdateNetDeviceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.devices):
            body['Devices'] = request.devices
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateNetDeviceInfo',
            version='2019-11-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudwifi_pop_20191118_models.UpdateNetDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_net_device_info(
        self,
        request: cloudwifi_pop_20191118_models.UpdateNetDeviceInfoRequest,
    ) -> cloudwifi_pop_20191118_models.UpdateNetDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_net_device_info_with_options(request, runtime)

    async def update_net_device_info_async(
        self,
        request: cloudwifi_pop_20191118_models.UpdateNetDeviceInfoRequest,
    ) -> cloudwifi_pop_20191118_models.UpdateNetDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_net_device_info_with_options_async(request, runtime)
