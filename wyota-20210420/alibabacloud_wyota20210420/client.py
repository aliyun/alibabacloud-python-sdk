# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_wyota20210420 import models as wyota_20210420_models
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
        self._signature_algorithm = 'v2'
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('wyota', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def activate_device_with_options(
        self,
        request: wyota_20210420_models.ActivateDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ActivateDeviceResponse:
        """
        @summary 设备激活
        
        @param request: ActivateDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActivateDeviceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ActivateDevice',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ActivateDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_device_with_options_async(
        self,
        request: wyota_20210420_models.ActivateDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ActivateDeviceResponse:
        """
        @summary 设备激活
        
        @param request: ActivateDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActivateDeviceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ActivateDevice',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ActivateDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def activate_device(
        self,
        request: wyota_20210420_models.ActivateDeviceRequest,
    ) -> wyota_20210420_models.ActivateDeviceResponse:
        """
        @summary 设备激活
        
        @param request: ActivateDeviceRequest
        @return: ActivateDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.activate_device_with_options(request, runtime)

    async def activate_device_async(
        self,
        request: wyota_20210420_models.ActivateDeviceRequest,
    ) -> wyota_20210420_models.ActivateDeviceResponse:
        """
        @summary 设备激活
        
        @param request: ActivateDeviceRequest
        @return: ActivateDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.activate_device_with_options_async(request, runtime)

    def add_device_from_snwith_options(
        self,
        request: wyota_20210420_models.AddDeviceFromSNRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.AddDeviceFromSNResponse:
        """
        @summary 通过序列号添加设备
        
        @param request: AddDeviceFromSNRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDeviceFromSNResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias):
            body['Alias'] = request.alias
        if not UtilClient.is_unset(request.custom_property):
            body['CustomProperty'] = request.custom_property
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.label_contents):
            body['LabelContents'] = request.label_contents
        if not UtilClient.is_unset(request.secure_network_type):
            body['SecureNetworkType'] = request.secure_network_type
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddDeviceFromSN',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.AddDeviceFromSNResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_device_from_snwith_options_async(
        self,
        request: wyota_20210420_models.AddDeviceFromSNRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.AddDeviceFromSNResponse:
        """
        @summary 通过序列号添加设备
        
        @param request: AddDeviceFromSNRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDeviceFromSNResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias):
            body['Alias'] = request.alias
        if not UtilClient.is_unset(request.custom_property):
            body['CustomProperty'] = request.custom_property
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.label_contents):
            body['LabelContents'] = request.label_contents
        if not UtilClient.is_unset(request.secure_network_type):
            body['SecureNetworkType'] = request.secure_network_type
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddDeviceFromSN',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.AddDeviceFromSNResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_device_from_sn(
        self,
        request: wyota_20210420_models.AddDeviceFromSNRequest,
    ) -> wyota_20210420_models.AddDeviceFromSNResponse:
        """
        @summary 通过序列号添加设备
        
        @param request: AddDeviceFromSNRequest
        @return: AddDeviceFromSNResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_device_from_snwith_options(request, runtime)

    async def add_device_from_sn_async(
        self,
        request: wyota_20210420_models.AddDeviceFromSNRequest,
    ) -> wyota_20210420_models.AddDeviceFromSNResponse:
        """
        @summary 通过序列号添加设备
        
        @param request: AddDeviceFromSNRequest
        @return: AddDeviceFromSNResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_device_from_snwith_options_async(request, runtime)

    def add_device_seats_and_labels_with_options(
        self,
        request: wyota_20210420_models.AddDeviceSeatsAndLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.AddDeviceSeatsAndLabelsResponse:
        """
        @summary 新增设备座位和标签
        
        @param request: AddDeviceSeatsAndLabelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDeviceSeatsAndLabelsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.is_unique):
            body['IsUnique'] = request.is_unique
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.label_list):
            body['LabelList'] = request.label_list
        if not UtilClient.is_unset(request.seat_name):
            body['SeatName'] = request.seat_name
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddDeviceSeatsAndLabels',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.AddDeviceSeatsAndLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_device_seats_and_labels_with_options_async(
        self,
        request: wyota_20210420_models.AddDeviceSeatsAndLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.AddDeviceSeatsAndLabelsResponse:
        """
        @summary 新增设备座位和标签
        
        @param request: AddDeviceSeatsAndLabelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDeviceSeatsAndLabelsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.is_unique):
            body['IsUnique'] = request.is_unique
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.label_list):
            body['LabelList'] = request.label_list
        if not UtilClient.is_unset(request.seat_name):
            body['SeatName'] = request.seat_name
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddDeviceSeatsAndLabels',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.AddDeviceSeatsAndLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_device_seats_and_labels(
        self,
        request: wyota_20210420_models.AddDeviceSeatsAndLabelsRequest,
    ) -> wyota_20210420_models.AddDeviceSeatsAndLabelsResponse:
        """
        @summary 新增设备座位和标签
        
        @param request: AddDeviceSeatsAndLabelsRequest
        @return: AddDeviceSeatsAndLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_device_seats_and_labels_with_options(request, runtime)

    async def add_device_seats_and_labels_async(
        self,
        request: wyota_20210420_models.AddDeviceSeatsAndLabelsRequest,
    ) -> wyota_20210420_models.AddDeviceSeatsAndLabelsResponse:
        """
        @summary 新增设备座位和标签
        
        @param request: AddDeviceSeatsAndLabelsRequest
        @return: AddDeviceSeatsAndLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_device_seats_and_labels_with_options_async(request, runtime)

    def add_devices_from_csvwith_options(
        self,
        request: wyota_20210420_models.AddDevicesFromCSVRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.AddDevicesFromCSVResponse:
        """
        @summary 通过CSV文件添加设备
        
        @param request: AddDevicesFromCSVRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDevicesFromCSVResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_type):
            body['FileType'] = request.file_type
        if not UtilClient.is_unset(request.seat_col):
            body['SeatCol'] = request.seat_col
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_name):
            body['SiteName'] = request.site_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddDevicesFromCSV',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.AddDevicesFromCSVResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_devices_from_csvwith_options_async(
        self,
        request: wyota_20210420_models.AddDevicesFromCSVRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.AddDevicesFromCSVResponse:
        """
        @summary 通过CSV文件添加设备
        
        @param request: AddDevicesFromCSVRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDevicesFromCSVResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_type):
            body['FileType'] = request.file_type
        if not UtilClient.is_unset(request.seat_col):
            body['SeatCol'] = request.seat_col
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_name):
            body['SiteName'] = request.site_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddDevicesFromCSV',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.AddDevicesFromCSVResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_devices_from_csv(
        self,
        request: wyota_20210420_models.AddDevicesFromCSVRequest,
    ) -> wyota_20210420_models.AddDevicesFromCSVResponse:
        """
        @summary 通过CSV文件添加设备
        
        @param request: AddDevicesFromCSVRequest
        @return: AddDevicesFromCSVResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_devices_from_csvwith_options(request, runtime)

    async def add_devices_from_csv_async(
        self,
        request: wyota_20210420_models.AddDevicesFromCSVRequest,
    ) -> wyota_20210420_models.AddDevicesFromCSVResponse:
        """
        @summary 通过CSV文件添加设备
        
        @param request: AddDevicesFromCSVRequest
        @return: AddDevicesFromCSVResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_devices_from_csvwith_options_async(request, runtime)

    def add_labels_with_options(
        self,
        request: wyota_20210420_models.AddLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.AddLabelsResponse:
        """
        @summary 添加标签
        
        @param request: AddLabelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddLabelsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.label_contents):
            body['LabelContents'] = request.label_contents
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddLabels',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.AddLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_labels_with_options_async(
        self,
        request: wyota_20210420_models.AddLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.AddLabelsResponse:
        """
        @summary 添加标签
        
        @param request: AddLabelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddLabelsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.label_contents):
            body['LabelContents'] = request.label_contents
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddLabels',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.AddLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_labels(
        self,
        request: wyota_20210420_models.AddLabelsRequest,
    ) -> wyota_20210420_models.AddLabelsResponse:
        """
        @summary 添加标签
        
        @param request: AddLabelsRequest
        @return: AddLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_labels_with_options(request, runtime)

    async def add_labels_async(
        self,
        request: wyota_20210420_models.AddLabelsRequest,
    ) -> wyota_20210420_models.AddLabelsResponse:
        """
        @summary 添加标签
        
        @param request: AddLabelsRequest
        @return: AddLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_labels_with_options_async(request, runtime)

    def add_or_update_device_seats_with_options(
        self,
        request: wyota_20210420_models.AddOrUpdateDeviceSeatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.AddOrUpdateDeviceSeatsResponse:
        """
        @summary 新增或更新设备工位
        
        @param request: AddOrUpdateDeviceSeatsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddOrUpdateDeviceSeatsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.user_custom_id):
            body['UserCustomId'] = request.user_custom_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddOrUpdateDeviceSeats',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.AddOrUpdateDeviceSeatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_or_update_device_seats_with_options_async(
        self,
        request: wyota_20210420_models.AddOrUpdateDeviceSeatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.AddOrUpdateDeviceSeatsResponse:
        """
        @summary 新增或更新设备工位
        
        @param request: AddOrUpdateDeviceSeatsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddOrUpdateDeviceSeatsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.user_custom_id):
            body['UserCustomId'] = request.user_custom_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddOrUpdateDeviceSeats',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.AddOrUpdateDeviceSeatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_or_update_device_seats(
        self,
        request: wyota_20210420_models.AddOrUpdateDeviceSeatsRequest,
    ) -> wyota_20210420_models.AddOrUpdateDeviceSeatsResponse:
        """
        @summary 新增或更新设备工位
        
        @param request: AddOrUpdateDeviceSeatsRequest
        @return: AddOrUpdateDeviceSeatsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_or_update_device_seats_with_options(request, runtime)

    async def add_or_update_device_seats_async(
        self,
        request: wyota_20210420_models.AddOrUpdateDeviceSeatsRequest,
    ) -> wyota_20210420_models.AddOrUpdateDeviceSeatsResponse:
        """
        @summary 新增或更新设备工位
        
        @param request: AddOrUpdateDeviceSeatsRequest
        @return: AddOrUpdateDeviceSeatsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_or_update_device_seats_with_options_async(request, runtime)

    def add_terminal_with_options(
        self,
        request: wyota_20210420_models.AddTerminalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.AddTerminalResponse:
        """
        @summary 添加终端
        
        @param request: AddTerminalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddTerminalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias):
            body['Alias'] = request.alias
        if not UtilClient.is_unset(request.serial_number):
            body['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.terminal_group_id):
            body['TerminalGroupId'] = request.terminal_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddTerminal',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.AddTerminalResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_terminal_with_options_async(
        self,
        request: wyota_20210420_models.AddTerminalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.AddTerminalResponse:
        """
        @summary 添加终端
        
        @param request: AddTerminalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddTerminalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias):
            body['Alias'] = request.alias
        if not UtilClient.is_unset(request.serial_number):
            body['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.terminal_group_id):
            body['TerminalGroupId'] = request.terminal_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddTerminal',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.AddTerminalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_terminal(
        self,
        request: wyota_20210420_models.AddTerminalRequest,
    ) -> wyota_20210420_models.AddTerminalResponse:
        """
        @summary 添加终端
        
        @param request: AddTerminalRequest
        @return: AddTerminalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_terminal_with_options(request, runtime)

    async def add_terminal_async(
        self,
        request: wyota_20210420_models.AddTerminalRequest,
    ) -> wyota_20210420_models.AddTerminalResponse:
        """
        @summary 添加终端
        
        @param request: AddTerminalRequest
        @return: AddTerminalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_terminal_with_options_async(request, runtime)

    def attach_end_users_with_options(
        self,
        request: wyota_20210420_models.AttachEndUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.AttachEndUsersResponse:
        """
        @summary 设备绑定终端用户
        
        @param request: AttachEndUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachEndUsersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_user_ids):
            body['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachEndUsers',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.AttachEndUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_end_users_with_options_async(
        self,
        request: wyota_20210420_models.AttachEndUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.AttachEndUsersResponse:
        """
        @summary 设备绑定终端用户
        
        @param request: AttachEndUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachEndUsersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_user_ids):
            body['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachEndUsers',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.AttachEndUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_end_users(
        self,
        request: wyota_20210420_models.AttachEndUsersRequest,
    ) -> wyota_20210420_models.AttachEndUsersResponse:
        """
        @summary 设备绑定终端用户
        
        @param request: AttachEndUsersRequest
        @return: AttachEndUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_end_users_with_options(request, runtime)

    async def attach_end_users_async(
        self,
        request: wyota_20210420_models.AttachEndUsersRequest,
    ) -> wyota_20210420_models.AttachEndUsersResponse:
        """
        @summary 设备绑定终端用户
        
        @param request: AttachEndUsersRequest
        @return: AttachEndUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_end_users_with_options_async(request, runtime)

    def attach_label_with_options(
        self,
        request: wyota_20210420_models.AttachLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.AttachLabelResponse:
        """
        @summary 设备绑定标签
        
        @param request: AttachLabelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachLabelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.label_content):
            body['LabelContent'] = request.label_content
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachLabel',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.AttachLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_label_with_options_async(
        self,
        request: wyota_20210420_models.AttachLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.AttachLabelResponse:
        """
        @summary 设备绑定标签
        
        @param request: AttachLabelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachLabelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.label_content):
            body['LabelContent'] = request.label_content
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachLabel',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.AttachLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_label(
        self,
        request: wyota_20210420_models.AttachLabelRequest,
    ) -> wyota_20210420_models.AttachLabelResponse:
        """
        @summary 设备绑定标签
        
        @param request: AttachLabelRequest
        @return: AttachLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_label_with_options(request, runtime)

    async def attach_label_async(
        self,
        request: wyota_20210420_models.AttachLabelRequest,
    ) -> wyota_20210420_models.AttachLabelResponse:
        """
        @summary 设备绑定标签
        
        @param request: AttachLabelRequest
        @return: AttachLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_label_with_options_async(request, runtime)

    def attach_labels_with_options(
        self,
        request: wyota_20210420_models.AttachLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.AttachLabelsResponse:
        """
        @summary 批量绑定标签
        
        @param request: AttachLabelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachLabelsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.label_ids):
            body['LabelIds'] = request.label_ids
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.serial_no_list):
            body['SerialNoList'] = request.serial_no_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachLabels',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.AttachLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_labels_with_options_async(
        self,
        request: wyota_20210420_models.AttachLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.AttachLabelsResponse:
        """
        @summary 批量绑定标签
        
        @param request: AttachLabelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachLabelsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.label_ids):
            body['LabelIds'] = request.label_ids
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.serial_no_list):
            body['SerialNoList'] = request.serial_no_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachLabels',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.AttachLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_labels(
        self,
        request: wyota_20210420_models.AttachLabelsRequest,
    ) -> wyota_20210420_models.AttachLabelsResponse:
        """
        @summary 批量绑定标签
        
        @param request: AttachLabelsRequest
        @return: AttachLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_labels_with_options(request, runtime)

    async def attach_labels_async(
        self,
        request: wyota_20210420_models.AttachLabelsRequest,
    ) -> wyota_20210420_models.AttachLabelsResponse:
        """
        @summary 批量绑定标签
        
        @param request: AttachLabelsRequest
        @return: AttachLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_labels_with_options_async(request, runtime)

    def bind_account_less_login_user_with_options(
        self,
        request: wyota_20210420_models.BindAccountLessLoginUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.BindAccountLessLoginUserResponse:
        """
        @summary 绑定免账号登录用户
        
        @param request: BindAccountLessLoginUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindAccountLessLoginUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.serial_number):
            body['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindAccountLessLoginUser',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.BindAccountLessLoginUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_account_less_login_user_with_options_async(
        self,
        request: wyota_20210420_models.BindAccountLessLoginUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.BindAccountLessLoginUserResponse:
        """
        @summary 绑定免账号登录用户
        
        @param request: BindAccountLessLoginUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindAccountLessLoginUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.serial_number):
            body['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindAccountLessLoginUser',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.BindAccountLessLoginUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_account_less_login_user(
        self,
        request: wyota_20210420_models.BindAccountLessLoginUserRequest,
    ) -> wyota_20210420_models.BindAccountLessLoginUserResponse:
        """
        @summary 绑定免账号登录用户
        
        @param request: BindAccountLessLoginUserRequest
        @return: BindAccountLessLoginUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_account_less_login_user_with_options(request, runtime)

    async def bind_account_less_login_user_async(
        self,
        request: wyota_20210420_models.BindAccountLessLoginUserRequest,
    ) -> wyota_20210420_models.BindAccountLessLoginUserResponse:
        """
        @summary 绑定免账号登录用户
        
        @param request: BindAccountLessLoginUserRequest
        @return: BindAccountLessLoginUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_account_less_login_user_with_options_async(request, runtime)

    def check_uuid_valid_with_options(
        self,
        request: wyota_20210420_models.CheckUuidValidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.CheckUuidValidResponse:
        """
        @summary 检查uuid有效性
        
        @param request: CheckUuidValidRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckUuidValidResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bluetooth):
            body['Bluetooth'] = request.bluetooth
        if not UtilClient.is_unset(request.build_id):
            body['BuildId'] = request.build_id
        if not UtilClient.is_unset(request.chip_id):
            body['ChipId'] = request.chip_id
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.custom_id):
            body['CustomId'] = request.custom_id
        if not UtilClient.is_unset(request.ether_mac):
            body['EtherMac'] = request.ether_mac
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        if not UtilClient.is_unset(request.wlan):
            body['Wlan'] = request.wlan
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckUuidValid',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.CheckUuidValidResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_uuid_valid_with_options_async(
        self,
        request: wyota_20210420_models.CheckUuidValidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.CheckUuidValidResponse:
        """
        @summary 检查uuid有效性
        
        @param request: CheckUuidValidRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckUuidValidResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bluetooth):
            body['Bluetooth'] = request.bluetooth
        if not UtilClient.is_unset(request.build_id):
            body['BuildId'] = request.build_id
        if not UtilClient.is_unset(request.chip_id):
            body['ChipId'] = request.chip_id
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.custom_id):
            body['CustomId'] = request.custom_id
        if not UtilClient.is_unset(request.ether_mac):
            body['EtherMac'] = request.ether_mac
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        if not UtilClient.is_unset(request.wlan):
            body['Wlan'] = request.wlan
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckUuidValid',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.CheckUuidValidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_uuid_valid(
        self,
        request: wyota_20210420_models.CheckUuidValidRequest,
    ) -> wyota_20210420_models.CheckUuidValidResponse:
        """
        @summary 检查uuid有效性
        
        @param request: CheckUuidValidRequest
        @return: CheckUuidValidResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_uuid_valid_with_options(request, runtime)

    async def check_uuid_valid_async(
        self,
        request: wyota_20210420_models.CheckUuidValidRequest,
    ) -> wyota_20210420_models.CheckUuidValidResponse:
        """
        @summary 检查uuid有效性
        
        @param request: CheckUuidValidRequest
        @return: CheckUuidValidResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_uuid_valid_with_options_async(request, runtime)

    def create_app_ota_task_with_options(
        self,
        request: wyota_20210420_models.CreateAppOtaTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.CreateAppOtaTaskResponse:
        """
        @summary 创建任务
        
        @param request: CreateAppOtaTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppOtaTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_version_uid):
            query['AppVersionUid'] = request.app_version_uid
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_id_list):
            query['ClientIdList'] = request.client_id_list
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.creator):
            query['Creator'] = request.creator
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.force_upgrade):
            query['ForceUpgrade'] = request.force_upgrade
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.regions):
            query['Regions'] = request.regions
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppOtaTask',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.CreateAppOtaTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_ota_task_with_options_async(
        self,
        request: wyota_20210420_models.CreateAppOtaTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.CreateAppOtaTaskResponse:
        """
        @summary 创建任务
        
        @param request: CreateAppOtaTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppOtaTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_version_uid):
            query['AppVersionUid'] = request.app_version_uid
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_id_list):
            query['ClientIdList'] = request.client_id_list
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.creator):
            query['Creator'] = request.creator
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.force_upgrade):
            query['ForceUpgrade'] = request.force_upgrade
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.regions):
            query['Regions'] = request.regions
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppOtaTask',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.CreateAppOtaTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_ota_task(
        self,
        request: wyota_20210420_models.CreateAppOtaTaskRequest,
    ) -> wyota_20210420_models.CreateAppOtaTaskResponse:
        """
        @summary 创建任务
        
        @param request: CreateAppOtaTaskRequest
        @return: CreateAppOtaTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_app_ota_task_with_options(request, runtime)

    async def create_app_ota_task_async(
        self,
        request: wyota_20210420_models.CreateAppOtaTaskRequest,
    ) -> wyota_20210420_models.CreateAppOtaTaskResponse:
        """
        @summary 创建任务
        
        @param request: CreateAppOtaTaskRequest
        @return: CreateAppOtaTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_app_ota_task_with_options_async(request, runtime)

    def create_app_ota_version_with_options(
        self,
        request: wyota_20210420_models.CreateAppOtaVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.CreateAppOtaVersionResponse:
        """
        @summary 创建版本
        
        @param request: CreateAppOtaVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppOtaVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.arch):
            query['Arch'] = request.arch
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.creator):
            query['Creator'] = request.creator
        if not UtilClient.is_unset(request.download_url):
            query['DownloadUrl'] = request.download_url
        if not UtilClient.is_unset(request.md_5):
            query['Md5'] = request.md_5
        if not UtilClient.is_unset(request.os):
            query['Os'] = request.os
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.ota_type):
            query['OtaType'] = request.ota_type
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.release_note):
            query['ReleaseNote'] = request.release_note
        if not UtilClient.is_unset(request.release_note_en):
            query['ReleaseNoteEn'] = request.release_note_en
        if not UtilClient.is_unset(request.release_note_jp):
            query['ReleaseNoteJp'] = request.release_note_jp
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.snapshot_region_id):
            query['SnapshotRegionId'] = request.snapshot_region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.version_type):
            query['VersionType'] = request.version_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppOtaVersion',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.CreateAppOtaVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_ota_version_with_options_async(
        self,
        request: wyota_20210420_models.CreateAppOtaVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.CreateAppOtaVersionResponse:
        """
        @summary 创建版本
        
        @param request: CreateAppOtaVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppOtaVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.arch):
            query['Arch'] = request.arch
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.creator):
            query['Creator'] = request.creator
        if not UtilClient.is_unset(request.download_url):
            query['DownloadUrl'] = request.download_url
        if not UtilClient.is_unset(request.md_5):
            query['Md5'] = request.md_5
        if not UtilClient.is_unset(request.os):
            query['Os'] = request.os
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.ota_type):
            query['OtaType'] = request.ota_type
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.release_note):
            query['ReleaseNote'] = request.release_note
        if not UtilClient.is_unset(request.release_note_en):
            query['ReleaseNoteEn'] = request.release_note_en
        if not UtilClient.is_unset(request.release_note_jp):
            query['ReleaseNoteJp'] = request.release_note_jp
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.snapshot_region_id):
            query['SnapshotRegionId'] = request.snapshot_region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.version_type):
            query['VersionType'] = request.version_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppOtaVersion',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.CreateAppOtaVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_ota_version(
        self,
        request: wyota_20210420_models.CreateAppOtaVersionRequest,
    ) -> wyota_20210420_models.CreateAppOtaVersionResponse:
        """
        @summary 创建版本
        
        @param request: CreateAppOtaVersionRequest
        @return: CreateAppOtaVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_app_ota_version_with_options(request, runtime)

    async def create_app_ota_version_async(
        self,
        request: wyota_20210420_models.CreateAppOtaVersionRequest,
    ) -> wyota_20210420_models.CreateAppOtaVersionResponse:
        """
        @summary 创建版本
        
        @param request: CreateAppOtaVersionRequest
        @return: CreateAppOtaVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_app_ota_version_with_options_async(request, runtime)

    def delete_app_ota_versions_with_options(
        self,
        request: wyota_20210420_models.DeleteAppOtaVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.DeleteAppOtaVersionsResponse:
        """
        @summary 删除版本
        
        @param request: DeleteAppOtaVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppOtaVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version_uid_list):
            query['VersionUidList'] = request.version_uid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppOtaVersions',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.DeleteAppOtaVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_ota_versions_with_options_async(
        self,
        request: wyota_20210420_models.DeleteAppOtaVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.DeleteAppOtaVersionsResponse:
        """
        @summary 删除版本
        
        @param request: DeleteAppOtaVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppOtaVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version_uid_list):
            query['VersionUidList'] = request.version_uid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppOtaVersions',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.DeleteAppOtaVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_ota_versions(
        self,
        request: wyota_20210420_models.DeleteAppOtaVersionsRequest,
    ) -> wyota_20210420_models.DeleteAppOtaVersionsResponse:
        """
        @summary 删除版本
        
        @param request: DeleteAppOtaVersionsRequest
        @return: DeleteAppOtaVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_app_ota_versions_with_options(request, runtime)

    async def delete_app_ota_versions_async(
        self,
        request: wyota_20210420_models.DeleteAppOtaVersionsRequest,
    ) -> wyota_20210420_models.DeleteAppOtaVersionsResponse:
        """
        @summary 删除版本
        
        @param request: DeleteAppOtaVersionsRequest
        @return: DeleteAppOtaVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_ota_versions_with_options_async(request, runtime)

    def delete_devices_with_options(
        self,
        request: wyota_20210420_models.DeleteDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.DeleteDevicesResponse:
        """
        @summary 删除设备
        
        @param request: DeleteDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        body = {}
        if not UtilClient.is_unset(request.force):
            body['Force'] = request.force
        if not UtilClient.is_unset(request.serial_nos):
            body['SerialNos'] = request.serial_nos
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDevices',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.DeleteDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_devices_with_options_async(
        self,
        request: wyota_20210420_models.DeleteDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.DeleteDevicesResponse:
        """
        @summary 删除设备
        
        @param request: DeleteDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        body = {}
        if not UtilClient.is_unset(request.force):
            body['Force'] = request.force
        if not UtilClient.is_unset(request.serial_nos):
            body['SerialNos'] = request.serial_nos
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDevices',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.DeleteDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_devices(
        self,
        request: wyota_20210420_models.DeleteDevicesRequest,
    ) -> wyota_20210420_models.DeleteDevicesResponse:
        """
        @summary 删除设备
        
        @param request: DeleteDevicesRequest
        @return: DeleteDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_devices_with_options(request, runtime)

    async def delete_devices_async(
        self,
        request: wyota_20210420_models.DeleteDevicesRequest,
    ) -> wyota_20210420_models.DeleteDevicesResponse:
        """
        @summary 删除设备
        
        @param request: DeleteDevicesRequest
        @return: DeleteDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_devices_with_options_async(request, runtime)

    def delete_label_with_options(
        self,
        request: wyota_20210420_models.DeleteLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.DeleteLabelResponse:
        """
        @summary 删除标签
        
        @param request: DeleteLabelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLabelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.force):
            body['Force'] = request.force
        if not UtilClient.is_unset(request.label_content):
            body['LabelContent'] = request.label_content
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLabel',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.DeleteLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_label_with_options_async(
        self,
        request: wyota_20210420_models.DeleteLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.DeleteLabelResponse:
        """
        @summary 删除标签
        
        @param request: DeleteLabelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLabelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.force):
            body['Force'] = request.force
        if not UtilClient.is_unset(request.label_content):
            body['LabelContent'] = request.label_content
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLabel',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.DeleteLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_label(
        self,
        request: wyota_20210420_models.DeleteLabelRequest,
    ) -> wyota_20210420_models.DeleteLabelResponse:
        """
        @summary 删除标签
        
        @param request: DeleteLabelRequest
        @return: DeleteLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_label_with_options(request, runtime)

    async def delete_label_async(
        self,
        request: wyota_20210420_models.DeleteLabelRequest,
    ) -> wyota_20210420_models.DeleteLabelResponse:
        """
        @summary 删除标签
        
        @param request: DeleteLabelRequest
        @return: DeleteLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_label_with_options_async(request, runtime)

    def describe_app_ota_version_with_options(
        self,
        request: wyota_20210420_models.DescribeAppOtaVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.DescribeAppOtaVersionResponse:
        """
        @summary 查询版本
        
        @param request: DescribeAppOtaVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppOtaVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.creator):
            query['Creator'] = request.creator
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.version_uid):
            query['VersionUid'] = request.version_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppOtaVersion',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.DescribeAppOtaVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_ota_version_with_options_async(
        self,
        request: wyota_20210420_models.DescribeAppOtaVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.DescribeAppOtaVersionResponse:
        """
        @summary 查询版本
        
        @param request: DescribeAppOtaVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppOtaVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.creator):
            query['Creator'] = request.creator
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.version_uid):
            query['VersionUid'] = request.version_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppOtaVersion',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.DescribeAppOtaVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_ota_version(
        self,
        request: wyota_20210420_models.DescribeAppOtaVersionRequest,
    ) -> wyota_20210420_models.DescribeAppOtaVersionResponse:
        """
        @summary 查询版本
        
        @param request: DescribeAppOtaVersionRequest
        @return: DescribeAppOtaVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_app_ota_version_with_options(request, runtime)

    async def describe_app_ota_version_async(
        self,
        request: wyota_20210420_models.DescribeAppOtaVersionRequest,
    ) -> wyota_20210420_models.DescribeAppOtaVersionResponse:
        """
        @summary 查询版本
        
        @param request: DescribeAppOtaVersionRequest
        @return: DescribeAppOtaVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_ota_version_with_options_async(request, runtime)

    def describe_device_seats_with_options(
        self,
        request: wyota_20210420_models.DescribeDeviceSeatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.DescribeDeviceSeatsResponse:
        """
        @summary 查询设备座位
        
        @param request: DescribeDeviceSeatsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDeviceSeatsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.serial_no_list):
            body['SerialNoList'] = request.serial_no_list
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDeviceSeats',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.DescribeDeviceSeatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_device_seats_with_options_async(
        self,
        request: wyota_20210420_models.DescribeDeviceSeatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.DescribeDeviceSeatsResponse:
        """
        @summary 查询设备座位
        
        @param request: DescribeDeviceSeatsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDeviceSeatsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.serial_no_list):
            body['SerialNoList'] = request.serial_no_list
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDeviceSeats',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.DescribeDeviceSeatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_device_seats(
        self,
        request: wyota_20210420_models.DescribeDeviceSeatsRequest,
    ) -> wyota_20210420_models.DescribeDeviceSeatsResponse:
        """
        @summary 查询设备座位
        
        @param request: DescribeDeviceSeatsRequest
        @return: DescribeDeviceSeatsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_device_seats_with_options(request, runtime)

    async def describe_device_seats_async(
        self,
        request: wyota_20210420_models.DescribeDeviceSeatsRequest,
    ) -> wyota_20210420_models.DescribeDeviceSeatsResponse:
        """
        @summary 查询设备座位
        
        @param request: DescribeDeviceSeatsRequest
        @return: DescribeDeviceSeatsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_device_seats_with_options_async(request, runtime)

    def describe_device_version_detail_with_options(
        self,
        request: wyota_20210420_models.DescribeDeviceVersionDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.DescribeDeviceVersionDetailResponse:
        """
        @summary 查询版本信息
        
        @param request: DescribeDeviceVersionDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDeviceVersionDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.network_type):
            body['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.version_name):
            body['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDeviceVersionDetail',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.DescribeDeviceVersionDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_device_version_detail_with_options_async(
        self,
        request: wyota_20210420_models.DescribeDeviceVersionDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.DescribeDeviceVersionDetailResponse:
        """
        @summary 查询版本信息
        
        @param request: DescribeDeviceVersionDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDeviceVersionDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.network_type):
            body['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.version_name):
            body['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDeviceVersionDetail',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.DescribeDeviceVersionDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_device_version_detail(
        self,
        request: wyota_20210420_models.DescribeDeviceVersionDetailRequest,
    ) -> wyota_20210420_models.DescribeDeviceVersionDetailResponse:
        """
        @summary 查询版本信息
        
        @param request: DescribeDeviceVersionDetailRequest
        @return: DescribeDeviceVersionDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_device_version_detail_with_options(request, runtime)

    async def describe_device_version_detail_async(
        self,
        request: wyota_20210420_models.DescribeDeviceVersionDetailRequest,
    ) -> wyota_20210420_models.DescribeDeviceVersionDetailResponse:
        """
        @summary 查询版本信息
        
        @param request: DescribeDeviceVersionDetailRequest
        @return: DescribeDeviceVersionDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_device_version_detail_with_options_async(request, runtime)

    def describe_sn_label_counts_with_options(
        self,
        request: wyota_20210420_models.DescribeSnLabelCountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.DescribeSnLabelCountsResponse:
        """
        @summary 查询设备标签数量
        
        @param request: DescribeSnLabelCountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSnLabelCountsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.label_list):
            body['LabelList'] = request.label_list
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.zone_name):
            body['ZoneName'] = request.zone_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSnLabelCounts',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.DescribeSnLabelCountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sn_label_counts_with_options_async(
        self,
        request: wyota_20210420_models.DescribeSnLabelCountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.DescribeSnLabelCountsResponse:
        """
        @summary 查询设备标签数量
        
        @param request: DescribeSnLabelCountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSnLabelCountsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.label_list):
            body['LabelList'] = request.label_list
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.zone_name):
            body['ZoneName'] = request.zone_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSnLabelCounts',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.DescribeSnLabelCountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sn_label_counts(
        self,
        request: wyota_20210420_models.DescribeSnLabelCountsRequest,
    ) -> wyota_20210420_models.DescribeSnLabelCountsResponse:
        """
        @summary 查询设备标签数量
        
        @param request: DescribeSnLabelCountsRequest
        @return: DescribeSnLabelCountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sn_label_counts_with_options(request, runtime)

    async def describe_sn_label_counts_async(
        self,
        request: wyota_20210420_models.DescribeSnLabelCountsRequest,
    ) -> wyota_20210420_models.DescribeSnLabelCountsResponse:
        """
        @summary 查询设备标签数量
        
        @param request: DescribeSnLabelCountsRequest
        @return: DescribeSnLabelCountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sn_label_counts_with_options_async(request, runtime)

    def describe_work_zones_with_options(
        self,
        request: wyota_20210420_models.DescribeWorkZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.DescribeWorkZonesResponse:
        """
        @summary 查询工作区域
        
        @param request: DescribeWorkZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWorkZonesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.zone_id_list):
            body['ZoneIdList'] = request.zone_id_list
        if not UtilClient.is_unset(request.zone_name_list):
            body['ZoneNameList'] = request.zone_name_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeWorkZones',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.DescribeWorkZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_work_zones_with_options_async(
        self,
        request: wyota_20210420_models.DescribeWorkZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.DescribeWorkZonesResponse:
        """
        @summary 查询工作区域
        
        @param request: DescribeWorkZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWorkZonesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.zone_id_list):
            body['ZoneIdList'] = request.zone_id_list
        if not UtilClient.is_unset(request.zone_name_list):
            body['ZoneNameList'] = request.zone_name_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeWorkZones',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.DescribeWorkZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_work_zones(
        self,
        request: wyota_20210420_models.DescribeWorkZonesRequest,
    ) -> wyota_20210420_models.DescribeWorkZonesResponse:
        """
        @summary 查询工作区域
        
        @param request: DescribeWorkZonesRequest
        @return: DescribeWorkZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_work_zones_with_options(request, runtime)

    async def describe_work_zones_async(
        self,
        request: wyota_20210420_models.DescribeWorkZonesRequest,
    ) -> wyota_20210420_models.DescribeWorkZonesResponse:
        """
        @summary 查询工作区域
        
        @param request: DescribeWorkZonesRequest
        @return: DescribeWorkZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_work_zones_with_options_async(request, runtime)

    def detach_end_users_with_options(
        self,
        request: wyota_20210420_models.DetachEndUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.DetachEndUsersResponse:
        """
        @summary 设备解绑终端用户
        
        @param request: DetachEndUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachEndUsersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_user_ids):
            body['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetachEndUsers',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.DetachEndUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_end_users_with_options_async(
        self,
        request: wyota_20210420_models.DetachEndUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.DetachEndUsersResponse:
        """
        @summary 设备解绑终端用户
        
        @param request: DetachEndUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachEndUsersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_user_ids):
            body['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetachEndUsers',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.DetachEndUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_end_users(
        self,
        request: wyota_20210420_models.DetachEndUsersRequest,
    ) -> wyota_20210420_models.DetachEndUsersResponse:
        """
        @summary 设备解绑终端用户
        
        @param request: DetachEndUsersRequest
        @return: DetachEndUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_end_users_with_options(request, runtime)

    async def detach_end_users_async(
        self,
        request: wyota_20210420_models.DetachEndUsersRequest,
    ) -> wyota_20210420_models.DetachEndUsersResponse:
        """
        @summary 设备解绑终端用户
        
        @param request: DetachEndUsersRequest
        @return: DetachEndUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_end_users_with_options_async(request, runtime)

    def detach_label_with_options(
        self,
        request: wyota_20210420_models.DetachLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.DetachLabelResponse:
        """
        @summary 设备绑定标签
        
        @param request: DetachLabelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachLabelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.label_content):
            body['LabelContent'] = request.label_content
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetachLabel',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.DetachLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_label_with_options_async(
        self,
        request: wyota_20210420_models.DetachLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.DetachLabelResponse:
        """
        @summary 设备绑定标签
        
        @param request: DetachLabelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachLabelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.label_content):
            body['LabelContent'] = request.label_content
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetachLabel',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.DetachLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_label(
        self,
        request: wyota_20210420_models.DetachLabelRequest,
    ) -> wyota_20210420_models.DetachLabelResponse:
        """
        @summary 设备绑定标签
        
        @param request: DetachLabelRequest
        @return: DetachLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_label_with_options(request, runtime)

    async def detach_label_async(
        self,
        request: wyota_20210420_models.DetachLabelRequest,
    ) -> wyota_20210420_models.DetachLabelResponse:
        """
        @summary 设备绑定标签
        
        @param request: DetachLabelRequest
        @return: DetachLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_label_with_options_async(request, runtime)

    def detach_labels_with_options(
        self,
        request: wyota_20210420_models.DetachLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.DetachLabelsResponse:
        """
        @summary 批量解绑标签
        
        @param request: DetachLabelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachLabelsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.label_ids):
            body['LabelIds'] = request.label_ids
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.serial_no_list):
            body['SerialNoList'] = request.serial_no_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetachLabels',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.DetachLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_labels_with_options_async(
        self,
        request: wyota_20210420_models.DetachLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.DetachLabelsResponse:
        """
        @summary 批量解绑标签
        
        @param request: DetachLabelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachLabelsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.label_ids):
            body['LabelIds'] = request.label_ids
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.serial_no_list):
            body['SerialNoList'] = request.serial_no_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetachLabels',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.DetachLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_labels(
        self,
        request: wyota_20210420_models.DetachLabelsRequest,
    ) -> wyota_20210420_models.DetachLabelsResponse:
        """
        @summary 批量解绑标签
        
        @param request: DetachLabelsRequest
        @return: DetachLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_labels_with_options(request, runtime)

    async def detach_labels_async(
        self,
        request: wyota_20210420_models.DetachLabelsRequest,
    ) -> wyota_20210420_models.DetachLabelsResponse:
        """
        @summary 批量解绑标签
        
        @param request: DetachLabelsRequest
        @return: DetachLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_labels_with_options_async(request, runtime)

    def generate_oss_url_with_options(
        self,
        request: wyota_20210420_models.GenerateOssUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.GenerateOssUrlResponse:
        """
        @summary 查询用户上传的文件
        
        @param request: GenerateOssUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateOssUrlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.object_name_list):
            body['ObjectNameList'] = request.object_name_list
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateOssUrl',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.GenerateOssUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_oss_url_with_options_async(
        self,
        request: wyota_20210420_models.GenerateOssUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.GenerateOssUrlResponse:
        """
        @summary 查询用户上传的文件
        
        @param request: GenerateOssUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateOssUrlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.object_name_list):
            body['ObjectNameList'] = request.object_name_list
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateOssUrl',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.GenerateOssUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_oss_url(
        self,
        request: wyota_20210420_models.GenerateOssUrlRequest,
    ) -> wyota_20210420_models.GenerateOssUrlResponse:
        """
        @summary 查询用户上传的文件
        
        @param request: GenerateOssUrlRequest
        @return: GenerateOssUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_oss_url_with_options(request, runtime)

    async def generate_oss_url_async(
        self,
        request: wyota_20210420_models.GenerateOssUrlRequest,
    ) -> wyota_20210420_models.GenerateOssUrlResponse:
        """
        @summary 查询用户上传的文件
        
        @param request: GenerateOssUrlRequest
        @return: GenerateOssUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_oss_url_with_options_async(request, runtime)

    def get_app_ota_latest_version_with_options(
        self,
        request: wyota_20210420_models.GetAppOtaLatestVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.GetAppOtaLatestVersionResponse:
        """
        @summary 获取应用最新版本
        
        @param request: GetAppOtaLatestVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppOtaLatestVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_version):
            query['BaseVersion'] = request.base_version
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.client_uid):
            query['ClientUid'] = request.client_uid
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppOtaLatestVersion',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.GetAppOtaLatestVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_ota_latest_version_with_options_async(
        self,
        request: wyota_20210420_models.GetAppOtaLatestVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.GetAppOtaLatestVersionResponse:
        """
        @summary 获取应用最新版本
        
        @param request: GetAppOtaLatestVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppOtaLatestVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_version):
            query['BaseVersion'] = request.base_version
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.client_uid):
            query['ClientUid'] = request.client_uid
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppOtaLatestVersion',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.GetAppOtaLatestVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_ota_latest_version(
        self,
        request: wyota_20210420_models.GetAppOtaLatestVersionRequest,
    ) -> wyota_20210420_models.GetAppOtaLatestVersionResponse:
        """
        @summary 获取应用最新版本
        
        @param request: GetAppOtaLatestVersionRequest
        @return: GetAppOtaLatestVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_app_ota_latest_version_with_options(request, runtime)

    async def get_app_ota_latest_version_async(
        self,
        request: wyota_20210420_models.GetAppOtaLatestVersionRequest,
    ) -> wyota_20210420_models.GetAppOtaLatestVersionResponse:
        """
        @summary 获取应用最新版本
        
        @param request: GetAppOtaLatestVersionRequest
        @return: GetAppOtaLatestVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_app_ota_latest_version_with_options_async(request, runtime)

    def get_device_configs_with_options(
        self,
        request: wyota_20210420_models.GetDeviceConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.GetDeviceConfigsResponse:
        """
        @summary 获取设备配置
        
        @param request: GetDeviceConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeviceConfigsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.network_type):
            body['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.urcl_version):
            body['UrclVersion'] = request.urcl_version
        if not UtilClient.is_unset(request.user_custom_id):
            body['UserCustomId'] = request.user_custom_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeviceConfigs',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.GetDeviceConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_configs_with_options_async(
        self,
        request: wyota_20210420_models.GetDeviceConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.GetDeviceConfigsResponse:
        """
        @summary 获取设备配置
        
        @param request: GetDeviceConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeviceConfigsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.network_type):
            body['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.urcl_version):
            body['UrclVersion'] = request.urcl_version
        if not UtilClient.is_unset(request.user_custom_id):
            body['UserCustomId'] = request.user_custom_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeviceConfigs',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.GetDeviceConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_configs(
        self,
        request: wyota_20210420_models.GetDeviceConfigsRequest,
    ) -> wyota_20210420_models.GetDeviceConfigsResponse:
        """
        @summary 获取设备配置
        
        @param request: GetDeviceConfigsRequest
        @return: GetDeviceConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_device_configs_with_options(request, runtime)

    async def get_device_configs_async(
        self,
        request: wyota_20210420_models.GetDeviceConfigsRequest,
    ) -> wyota_20210420_models.GetDeviceConfigsResponse:
        """
        @summary 获取设备配置
        
        @param request: GetDeviceConfigsRequest
        @return: GetDeviceConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_device_configs_with_options_async(request, runtime)

    def get_device_ota_auto_status_with_options(
        self,
        request: wyota_20210420_models.GetDeviceOtaAutoStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.GetDeviceOtaAutoStatusResponse:
        """
        @summary 获取是否开启自动升级状态
        
        @param request: GetDeviceOtaAutoStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeviceOtaAutoStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_type):
            body['ClientType'] = request.client_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeviceOtaAutoStatus',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.GetDeviceOtaAutoStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_ota_auto_status_with_options_async(
        self,
        request: wyota_20210420_models.GetDeviceOtaAutoStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.GetDeviceOtaAutoStatusResponse:
        """
        @summary 获取是否开启自动升级状态
        
        @param request: GetDeviceOtaAutoStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeviceOtaAutoStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_type):
            body['ClientType'] = request.client_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeviceOtaAutoStatus',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.GetDeviceOtaAutoStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_ota_auto_status(
        self,
        request: wyota_20210420_models.GetDeviceOtaAutoStatusRequest,
    ) -> wyota_20210420_models.GetDeviceOtaAutoStatusResponse:
        """
        @summary 获取是否开启自动升级状态
        
        @param request: GetDeviceOtaAutoStatusRequest
        @return: GetDeviceOtaAutoStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_device_ota_auto_status_with_options(request, runtime)

    async def get_device_ota_auto_status_async(
        self,
        request: wyota_20210420_models.GetDeviceOtaAutoStatusRequest,
    ) -> wyota_20210420_models.GetDeviceOtaAutoStatusResponse:
        """
        @summary 获取是否开启自动升级状态
        
        @param request: GetDeviceOtaAutoStatusRequest
        @return: GetDeviceOtaAutoStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_device_ota_auto_status_with_options_async(request, runtime)

    def get_device_ota_info_with_options(
        self,
        request: wyota_20210420_models.GetDeviceOtaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.GetDeviceOtaInfoResponse:
        """
        @summary 获取设备升级信息
        
        @param request: GetDeviceOtaInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeviceOtaInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.base_version):
            body['BaseVersion'] = request.base_version
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.network_type):
            body['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.os_version):
            body['OsVersion'] = request.os_version
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.target_version_type):
            body['TargetVersionType'] = request.target_version_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeviceOtaInfo',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.GetDeviceOtaInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_ota_info_with_options_async(
        self,
        request: wyota_20210420_models.GetDeviceOtaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.GetDeviceOtaInfoResponse:
        """
        @summary 获取设备升级信息
        
        @param request: GetDeviceOtaInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeviceOtaInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.base_version):
            body['BaseVersion'] = request.base_version
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.network_type):
            body['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.os_version):
            body['OsVersion'] = request.os_version
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.target_version_type):
            body['TargetVersionType'] = request.target_version_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeviceOtaInfo',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.GetDeviceOtaInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_ota_info(
        self,
        request: wyota_20210420_models.GetDeviceOtaInfoRequest,
    ) -> wyota_20210420_models.GetDeviceOtaInfoResponse:
        """
        @summary 获取设备升级信息
        
        @param request: GetDeviceOtaInfoRequest
        @return: GetDeviceOtaInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_device_ota_info_with_options(request, runtime)

    async def get_device_ota_info_async(
        self,
        request: wyota_20210420_models.GetDeviceOtaInfoRequest,
    ) -> wyota_20210420_models.GetDeviceOtaInfoResponse:
        """
        @summary 获取设备升级信息
        
        @param request: GetDeviceOtaInfoRequest
        @return: GetDeviceOtaInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_device_ota_info_with_options_async(request, runtime)

    def get_device_ota_info_test_with_options(
        self,
        request: wyota_20210420_models.GetDeviceOtaInfoTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.GetDeviceOtaInfoTestResponse:
        """
        @summary 获取设备升级信息
        
        @param request: GetDeviceOtaInfoTestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeviceOtaInfoTestResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.base_version):
            body['BaseVersion'] = request.base_version
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeviceOtaInfoTest',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.GetDeviceOtaInfoTestResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_ota_info_test_with_options_async(
        self,
        request: wyota_20210420_models.GetDeviceOtaInfoTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.GetDeviceOtaInfoTestResponse:
        """
        @summary 获取设备升级信息
        
        @param request: GetDeviceOtaInfoTestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeviceOtaInfoTestResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.base_version):
            body['BaseVersion'] = request.base_version
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeviceOtaInfoTest',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.GetDeviceOtaInfoTestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_ota_info_test(
        self,
        request: wyota_20210420_models.GetDeviceOtaInfoTestRequest,
    ) -> wyota_20210420_models.GetDeviceOtaInfoTestResponse:
        """
        @summary 获取设备升级信息
        
        @param request: GetDeviceOtaInfoTestRequest
        @return: GetDeviceOtaInfoTestResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_device_ota_info_test_with_options(request, runtime)

    async def get_device_ota_info_test_async(
        self,
        request: wyota_20210420_models.GetDeviceOtaInfoTestRequest,
    ) -> wyota_20210420_models.GetDeviceOtaInfoTestResponse:
        """
        @summary 获取设备升级信息
        
        @param request: GetDeviceOtaInfoTestRequest
        @return: GetDeviceOtaInfoTestResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_device_ota_info_test_with_options_async(request, runtime)

    def get_device_ota_task_version_info_with_options(
        self,
        request: wyota_20210420_models.GetDeviceOtaTaskVersionInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.GetDeviceOtaTaskVersionInfoResponse:
        """
        @summary 获取租户任务版本信息
        
        @param request: GetDeviceOtaTaskVersionInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeviceOtaTaskVersionInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeviceOtaTaskVersionInfo',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.GetDeviceOtaTaskVersionInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_ota_task_version_info_with_options_async(
        self,
        request: wyota_20210420_models.GetDeviceOtaTaskVersionInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.GetDeviceOtaTaskVersionInfoResponse:
        """
        @summary 获取租户任务版本信息
        
        @param request: GetDeviceOtaTaskVersionInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeviceOtaTaskVersionInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeviceOtaTaskVersionInfo',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.GetDeviceOtaTaskVersionInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_ota_task_version_info(
        self,
        request: wyota_20210420_models.GetDeviceOtaTaskVersionInfoRequest,
    ) -> wyota_20210420_models.GetDeviceOtaTaskVersionInfoResponse:
        """
        @summary 获取租户任务版本信息
        
        @param request: GetDeviceOtaTaskVersionInfoRequest
        @return: GetDeviceOtaTaskVersionInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_device_ota_task_version_info_with_options(request, runtime)

    async def get_device_ota_task_version_info_async(
        self,
        request: wyota_20210420_models.GetDeviceOtaTaskVersionInfoRequest,
    ) -> wyota_20210420_models.GetDeviceOtaTaskVersionInfoResponse:
        """
        @summary 获取租户任务版本信息
        
        @param request: GetDeviceOtaTaskVersionInfoRequest
        @return: GetDeviceOtaTaskVersionInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_device_ota_task_version_info_with_options_async(request, runtime)

    def get_device_upgrade_status_with_options(
        self,
        request: wyota_20210420_models.GetDeviceUpgradeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.GetDeviceUpgradeStatusResponse:
        """
        @summary 获得设备升级详情
        
        @param request: GetDeviceUpgradeStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeviceUpgradeStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.client_uid):
            query['ClientUid'] = request.client_uid
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.task_uid):
            query['TaskUid'] = request.task_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceUpgradeStatus',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.GetDeviceUpgradeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_upgrade_status_with_options_async(
        self,
        request: wyota_20210420_models.GetDeviceUpgradeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.GetDeviceUpgradeStatusResponse:
        """
        @summary 获得设备升级详情
        
        @param request: GetDeviceUpgradeStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeviceUpgradeStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.client_uid):
            query['ClientUid'] = request.client_uid
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.task_uid):
            query['TaskUid'] = request.task_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceUpgradeStatus',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.GetDeviceUpgradeStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_upgrade_status(
        self,
        request: wyota_20210420_models.GetDeviceUpgradeStatusRequest,
    ) -> wyota_20210420_models.GetDeviceUpgradeStatusResponse:
        """
        @summary 获得设备升级详情
        
        @param request: GetDeviceUpgradeStatusRequest
        @return: GetDeviceUpgradeStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_device_upgrade_status_with_options(request, runtime)

    async def get_device_upgrade_status_async(
        self,
        request: wyota_20210420_models.GetDeviceUpgradeStatusRequest,
    ) -> wyota_20210420_models.GetDeviceUpgradeStatusResponse:
        """
        @summary 获得设备升级详情
        
        @param request: GetDeviceUpgradeStatusRequest
        @return: GetDeviceUpgradeStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_device_upgrade_status_with_options_async(request, runtime)

    def get_export_device_info_oss_url_with_options(
        self,
        request: wyota_20210420_models.GetExportDeviceInfoOssUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.GetExportDeviceInfoOssUrlResponse:
        """
        @summary 导出设备工位列表
        
        @param request: GetExportDeviceInfoOssUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExportDeviceInfoOssUrlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.zone_name):
            body['ZoneName'] = request.zone_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetExportDeviceInfoOssUrl',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.GetExportDeviceInfoOssUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_export_device_info_oss_url_with_options_async(
        self,
        request: wyota_20210420_models.GetExportDeviceInfoOssUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.GetExportDeviceInfoOssUrlResponse:
        """
        @summary 导出设备工位列表
        
        @param request: GetExportDeviceInfoOssUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExportDeviceInfoOssUrlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.zone_name):
            body['ZoneName'] = request.zone_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetExportDeviceInfoOssUrl',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.GetExportDeviceInfoOssUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_export_device_info_oss_url(
        self,
        request: wyota_20210420_models.GetExportDeviceInfoOssUrlRequest,
    ) -> wyota_20210420_models.GetExportDeviceInfoOssUrlResponse:
        """
        @summary 导出设备工位列表
        
        @param request: GetExportDeviceInfoOssUrlRequest
        @return: GetExportDeviceInfoOssUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_export_device_info_oss_url_with_options(request, runtime)

    async def get_export_device_info_oss_url_async(
        self,
        request: wyota_20210420_models.GetExportDeviceInfoOssUrlRequest,
    ) -> wyota_20210420_models.GetExportDeviceInfoOssUrlResponse:
        """
        @summary 导出设备工位列表
        
        @param request: GetExportDeviceInfoOssUrlRequest
        @return: GetExportDeviceInfoOssUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_export_device_info_oss_url_with_options_async(request, runtime)

    def get_fb_oss_config_with_options(
        self,
        request: wyota_20210420_models.GetFbOssConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.GetFbOssConfigResponse:
        """
        @summary 查询OSS配置信息
        
        @param request: GetFbOssConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFbOssConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dir_prefix):
            body['DirPrefix'] = request.dir_prefix
        if not UtilClient.is_unset(request.is_dedicated_line):
            body['IsDedicatedLine'] = request.is_dedicated_line
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFbOssConfig',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.GetFbOssConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fb_oss_config_with_options_async(
        self,
        request: wyota_20210420_models.GetFbOssConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.GetFbOssConfigResponse:
        """
        @summary 查询OSS配置信息
        
        @param request: GetFbOssConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFbOssConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dir_prefix):
            body['DirPrefix'] = request.dir_prefix
        if not UtilClient.is_unset(request.is_dedicated_line):
            body['IsDedicatedLine'] = request.is_dedicated_line
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFbOssConfig',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.GetFbOssConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fb_oss_config(
        self,
        request: wyota_20210420_models.GetFbOssConfigRequest,
    ) -> wyota_20210420_models.GetFbOssConfigResponse:
        """
        @summary 查询OSS配置信息
        
        @param request: GetFbOssConfigRequest
        @return: GetFbOssConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_fb_oss_config_with_options(request, runtime)

    async def get_fb_oss_config_async(
        self,
        request: wyota_20210420_models.GetFbOssConfigRequest,
    ) -> wyota_20210420_models.GetFbOssConfigResponse:
        """
        @summary 查询OSS配置信息
        
        @param request: GetFbOssConfigRequest
        @return: GetFbOssConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_fb_oss_config_with_options_async(request, runtime)

    def get_oss_config_with_options(
        self,
        request: wyota_20210420_models.GetOssConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.GetOssConfigResponse:
        """
        @summary 获取OSS配置
        
        @param request: GetOssConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOssConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssConfig',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.GetOssConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_config_with_options_async(
        self,
        request: wyota_20210420_models.GetOssConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.GetOssConfigResponse:
        """
        @summary 获取OSS配置
        
        @param request: GetOssConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOssConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssConfig',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.GetOssConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_config(
        self,
        request: wyota_20210420_models.GetOssConfigRequest,
    ) -> wyota_20210420_models.GetOssConfigResponse:
        """
        @summary 获取OSS配置
        
        @param request: GetOssConfigRequest
        @return: GetOssConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_oss_config_with_options(request, runtime)

    async def get_oss_config_async(
        self,
        request: wyota_20210420_models.GetOssConfigRequest,
    ) -> wyota_20210420_models.GetOssConfigResponse:
        """
        @summary 获取OSS配置
        
        @param request: GetOssConfigRequest
        @return: GetOssConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_oss_config_with_options_async(request, runtime)

    def get_version_download_url_with_options(
        self,
        request: wyota_20210420_models.GetVersionDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.GetVersionDownloadUrlResponse:
        """
        @summary 获取版本下载地址
        
        @param request: GetVersionDownloadUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVersionDownloadUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVersionDownloadUrl',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.GetVersionDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_version_download_url_with_options_async(
        self,
        request: wyota_20210420_models.GetVersionDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.GetVersionDownloadUrlResponse:
        """
        @summary 获取版本下载地址
        
        @param request: GetVersionDownloadUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVersionDownloadUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVersionDownloadUrl',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.GetVersionDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_version_download_url(
        self,
        request: wyota_20210420_models.GetVersionDownloadUrlRequest,
    ) -> wyota_20210420_models.GetVersionDownloadUrlResponse:
        """
        @summary 获取版本下载地址
        
        @param request: GetVersionDownloadUrlRequest
        @return: GetVersionDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_version_download_url_with_options(request, runtime)

    async def get_version_download_url_async(
        self,
        request: wyota_20210420_models.GetVersionDownloadUrlRequest,
    ) -> wyota_20210420_models.GetVersionDownloadUrlResponse:
        """
        @summary 获取版本下载地址
        
        @param request: GetVersionDownloadUrlRequest
        @return: GetVersionDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_version_download_url_with_options_async(request, runtime)

    def list_device_ota_task_by_tenant_with_options(
        self,
        request: wyota_20210420_models.ListDeviceOtaTaskByTenantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ListDeviceOtaTaskByTenantResponse:
        """
        @summary 获取租户ota任务
        
        @param request: ListDeviceOtaTaskByTenantRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeviceOtaTaskByTenantResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDeviceOtaTaskByTenant',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ListDeviceOtaTaskByTenantResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_device_ota_task_by_tenant_with_options_async(
        self,
        request: wyota_20210420_models.ListDeviceOtaTaskByTenantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ListDeviceOtaTaskByTenantResponse:
        """
        @summary 获取租户ota任务
        
        @param request: ListDeviceOtaTaskByTenantRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeviceOtaTaskByTenantResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDeviceOtaTaskByTenant',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ListDeviceOtaTaskByTenantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_device_ota_task_by_tenant(
        self,
        request: wyota_20210420_models.ListDeviceOtaTaskByTenantRequest,
    ) -> wyota_20210420_models.ListDeviceOtaTaskByTenantResponse:
        """
        @summary 获取租户ota任务
        
        @param request: ListDeviceOtaTaskByTenantRequest
        @return: ListDeviceOtaTaskByTenantResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_device_ota_task_by_tenant_with_options(request, runtime)

    async def list_device_ota_task_by_tenant_async(
        self,
        request: wyota_20210420_models.ListDeviceOtaTaskByTenantRequest,
    ) -> wyota_20210420_models.ListDeviceOtaTaskByTenantResponse:
        """
        @summary 获取租户ota任务
        
        @param request: ListDeviceOtaTaskByTenantRequest
        @return: ListDeviceOtaTaskByTenantResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_device_ota_task_by_tenant_with_options_async(request, runtime)

    def list_device_seats_with_options(
        self,
        request: wyota_20210420_models.ListDeviceSeatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ListDeviceSeatsResponse:
        """
        @summary 查询设备座位列表
        
        @param request: ListDeviceSeatsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeviceSeatsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.seat_no):
            body['SeatNo'] = request.seat_no
        if not UtilClient.is_unset(request.serial_no_list):
            body['SerialNoList'] = request.serial_no_list
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDeviceSeats',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ListDeviceSeatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_device_seats_with_options_async(
        self,
        request: wyota_20210420_models.ListDeviceSeatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ListDeviceSeatsResponse:
        """
        @summary 查询设备座位列表
        
        @param request: ListDeviceSeatsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeviceSeatsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.seat_no):
            body['SeatNo'] = request.seat_no
        if not UtilClient.is_unset(request.serial_no_list):
            body['SerialNoList'] = request.serial_no_list
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDeviceSeats',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ListDeviceSeatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_device_seats(
        self,
        request: wyota_20210420_models.ListDeviceSeatsRequest,
    ) -> wyota_20210420_models.ListDeviceSeatsResponse:
        """
        @summary 查询设备座位列表
        
        @param request: ListDeviceSeatsRequest
        @return: ListDeviceSeatsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_device_seats_with_options(request, runtime)

    async def list_device_seats_async(
        self,
        request: wyota_20210420_models.ListDeviceSeatsRequest,
    ) -> wyota_20210420_models.ListDeviceSeatsResponse:
        """
        @summary 查询设备座位列表
        
        @param request: ListDeviceSeatsRequest
        @return: ListDeviceSeatsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_device_seats_with_options_async(request, runtime)

    def list_devices_with_options(
        self,
        request: wyota_20210420_models.ListDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ListDevicesResponse:
        """
        @summary 获取设备列表
        
        @param request: ListDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.device_ip_v4):
            query['DeviceIpV4'] = request.device_ip_v4
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_os):
            query['DeviceOS'] = request.device_os
        if not UtilClient.is_unset(request.device_platform):
            query['DevicePlatform'] = request.device_platform
        if not UtilClient.is_unset(request.location_info):
            query['LocationInfo'] = request.location_info
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        body = {}
        if not UtilClient.is_unset(request.alias):
            body['Alias'] = request.alias
        if not UtilClient.is_unset(request.build_id):
            body['BuildId'] = request.build_id
        if not UtilClient.is_unset(request.device_group_id):
            body['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.label_content):
            body['LabelContent'] = request.label_content
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDevices',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ListDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_devices_with_options_async(
        self,
        request: wyota_20210420_models.ListDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ListDevicesResponse:
        """
        @summary 获取设备列表
        
        @param request: ListDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.device_ip_v4):
            query['DeviceIpV4'] = request.device_ip_v4
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_os):
            query['DeviceOS'] = request.device_os
        if not UtilClient.is_unset(request.device_platform):
            query['DevicePlatform'] = request.device_platform
        if not UtilClient.is_unset(request.location_info):
            query['LocationInfo'] = request.location_info
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        body = {}
        if not UtilClient.is_unset(request.alias):
            body['Alias'] = request.alias
        if not UtilClient.is_unset(request.build_id):
            body['BuildId'] = request.build_id
        if not UtilClient.is_unset(request.device_group_id):
            body['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.label_content):
            body['LabelContent'] = request.label_content
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDevices',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ListDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_devices(
        self,
        request: wyota_20210420_models.ListDevicesRequest,
    ) -> wyota_20210420_models.ListDevicesResponse:
        """
        @summary 获取设备列表
        
        @param request: ListDevicesRequest
        @return: ListDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_devices_with_options(request, runtime)

    async def list_devices_async(
        self,
        request: wyota_20210420_models.ListDevicesRequest,
    ) -> wyota_20210420_models.ListDevicesResponse:
        """
        @summary 获取设备列表
        
        @param request: ListDevicesRequest
        @return: ListDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_devices_with_options_async(request, runtime)

    def list_fb_issue_labels_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ListFbIssueLabelsResponse:
        """
        @summary 查询用户问题标签
        
        @param request: ListFbIssueLabelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFbIssueLabelsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListFbIssueLabels',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ListFbIssueLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_fb_issue_labels_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ListFbIssueLabelsResponse:
        """
        @summary 查询用户问题标签
        
        @param request: ListFbIssueLabelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFbIssueLabelsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListFbIssueLabels',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ListFbIssueLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_fb_issue_labels(self) -> wyota_20210420_models.ListFbIssueLabelsResponse:
        """
        @summary 查询用户问题标签
        
        @return: ListFbIssueLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_fb_issue_labels_with_options(runtime)

    async def list_fb_issue_labels_async(self) -> wyota_20210420_models.ListFbIssueLabelsResponse:
        """
        @summary 查询用户问题标签
        
        @return: ListFbIssueLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_fb_issue_labels_with_options_async(runtime)

    def list_fb_issue_labels_by_lcwith_options(
        self,
        request: wyota_20210420_models.ListFbIssueLabelsByLCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ListFbIssueLabelsByLCResponse:
        """
        @summary 根据语言类型和调用方查询标签列表
        
        @param request: ListFbIssueLabelsByLCRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFbIssueLabelsByLCResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.caller):
            body['Caller'] = request.caller
        if not UtilClient.is_unset(request.language_type):
            body['LanguageType'] = request.language_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFbIssueLabelsByLC',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ListFbIssueLabelsByLCResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_fb_issue_labels_by_lcwith_options_async(
        self,
        request: wyota_20210420_models.ListFbIssueLabelsByLCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ListFbIssueLabelsByLCResponse:
        """
        @summary 根据语言类型和调用方查询标签列表
        
        @param request: ListFbIssueLabelsByLCRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFbIssueLabelsByLCResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.caller):
            body['Caller'] = request.caller
        if not UtilClient.is_unset(request.language_type):
            body['LanguageType'] = request.language_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFbIssueLabelsByLC',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ListFbIssueLabelsByLCResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_fb_issue_labels_by_lc(
        self,
        request: wyota_20210420_models.ListFbIssueLabelsByLCRequest,
    ) -> wyota_20210420_models.ListFbIssueLabelsByLCResponse:
        """
        @summary 根据语言类型和调用方查询标签列表
        
        @param request: ListFbIssueLabelsByLCRequest
        @return: ListFbIssueLabelsByLCResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_fb_issue_labels_by_lcwith_options(request, runtime)

    async def list_fb_issue_labels_by_lc_async(
        self,
        request: wyota_20210420_models.ListFbIssueLabelsByLCRequest,
    ) -> wyota_20210420_models.ListFbIssueLabelsByLCResponse:
        """
        @summary 根据语言类型和调用方查询标签列表
        
        @param request: ListFbIssueLabelsByLCRequest
        @return: ListFbIssueLabelsByLCResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_fb_issue_labels_by_lcwith_options_async(request, runtime)

    def list_labels_with_options(
        self,
        request: wyota_20210420_models.ListLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ListLabelsResponse:
        """
        @summary 获取标签列表
        
        @param request: ListLabelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLabelsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.label_content):
            body['LabelContent'] = request.label_content
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLabels',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ListLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_labels_with_options_async(
        self,
        request: wyota_20210420_models.ListLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ListLabelsResponse:
        """
        @summary 获取标签列表
        
        @param request: ListLabelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLabelsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.label_content):
            body['LabelContent'] = request.label_content
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLabels',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ListLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_labels(
        self,
        request: wyota_20210420_models.ListLabelsRequest,
    ) -> wyota_20210420_models.ListLabelsResponse:
        """
        @summary 获取标签列表
        
        @param request: ListLabelsRequest
        @return: ListLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_labels_with_options(request, runtime)

    async def list_labels_async(
        self,
        request: wyota_20210420_models.ListLabelsRequest,
    ) -> wyota_20210420_models.ListLabelsResponse:
        """
        @summary 获取标签列表
        
        @param request: ListLabelsRequest
        @return: ListLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_labels_with_options_async(request, runtime)

    def list_tenant_device_ota_info_with_options(
        self,
        request: wyota_20210420_models.ListTenantDeviceOtaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ListTenantDeviceOtaInfoResponse:
        """
        @summary 获取租户升级设备信息
        
        @param request: ListTenantDeviceOtaInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTenantDeviceOtaInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTenantDeviceOtaInfo',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ListTenantDeviceOtaInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tenant_device_ota_info_with_options_async(
        self,
        request: wyota_20210420_models.ListTenantDeviceOtaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ListTenantDeviceOtaInfoResponse:
        """
        @summary 获取租户升级设备信息
        
        @param request: ListTenantDeviceOtaInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTenantDeviceOtaInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTenantDeviceOtaInfo',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ListTenantDeviceOtaInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tenant_device_ota_info(
        self,
        request: wyota_20210420_models.ListTenantDeviceOtaInfoRequest,
    ) -> wyota_20210420_models.ListTenantDeviceOtaInfoResponse:
        """
        @summary 获取租户升级设备信息
        
        @param request: ListTenantDeviceOtaInfoRequest
        @return: ListTenantDeviceOtaInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tenant_device_ota_info_with_options(request, runtime)

    async def list_tenant_device_ota_info_async(
        self,
        request: wyota_20210420_models.ListTenantDeviceOtaInfoRequest,
    ) -> wyota_20210420_models.ListTenantDeviceOtaInfoResponse:
        """
        @summary 获取租户升级设备信息
        
        @param request: ListTenantDeviceOtaInfoRequest
        @return: ListTenantDeviceOtaInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tenant_device_ota_info_with_options_async(request, runtime)

    def list_terminal_with_options(
        self,
        request: wyota_20210420_models.ListTerminalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ListTerminalResponse:
        """
        @summary 查询终端列表
        
        @param request: ListTerminalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTerminalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias):
            body['Alias'] = request.alias
        if not UtilClient.is_unset(request.build_id):
            body['BuildId'] = request.build_id
        if not UtilClient.is_unset(request.client_type):
            body['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.in_manage):
            body['InManage'] = request.in_manage
        if not UtilClient.is_unset(request.ipv_4):
            body['Ipv4'] = request.ipv_4
        if not UtilClient.is_unset(request.location_info):
            body['LocationInfo'] = request.location_info
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_keyword):
            body['SearchKeyword'] = request.search_keyword
        if not UtilClient.is_unset(request.serial_number):
            body['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.terminal_group_id):
            body['TerminalGroupId'] = request.terminal_group_id
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTerminal',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ListTerminalResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_terminal_with_options_async(
        self,
        request: wyota_20210420_models.ListTerminalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ListTerminalResponse:
        """
        @summary 查询终端列表
        
        @param request: ListTerminalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTerminalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias):
            body['Alias'] = request.alias
        if not UtilClient.is_unset(request.build_id):
            body['BuildId'] = request.build_id
        if not UtilClient.is_unset(request.client_type):
            body['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.in_manage):
            body['InManage'] = request.in_manage
        if not UtilClient.is_unset(request.ipv_4):
            body['Ipv4'] = request.ipv_4
        if not UtilClient.is_unset(request.location_info):
            body['LocationInfo'] = request.location_info
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_keyword):
            body['SearchKeyword'] = request.search_keyword
        if not UtilClient.is_unset(request.serial_number):
            body['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.terminal_group_id):
            body['TerminalGroupId'] = request.terminal_group_id
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTerminal',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ListTerminalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_terminal(
        self,
        request: wyota_20210420_models.ListTerminalRequest,
    ) -> wyota_20210420_models.ListTerminalResponse:
        """
        @summary 查询终端列表
        
        @param request: ListTerminalRequest
        @return: ListTerminalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_terminal_with_options(request, runtime)

    async def list_terminal_async(
        self,
        request: wyota_20210420_models.ListTerminalRequest,
    ) -> wyota_20210420_models.ListTerminalResponse:
        """
        @summary 查询终端列表
        
        @param request: ListTerminalRequest
        @return: ListTerminalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_terminal_with_options_async(request, runtime)

    def list_terminals_with_options(
        self,
        request: wyota_20210420_models.ListTerminalsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ListTerminalsResponse:
        """
        @summary 批量查询终端基本信息
        
        @param request: ListTerminalsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTerminalsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_keyword):
            body['SearchKeyword'] = request.search_keyword
        if not UtilClient.is_unset(request.terminal_group_id):
            body['TerminalGroupId'] = request.terminal_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTerminals',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ListTerminalsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_terminals_with_options_async(
        self,
        request: wyota_20210420_models.ListTerminalsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ListTerminalsResponse:
        """
        @summary 批量查询终端基本信息
        
        @param request: ListTerminalsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTerminalsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_keyword):
            body['SearchKeyword'] = request.search_keyword
        if not UtilClient.is_unset(request.terminal_group_id):
            body['TerminalGroupId'] = request.terminal_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTerminals',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ListTerminalsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_terminals(
        self,
        request: wyota_20210420_models.ListTerminalsRequest,
    ) -> wyota_20210420_models.ListTerminalsResponse:
        """
        @summary 批量查询终端基本信息
        
        @param request: ListTerminalsRequest
        @return: ListTerminalsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_terminals_with_options(request, runtime)

    async def list_terminals_async(
        self,
        request: wyota_20210420_models.ListTerminalsRequest,
    ) -> wyota_20210420_models.ListTerminalsResponse:
        """
        @summary 批量查询终端基本信息
        
        @param request: ListTerminalsRequest
        @return: ListTerminalsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_terminals_with_options_async(request, runtime)

    def list_trust_devices_with_options(
        self,
        request: wyota_20210420_models.ListTrustDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ListTrustDevicesResponse:
        """
        @summary 查询可信设备列表
        
        @param request: ListTrustDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTrustDevicesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.label_content):
            body['LabelContent'] = request.label_content
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.user_custom_id):
            body['UserCustomId'] = request.user_custom_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTrustDevices',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ListTrustDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_trust_devices_with_options_async(
        self,
        request: wyota_20210420_models.ListTrustDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ListTrustDevicesResponse:
        """
        @summary 查询可信设备列表
        
        @param request: ListTrustDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTrustDevicesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.label_content):
            body['LabelContent'] = request.label_content
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.user_custom_id):
            body['UserCustomId'] = request.user_custom_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTrustDevices',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ListTrustDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_trust_devices(
        self,
        request: wyota_20210420_models.ListTrustDevicesRequest,
    ) -> wyota_20210420_models.ListTrustDevicesResponse:
        """
        @summary 查询可信设备列表
        
        @param request: ListTrustDevicesRequest
        @return: ListTrustDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_trust_devices_with_options(request, runtime)

    async def list_trust_devices_async(
        self,
        request: wyota_20210420_models.ListTrustDevicesRequest,
    ) -> wyota_20210420_models.ListTrustDevicesResponse:
        """
        @summary 查询可信设备列表
        
        @param request: ListTrustDevicesRequest
        @return: ListTrustDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_trust_devices_with_options_async(request, runtime)

    def list_user_fb_ac_issues_with_options(
        self,
        request: wyota_20210420_models.ListUserFbAcIssuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ListUserFbAcIssuesResponse:
        """
        @summary 查询问题反馈列表
        
        @param request: ListUserFbAcIssuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserFbAcIssuesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.error_message):
            body['ErrorMessage'] = request.error_message
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.issue_id):
            body['IssueId'] = request.issue_id
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.reserved_a):
            body['ReservedA'] = request.reserved_a
        if not UtilClient.is_unset(request.reserved_b):
            body['ReservedB'] = request.reserved_b
        if not UtilClient.is_unset(request.user_email):
            body['UserEmail'] = request.user_email
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUserFbAcIssues',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ListUserFbAcIssuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_fb_ac_issues_with_options_async(
        self,
        request: wyota_20210420_models.ListUserFbAcIssuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ListUserFbAcIssuesResponse:
        """
        @summary 查询问题反馈列表
        
        @param request: ListUserFbAcIssuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserFbAcIssuesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.error_message):
            body['ErrorMessage'] = request.error_message
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.issue_id):
            body['IssueId'] = request.issue_id
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.reserved_a):
            body['ReservedA'] = request.reserved_a
        if not UtilClient.is_unset(request.reserved_b):
            body['ReservedB'] = request.reserved_b
        if not UtilClient.is_unset(request.user_email):
            body['UserEmail'] = request.user_email
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUserFbAcIssues',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ListUserFbAcIssuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_fb_ac_issues(
        self,
        request: wyota_20210420_models.ListUserFbAcIssuesRequest,
    ) -> wyota_20210420_models.ListUserFbAcIssuesResponse:
        """
        @summary 查询问题反馈列表
        
        @param request: ListUserFbAcIssuesRequest
        @return: ListUserFbAcIssuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_fb_ac_issues_with_options(request, runtime)

    async def list_user_fb_ac_issues_async(
        self,
        request: wyota_20210420_models.ListUserFbAcIssuesRequest,
    ) -> wyota_20210420_models.ListUserFbAcIssuesResponse:
        """
        @summary 查询问题反馈列表
        
        @param request: ListUserFbAcIssuesRequest
        @return: ListUserFbAcIssuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_fb_ac_issues_with_options_async(request, runtime)

    def list_user_fb_issues_with_options(
        self,
        request: wyota_20210420_models.ListUserFbIssuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ListUserFbIssuesResponse:
        """
        @summary 查询用户反馈问题列表
        
        @param request: ListUserFbIssuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserFbIssuesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_model):
            body['ClientModel'] = request.client_model
        if not UtilClient.is_unset(request.client_sn):
            body['ClientSn'] = request.client_sn
        if not UtilClient.is_unset(request.customer_id):
            body['CustomerId'] = request.customer_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.desktop_id):
            body['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.error_code):
            body['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.error_msg):
            body['ErrorMsg'] = request.error_msg
        if not UtilClient.is_unset(request.fb_type):
            body['FbType'] = request.fb_type
        if not UtilClient.is_unset(request.issue_id):
            body['IssueId'] = request.issue_id
        if not UtilClient.is_unset(request.issue_label):
            body['IssueLabel'] = request.issue_label
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.user_email):
            body['UserEmail'] = request.user_email
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.was_read):
            body['WasRead'] = request.was_read
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUserFbIssues',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ListUserFbIssuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_fb_issues_with_options_async(
        self,
        request: wyota_20210420_models.ListUserFbIssuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ListUserFbIssuesResponse:
        """
        @summary 查询用户反馈问题列表
        
        @param request: ListUserFbIssuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserFbIssuesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_model):
            body['ClientModel'] = request.client_model
        if not UtilClient.is_unset(request.client_sn):
            body['ClientSn'] = request.client_sn
        if not UtilClient.is_unset(request.customer_id):
            body['CustomerId'] = request.customer_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.desktop_id):
            body['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.error_code):
            body['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.error_msg):
            body['ErrorMsg'] = request.error_msg
        if not UtilClient.is_unset(request.fb_type):
            body['FbType'] = request.fb_type
        if not UtilClient.is_unset(request.issue_id):
            body['IssueId'] = request.issue_id
        if not UtilClient.is_unset(request.issue_label):
            body['IssueLabel'] = request.issue_label
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.user_email):
            body['UserEmail'] = request.user_email
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.was_read):
            body['WasRead'] = request.was_read
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUserFbIssues',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ListUserFbIssuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_fb_issues(
        self,
        request: wyota_20210420_models.ListUserFbIssuesRequest,
    ) -> wyota_20210420_models.ListUserFbIssuesResponse:
        """
        @summary 查询用户反馈问题列表
        
        @param request: ListUserFbIssuesRequest
        @return: ListUserFbIssuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_fb_issues_with_options(request, runtime)

    async def list_user_fb_issues_async(
        self,
        request: wyota_20210420_models.ListUserFbIssuesRequest,
    ) -> wyota_20210420_models.ListUserFbIssuesResponse:
        """
        @summary 查询用户反馈问题列表
        
        @param request: ListUserFbIssuesRequest
        @return: ListUserFbIssuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_fb_issues_with_options_async(request, runtime)

    def modify_devices_secure_network_type_with_options(
        self,
        request: wyota_20210420_models.ModifyDevicesSecureNetworkTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ModifyDevicesSecureNetworkTypeResponse:
        """
        @summary 修改设备安全入网类型
        
        @param request: ModifyDevicesSecureNetworkTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDevicesSecureNetworkTypeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.all_devices):
            body['AllDevices'] = request.all_devices
        if not UtilClient.is_unset(request.secure_network_type):
            body['SecureNetworkType'] = request.secure_network_type
        if not UtilClient.is_unset(request.serial_nos):
            body['SerialNos'] = request.serial_nos
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDevicesSecureNetworkType',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ModifyDevicesSecureNetworkTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_devices_secure_network_type_with_options_async(
        self,
        request: wyota_20210420_models.ModifyDevicesSecureNetworkTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ModifyDevicesSecureNetworkTypeResponse:
        """
        @summary 修改设备安全入网类型
        
        @param request: ModifyDevicesSecureNetworkTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDevicesSecureNetworkTypeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.all_devices):
            body['AllDevices'] = request.all_devices
        if not UtilClient.is_unset(request.secure_network_type):
            body['SecureNetworkType'] = request.secure_network_type
        if not UtilClient.is_unset(request.serial_nos):
            body['SerialNos'] = request.serial_nos
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDevicesSecureNetworkType',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ModifyDevicesSecureNetworkTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_devices_secure_network_type(
        self,
        request: wyota_20210420_models.ModifyDevicesSecureNetworkTypeRequest,
    ) -> wyota_20210420_models.ModifyDevicesSecureNetworkTypeResponse:
        """
        @summary 修改设备安全入网类型
        
        @param request: ModifyDevicesSecureNetworkTypeRequest
        @return: ModifyDevicesSecureNetworkTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_devices_secure_network_type_with_options(request, runtime)

    async def modify_devices_secure_network_type_async(
        self,
        request: wyota_20210420_models.ModifyDevicesSecureNetworkTypeRequest,
    ) -> wyota_20210420_models.ModifyDevicesSecureNetworkTypeResponse:
        """
        @summary 修改设备安全入网类型
        
        @param request: ModifyDevicesSecureNetworkTypeRequest
        @return: ModifyDevicesSecureNetworkTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_devices_secure_network_type_with_options_async(request, runtime)

    def modify_secure_network_type_with_options(
        self,
        request: wyota_20210420_models.ModifySecureNetworkTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ModifySecureNetworkTypeResponse:
        """
        @summary 匿名api修改安全入网配置
        
        @param request: ModifySecureNetworkTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecureNetworkTypeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.secure_network_type):
            body['SecureNetworkType'] = request.secure_network_type
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifySecureNetworkType',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ModifySecureNetworkTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_secure_network_type_with_options_async(
        self,
        request: wyota_20210420_models.ModifySecureNetworkTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ModifySecureNetworkTypeResponse:
        """
        @summary 匿名api修改安全入网配置
        
        @param request: ModifySecureNetworkTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecureNetworkTypeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.secure_network_type):
            body['SecureNetworkType'] = request.secure_network_type
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifySecureNetworkType',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ModifySecureNetworkTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_secure_network_type(
        self,
        request: wyota_20210420_models.ModifySecureNetworkTypeRequest,
    ) -> wyota_20210420_models.ModifySecureNetworkTypeResponse:
        """
        @summary 匿名api修改安全入网配置
        
        @param request: ModifySecureNetworkTypeRequest
        @return: ModifySecureNetworkTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_secure_network_type_with_options(request, runtime)

    async def modify_secure_network_type_async(
        self,
        request: wyota_20210420_models.ModifySecureNetworkTypeRequest,
    ) -> wyota_20210420_models.ModifySecureNetworkTypeResponse:
        """
        @summary 匿名api修改安全入网配置
        
        @param request: ModifySecureNetworkTypeRequest
        @return: ModifySecureNetworkTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_secure_network_type_with_options_async(request, runtime)

    def register_device_with_options(
        self,
        request: wyota_20210420_models.RegisterDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.RegisterDeviceResponse:
        """
        @summary 设备注册
        
        @param request: RegisterDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterDeviceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bluetooth):
            body['Bluetooth'] = request.bluetooth
        if not UtilClient.is_unset(request.build_id):
            body['BuildId'] = request.build_id
        if not UtilClient.is_unset(request.chip_id):
            body['ChipId'] = request.chip_id
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_type):
            body['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.cpu):
            body['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.custom_id):
            body['CustomId'] = request.custom_id
        if not UtilClient.is_unset(request.ether_mac):
            body['EtherMac'] = request.ether_mac
        if not UtilClient.is_unset(request.memory):
            body['Memory'] = request.memory
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.storage):
            body['Storage'] = request.storage
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.wlan):
            body['Wlan'] = request.wlan
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegisterDevice',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.RegisterDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_device_with_options_async(
        self,
        request: wyota_20210420_models.RegisterDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.RegisterDeviceResponse:
        """
        @summary 设备注册
        
        @param request: RegisterDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterDeviceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bluetooth):
            body['Bluetooth'] = request.bluetooth
        if not UtilClient.is_unset(request.build_id):
            body['BuildId'] = request.build_id
        if not UtilClient.is_unset(request.chip_id):
            body['ChipId'] = request.chip_id
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_type):
            body['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.cpu):
            body['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.custom_id):
            body['CustomId'] = request.custom_id
        if not UtilClient.is_unset(request.ether_mac):
            body['EtherMac'] = request.ether_mac
        if not UtilClient.is_unset(request.memory):
            body['Memory'] = request.memory
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.storage):
            body['Storage'] = request.storage
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.wlan):
            body['Wlan'] = request.wlan
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegisterDevice',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.RegisterDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_device(
        self,
        request: wyota_20210420_models.RegisterDeviceRequest,
    ) -> wyota_20210420_models.RegisterDeviceResponse:
        """
        @summary 设备注册
        
        @param request: RegisterDeviceRequest
        @return: RegisterDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.register_device_with_options(request, runtime)

    async def register_device_async(
        self,
        request: wyota_20210420_models.RegisterDeviceRequest,
    ) -> wyota_20210420_models.RegisterDeviceResponse:
        """
        @summary 设备注册
        
        @param request: RegisterDeviceRequest
        @return: RegisterDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.register_device_with_options_async(request, runtime)

    def report_app_ota_info_with_options(
        self,
        request: wyota_20210420_models.ReportAppOtaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ReportAppOtaInfoResponse:
        """
        @summary 上报升级信息
        
        @param request: ReportAppOtaInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReportAppOtaInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_version):
            query['BaseVersion'] = request.base_version
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.client_uid):
            query['ClientUid'] = request.client_uid
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.target_version):
            query['TargetVersion'] = request.target_version
        if not UtilClient.is_unset(request.task_uid):
            query['TaskUid'] = request.task_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportAppOtaInfo',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ReportAppOtaInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_app_ota_info_with_options_async(
        self,
        request: wyota_20210420_models.ReportAppOtaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ReportAppOtaInfoResponse:
        """
        @summary 上报升级信息
        
        @param request: ReportAppOtaInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReportAppOtaInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_version):
            query['BaseVersion'] = request.base_version
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.client_uid):
            query['ClientUid'] = request.client_uid
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.target_version):
            query['TargetVersion'] = request.target_version
        if not UtilClient.is_unset(request.task_uid):
            query['TaskUid'] = request.task_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportAppOtaInfo',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ReportAppOtaInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_app_ota_info(
        self,
        request: wyota_20210420_models.ReportAppOtaInfoRequest,
    ) -> wyota_20210420_models.ReportAppOtaInfoResponse:
        """
        @summary 上报升级信息
        
        @param request: ReportAppOtaInfoRequest
        @return: ReportAppOtaInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.report_app_ota_info_with_options(request, runtime)

    async def report_app_ota_info_async(
        self,
        request: wyota_20210420_models.ReportAppOtaInfoRequest,
    ) -> wyota_20210420_models.ReportAppOtaInfoResponse:
        """
        @summary 上报升级信息
        
        @param request: ReportAppOtaInfoRequest
        @return: ReportAppOtaInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.report_app_ota_info_with_options_async(request, runtime)

    def report_device_ota_info_with_options(
        self,
        request: wyota_20210420_models.ReportDeviceOtaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ReportDeviceOtaInfoResponse:
        """
        @summary 升级信息上报
        
        @param request: ReportDeviceOtaInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReportDeviceOtaInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.base_version):
            body['BaseVersion'] = request.base_version
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.note):
            body['Note'] = request.note
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.target_version):
            body['TargetVersion'] = request.target_version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReportDeviceOtaInfo',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ReportDeviceOtaInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_device_ota_info_with_options_async(
        self,
        request: wyota_20210420_models.ReportDeviceOtaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ReportDeviceOtaInfoResponse:
        """
        @summary 升级信息上报
        
        @param request: ReportDeviceOtaInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReportDeviceOtaInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.base_version):
            body['BaseVersion'] = request.base_version
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.note):
            body['Note'] = request.note
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.target_version):
            body['TargetVersion'] = request.target_version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReportDeviceOtaInfo',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ReportDeviceOtaInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_device_ota_info(
        self,
        request: wyota_20210420_models.ReportDeviceOtaInfoRequest,
    ) -> wyota_20210420_models.ReportDeviceOtaInfoResponse:
        """
        @summary 升级信息上报
        
        @param request: ReportDeviceOtaInfoRequest
        @return: ReportDeviceOtaInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.report_device_ota_info_with_options(request, runtime)

    async def report_device_ota_info_async(
        self,
        request: wyota_20210420_models.ReportDeviceOtaInfoRequest,
    ) -> wyota_20210420_models.ReportDeviceOtaInfoResponse:
        """
        @summary 升级信息上报
        
        @param request: ReportDeviceOtaInfoRequest
        @return: ReportDeviceOtaInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.report_device_ota_info_with_options_async(request, runtime)

    def report_user_fb_ac_issue_with_options(
        self,
        tmp_req: wyota_20210420_models.ReportUserFbAcIssueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ReportUserFbAcIssueResponse:
        """
        @summary 应用中心用户问题反馈
        
        @param tmp_req: ReportUserFbAcIssueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReportUserFbAcIssueResponse
        """
        UtilClient.validate_model(tmp_req)
        request = wyota_20210420_models.ReportUserFbAcIssueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.file_list):
            request.file_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.file_list, 'FileList', 'json')
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.error_msg):
            body['ErrorMsg'] = request.error_msg
        if not UtilClient.is_unset(request.file_list_shrink):
            body['FileList'] = request.file_list_shrink
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.reserved_a):
            body['ReservedA'] = request.reserved_a
        if not UtilClient.is_unset(request.reserved_b):
            body['ReservedB'] = request.reserved_b
        if not UtilClient.is_unset(request.user_email):
            body['UserEmail'] = request.user_email
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReportUserFbAcIssue',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ReportUserFbAcIssueResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_user_fb_ac_issue_with_options_async(
        self,
        tmp_req: wyota_20210420_models.ReportUserFbAcIssueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ReportUserFbAcIssueResponse:
        """
        @summary 应用中心用户问题反馈
        
        @param tmp_req: ReportUserFbAcIssueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReportUserFbAcIssueResponse
        """
        UtilClient.validate_model(tmp_req)
        request = wyota_20210420_models.ReportUserFbAcIssueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.file_list):
            request.file_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.file_list, 'FileList', 'json')
        body = {}
        if not UtilClient.is_unset(request.account):
            body['Account'] = request.account
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.error_msg):
            body['ErrorMsg'] = request.error_msg
        if not UtilClient.is_unset(request.file_list_shrink):
            body['FileList'] = request.file_list_shrink
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.reserved_a):
            body['ReservedA'] = request.reserved_a
        if not UtilClient.is_unset(request.reserved_b):
            body['ReservedB'] = request.reserved_b
        if not UtilClient.is_unset(request.user_email):
            body['UserEmail'] = request.user_email
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReportUserFbAcIssue',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ReportUserFbAcIssueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_user_fb_ac_issue(
        self,
        request: wyota_20210420_models.ReportUserFbAcIssueRequest,
    ) -> wyota_20210420_models.ReportUserFbAcIssueResponse:
        """
        @summary 应用中心用户问题反馈
        
        @param request: ReportUserFbAcIssueRequest
        @return: ReportUserFbAcIssueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.report_user_fb_ac_issue_with_options(request, runtime)

    async def report_user_fb_ac_issue_async(
        self,
        request: wyota_20210420_models.ReportUserFbAcIssueRequest,
    ) -> wyota_20210420_models.ReportUserFbAcIssueResponse:
        """
        @summary 应用中心用户问题反馈
        
        @param request: ReportUserFbAcIssueRequest
        @return: ReportUserFbAcIssueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.report_user_fb_ac_issue_with_options_async(request, runtime)

    def report_user_fb_issue_with_options(
        self,
        tmp_req: wyota_20210420_models.ReportUserFbIssueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ReportUserFbIssueResponse:
        """
        @summary 上报用户反馈问题
        
        @param tmp_req: ReportUserFbIssueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReportUserFbIssueResponse
        """
        UtilClient.validate_model(tmp_req)
        request = wyota_20210420_models.ReportUserFbIssueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.file_list):
            request.file_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.file_list, 'FileList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_model):
            body['ClientModel'] = request.client_model
        if not UtilClient.is_unset(request.client_os_name):
            body['ClientOsName'] = request.client_os_name
        if not UtilClient.is_unset(request.client_sn):
            body['ClientSn'] = request.client_sn
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.customer_id):
            body['CustomerId'] = request.customer_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.desktop_id):
            body['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_type):
            body['DesktopType'] = request.desktop_type
        if not UtilClient.is_unset(request.error_code):
            body['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.error_msg):
            body['ErrorMsg'] = request.error_msg
        if not UtilClient.is_unset(request.fb_type):
            body['FbType'] = request.fb_type
        if not UtilClient.is_unset(request.file_list_shrink):
            body['FileList'] = request.file_list_shrink
        if not UtilClient.is_unset(request.issue_label):
            body['IssueLabel'] = request.issue_label
        if not UtilClient.is_unset(request.occur_time):
            body['OccurTime'] = request.occur_time
        if not UtilClient.is_unset(request.reserved_a):
            body['ReservedA'] = request.reserved_a
        if not UtilClient.is_unset(request.reserved_b):
            body['ReservedB'] = request.reserved_b
        if not UtilClient.is_unset(request.tel_no):
            body['TelNo'] = request.tel_no
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.user_email):
            body['UserEmail'] = request.user_email
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.wy_id):
            body['WyId'] = request.wy_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReportUserFbIssue',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ReportUserFbIssueResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_user_fb_issue_with_options_async(
        self,
        tmp_req: wyota_20210420_models.ReportUserFbIssueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.ReportUserFbIssueResponse:
        """
        @summary 上报用户反馈问题
        
        @param tmp_req: ReportUserFbIssueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReportUserFbIssueResponse
        """
        UtilClient.validate_model(tmp_req)
        request = wyota_20210420_models.ReportUserFbIssueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.file_list):
            request.file_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.file_list, 'FileList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_model):
            body['ClientModel'] = request.client_model
        if not UtilClient.is_unset(request.client_os_name):
            body['ClientOsName'] = request.client_os_name
        if not UtilClient.is_unset(request.client_sn):
            body['ClientSn'] = request.client_sn
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.customer_id):
            body['CustomerId'] = request.customer_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.desktop_id):
            body['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_type):
            body['DesktopType'] = request.desktop_type
        if not UtilClient.is_unset(request.error_code):
            body['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.error_msg):
            body['ErrorMsg'] = request.error_msg
        if not UtilClient.is_unset(request.fb_type):
            body['FbType'] = request.fb_type
        if not UtilClient.is_unset(request.file_list_shrink):
            body['FileList'] = request.file_list_shrink
        if not UtilClient.is_unset(request.issue_label):
            body['IssueLabel'] = request.issue_label
        if not UtilClient.is_unset(request.occur_time):
            body['OccurTime'] = request.occur_time
        if not UtilClient.is_unset(request.reserved_a):
            body['ReservedA'] = request.reserved_a
        if not UtilClient.is_unset(request.reserved_b):
            body['ReservedB'] = request.reserved_b
        if not UtilClient.is_unset(request.tel_no):
            body['TelNo'] = request.tel_no
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.user_email):
            body['UserEmail'] = request.user_email
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.wy_id):
            body['WyId'] = request.wy_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReportUserFbIssue',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.ReportUserFbIssueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_user_fb_issue(
        self,
        request: wyota_20210420_models.ReportUserFbIssueRequest,
    ) -> wyota_20210420_models.ReportUserFbIssueResponse:
        """
        @summary 上报用户反馈问题
        
        @param request: ReportUserFbIssueRequest
        @return: ReportUserFbIssueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.report_user_fb_issue_with_options(request, runtime)

    async def report_user_fb_issue_async(
        self,
        request: wyota_20210420_models.ReportUserFbIssueRequest,
    ) -> wyota_20210420_models.ReportUserFbIssueResponse:
        """
        @summary 上报用户反馈问题
        
        @param request: ReportUserFbIssueRequest
        @return: ReportUserFbIssueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.report_user_fb_issue_with_options_async(request, runtime)

    def send_ops_message_to_terminals_with_options(
        self,
        request: wyota_20210420_models.SendOpsMessageToTerminalsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.SendOpsMessageToTerminalsResponse:
        """
        @summary 向终端发送运维命令
        
        @param request: SendOpsMessageToTerminalsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendOpsMessageToTerminalsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delay):
            query['Delay'] = request.delay
        body = {}
        if not UtilClient.is_unset(request.msg):
            body['Msg'] = request.msg
        if not UtilClient.is_unset(request.ops_action):
            body['OpsAction'] = request.ops_action
        body_flat = {}
        if not UtilClient.is_unset(request.uuids):
            body_flat['Uuids'] = request.uuids
        if not UtilClient.is_unset(request.wait_for_ack):
            body['WaitForAck'] = request.wait_for_ack
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendOpsMessageToTerminals',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.SendOpsMessageToTerminalsResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_ops_message_to_terminals_with_options_async(
        self,
        request: wyota_20210420_models.SendOpsMessageToTerminalsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.SendOpsMessageToTerminalsResponse:
        """
        @summary 向终端发送运维命令
        
        @param request: SendOpsMessageToTerminalsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendOpsMessageToTerminalsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delay):
            query['Delay'] = request.delay
        body = {}
        if not UtilClient.is_unset(request.msg):
            body['Msg'] = request.msg
        if not UtilClient.is_unset(request.ops_action):
            body['OpsAction'] = request.ops_action
        body_flat = {}
        if not UtilClient.is_unset(request.uuids):
            body_flat['Uuids'] = request.uuids
        if not UtilClient.is_unset(request.wait_for_ack):
            body['WaitForAck'] = request.wait_for_ack
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendOpsMessageToTerminals',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.SendOpsMessageToTerminalsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_ops_message_to_terminals(
        self,
        request: wyota_20210420_models.SendOpsMessageToTerminalsRequest,
    ) -> wyota_20210420_models.SendOpsMessageToTerminalsResponse:
        """
        @summary 向终端发送运维命令
        
        @param request: SendOpsMessageToTerminalsRequest
        @return: SendOpsMessageToTerminalsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_ops_message_to_terminals_with_options(request, runtime)

    async def send_ops_message_to_terminals_async(
        self,
        request: wyota_20210420_models.SendOpsMessageToTerminalsRequest,
    ) -> wyota_20210420_models.SendOpsMessageToTerminalsResponse:
        """
        @summary 向终端发送运维命令
        
        @param request: SendOpsMessageToTerminalsRequest
        @return: SendOpsMessageToTerminalsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_ops_message_to_terminals_with_options_async(request, runtime)

    def set_device_ota_auto_status_with_options(
        self,
        request: wyota_20210420_models.SetDeviceOtaAutoStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.SetDeviceOtaAutoStatusResponse:
        """
        @summary 设置租户ota自动开启/关闭
        
        @param request: SetDeviceOtaAutoStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDeviceOtaAutoStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_update):
            body['AutoUpdate'] = request.auto_update
        if not UtilClient.is_unset(request.auto_update_time_schedule):
            body['AutoUpdateTimeSchedule'] = request.auto_update_time_schedule
        if not UtilClient.is_unset(request.client_type):
            body['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.force_upgrade):
            body['ForceUpgrade'] = request.force_upgrade
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetDeviceOtaAutoStatus',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.SetDeviceOtaAutoStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_device_ota_auto_status_with_options_async(
        self,
        request: wyota_20210420_models.SetDeviceOtaAutoStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.SetDeviceOtaAutoStatusResponse:
        """
        @summary 设置租户ota自动开启/关闭
        
        @param request: SetDeviceOtaAutoStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDeviceOtaAutoStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_update):
            body['AutoUpdate'] = request.auto_update
        if not UtilClient.is_unset(request.auto_update_time_schedule):
            body['AutoUpdateTimeSchedule'] = request.auto_update_time_schedule
        if not UtilClient.is_unset(request.client_type):
            body['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.force_upgrade):
            body['ForceUpgrade'] = request.force_upgrade
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetDeviceOtaAutoStatus',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.SetDeviceOtaAutoStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_device_ota_auto_status(
        self,
        request: wyota_20210420_models.SetDeviceOtaAutoStatusRequest,
    ) -> wyota_20210420_models.SetDeviceOtaAutoStatusResponse:
        """
        @summary 设置租户ota自动开启/关闭
        
        @param request: SetDeviceOtaAutoStatusRequest
        @return: SetDeviceOtaAutoStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_device_ota_auto_status_with_options(request, runtime)

    async def set_device_ota_auto_status_async(
        self,
        request: wyota_20210420_models.SetDeviceOtaAutoStatusRequest,
    ) -> wyota_20210420_models.SetDeviceOtaAutoStatusResponse:
        """
        @summary 设置租户ota自动开启/关闭
        
        @param request: SetDeviceOtaAutoStatusRequest
        @return: SetDeviceOtaAutoStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_device_ota_auto_status_with_options_async(request, runtime)

    def set_device_ota_task_status_with_options(
        self,
        request: wyota_20210420_models.SetDeviceOtaTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.SetDeviceOtaTaskStatusResponse:
        """
        @summary 租户设置设备ota任务的状态
        
        @param request: SetDeviceOtaTaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDeviceOtaTaskStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation_status):
            body['OperationStatus'] = request.operation_status
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetDeviceOtaTaskStatus',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.SetDeviceOtaTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_device_ota_task_status_with_options_async(
        self,
        request: wyota_20210420_models.SetDeviceOtaTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.SetDeviceOtaTaskStatusResponse:
        """
        @summary 租户设置设备ota任务的状态
        
        @param request: SetDeviceOtaTaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDeviceOtaTaskStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation_status):
            body['OperationStatus'] = request.operation_status
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetDeviceOtaTaskStatus',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.SetDeviceOtaTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_device_ota_task_status(
        self,
        request: wyota_20210420_models.SetDeviceOtaTaskStatusRequest,
    ) -> wyota_20210420_models.SetDeviceOtaTaskStatusResponse:
        """
        @summary 租户设置设备ota任务的状态
        
        @param request: SetDeviceOtaTaskStatusRequest
        @return: SetDeviceOtaTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_device_ota_task_status_with_options(request, runtime)

    async def set_device_ota_task_status_async(
        self,
        request: wyota_20210420_models.SetDeviceOtaTaskStatusRequest,
    ) -> wyota_20210420_models.SetDeviceOtaTaskStatusResponse:
        """
        @summary 租户设置设备ota任务的状态
        
        @param request: SetDeviceOtaTaskStatusRequest
        @return: SetDeviceOtaTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_device_ota_task_status_with_options_async(request, runtime)

    def unbind_account_less_login_user_with_options(
        self,
        request: wyota_20210420_models.UnbindAccountLessLoginUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.UnbindAccountLessLoginUserResponse:
        """
        @summary 解绑免账号登录用户
        
        @param request: UnbindAccountLessLoginUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindAccountLessLoginUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.serial_number):
            body['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnbindAccountLessLoginUser',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.UnbindAccountLessLoginUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_account_less_login_user_with_options_async(
        self,
        request: wyota_20210420_models.UnbindAccountLessLoginUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.UnbindAccountLessLoginUserResponse:
        """
        @summary 解绑免账号登录用户
        
        @param request: UnbindAccountLessLoginUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindAccountLessLoginUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.serial_number):
            body['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnbindAccountLessLoginUser',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.UnbindAccountLessLoginUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_account_less_login_user(
        self,
        request: wyota_20210420_models.UnbindAccountLessLoginUserRequest,
    ) -> wyota_20210420_models.UnbindAccountLessLoginUserResponse:
        """
        @summary 解绑免账号登录用户
        
        @param request: UnbindAccountLessLoginUserRequest
        @return: UnbindAccountLessLoginUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_account_less_login_user_with_options(request, runtime)

    async def unbind_account_less_login_user_async(
        self,
        request: wyota_20210420_models.UnbindAccountLessLoginUserRequest,
    ) -> wyota_20210420_models.UnbindAccountLessLoginUserResponse:
        """
        @summary 解绑免账号登录用户
        
        @param request: UnbindAccountLessLoginUserRequest
        @return: UnbindAccountLessLoginUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_account_less_login_user_with_options_async(request, runtime)

    def unbind_device_seats_with_options(
        self,
        tmp_req: wyota_20210420_models.UnbindDeviceSeatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.UnbindDeviceSeatsResponse:
        """
        @summary 解绑设备座位
        
        @param tmp_req: UnbindDeviceSeatsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindDeviceSeatsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = wyota_20210420_models.UnbindDeviceSeatsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.serial_no_list):
            request.serial_no_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.serial_no_list, 'SerialNoList', 'json')
        body = {}
        if not UtilClient.is_unset(request.serial_no_list_shrink):
            body['SerialNoList'] = request.serial_no_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnbindDeviceSeats',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.UnbindDeviceSeatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_device_seats_with_options_async(
        self,
        tmp_req: wyota_20210420_models.UnbindDeviceSeatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.UnbindDeviceSeatsResponse:
        """
        @summary 解绑设备座位
        
        @param tmp_req: UnbindDeviceSeatsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindDeviceSeatsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = wyota_20210420_models.UnbindDeviceSeatsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.serial_no_list):
            request.serial_no_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.serial_no_list, 'SerialNoList', 'json')
        body = {}
        if not UtilClient.is_unset(request.serial_no_list_shrink):
            body['SerialNoList'] = request.serial_no_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnbindDeviceSeats',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.UnbindDeviceSeatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_device_seats(
        self,
        request: wyota_20210420_models.UnbindDeviceSeatsRequest,
    ) -> wyota_20210420_models.UnbindDeviceSeatsResponse:
        """
        @summary 解绑设备座位
        
        @param request: UnbindDeviceSeatsRequest
        @return: UnbindDeviceSeatsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_device_seats_with_options(request, runtime)

    async def unbind_device_seats_async(
        self,
        request: wyota_20210420_models.UnbindDeviceSeatsRequest,
    ) -> wyota_20210420_models.UnbindDeviceSeatsResponse:
        """
        @summary 解绑设备座位
        
        @param request: UnbindDeviceSeatsRequest
        @return: UnbindDeviceSeatsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_device_seats_with_options_async(request, runtime)

    def update_alias_with_options(
        self,
        request: wyota_20210420_models.UpdateAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.UpdateAliasResponse:
        """
        @summary 更新设备别名
        
        @param request: UpdateAliasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAliasResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias):
            body['Alias'] = request.alias
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAlias',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.UpdateAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alias_with_options_async(
        self,
        request: wyota_20210420_models.UpdateAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.UpdateAliasResponse:
        """
        @summary 更新设备别名
        
        @param request: UpdateAliasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAliasResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias):
            body['Alias'] = request.alias
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAlias',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.UpdateAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alias(
        self,
        request: wyota_20210420_models.UpdateAliasRequest,
    ) -> wyota_20210420_models.UpdateAliasResponse:
        """
        @summary 更新设备别名
        
        @param request: UpdateAliasRequest
        @return: UpdateAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_alias_with_options(request, runtime)

    async def update_alias_async(
        self,
        request: wyota_20210420_models.UpdateAliasRequest,
    ) -> wyota_20210420_models.UpdateAliasResponse:
        """
        @summary 更新设备别名
        
        @param request: UpdateAliasRequest
        @return: UpdateAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_alias_with_options_async(request, runtime)

    def update_device_binded_end_user_with_options(
        self,
        request: wyota_20210420_models.UpdateDeviceBindedEndUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.UpdateDeviceBindedEndUserResponse:
        """
        @summary 批量更新设备绑定的终端用户
        
        @param request: UpdateDeviceBindedEndUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDeviceBindedEndUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.source_ad_end_users):
            body['SourceAdEndUsers'] = request.source_ad_end_users
        if not UtilClient.is_unset(request.source_end_user_ids):
            body['SourceEndUserIds'] = request.source_end_user_ids
        if not UtilClient.is_unset(request.target_ad_end_users):
            body['TargetAdEndUsers'] = request.target_ad_end_users
        if not UtilClient.is_unset(request.target_end_user_ids):
            body['TargetEndUserIds'] = request.target_end_user_ids
        if not UtilClient.is_unset(request.user_type):
            body['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDeviceBindedEndUser',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.UpdateDeviceBindedEndUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_device_binded_end_user_with_options_async(
        self,
        request: wyota_20210420_models.UpdateDeviceBindedEndUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.UpdateDeviceBindedEndUserResponse:
        """
        @summary 批量更新设备绑定的终端用户
        
        @param request: UpdateDeviceBindedEndUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDeviceBindedEndUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.serial_no):
            body['SerialNo'] = request.serial_no
        if not UtilClient.is_unset(request.source_ad_end_users):
            body['SourceAdEndUsers'] = request.source_ad_end_users
        if not UtilClient.is_unset(request.source_end_user_ids):
            body['SourceEndUserIds'] = request.source_end_user_ids
        if not UtilClient.is_unset(request.target_ad_end_users):
            body['TargetAdEndUsers'] = request.target_ad_end_users
        if not UtilClient.is_unset(request.target_end_user_ids):
            body['TargetEndUserIds'] = request.target_end_user_ids
        if not UtilClient.is_unset(request.user_type):
            body['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDeviceBindedEndUser',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.UpdateDeviceBindedEndUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_device_binded_end_user(
        self,
        request: wyota_20210420_models.UpdateDeviceBindedEndUserRequest,
    ) -> wyota_20210420_models.UpdateDeviceBindedEndUserResponse:
        """
        @summary 批量更新设备绑定的终端用户
        
        @param request: UpdateDeviceBindedEndUserRequest
        @return: UpdateDeviceBindedEndUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_device_binded_end_user_with_options(request, runtime)

    async def update_device_binded_end_user_async(
        self,
        request: wyota_20210420_models.UpdateDeviceBindedEndUserRequest,
    ) -> wyota_20210420_models.UpdateDeviceBindedEndUserResponse:
        """
        @summary 批量更新设备绑定的终端用户
        
        @param request: UpdateDeviceBindedEndUserRequest
        @return: UpdateDeviceBindedEndUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_device_binded_end_user_with_options_async(request, runtime)

    def update_label_with_options(
        self,
        request: wyota_20210420_models.UpdateLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.UpdateLabelResponse:
        """
        @summary 修改标签
        
        @param request: UpdateLabelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLabelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.label_content):
            body['LabelContent'] = request.label_content
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLabel',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.UpdateLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_label_with_options_async(
        self,
        request: wyota_20210420_models.UpdateLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.UpdateLabelResponse:
        """
        @summary 修改标签
        
        @param request: UpdateLabelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLabelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.label_content):
            body['LabelContent'] = request.label_content
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLabel',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.UpdateLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_label(
        self,
        request: wyota_20210420_models.UpdateLabelRequest,
    ) -> wyota_20210420_models.UpdateLabelResponse:
        """
        @summary 修改标签
        
        @param request: UpdateLabelRequest
        @return: UpdateLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_label_with_options(request, runtime)

    async def update_label_async(
        self,
        request: wyota_20210420_models.UpdateLabelRequest,
    ) -> wyota_20210420_models.UpdateLabelResponse:
        """
        @summary 修改标签
        
        @param request: UpdateLabelRequest
        @return: UpdateLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_label_with_options_async(request, runtime)

    def update_terminal_policy_with_options(
        self,
        request: wyota_20210420_models.UpdateTerminalPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.UpdateTerminalPolicyResponse:
        """
        @summary 修改终端策略
        
        @param request: UpdateTerminalPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTerminalPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.display_layout):
            body['DisplayLayout'] = request.display_layout
        if not UtilClient.is_unset(request.display_resolution):
            body['DisplayResolution'] = request.display_resolution
        if not UtilClient.is_unset(request.display_scale_ratio):
            body['DisplayScaleRatio'] = request.display_scale_ratio
        if not UtilClient.is_unset(request.enable_auto_lock_screen):
            body['EnableAutoLockScreen'] = request.enable_auto_lock_screen
        if not UtilClient.is_unset(request.enable_auto_login):
            body['EnableAutoLogin'] = request.enable_auto_login
        if not UtilClient.is_unset(request.enable_bluetooth):
            body['EnableBluetooth'] = request.enable_bluetooth
        if not UtilClient.is_unset(request.enable_modify_password):
            body['EnableModifyPassword'] = request.enable_modify_password
        if not UtilClient.is_unset(request.enable_scheduled_shutdown):
            body['EnableScheduledShutdown'] = request.enable_scheduled_shutdown
        if not UtilClient.is_unset(request.enable_switch_personal):
            body['EnableSwitchPersonal'] = request.enable_switch_personal
        if not UtilClient.is_unset(request.enable_wlan):
            body['EnableWlan'] = request.enable_wlan
        if not UtilClient.is_unset(request.idle_timeout):
            body['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.idle_timeout_action):
            body['IdleTimeoutAction'] = request.idle_timeout_action
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.power_button_define):
            body['PowerButtonDefine'] = request.power_button_define
        if not UtilClient.is_unset(request.power_button_define_for_as):
            body['PowerButtonDefineForAs'] = request.power_button_define_for_as
        if not UtilClient.is_unset(request.power_button_define_for_ns):
            body['PowerButtonDefineForNs'] = request.power_button_define_for_ns
        if not UtilClient.is_unset(request.power_on_behavior):
            body['PowerOnBehavior'] = request.power_on_behavior
        if not UtilClient.is_unset(request.scheduled_shutdown):
            body['ScheduledShutdown'] = request.scheduled_shutdown
        if not UtilClient.is_unset(request.setting_lock):
            body['SettingLock'] = request.setting_lock
        if not UtilClient.is_unset(request.terminal_policy_id):
            body['TerminalPolicyId'] = request.terminal_policy_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTerminalPolicy',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.UpdateTerminalPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_terminal_policy_with_options_async(
        self,
        request: wyota_20210420_models.UpdateTerminalPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> wyota_20210420_models.UpdateTerminalPolicyResponse:
        """
        @summary 修改终端策略
        
        @param request: UpdateTerminalPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTerminalPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.display_layout):
            body['DisplayLayout'] = request.display_layout
        if not UtilClient.is_unset(request.display_resolution):
            body['DisplayResolution'] = request.display_resolution
        if not UtilClient.is_unset(request.display_scale_ratio):
            body['DisplayScaleRatio'] = request.display_scale_ratio
        if not UtilClient.is_unset(request.enable_auto_lock_screen):
            body['EnableAutoLockScreen'] = request.enable_auto_lock_screen
        if not UtilClient.is_unset(request.enable_auto_login):
            body['EnableAutoLogin'] = request.enable_auto_login
        if not UtilClient.is_unset(request.enable_bluetooth):
            body['EnableBluetooth'] = request.enable_bluetooth
        if not UtilClient.is_unset(request.enable_modify_password):
            body['EnableModifyPassword'] = request.enable_modify_password
        if not UtilClient.is_unset(request.enable_scheduled_shutdown):
            body['EnableScheduledShutdown'] = request.enable_scheduled_shutdown
        if not UtilClient.is_unset(request.enable_switch_personal):
            body['EnableSwitchPersonal'] = request.enable_switch_personal
        if not UtilClient.is_unset(request.enable_wlan):
            body['EnableWlan'] = request.enable_wlan
        if not UtilClient.is_unset(request.idle_timeout):
            body['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.idle_timeout_action):
            body['IdleTimeoutAction'] = request.idle_timeout_action
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.power_button_define):
            body['PowerButtonDefine'] = request.power_button_define
        if not UtilClient.is_unset(request.power_button_define_for_as):
            body['PowerButtonDefineForAs'] = request.power_button_define_for_as
        if not UtilClient.is_unset(request.power_button_define_for_ns):
            body['PowerButtonDefineForNs'] = request.power_button_define_for_ns
        if not UtilClient.is_unset(request.power_on_behavior):
            body['PowerOnBehavior'] = request.power_on_behavior
        if not UtilClient.is_unset(request.scheduled_shutdown):
            body['ScheduledShutdown'] = request.scheduled_shutdown
        if not UtilClient.is_unset(request.setting_lock):
            body['SettingLock'] = request.setting_lock
        if not UtilClient.is_unset(request.terminal_policy_id):
            body['TerminalPolicyId'] = request.terminal_policy_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTerminalPolicy',
            version='2021-04-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            wyota_20210420_models.UpdateTerminalPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_terminal_policy(
        self,
        request: wyota_20210420_models.UpdateTerminalPolicyRequest,
    ) -> wyota_20210420_models.UpdateTerminalPolicyResponse:
        """
        @summary 修改终端策略
        
        @param request: UpdateTerminalPolicyRequest
        @return: UpdateTerminalPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_terminal_policy_with_options(request, runtime)

    async def update_terminal_policy_async(
        self,
        request: wyota_20210420_models.UpdateTerminalPolicyRequest,
    ) -> wyota_20210420_models.UpdateTerminalPolicyResponse:
        """
        @summary 修改终端策略
        
        @param request: UpdateTerminalPolicyRequest
        @return: UpdateTerminalPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_terminal_policy_with_options_async(request, runtime)
