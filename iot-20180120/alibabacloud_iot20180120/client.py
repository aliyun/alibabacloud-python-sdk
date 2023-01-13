# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore
from typing import Dict

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_tea_rpc import models as rpc_models
from alibabacloud_iot20180120 import models as iot_20180120_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_rpc_util.client import Client as RPCUtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(
        self, 
        config: rpc_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-2-pop': 'iot.aliyuncs.com',
            'ap-south-1': 'iot.aliyuncs.com',
            'ap-southeast-2': 'iot.aliyuncs.com',
            'ap-southeast-3': 'iot.aliyuncs.com',
            'ap-southeast-5': 'iot.aliyuncs.com',
            'cn-beijing-finance-1': 'iot.aliyuncs.com',
            'cn-beijing-finance-pop': 'iot.aliyuncs.com',
            'cn-beijing-gov-1': 'iot.aliyuncs.com',
            'cn-beijing-nu16-b01': 'iot.aliyuncs.com',
            'cn-chengdu': 'iot.aliyuncs.com',
            'cn-edge-1': 'iot.aliyuncs.com',
            'cn-fujian': 'iot.aliyuncs.com',
            'cn-haidian-cm12-c01': 'iot.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'iot.aliyuncs.com',
            'cn-hangzhou-finance': 'iot.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'iot.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'iot.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'iot.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'iot.aliyuncs.com',
            'cn-hangzhou-test-306': 'iot.aliyuncs.com',
            'cn-hongkong': 'iot.aliyuncs.com',
            'cn-hongkong-finance-pop': 'iot.aliyuncs.com',
            'cn-huhehaote': 'iot.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'iot.aliyuncs.com',
            'cn-qingdao': 'iot.aliyuncs.com',
            'cn-qingdao-nebula': 'iot.aliyuncs.com',
            'cn-shanghai-et15-b01': 'iot.aliyuncs.com',
            'cn-shanghai-et2-b01': 'iot.aliyuncs.com',
            'cn-shanghai-finance-1': 'iot.aliyuncs.com',
            'cn-shanghai-inner': 'iot.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'iot.aliyuncs.com',
            'cn-shenzhen-finance-1': 'iot.aliyuncs.com',
            'cn-shenzhen-inner': 'iot.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'iot.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'iot.aliyuncs.com',
            'cn-wuhan': 'iot.aliyuncs.com',
            'cn-wulanchabu': 'iot.aliyuncs.com',
            'cn-yushanfang': 'iot.aliyuncs.com',
            'cn-zhangbei': 'iot.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'iot.aliyuncs.com',
            'cn-zhangjiakou': 'iot.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'iot.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'iot.aliyuncs.com',
            'eu-west-1': 'iot.aliyuncs.com',
            'eu-west-1-oxs': 'iot.aliyuncs.com',
            'me-east-1': 'iot.aliyuncs.com',
            'rus-west-1-pop': 'iot.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('iot', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def add_data_for_api_source_with_options(
        self,
        request: iot_20180120_models.AddDataForApiSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.AddDataForApiSourceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.AddDataForApiSourceResponse(),
            self.do_request('AddDataForApiSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def add_data_for_api_source_with_options_async(
        self,
        request: iot_20180120_models.AddDataForApiSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.AddDataForApiSourceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.AddDataForApiSourceResponse(),
            await self.do_request_async('AddDataForApiSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def add_data_for_api_source(
        self,
        request: iot_20180120_models.AddDataForApiSourceRequest,
    ) -> iot_20180120_models.AddDataForApiSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_data_for_api_source_with_options(request, runtime)

    async def add_data_for_api_source_async(
        self,
        request: iot_20180120_models.AddDataForApiSourceRequest,
    ) -> iot_20180120_models.AddDataForApiSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_data_for_api_source_with_options_async(request, runtime)

    def add_share_task_device_with_options(
        self,
        request: iot_20180120_models.AddShareTaskDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.AddShareTaskDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.AddShareTaskDeviceResponse(),
            self.do_request('AddShareTaskDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def add_share_task_device_with_options_async(
        self,
        request: iot_20180120_models.AddShareTaskDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.AddShareTaskDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.AddShareTaskDeviceResponse(),
            await self.do_request_async('AddShareTaskDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def add_share_task_device(
        self,
        request: iot_20180120_models.AddShareTaskDeviceRequest,
    ) -> iot_20180120_models.AddShareTaskDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_share_task_device_with_options(request, runtime)

    async def add_share_task_device_async(
        self,
        request: iot_20180120_models.AddShareTaskDeviceRequest,
    ) -> iot_20180120_models.AddShareTaskDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_share_task_device_with_options_async(request, runtime)

    def attach_destination_with_options(
        self,
        request: iot_20180120_models.AttachDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.AttachDestinationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.AttachDestinationResponse(),
            self.do_request('AttachDestination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def attach_destination_with_options_async(
        self,
        request: iot_20180120_models.AttachDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.AttachDestinationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.AttachDestinationResponse(),
            await self.do_request_async('AttachDestination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def attach_destination(
        self,
        request: iot_20180120_models.AttachDestinationRequest,
    ) -> iot_20180120_models.AttachDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_destination_with_options(request, runtime)

    async def attach_destination_async(
        self,
        request: iot_20180120_models.AttachDestinationRequest,
    ) -> iot_20180120_models.AttachDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_destination_with_options_async(request, runtime)

    def attach_parser_data_source_with_options(
        self,
        request: iot_20180120_models.AttachParserDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.AttachParserDataSourceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.AttachParserDataSourceResponse(),
            self.do_request('AttachParserDataSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def attach_parser_data_source_with_options_async(
        self,
        request: iot_20180120_models.AttachParserDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.AttachParserDataSourceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.AttachParserDataSourceResponse(),
            await self.do_request_async('AttachParserDataSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def attach_parser_data_source(
        self,
        request: iot_20180120_models.AttachParserDataSourceRequest,
    ) -> iot_20180120_models.AttachParserDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_parser_data_source_with_options(request, runtime)

    async def attach_parser_data_source_async(
        self,
        request: iot_20180120_models.AttachParserDataSourceRequest,
    ) -> iot_20180120_models.AttachParserDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_parser_data_source_with_options_async(request, runtime)

    def batch_add_data_for_api_source_with_options(
        self,
        tmp: iot_20180120_models.BatchAddDataForApiSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchAddDataForApiSourceResponse:
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.BatchAddDataForApiSourceShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.content_list):
            request.content_list_shrink = UtilClient.to_jsonstring(tmp.content_list)
        return TeaCore.from_map(
            iot_20180120_models.BatchAddDataForApiSourceResponse(),
            self.do_request('BatchAddDataForApiSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_add_data_for_api_source_with_options_async(
        self,
        tmp: iot_20180120_models.BatchAddDataForApiSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchAddDataForApiSourceResponse:
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.BatchAddDataForApiSourceShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.content_list):
            request.content_list_shrink = UtilClient.to_jsonstring(tmp.content_list)
        return TeaCore.from_map(
            iot_20180120_models.BatchAddDataForApiSourceResponse(),
            await self.do_request_async('BatchAddDataForApiSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_add_data_for_api_source(
        self,
        request: iot_20180120_models.BatchAddDataForApiSourceRequest,
    ) -> iot_20180120_models.BatchAddDataForApiSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_add_data_for_api_source_with_options(request, runtime)

    async def batch_add_data_for_api_source_async(
        self,
        request: iot_20180120_models.BatchAddDataForApiSourceRequest,
    ) -> iot_20180120_models.BatchAddDataForApiSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_add_data_for_api_source_with_options_async(request, runtime)

    def batch_add_device_group_relations_with_options(
        self,
        request: iot_20180120_models.BatchAddDeviceGroupRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchAddDeviceGroupRelationsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchAddDeviceGroupRelationsResponse(),
            self.do_request('BatchAddDeviceGroupRelations', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_add_device_group_relations_with_options_async(
        self,
        request: iot_20180120_models.BatchAddDeviceGroupRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchAddDeviceGroupRelationsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchAddDeviceGroupRelationsResponse(),
            await self.do_request_async('BatchAddDeviceGroupRelations', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_add_device_group_relations(
        self,
        request: iot_20180120_models.BatchAddDeviceGroupRelationsRequest,
    ) -> iot_20180120_models.BatchAddDeviceGroupRelationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_add_device_group_relations_with_options(request, runtime)

    async def batch_add_device_group_relations_async(
        self,
        request: iot_20180120_models.BatchAddDeviceGroupRelationsRequest,
    ) -> iot_20180120_models.BatchAddDeviceGroupRelationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_add_device_group_relations_with_options_async(request, runtime)

    def batch_add_thing_topo_with_options(
        self,
        request: iot_20180120_models.BatchAddThingTopoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchAddThingTopoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchAddThingTopoResponse(),
            self.do_request('BatchAddThingTopo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_add_thing_topo_with_options_async(
        self,
        request: iot_20180120_models.BatchAddThingTopoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchAddThingTopoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchAddThingTopoResponse(),
            await self.do_request_async('BatchAddThingTopo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_add_thing_topo(
        self,
        request: iot_20180120_models.BatchAddThingTopoRequest,
    ) -> iot_20180120_models.BatchAddThingTopoResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_add_thing_topo_with_options(request, runtime)

    async def batch_add_thing_topo_async(
        self,
        request: iot_20180120_models.BatchAddThingTopoRequest,
    ) -> iot_20180120_models.BatchAddThingTopoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_add_thing_topo_with_options_async(request, runtime)

    def batch_bind_device_to_edge_instance_with_driver_with_options(
        self,
        request: iot_20180120_models.BatchBindDeviceToEdgeInstanceWithDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchBindDeviceToEdgeInstanceWithDriverResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchBindDeviceToEdgeInstanceWithDriverResponse(),
            self.do_request('BatchBindDeviceToEdgeInstanceWithDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_bind_device_to_edge_instance_with_driver_with_options_async(
        self,
        request: iot_20180120_models.BatchBindDeviceToEdgeInstanceWithDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchBindDeviceToEdgeInstanceWithDriverResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchBindDeviceToEdgeInstanceWithDriverResponse(),
            await self.do_request_async('BatchBindDeviceToEdgeInstanceWithDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_bind_device_to_edge_instance_with_driver(
        self,
        request: iot_20180120_models.BatchBindDeviceToEdgeInstanceWithDriverRequest,
    ) -> iot_20180120_models.BatchBindDeviceToEdgeInstanceWithDriverResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_device_to_edge_instance_with_driver_with_options(request, runtime)

    async def batch_bind_device_to_edge_instance_with_driver_async(
        self,
        request: iot_20180120_models.BatchBindDeviceToEdgeInstanceWithDriverRequest,
    ) -> iot_20180120_models.BatchBindDeviceToEdgeInstanceWithDriverResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_bind_device_to_edge_instance_with_driver_with_options_async(request, runtime)

    def batch_bind_devices_into_project_with_options(
        self,
        request: iot_20180120_models.BatchBindDevicesIntoProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchBindDevicesIntoProjectResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchBindDevicesIntoProjectResponse(),
            self.do_request('BatchBindDevicesIntoProject', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_bind_devices_into_project_with_options_async(
        self,
        request: iot_20180120_models.BatchBindDevicesIntoProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchBindDevicesIntoProjectResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchBindDevicesIntoProjectResponse(),
            await self.do_request_async('BatchBindDevicesIntoProject', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_bind_devices_into_project(
        self,
        request: iot_20180120_models.BatchBindDevicesIntoProjectRequest,
    ) -> iot_20180120_models.BatchBindDevicesIntoProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_devices_into_project_with_options(request, runtime)

    async def batch_bind_devices_into_project_async(
        self,
        request: iot_20180120_models.BatchBindDevicesIntoProjectRequest,
    ) -> iot_20180120_models.BatchBindDevicesIntoProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_bind_devices_into_project_with_options_async(request, runtime)

    def batch_bind_products_into_project_with_options(
        self,
        request: iot_20180120_models.BatchBindProductsIntoProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchBindProductsIntoProjectResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchBindProductsIntoProjectResponse(),
            self.do_request('BatchBindProductsIntoProject', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_bind_products_into_project_with_options_async(
        self,
        request: iot_20180120_models.BatchBindProductsIntoProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchBindProductsIntoProjectResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchBindProductsIntoProjectResponse(),
            await self.do_request_async('BatchBindProductsIntoProject', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_bind_products_into_project(
        self,
        request: iot_20180120_models.BatchBindProductsIntoProjectRequest,
    ) -> iot_20180120_models.BatchBindProductsIntoProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_products_into_project_with_options(request, runtime)

    async def batch_bind_products_into_project_async(
        self,
        request: iot_20180120_models.BatchBindProductsIntoProjectRequest,
    ) -> iot_20180120_models.BatchBindProductsIntoProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_bind_products_into_project_with_options_async(request, runtime)

    def batch_check_device_names_with_options(
        self,
        request: iot_20180120_models.BatchCheckDeviceNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchCheckDeviceNamesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchCheckDeviceNamesResponse(),
            self.do_request('BatchCheckDeviceNames', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_check_device_names_with_options_async(
        self,
        request: iot_20180120_models.BatchCheckDeviceNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchCheckDeviceNamesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchCheckDeviceNamesResponse(),
            await self.do_request_async('BatchCheckDeviceNames', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_check_device_names(
        self,
        request: iot_20180120_models.BatchCheckDeviceNamesRequest,
    ) -> iot_20180120_models.BatchCheckDeviceNamesResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_check_device_names_with_options(request, runtime)

    async def batch_check_device_names_async(
        self,
        request: iot_20180120_models.BatchCheckDeviceNamesRequest,
    ) -> iot_20180120_models.BatchCheckDeviceNamesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_check_device_names_with_options_async(request, runtime)

    def batch_check_import_device_with_options(
        self,
        request: iot_20180120_models.BatchCheckImportDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchCheckImportDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchCheckImportDeviceResponse(),
            self.do_request('BatchCheckImportDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_check_import_device_with_options_async(
        self,
        request: iot_20180120_models.BatchCheckImportDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchCheckImportDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchCheckImportDeviceResponse(),
            await self.do_request_async('BatchCheckImportDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_check_import_device(
        self,
        request: iot_20180120_models.BatchCheckImportDeviceRequest,
    ) -> iot_20180120_models.BatchCheckImportDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_check_import_device_with_options(request, runtime)

    async def batch_check_import_device_async(
        self,
        request: iot_20180120_models.BatchCheckImportDeviceRequest,
    ) -> iot_20180120_models.BatchCheckImportDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_check_import_device_with_options_async(request, runtime)

    def batch_check_vehicle_device_with_options(
        self,
        request: iot_20180120_models.BatchCheckVehicleDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchCheckVehicleDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchCheckVehicleDeviceResponse(),
            self.do_request('BatchCheckVehicleDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_check_vehicle_device_with_options_async(
        self,
        request: iot_20180120_models.BatchCheckVehicleDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchCheckVehicleDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchCheckVehicleDeviceResponse(),
            await self.do_request_async('BatchCheckVehicleDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_check_vehicle_device(
        self,
        request: iot_20180120_models.BatchCheckVehicleDeviceRequest,
    ) -> iot_20180120_models.BatchCheckVehicleDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_check_vehicle_device_with_options(request, runtime)

    async def batch_check_vehicle_device_async(
        self,
        request: iot_20180120_models.BatchCheckVehicleDeviceRequest,
    ) -> iot_20180120_models.BatchCheckVehicleDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_check_vehicle_device_with_options_async(request, runtime)

    def batch_clear_edge_instance_device_config_with_options(
        self,
        request: iot_20180120_models.BatchClearEdgeInstanceDeviceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchClearEdgeInstanceDeviceConfigResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchClearEdgeInstanceDeviceConfigResponse(),
            self.do_request('BatchClearEdgeInstanceDeviceConfig', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_clear_edge_instance_device_config_with_options_async(
        self,
        request: iot_20180120_models.BatchClearEdgeInstanceDeviceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchClearEdgeInstanceDeviceConfigResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchClearEdgeInstanceDeviceConfigResponse(),
            await self.do_request_async('BatchClearEdgeInstanceDeviceConfig', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_clear_edge_instance_device_config(
        self,
        request: iot_20180120_models.BatchClearEdgeInstanceDeviceConfigRequest,
    ) -> iot_20180120_models.BatchClearEdgeInstanceDeviceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_clear_edge_instance_device_config_with_options(request, runtime)

    async def batch_clear_edge_instance_device_config_async(
        self,
        request: iot_20180120_models.BatchClearEdgeInstanceDeviceConfigRequest,
    ) -> iot_20180120_models.BatchClearEdgeInstanceDeviceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_clear_edge_instance_device_config_with_options_async(request, runtime)

    def batch_create_sound_code_label_with_options(
        self,
        request: iot_20180120_models.BatchCreateSoundCodeLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchCreateSoundCodeLabelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchCreateSoundCodeLabelResponse(),
            self.do_request('BatchCreateSoundCodeLabel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_create_sound_code_label_with_options_async(
        self,
        request: iot_20180120_models.BatchCreateSoundCodeLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchCreateSoundCodeLabelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchCreateSoundCodeLabelResponse(),
            await self.do_request_async('BatchCreateSoundCodeLabel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_create_sound_code_label(
        self,
        request: iot_20180120_models.BatchCreateSoundCodeLabelRequest,
    ) -> iot_20180120_models.BatchCreateSoundCodeLabelResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_create_sound_code_label_with_options(request, runtime)

    async def batch_create_sound_code_label_async(
        self,
        request: iot_20180120_models.BatchCreateSoundCodeLabelRequest,
    ) -> iot_20180120_models.BatchCreateSoundCodeLabelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_create_sound_code_label_with_options_async(request, runtime)

    def batch_create_sound_code_label_with_labels_with_options(
        self,
        request: iot_20180120_models.BatchCreateSoundCodeLabelWithLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchCreateSoundCodeLabelWithLabelsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchCreateSoundCodeLabelWithLabelsResponse(),
            self.do_request('BatchCreateSoundCodeLabelWithLabels', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_create_sound_code_label_with_labels_with_options_async(
        self,
        request: iot_20180120_models.BatchCreateSoundCodeLabelWithLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchCreateSoundCodeLabelWithLabelsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchCreateSoundCodeLabelWithLabelsResponse(),
            await self.do_request_async('BatchCreateSoundCodeLabelWithLabels', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_create_sound_code_label_with_labels(
        self,
        request: iot_20180120_models.BatchCreateSoundCodeLabelWithLabelsRequest,
    ) -> iot_20180120_models.BatchCreateSoundCodeLabelWithLabelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_create_sound_code_label_with_labels_with_options(request, runtime)

    async def batch_create_sound_code_label_with_labels_async(
        self,
        request: iot_20180120_models.BatchCreateSoundCodeLabelWithLabelsRequest,
    ) -> iot_20180120_models.BatchCreateSoundCodeLabelWithLabelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_create_sound_code_label_with_labels_with_options_async(request, runtime)

    def batch_delete_device_group_relations_with_options(
        self,
        request: iot_20180120_models.BatchDeleteDeviceGroupRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchDeleteDeviceGroupRelationsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchDeleteDeviceGroupRelationsResponse(),
            self.do_request('BatchDeleteDeviceGroupRelations', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_delete_device_group_relations_with_options_async(
        self,
        request: iot_20180120_models.BatchDeleteDeviceGroupRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchDeleteDeviceGroupRelationsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchDeleteDeviceGroupRelationsResponse(),
            await self.do_request_async('BatchDeleteDeviceGroupRelations', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_delete_device_group_relations(
        self,
        request: iot_20180120_models.BatchDeleteDeviceGroupRelationsRequest,
    ) -> iot_20180120_models.BatchDeleteDeviceGroupRelationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_device_group_relations_with_options(request, runtime)

    async def batch_delete_device_group_relations_async(
        self,
        request: iot_20180120_models.BatchDeleteDeviceGroupRelationsRequest,
    ) -> iot_20180120_models.BatchDeleteDeviceGroupRelationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_device_group_relations_with_options_async(request, runtime)

    def batch_delete_edge_instance_channel_with_options(
        self,
        request: iot_20180120_models.BatchDeleteEdgeInstanceChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchDeleteEdgeInstanceChannelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchDeleteEdgeInstanceChannelResponse(),
            self.do_request('BatchDeleteEdgeInstanceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_delete_edge_instance_channel_with_options_async(
        self,
        request: iot_20180120_models.BatchDeleteEdgeInstanceChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchDeleteEdgeInstanceChannelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchDeleteEdgeInstanceChannelResponse(),
            await self.do_request_async('BatchDeleteEdgeInstanceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_delete_edge_instance_channel(
        self,
        request: iot_20180120_models.BatchDeleteEdgeInstanceChannelRequest,
    ) -> iot_20180120_models.BatchDeleteEdgeInstanceChannelResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_edge_instance_channel_with_options(request, runtime)

    async def batch_delete_edge_instance_channel_async(
        self,
        request: iot_20180120_models.BatchDeleteEdgeInstanceChannelRequest,
    ) -> iot_20180120_models.BatchDeleteEdgeInstanceChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_edge_instance_channel_with_options_async(request, runtime)

    def batch_get_device_bind_status_with_options(
        self,
        request: iot_20180120_models.BatchGetDeviceBindStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchGetDeviceBindStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchGetDeviceBindStatusResponse(),
            self.do_request('BatchGetDeviceBindStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_get_device_bind_status_with_options_async(
        self,
        request: iot_20180120_models.BatchGetDeviceBindStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchGetDeviceBindStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchGetDeviceBindStatusResponse(),
            await self.do_request_async('BatchGetDeviceBindStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_get_device_bind_status(
        self,
        request: iot_20180120_models.BatchGetDeviceBindStatusRequest,
    ) -> iot_20180120_models.BatchGetDeviceBindStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_get_device_bind_status_with_options(request, runtime)

    async def batch_get_device_bind_status_async(
        self,
        request: iot_20180120_models.BatchGetDeviceBindStatusRequest,
    ) -> iot_20180120_models.BatchGetDeviceBindStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_get_device_bind_status_with_options_async(request, runtime)

    def batch_get_device_state_with_options(
        self,
        request: iot_20180120_models.BatchGetDeviceStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchGetDeviceStateResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchGetDeviceStateResponse(),
            self.do_request('BatchGetDeviceState', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_get_device_state_with_options_async(
        self,
        request: iot_20180120_models.BatchGetDeviceStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchGetDeviceStateResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchGetDeviceStateResponse(),
            await self.do_request_async('BatchGetDeviceState', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_get_device_state(
        self,
        request: iot_20180120_models.BatchGetDeviceStateRequest,
    ) -> iot_20180120_models.BatchGetDeviceStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_get_device_state_with_options(request, runtime)

    async def batch_get_device_state_async(
        self,
        request: iot_20180120_models.BatchGetDeviceStateRequest,
    ) -> iot_20180120_models.BatchGetDeviceStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_get_device_state_with_options_async(request, runtime)

    def batch_get_edge_driver_with_options(
        self,
        request: iot_20180120_models.BatchGetEdgeDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchGetEdgeDriverResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeDriverResponse(),
            self.do_request('BatchGetEdgeDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_get_edge_driver_with_options_async(
        self,
        request: iot_20180120_models.BatchGetEdgeDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchGetEdgeDriverResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeDriverResponse(),
            await self.do_request_async('BatchGetEdgeDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_get_edge_driver(
        self,
        request: iot_20180120_models.BatchGetEdgeDriverRequest,
    ) -> iot_20180120_models.BatchGetEdgeDriverResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_get_edge_driver_with_options(request, runtime)

    async def batch_get_edge_driver_async(
        self,
        request: iot_20180120_models.BatchGetEdgeDriverRequest,
    ) -> iot_20180120_models.BatchGetEdgeDriverResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_get_edge_driver_with_options_async(request, runtime)

    def batch_get_edge_instance_channel_with_options(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchGetEdgeInstanceChannelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceChannelResponse(),
            self.do_request('BatchGetEdgeInstanceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_get_edge_instance_channel_with_options_async(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchGetEdgeInstanceChannelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceChannelResponse(),
            await self.do_request_async('BatchGetEdgeInstanceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_get_edge_instance_channel(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceChannelRequest,
    ) -> iot_20180120_models.BatchGetEdgeInstanceChannelResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_get_edge_instance_channel_with_options(request, runtime)

    async def batch_get_edge_instance_channel_async(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceChannelRequest,
    ) -> iot_20180120_models.BatchGetEdgeInstanceChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_get_edge_instance_channel_with_options_async(request, runtime)

    def batch_get_edge_instance_device_channel_with_options(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceDeviceChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchGetEdgeInstanceDeviceChannelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceDeviceChannelResponse(),
            self.do_request('BatchGetEdgeInstanceDeviceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_get_edge_instance_device_channel_with_options_async(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceDeviceChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchGetEdgeInstanceDeviceChannelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceDeviceChannelResponse(),
            await self.do_request_async('BatchGetEdgeInstanceDeviceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_get_edge_instance_device_channel(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceDeviceChannelRequest,
    ) -> iot_20180120_models.BatchGetEdgeInstanceDeviceChannelResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_get_edge_instance_device_channel_with_options(request, runtime)

    async def batch_get_edge_instance_device_channel_async(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceDeviceChannelRequest,
    ) -> iot_20180120_models.BatchGetEdgeInstanceDeviceChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_get_edge_instance_device_channel_with_options_async(request, runtime)

    def batch_get_edge_instance_device_config_with_options(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceDeviceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchGetEdgeInstanceDeviceConfigResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceDeviceConfigResponse(),
            self.do_request('BatchGetEdgeInstanceDeviceConfig', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_get_edge_instance_device_config_with_options_async(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceDeviceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchGetEdgeInstanceDeviceConfigResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceDeviceConfigResponse(),
            await self.do_request_async('BatchGetEdgeInstanceDeviceConfig', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_get_edge_instance_device_config(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceDeviceConfigRequest,
    ) -> iot_20180120_models.BatchGetEdgeInstanceDeviceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_get_edge_instance_device_config_with_options(request, runtime)

    async def batch_get_edge_instance_device_config_async(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceDeviceConfigRequest,
    ) -> iot_20180120_models.BatchGetEdgeInstanceDeviceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_get_edge_instance_device_config_with_options_async(request, runtime)

    def batch_get_edge_instance_device_driver_with_options(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceDeviceDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchGetEdgeInstanceDeviceDriverResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceDeviceDriverResponse(),
            self.do_request('BatchGetEdgeInstanceDeviceDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_get_edge_instance_device_driver_with_options_async(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceDeviceDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchGetEdgeInstanceDeviceDriverResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceDeviceDriverResponse(),
            await self.do_request_async('BatchGetEdgeInstanceDeviceDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_get_edge_instance_device_driver(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceDeviceDriverRequest,
    ) -> iot_20180120_models.BatchGetEdgeInstanceDeviceDriverResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_get_edge_instance_device_driver_with_options(request, runtime)

    async def batch_get_edge_instance_device_driver_async(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceDeviceDriverRequest,
    ) -> iot_20180120_models.BatchGetEdgeInstanceDeviceDriverResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_get_edge_instance_device_driver_with_options_async(request, runtime)

    def batch_get_edge_instance_driver_configs_with_options(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceDriverConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchGetEdgeInstanceDriverConfigsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceDriverConfigsResponse(),
            self.do_request('BatchGetEdgeInstanceDriverConfigs', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_get_edge_instance_driver_configs_with_options_async(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceDriverConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchGetEdgeInstanceDriverConfigsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceDriverConfigsResponse(),
            await self.do_request_async('BatchGetEdgeInstanceDriverConfigs', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_get_edge_instance_driver_configs(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceDriverConfigsRequest,
    ) -> iot_20180120_models.BatchGetEdgeInstanceDriverConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_get_edge_instance_driver_configs_with_options(request, runtime)

    async def batch_get_edge_instance_driver_configs_async(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceDriverConfigsRequest,
    ) -> iot_20180120_models.BatchGetEdgeInstanceDriverConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_get_edge_instance_driver_configs_with_options_async(request, runtime)

    def batch_import_device_with_options(
        self,
        request: iot_20180120_models.BatchImportDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchImportDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchImportDeviceResponse(),
            self.do_request('BatchImportDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_import_device_with_options_async(
        self,
        request: iot_20180120_models.BatchImportDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchImportDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchImportDeviceResponse(),
            await self.do_request_async('BatchImportDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_import_device(
        self,
        request: iot_20180120_models.BatchImportDeviceRequest,
    ) -> iot_20180120_models.BatchImportDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_import_device_with_options(request, runtime)

    async def batch_import_device_async(
        self,
        request: iot_20180120_models.BatchImportDeviceRequest,
    ) -> iot_20180120_models.BatchImportDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_import_device_with_options_async(request, runtime)

    def batch_import_vehicle_device_with_options(
        self,
        request: iot_20180120_models.BatchImportVehicleDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchImportVehicleDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchImportVehicleDeviceResponse(),
            self.do_request('BatchImportVehicleDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_import_vehicle_device_with_options_async(
        self,
        request: iot_20180120_models.BatchImportVehicleDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchImportVehicleDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchImportVehicleDeviceResponse(),
            await self.do_request_async('BatchImportVehicleDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_import_vehicle_device(
        self,
        request: iot_20180120_models.BatchImportVehicleDeviceRequest,
    ) -> iot_20180120_models.BatchImportVehicleDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_import_vehicle_device_with_options(request, runtime)

    async def batch_import_vehicle_device_async(
        self,
        request: iot_20180120_models.BatchImportVehicleDeviceRequest,
    ) -> iot_20180120_models.BatchImportVehicleDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_import_vehicle_device_with_options_async(request, runtime)

    def batch_pub_with_options(
        self,
        request: iot_20180120_models.BatchPubRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchPubResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchPubResponse(),
            self.do_request('BatchPub', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_pub_with_options_async(
        self,
        request: iot_20180120_models.BatchPubRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchPubResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchPubResponse(),
            await self.do_request_async('BatchPub', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_pub(
        self,
        request: iot_20180120_models.BatchPubRequest,
    ) -> iot_20180120_models.BatchPubResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_pub_with_options(request, runtime)

    async def batch_pub_async(
        self,
        request: iot_20180120_models.BatchPubRequest,
    ) -> iot_20180120_models.BatchPubResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_pub_with_options_async(request, runtime)

    def batch_query_device_detail_with_options(
        self,
        request: iot_20180120_models.BatchQueryDeviceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchQueryDeviceDetailResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchQueryDeviceDetailResponse(),
            self.do_request('BatchQueryDeviceDetail', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_query_device_detail_with_options_async(
        self,
        request: iot_20180120_models.BatchQueryDeviceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchQueryDeviceDetailResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchQueryDeviceDetailResponse(),
            await self.do_request_async('BatchQueryDeviceDetail', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_query_device_detail(
        self,
        request: iot_20180120_models.BatchQueryDeviceDetailRequest,
    ) -> iot_20180120_models.BatchQueryDeviceDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_query_device_detail_with_options(request, runtime)

    async def batch_query_device_detail_async(
        self,
        request: iot_20180120_models.BatchQueryDeviceDetailRequest,
    ) -> iot_20180120_models.BatchQueryDeviceDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_query_device_detail_with_options_async(request, runtime)

    def batch_register_device_with_options(
        self,
        request: iot_20180120_models.BatchRegisterDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchRegisterDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchRegisterDeviceResponse(),
            self.do_request('BatchRegisterDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_register_device_with_options_async(
        self,
        request: iot_20180120_models.BatchRegisterDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchRegisterDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchRegisterDeviceResponse(),
            await self.do_request_async('BatchRegisterDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_register_device(
        self,
        request: iot_20180120_models.BatchRegisterDeviceRequest,
    ) -> iot_20180120_models.BatchRegisterDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_register_device_with_options(request, runtime)

    async def batch_register_device_async(
        self,
        request: iot_20180120_models.BatchRegisterDeviceRequest,
    ) -> iot_20180120_models.BatchRegisterDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_register_device_with_options_async(request, runtime)

    def batch_register_device_with_apply_id_with_options(
        self,
        request: iot_20180120_models.BatchRegisterDeviceWithApplyIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchRegisterDeviceWithApplyIdResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchRegisterDeviceWithApplyIdResponse(),
            self.do_request('BatchRegisterDeviceWithApplyId', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_register_device_with_apply_id_with_options_async(
        self,
        request: iot_20180120_models.BatchRegisterDeviceWithApplyIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchRegisterDeviceWithApplyIdResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchRegisterDeviceWithApplyIdResponse(),
            await self.do_request_async('BatchRegisterDeviceWithApplyId', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_register_device_with_apply_id(
        self,
        request: iot_20180120_models.BatchRegisterDeviceWithApplyIdRequest,
    ) -> iot_20180120_models.BatchRegisterDeviceWithApplyIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_register_device_with_apply_id_with_options(request, runtime)

    async def batch_register_device_with_apply_id_async(
        self,
        request: iot_20180120_models.BatchRegisterDeviceWithApplyIdRequest,
    ) -> iot_20180120_models.BatchRegisterDeviceWithApplyIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_register_device_with_apply_id_with_options_async(request, runtime)

    def batch_set_edge_instance_device_channel_with_options(
        self,
        request: iot_20180120_models.BatchSetEdgeInstanceDeviceChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchSetEdgeInstanceDeviceChannelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchSetEdgeInstanceDeviceChannelResponse(),
            self.do_request('BatchSetEdgeInstanceDeviceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_set_edge_instance_device_channel_with_options_async(
        self,
        request: iot_20180120_models.BatchSetEdgeInstanceDeviceChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchSetEdgeInstanceDeviceChannelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchSetEdgeInstanceDeviceChannelResponse(),
            await self.do_request_async('BatchSetEdgeInstanceDeviceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_set_edge_instance_device_channel(
        self,
        request: iot_20180120_models.BatchSetEdgeInstanceDeviceChannelRequest,
    ) -> iot_20180120_models.BatchSetEdgeInstanceDeviceChannelResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_set_edge_instance_device_channel_with_options(request, runtime)

    async def batch_set_edge_instance_device_channel_async(
        self,
        request: iot_20180120_models.BatchSetEdgeInstanceDeviceChannelRequest,
    ) -> iot_20180120_models.BatchSetEdgeInstanceDeviceChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_set_edge_instance_device_channel_with_options_async(request, runtime)

    def batch_set_edge_instance_device_config_with_options(
        self,
        request: iot_20180120_models.BatchSetEdgeInstanceDeviceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchSetEdgeInstanceDeviceConfigResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchSetEdgeInstanceDeviceConfigResponse(),
            self.do_request('BatchSetEdgeInstanceDeviceConfig', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_set_edge_instance_device_config_with_options_async(
        self,
        request: iot_20180120_models.BatchSetEdgeInstanceDeviceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchSetEdgeInstanceDeviceConfigResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchSetEdgeInstanceDeviceConfigResponse(),
            await self.do_request_async('BatchSetEdgeInstanceDeviceConfig', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_set_edge_instance_device_config(
        self,
        request: iot_20180120_models.BatchSetEdgeInstanceDeviceConfigRequest,
    ) -> iot_20180120_models.BatchSetEdgeInstanceDeviceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_set_edge_instance_device_config_with_options(request, runtime)

    async def batch_set_edge_instance_device_config_async(
        self,
        request: iot_20180120_models.BatchSetEdgeInstanceDeviceConfigRequest,
    ) -> iot_20180120_models.BatchSetEdgeInstanceDeviceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_set_edge_instance_device_config_with_options_async(request, runtime)

    def batch_unbind_device_from_edge_instance_with_options(
        self,
        request: iot_20180120_models.BatchUnbindDeviceFromEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchUnbindDeviceFromEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchUnbindDeviceFromEdgeInstanceResponse(),
            self.do_request('BatchUnbindDeviceFromEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_unbind_device_from_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.BatchUnbindDeviceFromEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchUnbindDeviceFromEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchUnbindDeviceFromEdgeInstanceResponse(),
            await self.do_request_async('BatchUnbindDeviceFromEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_unbind_device_from_edge_instance(
        self,
        request: iot_20180120_models.BatchUnbindDeviceFromEdgeInstanceRequest,
    ) -> iot_20180120_models.BatchUnbindDeviceFromEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_device_from_edge_instance_with_options(request, runtime)

    async def batch_unbind_device_from_edge_instance_async(
        self,
        request: iot_20180120_models.BatchUnbindDeviceFromEdgeInstanceRequest,
    ) -> iot_20180120_models.BatchUnbindDeviceFromEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_unbind_device_from_edge_instance_with_options_async(request, runtime)

    def batch_unbind_project_devices_with_options(
        self,
        request: iot_20180120_models.BatchUnbindProjectDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchUnbindProjectDevicesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchUnbindProjectDevicesResponse(),
            self.do_request('BatchUnbindProjectDevices', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_unbind_project_devices_with_options_async(
        self,
        request: iot_20180120_models.BatchUnbindProjectDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchUnbindProjectDevicesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchUnbindProjectDevicesResponse(),
            await self.do_request_async('BatchUnbindProjectDevices', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_unbind_project_devices(
        self,
        request: iot_20180120_models.BatchUnbindProjectDevicesRequest,
    ) -> iot_20180120_models.BatchUnbindProjectDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_project_devices_with_options(request, runtime)

    async def batch_unbind_project_devices_async(
        self,
        request: iot_20180120_models.BatchUnbindProjectDevicesRequest,
    ) -> iot_20180120_models.BatchUnbindProjectDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_unbind_project_devices_with_options_async(request, runtime)

    def batch_unbind_project_products_with_options(
        self,
        request: iot_20180120_models.BatchUnbindProjectProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchUnbindProjectProductsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchUnbindProjectProductsResponse(),
            self.do_request('BatchUnbindProjectProducts', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_unbind_project_products_with_options_async(
        self,
        request: iot_20180120_models.BatchUnbindProjectProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchUnbindProjectProductsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchUnbindProjectProductsResponse(),
            await self.do_request_async('BatchUnbindProjectProducts', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_unbind_project_products(
        self,
        request: iot_20180120_models.BatchUnbindProjectProductsRequest,
    ) -> iot_20180120_models.BatchUnbindProjectProductsResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_project_products_with_options(request, runtime)

    async def batch_unbind_project_products_async(
        self,
        request: iot_20180120_models.BatchUnbindProjectProductsRequest,
    ) -> iot_20180120_models.BatchUnbindProjectProductsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_unbind_project_products_with_options_async(request, runtime)

    def batch_update_device_nickname_with_options(
        self,
        request: iot_20180120_models.BatchUpdateDeviceNicknameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchUpdateDeviceNicknameResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchUpdateDeviceNicknameResponse(),
            self.do_request('BatchUpdateDeviceNickname', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def batch_update_device_nickname_with_options_async(
        self,
        request: iot_20180120_models.BatchUpdateDeviceNicknameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchUpdateDeviceNicknameResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchUpdateDeviceNicknameResponse(),
            await self.do_request_async('BatchUpdateDeviceNickname', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_update_device_nickname(
        self,
        request: iot_20180120_models.BatchUpdateDeviceNicknameRequest,
    ) -> iot_20180120_models.BatchUpdateDeviceNicknameResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_update_device_nickname_with_options(request, runtime)

    async def batch_update_device_nickname_async(
        self,
        request: iot_20180120_models.BatchUpdateDeviceNicknameRequest,
    ) -> iot_20180120_models.BatchUpdateDeviceNicknameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_update_device_nickname_with_options_async(request, runtime)

    def bind_application_to_edge_instance_with_options(
        self,
        request: iot_20180120_models.BindApplicationToEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BindApplicationToEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BindApplicationToEdgeInstanceResponse(),
            self.do_request('BindApplicationToEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def bind_application_to_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.BindApplicationToEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BindApplicationToEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BindApplicationToEdgeInstanceResponse(),
            await self.do_request_async('BindApplicationToEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def bind_application_to_edge_instance(
        self,
        request: iot_20180120_models.BindApplicationToEdgeInstanceRequest,
    ) -> iot_20180120_models.BindApplicationToEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_application_to_edge_instance_with_options(request, runtime)

    async def bind_application_to_edge_instance_async(
        self,
        request: iot_20180120_models.BindApplicationToEdgeInstanceRequest,
    ) -> iot_20180120_models.BindApplicationToEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_application_to_edge_instance_with_options_async(request, runtime)

    def bind_driver_to_edge_instance_with_options(
        self,
        request: iot_20180120_models.BindDriverToEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BindDriverToEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BindDriverToEdgeInstanceResponse(),
            self.do_request('BindDriverToEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def bind_driver_to_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.BindDriverToEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BindDriverToEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BindDriverToEdgeInstanceResponse(),
            await self.do_request_async('BindDriverToEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def bind_driver_to_edge_instance(
        self,
        request: iot_20180120_models.BindDriverToEdgeInstanceRequest,
    ) -> iot_20180120_models.BindDriverToEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_driver_to_edge_instance_with_options(request, runtime)

    async def bind_driver_to_edge_instance_async(
        self,
        request: iot_20180120_models.BindDriverToEdgeInstanceRequest,
    ) -> iot_20180120_models.BindDriverToEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_driver_to_edge_instance_with_options_async(request, runtime)

    def bind_gateway_to_edge_instance_with_options(
        self,
        request: iot_20180120_models.BindGatewayToEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BindGatewayToEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BindGatewayToEdgeInstanceResponse(),
            self.do_request('BindGatewayToEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def bind_gateway_to_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.BindGatewayToEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BindGatewayToEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BindGatewayToEdgeInstanceResponse(),
            await self.do_request_async('BindGatewayToEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def bind_gateway_to_edge_instance(
        self,
        request: iot_20180120_models.BindGatewayToEdgeInstanceRequest,
    ) -> iot_20180120_models.BindGatewayToEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_gateway_to_edge_instance_with_options(request, runtime)

    async def bind_gateway_to_edge_instance_async(
        self,
        request: iot_20180120_models.BindGatewayToEdgeInstanceRequest,
    ) -> iot_20180120_models.BindGatewayToEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_gateway_to_edge_instance_with_options_async(request, runtime)

    def bind_license_device_with_options(
        self,
        request: iot_20180120_models.BindLicenseDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BindLicenseDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BindLicenseDeviceResponse(),
            self.do_request('BindLicenseDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def bind_license_device_with_options_async(
        self,
        request: iot_20180120_models.BindLicenseDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BindLicenseDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BindLicenseDeviceResponse(),
            await self.do_request_async('BindLicenseDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def bind_license_device(
        self,
        request: iot_20180120_models.BindLicenseDeviceRequest,
    ) -> iot_20180120_models.BindLicenseDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_license_device_with_options(request, runtime)

    async def bind_license_device_async(
        self,
        request: iot_20180120_models.BindLicenseDeviceRequest,
    ) -> iot_20180120_models.BindLicenseDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_license_device_with_options_async(request, runtime)

    def bind_license_product_with_options(
        self,
        request: iot_20180120_models.BindLicenseProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BindLicenseProductResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BindLicenseProductResponse(),
            self.do_request('BindLicenseProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def bind_license_product_with_options_async(
        self,
        request: iot_20180120_models.BindLicenseProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BindLicenseProductResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BindLicenseProductResponse(),
            await self.do_request_async('BindLicenseProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def bind_license_product(
        self,
        request: iot_20180120_models.BindLicenseProductRequest,
    ) -> iot_20180120_models.BindLicenseProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_license_product_with_options(request, runtime)

    async def bind_license_product_async(
        self,
        request: iot_20180120_models.BindLicenseProductRequest,
    ) -> iot_20180120_models.BindLicenseProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_license_product_with_options_async(request, runtime)

    def bind_role_to_edge_instance_with_options(
        self,
        request: iot_20180120_models.BindRoleToEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BindRoleToEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BindRoleToEdgeInstanceResponse(),
            self.do_request('BindRoleToEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def bind_role_to_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.BindRoleToEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BindRoleToEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BindRoleToEdgeInstanceResponse(),
            await self.do_request_async('BindRoleToEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def bind_role_to_edge_instance(
        self,
        request: iot_20180120_models.BindRoleToEdgeInstanceRequest,
    ) -> iot_20180120_models.BindRoleToEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_role_to_edge_instance_with_options(request, runtime)

    async def bind_role_to_edge_instance_async(
        self,
        request: iot_20180120_models.BindRoleToEdgeInstanceRequest,
    ) -> iot_20180120_models.BindRoleToEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_role_to_edge_instance_with_options_async(request, runtime)

    def bind_scene_rule_to_edge_instance_with_options(
        self,
        request: iot_20180120_models.BindSceneRuleToEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BindSceneRuleToEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BindSceneRuleToEdgeInstanceResponse(),
            self.do_request('BindSceneRuleToEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def bind_scene_rule_to_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.BindSceneRuleToEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BindSceneRuleToEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BindSceneRuleToEdgeInstanceResponse(),
            await self.do_request_async('BindSceneRuleToEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def bind_scene_rule_to_edge_instance(
        self,
        request: iot_20180120_models.BindSceneRuleToEdgeInstanceRequest,
    ) -> iot_20180120_models.BindSceneRuleToEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_scene_rule_to_edge_instance_with_options(request, runtime)

    async def bind_scene_rule_to_edge_instance_async(
        self,
        request: iot_20180120_models.BindSceneRuleToEdgeInstanceRequest,
    ) -> iot_20180120_models.BindSceneRuleToEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_scene_rule_to_edge_instance_with_options_async(request, runtime)

    def cancel_job_with_options(
        self,
        request: iot_20180120_models.CancelJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CancelJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CancelJobResponse(),
            self.do_request('CancelJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def cancel_job_with_options_async(
        self,
        request: iot_20180120_models.CancelJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CancelJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CancelJobResponse(),
            await self.do_request_async('CancelJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def cancel_job(
        self,
        request: iot_20180120_models.CancelJobRequest,
    ) -> iot_20180120_models.CancelJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_job_with_options(request, runtime)

    async def cancel_job_async(
        self,
        request: iot_20180120_models.CancelJobRequest,
    ) -> iot_20180120_models.CancelJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_job_with_options_async(request, runtime)

    def cancel_otastrategy_by_job_with_options(
        self,
        request: iot_20180120_models.CancelOTAStrategyByJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CancelOTAStrategyByJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CancelOTAStrategyByJobResponse(),
            self.do_request('CancelOTAStrategyByJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def cancel_otastrategy_by_job_with_options_async(
        self,
        request: iot_20180120_models.CancelOTAStrategyByJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CancelOTAStrategyByJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CancelOTAStrategyByJobResponse(),
            await self.do_request_async('CancelOTAStrategyByJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def cancel_otastrategy_by_job(
        self,
        request: iot_20180120_models.CancelOTAStrategyByJobRequest,
    ) -> iot_20180120_models.CancelOTAStrategyByJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_otastrategy_by_job_with_options(request, runtime)

    async def cancel_otastrategy_by_job_async(
        self,
        request: iot_20180120_models.CancelOTAStrategyByJobRequest,
    ) -> iot_20180120_models.CancelOTAStrategyByJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_otastrategy_by_job_with_options_async(request, runtime)

    def cancel_otatask_by_device_with_options(
        self,
        request: iot_20180120_models.CancelOTATaskByDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CancelOTATaskByDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CancelOTATaskByDeviceResponse(),
            self.do_request('CancelOTATaskByDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def cancel_otatask_by_device_with_options_async(
        self,
        request: iot_20180120_models.CancelOTATaskByDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CancelOTATaskByDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CancelOTATaskByDeviceResponse(),
            await self.do_request_async('CancelOTATaskByDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def cancel_otatask_by_device(
        self,
        request: iot_20180120_models.CancelOTATaskByDeviceRequest,
    ) -> iot_20180120_models.CancelOTATaskByDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_otatask_by_device_with_options(request, runtime)

    async def cancel_otatask_by_device_async(
        self,
        request: iot_20180120_models.CancelOTATaskByDeviceRequest,
    ) -> iot_20180120_models.CancelOTATaskByDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_otatask_by_device_with_options_async(request, runtime)

    def cancel_otatask_by_job_with_options(
        self,
        request: iot_20180120_models.CancelOTATaskByJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CancelOTATaskByJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CancelOTATaskByJobResponse(),
            self.do_request('CancelOTATaskByJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def cancel_otatask_by_job_with_options_async(
        self,
        request: iot_20180120_models.CancelOTATaskByJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CancelOTATaskByJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CancelOTATaskByJobResponse(),
            await self.do_request_async('CancelOTATaskByJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def cancel_otatask_by_job(
        self,
        request: iot_20180120_models.CancelOTATaskByJobRequest,
    ) -> iot_20180120_models.CancelOTATaskByJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_otatask_by_job_with_options(request, runtime)

    async def cancel_otatask_by_job_async(
        self,
        request: iot_20180120_models.CancelOTATaskByJobRequest,
    ) -> iot_20180120_models.CancelOTATaskByJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_otatask_by_job_with_options_async(request, runtime)

    def cancel_release_product_with_options(
        self,
        request: iot_20180120_models.CancelReleaseProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CancelReleaseProductResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CancelReleaseProductResponse(),
            self.do_request('CancelReleaseProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def cancel_release_product_with_options_async(
        self,
        request: iot_20180120_models.CancelReleaseProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CancelReleaseProductResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CancelReleaseProductResponse(),
            await self.do_request_async('CancelReleaseProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def cancel_release_product(
        self,
        request: iot_20180120_models.CancelReleaseProductRequest,
    ) -> iot_20180120_models.CancelReleaseProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_release_product_with_options(request, runtime)

    async def cancel_release_product_async(
        self,
        request: iot_20180120_models.CancelReleaseProductRequest,
    ) -> iot_20180120_models.CancelReleaseProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_release_product_with_options_async(request, runtime)

    def check_bind_license_device_progress_with_options(
        self,
        request: iot_20180120_models.CheckBindLicenseDeviceProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CheckBindLicenseDeviceProgressResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CheckBindLicenseDeviceProgressResponse(),
            self.do_request('CheckBindLicenseDeviceProgress', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def check_bind_license_device_progress_with_options_async(
        self,
        request: iot_20180120_models.CheckBindLicenseDeviceProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CheckBindLicenseDeviceProgressResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CheckBindLicenseDeviceProgressResponse(),
            await self.do_request_async('CheckBindLicenseDeviceProgress', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def check_bind_license_device_progress(
        self,
        request: iot_20180120_models.CheckBindLicenseDeviceProgressRequest,
    ) -> iot_20180120_models.CheckBindLicenseDeviceProgressResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_bind_license_device_progress_with_options(request, runtime)

    async def check_bind_license_device_progress_async(
        self,
        request: iot_20180120_models.CheckBindLicenseDeviceProgressRequest,
    ) -> iot_20180120_models.CheckBindLicenseDeviceProgressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_bind_license_device_progress_with_options_async(request, runtime)

    def clear_device_desired_property_with_options(
        self,
        request: iot_20180120_models.ClearDeviceDesiredPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ClearDeviceDesiredPropertyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ClearDeviceDesiredPropertyResponse(),
            self.do_request('ClearDeviceDesiredProperty', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def clear_device_desired_property_with_options_async(
        self,
        request: iot_20180120_models.ClearDeviceDesiredPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ClearDeviceDesiredPropertyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ClearDeviceDesiredPropertyResponse(),
            await self.do_request_async('ClearDeviceDesiredProperty', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def clear_device_desired_property(
        self,
        request: iot_20180120_models.ClearDeviceDesiredPropertyRequest,
    ) -> iot_20180120_models.ClearDeviceDesiredPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return self.clear_device_desired_property_with_options(request, runtime)

    async def clear_device_desired_property_async(
        self,
        request: iot_20180120_models.ClearDeviceDesiredPropertyRequest,
    ) -> iot_20180120_models.ClearDeviceDesiredPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clear_device_desired_property_with_options_async(request, runtime)

    def clear_edge_instance_driver_configs_with_options(
        self,
        request: iot_20180120_models.ClearEdgeInstanceDriverConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ClearEdgeInstanceDriverConfigsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ClearEdgeInstanceDriverConfigsResponse(),
            self.do_request('ClearEdgeInstanceDriverConfigs', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def clear_edge_instance_driver_configs_with_options_async(
        self,
        request: iot_20180120_models.ClearEdgeInstanceDriverConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ClearEdgeInstanceDriverConfigsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ClearEdgeInstanceDriverConfigsResponse(),
            await self.do_request_async('ClearEdgeInstanceDriverConfigs', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def clear_edge_instance_driver_configs(
        self,
        request: iot_20180120_models.ClearEdgeInstanceDriverConfigsRequest,
    ) -> iot_20180120_models.ClearEdgeInstanceDriverConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.clear_edge_instance_driver_configs_with_options(request, runtime)

    async def clear_edge_instance_driver_configs_async(
        self,
        request: iot_20180120_models.ClearEdgeInstanceDriverConfigsRequest,
    ) -> iot_20180120_models.ClearEdgeInstanceDriverConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clear_edge_instance_driver_configs_with_options_async(request, runtime)

    def close_device_tunnel_with_options(
        self,
        request: iot_20180120_models.CloseDeviceTunnelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CloseDeviceTunnelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CloseDeviceTunnelResponse(),
            self.do_request('CloseDeviceTunnel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def close_device_tunnel_with_options_async(
        self,
        request: iot_20180120_models.CloseDeviceTunnelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CloseDeviceTunnelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CloseDeviceTunnelResponse(),
            await self.do_request_async('CloseDeviceTunnel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def close_device_tunnel(
        self,
        request: iot_20180120_models.CloseDeviceTunnelRequest,
    ) -> iot_20180120_models.CloseDeviceTunnelResponse:
        runtime = util_models.RuntimeOptions()
        return self.close_device_tunnel_with_options(request, runtime)

    async def close_device_tunnel_async(
        self,
        request: iot_20180120_models.CloseDeviceTunnelRequest,
    ) -> iot_20180120_models.CloseDeviceTunnelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.close_device_tunnel_with_options_async(request, runtime)

    def close_edge_instance_deployment_with_options(
        self,
        request: iot_20180120_models.CloseEdgeInstanceDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CloseEdgeInstanceDeploymentResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CloseEdgeInstanceDeploymentResponse(),
            self.do_request('CloseEdgeInstanceDeployment', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def close_edge_instance_deployment_with_options_async(
        self,
        request: iot_20180120_models.CloseEdgeInstanceDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CloseEdgeInstanceDeploymentResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CloseEdgeInstanceDeploymentResponse(),
            await self.do_request_async('CloseEdgeInstanceDeployment', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def close_edge_instance_deployment(
        self,
        request: iot_20180120_models.CloseEdgeInstanceDeploymentRequest,
    ) -> iot_20180120_models.CloseEdgeInstanceDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        return self.close_edge_instance_deployment_with_options(request, runtime)

    async def close_edge_instance_deployment_async(
        self,
        request: iot_20180120_models.CloseEdgeInstanceDeploymentRequest,
    ) -> iot_20180120_models.CloseEdgeInstanceDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.close_edge_instance_deployment_with_options_async(request, runtime)

    def confirm_otatask_with_options(
        self,
        request: iot_20180120_models.ConfirmOTATaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ConfirmOTATaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ConfirmOTATaskResponse(),
            self.do_request('ConfirmOTATask', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def confirm_otatask_with_options_async(
        self,
        request: iot_20180120_models.ConfirmOTATaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ConfirmOTATaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ConfirmOTATaskResponse(),
            await self.do_request_async('ConfirmOTATask', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def confirm_otatask(
        self,
        request: iot_20180120_models.ConfirmOTATaskRequest,
    ) -> iot_20180120_models.ConfirmOTATaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.confirm_otatask_with_options(request, runtime)

    async def confirm_otatask_async(
        self,
        request: iot_20180120_models.ConfirmOTATaskRequest,
    ) -> iot_20180120_models.ConfirmOTATaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.confirm_otatask_with_options_async(request, runtime)

    def copy_thing_model_with_options(
        self,
        request: iot_20180120_models.CopyThingModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CopyThingModelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CopyThingModelResponse(),
            self.do_request('CopyThingModel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def copy_thing_model_with_options_async(
        self,
        request: iot_20180120_models.CopyThingModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CopyThingModelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CopyThingModelResponse(),
            await self.do_request_async('CopyThingModel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def copy_thing_model(
        self,
        request: iot_20180120_models.CopyThingModelRequest,
    ) -> iot_20180120_models.CopyThingModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.copy_thing_model_with_options(request, runtime)

    async def copy_thing_model_async(
        self,
        request: iot_20180120_models.CopyThingModelRequest,
    ) -> iot_20180120_models.CopyThingModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.copy_thing_model_with_options_async(request, runtime)

    def count_speech_broadcast_hour_with_options(
        self,
        request: iot_20180120_models.CountSpeechBroadcastHourRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CountSpeechBroadcastHourResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CountSpeechBroadcastHourResponse(),
            self.do_request('CountSpeechBroadcastHour', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def count_speech_broadcast_hour_with_options_async(
        self,
        request: iot_20180120_models.CountSpeechBroadcastHourRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CountSpeechBroadcastHourResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CountSpeechBroadcastHourResponse(),
            await self.do_request_async('CountSpeechBroadcastHour', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def count_speech_broadcast_hour(
        self,
        request: iot_20180120_models.CountSpeechBroadcastHourRequest,
    ) -> iot_20180120_models.CountSpeechBroadcastHourResponse:
        runtime = util_models.RuntimeOptions()
        return self.count_speech_broadcast_hour_with_options(request, runtime)

    async def count_speech_broadcast_hour_async(
        self,
        request: iot_20180120_models.CountSpeechBroadcastHourRequest,
    ) -> iot_20180120_models.CountSpeechBroadcastHourResponse:
        runtime = util_models.RuntimeOptions()
        return await self.count_speech_broadcast_hour_with_options_async(request, runtime)

    def create_consumer_group_with_options(
        self,
        request: iot_20180120_models.CreateConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateConsumerGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateConsumerGroupResponse(),
            self.do_request('CreateConsumerGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_consumer_group_with_options_async(
        self,
        request: iot_20180120_models.CreateConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateConsumerGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateConsumerGroupResponse(),
            await self.do_request_async('CreateConsumerGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_consumer_group(
        self,
        request: iot_20180120_models.CreateConsumerGroupRequest,
    ) -> iot_20180120_models.CreateConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_consumer_group_with_options(request, runtime)

    async def create_consumer_group_async(
        self,
        request: iot_20180120_models.CreateConsumerGroupRequest,
    ) -> iot_20180120_models.CreateConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_consumer_group_with_options_async(request, runtime)

    def create_consumer_group_subscribe_relation_with_options(
        self,
        request: iot_20180120_models.CreateConsumerGroupSubscribeRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateConsumerGroupSubscribeRelationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateConsumerGroupSubscribeRelationResponse(),
            self.do_request('CreateConsumerGroupSubscribeRelation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_consumer_group_subscribe_relation_with_options_async(
        self,
        request: iot_20180120_models.CreateConsumerGroupSubscribeRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateConsumerGroupSubscribeRelationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateConsumerGroupSubscribeRelationResponse(),
            await self.do_request_async('CreateConsumerGroupSubscribeRelation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_consumer_group_subscribe_relation(
        self,
        request: iot_20180120_models.CreateConsumerGroupSubscribeRelationRequest,
    ) -> iot_20180120_models.CreateConsumerGroupSubscribeRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_consumer_group_subscribe_relation_with_options(request, runtime)

    async def create_consumer_group_subscribe_relation_async(
        self,
        request: iot_20180120_models.CreateConsumerGroupSubscribeRelationRequest,
    ) -> iot_20180120_models.CreateConsumerGroupSubscribeRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_consumer_group_subscribe_relation_with_options_async(request, runtime)

    def create_data_apiservice_with_options(
        self,
        request: iot_20180120_models.CreateDataAPIServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateDataAPIServiceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateDataAPIServiceResponse(),
            self.do_request('CreateDataAPIService', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_data_apiservice_with_options_async(
        self,
        request: iot_20180120_models.CreateDataAPIServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateDataAPIServiceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateDataAPIServiceResponse(),
            await self.do_request_async('CreateDataAPIService', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_data_apiservice(
        self,
        request: iot_20180120_models.CreateDataAPIServiceRequest,
    ) -> iot_20180120_models.CreateDataAPIServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_data_apiservice_with_options(request, runtime)

    async def create_data_apiservice_async(
        self,
        request: iot_20180120_models.CreateDataAPIServiceRequest,
    ) -> iot_20180120_models.CreateDataAPIServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_data_apiservice_with_options_async(request, runtime)

    def create_data_source_item_with_options(
        self,
        request: iot_20180120_models.CreateDataSourceItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateDataSourceItemResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateDataSourceItemResponse(),
            self.do_request('CreateDataSourceItem', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_data_source_item_with_options_async(
        self,
        request: iot_20180120_models.CreateDataSourceItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateDataSourceItemResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateDataSourceItemResponse(),
            await self.do_request_async('CreateDataSourceItem', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_data_source_item(
        self,
        request: iot_20180120_models.CreateDataSourceItemRequest,
    ) -> iot_20180120_models.CreateDataSourceItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_data_source_item_with_options(request, runtime)

    async def create_data_source_item_async(
        self,
        request: iot_20180120_models.CreateDataSourceItemRequest,
    ) -> iot_20180120_models.CreateDataSourceItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_data_source_item_with_options_async(request, runtime)

    def create_destination_with_options(
        self,
        request: iot_20180120_models.CreateDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateDestinationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateDestinationResponse(),
            self.do_request('CreateDestination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_destination_with_options_async(
        self,
        request: iot_20180120_models.CreateDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateDestinationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateDestinationResponse(),
            await self.do_request_async('CreateDestination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_destination(
        self,
        request: iot_20180120_models.CreateDestinationRequest,
    ) -> iot_20180120_models.CreateDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_destination_with_options(request, runtime)

    async def create_destination_async(
        self,
        request: iot_20180120_models.CreateDestinationRequest,
    ) -> iot_20180120_models.CreateDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_destination_with_options_async(request, runtime)

    def create_device_distribute_job_with_options(
        self,
        request: iot_20180120_models.CreateDeviceDistributeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateDeviceDistributeJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateDeviceDistributeJobResponse(),
            self.do_request('CreateDeviceDistributeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_device_distribute_job_with_options_async(
        self,
        request: iot_20180120_models.CreateDeviceDistributeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateDeviceDistributeJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateDeviceDistributeJobResponse(),
            await self.do_request_async('CreateDeviceDistributeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_device_distribute_job(
        self,
        request: iot_20180120_models.CreateDeviceDistributeJobRequest,
    ) -> iot_20180120_models.CreateDeviceDistributeJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_device_distribute_job_with_options(request, runtime)

    async def create_device_distribute_job_async(
        self,
        request: iot_20180120_models.CreateDeviceDistributeJobRequest,
    ) -> iot_20180120_models.CreateDeviceDistributeJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_device_distribute_job_with_options_async(request, runtime)

    def create_device_dynamic_group_with_options(
        self,
        request: iot_20180120_models.CreateDeviceDynamicGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateDeviceDynamicGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateDeviceDynamicGroupResponse(),
            self.do_request('CreateDeviceDynamicGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_device_dynamic_group_with_options_async(
        self,
        request: iot_20180120_models.CreateDeviceDynamicGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateDeviceDynamicGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateDeviceDynamicGroupResponse(),
            await self.do_request_async('CreateDeviceDynamicGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_device_dynamic_group(
        self,
        request: iot_20180120_models.CreateDeviceDynamicGroupRequest,
    ) -> iot_20180120_models.CreateDeviceDynamicGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_device_dynamic_group_with_options(request, runtime)

    async def create_device_dynamic_group_async(
        self,
        request: iot_20180120_models.CreateDeviceDynamicGroupRequest,
    ) -> iot_20180120_models.CreateDeviceDynamicGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_device_dynamic_group_with_options_async(request, runtime)

    def create_device_group_with_options(
        self,
        request: iot_20180120_models.CreateDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateDeviceGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateDeviceGroupResponse(),
            self.do_request('CreateDeviceGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_device_group_with_options_async(
        self,
        request: iot_20180120_models.CreateDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateDeviceGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateDeviceGroupResponse(),
            await self.do_request_async('CreateDeviceGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_device_group(
        self,
        request: iot_20180120_models.CreateDeviceGroupRequest,
    ) -> iot_20180120_models.CreateDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_device_group_with_options(request, runtime)

    async def create_device_group_async(
        self,
        request: iot_20180120_models.CreateDeviceGroupRequest,
    ) -> iot_20180120_models.CreateDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_device_group_with_options_async(request, runtime)

    def create_device_tunnel_with_options(
        self,
        request: iot_20180120_models.CreateDeviceTunnelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateDeviceTunnelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateDeviceTunnelResponse(),
            self.do_request('CreateDeviceTunnel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_device_tunnel_with_options_async(
        self,
        request: iot_20180120_models.CreateDeviceTunnelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateDeviceTunnelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateDeviceTunnelResponse(),
            await self.do_request_async('CreateDeviceTunnel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_device_tunnel(
        self,
        request: iot_20180120_models.CreateDeviceTunnelRequest,
    ) -> iot_20180120_models.CreateDeviceTunnelResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_device_tunnel_with_options(request, runtime)

    async def create_device_tunnel_async(
        self,
        request: iot_20180120_models.CreateDeviceTunnelRequest,
    ) -> iot_20180120_models.CreateDeviceTunnelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_device_tunnel_with_options_async(request, runtime)

    def create_download_data_job_with_options(
        self,
        tmp: iot_20180120_models.CreateDownloadDataJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateDownloadDataJobResponse:
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.CreateDownloadDataJobShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.context):
            request.context_shrink = UtilClient.to_jsonstring(tmp.context)
        if not UtilClient.is_unset(tmp.file_config):
            request.file_config_shrink = UtilClient.to_jsonstring(tmp.file_config)
        return TeaCore.from_map(
            iot_20180120_models.CreateDownloadDataJobResponse(),
            self.do_request('CreateDownloadDataJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_download_data_job_with_options_async(
        self,
        tmp: iot_20180120_models.CreateDownloadDataJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateDownloadDataJobResponse:
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.CreateDownloadDataJobShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.context):
            request.context_shrink = UtilClient.to_jsonstring(tmp.context)
        if not UtilClient.is_unset(tmp.file_config):
            request.file_config_shrink = UtilClient.to_jsonstring(tmp.file_config)
        return TeaCore.from_map(
            iot_20180120_models.CreateDownloadDataJobResponse(),
            await self.do_request_async('CreateDownloadDataJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_download_data_job(
        self,
        request: iot_20180120_models.CreateDownloadDataJobRequest,
    ) -> iot_20180120_models.CreateDownloadDataJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_download_data_job_with_options(request, runtime)

    async def create_download_data_job_async(
        self,
        request: iot_20180120_models.CreateDownloadDataJobRequest,
    ) -> iot_20180120_models.CreateDownloadDataJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_download_data_job_with_options_async(request, runtime)

    def create_edge_driver_with_options(
        self,
        request: iot_20180120_models.CreateEdgeDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateEdgeDriverResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeDriverResponse(),
            self.do_request('CreateEdgeDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_edge_driver_with_options_async(
        self,
        request: iot_20180120_models.CreateEdgeDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateEdgeDriverResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeDriverResponse(),
            await self.do_request_async('CreateEdgeDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_edge_driver(
        self,
        request: iot_20180120_models.CreateEdgeDriverRequest,
    ) -> iot_20180120_models.CreateEdgeDriverResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_edge_driver_with_options(request, runtime)

    async def create_edge_driver_async(
        self,
        request: iot_20180120_models.CreateEdgeDriverRequest,
    ) -> iot_20180120_models.CreateEdgeDriverResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_edge_driver_with_options_async(request, runtime)

    def create_edge_driver_version_with_options(
        self,
        request: iot_20180120_models.CreateEdgeDriverVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateEdgeDriverVersionResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeDriverVersionResponse(),
            self.do_request('CreateEdgeDriverVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_edge_driver_version_with_options_async(
        self,
        request: iot_20180120_models.CreateEdgeDriverVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateEdgeDriverVersionResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeDriverVersionResponse(),
            await self.do_request_async('CreateEdgeDriverVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_edge_driver_version(
        self,
        request: iot_20180120_models.CreateEdgeDriverVersionRequest,
    ) -> iot_20180120_models.CreateEdgeDriverVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_edge_driver_version_with_options(request, runtime)

    async def create_edge_driver_version_async(
        self,
        request: iot_20180120_models.CreateEdgeDriverVersionRequest,
    ) -> iot_20180120_models.CreateEdgeDriverVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_edge_driver_version_with_options_async(request, runtime)

    def create_edge_instance_with_options(
        self,
        request: iot_20180120_models.CreateEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeInstanceResponse(),
            self.do_request('CreateEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.CreateEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeInstanceResponse(),
            await self.do_request_async('CreateEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_edge_instance(
        self,
        request: iot_20180120_models.CreateEdgeInstanceRequest,
    ) -> iot_20180120_models.CreateEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_edge_instance_with_options(request, runtime)

    async def create_edge_instance_async(
        self,
        request: iot_20180120_models.CreateEdgeInstanceRequest,
    ) -> iot_20180120_models.CreateEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_edge_instance_with_options_async(request, runtime)

    def create_edge_instance_channel_with_options(
        self,
        request: iot_20180120_models.CreateEdgeInstanceChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateEdgeInstanceChannelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeInstanceChannelResponse(),
            self.do_request('CreateEdgeInstanceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_edge_instance_channel_with_options_async(
        self,
        request: iot_20180120_models.CreateEdgeInstanceChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateEdgeInstanceChannelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeInstanceChannelResponse(),
            await self.do_request_async('CreateEdgeInstanceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_edge_instance_channel(
        self,
        request: iot_20180120_models.CreateEdgeInstanceChannelRequest,
    ) -> iot_20180120_models.CreateEdgeInstanceChannelResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_edge_instance_channel_with_options(request, runtime)

    async def create_edge_instance_channel_async(
        self,
        request: iot_20180120_models.CreateEdgeInstanceChannelRequest,
    ) -> iot_20180120_models.CreateEdgeInstanceChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_edge_instance_channel_with_options_async(request, runtime)

    def create_edge_instance_deployment_with_options(
        self,
        request: iot_20180120_models.CreateEdgeInstanceDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateEdgeInstanceDeploymentResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeInstanceDeploymentResponse(),
            self.do_request('CreateEdgeInstanceDeployment', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_edge_instance_deployment_with_options_async(
        self,
        request: iot_20180120_models.CreateEdgeInstanceDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateEdgeInstanceDeploymentResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeInstanceDeploymentResponse(),
            await self.do_request_async('CreateEdgeInstanceDeployment', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_edge_instance_deployment(
        self,
        request: iot_20180120_models.CreateEdgeInstanceDeploymentRequest,
    ) -> iot_20180120_models.CreateEdgeInstanceDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_edge_instance_deployment_with_options(request, runtime)

    async def create_edge_instance_deployment_async(
        self,
        request: iot_20180120_models.CreateEdgeInstanceDeploymentRequest,
    ) -> iot_20180120_models.CreateEdgeInstanceDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_edge_instance_deployment_with_options_async(request, runtime)

    def create_edge_instance_message_routing_with_options(
        self,
        request: iot_20180120_models.CreateEdgeInstanceMessageRoutingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateEdgeInstanceMessageRoutingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeInstanceMessageRoutingResponse(),
            self.do_request('CreateEdgeInstanceMessageRouting', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_edge_instance_message_routing_with_options_async(
        self,
        request: iot_20180120_models.CreateEdgeInstanceMessageRoutingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateEdgeInstanceMessageRoutingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeInstanceMessageRoutingResponse(),
            await self.do_request_async('CreateEdgeInstanceMessageRouting', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_edge_instance_message_routing(
        self,
        request: iot_20180120_models.CreateEdgeInstanceMessageRoutingRequest,
    ) -> iot_20180120_models.CreateEdgeInstanceMessageRoutingResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_edge_instance_message_routing_with_options(request, runtime)

    async def create_edge_instance_message_routing_async(
        self,
        request: iot_20180120_models.CreateEdgeInstanceMessageRoutingRequest,
    ) -> iot_20180120_models.CreateEdgeInstanceMessageRoutingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_edge_instance_message_routing_with_options_async(request, runtime)

    def create_edge_oss_pre_signed_address_with_options(
        self,
        request: iot_20180120_models.CreateEdgeOssPreSignedAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateEdgeOssPreSignedAddressResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeOssPreSignedAddressResponse(),
            self.do_request('CreateEdgeOssPreSignedAddress', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_edge_oss_pre_signed_address_with_options_async(
        self,
        request: iot_20180120_models.CreateEdgeOssPreSignedAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateEdgeOssPreSignedAddressResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeOssPreSignedAddressResponse(),
            await self.do_request_async('CreateEdgeOssPreSignedAddress', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_edge_oss_pre_signed_address(
        self,
        request: iot_20180120_models.CreateEdgeOssPreSignedAddressRequest,
    ) -> iot_20180120_models.CreateEdgeOssPreSignedAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_edge_oss_pre_signed_address_with_options(request, runtime)

    async def create_edge_oss_pre_signed_address_async(
        self,
        request: iot_20180120_models.CreateEdgeOssPreSignedAddressRequest,
    ) -> iot_20180120_models.CreateEdgeOssPreSignedAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_edge_oss_pre_signed_address_with_options_async(request, runtime)

    def create_job_with_options(
        self,
        tmp: iot_20180120_models.CreateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateJobResponse:
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.CreateJobShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.job_file):
            request.job_file_shrink = UtilClient.to_jsonstring(tmp.job_file)
        if not UtilClient.is_unset(tmp.rollout_config):
            request.rollout_config_shrink = UtilClient.to_jsonstring(tmp.rollout_config)
        if not UtilClient.is_unset(tmp.target_config):
            request.target_config_shrink = UtilClient.to_jsonstring(tmp.target_config)
        if not UtilClient.is_unset(tmp.timeout_config):
            request.timeout_config_shrink = UtilClient.to_jsonstring(tmp.timeout_config)
        return TeaCore.from_map(
            iot_20180120_models.CreateJobResponse(),
            self.do_request('CreateJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_job_with_options_async(
        self,
        tmp: iot_20180120_models.CreateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateJobResponse:
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.CreateJobShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.job_file):
            request.job_file_shrink = UtilClient.to_jsonstring(tmp.job_file)
        if not UtilClient.is_unset(tmp.rollout_config):
            request.rollout_config_shrink = UtilClient.to_jsonstring(tmp.rollout_config)
        if not UtilClient.is_unset(tmp.target_config):
            request.target_config_shrink = UtilClient.to_jsonstring(tmp.target_config)
        if not UtilClient.is_unset(tmp.timeout_config):
            request.timeout_config_shrink = UtilClient.to_jsonstring(tmp.timeout_config)
        return TeaCore.from_map(
            iot_20180120_models.CreateJobResponse(),
            await self.do_request_async('CreateJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_job(
        self,
        request: iot_20180120_models.CreateJobRequest,
    ) -> iot_20180120_models.CreateJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_job_with_options(request, runtime)

    async def create_job_async(
        self,
        request: iot_20180120_models.CreateJobRequest,
    ) -> iot_20180120_models.CreateJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_job_with_options_async(request, runtime)

    def create_lo_ra_nodes_task_with_options(
        self,
        request: iot_20180120_models.CreateLoRaNodesTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateLoRaNodesTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateLoRaNodesTaskResponse(),
            self.do_request('CreateLoRaNodesTask', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_lo_ra_nodes_task_with_options_async(
        self,
        request: iot_20180120_models.CreateLoRaNodesTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateLoRaNodesTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateLoRaNodesTaskResponse(),
            await self.do_request_async('CreateLoRaNodesTask', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_lo_ra_nodes_task(
        self,
        request: iot_20180120_models.CreateLoRaNodesTaskRequest,
    ) -> iot_20180120_models.CreateLoRaNodesTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_lo_ra_nodes_task_with_options(request, runtime)

    async def create_lo_ra_nodes_task_async(
        self,
        request: iot_20180120_models.CreateLoRaNodesTaskRequest,
    ) -> iot_20180120_models.CreateLoRaNodesTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_lo_ra_nodes_task_with_options_async(request, runtime)

    def create_otadynamic_upgrade_job_with_options(
        self,
        request: iot_20180120_models.CreateOTADynamicUpgradeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateOTADynamicUpgradeJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateOTADynamicUpgradeJobResponse(),
            self.do_request('CreateOTADynamicUpgradeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_otadynamic_upgrade_job_with_options_async(
        self,
        request: iot_20180120_models.CreateOTADynamicUpgradeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateOTADynamicUpgradeJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateOTADynamicUpgradeJobResponse(),
            await self.do_request_async('CreateOTADynamicUpgradeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_otadynamic_upgrade_job(
        self,
        request: iot_20180120_models.CreateOTADynamicUpgradeJobRequest,
    ) -> iot_20180120_models.CreateOTADynamicUpgradeJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_otadynamic_upgrade_job_with_options(request, runtime)

    async def create_otadynamic_upgrade_job_async(
        self,
        request: iot_20180120_models.CreateOTADynamicUpgradeJobRequest,
    ) -> iot_20180120_models.CreateOTADynamicUpgradeJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_otadynamic_upgrade_job_with_options_async(request, runtime)

    def create_otafirmware_with_options(
        self,
        request: iot_20180120_models.CreateOTAFirmwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateOTAFirmwareResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateOTAFirmwareResponse(),
            self.do_request('CreateOTAFirmware', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_otafirmware_with_options_async(
        self,
        request: iot_20180120_models.CreateOTAFirmwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateOTAFirmwareResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateOTAFirmwareResponse(),
            await self.do_request_async('CreateOTAFirmware', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_otafirmware(
        self,
        request: iot_20180120_models.CreateOTAFirmwareRequest,
    ) -> iot_20180120_models.CreateOTAFirmwareResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_otafirmware_with_options(request, runtime)

    async def create_otafirmware_async(
        self,
        request: iot_20180120_models.CreateOTAFirmwareRequest,
    ) -> iot_20180120_models.CreateOTAFirmwareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_otafirmware_with_options_async(request, runtime)

    def create_otamodule_with_options(
        self,
        request: iot_20180120_models.CreateOTAModuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateOTAModuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateOTAModuleResponse(),
            self.do_request('CreateOTAModule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_otamodule_with_options_async(
        self,
        request: iot_20180120_models.CreateOTAModuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateOTAModuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateOTAModuleResponse(),
            await self.do_request_async('CreateOTAModule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_otamodule(
        self,
        request: iot_20180120_models.CreateOTAModuleRequest,
    ) -> iot_20180120_models.CreateOTAModuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_otamodule_with_options(request, runtime)

    async def create_otamodule_async(
        self,
        request: iot_20180120_models.CreateOTAModuleRequest,
    ) -> iot_20180120_models.CreateOTAModuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_otamodule_with_options_async(request, runtime)

    def create_otastatic_upgrade_job_with_options(
        self,
        request: iot_20180120_models.CreateOTAStaticUpgradeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateOTAStaticUpgradeJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateOTAStaticUpgradeJobResponse(),
            self.do_request('CreateOTAStaticUpgradeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_otastatic_upgrade_job_with_options_async(
        self,
        request: iot_20180120_models.CreateOTAStaticUpgradeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateOTAStaticUpgradeJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateOTAStaticUpgradeJobResponse(),
            await self.do_request_async('CreateOTAStaticUpgradeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_otastatic_upgrade_job(
        self,
        request: iot_20180120_models.CreateOTAStaticUpgradeJobRequest,
    ) -> iot_20180120_models.CreateOTAStaticUpgradeJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_otastatic_upgrade_job_with_options(request, runtime)

    async def create_otastatic_upgrade_job_async(
        self,
        request: iot_20180120_models.CreateOTAStaticUpgradeJobRequest,
    ) -> iot_20180120_models.CreateOTAStaticUpgradeJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_otastatic_upgrade_job_with_options_async(request, runtime)

    def create_otaverify_job_with_options(
        self,
        request: iot_20180120_models.CreateOTAVerifyJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateOTAVerifyJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateOTAVerifyJobResponse(),
            self.do_request('CreateOTAVerifyJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_otaverify_job_with_options_async(
        self,
        request: iot_20180120_models.CreateOTAVerifyJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateOTAVerifyJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateOTAVerifyJobResponse(),
            await self.do_request_async('CreateOTAVerifyJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_otaverify_job(
        self,
        request: iot_20180120_models.CreateOTAVerifyJobRequest,
    ) -> iot_20180120_models.CreateOTAVerifyJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_otaverify_job_with_options(request, runtime)

    async def create_otaverify_job_async(
        self,
        request: iot_20180120_models.CreateOTAVerifyJobRequest,
    ) -> iot_20180120_models.CreateOTAVerifyJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_otaverify_job_with_options_async(request, runtime)

    def create_parser_with_options(
        self,
        request: iot_20180120_models.CreateParserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateParserResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateParserResponse(),
            self.do_request('CreateParser', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_parser_with_options_async(
        self,
        request: iot_20180120_models.CreateParserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateParserResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateParserResponse(),
            await self.do_request_async('CreateParser', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_parser(
        self,
        request: iot_20180120_models.CreateParserRequest,
    ) -> iot_20180120_models.CreateParserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_parser_with_options(request, runtime)

    async def create_parser_async(
        self,
        request: iot_20180120_models.CreateParserRequest,
    ) -> iot_20180120_models.CreateParserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_parser_with_options_async(request, runtime)

    def create_parser_data_source_with_options(
        self,
        request: iot_20180120_models.CreateParserDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateParserDataSourceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateParserDataSourceResponse(),
            self.do_request('CreateParserDataSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_parser_data_source_with_options_async(
        self,
        request: iot_20180120_models.CreateParserDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateParserDataSourceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateParserDataSourceResponse(),
            await self.do_request_async('CreateParserDataSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_parser_data_source(
        self,
        request: iot_20180120_models.CreateParserDataSourceRequest,
    ) -> iot_20180120_models.CreateParserDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_parser_data_source_with_options(request, runtime)

    async def create_parser_data_source_async(
        self,
        request: iot_20180120_models.CreateParserDataSourceRequest,
    ) -> iot_20180120_models.CreateParserDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_parser_data_source_with_options_async(request, runtime)

    def create_product_with_options(
        self,
        request: iot_20180120_models.CreateProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateProductResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateProductResponse(),
            self.do_request('CreateProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_product_with_options_async(
        self,
        request: iot_20180120_models.CreateProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateProductResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateProductResponse(),
            await self.do_request_async('CreateProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_product(
        self,
        request: iot_20180120_models.CreateProductRequest,
    ) -> iot_20180120_models.CreateProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_product_with_options(request, runtime)

    async def create_product_async(
        self,
        request: iot_20180120_models.CreateProductRequest,
    ) -> iot_20180120_models.CreateProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_product_with_options_async(request, runtime)

    def create_product_distribute_job_with_options(
        self,
        request: iot_20180120_models.CreateProductDistributeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateProductDistributeJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateProductDistributeJobResponse(),
            self.do_request('CreateProductDistributeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_product_distribute_job_with_options_async(
        self,
        request: iot_20180120_models.CreateProductDistributeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateProductDistributeJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateProductDistributeJobResponse(),
            await self.do_request_async('CreateProductDistributeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_product_distribute_job(
        self,
        request: iot_20180120_models.CreateProductDistributeJobRequest,
    ) -> iot_20180120_models.CreateProductDistributeJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_product_distribute_job_with_options(request, runtime)

    async def create_product_distribute_job_async(
        self,
        request: iot_20180120_models.CreateProductDistributeJobRequest,
    ) -> iot_20180120_models.CreateProductDistributeJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_product_distribute_job_with_options_async(request, runtime)

    def create_product_tags_with_options(
        self,
        request: iot_20180120_models.CreateProductTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateProductTagsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateProductTagsResponse(),
            self.do_request('CreateProductTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_product_tags_with_options_async(
        self,
        request: iot_20180120_models.CreateProductTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateProductTagsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateProductTagsResponse(),
            await self.do_request_async('CreateProductTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_product_tags(
        self,
        request: iot_20180120_models.CreateProductTagsRequest,
    ) -> iot_20180120_models.CreateProductTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_product_tags_with_options(request, runtime)

    async def create_product_tags_async(
        self,
        request: iot_20180120_models.CreateProductTagsRequest,
    ) -> iot_20180120_models.CreateProductTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_product_tags_with_options_async(request, runtime)

    def create_product_topic_with_options(
        self,
        request: iot_20180120_models.CreateProductTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateProductTopicResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateProductTopicResponse(),
            self.do_request('CreateProductTopic', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_product_topic_with_options_async(
        self,
        request: iot_20180120_models.CreateProductTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateProductTopicResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateProductTopicResponse(),
            await self.do_request_async('CreateProductTopic', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_product_topic(
        self,
        request: iot_20180120_models.CreateProductTopicRequest,
    ) -> iot_20180120_models.CreateProductTopicResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_product_topic_with_options(request, runtime)

    async def create_product_topic_async(
        self,
        request: iot_20180120_models.CreateProductTopicRequest,
    ) -> iot_20180120_models.CreateProductTopicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_product_topic_with_options_async(request, runtime)

    def create_rule_with_options(
        self,
        request: iot_20180120_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateRuleResponse(),
            self.do_request('CreateRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_rule_with_options_async(
        self,
        request: iot_20180120_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateRuleResponse(),
            await self.do_request_async('CreateRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_rule(
        self,
        request: iot_20180120_models.CreateRuleRequest,
    ) -> iot_20180120_models.CreateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_rule_with_options(request, runtime)

    async def create_rule_async(
        self,
        request: iot_20180120_models.CreateRuleRequest,
    ) -> iot_20180120_models.CreateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_rule_with_options_async(request, runtime)

    def create_rule_action_with_options(
        self,
        request: iot_20180120_models.CreateRuleActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateRuleActionResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateRuleActionResponse(),
            self.do_request('CreateRuleAction', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_rule_action_with_options_async(
        self,
        request: iot_20180120_models.CreateRuleActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateRuleActionResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateRuleActionResponse(),
            await self.do_request_async('CreateRuleAction', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_rule_action(
        self,
        request: iot_20180120_models.CreateRuleActionRequest,
    ) -> iot_20180120_models.CreateRuleActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_rule_action_with_options(request, runtime)

    async def create_rule_action_async(
        self,
        request: iot_20180120_models.CreateRuleActionRequest,
    ) -> iot_20180120_models.CreateRuleActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_rule_action_with_options_async(request, runtime)

    def create_scene_rule_with_options(
        self,
        request: iot_20180120_models.CreateSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateSceneRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateSceneRuleResponse(),
            self.do_request('CreateSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_scene_rule_with_options_async(
        self,
        request: iot_20180120_models.CreateSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateSceneRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateSceneRuleResponse(),
            await self.do_request_async('CreateSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_scene_rule(
        self,
        request: iot_20180120_models.CreateSceneRuleRequest,
    ) -> iot_20180120_models.CreateSceneRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_scene_rule_with_options(request, runtime)

    async def create_scene_rule_async(
        self,
        request: iot_20180120_models.CreateSceneRuleRequest,
    ) -> iot_20180120_models.CreateSceneRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_scene_rule_with_options_async(request, runtime)

    def create_schedule_period_with_options(
        self,
        request: iot_20180120_models.CreateSchedulePeriodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateSchedulePeriodResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateSchedulePeriodResponse(),
            self.do_request('CreateSchedulePeriod', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_schedule_period_with_options_async(
        self,
        request: iot_20180120_models.CreateSchedulePeriodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateSchedulePeriodResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateSchedulePeriodResponse(),
            await self.do_request_async('CreateSchedulePeriod', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_schedule_period(
        self,
        request: iot_20180120_models.CreateSchedulePeriodRequest,
    ) -> iot_20180120_models.CreateSchedulePeriodResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_schedule_period_with_options(request, runtime)

    async def create_schedule_period_async(
        self,
        request: iot_20180120_models.CreateSchedulePeriodRequest,
    ) -> iot_20180120_models.CreateSchedulePeriodResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_schedule_period_with_options_async(request, runtime)

    def create_sound_code_with_options(
        self,
        request: iot_20180120_models.CreateSoundCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateSoundCodeResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateSoundCodeResponse(),
            self.do_request('CreateSoundCode', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_sound_code_with_options_async(
        self,
        request: iot_20180120_models.CreateSoundCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateSoundCodeResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateSoundCodeResponse(),
            await self.do_request_async('CreateSoundCode', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_sound_code(
        self,
        request: iot_20180120_models.CreateSoundCodeRequest,
    ) -> iot_20180120_models.CreateSoundCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_sound_code_with_options(request, runtime)

    async def create_sound_code_async(
        self,
        request: iot_20180120_models.CreateSoundCodeRequest,
    ) -> iot_20180120_models.CreateSoundCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_sound_code_with_options_async(request, runtime)

    def create_sound_code_label_with_options(
        self,
        request: iot_20180120_models.CreateSoundCodeLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateSoundCodeLabelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateSoundCodeLabelResponse(),
            self.do_request('CreateSoundCodeLabel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_sound_code_label_with_options_async(
        self,
        request: iot_20180120_models.CreateSoundCodeLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateSoundCodeLabelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateSoundCodeLabelResponse(),
            await self.do_request_async('CreateSoundCodeLabel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_sound_code_label(
        self,
        request: iot_20180120_models.CreateSoundCodeLabelRequest,
    ) -> iot_20180120_models.CreateSoundCodeLabelResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_sound_code_label_with_options(request, runtime)

    async def create_sound_code_label_async(
        self,
        request: iot_20180120_models.CreateSoundCodeLabelRequest,
    ) -> iot_20180120_models.CreateSoundCodeLabelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_sound_code_label_with_options_async(request, runtime)

    def create_sound_code_schedule_with_options(
        self,
        request: iot_20180120_models.CreateSoundCodeScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateSoundCodeScheduleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateSoundCodeScheduleResponse(),
            self.do_request('CreateSoundCodeSchedule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_sound_code_schedule_with_options_async(
        self,
        request: iot_20180120_models.CreateSoundCodeScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateSoundCodeScheduleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateSoundCodeScheduleResponse(),
            await self.do_request_async('CreateSoundCodeSchedule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_sound_code_schedule(
        self,
        request: iot_20180120_models.CreateSoundCodeScheduleRequest,
    ) -> iot_20180120_models.CreateSoundCodeScheduleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_sound_code_schedule_with_options(request, runtime)

    async def create_sound_code_schedule_async(
        self,
        request: iot_20180120_models.CreateSoundCodeScheduleRequest,
    ) -> iot_20180120_models.CreateSoundCodeScheduleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_sound_code_schedule_with_options_async(request, runtime)

    def create_speech_with_options(
        self,
        tmp: iot_20180120_models.CreateSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateSpeechResponse:
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.CreateSpeechShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.sound_code_config):
            request.sound_code_config_shrink = UtilClient.to_jsonstring(tmp.sound_code_config)
        return TeaCore.from_map(
            iot_20180120_models.CreateSpeechResponse(),
            self.do_request('CreateSpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_speech_with_options_async(
        self,
        tmp: iot_20180120_models.CreateSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateSpeechResponse:
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.CreateSpeechShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.sound_code_config):
            request.sound_code_config_shrink = UtilClient.to_jsonstring(tmp.sound_code_config)
        return TeaCore.from_map(
            iot_20180120_models.CreateSpeechResponse(),
            await self.do_request_async('CreateSpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_speech(
        self,
        request: iot_20180120_models.CreateSpeechRequest,
    ) -> iot_20180120_models.CreateSpeechResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_speech_with_options(request, runtime)

    async def create_speech_async(
        self,
        request: iot_20180120_models.CreateSpeechRequest,
    ) -> iot_20180120_models.CreateSpeechResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_speech_with_options_async(request, runtime)

    def create_studio_app_domain_open_with_options(
        self,
        request: iot_20180120_models.CreateStudioAppDomainOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateStudioAppDomainOpenResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateStudioAppDomainOpenResponse(),
            self.do_request('CreateStudioAppDomainOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_studio_app_domain_open_with_options_async(
        self,
        request: iot_20180120_models.CreateStudioAppDomainOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateStudioAppDomainOpenResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateStudioAppDomainOpenResponse(),
            await self.do_request_async('CreateStudioAppDomainOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_studio_app_domain_open(
        self,
        request: iot_20180120_models.CreateStudioAppDomainOpenRequest,
    ) -> iot_20180120_models.CreateStudioAppDomainOpenResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_studio_app_domain_open_with_options(request, runtime)

    async def create_studio_app_domain_open_async(
        self,
        request: iot_20180120_models.CreateStudioAppDomainOpenRequest,
    ) -> iot_20180120_models.CreateStudioAppDomainOpenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_studio_app_domain_open_with_options_async(request, runtime)

    def create_subscribe_relation_with_options(
        self,
        request: iot_20180120_models.CreateSubscribeRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateSubscribeRelationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateSubscribeRelationResponse(),
            self.do_request('CreateSubscribeRelation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_subscribe_relation_with_options_async(
        self,
        request: iot_20180120_models.CreateSubscribeRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateSubscribeRelationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateSubscribeRelationResponse(),
            await self.do_request_async('CreateSubscribeRelation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_subscribe_relation(
        self,
        request: iot_20180120_models.CreateSubscribeRelationRequest,
    ) -> iot_20180120_models.CreateSubscribeRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_subscribe_relation_with_options(request, runtime)

    async def create_subscribe_relation_async(
        self,
        request: iot_20180120_models.CreateSubscribeRelationRequest,
    ) -> iot_20180120_models.CreateSubscribeRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_subscribe_relation_with_options_async(request, runtime)

    def create_thing_model_with_options(
        self,
        request: iot_20180120_models.CreateThingModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateThingModelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateThingModelResponse(),
            self.do_request('CreateThingModel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_thing_model_with_options_async(
        self,
        request: iot_20180120_models.CreateThingModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateThingModelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateThingModelResponse(),
            await self.do_request_async('CreateThingModel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_thing_model(
        self,
        request: iot_20180120_models.CreateThingModelRequest,
    ) -> iot_20180120_models.CreateThingModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_thing_model_with_options(request, runtime)

    async def create_thing_model_async(
        self,
        request: iot_20180120_models.CreateThingModelRequest,
    ) -> iot_20180120_models.CreateThingModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_thing_model_with_options_async(request, runtime)

    def create_thing_script_with_options(
        self,
        request: iot_20180120_models.CreateThingScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateThingScriptResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateThingScriptResponse(),
            self.do_request('CreateThingScript', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_thing_script_with_options_async(
        self,
        request: iot_20180120_models.CreateThingScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateThingScriptResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateThingScriptResponse(),
            await self.do_request_async('CreateThingScript', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_thing_script(
        self,
        request: iot_20180120_models.CreateThingScriptRequest,
    ) -> iot_20180120_models.CreateThingScriptResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_thing_script_with_options(request, runtime)

    async def create_thing_script_async(
        self,
        request: iot_20180120_models.CreateThingScriptRequest,
    ) -> iot_20180120_models.CreateThingScriptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_thing_script_with_options_async(request, runtime)

    def create_topic_route_table_with_options(
        self,
        request: iot_20180120_models.CreateTopicRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateTopicRouteTableResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateTopicRouteTableResponse(),
            self.do_request('CreateTopicRouteTable', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_topic_route_table_with_options_async(
        self,
        request: iot_20180120_models.CreateTopicRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateTopicRouteTableResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateTopicRouteTableResponse(),
            await self.do_request_async('CreateTopicRouteTable', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_topic_route_table(
        self,
        request: iot_20180120_models.CreateTopicRouteTableRequest,
    ) -> iot_20180120_models.CreateTopicRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_topic_route_table_with_options(request, runtime)

    async def create_topic_route_table_async(
        self,
        request: iot_20180120_models.CreateTopicRouteTableRequest,
    ) -> iot_20180120_models.CreateTopicRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_topic_route_table_with_options_async(request, runtime)

    def delete_client_ids_with_options(
        self,
        request: iot_20180120_models.DeleteClientIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteClientIdsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteClientIdsResponse(),
            self.do_request('DeleteClientIds', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_client_ids_with_options_async(
        self,
        request: iot_20180120_models.DeleteClientIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteClientIdsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteClientIdsResponse(),
            await self.do_request_async('DeleteClientIds', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_client_ids(
        self,
        request: iot_20180120_models.DeleteClientIdsRequest,
    ) -> iot_20180120_models.DeleteClientIdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_client_ids_with_options(request, runtime)

    async def delete_client_ids_async(
        self,
        request: iot_20180120_models.DeleteClientIdsRequest,
    ) -> iot_20180120_models.DeleteClientIdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_client_ids_with_options_async(request, runtime)

    def delete_consumer_group_with_options(
        self,
        request: iot_20180120_models.DeleteConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteConsumerGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteConsumerGroupResponse(),
            self.do_request('DeleteConsumerGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_consumer_group_with_options_async(
        self,
        request: iot_20180120_models.DeleteConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteConsumerGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteConsumerGroupResponse(),
            await self.do_request_async('DeleteConsumerGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_consumer_group(
        self,
        request: iot_20180120_models.DeleteConsumerGroupRequest,
    ) -> iot_20180120_models.DeleteConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_consumer_group_with_options(request, runtime)

    async def delete_consumer_group_async(
        self,
        request: iot_20180120_models.DeleteConsumerGroupRequest,
    ) -> iot_20180120_models.DeleteConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_consumer_group_with_options_async(request, runtime)

    def delete_consumer_group_subscribe_relation_with_options(
        self,
        request: iot_20180120_models.DeleteConsumerGroupSubscribeRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteConsumerGroupSubscribeRelationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteConsumerGroupSubscribeRelationResponse(),
            self.do_request('DeleteConsumerGroupSubscribeRelation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_consumer_group_subscribe_relation_with_options_async(
        self,
        request: iot_20180120_models.DeleteConsumerGroupSubscribeRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteConsumerGroupSubscribeRelationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteConsumerGroupSubscribeRelationResponse(),
            await self.do_request_async('DeleteConsumerGroupSubscribeRelation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_consumer_group_subscribe_relation(
        self,
        request: iot_20180120_models.DeleteConsumerGroupSubscribeRelationRequest,
    ) -> iot_20180120_models.DeleteConsumerGroupSubscribeRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_consumer_group_subscribe_relation_with_options(request, runtime)

    async def delete_consumer_group_subscribe_relation_async(
        self,
        request: iot_20180120_models.DeleteConsumerGroupSubscribeRelationRequest,
    ) -> iot_20180120_models.DeleteConsumerGroupSubscribeRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_consumer_group_subscribe_relation_with_options_async(request, runtime)

    def delete_data_source_item_with_options(
        self,
        request: iot_20180120_models.DeleteDataSourceItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDataSourceItemResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDataSourceItemResponse(),
            self.do_request('DeleteDataSourceItem', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_data_source_item_with_options_async(
        self,
        request: iot_20180120_models.DeleteDataSourceItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDataSourceItemResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDataSourceItemResponse(),
            await self.do_request_async('DeleteDataSourceItem', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_data_source_item(
        self,
        request: iot_20180120_models.DeleteDataSourceItemRequest,
    ) -> iot_20180120_models.DeleteDataSourceItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_item_with_options(request, runtime)

    async def delete_data_source_item_async(
        self,
        request: iot_20180120_models.DeleteDataSourceItemRequest,
    ) -> iot_20180120_models.DeleteDataSourceItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_source_item_with_options_async(request, runtime)

    def delete_destination_with_options(
        self,
        request: iot_20180120_models.DeleteDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDestinationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDestinationResponse(),
            self.do_request('DeleteDestination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_destination_with_options_async(
        self,
        request: iot_20180120_models.DeleteDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDestinationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDestinationResponse(),
            await self.do_request_async('DeleteDestination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_destination(
        self,
        request: iot_20180120_models.DeleteDestinationRequest,
    ) -> iot_20180120_models.DeleteDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_destination_with_options(request, runtime)

    async def delete_destination_async(
        self,
        request: iot_20180120_models.DeleteDestinationRequest,
    ) -> iot_20180120_models.DeleteDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_destination_with_options_async(request, runtime)

    def delete_device_with_options(
        self,
        request: iot_20180120_models.DeleteDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceResponse(),
            self.do_request('DeleteDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_device_with_options_async(
        self,
        request: iot_20180120_models.DeleteDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceResponse(),
            await self.do_request_async('DeleteDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_device(
        self,
        request: iot_20180120_models.DeleteDeviceRequest,
    ) -> iot_20180120_models.DeleteDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_device_with_options(request, runtime)

    async def delete_device_async(
        self,
        request: iot_20180120_models.DeleteDeviceRequest,
    ) -> iot_20180120_models.DeleteDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_with_options_async(request, runtime)

    def delete_device_distribute_job_with_options(
        self,
        request: iot_20180120_models.DeleteDeviceDistributeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDeviceDistributeJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceDistributeJobResponse(),
            self.do_request('DeleteDeviceDistributeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_device_distribute_job_with_options_async(
        self,
        request: iot_20180120_models.DeleteDeviceDistributeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDeviceDistributeJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceDistributeJobResponse(),
            await self.do_request_async('DeleteDeviceDistributeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_device_distribute_job(
        self,
        request: iot_20180120_models.DeleteDeviceDistributeJobRequest,
    ) -> iot_20180120_models.DeleteDeviceDistributeJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_device_distribute_job_with_options(request, runtime)

    async def delete_device_distribute_job_async(
        self,
        request: iot_20180120_models.DeleteDeviceDistributeJobRequest,
    ) -> iot_20180120_models.DeleteDeviceDistributeJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_distribute_job_with_options_async(request, runtime)

    def delete_device_dynamic_group_with_options(
        self,
        request: iot_20180120_models.DeleteDeviceDynamicGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDeviceDynamicGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceDynamicGroupResponse(),
            self.do_request('DeleteDeviceDynamicGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_device_dynamic_group_with_options_async(
        self,
        request: iot_20180120_models.DeleteDeviceDynamicGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDeviceDynamicGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceDynamicGroupResponse(),
            await self.do_request_async('DeleteDeviceDynamicGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_device_dynamic_group(
        self,
        request: iot_20180120_models.DeleteDeviceDynamicGroupRequest,
    ) -> iot_20180120_models.DeleteDeviceDynamicGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_device_dynamic_group_with_options(request, runtime)

    async def delete_device_dynamic_group_async(
        self,
        request: iot_20180120_models.DeleteDeviceDynamicGroupRequest,
    ) -> iot_20180120_models.DeleteDeviceDynamicGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_dynamic_group_with_options_async(request, runtime)

    def delete_device_file_with_options(
        self,
        request: iot_20180120_models.DeleteDeviceFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDeviceFileResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceFileResponse(),
            self.do_request('DeleteDeviceFile', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_device_file_with_options_async(
        self,
        request: iot_20180120_models.DeleteDeviceFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDeviceFileResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceFileResponse(),
            await self.do_request_async('DeleteDeviceFile', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_device_file(
        self,
        request: iot_20180120_models.DeleteDeviceFileRequest,
    ) -> iot_20180120_models.DeleteDeviceFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_device_file_with_options(request, runtime)

    async def delete_device_file_async(
        self,
        request: iot_20180120_models.DeleteDeviceFileRequest,
    ) -> iot_20180120_models.DeleteDeviceFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_file_with_options_async(request, runtime)

    def delete_device_group_with_options(
        self,
        request: iot_20180120_models.DeleteDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDeviceGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceGroupResponse(),
            self.do_request('DeleteDeviceGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_device_group_with_options_async(
        self,
        request: iot_20180120_models.DeleteDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDeviceGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceGroupResponse(),
            await self.do_request_async('DeleteDeviceGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_device_group(
        self,
        request: iot_20180120_models.DeleteDeviceGroupRequest,
    ) -> iot_20180120_models.DeleteDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_device_group_with_options(request, runtime)

    async def delete_device_group_async(
        self,
        request: iot_20180120_models.DeleteDeviceGroupRequest,
    ) -> iot_20180120_models.DeleteDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_group_with_options_async(request, runtime)

    def delete_device_prop_with_options(
        self,
        request: iot_20180120_models.DeleteDevicePropRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDevicePropResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDevicePropResponse(),
            self.do_request('DeleteDeviceProp', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_device_prop_with_options_async(
        self,
        request: iot_20180120_models.DeleteDevicePropRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDevicePropResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDevicePropResponse(),
            await self.do_request_async('DeleteDeviceProp', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_device_prop(
        self,
        request: iot_20180120_models.DeleteDevicePropRequest,
    ) -> iot_20180120_models.DeleteDevicePropResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_device_prop_with_options(request, runtime)

    async def delete_device_prop_async(
        self,
        request: iot_20180120_models.DeleteDevicePropRequest,
    ) -> iot_20180120_models.DeleteDevicePropResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_prop_with_options_async(request, runtime)

    def delete_device_speech_with_options(
        self,
        request: iot_20180120_models.DeleteDeviceSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDeviceSpeechResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceSpeechResponse(),
            self.do_request('DeleteDeviceSpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_device_speech_with_options_async(
        self,
        request: iot_20180120_models.DeleteDeviceSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDeviceSpeechResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceSpeechResponse(),
            await self.do_request_async('DeleteDeviceSpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_device_speech(
        self,
        request: iot_20180120_models.DeleteDeviceSpeechRequest,
    ) -> iot_20180120_models.DeleteDeviceSpeechResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_device_speech_with_options(request, runtime)

    async def delete_device_speech_async(
        self,
        request: iot_20180120_models.DeleteDeviceSpeechRequest,
    ) -> iot_20180120_models.DeleteDeviceSpeechResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_speech_with_options_async(request, runtime)

    def delete_device_tunnel_with_options(
        self,
        request: iot_20180120_models.DeleteDeviceTunnelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDeviceTunnelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceTunnelResponse(),
            self.do_request('DeleteDeviceTunnel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_device_tunnel_with_options_async(
        self,
        request: iot_20180120_models.DeleteDeviceTunnelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDeviceTunnelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceTunnelResponse(),
            await self.do_request_async('DeleteDeviceTunnel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_device_tunnel(
        self,
        request: iot_20180120_models.DeleteDeviceTunnelRequest,
    ) -> iot_20180120_models.DeleteDeviceTunnelResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_device_tunnel_with_options(request, runtime)

    async def delete_device_tunnel_async(
        self,
        request: iot_20180120_models.DeleteDeviceTunnelRequest,
    ) -> iot_20180120_models.DeleteDeviceTunnelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_tunnel_with_options_async(request, runtime)

    def delete_edge_driver_with_options(
        self,
        request: iot_20180120_models.DeleteEdgeDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteEdgeDriverResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteEdgeDriverResponse(),
            self.do_request('DeleteEdgeDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_edge_driver_with_options_async(
        self,
        request: iot_20180120_models.DeleteEdgeDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteEdgeDriverResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteEdgeDriverResponse(),
            await self.do_request_async('DeleteEdgeDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_edge_driver(
        self,
        request: iot_20180120_models.DeleteEdgeDriverRequest,
    ) -> iot_20180120_models.DeleteEdgeDriverResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_edge_driver_with_options(request, runtime)

    async def delete_edge_driver_async(
        self,
        request: iot_20180120_models.DeleteEdgeDriverRequest,
    ) -> iot_20180120_models.DeleteEdgeDriverResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_edge_driver_with_options_async(request, runtime)

    def delete_edge_driver_version_with_options(
        self,
        request: iot_20180120_models.DeleteEdgeDriverVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteEdgeDriverVersionResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteEdgeDriverVersionResponse(),
            self.do_request('DeleteEdgeDriverVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_edge_driver_version_with_options_async(
        self,
        request: iot_20180120_models.DeleteEdgeDriverVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteEdgeDriverVersionResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteEdgeDriverVersionResponse(),
            await self.do_request_async('DeleteEdgeDriverVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_edge_driver_version(
        self,
        request: iot_20180120_models.DeleteEdgeDriverVersionRequest,
    ) -> iot_20180120_models.DeleteEdgeDriverVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_edge_driver_version_with_options(request, runtime)

    async def delete_edge_driver_version_async(
        self,
        request: iot_20180120_models.DeleteEdgeDriverVersionRequest,
    ) -> iot_20180120_models.DeleteEdgeDriverVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_edge_driver_version_with_options_async(request, runtime)

    def delete_edge_instance_with_options(
        self,
        request: iot_20180120_models.DeleteEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteEdgeInstanceResponse(),
            self.do_request('DeleteEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.DeleteEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteEdgeInstanceResponse(),
            await self.do_request_async('DeleteEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_edge_instance(
        self,
        request: iot_20180120_models.DeleteEdgeInstanceRequest,
    ) -> iot_20180120_models.DeleteEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_edge_instance_with_options(request, runtime)

    async def delete_edge_instance_async(
        self,
        request: iot_20180120_models.DeleteEdgeInstanceRequest,
    ) -> iot_20180120_models.DeleteEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_edge_instance_with_options_async(request, runtime)

    def delete_edge_instance_message_routing_with_options(
        self,
        request: iot_20180120_models.DeleteEdgeInstanceMessageRoutingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteEdgeInstanceMessageRoutingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteEdgeInstanceMessageRoutingResponse(),
            self.do_request('DeleteEdgeInstanceMessageRouting', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_edge_instance_message_routing_with_options_async(
        self,
        request: iot_20180120_models.DeleteEdgeInstanceMessageRoutingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteEdgeInstanceMessageRoutingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteEdgeInstanceMessageRoutingResponse(),
            await self.do_request_async('DeleteEdgeInstanceMessageRouting', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_edge_instance_message_routing(
        self,
        request: iot_20180120_models.DeleteEdgeInstanceMessageRoutingRequest,
    ) -> iot_20180120_models.DeleteEdgeInstanceMessageRoutingResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_edge_instance_message_routing_with_options(request, runtime)

    async def delete_edge_instance_message_routing_async(
        self,
        request: iot_20180120_models.DeleteEdgeInstanceMessageRoutingRequest,
    ) -> iot_20180120_models.DeleteEdgeInstanceMessageRoutingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_edge_instance_message_routing_with_options_async(request, runtime)

    def delete_job_with_options(
        self,
        request: iot_20180120_models.DeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteJobResponse(),
            self.do_request('DeleteJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_job_with_options_async(
        self,
        request: iot_20180120_models.DeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteJobResponse(),
            await self.do_request_async('DeleteJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_job(
        self,
        request: iot_20180120_models.DeleteJobRequest,
    ) -> iot_20180120_models.DeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_job_with_options(request, runtime)

    async def delete_job_async(
        self,
        request: iot_20180120_models.DeleteJobRequest,
    ) -> iot_20180120_models.DeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_job_with_options_async(request, runtime)

    def delete_otafirmware_with_options(
        self,
        request: iot_20180120_models.DeleteOTAFirmwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteOTAFirmwareResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteOTAFirmwareResponse(),
            self.do_request('DeleteOTAFirmware', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_otafirmware_with_options_async(
        self,
        request: iot_20180120_models.DeleteOTAFirmwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteOTAFirmwareResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteOTAFirmwareResponse(),
            await self.do_request_async('DeleteOTAFirmware', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_otafirmware(
        self,
        request: iot_20180120_models.DeleteOTAFirmwareRequest,
    ) -> iot_20180120_models.DeleteOTAFirmwareResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_otafirmware_with_options(request, runtime)

    async def delete_otafirmware_async(
        self,
        request: iot_20180120_models.DeleteOTAFirmwareRequest,
    ) -> iot_20180120_models.DeleteOTAFirmwareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_otafirmware_with_options_async(request, runtime)

    def delete_otamodule_with_options(
        self,
        request: iot_20180120_models.DeleteOTAModuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteOTAModuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteOTAModuleResponse(),
            self.do_request('DeleteOTAModule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_otamodule_with_options_async(
        self,
        request: iot_20180120_models.DeleteOTAModuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteOTAModuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteOTAModuleResponse(),
            await self.do_request_async('DeleteOTAModule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_otamodule(
        self,
        request: iot_20180120_models.DeleteOTAModuleRequest,
    ) -> iot_20180120_models.DeleteOTAModuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_otamodule_with_options(request, runtime)

    async def delete_otamodule_async(
        self,
        request: iot_20180120_models.DeleteOTAModuleRequest,
    ) -> iot_20180120_models.DeleteOTAModuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_otamodule_with_options_async(request, runtime)

    def delete_parser_with_options(
        self,
        request: iot_20180120_models.DeleteParserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteParserResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteParserResponse(),
            self.do_request('DeleteParser', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_parser_with_options_async(
        self,
        request: iot_20180120_models.DeleteParserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteParserResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteParserResponse(),
            await self.do_request_async('DeleteParser', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_parser(
        self,
        request: iot_20180120_models.DeleteParserRequest,
    ) -> iot_20180120_models.DeleteParserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_parser_with_options(request, runtime)

    async def delete_parser_async(
        self,
        request: iot_20180120_models.DeleteParserRequest,
    ) -> iot_20180120_models.DeleteParserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_parser_with_options_async(request, runtime)

    def delete_parser_data_source_with_options(
        self,
        request: iot_20180120_models.DeleteParserDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteParserDataSourceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteParserDataSourceResponse(),
            self.do_request('DeleteParserDataSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_parser_data_source_with_options_async(
        self,
        request: iot_20180120_models.DeleteParserDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteParserDataSourceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteParserDataSourceResponse(),
            await self.do_request_async('DeleteParserDataSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_parser_data_source(
        self,
        request: iot_20180120_models.DeleteParserDataSourceRequest,
    ) -> iot_20180120_models.DeleteParserDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_parser_data_source_with_options(request, runtime)

    async def delete_parser_data_source_async(
        self,
        request: iot_20180120_models.DeleteParserDataSourceRequest,
    ) -> iot_20180120_models.DeleteParserDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_parser_data_source_with_options_async(request, runtime)

    def delete_product_with_options(
        self,
        request: iot_20180120_models.DeleteProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteProductResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteProductResponse(),
            self.do_request('DeleteProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_product_with_options_async(
        self,
        request: iot_20180120_models.DeleteProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteProductResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteProductResponse(),
            await self.do_request_async('DeleteProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_product(
        self,
        request: iot_20180120_models.DeleteProductRequest,
    ) -> iot_20180120_models.DeleteProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_product_with_options(request, runtime)

    async def delete_product_async(
        self,
        request: iot_20180120_models.DeleteProductRequest,
    ) -> iot_20180120_models.DeleteProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_product_with_options_async(request, runtime)

    def delete_product_tags_with_options(
        self,
        request: iot_20180120_models.DeleteProductTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteProductTagsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteProductTagsResponse(),
            self.do_request('DeleteProductTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_product_tags_with_options_async(
        self,
        request: iot_20180120_models.DeleteProductTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteProductTagsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteProductTagsResponse(),
            await self.do_request_async('DeleteProductTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_product_tags(
        self,
        request: iot_20180120_models.DeleteProductTagsRequest,
    ) -> iot_20180120_models.DeleteProductTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_product_tags_with_options(request, runtime)

    async def delete_product_tags_async(
        self,
        request: iot_20180120_models.DeleteProductTagsRequest,
    ) -> iot_20180120_models.DeleteProductTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_product_tags_with_options_async(request, runtime)

    def delete_product_topic_with_options(
        self,
        request: iot_20180120_models.DeleteProductTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteProductTopicResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteProductTopicResponse(),
            self.do_request('DeleteProductTopic', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_product_topic_with_options_async(
        self,
        request: iot_20180120_models.DeleteProductTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteProductTopicResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteProductTopicResponse(),
            await self.do_request_async('DeleteProductTopic', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_product_topic(
        self,
        request: iot_20180120_models.DeleteProductTopicRequest,
    ) -> iot_20180120_models.DeleteProductTopicResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_product_topic_with_options(request, runtime)

    async def delete_product_topic_async(
        self,
        request: iot_20180120_models.DeleteProductTopicRequest,
    ) -> iot_20180120_models.DeleteProductTopicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_product_topic_with_options_async(request, runtime)

    def delete_rule_with_options(
        self,
        request: iot_20180120_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteRuleResponse(),
            self.do_request('DeleteRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_rule_with_options_async(
        self,
        request: iot_20180120_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteRuleResponse(),
            await self.do_request_async('DeleteRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_rule(
        self,
        request: iot_20180120_models.DeleteRuleRequest,
    ) -> iot_20180120_models.DeleteRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    async def delete_rule_async(
        self,
        request: iot_20180120_models.DeleteRuleRequest,
    ) -> iot_20180120_models.DeleteRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_rule_with_options_async(request, runtime)

    def delete_rule_action_with_options(
        self,
        request: iot_20180120_models.DeleteRuleActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteRuleActionResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteRuleActionResponse(),
            self.do_request('DeleteRuleAction', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_rule_action_with_options_async(
        self,
        request: iot_20180120_models.DeleteRuleActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteRuleActionResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteRuleActionResponse(),
            await self.do_request_async('DeleteRuleAction', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_rule_action(
        self,
        request: iot_20180120_models.DeleteRuleActionRequest,
    ) -> iot_20180120_models.DeleteRuleActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_action_with_options(request, runtime)

    async def delete_rule_action_async(
        self,
        request: iot_20180120_models.DeleteRuleActionRequest,
    ) -> iot_20180120_models.DeleteRuleActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_rule_action_with_options_async(request, runtime)

    def delete_scene_rule_with_options(
        self,
        request: iot_20180120_models.DeleteSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteSceneRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteSceneRuleResponse(),
            self.do_request('DeleteSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_scene_rule_with_options_async(
        self,
        request: iot_20180120_models.DeleteSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteSceneRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteSceneRuleResponse(),
            await self.do_request_async('DeleteSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_scene_rule(
        self,
        request: iot_20180120_models.DeleteSceneRuleRequest,
    ) -> iot_20180120_models.DeleteSceneRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_scene_rule_with_options(request, runtime)

    async def delete_scene_rule_async(
        self,
        request: iot_20180120_models.DeleteSceneRuleRequest,
    ) -> iot_20180120_models.DeleteSceneRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scene_rule_with_options_async(request, runtime)

    def delete_schedule_period_with_options(
        self,
        request: iot_20180120_models.DeleteSchedulePeriodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteSchedulePeriodResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteSchedulePeriodResponse(),
            self.do_request('DeleteSchedulePeriod', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_schedule_period_with_options_async(
        self,
        request: iot_20180120_models.DeleteSchedulePeriodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteSchedulePeriodResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteSchedulePeriodResponse(),
            await self.do_request_async('DeleteSchedulePeriod', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_schedule_period(
        self,
        request: iot_20180120_models.DeleteSchedulePeriodRequest,
    ) -> iot_20180120_models.DeleteSchedulePeriodResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_schedule_period_with_options(request, runtime)

    async def delete_schedule_period_async(
        self,
        request: iot_20180120_models.DeleteSchedulePeriodRequest,
    ) -> iot_20180120_models.DeleteSchedulePeriodResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_schedule_period_with_options_async(request, runtime)

    def delete_share_task_device_with_options(
        self,
        request: iot_20180120_models.DeleteShareTaskDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteShareTaskDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteShareTaskDeviceResponse(),
            self.do_request('DeleteShareTaskDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_share_task_device_with_options_async(
        self,
        request: iot_20180120_models.DeleteShareTaskDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteShareTaskDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteShareTaskDeviceResponse(),
            await self.do_request_async('DeleteShareTaskDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_share_task_device(
        self,
        request: iot_20180120_models.DeleteShareTaskDeviceRequest,
    ) -> iot_20180120_models.DeleteShareTaskDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_share_task_device_with_options(request, runtime)

    async def delete_share_task_device_async(
        self,
        request: iot_20180120_models.DeleteShareTaskDeviceRequest,
    ) -> iot_20180120_models.DeleteShareTaskDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_share_task_device_with_options_async(request, runtime)

    def delete_sound_code_with_options(
        self,
        request: iot_20180120_models.DeleteSoundCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteSoundCodeResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteSoundCodeResponse(),
            self.do_request('DeleteSoundCode', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_sound_code_with_options_async(
        self,
        request: iot_20180120_models.DeleteSoundCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteSoundCodeResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteSoundCodeResponse(),
            await self.do_request_async('DeleteSoundCode', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_sound_code(
        self,
        request: iot_20180120_models.DeleteSoundCodeRequest,
    ) -> iot_20180120_models.DeleteSoundCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sound_code_with_options(request, runtime)

    async def delete_sound_code_async(
        self,
        request: iot_20180120_models.DeleteSoundCodeRequest,
    ) -> iot_20180120_models.DeleteSoundCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sound_code_with_options_async(request, runtime)

    def delete_sound_code_label_with_options(
        self,
        request: iot_20180120_models.DeleteSoundCodeLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteSoundCodeLabelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteSoundCodeLabelResponse(),
            self.do_request('DeleteSoundCodeLabel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_sound_code_label_with_options_async(
        self,
        request: iot_20180120_models.DeleteSoundCodeLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteSoundCodeLabelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteSoundCodeLabelResponse(),
            await self.do_request_async('DeleteSoundCodeLabel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_sound_code_label(
        self,
        request: iot_20180120_models.DeleteSoundCodeLabelRequest,
    ) -> iot_20180120_models.DeleteSoundCodeLabelResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sound_code_label_with_options(request, runtime)

    async def delete_sound_code_label_async(
        self,
        request: iot_20180120_models.DeleteSoundCodeLabelRequest,
    ) -> iot_20180120_models.DeleteSoundCodeLabelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sound_code_label_with_options_async(request, runtime)

    def delete_sound_code_schedule_with_options(
        self,
        request: iot_20180120_models.DeleteSoundCodeScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteSoundCodeScheduleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteSoundCodeScheduleResponse(),
            self.do_request('DeleteSoundCodeSchedule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_sound_code_schedule_with_options_async(
        self,
        request: iot_20180120_models.DeleteSoundCodeScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteSoundCodeScheduleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteSoundCodeScheduleResponse(),
            await self.do_request_async('DeleteSoundCodeSchedule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_sound_code_schedule(
        self,
        request: iot_20180120_models.DeleteSoundCodeScheduleRequest,
    ) -> iot_20180120_models.DeleteSoundCodeScheduleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sound_code_schedule_with_options(request, runtime)

    async def delete_sound_code_schedule_async(
        self,
        request: iot_20180120_models.DeleteSoundCodeScheduleRequest,
    ) -> iot_20180120_models.DeleteSoundCodeScheduleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sound_code_schedule_with_options_async(request, runtime)

    def delete_speech_with_options(
        self,
        request: iot_20180120_models.DeleteSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteSpeechResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteSpeechResponse(),
            self.do_request('DeleteSpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_speech_with_options_async(
        self,
        request: iot_20180120_models.DeleteSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteSpeechResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteSpeechResponse(),
            await self.do_request_async('DeleteSpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_speech(
        self,
        request: iot_20180120_models.DeleteSpeechRequest,
    ) -> iot_20180120_models.DeleteSpeechResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_speech_with_options(request, runtime)

    async def delete_speech_async(
        self,
        request: iot_20180120_models.DeleteSpeechRequest,
    ) -> iot_20180120_models.DeleteSpeechResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_speech_with_options_async(request, runtime)

    def delete_studio_app_domain_open_with_options(
        self,
        request: iot_20180120_models.DeleteStudioAppDomainOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteStudioAppDomainOpenResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteStudioAppDomainOpenResponse(),
            self.do_request('DeleteStudioAppDomainOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_studio_app_domain_open_with_options_async(
        self,
        request: iot_20180120_models.DeleteStudioAppDomainOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteStudioAppDomainOpenResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteStudioAppDomainOpenResponse(),
            await self.do_request_async('DeleteStudioAppDomainOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_studio_app_domain_open(
        self,
        request: iot_20180120_models.DeleteStudioAppDomainOpenRequest,
    ) -> iot_20180120_models.DeleteStudioAppDomainOpenResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_studio_app_domain_open_with_options(request, runtime)

    async def delete_studio_app_domain_open_async(
        self,
        request: iot_20180120_models.DeleteStudioAppDomainOpenRequest,
    ) -> iot_20180120_models.DeleteStudioAppDomainOpenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_studio_app_domain_open_with_options_async(request, runtime)

    def delete_subscribe_relation_with_options(
        self,
        request: iot_20180120_models.DeleteSubscribeRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteSubscribeRelationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteSubscribeRelationResponse(),
            self.do_request('DeleteSubscribeRelation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_subscribe_relation_with_options_async(
        self,
        request: iot_20180120_models.DeleteSubscribeRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteSubscribeRelationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteSubscribeRelationResponse(),
            await self.do_request_async('DeleteSubscribeRelation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_subscribe_relation(
        self,
        request: iot_20180120_models.DeleteSubscribeRelationRequest,
    ) -> iot_20180120_models.DeleteSubscribeRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_subscribe_relation_with_options(request, runtime)

    async def delete_subscribe_relation_async(
        self,
        request: iot_20180120_models.DeleteSubscribeRelationRequest,
    ) -> iot_20180120_models.DeleteSubscribeRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_subscribe_relation_with_options_async(request, runtime)

    def delete_thing_model_with_options(
        self,
        request: iot_20180120_models.DeleteThingModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteThingModelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteThingModelResponse(),
            self.do_request('DeleteThingModel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_thing_model_with_options_async(
        self,
        request: iot_20180120_models.DeleteThingModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteThingModelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteThingModelResponse(),
            await self.do_request_async('DeleteThingModel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_thing_model(
        self,
        request: iot_20180120_models.DeleteThingModelRequest,
    ) -> iot_20180120_models.DeleteThingModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_thing_model_with_options(request, runtime)

    async def delete_thing_model_async(
        self,
        request: iot_20180120_models.DeleteThingModelRequest,
    ) -> iot_20180120_models.DeleteThingModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_thing_model_with_options_async(request, runtime)

    def delete_topic_route_table_with_options(
        self,
        request: iot_20180120_models.DeleteTopicRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteTopicRouteTableResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteTopicRouteTableResponse(),
            self.do_request('DeleteTopicRouteTable', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_topic_route_table_with_options_async(
        self,
        request: iot_20180120_models.DeleteTopicRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteTopicRouteTableResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteTopicRouteTableResponse(),
            await self.do_request_async('DeleteTopicRouteTable', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_topic_route_table(
        self,
        request: iot_20180120_models.DeleteTopicRouteTableRequest,
    ) -> iot_20180120_models.DeleteTopicRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_topic_route_table_with_options(request, runtime)

    async def delete_topic_route_table_async(
        self,
        request: iot_20180120_models.DeleteTopicRouteTableRequest,
    ) -> iot_20180120_models.DeleteTopicRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_topic_route_table_with_options_async(request, runtime)

    def detach_destination_with_options(
        self,
        request: iot_20180120_models.DetachDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DetachDestinationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DetachDestinationResponse(),
            self.do_request('DetachDestination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def detach_destination_with_options_async(
        self,
        request: iot_20180120_models.DetachDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DetachDestinationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DetachDestinationResponse(),
            await self.do_request_async('DetachDestination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def detach_destination(
        self,
        request: iot_20180120_models.DetachDestinationRequest,
    ) -> iot_20180120_models.DetachDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_destination_with_options(request, runtime)

    async def detach_destination_async(
        self,
        request: iot_20180120_models.DetachDestinationRequest,
    ) -> iot_20180120_models.DetachDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_destination_with_options_async(request, runtime)

    def detach_parser_data_source_with_options(
        self,
        request: iot_20180120_models.DetachParserDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DetachParserDataSourceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DetachParserDataSourceResponse(),
            self.do_request('DetachParserDataSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def detach_parser_data_source_with_options_async(
        self,
        request: iot_20180120_models.DetachParserDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DetachParserDataSourceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DetachParserDataSourceResponse(),
            await self.do_request_async('DetachParserDataSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def detach_parser_data_source(
        self,
        request: iot_20180120_models.DetachParserDataSourceRequest,
    ) -> iot_20180120_models.DetachParserDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_parser_data_source_with_options(request, runtime)

    async def detach_parser_data_source_async(
        self,
        request: iot_20180120_models.DetachParserDataSourceRequest,
    ) -> iot_20180120_models.DetachParserDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_parser_data_source_with_options_async(request, runtime)

    def disable_device_tunnel_with_options(
        self,
        request: iot_20180120_models.DisableDeviceTunnelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DisableDeviceTunnelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DisableDeviceTunnelResponse(),
            self.do_request('DisableDeviceTunnel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def disable_device_tunnel_with_options_async(
        self,
        request: iot_20180120_models.DisableDeviceTunnelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DisableDeviceTunnelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DisableDeviceTunnelResponse(),
            await self.do_request_async('DisableDeviceTunnel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def disable_device_tunnel(
        self,
        request: iot_20180120_models.DisableDeviceTunnelRequest,
    ) -> iot_20180120_models.DisableDeviceTunnelResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_device_tunnel_with_options(request, runtime)

    async def disable_device_tunnel_async(
        self,
        request: iot_20180120_models.DisableDeviceTunnelRequest,
    ) -> iot_20180120_models.DisableDeviceTunnelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_device_tunnel_with_options_async(request, runtime)

    def disable_device_tunnel_share_with_options(
        self,
        request: iot_20180120_models.DisableDeviceTunnelShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DisableDeviceTunnelShareResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DisableDeviceTunnelShareResponse(),
            self.do_request('DisableDeviceTunnelShare', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def disable_device_tunnel_share_with_options_async(
        self,
        request: iot_20180120_models.DisableDeviceTunnelShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DisableDeviceTunnelShareResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DisableDeviceTunnelShareResponse(),
            await self.do_request_async('DisableDeviceTunnelShare', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def disable_device_tunnel_share(
        self,
        request: iot_20180120_models.DisableDeviceTunnelShareRequest,
    ) -> iot_20180120_models.DisableDeviceTunnelShareResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_device_tunnel_share_with_options(request, runtime)

    async def disable_device_tunnel_share_async(
        self,
        request: iot_20180120_models.DisableDeviceTunnelShareRequest,
    ) -> iot_20180120_models.DisableDeviceTunnelShareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_device_tunnel_share_with_options_async(request, runtime)

    def disable_scene_rule_with_options(
        self,
        request: iot_20180120_models.DisableSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DisableSceneRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DisableSceneRuleResponse(),
            self.do_request('DisableSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def disable_scene_rule_with_options_async(
        self,
        request: iot_20180120_models.DisableSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DisableSceneRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DisableSceneRuleResponse(),
            await self.do_request_async('DisableSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def disable_scene_rule(
        self,
        request: iot_20180120_models.DisableSceneRuleRequest,
    ) -> iot_20180120_models.DisableSceneRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_scene_rule_with_options(request, runtime)

    async def disable_scene_rule_async(
        self,
        request: iot_20180120_models.DisableSceneRuleRequest,
    ) -> iot_20180120_models.DisableSceneRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_scene_rule_with_options_async(request, runtime)

    def disable_thing_with_options(
        self,
        request: iot_20180120_models.DisableThingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DisableThingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DisableThingResponse(),
            self.do_request('DisableThing', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def disable_thing_with_options_async(
        self,
        request: iot_20180120_models.DisableThingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DisableThingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DisableThingResponse(),
            await self.do_request_async('DisableThing', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def disable_thing(
        self,
        request: iot_20180120_models.DisableThingRequest,
    ) -> iot_20180120_models.DisableThingResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_thing_with_options(request, runtime)

    async def disable_thing_async(
        self,
        request: iot_20180120_models.DisableThingRequest,
    ) -> iot_20180120_models.DisableThingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_thing_with_options_async(request, runtime)

    def enable_device_tunnel_with_options(
        self,
        request: iot_20180120_models.EnableDeviceTunnelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.EnableDeviceTunnelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.EnableDeviceTunnelResponse(),
            self.do_request('EnableDeviceTunnel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def enable_device_tunnel_with_options_async(
        self,
        request: iot_20180120_models.EnableDeviceTunnelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.EnableDeviceTunnelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.EnableDeviceTunnelResponse(),
            await self.do_request_async('EnableDeviceTunnel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def enable_device_tunnel(
        self,
        request: iot_20180120_models.EnableDeviceTunnelRequest,
    ) -> iot_20180120_models.EnableDeviceTunnelResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_device_tunnel_with_options(request, runtime)

    async def enable_device_tunnel_async(
        self,
        request: iot_20180120_models.EnableDeviceTunnelRequest,
    ) -> iot_20180120_models.EnableDeviceTunnelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_device_tunnel_with_options_async(request, runtime)

    def enable_device_tunnel_share_with_options(
        self,
        request: iot_20180120_models.EnableDeviceTunnelShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.EnableDeviceTunnelShareResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.EnableDeviceTunnelShareResponse(),
            self.do_request('EnableDeviceTunnelShare', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def enable_device_tunnel_share_with_options_async(
        self,
        request: iot_20180120_models.EnableDeviceTunnelShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.EnableDeviceTunnelShareResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.EnableDeviceTunnelShareResponse(),
            await self.do_request_async('EnableDeviceTunnelShare', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def enable_device_tunnel_share(
        self,
        request: iot_20180120_models.EnableDeviceTunnelShareRequest,
    ) -> iot_20180120_models.EnableDeviceTunnelShareResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_device_tunnel_share_with_options(request, runtime)

    async def enable_device_tunnel_share_async(
        self,
        request: iot_20180120_models.EnableDeviceTunnelShareRequest,
    ) -> iot_20180120_models.EnableDeviceTunnelShareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_device_tunnel_share_with_options_async(request, runtime)

    def enable_scene_rule_with_options(
        self,
        request: iot_20180120_models.EnableSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.EnableSceneRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.EnableSceneRuleResponse(),
            self.do_request('EnableSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def enable_scene_rule_with_options_async(
        self,
        request: iot_20180120_models.EnableSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.EnableSceneRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.EnableSceneRuleResponse(),
            await self.do_request_async('EnableSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def enable_scene_rule(
        self,
        request: iot_20180120_models.EnableSceneRuleRequest,
    ) -> iot_20180120_models.EnableSceneRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_scene_rule_with_options(request, runtime)

    async def enable_scene_rule_async(
        self,
        request: iot_20180120_models.EnableSceneRuleRequest,
    ) -> iot_20180120_models.EnableSceneRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_scene_rule_with_options_async(request, runtime)

    def enable_thing_with_options(
        self,
        request: iot_20180120_models.EnableThingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.EnableThingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.EnableThingResponse(),
            self.do_request('EnableThing', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def enable_thing_with_options_async(
        self,
        request: iot_20180120_models.EnableThingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.EnableThingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.EnableThingResponse(),
            await self.do_request_async('EnableThing', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def enable_thing(
        self,
        request: iot_20180120_models.EnableThingRequest,
    ) -> iot_20180120_models.EnableThingResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_thing_with_options(request, runtime)

    async def enable_thing_async(
        self,
        request: iot_20180120_models.EnableThingRequest,
    ) -> iot_20180120_models.EnableThingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_thing_with_options_async(request, runtime)

    def generate_device_name_list_urlwith_options(
        self,
        request: iot_20180120_models.GenerateDeviceNameListURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GenerateDeviceNameListURLResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GenerateDeviceNameListURLResponse(),
            self.do_request('GenerateDeviceNameListURL', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def generate_device_name_list_urlwith_options_async(
        self,
        request: iot_20180120_models.GenerateDeviceNameListURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GenerateDeviceNameListURLResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GenerateDeviceNameListURLResponse(),
            await self.do_request_async('GenerateDeviceNameListURL', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def generate_device_name_list_url(
        self,
        request: iot_20180120_models.GenerateDeviceNameListURLRequest,
    ) -> iot_20180120_models.GenerateDeviceNameListURLResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_device_name_list_urlwith_options(request, runtime)

    async def generate_device_name_list_url_async(
        self,
        request: iot_20180120_models.GenerateDeviceNameListURLRequest,
    ) -> iot_20180120_models.GenerateDeviceNameListURLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_device_name_list_urlwith_options_async(request, runtime)

    def generate_file_upload_urlwith_options(
        self,
        request: iot_20180120_models.GenerateFileUploadURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GenerateFileUploadURLResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GenerateFileUploadURLResponse(),
            self.do_request('GenerateFileUploadURL', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def generate_file_upload_urlwith_options_async(
        self,
        request: iot_20180120_models.GenerateFileUploadURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GenerateFileUploadURLResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GenerateFileUploadURLResponse(),
            await self.do_request_async('GenerateFileUploadURL', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def generate_file_upload_url(
        self,
        request: iot_20180120_models.GenerateFileUploadURLRequest,
    ) -> iot_20180120_models.GenerateFileUploadURLResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_file_upload_urlwith_options(request, runtime)

    async def generate_file_upload_url_async(
        self,
        request: iot_20180120_models.GenerateFileUploadURLRequest,
    ) -> iot_20180120_models.GenerateFileUploadURLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_file_upload_urlwith_options_async(request, runtime)

    def generate_otaupload_urlwith_options(
        self,
        request: iot_20180120_models.GenerateOTAUploadURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GenerateOTAUploadURLResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GenerateOTAUploadURLResponse(),
            self.do_request('GenerateOTAUploadURL', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def generate_otaupload_urlwith_options_async(
        self,
        request: iot_20180120_models.GenerateOTAUploadURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GenerateOTAUploadURLResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GenerateOTAUploadURLResponse(),
            await self.do_request_async('GenerateOTAUploadURL', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def generate_otaupload_url(
        self,
        request: iot_20180120_models.GenerateOTAUploadURLRequest,
    ) -> iot_20180120_models.GenerateOTAUploadURLResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_otaupload_urlwith_options(request, runtime)

    async def generate_otaupload_url_async(
        self,
        request: iot_20180120_models.GenerateOTAUploadURLRequest,
    ) -> iot_20180120_models.GenerateOTAUploadURLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_otaupload_urlwith_options_async(request, runtime)

    def get_data_apiservice_detail_with_options(
        self,
        request: iot_20180120_models.GetDataAPIServiceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetDataAPIServiceDetailResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetDataAPIServiceDetailResponse(),
            self.do_request('GetDataAPIServiceDetail', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_data_apiservice_detail_with_options_async(
        self,
        request: iot_20180120_models.GetDataAPIServiceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetDataAPIServiceDetailResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetDataAPIServiceDetailResponse(),
            await self.do_request_async('GetDataAPIServiceDetail', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_data_apiservice_detail(
        self,
        request: iot_20180120_models.GetDataAPIServiceDetailRequest,
    ) -> iot_20180120_models.GetDataAPIServiceDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_data_apiservice_detail_with_options(request, runtime)

    async def get_data_apiservice_detail_async(
        self,
        request: iot_20180120_models.GetDataAPIServiceDetailRequest,
    ) -> iot_20180120_models.GetDataAPIServiceDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_data_apiservice_detail_with_options_async(request, runtime)

    def get_destination_with_options(
        self,
        request: iot_20180120_models.GetDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetDestinationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetDestinationResponse(),
            self.do_request('GetDestination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_destination_with_options_async(
        self,
        request: iot_20180120_models.GetDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetDestinationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetDestinationResponse(),
            await self.do_request_async('GetDestination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_destination(
        self,
        request: iot_20180120_models.GetDestinationRequest,
    ) -> iot_20180120_models.GetDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_destination_with_options(request, runtime)

    async def get_destination_async(
        self,
        request: iot_20180120_models.GetDestinationRequest,
    ) -> iot_20180120_models.GetDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_destination_with_options_async(request, runtime)

    def get_device_shadow_with_options(
        self,
        request: iot_20180120_models.GetDeviceShadowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetDeviceShadowResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetDeviceShadowResponse(),
            self.do_request('GetDeviceShadow', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_device_shadow_with_options_async(
        self,
        request: iot_20180120_models.GetDeviceShadowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetDeviceShadowResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetDeviceShadowResponse(),
            await self.do_request_async('GetDeviceShadow', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_device_shadow(
        self,
        request: iot_20180120_models.GetDeviceShadowRequest,
    ) -> iot_20180120_models.GetDeviceShadowResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_shadow_with_options(request, runtime)

    async def get_device_shadow_async(
        self,
        request: iot_20180120_models.GetDeviceShadowRequest,
    ) -> iot_20180120_models.GetDeviceShadowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_shadow_with_options_async(request, runtime)

    def get_device_status_with_options(
        self,
        request: iot_20180120_models.GetDeviceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetDeviceStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetDeviceStatusResponse(),
            self.do_request('GetDeviceStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_device_status_with_options_async(
        self,
        request: iot_20180120_models.GetDeviceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetDeviceStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetDeviceStatusResponse(),
            await self.do_request_async('GetDeviceStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_device_status(
        self,
        request: iot_20180120_models.GetDeviceStatusRequest,
    ) -> iot_20180120_models.GetDeviceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_status_with_options(request, runtime)

    async def get_device_status_async(
        self,
        request: iot_20180120_models.GetDeviceStatusRequest,
    ) -> iot_20180120_models.GetDeviceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_status_with_options_async(request, runtime)

    def get_device_tunnel_share_status_with_options(
        self,
        request: iot_20180120_models.GetDeviceTunnelShareStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetDeviceTunnelShareStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetDeviceTunnelShareStatusResponse(),
            self.do_request('GetDeviceTunnelShareStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_device_tunnel_share_status_with_options_async(
        self,
        request: iot_20180120_models.GetDeviceTunnelShareStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetDeviceTunnelShareStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetDeviceTunnelShareStatusResponse(),
            await self.do_request_async('GetDeviceTunnelShareStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_device_tunnel_share_status(
        self,
        request: iot_20180120_models.GetDeviceTunnelShareStatusRequest,
    ) -> iot_20180120_models.GetDeviceTunnelShareStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_tunnel_share_status_with_options(request, runtime)

    async def get_device_tunnel_share_status_async(
        self,
        request: iot_20180120_models.GetDeviceTunnelShareStatusRequest,
    ) -> iot_20180120_models.GetDeviceTunnelShareStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_tunnel_share_status_with_options_async(request, runtime)

    def get_device_tunnel_status_with_options(
        self,
        request: iot_20180120_models.GetDeviceTunnelStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetDeviceTunnelStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetDeviceTunnelStatusResponse(),
            self.do_request('GetDeviceTunnelStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_device_tunnel_status_with_options_async(
        self,
        request: iot_20180120_models.GetDeviceTunnelStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetDeviceTunnelStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetDeviceTunnelStatusResponse(),
            await self.do_request_async('GetDeviceTunnelStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_device_tunnel_status(
        self,
        request: iot_20180120_models.GetDeviceTunnelStatusRequest,
    ) -> iot_20180120_models.GetDeviceTunnelStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_tunnel_status_with_options(request, runtime)

    async def get_device_tunnel_status_async(
        self,
        request: iot_20180120_models.GetDeviceTunnelStatusRequest,
    ) -> iot_20180120_models.GetDeviceTunnelStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_tunnel_status_with_options_async(request, runtime)

    def get_download_file_with_options(
        self,
        tmp: iot_20180120_models.GetDownloadFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetDownloadFileResponse:
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.GetDownloadFileShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.context):
            request.context_shrink = UtilClient.to_jsonstring(tmp.context)
        return TeaCore.from_map(
            iot_20180120_models.GetDownloadFileResponse(),
            self.do_request('GetDownloadFile', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_download_file_with_options_async(
        self,
        tmp: iot_20180120_models.GetDownloadFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetDownloadFileResponse:
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.GetDownloadFileShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.context):
            request.context_shrink = UtilClient.to_jsonstring(tmp.context)
        return TeaCore.from_map(
            iot_20180120_models.GetDownloadFileResponse(),
            await self.do_request_async('GetDownloadFile', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_download_file(
        self,
        request: iot_20180120_models.GetDownloadFileRequest,
    ) -> iot_20180120_models.GetDownloadFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_download_file_with_options(request, runtime)

    async def get_download_file_async(
        self,
        request: iot_20180120_models.GetDownloadFileRequest,
    ) -> iot_20180120_models.GetDownloadFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_download_file_with_options_async(request, runtime)

    def get_edge_driver_version_with_options(
        self,
        request: iot_20180120_models.GetEdgeDriverVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetEdgeDriverVersionResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetEdgeDriverVersionResponse(),
            self.do_request('GetEdgeDriverVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_edge_driver_version_with_options_async(
        self,
        request: iot_20180120_models.GetEdgeDriverVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetEdgeDriverVersionResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetEdgeDriverVersionResponse(),
            await self.do_request_async('GetEdgeDriverVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_edge_driver_version(
        self,
        request: iot_20180120_models.GetEdgeDriverVersionRequest,
    ) -> iot_20180120_models.GetEdgeDriverVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_edge_driver_version_with_options(request, runtime)

    async def get_edge_driver_version_async(
        self,
        request: iot_20180120_models.GetEdgeDriverVersionRequest,
    ) -> iot_20180120_models.GetEdgeDriverVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_edge_driver_version_with_options_async(request, runtime)

    def get_edge_instance_with_options(
        self,
        request: iot_20180120_models.GetEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetEdgeInstanceResponse(),
            self.do_request('GetEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.GetEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetEdgeInstanceResponse(),
            await self.do_request_async('GetEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_edge_instance(
        self,
        request: iot_20180120_models.GetEdgeInstanceRequest,
    ) -> iot_20180120_models.GetEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_edge_instance_with_options(request, runtime)

    async def get_edge_instance_async(
        self,
        request: iot_20180120_models.GetEdgeInstanceRequest,
    ) -> iot_20180120_models.GetEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_edge_instance_with_options_async(request, runtime)

    def get_edge_instance_deployment_with_options(
        self,
        request: iot_20180120_models.GetEdgeInstanceDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetEdgeInstanceDeploymentResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetEdgeInstanceDeploymentResponse(),
            self.do_request('GetEdgeInstanceDeployment', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_edge_instance_deployment_with_options_async(
        self,
        request: iot_20180120_models.GetEdgeInstanceDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetEdgeInstanceDeploymentResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetEdgeInstanceDeploymentResponse(),
            await self.do_request_async('GetEdgeInstanceDeployment', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_edge_instance_deployment(
        self,
        request: iot_20180120_models.GetEdgeInstanceDeploymentRequest,
    ) -> iot_20180120_models.GetEdgeInstanceDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_edge_instance_deployment_with_options(request, runtime)

    async def get_edge_instance_deployment_async(
        self,
        request: iot_20180120_models.GetEdgeInstanceDeploymentRequest,
    ) -> iot_20180120_models.GetEdgeInstanceDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_edge_instance_deployment_with_options_async(request, runtime)

    def get_edge_instance_message_routing_with_options(
        self,
        request: iot_20180120_models.GetEdgeInstanceMessageRoutingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetEdgeInstanceMessageRoutingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetEdgeInstanceMessageRoutingResponse(),
            self.do_request('GetEdgeInstanceMessageRouting', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_edge_instance_message_routing_with_options_async(
        self,
        request: iot_20180120_models.GetEdgeInstanceMessageRoutingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetEdgeInstanceMessageRoutingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetEdgeInstanceMessageRoutingResponse(),
            await self.do_request_async('GetEdgeInstanceMessageRouting', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_edge_instance_message_routing(
        self,
        request: iot_20180120_models.GetEdgeInstanceMessageRoutingRequest,
    ) -> iot_20180120_models.GetEdgeInstanceMessageRoutingResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_edge_instance_message_routing_with_options(request, runtime)

    async def get_edge_instance_message_routing_async(
        self,
        request: iot_20180120_models.GetEdgeInstanceMessageRoutingRequest,
    ) -> iot_20180120_models.GetEdgeInstanceMessageRoutingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_edge_instance_message_routing_with_options_async(request, runtime)

    def get_gateway_by_sub_device_with_options(
        self,
        request: iot_20180120_models.GetGatewayBySubDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetGatewayBySubDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetGatewayBySubDeviceResponse(),
            self.do_request('GetGatewayBySubDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_gateway_by_sub_device_with_options_async(
        self,
        request: iot_20180120_models.GetGatewayBySubDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetGatewayBySubDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetGatewayBySubDeviceResponse(),
            await self.do_request_async('GetGatewayBySubDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_gateway_by_sub_device(
        self,
        request: iot_20180120_models.GetGatewayBySubDeviceRequest,
    ) -> iot_20180120_models.GetGatewayBySubDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_gateway_by_sub_device_with_options(request, runtime)

    async def get_gateway_by_sub_device_async(
        self,
        request: iot_20180120_models.GetGatewayBySubDeviceRequest,
    ) -> iot_20180120_models.GetGatewayBySubDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_gateway_by_sub_device_with_options_async(request, runtime)

    def get_lora_nodes_task_with_options(
        self,
        request: iot_20180120_models.GetLoraNodesTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetLoraNodesTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetLoraNodesTaskResponse(),
            self.do_request('GetLoraNodesTask', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_lora_nodes_task_with_options_async(
        self,
        request: iot_20180120_models.GetLoraNodesTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetLoraNodesTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetLoraNodesTaskResponse(),
            await self.do_request_async('GetLoraNodesTask', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_lora_nodes_task(
        self,
        request: iot_20180120_models.GetLoraNodesTaskRequest,
    ) -> iot_20180120_models.GetLoraNodesTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_lora_nodes_task_with_options(request, runtime)

    async def get_lora_nodes_task_async(
        self,
        request: iot_20180120_models.GetLoraNodesTaskRequest,
    ) -> iot_20180120_models.GetLoraNodesTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_lora_nodes_task_with_options_async(request, runtime)

    def get_parser_with_options(
        self,
        request: iot_20180120_models.GetParserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetParserResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetParserResponse(),
            self.do_request('GetParser', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_parser_with_options_async(
        self,
        request: iot_20180120_models.GetParserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetParserResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetParserResponse(),
            await self.do_request_async('GetParser', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_parser(
        self,
        request: iot_20180120_models.GetParserRequest,
    ) -> iot_20180120_models.GetParserResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_parser_with_options(request, runtime)

    async def get_parser_async(
        self,
        request: iot_20180120_models.GetParserRequest,
    ) -> iot_20180120_models.GetParserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_parser_with_options_async(request, runtime)

    def get_parser_data_source_with_options(
        self,
        request: iot_20180120_models.GetParserDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetParserDataSourceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetParserDataSourceResponse(),
            self.do_request('GetParserDataSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_parser_data_source_with_options_async(
        self,
        request: iot_20180120_models.GetParserDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetParserDataSourceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetParserDataSourceResponse(),
            await self.do_request_async('GetParserDataSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_parser_data_source(
        self,
        request: iot_20180120_models.GetParserDataSourceRequest,
    ) -> iot_20180120_models.GetParserDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_parser_data_source_with_options(request, runtime)

    async def get_parser_data_source_async(
        self,
        request: iot_20180120_models.GetParserDataSourceRequest,
    ) -> iot_20180120_models.GetParserDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_parser_data_source_with_options_async(request, runtime)

    def get_rule_with_options(
        self,
        request: iot_20180120_models.GetRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetRuleResponse(),
            self.do_request('GetRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_rule_with_options_async(
        self,
        request: iot_20180120_models.GetRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetRuleResponse(),
            await self.do_request_async('GetRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_rule(
        self,
        request: iot_20180120_models.GetRuleRequest,
    ) -> iot_20180120_models.GetRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_rule_with_options(request, runtime)

    async def get_rule_async(
        self,
        request: iot_20180120_models.GetRuleRequest,
    ) -> iot_20180120_models.GetRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_rule_with_options_async(request, runtime)

    def get_rule_action_with_options(
        self,
        request: iot_20180120_models.GetRuleActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetRuleActionResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetRuleActionResponse(),
            self.do_request('GetRuleAction', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_rule_action_with_options_async(
        self,
        request: iot_20180120_models.GetRuleActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetRuleActionResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetRuleActionResponse(),
            await self.do_request_async('GetRuleAction', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_rule_action(
        self,
        request: iot_20180120_models.GetRuleActionRequest,
    ) -> iot_20180120_models.GetRuleActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_rule_action_with_options(request, runtime)

    async def get_rule_action_async(
        self,
        request: iot_20180120_models.GetRuleActionRequest,
    ) -> iot_20180120_models.GetRuleActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_rule_action_with_options_async(request, runtime)

    def get_scene_rule_with_options(
        self,
        request: iot_20180120_models.GetSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetSceneRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetSceneRuleResponse(),
            self.do_request('GetSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_scene_rule_with_options_async(
        self,
        request: iot_20180120_models.GetSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetSceneRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetSceneRuleResponse(),
            await self.do_request_async('GetSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_scene_rule(
        self,
        request: iot_20180120_models.GetSceneRuleRequest,
    ) -> iot_20180120_models.GetSceneRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_scene_rule_with_options(request, runtime)

    async def get_scene_rule_async(
        self,
        request: iot_20180120_models.GetSceneRuleRequest,
    ) -> iot_20180120_models.GetSceneRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_scene_rule_with_options_async(request, runtime)

    def get_share_task_by_device_open_with_options(
        self,
        request: iot_20180120_models.GetShareTaskByDeviceOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetShareTaskByDeviceOpenResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetShareTaskByDeviceOpenResponse(),
            self.do_request('GetShareTaskByDeviceOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_share_task_by_device_open_with_options_async(
        self,
        request: iot_20180120_models.GetShareTaskByDeviceOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetShareTaskByDeviceOpenResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetShareTaskByDeviceOpenResponse(),
            await self.do_request_async('GetShareTaskByDeviceOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_share_task_by_device_open(
        self,
        request: iot_20180120_models.GetShareTaskByDeviceOpenRequest,
    ) -> iot_20180120_models.GetShareTaskByDeviceOpenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_share_task_by_device_open_with_options(request, runtime)

    async def get_share_task_by_device_open_async(
        self,
        request: iot_20180120_models.GetShareTaskByDeviceOpenRequest,
    ) -> iot_20180120_models.GetShareTaskByDeviceOpenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_share_task_by_device_open_with_options_async(request, runtime)

    def get_sound_code_audio_with_options(
        self,
        request: iot_20180120_models.GetSoundCodeAudioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetSoundCodeAudioResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetSoundCodeAudioResponse(),
            self.do_request('GetSoundCodeAudio', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_sound_code_audio_with_options_async(
        self,
        request: iot_20180120_models.GetSoundCodeAudioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetSoundCodeAudioResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetSoundCodeAudioResponse(),
            await self.do_request_async('GetSoundCodeAudio', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_sound_code_audio(
        self,
        request: iot_20180120_models.GetSoundCodeAudioRequest,
    ) -> iot_20180120_models.GetSoundCodeAudioResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sound_code_audio_with_options(request, runtime)

    async def get_sound_code_audio_async(
        self,
        request: iot_20180120_models.GetSoundCodeAudioRequest,
    ) -> iot_20180120_models.GetSoundCodeAudioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sound_code_audio_with_options_async(request, runtime)

    def get_sound_code_schedule_with_options(
        self,
        request: iot_20180120_models.GetSoundCodeScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetSoundCodeScheduleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetSoundCodeScheduleResponse(),
            self.do_request('GetSoundCodeSchedule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_sound_code_schedule_with_options_async(
        self,
        request: iot_20180120_models.GetSoundCodeScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetSoundCodeScheduleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetSoundCodeScheduleResponse(),
            await self.do_request_async('GetSoundCodeSchedule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_sound_code_schedule(
        self,
        request: iot_20180120_models.GetSoundCodeScheduleRequest,
    ) -> iot_20180120_models.GetSoundCodeScheduleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sound_code_schedule_with_options(request, runtime)

    async def get_sound_code_schedule_async(
        self,
        request: iot_20180120_models.GetSoundCodeScheduleRequest,
    ) -> iot_20180120_models.GetSoundCodeScheduleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sound_code_schedule_with_options_async(request, runtime)

    def get_speech_device_detail_with_options(
        self,
        request: iot_20180120_models.GetSpeechDeviceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetSpeechDeviceDetailResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetSpeechDeviceDetailResponse(),
            self.do_request('GetSpeechDeviceDetail', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_speech_device_detail_with_options_async(
        self,
        request: iot_20180120_models.GetSpeechDeviceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetSpeechDeviceDetailResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetSpeechDeviceDetailResponse(),
            await self.do_request_async('GetSpeechDeviceDetail', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_speech_device_detail(
        self,
        request: iot_20180120_models.GetSpeechDeviceDetailRequest,
    ) -> iot_20180120_models.GetSpeechDeviceDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_speech_device_detail_with_options(request, runtime)

    async def get_speech_device_detail_async(
        self,
        request: iot_20180120_models.GetSpeechDeviceDetailRequest,
    ) -> iot_20180120_models.GetSpeechDeviceDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_speech_device_detail_with_options_async(request, runtime)

    def get_speech_license_device_statistics_with_options(
        self,
        request: iot_20180120_models.GetSpeechLicenseDeviceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetSpeechLicenseDeviceStatisticsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetSpeechLicenseDeviceStatisticsResponse(),
            self.do_request('GetSpeechLicenseDeviceStatistics', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_speech_license_device_statistics_with_options_async(
        self,
        request: iot_20180120_models.GetSpeechLicenseDeviceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetSpeechLicenseDeviceStatisticsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetSpeechLicenseDeviceStatisticsResponse(),
            await self.do_request_async('GetSpeechLicenseDeviceStatistics', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_speech_license_device_statistics(
        self,
        request: iot_20180120_models.GetSpeechLicenseDeviceStatisticsRequest,
    ) -> iot_20180120_models.GetSpeechLicenseDeviceStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_speech_license_device_statistics_with_options(request, runtime)

    async def get_speech_license_device_statistics_async(
        self,
        request: iot_20180120_models.GetSpeechLicenseDeviceStatisticsRequest,
    ) -> iot_20180120_models.GetSpeechLicenseDeviceStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_speech_license_device_statistics_with_options_async(request, runtime)

    def get_speech_voice_with_options(
        self,
        request: iot_20180120_models.GetSpeechVoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetSpeechVoiceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetSpeechVoiceResponse(),
            self.do_request('GetSpeechVoice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_speech_voice_with_options_async(
        self,
        request: iot_20180120_models.GetSpeechVoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetSpeechVoiceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetSpeechVoiceResponse(),
            await self.do_request_async('GetSpeechVoice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_speech_voice(
        self,
        request: iot_20180120_models.GetSpeechVoiceRequest,
    ) -> iot_20180120_models.GetSpeechVoiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_speech_voice_with_options(request, runtime)

    async def get_speech_voice_async(
        self,
        request: iot_20180120_models.GetSpeechVoiceRequest,
    ) -> iot_20180120_models.GetSpeechVoiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_speech_voice_with_options_async(request, runtime)

    def get_studio_app_token_open_with_options(
        self,
        request: iot_20180120_models.GetStudioAppTokenOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetStudioAppTokenOpenResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetStudioAppTokenOpenResponse(),
            self.do_request('GetStudioAppTokenOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_studio_app_token_open_with_options_async(
        self,
        request: iot_20180120_models.GetStudioAppTokenOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetStudioAppTokenOpenResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetStudioAppTokenOpenResponse(),
            await self.do_request_async('GetStudioAppTokenOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_studio_app_token_open(
        self,
        request: iot_20180120_models.GetStudioAppTokenOpenRequest,
    ) -> iot_20180120_models.GetStudioAppTokenOpenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_studio_app_token_open_with_options(request, runtime)

    async def get_studio_app_token_open_async(
        self,
        request: iot_20180120_models.GetStudioAppTokenOpenRequest,
    ) -> iot_20180120_models.GetStudioAppTokenOpenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_studio_app_token_open_with_options_async(request, runtime)

    def get_thing_model_tsl_with_options(
        self,
        request: iot_20180120_models.GetThingModelTslRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetThingModelTslResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetThingModelTslResponse(),
            self.do_request('GetThingModelTsl', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_thing_model_tsl_with_options_async(
        self,
        request: iot_20180120_models.GetThingModelTslRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetThingModelTslResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetThingModelTslResponse(),
            await self.do_request_async('GetThingModelTsl', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_thing_model_tsl(
        self,
        request: iot_20180120_models.GetThingModelTslRequest,
    ) -> iot_20180120_models.GetThingModelTslResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_thing_model_tsl_with_options(request, runtime)

    async def get_thing_model_tsl_async(
        self,
        request: iot_20180120_models.GetThingModelTslRequest,
    ) -> iot_20180120_models.GetThingModelTslResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_thing_model_tsl_with_options_async(request, runtime)

    def get_thing_model_tsl_published_with_options(
        self,
        request: iot_20180120_models.GetThingModelTslPublishedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetThingModelTslPublishedResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetThingModelTslPublishedResponse(),
            self.do_request('GetThingModelTslPublished', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_thing_model_tsl_published_with_options_async(
        self,
        request: iot_20180120_models.GetThingModelTslPublishedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetThingModelTslPublishedResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetThingModelTslPublishedResponse(),
            await self.do_request_async('GetThingModelTslPublished', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_thing_model_tsl_published(
        self,
        request: iot_20180120_models.GetThingModelTslPublishedRequest,
    ) -> iot_20180120_models.GetThingModelTslPublishedResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_thing_model_tsl_published_with_options(request, runtime)

    async def get_thing_model_tsl_published_async(
        self,
        request: iot_20180120_models.GetThingModelTslPublishedRequest,
    ) -> iot_20180120_models.GetThingModelTslPublishedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_thing_model_tsl_published_with_options_async(request, runtime)

    def get_thing_script_with_options(
        self,
        request: iot_20180120_models.GetThingScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetThingScriptResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetThingScriptResponse(),
            self.do_request('GetThingScript', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_thing_script_with_options_async(
        self,
        request: iot_20180120_models.GetThingScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetThingScriptResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetThingScriptResponse(),
            await self.do_request_async('GetThingScript', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_thing_script(
        self,
        request: iot_20180120_models.GetThingScriptRequest,
    ) -> iot_20180120_models.GetThingScriptResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_thing_script_with_options(request, runtime)

    async def get_thing_script_async(
        self,
        request: iot_20180120_models.GetThingScriptRequest,
    ) -> iot_20180120_models.GetThingScriptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_thing_script_with_options_async(request, runtime)

    def get_thing_template_with_options(
        self,
        request: iot_20180120_models.GetThingTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetThingTemplateResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetThingTemplateResponse(),
            self.do_request('GetThingTemplate', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_thing_template_with_options_async(
        self,
        request: iot_20180120_models.GetThingTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetThingTemplateResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetThingTemplateResponse(),
            await self.do_request_async('GetThingTemplate', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_thing_template(
        self,
        request: iot_20180120_models.GetThingTemplateRequest,
    ) -> iot_20180120_models.GetThingTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_thing_template_with_options(request, runtime)

    async def get_thing_template_async(
        self,
        request: iot_20180120_models.GetThingTemplateRequest,
    ) -> iot_20180120_models.GetThingTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_thing_template_with_options_async(request, runtime)

    def get_thing_topo_with_options(
        self,
        request: iot_20180120_models.GetThingTopoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetThingTopoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetThingTopoResponse(),
            self.do_request('GetThingTopo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_thing_topo_with_options_async(
        self,
        request: iot_20180120_models.GetThingTopoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetThingTopoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetThingTopoResponse(),
            await self.do_request_async('GetThingTopo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_thing_topo(
        self,
        request: iot_20180120_models.GetThingTopoRequest,
    ) -> iot_20180120_models.GetThingTopoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_thing_topo_with_options(request, runtime)

    async def get_thing_topo_async(
        self,
        request: iot_20180120_models.GetThingTopoRequest,
    ) -> iot_20180120_models.GetThingTopoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_thing_topo_with_options_async(request, runtime)

    def gis_query_device_location_with_options(
        self,
        request: iot_20180120_models.GisQueryDeviceLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GisQueryDeviceLocationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GisQueryDeviceLocationResponse(),
            self.do_request('GisQueryDeviceLocation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def gis_query_device_location_with_options_async(
        self,
        request: iot_20180120_models.GisQueryDeviceLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GisQueryDeviceLocationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GisQueryDeviceLocationResponse(),
            await self.do_request_async('GisQueryDeviceLocation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def gis_query_device_location(
        self,
        request: iot_20180120_models.GisQueryDeviceLocationRequest,
    ) -> iot_20180120_models.GisQueryDeviceLocationResponse:
        runtime = util_models.RuntimeOptions()
        return self.gis_query_device_location_with_options(request, runtime)

    async def gis_query_device_location_async(
        self,
        request: iot_20180120_models.GisQueryDeviceLocationRequest,
    ) -> iot_20180120_models.GisQueryDeviceLocationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.gis_query_device_location_with_options_async(request, runtime)

    def gis_search_device_trace_with_options(
        self,
        request: iot_20180120_models.GisSearchDeviceTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GisSearchDeviceTraceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GisSearchDeviceTraceResponse(),
            self.do_request('GisSearchDeviceTrace', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def gis_search_device_trace_with_options_async(
        self,
        request: iot_20180120_models.GisSearchDeviceTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GisSearchDeviceTraceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GisSearchDeviceTraceResponse(),
            await self.do_request_async('GisSearchDeviceTrace', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def gis_search_device_trace(
        self,
        request: iot_20180120_models.GisSearchDeviceTraceRequest,
    ) -> iot_20180120_models.GisSearchDeviceTraceResponse:
        runtime = util_models.RuntimeOptions()
        return self.gis_search_device_trace_with_options(request, runtime)

    async def gis_search_device_trace_async(
        self,
        request: iot_20180120_models.GisSearchDeviceTraceRequest,
    ) -> iot_20180120_models.GisSearchDeviceTraceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.gis_search_device_trace_with_options_async(request, runtime)

    def import_dtdata_with_options(
        self,
        request: iot_20180120_models.ImportDTDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ImportDTDataResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ImportDTDataResponse(),
            self.do_request('ImportDTData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def import_dtdata_with_options_async(
        self,
        request: iot_20180120_models.ImportDTDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ImportDTDataResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ImportDTDataResponse(),
            await self.do_request_async('ImportDTData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def import_dtdata(
        self,
        request: iot_20180120_models.ImportDTDataRequest,
    ) -> iot_20180120_models.ImportDTDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_dtdata_with_options(request, runtime)

    async def import_dtdata_async(
        self,
        request: iot_20180120_models.ImportDTDataRequest,
    ) -> iot_20180120_models.ImportDTDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_dtdata_with_options_async(request, runtime)

    def import_device_with_options(
        self,
        request: iot_20180120_models.ImportDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ImportDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ImportDeviceResponse(),
            self.do_request('ImportDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def import_device_with_options_async(
        self,
        request: iot_20180120_models.ImportDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ImportDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ImportDeviceResponse(),
            await self.do_request_async('ImportDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def import_device(
        self,
        request: iot_20180120_models.ImportDeviceRequest,
    ) -> iot_20180120_models.ImportDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_device_with_options(request, runtime)

    async def import_device_async(
        self,
        request: iot_20180120_models.ImportDeviceRequest,
    ) -> iot_20180120_models.ImportDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_device_with_options_async(request, runtime)

    def import_thing_model_tsl_with_options(
        self,
        request: iot_20180120_models.ImportThingModelTslRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ImportThingModelTslResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ImportThingModelTslResponse(),
            self.do_request('ImportThingModelTsl', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def import_thing_model_tsl_with_options_async(
        self,
        request: iot_20180120_models.ImportThingModelTslRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ImportThingModelTslResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ImportThingModelTslResponse(),
            await self.do_request_async('ImportThingModelTsl', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def import_thing_model_tsl(
        self,
        request: iot_20180120_models.ImportThingModelTslRequest,
    ) -> iot_20180120_models.ImportThingModelTslResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_thing_model_tsl_with_options(request, runtime)

    async def import_thing_model_tsl_async(
        self,
        request: iot_20180120_models.ImportThingModelTslRequest,
    ) -> iot_20180120_models.ImportThingModelTslResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_thing_model_tsl_with_options_async(request, runtime)

    def invoke_data_apiservice_with_options(
        self,
        request: iot_20180120_models.InvokeDataAPIServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.InvokeDataAPIServiceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.InvokeDataAPIServiceResponse(),
            self.do_request('InvokeDataAPIService', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def invoke_data_apiservice_with_options_async(
        self,
        request: iot_20180120_models.InvokeDataAPIServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.InvokeDataAPIServiceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.InvokeDataAPIServiceResponse(),
            await self.do_request_async('InvokeDataAPIService', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def invoke_data_apiservice(
        self,
        request: iot_20180120_models.InvokeDataAPIServiceRequest,
    ) -> iot_20180120_models.InvokeDataAPIServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.invoke_data_apiservice_with_options(request, runtime)

    async def invoke_data_apiservice_async(
        self,
        request: iot_20180120_models.InvokeDataAPIServiceRequest,
    ) -> iot_20180120_models.InvokeDataAPIServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.invoke_data_apiservice_with_options_async(request, runtime)

    def invoke_thing_service_with_options(
        self,
        request: iot_20180120_models.InvokeThingServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.InvokeThingServiceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.InvokeThingServiceResponse(),
            self.do_request('InvokeThingService', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def invoke_thing_service_with_options_async(
        self,
        request: iot_20180120_models.InvokeThingServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.InvokeThingServiceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.InvokeThingServiceResponse(),
            await self.do_request_async('InvokeThingService', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def invoke_thing_service(
        self,
        request: iot_20180120_models.InvokeThingServiceRequest,
    ) -> iot_20180120_models.InvokeThingServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.invoke_thing_service_with_options(request, runtime)

    async def invoke_thing_service_async(
        self,
        request: iot_20180120_models.InvokeThingServiceRequest,
    ) -> iot_20180120_models.InvokeThingServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.invoke_thing_service_with_options_async(request, runtime)

    def invoke_things_service_with_options(
        self,
        request: iot_20180120_models.InvokeThingsServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.InvokeThingsServiceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.InvokeThingsServiceResponse(),
            self.do_request('InvokeThingsService', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def invoke_things_service_with_options_async(
        self,
        request: iot_20180120_models.InvokeThingsServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.InvokeThingsServiceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.InvokeThingsServiceResponse(),
            await self.do_request_async('InvokeThingsService', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def invoke_things_service(
        self,
        request: iot_20180120_models.InvokeThingsServiceRequest,
    ) -> iot_20180120_models.InvokeThingsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.invoke_things_service_with_options(request, runtime)

    async def invoke_things_service_async(
        self,
        request: iot_20180120_models.InvokeThingsServiceRequest,
    ) -> iot_20180120_models.InvokeThingsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.invoke_things_service_with_options_async(request, runtime)

    def list_analytics_data_with_options(
        self,
        request: iot_20180120_models.ListAnalyticsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListAnalyticsDataResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListAnalyticsDataResponse(),
            self.do_request('ListAnalyticsData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_analytics_data_with_options_async(
        self,
        request: iot_20180120_models.ListAnalyticsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListAnalyticsDataResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListAnalyticsDataResponse(),
            await self.do_request_async('ListAnalyticsData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_analytics_data(
        self,
        request: iot_20180120_models.ListAnalyticsDataRequest,
    ) -> iot_20180120_models.ListAnalyticsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_analytics_data_with_options(request, runtime)

    async def list_analytics_data_async(
        self,
        request: iot_20180120_models.ListAnalyticsDataRequest,
    ) -> iot_20180120_models.ListAnalyticsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_analytics_data_with_options_async(request, runtime)

    def list_data_source_item_with_options(
        self,
        request: iot_20180120_models.ListDataSourceItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListDataSourceItemResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListDataSourceItemResponse(),
            self.do_request('ListDataSourceItem', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_data_source_item_with_options_async(
        self,
        request: iot_20180120_models.ListDataSourceItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListDataSourceItemResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListDataSourceItemResponse(),
            await self.do_request_async('ListDataSourceItem', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_data_source_item(
        self,
        request: iot_20180120_models.ListDataSourceItemRequest,
    ) -> iot_20180120_models.ListDataSourceItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_data_source_item_with_options(request, runtime)

    async def list_data_source_item_async(
        self,
        request: iot_20180120_models.ListDataSourceItemRequest,
    ) -> iot_20180120_models.ListDataSourceItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_data_source_item_with_options_async(request, runtime)

    def list_destination_with_options(
        self,
        request: iot_20180120_models.ListDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListDestinationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListDestinationResponse(),
            self.do_request('ListDestination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_destination_with_options_async(
        self,
        request: iot_20180120_models.ListDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListDestinationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListDestinationResponse(),
            await self.do_request_async('ListDestination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_destination(
        self,
        request: iot_20180120_models.ListDestinationRequest,
    ) -> iot_20180120_models.ListDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_destination_with_options(request, runtime)

    async def list_destination_async(
        self,
        request: iot_20180120_models.ListDestinationRequest,
    ) -> iot_20180120_models.ListDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_destination_with_options_async(request, runtime)

    def list_device_distribute_job_with_options(
        self,
        request: iot_20180120_models.ListDeviceDistributeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListDeviceDistributeJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListDeviceDistributeJobResponse(),
            self.do_request('ListDeviceDistributeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_device_distribute_job_with_options_async(
        self,
        request: iot_20180120_models.ListDeviceDistributeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListDeviceDistributeJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListDeviceDistributeJobResponse(),
            await self.do_request_async('ListDeviceDistributeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_device_distribute_job(
        self,
        request: iot_20180120_models.ListDeviceDistributeJobRequest,
    ) -> iot_20180120_models.ListDeviceDistributeJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_device_distribute_job_with_options(request, runtime)

    async def list_device_distribute_job_async(
        self,
        request: iot_20180120_models.ListDeviceDistributeJobRequest,
    ) -> iot_20180120_models.ListDeviceDistributeJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_device_distribute_job_with_options_async(request, runtime)

    def list_distributed_device_with_options(
        self,
        request: iot_20180120_models.ListDistributedDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListDistributedDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListDistributedDeviceResponse(),
            self.do_request('ListDistributedDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_distributed_device_with_options_async(
        self,
        request: iot_20180120_models.ListDistributedDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListDistributedDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListDistributedDeviceResponse(),
            await self.do_request_async('ListDistributedDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_distributed_device(
        self,
        request: iot_20180120_models.ListDistributedDeviceRequest,
    ) -> iot_20180120_models.ListDistributedDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_distributed_device_with_options(request, runtime)

    async def list_distributed_device_async(
        self,
        request: iot_20180120_models.ListDistributedDeviceRequest,
    ) -> iot_20180120_models.ListDistributedDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_distributed_device_with_options_async(request, runtime)

    def list_distributed_product_with_options(
        self,
        request: iot_20180120_models.ListDistributedProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListDistributedProductResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListDistributedProductResponse(),
            self.do_request('ListDistributedProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_distributed_product_with_options_async(
        self,
        request: iot_20180120_models.ListDistributedProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListDistributedProductResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListDistributedProductResponse(),
            await self.do_request_async('ListDistributedProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_distributed_product(
        self,
        request: iot_20180120_models.ListDistributedProductRequest,
    ) -> iot_20180120_models.ListDistributedProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_distributed_product_with_options(request, runtime)

    async def list_distributed_product_async(
        self,
        request: iot_20180120_models.ListDistributedProductRequest,
    ) -> iot_20180120_models.ListDistributedProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_distributed_product_with_options_async(request, runtime)

    def list_job_with_options(
        self,
        request: iot_20180120_models.ListJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListJobResponse(),
            self.do_request('ListJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_job_with_options_async(
        self,
        request: iot_20180120_models.ListJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListJobResponse(),
            await self.do_request_async('ListJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_job(
        self,
        request: iot_20180120_models.ListJobRequest,
    ) -> iot_20180120_models.ListJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_job_with_options(request, runtime)

    async def list_job_async(
        self,
        request: iot_20180120_models.ListJobRequest,
    ) -> iot_20180120_models.ListJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_job_with_options_async(request, runtime)

    def list_otafirmware_with_options(
        self,
        request: iot_20180120_models.ListOTAFirmwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListOTAFirmwareResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListOTAFirmwareResponse(),
            self.do_request('ListOTAFirmware', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_otafirmware_with_options_async(
        self,
        request: iot_20180120_models.ListOTAFirmwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListOTAFirmwareResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListOTAFirmwareResponse(),
            await self.do_request_async('ListOTAFirmware', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_otafirmware(
        self,
        request: iot_20180120_models.ListOTAFirmwareRequest,
    ) -> iot_20180120_models.ListOTAFirmwareResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_otafirmware_with_options(request, runtime)

    async def list_otafirmware_async(
        self,
        request: iot_20180120_models.ListOTAFirmwareRequest,
    ) -> iot_20180120_models.ListOTAFirmwareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_otafirmware_with_options_async(request, runtime)

    def list_otajob_by_device_with_options(
        self,
        request: iot_20180120_models.ListOTAJobByDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListOTAJobByDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListOTAJobByDeviceResponse(),
            self.do_request('ListOTAJobByDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_otajob_by_device_with_options_async(
        self,
        request: iot_20180120_models.ListOTAJobByDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListOTAJobByDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListOTAJobByDeviceResponse(),
            await self.do_request_async('ListOTAJobByDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_otajob_by_device(
        self,
        request: iot_20180120_models.ListOTAJobByDeviceRequest,
    ) -> iot_20180120_models.ListOTAJobByDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_otajob_by_device_with_options(request, runtime)

    async def list_otajob_by_device_async(
        self,
        request: iot_20180120_models.ListOTAJobByDeviceRequest,
    ) -> iot_20180120_models.ListOTAJobByDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_otajob_by_device_with_options_async(request, runtime)

    def list_otajob_by_firmware_with_options(
        self,
        request: iot_20180120_models.ListOTAJobByFirmwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListOTAJobByFirmwareResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListOTAJobByFirmwareResponse(),
            self.do_request('ListOTAJobByFirmware', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_otajob_by_firmware_with_options_async(
        self,
        request: iot_20180120_models.ListOTAJobByFirmwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListOTAJobByFirmwareResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListOTAJobByFirmwareResponse(),
            await self.do_request_async('ListOTAJobByFirmware', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_otajob_by_firmware(
        self,
        request: iot_20180120_models.ListOTAJobByFirmwareRequest,
    ) -> iot_20180120_models.ListOTAJobByFirmwareResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_otajob_by_firmware_with_options(request, runtime)

    async def list_otajob_by_firmware_async(
        self,
        request: iot_20180120_models.ListOTAJobByFirmwareRequest,
    ) -> iot_20180120_models.ListOTAJobByFirmwareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_otajob_by_firmware_with_options_async(request, runtime)

    def list_otamodule_by_product_with_options(
        self,
        request: iot_20180120_models.ListOTAModuleByProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListOTAModuleByProductResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListOTAModuleByProductResponse(),
            self.do_request('ListOTAModuleByProduct', 'HTTPS', 'GET', '2018-01-20', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def list_otamodule_by_product_with_options_async(
        self,
        request: iot_20180120_models.ListOTAModuleByProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListOTAModuleByProductResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListOTAModuleByProductResponse(),
            await self.do_request_async('ListOTAModuleByProduct', 'HTTPS', 'GET', '2018-01-20', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def list_otamodule_by_product(
        self,
        request: iot_20180120_models.ListOTAModuleByProductRequest,
    ) -> iot_20180120_models.ListOTAModuleByProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_otamodule_by_product_with_options(request, runtime)

    async def list_otamodule_by_product_async(
        self,
        request: iot_20180120_models.ListOTAModuleByProductRequest,
    ) -> iot_20180120_models.ListOTAModuleByProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_otamodule_by_product_with_options_async(request, runtime)

    def list_otamodule_versions_by_device_with_options(
        self,
        request: iot_20180120_models.ListOTAModuleVersionsByDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListOTAModuleVersionsByDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListOTAModuleVersionsByDeviceResponse(),
            self.do_request('ListOTAModuleVersionsByDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_otamodule_versions_by_device_with_options_async(
        self,
        request: iot_20180120_models.ListOTAModuleVersionsByDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListOTAModuleVersionsByDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListOTAModuleVersionsByDeviceResponse(),
            await self.do_request_async('ListOTAModuleVersionsByDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_otamodule_versions_by_device(
        self,
        request: iot_20180120_models.ListOTAModuleVersionsByDeviceRequest,
    ) -> iot_20180120_models.ListOTAModuleVersionsByDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_otamodule_versions_by_device_with_options(request, runtime)

    async def list_otamodule_versions_by_device_async(
        self,
        request: iot_20180120_models.ListOTAModuleVersionsByDeviceRequest,
    ) -> iot_20180120_models.ListOTAModuleVersionsByDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_otamodule_versions_by_device_with_options_async(request, runtime)

    def list_otatask_by_job_with_options(
        self,
        request: iot_20180120_models.ListOTATaskByJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListOTATaskByJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListOTATaskByJobResponse(),
            self.do_request('ListOTATaskByJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_otatask_by_job_with_options_async(
        self,
        request: iot_20180120_models.ListOTATaskByJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListOTATaskByJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListOTATaskByJobResponse(),
            await self.do_request_async('ListOTATaskByJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_otatask_by_job(
        self,
        request: iot_20180120_models.ListOTATaskByJobRequest,
    ) -> iot_20180120_models.ListOTATaskByJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_otatask_by_job_with_options(request, runtime)

    async def list_otatask_by_job_async(
        self,
        request: iot_20180120_models.ListOTATaskByJobRequest,
    ) -> iot_20180120_models.ListOTATaskByJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_otatask_by_job_with_options_async(request, runtime)

    def list_otaunfinished_task_by_device_with_options(
        self,
        request: iot_20180120_models.ListOTAUnfinishedTaskByDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListOTAUnfinishedTaskByDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListOTAUnfinishedTaskByDeviceResponse(),
            self.do_request('ListOTAUnfinishedTaskByDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_otaunfinished_task_by_device_with_options_async(
        self,
        request: iot_20180120_models.ListOTAUnfinishedTaskByDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListOTAUnfinishedTaskByDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListOTAUnfinishedTaskByDeviceResponse(),
            await self.do_request_async('ListOTAUnfinishedTaskByDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_otaunfinished_task_by_device(
        self,
        request: iot_20180120_models.ListOTAUnfinishedTaskByDeviceRequest,
    ) -> iot_20180120_models.ListOTAUnfinishedTaskByDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_otaunfinished_task_by_device_with_options(request, runtime)

    async def list_otaunfinished_task_by_device_async(
        self,
        request: iot_20180120_models.ListOTAUnfinishedTaskByDeviceRequest,
    ) -> iot_20180120_models.ListOTAUnfinishedTaskByDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_otaunfinished_task_by_device_with_options_async(request, runtime)

    def list_parser_with_options(
        self,
        request: iot_20180120_models.ListParserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListParserResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListParserResponse(),
            self.do_request('ListParser', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_parser_with_options_async(
        self,
        request: iot_20180120_models.ListParserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListParserResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListParserResponse(),
            await self.do_request_async('ListParser', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_parser(
        self,
        request: iot_20180120_models.ListParserRequest,
    ) -> iot_20180120_models.ListParserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_parser_with_options(request, runtime)

    async def list_parser_async(
        self,
        request: iot_20180120_models.ListParserRequest,
    ) -> iot_20180120_models.ListParserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_parser_with_options_async(request, runtime)

    def list_parser_data_source_with_options(
        self,
        request: iot_20180120_models.ListParserDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListParserDataSourceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListParserDataSourceResponse(),
            self.do_request('ListParserDataSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_parser_data_source_with_options_async(
        self,
        request: iot_20180120_models.ListParserDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListParserDataSourceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListParserDataSourceResponse(),
            await self.do_request_async('ListParserDataSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_parser_data_source(
        self,
        request: iot_20180120_models.ListParserDataSourceRequest,
    ) -> iot_20180120_models.ListParserDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_parser_data_source_with_options(request, runtime)

    async def list_parser_data_source_async(
        self,
        request: iot_20180120_models.ListParserDataSourceRequest,
    ) -> iot_20180120_models.ListParserDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_parser_data_source_with_options_async(request, runtime)

    def list_parser_destination_with_options(
        self,
        request: iot_20180120_models.ListParserDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListParserDestinationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListParserDestinationResponse(),
            self.do_request('ListParserDestination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_parser_destination_with_options_async(
        self,
        request: iot_20180120_models.ListParserDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListParserDestinationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListParserDestinationResponse(),
            await self.do_request_async('ListParserDestination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_parser_destination(
        self,
        request: iot_20180120_models.ListParserDestinationRequest,
    ) -> iot_20180120_models.ListParserDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_parser_destination_with_options(request, runtime)

    async def list_parser_destination_async(
        self,
        request: iot_20180120_models.ListParserDestinationRequest,
    ) -> iot_20180120_models.ListParserDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_parser_destination_with_options_async(request, runtime)

    def list_product_by_tags_with_options(
        self,
        request: iot_20180120_models.ListProductByTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListProductByTagsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListProductByTagsResponse(),
            self.do_request('ListProductByTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_product_by_tags_with_options_async(
        self,
        request: iot_20180120_models.ListProductByTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListProductByTagsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListProductByTagsResponse(),
            await self.do_request_async('ListProductByTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_product_by_tags(
        self,
        request: iot_20180120_models.ListProductByTagsRequest,
    ) -> iot_20180120_models.ListProductByTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_product_by_tags_with_options(request, runtime)

    async def list_product_by_tags_async(
        self,
        request: iot_20180120_models.ListProductByTagsRequest,
    ) -> iot_20180120_models.ListProductByTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_product_by_tags_with_options_async(request, runtime)

    def list_product_tags_with_options(
        self,
        request: iot_20180120_models.ListProductTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListProductTagsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListProductTagsResponse(),
            self.do_request('ListProductTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_product_tags_with_options_async(
        self,
        request: iot_20180120_models.ListProductTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListProductTagsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListProductTagsResponse(),
            await self.do_request_async('ListProductTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_product_tags(
        self,
        request: iot_20180120_models.ListProductTagsRequest,
    ) -> iot_20180120_models.ListProductTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_product_tags_with_options(request, runtime)

    async def list_product_tags_async(
        self,
        request: iot_20180120_models.ListProductTagsRequest,
    ) -> iot_20180120_models.ListProductTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_product_tags_with_options_async(request, runtime)

    def list_rule_with_options(
        self,
        request: iot_20180120_models.ListRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListRuleResponse(),
            self.do_request('ListRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_rule_with_options_async(
        self,
        request: iot_20180120_models.ListRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListRuleResponse(),
            await self.do_request_async('ListRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_rule(
        self,
        request: iot_20180120_models.ListRuleRequest,
    ) -> iot_20180120_models.ListRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_rule_with_options(request, runtime)

    async def list_rule_async(
        self,
        request: iot_20180120_models.ListRuleRequest,
    ) -> iot_20180120_models.ListRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_rule_with_options_async(request, runtime)

    def list_rule_actions_with_options(
        self,
        request: iot_20180120_models.ListRuleActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListRuleActionsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListRuleActionsResponse(),
            self.do_request('ListRuleActions', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_rule_actions_with_options_async(
        self,
        request: iot_20180120_models.ListRuleActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListRuleActionsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListRuleActionsResponse(),
            await self.do_request_async('ListRuleActions', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_rule_actions(
        self,
        request: iot_20180120_models.ListRuleActionsRequest,
    ) -> iot_20180120_models.ListRuleActionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_rule_actions_with_options(request, runtime)

    async def list_rule_actions_async(
        self,
        request: iot_20180120_models.ListRuleActionsRequest,
    ) -> iot_20180120_models.ListRuleActionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_rule_actions_with_options_async(request, runtime)

    def list_task_with_options(
        self,
        tmp: iot_20180120_models.ListTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListTaskResponse:
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.ListTaskShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.device):
            request.device_shrink = UtilClient.to_jsonstring(tmp.device)
        return TeaCore.from_map(
            iot_20180120_models.ListTaskResponse(),
            self.do_request('ListTask', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_task_with_options_async(
        self,
        tmp: iot_20180120_models.ListTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListTaskResponse:
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.ListTaskShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.device):
            request.device_shrink = UtilClient.to_jsonstring(tmp.device)
        return TeaCore.from_map(
            iot_20180120_models.ListTaskResponse(),
            await self.do_request_async('ListTask', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_task(
        self,
        request: iot_20180120_models.ListTaskRequest,
    ) -> iot_20180120_models.ListTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_task_with_options(request, runtime)

    async def list_task_async(
        self,
        request: iot_20180120_models.ListTaskRequest,
    ) -> iot_20180120_models.ListTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_task_with_options_async(request, runtime)

    def list_thing_model_version_with_options(
        self,
        request: iot_20180120_models.ListThingModelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListThingModelVersionResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListThingModelVersionResponse(),
            self.do_request('ListThingModelVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_thing_model_version_with_options_async(
        self,
        request: iot_20180120_models.ListThingModelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListThingModelVersionResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListThingModelVersionResponse(),
            await self.do_request_async('ListThingModelVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_thing_model_version(
        self,
        request: iot_20180120_models.ListThingModelVersionRequest,
    ) -> iot_20180120_models.ListThingModelVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_thing_model_version_with_options(request, runtime)

    async def list_thing_model_version_async(
        self,
        request: iot_20180120_models.ListThingModelVersionRequest,
    ) -> iot_20180120_models.ListThingModelVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_thing_model_version_with_options_async(request, runtime)

    def list_thing_templates_with_options(
        self,
        request: iot_20180120_models.ListThingTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListThingTemplatesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListThingTemplatesResponse(),
            self.do_request('ListThingTemplates', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_thing_templates_with_options_async(
        self,
        request: iot_20180120_models.ListThingTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListThingTemplatesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListThingTemplatesResponse(),
            await self.do_request_async('ListThingTemplates', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_thing_templates(
        self,
        request: iot_20180120_models.ListThingTemplatesRequest,
    ) -> iot_20180120_models.ListThingTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_thing_templates_with_options(request, runtime)

    async def list_thing_templates_async(
        self,
        request: iot_20180120_models.ListThingTemplatesRequest,
    ) -> iot_20180120_models.ListThingTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_thing_templates_with_options_async(request, runtime)

    def notify_add_thing_topo_with_options(
        self,
        request: iot_20180120_models.NotifyAddThingTopoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.NotifyAddThingTopoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.NotifyAddThingTopoResponse(),
            self.do_request('NotifyAddThingTopo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def notify_add_thing_topo_with_options_async(
        self,
        request: iot_20180120_models.NotifyAddThingTopoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.NotifyAddThingTopoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.NotifyAddThingTopoResponse(),
            await self.do_request_async('NotifyAddThingTopo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def notify_add_thing_topo(
        self,
        request: iot_20180120_models.NotifyAddThingTopoRequest,
    ) -> iot_20180120_models.NotifyAddThingTopoResponse:
        runtime = util_models.RuntimeOptions()
        return self.notify_add_thing_topo_with_options(request, runtime)

    async def notify_add_thing_topo_async(
        self,
        request: iot_20180120_models.NotifyAddThingTopoRequest,
    ) -> iot_20180120_models.NotifyAddThingTopoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.notify_add_thing_topo_with_options_async(request, runtime)

    def open_iot_service_with_options(
        self,
        request: iot_20180120_models.OpenIotServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.OpenIotServiceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.OpenIotServiceResponse(),
            self.do_request('OpenIotService', 'HTTPS', 'POST', '2018-01-20', 'AK,APP,PrivateKey,BearerToken', None, TeaCore.to_map(request), runtime)
        )

    async def open_iot_service_with_options_async(
        self,
        request: iot_20180120_models.OpenIotServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.OpenIotServiceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.OpenIotServiceResponse(),
            await self.do_request_async('OpenIotService', 'HTTPS', 'POST', '2018-01-20', 'AK,APP,PrivateKey,BearerToken', None, TeaCore.to_map(request), runtime)
        )

    def open_iot_service(
        self,
        request: iot_20180120_models.OpenIotServiceRequest,
    ) -> iot_20180120_models.OpenIotServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_iot_service_with_options(request, runtime)

    async def open_iot_service_async(
        self,
        request: iot_20180120_models.OpenIotServiceRequest,
    ) -> iot_20180120_models.OpenIotServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_iot_service_with_options_async(request, runtime)

    def package_sound_code_label_batch_audio_with_options(
        self,
        request: iot_20180120_models.PackageSoundCodeLabelBatchAudioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PackageSoundCodeLabelBatchAudioResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PackageSoundCodeLabelBatchAudioResponse(),
            self.do_request('PackageSoundCodeLabelBatchAudio', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def package_sound_code_label_batch_audio_with_options_async(
        self,
        request: iot_20180120_models.PackageSoundCodeLabelBatchAudioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PackageSoundCodeLabelBatchAudioResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PackageSoundCodeLabelBatchAudioResponse(),
            await self.do_request_async('PackageSoundCodeLabelBatchAudio', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def package_sound_code_label_batch_audio(
        self,
        request: iot_20180120_models.PackageSoundCodeLabelBatchAudioRequest,
    ) -> iot_20180120_models.PackageSoundCodeLabelBatchAudioResponse:
        runtime = util_models.RuntimeOptions()
        return self.package_sound_code_label_batch_audio_with_options(request, runtime)

    async def package_sound_code_label_batch_audio_async(
        self,
        request: iot_20180120_models.PackageSoundCodeLabelBatchAudioRequest,
    ) -> iot_20180120_models.PackageSoundCodeLabelBatchAudioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.package_sound_code_label_batch_audio_with_options_async(request, runtime)

    def page_query_shared_speech_open_with_options(
        self,
        request: iot_20180120_models.PageQuerySharedSpeechOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PageQuerySharedSpeechOpenResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PageQuerySharedSpeechOpenResponse(),
            self.do_request('PageQuerySharedSpeechOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def page_query_shared_speech_open_with_options_async(
        self,
        request: iot_20180120_models.PageQuerySharedSpeechOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PageQuerySharedSpeechOpenResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PageQuerySharedSpeechOpenResponse(),
            await self.do_request_async('PageQuerySharedSpeechOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def page_query_shared_speech_open(
        self,
        request: iot_20180120_models.PageQuerySharedSpeechOpenRequest,
    ) -> iot_20180120_models.PageQuerySharedSpeechOpenResponse:
        runtime = util_models.RuntimeOptions()
        return self.page_query_shared_speech_open_with_options(request, runtime)

    async def page_query_shared_speech_open_async(
        self,
        request: iot_20180120_models.PageQuerySharedSpeechOpenRequest,
    ) -> iot_20180120_models.PageQuerySharedSpeechOpenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.page_query_shared_speech_open_with_options_async(request, runtime)

    def page_query_speech_broadcast_hour_with_options(
        self,
        request: iot_20180120_models.PageQuerySpeechBroadcastHourRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PageQuerySpeechBroadcastHourResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PageQuerySpeechBroadcastHourResponse(),
            self.do_request('PageQuerySpeechBroadcastHour', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def page_query_speech_broadcast_hour_with_options_async(
        self,
        request: iot_20180120_models.PageQuerySpeechBroadcastHourRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PageQuerySpeechBroadcastHourResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PageQuerySpeechBroadcastHourResponse(),
            await self.do_request_async('PageQuerySpeechBroadcastHour', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def page_query_speech_broadcast_hour(
        self,
        request: iot_20180120_models.PageQuerySpeechBroadcastHourRequest,
    ) -> iot_20180120_models.PageQuerySpeechBroadcastHourResponse:
        runtime = util_models.RuntimeOptions()
        return self.page_query_speech_broadcast_hour_with_options(request, runtime)

    async def page_query_speech_broadcast_hour_async(
        self,
        request: iot_20180120_models.PageQuerySpeechBroadcastHourRequest,
    ) -> iot_20180120_models.PageQuerySpeechBroadcastHourResponse:
        runtime = util_models.RuntimeOptions()
        return await self.page_query_speech_broadcast_hour_with_options_async(request, runtime)

    def print_by_template_with_options(
        self,
        request: iot_20180120_models.PrintByTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PrintByTemplateResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PrintByTemplateResponse(),
            self.do_request('PrintByTemplate', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def print_by_template_with_options_async(
        self,
        request: iot_20180120_models.PrintByTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PrintByTemplateResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PrintByTemplateResponse(),
            await self.do_request_async('PrintByTemplate', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def print_by_template(
        self,
        request: iot_20180120_models.PrintByTemplateRequest,
    ) -> iot_20180120_models.PrintByTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.print_by_template_with_options(request, runtime)

    async def print_by_template_async(
        self,
        request: iot_20180120_models.PrintByTemplateRequest,
    ) -> iot_20180120_models.PrintByTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.print_by_template_with_options_async(request, runtime)

    def pub_with_options(
        self,
        request: iot_20180120_models.PubRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PubResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PubResponse(),
            self.do_request('Pub', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def pub_with_options_async(
        self,
        request: iot_20180120_models.PubRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PubResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PubResponse(),
            await self.do_request_async('Pub', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def pub(
        self,
        request: iot_20180120_models.PubRequest,
    ) -> iot_20180120_models.PubResponse:
        runtime = util_models.RuntimeOptions()
        return self.pub_with_options(request, runtime)

    async def pub_async(
        self,
        request: iot_20180120_models.PubRequest,
    ) -> iot_20180120_models.PubResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pub_with_options_async(request, runtime)

    def pub_broadcast_with_options(
        self,
        request: iot_20180120_models.PubBroadcastRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PubBroadcastResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PubBroadcastResponse(),
            self.do_request('PubBroadcast', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def pub_broadcast_with_options_async(
        self,
        request: iot_20180120_models.PubBroadcastRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PubBroadcastResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PubBroadcastResponse(),
            await self.do_request_async('PubBroadcast', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def pub_broadcast(
        self,
        request: iot_20180120_models.PubBroadcastRequest,
    ) -> iot_20180120_models.PubBroadcastResponse:
        runtime = util_models.RuntimeOptions()
        return self.pub_broadcast_with_options(request, runtime)

    async def pub_broadcast_async(
        self,
        request: iot_20180120_models.PubBroadcastRequest,
    ) -> iot_20180120_models.PubBroadcastResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pub_broadcast_with_options_async(request, runtime)

    def publish_script_with_options(
        self,
        request: iot_20180120_models.PublishScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PublishScriptResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PublishScriptResponse(),
            self.do_request('PublishScript', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def publish_script_with_options_async(
        self,
        request: iot_20180120_models.PublishScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PublishScriptResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PublishScriptResponse(),
            await self.do_request_async('PublishScript', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def publish_script(
        self,
        request: iot_20180120_models.PublishScriptRequest,
    ) -> iot_20180120_models.PublishScriptResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_script_with_options(request, runtime)

    async def publish_script_async(
        self,
        request: iot_20180120_models.PublishScriptRequest,
    ) -> iot_20180120_models.PublishScriptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_script_with_options_async(request, runtime)

    def publish_studio_app_with_options(
        self,
        request: iot_20180120_models.PublishStudioAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PublishStudioAppResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PublishStudioAppResponse(),
            self.do_request('PublishStudioApp', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def publish_studio_app_with_options_async(
        self,
        request: iot_20180120_models.PublishStudioAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PublishStudioAppResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PublishStudioAppResponse(),
            await self.do_request_async('PublishStudioApp', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def publish_studio_app(
        self,
        request: iot_20180120_models.PublishStudioAppRequest,
    ) -> iot_20180120_models.PublishStudioAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_studio_app_with_options(request, runtime)

    async def publish_studio_app_async(
        self,
        request: iot_20180120_models.PublishStudioAppRequest,
    ) -> iot_20180120_models.PublishStudioAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_studio_app_with_options_async(request, runtime)

    def publish_thing_model_with_options(
        self,
        request: iot_20180120_models.PublishThingModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PublishThingModelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PublishThingModelResponse(),
            self.do_request('PublishThingModel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def publish_thing_model_with_options_async(
        self,
        request: iot_20180120_models.PublishThingModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PublishThingModelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PublishThingModelResponse(),
            await self.do_request_async('PublishThingModel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def publish_thing_model(
        self,
        request: iot_20180120_models.PublishThingModelRequest,
    ) -> iot_20180120_models.PublishThingModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_thing_model_with_options(request, runtime)

    async def publish_thing_model_async(
        self,
        request: iot_20180120_models.PublishThingModelRequest,
    ) -> iot_20180120_models.PublishThingModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_thing_model_with_options_async(request, runtime)

    def push_speech_with_options(
        self,
        request: iot_20180120_models.PushSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PushSpeechResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PushSpeechResponse(),
            self.do_request('PushSpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def push_speech_with_options_async(
        self,
        request: iot_20180120_models.PushSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PushSpeechResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PushSpeechResponse(),
            await self.do_request_async('PushSpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def push_speech(
        self,
        request: iot_20180120_models.PushSpeechRequest,
    ) -> iot_20180120_models.PushSpeechResponse:
        runtime = util_models.RuntimeOptions()
        return self.push_speech_with_options(request, runtime)

    async def push_speech_async(
        self,
        request: iot_20180120_models.PushSpeechRequest,
    ) -> iot_20180120_models.PushSpeechResponse:
        runtime = util_models.RuntimeOptions()
        return await self.push_speech_with_options_async(request, runtime)

    def query_batch_register_device_status_with_options(
        self,
        request: iot_20180120_models.QueryBatchRegisterDeviceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryBatchRegisterDeviceStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryBatchRegisterDeviceStatusResponse(),
            self.do_request('QueryBatchRegisterDeviceStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_batch_register_device_status_with_options_async(
        self,
        request: iot_20180120_models.QueryBatchRegisterDeviceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryBatchRegisterDeviceStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryBatchRegisterDeviceStatusResponse(),
            await self.do_request_async('QueryBatchRegisterDeviceStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_batch_register_device_status(
        self,
        request: iot_20180120_models.QueryBatchRegisterDeviceStatusRequest,
    ) -> iot_20180120_models.QueryBatchRegisterDeviceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_batch_register_device_status_with_options(request, runtime)

    async def query_batch_register_device_status_async(
        self,
        request: iot_20180120_models.QueryBatchRegisterDeviceStatusRequest,
    ) -> iot_20180120_models.QueryBatchRegisterDeviceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_batch_register_device_status_with_options_async(request, runtime)

    def query_cert_url_by_apply_id_with_options(
        self,
        request: iot_20180120_models.QueryCertUrlByApplyIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryCertUrlByApplyIdResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryCertUrlByApplyIdResponse(),
            self.do_request('QueryCertUrlByApplyId', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_cert_url_by_apply_id_with_options_async(
        self,
        request: iot_20180120_models.QueryCertUrlByApplyIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryCertUrlByApplyIdResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryCertUrlByApplyIdResponse(),
            await self.do_request_async('QueryCertUrlByApplyId', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_cert_url_by_apply_id(
        self,
        request: iot_20180120_models.QueryCertUrlByApplyIdRequest,
    ) -> iot_20180120_models.QueryCertUrlByApplyIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_cert_url_by_apply_id_with_options(request, runtime)

    async def query_cert_url_by_apply_id_async(
        self,
        request: iot_20180120_models.QueryCertUrlByApplyIdRequest,
    ) -> iot_20180120_models.QueryCertUrlByApplyIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_cert_url_by_apply_id_with_options_async(request, runtime)

    def query_client_ids_with_options(
        self,
        request: iot_20180120_models.QueryClientIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryClientIdsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryClientIdsResponse(),
            self.do_request('QueryClientIds', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_client_ids_with_options_async(
        self,
        request: iot_20180120_models.QueryClientIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryClientIdsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryClientIdsResponse(),
            await self.do_request_async('QueryClientIds', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_client_ids(
        self,
        request: iot_20180120_models.QueryClientIdsRequest,
    ) -> iot_20180120_models.QueryClientIdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_client_ids_with_options(request, runtime)

    async def query_client_ids_async(
        self,
        request: iot_20180120_models.QueryClientIdsRequest,
    ) -> iot_20180120_models.QueryClientIdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_client_ids_with_options_async(request, runtime)

    def query_consumer_group_by_group_id_with_options(
        self,
        request: iot_20180120_models.QueryConsumerGroupByGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryConsumerGroupByGroupIdResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryConsumerGroupByGroupIdResponse(),
            self.do_request('QueryConsumerGroupByGroupId', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_consumer_group_by_group_id_with_options_async(
        self,
        request: iot_20180120_models.QueryConsumerGroupByGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryConsumerGroupByGroupIdResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryConsumerGroupByGroupIdResponse(),
            await self.do_request_async('QueryConsumerGroupByGroupId', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_consumer_group_by_group_id(
        self,
        request: iot_20180120_models.QueryConsumerGroupByGroupIdRequest,
    ) -> iot_20180120_models.QueryConsumerGroupByGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_consumer_group_by_group_id_with_options(request, runtime)

    async def query_consumer_group_by_group_id_async(
        self,
        request: iot_20180120_models.QueryConsumerGroupByGroupIdRequest,
    ) -> iot_20180120_models.QueryConsumerGroupByGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_consumer_group_by_group_id_with_options_async(request, runtime)

    def query_consumer_group_list_with_options(
        self,
        request: iot_20180120_models.QueryConsumerGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryConsumerGroupListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryConsumerGroupListResponse(),
            self.do_request('QueryConsumerGroupList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_consumer_group_list_with_options_async(
        self,
        request: iot_20180120_models.QueryConsumerGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryConsumerGroupListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryConsumerGroupListResponse(),
            await self.do_request_async('QueryConsumerGroupList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_consumer_group_list(
        self,
        request: iot_20180120_models.QueryConsumerGroupListRequest,
    ) -> iot_20180120_models.QueryConsumerGroupListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_consumer_group_list_with_options(request, runtime)

    async def query_consumer_group_list_async(
        self,
        request: iot_20180120_models.QueryConsumerGroupListRequest,
    ) -> iot_20180120_models.QueryConsumerGroupListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_consumer_group_list_with_options_async(request, runtime)

    def query_consumer_group_status_with_options(
        self,
        request: iot_20180120_models.QueryConsumerGroupStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryConsumerGroupStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryConsumerGroupStatusResponse(),
            self.do_request('QueryConsumerGroupStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_consumer_group_status_with_options_async(
        self,
        request: iot_20180120_models.QueryConsumerGroupStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryConsumerGroupStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryConsumerGroupStatusResponse(),
            await self.do_request_async('QueryConsumerGroupStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_consumer_group_status(
        self,
        request: iot_20180120_models.QueryConsumerGroupStatusRequest,
    ) -> iot_20180120_models.QueryConsumerGroupStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_consumer_group_status_with_options(request, runtime)

    async def query_consumer_group_status_async(
        self,
        request: iot_20180120_models.QueryConsumerGroupStatusRequest,
    ) -> iot_20180120_models.QueryConsumerGroupStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_consumer_group_status_with_options_async(request, runtime)

    def query_detail_scene_rule_log_with_options(
        self,
        request: iot_20180120_models.QueryDetailSceneRuleLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDetailSceneRuleLogResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDetailSceneRuleLogResponse(),
            self.do_request('QueryDetailSceneRuleLog', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_detail_scene_rule_log_with_options_async(
        self,
        request: iot_20180120_models.QueryDetailSceneRuleLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDetailSceneRuleLogResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDetailSceneRuleLogResponse(),
            await self.do_request_async('QueryDetailSceneRuleLog', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_detail_scene_rule_log(
        self,
        request: iot_20180120_models.QueryDetailSceneRuleLogRequest,
    ) -> iot_20180120_models.QueryDetailSceneRuleLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_detail_scene_rule_log_with_options(request, runtime)

    async def query_detail_scene_rule_log_async(
        self,
        request: iot_20180120_models.QueryDetailSceneRuleLogRequest,
    ) -> iot_20180120_models.QueryDetailSceneRuleLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_detail_scene_rule_log_with_options_async(request, runtime)

    def query_device_with_options(
        self,
        request: iot_20180120_models.QueryDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceResponse(),
            self.do_request('QueryDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceResponse(),
            await self.do_request_async('QueryDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device(
        self,
        request: iot_20180120_models.QueryDeviceRequest,
    ) -> iot_20180120_models.QueryDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_with_options(request, runtime)

    async def query_device_async(
        self,
        request: iot_20180120_models.QueryDeviceRequest,
    ) -> iot_20180120_models.QueryDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_with_options_async(request, runtime)

    def query_device_by_sqlwith_options(
        self,
        request: iot_20180120_models.QueryDeviceBySQLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceBySQLResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceBySQLResponse(),
            self.do_request('QueryDeviceBySQL', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_by_sqlwith_options_async(
        self,
        request: iot_20180120_models.QueryDeviceBySQLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceBySQLResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceBySQLResponse(),
            await self.do_request_async('QueryDeviceBySQL', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_by_sql(
        self,
        request: iot_20180120_models.QueryDeviceBySQLRequest,
    ) -> iot_20180120_models.QueryDeviceBySQLResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_by_sqlwith_options(request, runtime)

    async def query_device_by_sql_async(
        self,
        request: iot_20180120_models.QueryDeviceBySQLRequest,
    ) -> iot_20180120_models.QueryDeviceBySQLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_by_sqlwith_options_async(request, runtime)

    def query_device_by_status_with_options(
        self,
        request: iot_20180120_models.QueryDeviceByStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceByStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceByStatusResponse(),
            self.do_request('QueryDeviceByStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_by_status_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceByStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceByStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceByStatusResponse(),
            await self.do_request_async('QueryDeviceByStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_by_status(
        self,
        request: iot_20180120_models.QueryDeviceByStatusRequest,
    ) -> iot_20180120_models.QueryDeviceByStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_by_status_with_options(request, runtime)

    async def query_device_by_status_async(
        self,
        request: iot_20180120_models.QueryDeviceByStatusRequest,
    ) -> iot_20180120_models.QueryDeviceByStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_by_status_with_options_async(request, runtime)

    def query_device_by_tags_with_options(
        self,
        request: iot_20180120_models.QueryDeviceByTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceByTagsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceByTagsResponse(),
            self.do_request('QueryDeviceByTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_by_tags_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceByTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceByTagsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceByTagsResponse(),
            await self.do_request_async('QueryDeviceByTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_by_tags(
        self,
        request: iot_20180120_models.QueryDeviceByTagsRequest,
    ) -> iot_20180120_models.QueryDeviceByTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_by_tags_with_options(request, runtime)

    async def query_device_by_tags_async(
        self,
        request: iot_20180120_models.QueryDeviceByTagsRequest,
    ) -> iot_20180120_models.QueryDeviceByTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_by_tags_with_options_async(request, runtime)

    def query_device_cert_with_options(
        self,
        request: iot_20180120_models.QueryDeviceCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceCertResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceCertResponse(),
            self.do_request('QueryDeviceCert', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_cert_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceCertResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceCertResponse(),
            await self.do_request_async('QueryDeviceCert', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_cert(
        self,
        request: iot_20180120_models.QueryDeviceCertRequest,
    ) -> iot_20180120_models.QueryDeviceCertResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_cert_with_options(request, runtime)

    async def query_device_cert_async(
        self,
        request: iot_20180120_models.QueryDeviceCertRequest,
    ) -> iot_20180120_models.QueryDeviceCertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_cert_with_options_async(request, runtime)

    def query_device_desired_property_with_options(
        self,
        request: iot_20180120_models.QueryDeviceDesiredPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceDesiredPropertyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceDesiredPropertyResponse(),
            self.do_request('QueryDeviceDesiredProperty', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_desired_property_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceDesiredPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceDesiredPropertyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceDesiredPropertyResponse(),
            await self.do_request_async('QueryDeviceDesiredProperty', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_desired_property(
        self,
        request: iot_20180120_models.QueryDeviceDesiredPropertyRequest,
    ) -> iot_20180120_models.QueryDeviceDesiredPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_desired_property_with_options(request, runtime)

    async def query_device_desired_property_async(
        self,
        request: iot_20180120_models.QueryDeviceDesiredPropertyRequest,
    ) -> iot_20180120_models.QueryDeviceDesiredPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_desired_property_with_options_async(request, runtime)

    def query_device_detail_with_options(
        self,
        request: iot_20180120_models.QueryDeviceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceDetailResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceDetailResponse(),
            self.do_request('QueryDeviceDetail', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_detail_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceDetailResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceDetailResponse(),
            await self.do_request_async('QueryDeviceDetail', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_detail(
        self,
        request: iot_20180120_models.QueryDeviceDetailRequest,
    ) -> iot_20180120_models.QueryDeviceDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_detail_with_options(request, runtime)

    async def query_device_detail_async(
        self,
        request: iot_20180120_models.QueryDeviceDetailRequest,
    ) -> iot_20180120_models.QueryDeviceDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_detail_with_options_async(request, runtime)

    def query_device_distribute_detail_with_options(
        self,
        request: iot_20180120_models.QueryDeviceDistributeDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceDistributeDetailResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceDistributeDetailResponse(),
            self.do_request('QueryDeviceDistributeDetail', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_distribute_detail_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceDistributeDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceDistributeDetailResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceDistributeDetailResponse(),
            await self.do_request_async('QueryDeviceDistributeDetail', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_distribute_detail(
        self,
        request: iot_20180120_models.QueryDeviceDistributeDetailRequest,
    ) -> iot_20180120_models.QueryDeviceDistributeDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_distribute_detail_with_options(request, runtime)

    async def query_device_distribute_detail_async(
        self,
        request: iot_20180120_models.QueryDeviceDistributeDetailRequest,
    ) -> iot_20180120_models.QueryDeviceDistributeDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_distribute_detail_with_options_async(request, runtime)

    def query_device_distribute_job_with_options(
        self,
        request: iot_20180120_models.QueryDeviceDistributeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceDistributeJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceDistributeJobResponse(),
            self.do_request('QueryDeviceDistributeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_distribute_job_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceDistributeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceDistributeJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceDistributeJobResponse(),
            await self.do_request_async('QueryDeviceDistributeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_distribute_job(
        self,
        request: iot_20180120_models.QueryDeviceDistributeJobRequest,
    ) -> iot_20180120_models.QueryDeviceDistributeJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_distribute_job_with_options(request, runtime)

    async def query_device_distribute_job_async(
        self,
        request: iot_20180120_models.QueryDeviceDistributeJobRequest,
    ) -> iot_20180120_models.QueryDeviceDistributeJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_distribute_job_with_options_async(request, runtime)

    def query_device_event_data_with_options(
        self,
        request: iot_20180120_models.QueryDeviceEventDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceEventDataResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceEventDataResponse(),
            self.do_request('QueryDeviceEventData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_event_data_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceEventDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceEventDataResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceEventDataResponse(),
            await self.do_request_async('QueryDeviceEventData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_event_data(
        self,
        request: iot_20180120_models.QueryDeviceEventDataRequest,
    ) -> iot_20180120_models.QueryDeviceEventDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_event_data_with_options(request, runtime)

    async def query_device_event_data_async(
        self,
        request: iot_20180120_models.QueryDeviceEventDataRequest,
    ) -> iot_20180120_models.QueryDeviceEventDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_event_data_with_options_async(request, runtime)

    def query_device_file_with_options(
        self,
        request: iot_20180120_models.QueryDeviceFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceFileResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceFileResponse(),
            self.do_request('QueryDeviceFile', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_file_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceFileResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceFileResponse(),
            await self.do_request_async('QueryDeviceFile', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_file(
        self,
        request: iot_20180120_models.QueryDeviceFileRequest,
    ) -> iot_20180120_models.QueryDeviceFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_file_with_options(request, runtime)

    async def query_device_file_async(
        self,
        request: iot_20180120_models.QueryDeviceFileRequest,
    ) -> iot_20180120_models.QueryDeviceFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_file_with_options_async(request, runtime)

    def query_device_file_list_with_options(
        self,
        request: iot_20180120_models.QueryDeviceFileListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceFileListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceFileListResponse(),
            self.do_request('QueryDeviceFileList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_file_list_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceFileListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceFileListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceFileListResponse(),
            await self.do_request_async('QueryDeviceFileList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_file_list(
        self,
        request: iot_20180120_models.QueryDeviceFileListRequest,
    ) -> iot_20180120_models.QueryDeviceFileListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_file_list_with_options(request, runtime)

    async def query_device_file_list_async(
        self,
        request: iot_20180120_models.QueryDeviceFileListRequest,
    ) -> iot_20180120_models.QueryDeviceFileListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_file_list_with_options_async(request, runtime)

    def query_device_group_by_device_with_options(
        self,
        request: iot_20180120_models.QueryDeviceGroupByDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceGroupByDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupByDeviceResponse(),
            self.do_request('QueryDeviceGroupByDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_group_by_device_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceGroupByDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceGroupByDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupByDeviceResponse(),
            await self.do_request_async('QueryDeviceGroupByDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_group_by_device(
        self,
        request: iot_20180120_models.QueryDeviceGroupByDeviceRequest,
    ) -> iot_20180120_models.QueryDeviceGroupByDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_group_by_device_with_options(request, runtime)

    async def query_device_group_by_device_async(
        self,
        request: iot_20180120_models.QueryDeviceGroupByDeviceRequest,
    ) -> iot_20180120_models.QueryDeviceGroupByDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_group_by_device_with_options_async(request, runtime)

    def query_device_group_by_tags_with_options(
        self,
        request: iot_20180120_models.QueryDeviceGroupByTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceGroupByTagsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupByTagsResponse(),
            self.do_request('QueryDeviceGroupByTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_group_by_tags_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceGroupByTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceGroupByTagsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupByTagsResponse(),
            await self.do_request_async('QueryDeviceGroupByTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_group_by_tags(
        self,
        request: iot_20180120_models.QueryDeviceGroupByTagsRequest,
    ) -> iot_20180120_models.QueryDeviceGroupByTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_group_by_tags_with_options(request, runtime)

    async def query_device_group_by_tags_async(
        self,
        request: iot_20180120_models.QueryDeviceGroupByTagsRequest,
    ) -> iot_20180120_models.QueryDeviceGroupByTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_group_by_tags_with_options_async(request, runtime)

    def query_device_group_info_with_options(
        self,
        request: iot_20180120_models.QueryDeviceGroupInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceGroupInfoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupInfoResponse(),
            self.do_request('QueryDeviceGroupInfo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_group_info_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceGroupInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceGroupInfoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupInfoResponse(),
            await self.do_request_async('QueryDeviceGroupInfo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_group_info(
        self,
        request: iot_20180120_models.QueryDeviceGroupInfoRequest,
    ) -> iot_20180120_models.QueryDeviceGroupInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_group_info_with_options(request, runtime)

    async def query_device_group_info_async(
        self,
        request: iot_20180120_models.QueryDeviceGroupInfoRequest,
    ) -> iot_20180120_models.QueryDeviceGroupInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_group_info_with_options_async(request, runtime)

    def query_device_group_list_with_options(
        self,
        request: iot_20180120_models.QueryDeviceGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceGroupListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupListResponse(),
            self.do_request('QueryDeviceGroupList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_group_list_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceGroupListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupListResponse(),
            await self.do_request_async('QueryDeviceGroupList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_group_list(
        self,
        request: iot_20180120_models.QueryDeviceGroupListRequest,
    ) -> iot_20180120_models.QueryDeviceGroupListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_group_list_with_options(request, runtime)

    async def query_device_group_list_async(
        self,
        request: iot_20180120_models.QueryDeviceGroupListRequest,
    ) -> iot_20180120_models.QueryDeviceGroupListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_group_list_with_options_async(request, runtime)

    def query_device_group_tag_list_with_options(
        self,
        request: iot_20180120_models.QueryDeviceGroupTagListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceGroupTagListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupTagListResponse(),
            self.do_request('QueryDeviceGroupTagList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_group_tag_list_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceGroupTagListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceGroupTagListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupTagListResponse(),
            await self.do_request_async('QueryDeviceGroupTagList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_group_tag_list(
        self,
        request: iot_20180120_models.QueryDeviceGroupTagListRequest,
    ) -> iot_20180120_models.QueryDeviceGroupTagListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_group_tag_list_with_options(request, runtime)

    async def query_device_group_tag_list_async(
        self,
        request: iot_20180120_models.QueryDeviceGroupTagListRequest,
    ) -> iot_20180120_models.QueryDeviceGroupTagListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_group_tag_list_with_options_async(request, runtime)

    def query_device_info_with_options(
        self,
        request: iot_20180120_models.QueryDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceInfoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceInfoResponse(),
            self.do_request('QueryDeviceInfo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_info_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceInfoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceInfoResponse(),
            await self.do_request_async('QueryDeviceInfo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_info(
        self,
        request: iot_20180120_models.QueryDeviceInfoRequest,
    ) -> iot_20180120_models.QueryDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_info_with_options(request, runtime)

    async def query_device_info_async(
        self,
        request: iot_20180120_models.QueryDeviceInfoRequest,
    ) -> iot_20180120_models.QueryDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_info_with_options_async(request, runtime)

    def query_device_list_by_device_group_with_options(
        self,
        request: iot_20180120_models.QueryDeviceListByDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceListByDeviceGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceListByDeviceGroupResponse(),
            self.do_request('QueryDeviceListByDeviceGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_list_by_device_group_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceListByDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceListByDeviceGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceListByDeviceGroupResponse(),
            await self.do_request_async('QueryDeviceListByDeviceGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_list_by_device_group(
        self,
        request: iot_20180120_models.QueryDeviceListByDeviceGroupRequest,
    ) -> iot_20180120_models.QueryDeviceListByDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_list_by_device_group_with_options(request, runtime)

    async def query_device_list_by_device_group_async(
        self,
        request: iot_20180120_models.QueryDeviceListByDeviceGroupRequest,
    ) -> iot_20180120_models.QueryDeviceListByDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_list_by_device_group_with_options_async(request, runtime)

    def query_device_original_event_data_with_options(
        self,
        request: iot_20180120_models.QueryDeviceOriginalEventDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceOriginalEventDataResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceOriginalEventDataResponse(),
            self.do_request('QueryDeviceOriginalEventData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_original_event_data_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceOriginalEventDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceOriginalEventDataResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceOriginalEventDataResponse(),
            await self.do_request_async('QueryDeviceOriginalEventData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_original_event_data(
        self,
        request: iot_20180120_models.QueryDeviceOriginalEventDataRequest,
    ) -> iot_20180120_models.QueryDeviceOriginalEventDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_original_event_data_with_options(request, runtime)

    async def query_device_original_event_data_async(
        self,
        request: iot_20180120_models.QueryDeviceOriginalEventDataRequest,
    ) -> iot_20180120_models.QueryDeviceOriginalEventDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_original_event_data_with_options_async(request, runtime)

    def query_device_original_property_data_with_options(
        self,
        request: iot_20180120_models.QueryDeviceOriginalPropertyDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceOriginalPropertyDataResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceOriginalPropertyDataResponse(),
            self.do_request('QueryDeviceOriginalPropertyData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_original_property_data_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceOriginalPropertyDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceOriginalPropertyDataResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceOriginalPropertyDataResponse(),
            await self.do_request_async('QueryDeviceOriginalPropertyData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_original_property_data(
        self,
        request: iot_20180120_models.QueryDeviceOriginalPropertyDataRequest,
    ) -> iot_20180120_models.QueryDeviceOriginalPropertyDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_original_property_data_with_options(request, runtime)

    async def query_device_original_property_data_async(
        self,
        request: iot_20180120_models.QueryDeviceOriginalPropertyDataRequest,
    ) -> iot_20180120_models.QueryDeviceOriginalPropertyDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_original_property_data_with_options_async(request, runtime)

    def query_device_original_property_status_with_options(
        self,
        request: iot_20180120_models.QueryDeviceOriginalPropertyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceOriginalPropertyStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceOriginalPropertyStatusResponse(),
            self.do_request('QueryDeviceOriginalPropertyStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_original_property_status_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceOriginalPropertyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceOriginalPropertyStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceOriginalPropertyStatusResponse(),
            await self.do_request_async('QueryDeviceOriginalPropertyStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_original_property_status(
        self,
        request: iot_20180120_models.QueryDeviceOriginalPropertyStatusRequest,
    ) -> iot_20180120_models.QueryDeviceOriginalPropertyStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_original_property_status_with_options(request, runtime)

    async def query_device_original_property_status_async(
        self,
        request: iot_20180120_models.QueryDeviceOriginalPropertyStatusRequest,
    ) -> iot_20180120_models.QueryDeviceOriginalPropertyStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_original_property_status_with_options_async(request, runtime)

    def query_device_original_service_data_with_options(
        self,
        request: iot_20180120_models.QueryDeviceOriginalServiceDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceOriginalServiceDataResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceOriginalServiceDataResponse(),
            self.do_request('QueryDeviceOriginalServiceData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_original_service_data_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceOriginalServiceDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceOriginalServiceDataResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceOriginalServiceDataResponse(),
            await self.do_request_async('QueryDeviceOriginalServiceData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_original_service_data(
        self,
        request: iot_20180120_models.QueryDeviceOriginalServiceDataRequest,
    ) -> iot_20180120_models.QueryDeviceOriginalServiceDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_original_service_data_with_options(request, runtime)

    async def query_device_original_service_data_async(
        self,
        request: iot_20180120_models.QueryDeviceOriginalServiceDataRequest,
    ) -> iot_20180120_models.QueryDeviceOriginalServiceDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_original_service_data_with_options_async(request, runtime)

    def query_device_prop_with_options(
        self,
        request: iot_20180120_models.QueryDevicePropRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDevicePropResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicePropResponse(),
            self.do_request('QueryDeviceProp', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_prop_with_options_async(
        self,
        request: iot_20180120_models.QueryDevicePropRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDevicePropResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicePropResponse(),
            await self.do_request_async('QueryDeviceProp', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_prop(
        self,
        request: iot_20180120_models.QueryDevicePropRequest,
    ) -> iot_20180120_models.QueryDevicePropResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_prop_with_options(request, runtime)

    async def query_device_prop_async(
        self,
        request: iot_20180120_models.QueryDevicePropRequest,
    ) -> iot_20180120_models.QueryDevicePropResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_prop_with_options_async(request, runtime)

    def query_device_properties_data_with_options(
        self,
        request: iot_20180120_models.QueryDevicePropertiesDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDevicePropertiesDataResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicePropertiesDataResponse(),
            self.do_request('QueryDevicePropertiesData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_properties_data_with_options_async(
        self,
        request: iot_20180120_models.QueryDevicePropertiesDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDevicePropertiesDataResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicePropertiesDataResponse(),
            await self.do_request_async('QueryDevicePropertiesData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_properties_data(
        self,
        request: iot_20180120_models.QueryDevicePropertiesDataRequest,
    ) -> iot_20180120_models.QueryDevicePropertiesDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_properties_data_with_options(request, runtime)

    async def query_device_properties_data_async(
        self,
        request: iot_20180120_models.QueryDevicePropertiesDataRequest,
    ) -> iot_20180120_models.QueryDevicePropertiesDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_properties_data_with_options_async(request, runtime)

    def query_device_property_data_with_options(
        self,
        request: iot_20180120_models.QueryDevicePropertyDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDevicePropertyDataResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicePropertyDataResponse(),
            self.do_request('QueryDevicePropertyData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_property_data_with_options_async(
        self,
        request: iot_20180120_models.QueryDevicePropertyDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDevicePropertyDataResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicePropertyDataResponse(),
            await self.do_request_async('QueryDevicePropertyData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_property_data(
        self,
        request: iot_20180120_models.QueryDevicePropertyDataRequest,
    ) -> iot_20180120_models.QueryDevicePropertyDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_property_data_with_options(request, runtime)

    async def query_device_property_data_async(
        self,
        request: iot_20180120_models.QueryDevicePropertyDataRequest,
    ) -> iot_20180120_models.QueryDevicePropertyDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_property_data_with_options_async(request, runtime)

    def query_device_property_status_with_options(
        self,
        request: iot_20180120_models.QueryDevicePropertyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDevicePropertyStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicePropertyStatusResponse(),
            self.do_request('QueryDevicePropertyStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_property_status_with_options_async(
        self,
        request: iot_20180120_models.QueryDevicePropertyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDevicePropertyStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicePropertyStatusResponse(),
            await self.do_request_async('QueryDevicePropertyStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_property_status(
        self,
        request: iot_20180120_models.QueryDevicePropertyStatusRequest,
    ) -> iot_20180120_models.QueryDevicePropertyStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_property_status_with_options(request, runtime)

    async def query_device_property_status_async(
        self,
        request: iot_20180120_models.QueryDevicePropertyStatusRequest,
    ) -> iot_20180120_models.QueryDevicePropertyStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_property_status_with_options_async(request, runtime)

    def query_device_service_data_with_options(
        self,
        request: iot_20180120_models.QueryDeviceServiceDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceServiceDataResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceServiceDataResponse(),
            self.do_request('QueryDeviceServiceData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_service_data_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceServiceDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceServiceDataResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceServiceDataResponse(),
            await self.do_request_async('QueryDeviceServiceData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_service_data(
        self,
        request: iot_20180120_models.QueryDeviceServiceDataRequest,
    ) -> iot_20180120_models.QueryDeviceServiceDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_service_data_with_options(request, runtime)

    async def query_device_service_data_async(
        self,
        request: iot_20180120_models.QueryDeviceServiceDataRequest,
    ) -> iot_20180120_models.QueryDeviceServiceDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_service_data_with_options_async(request, runtime)

    def query_device_speech_with_options(
        self,
        request: iot_20180120_models.QueryDeviceSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceSpeechResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceSpeechResponse(),
            self.do_request('QueryDeviceSpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_speech_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceSpeechResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceSpeechResponse(),
            await self.do_request_async('QueryDeviceSpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_speech(
        self,
        request: iot_20180120_models.QueryDeviceSpeechRequest,
    ) -> iot_20180120_models.QueryDeviceSpeechResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_speech_with_options(request, runtime)

    async def query_device_speech_async(
        self,
        request: iot_20180120_models.QueryDeviceSpeechRequest,
    ) -> iot_20180120_models.QueryDeviceSpeechResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_speech_with_options_async(request, runtime)

    def query_device_statistics_with_options(
        self,
        request: iot_20180120_models.QueryDeviceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceStatisticsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceStatisticsResponse(),
            self.do_request('QueryDeviceStatistics', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_statistics_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceStatisticsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceStatisticsResponse(),
            await self.do_request_async('QueryDeviceStatistics', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_statistics(
        self,
        request: iot_20180120_models.QueryDeviceStatisticsRequest,
    ) -> iot_20180120_models.QueryDeviceStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_statistics_with_options(request, runtime)

    async def query_device_statistics_async(
        self,
        request: iot_20180120_models.QueryDeviceStatisticsRequest,
    ) -> iot_20180120_models.QueryDeviceStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_statistics_with_options_async(request, runtime)

    def query_device_sub_topic_with_options(
        self,
        request: iot_20180120_models.QueryDeviceSubTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceSubTopicResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceSubTopicResponse(),
            self.do_request('QueryDeviceSubTopic', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_sub_topic_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceSubTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceSubTopicResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceSubTopicResponse(),
            await self.do_request_async('QueryDeviceSubTopic', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_sub_topic(
        self,
        request: iot_20180120_models.QueryDeviceSubTopicRequest,
    ) -> iot_20180120_models.QueryDeviceSubTopicResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_sub_topic_with_options(request, runtime)

    async def query_device_sub_topic_async(
        self,
        request: iot_20180120_models.QueryDeviceSubTopicRequest,
    ) -> iot_20180120_models.QueryDeviceSubTopicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_sub_topic_with_options_async(request, runtime)

    def query_device_tunnel_with_options(
        self,
        request: iot_20180120_models.QueryDeviceTunnelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceTunnelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceTunnelResponse(),
            self.do_request('QueryDeviceTunnel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_device_tunnel_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceTunnelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceTunnelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceTunnelResponse(),
            await self.do_request_async('QueryDeviceTunnel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_tunnel(
        self,
        request: iot_20180120_models.QueryDeviceTunnelRequest,
    ) -> iot_20180120_models.QueryDeviceTunnelResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_tunnel_with_options(request, runtime)

    async def query_device_tunnel_async(
        self,
        request: iot_20180120_models.QueryDeviceTunnelRequest,
    ) -> iot_20180120_models.QueryDeviceTunnelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_tunnel_with_options_async(request, runtime)

    def query_devices_hot_storage_data_with_options(
        self,
        request: iot_20180120_models.QueryDevicesHotStorageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDevicesHotStorageDataResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicesHotStorageDataResponse(),
            self.do_request('QueryDevicesHotStorageData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_devices_hot_storage_data_with_options_async(
        self,
        request: iot_20180120_models.QueryDevicesHotStorageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDevicesHotStorageDataResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicesHotStorageDataResponse(),
            await self.do_request_async('QueryDevicesHotStorageData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_devices_hot_storage_data(
        self,
        request: iot_20180120_models.QueryDevicesHotStorageDataRequest,
    ) -> iot_20180120_models.QueryDevicesHotStorageDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_devices_hot_storage_data_with_options(request, runtime)

    async def query_devices_hot_storage_data_async(
        self,
        request: iot_20180120_models.QueryDevicesHotStorageDataRequest,
    ) -> iot_20180120_models.QueryDevicesHotStorageDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_devices_hot_storage_data_with_options_async(request, runtime)

    def query_devices_hot_storage_data_status_with_options(
        self,
        request: iot_20180120_models.QueryDevicesHotStorageDataStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDevicesHotStorageDataStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicesHotStorageDataStatusResponse(),
            self.do_request('QueryDevicesHotStorageDataStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_devices_hot_storage_data_status_with_options_async(
        self,
        request: iot_20180120_models.QueryDevicesHotStorageDataStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDevicesHotStorageDataStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicesHotStorageDataStatusResponse(),
            await self.do_request_async('QueryDevicesHotStorageDataStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_devices_hot_storage_data_status(
        self,
        request: iot_20180120_models.QueryDevicesHotStorageDataStatusRequest,
    ) -> iot_20180120_models.QueryDevicesHotStorageDataStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_devices_hot_storage_data_status_with_options(request, runtime)

    async def query_devices_hot_storage_data_status_async(
        self,
        request: iot_20180120_models.QueryDevicesHotStorageDataStatusRequest,
    ) -> iot_20180120_models.QueryDevicesHotStorageDataStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_devices_hot_storage_data_status_with_options_async(request, runtime)

    def query_dynamic_group_devices_with_options(
        self,
        request: iot_20180120_models.QueryDynamicGroupDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDynamicGroupDevicesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDynamicGroupDevicesResponse(),
            self.do_request('QueryDynamicGroupDevices', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_dynamic_group_devices_with_options_async(
        self,
        request: iot_20180120_models.QueryDynamicGroupDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDynamicGroupDevicesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDynamicGroupDevicesResponse(),
            await self.do_request_async('QueryDynamicGroupDevices', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_dynamic_group_devices(
        self,
        request: iot_20180120_models.QueryDynamicGroupDevicesRequest,
    ) -> iot_20180120_models.QueryDynamicGroupDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_dynamic_group_devices_with_options(request, runtime)

    async def query_dynamic_group_devices_async(
        self,
        request: iot_20180120_models.QueryDynamicGroupDevicesRequest,
    ) -> iot_20180120_models.QueryDynamicGroupDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_dynamic_group_devices_with_options_async(request, runtime)

    def query_edge_driver_with_options(
        self,
        request: iot_20180120_models.QueryEdgeDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeDriverResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeDriverResponse(),
            self.do_request('QueryEdgeDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_edge_driver_with_options_async(
        self,
        request: iot_20180120_models.QueryEdgeDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeDriverResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeDriverResponse(),
            await self.do_request_async('QueryEdgeDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_driver(
        self,
        request: iot_20180120_models.QueryEdgeDriverRequest,
    ) -> iot_20180120_models.QueryEdgeDriverResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_edge_driver_with_options(request, runtime)

    async def query_edge_driver_async(
        self,
        request: iot_20180120_models.QueryEdgeDriverRequest,
    ) -> iot_20180120_models.QueryEdgeDriverResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_edge_driver_with_options_async(request, runtime)

    def query_edge_driver_version_with_options(
        self,
        request: iot_20180120_models.QueryEdgeDriverVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeDriverVersionResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeDriverVersionResponse(),
            self.do_request('QueryEdgeDriverVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_edge_driver_version_with_options_async(
        self,
        request: iot_20180120_models.QueryEdgeDriverVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeDriverVersionResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeDriverVersionResponse(),
            await self.do_request_async('QueryEdgeDriverVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_driver_version(
        self,
        request: iot_20180120_models.QueryEdgeDriverVersionRequest,
    ) -> iot_20180120_models.QueryEdgeDriverVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_edge_driver_version_with_options(request, runtime)

    async def query_edge_driver_version_async(
        self,
        request: iot_20180120_models.QueryEdgeDriverVersionRequest,
    ) -> iot_20180120_models.QueryEdgeDriverVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_edge_driver_version_with_options_async(request, runtime)

    def query_edge_instance_with_options(
        self,
        request: iot_20180120_models.QueryEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceResponse(),
            self.do_request('QueryEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceResponse(),
            await self.do_request_async('QueryEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance(
        self,
        request: iot_20180120_models.QueryEdgeInstanceRequest,
    ) -> iot_20180120_models.QueryEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_with_options(request, runtime)

    async def query_edge_instance_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceRequest,
    ) -> iot_20180120_models.QueryEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_edge_instance_with_options_async(request, runtime)

    def query_edge_instance_channel_with_options(
        self,
        request: iot_20180120_models.QueryEdgeInstanceChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceChannelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceChannelResponse(),
            self.do_request('QueryEdgeInstanceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_edge_instance_channel_with_options_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceChannelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceChannelResponse(),
            await self.do_request_async('QueryEdgeInstanceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance_channel(
        self,
        request: iot_20180120_models.QueryEdgeInstanceChannelRequest,
    ) -> iot_20180120_models.QueryEdgeInstanceChannelResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_channel_with_options(request, runtime)

    async def query_edge_instance_channel_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceChannelRequest,
    ) -> iot_20180120_models.QueryEdgeInstanceChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_edge_instance_channel_with_options_async(request, runtime)

    def query_edge_instance_device_with_options(
        self,
        request: iot_20180120_models.QueryEdgeInstanceDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceDeviceResponse(),
            self.do_request('QueryEdgeInstanceDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_edge_instance_device_with_options_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceDeviceResponse(),
            await self.do_request_async('QueryEdgeInstanceDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance_device(
        self,
        request: iot_20180120_models.QueryEdgeInstanceDeviceRequest,
    ) -> iot_20180120_models.QueryEdgeInstanceDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_device_with_options(request, runtime)

    async def query_edge_instance_device_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceDeviceRequest,
    ) -> iot_20180120_models.QueryEdgeInstanceDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_edge_instance_device_with_options_async(request, runtime)

    def query_edge_instance_device_by_driver_with_options(
        self,
        request: iot_20180120_models.QueryEdgeInstanceDeviceByDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceDeviceByDriverResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceDeviceByDriverResponse(),
            self.do_request('QueryEdgeInstanceDeviceByDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_edge_instance_device_by_driver_with_options_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceDeviceByDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceDeviceByDriverResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceDeviceByDriverResponse(),
            await self.do_request_async('QueryEdgeInstanceDeviceByDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance_device_by_driver(
        self,
        request: iot_20180120_models.QueryEdgeInstanceDeviceByDriverRequest,
    ) -> iot_20180120_models.QueryEdgeInstanceDeviceByDriverResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_device_by_driver_with_options(request, runtime)

    async def query_edge_instance_device_by_driver_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceDeviceByDriverRequest,
    ) -> iot_20180120_models.QueryEdgeInstanceDeviceByDriverResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_edge_instance_device_by_driver_with_options_async(request, runtime)

    def query_edge_instance_driver_with_options(
        self,
        request: iot_20180120_models.QueryEdgeInstanceDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceDriverResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceDriverResponse(),
            self.do_request('QueryEdgeInstanceDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_edge_instance_driver_with_options_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceDriverResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceDriverResponse(),
            await self.do_request_async('QueryEdgeInstanceDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance_driver(
        self,
        request: iot_20180120_models.QueryEdgeInstanceDriverRequest,
    ) -> iot_20180120_models.QueryEdgeInstanceDriverResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_driver_with_options(request, runtime)

    async def query_edge_instance_driver_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceDriverRequest,
    ) -> iot_20180120_models.QueryEdgeInstanceDriverResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_edge_instance_driver_with_options_async(request, runtime)

    def query_edge_instance_gateway_with_options(
        self,
        request: iot_20180120_models.QueryEdgeInstanceGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceGatewayResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceGatewayResponse(),
            self.do_request('QueryEdgeInstanceGateway', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_edge_instance_gateway_with_options_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceGatewayResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceGatewayResponse(),
            await self.do_request_async('QueryEdgeInstanceGateway', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance_gateway(
        self,
        request: iot_20180120_models.QueryEdgeInstanceGatewayRequest,
    ) -> iot_20180120_models.QueryEdgeInstanceGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_gateway_with_options(request, runtime)

    async def query_edge_instance_gateway_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceGatewayRequest,
    ) -> iot_20180120_models.QueryEdgeInstanceGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_edge_instance_gateway_with_options_async(request, runtime)

    def query_edge_instance_historic_deployment_with_options(
        self,
        request: iot_20180120_models.QueryEdgeInstanceHistoricDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceHistoricDeploymentResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceHistoricDeploymentResponse(),
            self.do_request('QueryEdgeInstanceHistoricDeployment', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_edge_instance_historic_deployment_with_options_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceHistoricDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceHistoricDeploymentResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceHistoricDeploymentResponse(),
            await self.do_request_async('QueryEdgeInstanceHistoricDeployment', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance_historic_deployment(
        self,
        request: iot_20180120_models.QueryEdgeInstanceHistoricDeploymentRequest,
    ) -> iot_20180120_models.QueryEdgeInstanceHistoricDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_historic_deployment_with_options(request, runtime)

    async def query_edge_instance_historic_deployment_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceHistoricDeploymentRequest,
    ) -> iot_20180120_models.QueryEdgeInstanceHistoricDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_edge_instance_historic_deployment_with_options_async(request, runtime)

    def query_edge_instance_message_routing_with_options(
        self,
        request: iot_20180120_models.QueryEdgeInstanceMessageRoutingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceMessageRoutingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceMessageRoutingResponse(),
            self.do_request('QueryEdgeInstanceMessageRouting', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_edge_instance_message_routing_with_options_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceMessageRoutingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceMessageRoutingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceMessageRoutingResponse(),
            await self.do_request_async('QueryEdgeInstanceMessageRouting', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance_message_routing(
        self,
        request: iot_20180120_models.QueryEdgeInstanceMessageRoutingRequest,
    ) -> iot_20180120_models.QueryEdgeInstanceMessageRoutingResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_message_routing_with_options(request, runtime)

    async def query_edge_instance_message_routing_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceMessageRoutingRequest,
    ) -> iot_20180120_models.QueryEdgeInstanceMessageRoutingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_edge_instance_message_routing_with_options_async(request, runtime)

    def query_edge_instance_scene_rule_with_options(
        self,
        request: iot_20180120_models.QueryEdgeInstanceSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceSceneRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceSceneRuleResponse(),
            self.do_request('QueryEdgeInstanceSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_edge_instance_scene_rule_with_options_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceSceneRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceSceneRuleResponse(),
            await self.do_request_async('QueryEdgeInstanceSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance_scene_rule(
        self,
        request: iot_20180120_models.QueryEdgeInstanceSceneRuleRequest,
    ) -> iot_20180120_models.QueryEdgeInstanceSceneRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_scene_rule_with_options(request, runtime)

    async def query_edge_instance_scene_rule_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceSceneRuleRequest,
    ) -> iot_20180120_models.QueryEdgeInstanceSceneRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_edge_instance_scene_rule_with_options_async(request, runtime)

    def query_imported_device_by_apply_id_with_options(
        self,
        request: iot_20180120_models.QueryImportedDeviceByApplyIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryImportedDeviceByApplyIdResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryImportedDeviceByApplyIdResponse(),
            self.do_request('QueryImportedDeviceByApplyId', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_imported_device_by_apply_id_with_options_async(
        self,
        request: iot_20180120_models.QueryImportedDeviceByApplyIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryImportedDeviceByApplyIdResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryImportedDeviceByApplyIdResponse(),
            await self.do_request_async('QueryImportedDeviceByApplyId', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_imported_device_by_apply_id(
        self,
        request: iot_20180120_models.QueryImportedDeviceByApplyIdRequest,
    ) -> iot_20180120_models.QueryImportedDeviceByApplyIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_imported_device_by_apply_id_with_options(request, runtime)

    async def query_imported_device_by_apply_id_async(
        self,
        request: iot_20180120_models.QueryImportedDeviceByApplyIdRequest,
    ) -> iot_20180120_models.QueryImportedDeviceByApplyIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_imported_device_by_apply_id_with_options_async(request, runtime)

    def query_job_with_options(
        self,
        request: iot_20180120_models.QueryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryJobResponse(),
            self.do_request('QueryJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_job_with_options_async(
        self,
        request: iot_20180120_models.QueryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryJobResponse(),
            await self.do_request_async('QueryJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_job(
        self,
        request: iot_20180120_models.QueryJobRequest,
    ) -> iot_20180120_models.QueryJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_job_with_options(request, runtime)

    async def query_job_async(
        self,
        request: iot_20180120_models.QueryJobRequest,
    ) -> iot_20180120_models.QueryJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_job_with_options_async(request, runtime)

    def query_job_statistics_with_options(
        self,
        request: iot_20180120_models.QueryJobStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryJobStatisticsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryJobStatisticsResponse(),
            self.do_request('QueryJobStatistics', 'HTTPS', 'GET', '2018-01-20', 'AK', TeaCore.to_map(request), None, runtime)
        )

    async def query_job_statistics_with_options_async(
        self,
        request: iot_20180120_models.QueryJobStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryJobStatisticsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryJobStatisticsResponse(),
            await self.do_request_async('QueryJobStatistics', 'HTTPS', 'GET', '2018-01-20', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def query_job_statistics(
        self,
        request: iot_20180120_models.QueryJobStatisticsRequest,
    ) -> iot_20180120_models.QueryJobStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_job_statistics_with_options(request, runtime)

    async def query_job_statistics_async(
        self,
        request: iot_20180120_models.QueryJobStatisticsRequest,
    ) -> iot_20180120_models.QueryJobStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_job_statistics_with_options_async(request, runtime)

    def query_license_device_list_with_options(
        self,
        request: iot_20180120_models.QueryLicenseDeviceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryLicenseDeviceListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryLicenseDeviceListResponse(),
            self.do_request('QueryLicenseDeviceList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_license_device_list_with_options_async(
        self,
        request: iot_20180120_models.QueryLicenseDeviceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryLicenseDeviceListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryLicenseDeviceListResponse(),
            await self.do_request_async('QueryLicenseDeviceList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_license_device_list(
        self,
        request: iot_20180120_models.QueryLicenseDeviceListRequest,
    ) -> iot_20180120_models.QueryLicenseDeviceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_license_device_list_with_options(request, runtime)

    async def query_license_device_list_async(
        self,
        request: iot_20180120_models.QueryLicenseDeviceListRequest,
    ) -> iot_20180120_models.QueryLicenseDeviceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_license_device_list_with_options_async(request, runtime)

    def query_lo_ra_join_permissions_with_options(
        self,
        request: iot_20180120_models.QueryLoRaJoinPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryLoRaJoinPermissionsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryLoRaJoinPermissionsResponse(),
            self.do_request('QueryLoRaJoinPermissions', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_lo_ra_join_permissions_with_options_async(
        self,
        request: iot_20180120_models.QueryLoRaJoinPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryLoRaJoinPermissionsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryLoRaJoinPermissionsResponse(),
            await self.do_request_async('QueryLoRaJoinPermissions', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_lo_ra_join_permissions(
        self,
        request: iot_20180120_models.QueryLoRaJoinPermissionsRequest,
    ) -> iot_20180120_models.QueryLoRaJoinPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_lo_ra_join_permissions_with_options(request, runtime)

    async def query_lo_ra_join_permissions_async(
        self,
        request: iot_20180120_models.QueryLoRaJoinPermissionsRequest,
    ) -> iot_20180120_models.QueryLoRaJoinPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_lo_ra_join_permissions_with_options_async(request, runtime)

    def query_message_info_with_options(
        self,
        request: iot_20180120_models.QueryMessageInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryMessageInfoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryMessageInfoResponse(),
            self.do_request('QueryMessageInfo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_message_info_with_options_async(
        self,
        request: iot_20180120_models.QueryMessageInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryMessageInfoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryMessageInfoResponse(),
            await self.do_request_async('QueryMessageInfo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_message_info(
        self,
        request: iot_20180120_models.QueryMessageInfoRequest,
    ) -> iot_20180120_models.QueryMessageInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_message_info_with_options(request, runtime)

    async def query_message_info_async(
        self,
        request: iot_20180120_models.QueryMessageInfoRequest,
    ) -> iot_20180120_models.QueryMessageInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_message_info_with_options_async(request, runtime)

    def query_otafirmware_with_options(
        self,
        request: iot_20180120_models.QueryOTAFirmwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryOTAFirmwareResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryOTAFirmwareResponse(),
            self.do_request('QueryOTAFirmware', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_otafirmware_with_options_async(
        self,
        request: iot_20180120_models.QueryOTAFirmwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryOTAFirmwareResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryOTAFirmwareResponse(),
            await self.do_request_async('QueryOTAFirmware', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_otafirmware(
        self,
        request: iot_20180120_models.QueryOTAFirmwareRequest,
    ) -> iot_20180120_models.QueryOTAFirmwareResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_otafirmware_with_options(request, runtime)

    async def query_otafirmware_async(
        self,
        request: iot_20180120_models.QueryOTAFirmwareRequest,
    ) -> iot_20180120_models.QueryOTAFirmwareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_otafirmware_with_options_async(request, runtime)

    def query_otajob_with_options(
        self,
        request: iot_20180120_models.QueryOTAJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryOTAJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryOTAJobResponse(),
            self.do_request('QueryOTAJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_otajob_with_options_async(
        self,
        request: iot_20180120_models.QueryOTAJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryOTAJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryOTAJobResponse(),
            await self.do_request_async('QueryOTAJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_otajob(
        self,
        request: iot_20180120_models.QueryOTAJobRequest,
    ) -> iot_20180120_models.QueryOTAJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_otajob_with_options(request, runtime)

    async def query_otajob_async(
        self,
        request: iot_20180120_models.QueryOTAJobRequest,
    ) -> iot_20180120_models.QueryOTAJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_otajob_with_options_async(request, runtime)

    def query_page_by_apply_id_with_options(
        self,
        request: iot_20180120_models.QueryPageByApplyIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryPageByApplyIdResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryPageByApplyIdResponse(),
            self.do_request('QueryPageByApplyId', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_page_by_apply_id_with_options_async(
        self,
        request: iot_20180120_models.QueryPageByApplyIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryPageByApplyIdResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryPageByApplyIdResponse(),
            await self.do_request_async('QueryPageByApplyId', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_page_by_apply_id(
        self,
        request: iot_20180120_models.QueryPageByApplyIdRequest,
    ) -> iot_20180120_models.QueryPageByApplyIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_page_by_apply_id_with_options(request, runtime)

    async def query_page_by_apply_id_async(
        self,
        request: iot_20180120_models.QueryPageByApplyIdRequest,
    ) -> iot_20180120_models.QueryPageByApplyIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_page_by_apply_id_with_options_async(request, runtime)

    def query_product_with_options(
        self,
        request: iot_20180120_models.QueryProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryProductResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryProductResponse(),
            self.do_request('QueryProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_product_with_options_async(
        self,
        request: iot_20180120_models.QueryProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryProductResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryProductResponse(),
            await self.do_request_async('QueryProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_product(
        self,
        request: iot_20180120_models.QueryProductRequest,
    ) -> iot_20180120_models.QueryProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_product_with_options(request, runtime)

    async def query_product_async(
        self,
        request: iot_20180120_models.QueryProductRequest,
    ) -> iot_20180120_models.QueryProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_product_with_options_async(request, runtime)

    def query_product_cert_info_with_options(
        self,
        request: iot_20180120_models.QueryProductCertInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryProductCertInfoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryProductCertInfoResponse(),
            self.do_request('QueryProductCertInfo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_product_cert_info_with_options_async(
        self,
        request: iot_20180120_models.QueryProductCertInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryProductCertInfoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryProductCertInfoResponse(),
            await self.do_request_async('QueryProductCertInfo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_product_cert_info(
        self,
        request: iot_20180120_models.QueryProductCertInfoRequest,
    ) -> iot_20180120_models.QueryProductCertInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_product_cert_info_with_options(request, runtime)

    async def query_product_cert_info_async(
        self,
        request: iot_20180120_models.QueryProductCertInfoRequest,
    ) -> iot_20180120_models.QueryProductCertInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_product_cert_info_with_options_async(request, runtime)

    def query_product_list_with_options(
        self,
        request: iot_20180120_models.QueryProductListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryProductListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryProductListResponse(),
            self.do_request('QueryProductList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_product_list_with_options_async(
        self,
        request: iot_20180120_models.QueryProductListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryProductListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryProductListResponse(),
            await self.do_request_async('QueryProductList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_product_list(
        self,
        request: iot_20180120_models.QueryProductListRequest,
    ) -> iot_20180120_models.QueryProductListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_product_list_with_options(request, runtime)

    async def query_product_list_async(
        self,
        request: iot_20180120_models.QueryProductListRequest,
    ) -> iot_20180120_models.QueryProductListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_product_list_with_options_async(request, runtime)

    def query_product_topic_with_options(
        self,
        request: iot_20180120_models.QueryProductTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryProductTopicResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryProductTopicResponse(),
            self.do_request('QueryProductTopic', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_product_topic_with_options_async(
        self,
        request: iot_20180120_models.QueryProductTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryProductTopicResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryProductTopicResponse(),
            await self.do_request_async('QueryProductTopic', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_product_topic(
        self,
        request: iot_20180120_models.QueryProductTopicRequest,
    ) -> iot_20180120_models.QueryProductTopicResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_product_topic_with_options(request, runtime)

    async def query_product_topic_async(
        self,
        request: iot_20180120_models.QueryProductTopicRequest,
    ) -> iot_20180120_models.QueryProductTopicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_product_topic_with_options_async(request, runtime)

    def query_project_share_device_list_with_options(
        self,
        request: iot_20180120_models.QueryProjectShareDeviceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryProjectShareDeviceListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryProjectShareDeviceListResponse(),
            self.do_request('QueryProjectShareDeviceList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_project_share_device_list_with_options_async(
        self,
        request: iot_20180120_models.QueryProjectShareDeviceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryProjectShareDeviceListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryProjectShareDeviceListResponse(),
            await self.do_request_async('QueryProjectShareDeviceList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_project_share_device_list(
        self,
        request: iot_20180120_models.QueryProjectShareDeviceListRequest,
    ) -> iot_20180120_models.QueryProjectShareDeviceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_project_share_device_list_with_options(request, runtime)

    async def query_project_share_device_list_async(
        self,
        request: iot_20180120_models.QueryProjectShareDeviceListRequest,
    ) -> iot_20180120_models.QueryProjectShareDeviceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_project_share_device_list_with_options_async(request, runtime)

    def query_scene_rule_with_options(
        self,
        request: iot_20180120_models.QuerySceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySceneRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySceneRuleResponse(),
            self.do_request('QuerySceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_scene_rule_with_options_async(
        self,
        request: iot_20180120_models.QuerySceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySceneRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySceneRuleResponse(),
            await self.do_request_async('QuerySceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_scene_rule(
        self,
        request: iot_20180120_models.QuerySceneRuleRequest,
    ) -> iot_20180120_models.QuerySceneRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_scene_rule_with_options(request, runtime)

    async def query_scene_rule_async(
        self,
        request: iot_20180120_models.QuerySceneRuleRequest,
    ) -> iot_20180120_models.QuerySceneRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_scene_rule_with_options_async(request, runtime)

    def query_schedule_period_list_with_options(
        self,
        request: iot_20180120_models.QuerySchedulePeriodListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySchedulePeriodListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySchedulePeriodListResponse(),
            self.do_request('QuerySchedulePeriodList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_schedule_period_list_with_options_async(
        self,
        request: iot_20180120_models.QuerySchedulePeriodListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySchedulePeriodListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySchedulePeriodListResponse(),
            await self.do_request_async('QuerySchedulePeriodList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_schedule_period_list(
        self,
        request: iot_20180120_models.QuerySchedulePeriodListRequest,
    ) -> iot_20180120_models.QuerySchedulePeriodListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_schedule_period_list_with_options(request, runtime)

    async def query_schedule_period_list_async(
        self,
        request: iot_20180120_models.QuerySchedulePeriodListRequest,
    ) -> iot_20180120_models.QuerySchedulePeriodListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_schedule_period_list_with_options_async(request, runtime)

    def query_share_task_device_list_with_options(
        self,
        request: iot_20180120_models.QueryShareTaskDeviceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryShareTaskDeviceListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryShareTaskDeviceListResponse(),
            self.do_request('QueryShareTaskDeviceList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_share_task_device_list_with_options_async(
        self,
        request: iot_20180120_models.QueryShareTaskDeviceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryShareTaskDeviceListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryShareTaskDeviceListResponse(),
            await self.do_request_async('QueryShareTaskDeviceList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_share_task_device_list(
        self,
        request: iot_20180120_models.QueryShareTaskDeviceListRequest,
    ) -> iot_20180120_models.QueryShareTaskDeviceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_share_task_device_list_with_options(request, runtime)

    async def query_share_task_device_list_async(
        self,
        request: iot_20180120_models.QueryShareTaskDeviceListRequest,
    ) -> iot_20180120_models.QueryShareTaskDeviceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_share_task_device_list_with_options_async(request, runtime)

    def query_solution_device_group_page_with_options(
        self,
        request: iot_20180120_models.QuerySolutionDeviceGroupPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySolutionDeviceGroupPageResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySolutionDeviceGroupPageResponse(),
            self.do_request('QuerySolutionDeviceGroupPage', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_solution_device_group_page_with_options_async(
        self,
        request: iot_20180120_models.QuerySolutionDeviceGroupPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySolutionDeviceGroupPageResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySolutionDeviceGroupPageResponse(),
            await self.do_request_async('QuerySolutionDeviceGroupPage', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_solution_device_group_page(
        self,
        request: iot_20180120_models.QuerySolutionDeviceGroupPageRequest,
    ) -> iot_20180120_models.QuerySolutionDeviceGroupPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_solution_device_group_page_with_options(request, runtime)

    async def query_solution_device_group_page_async(
        self,
        request: iot_20180120_models.QuerySolutionDeviceGroupPageRequest,
    ) -> iot_20180120_models.QuerySolutionDeviceGroupPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_solution_device_group_page_with_options_async(request, runtime)

    def query_sound_code_label_batch_failed_result_with_options(
        self,
        request: iot_20180120_models.QuerySoundCodeLabelBatchFailedResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySoundCodeLabelBatchFailedResultResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySoundCodeLabelBatchFailedResultResponse(),
            self.do_request('QuerySoundCodeLabelBatchFailedResult', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_sound_code_label_batch_failed_result_with_options_async(
        self,
        request: iot_20180120_models.QuerySoundCodeLabelBatchFailedResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySoundCodeLabelBatchFailedResultResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySoundCodeLabelBatchFailedResultResponse(),
            await self.do_request_async('QuerySoundCodeLabelBatchFailedResult', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_sound_code_label_batch_failed_result(
        self,
        request: iot_20180120_models.QuerySoundCodeLabelBatchFailedResultRequest,
    ) -> iot_20180120_models.QuerySoundCodeLabelBatchFailedResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_sound_code_label_batch_failed_result_with_options(request, runtime)

    async def query_sound_code_label_batch_failed_result_async(
        self,
        request: iot_20180120_models.QuerySoundCodeLabelBatchFailedResultRequest,
    ) -> iot_20180120_models.QuerySoundCodeLabelBatchFailedResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_sound_code_label_batch_failed_result_with_options_async(request, runtime)

    def query_sound_code_label_batch_list_with_options(
        self,
        request: iot_20180120_models.QuerySoundCodeLabelBatchListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySoundCodeLabelBatchListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySoundCodeLabelBatchListResponse(),
            self.do_request('QuerySoundCodeLabelBatchList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_sound_code_label_batch_list_with_options_async(
        self,
        request: iot_20180120_models.QuerySoundCodeLabelBatchListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySoundCodeLabelBatchListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySoundCodeLabelBatchListResponse(),
            await self.do_request_async('QuerySoundCodeLabelBatchList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_sound_code_label_batch_list(
        self,
        request: iot_20180120_models.QuerySoundCodeLabelBatchListRequest,
    ) -> iot_20180120_models.QuerySoundCodeLabelBatchListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_sound_code_label_batch_list_with_options(request, runtime)

    async def query_sound_code_label_batch_list_async(
        self,
        request: iot_20180120_models.QuerySoundCodeLabelBatchListRequest,
    ) -> iot_20180120_models.QuerySoundCodeLabelBatchListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_sound_code_label_batch_list_with_options_async(request, runtime)

    def query_sound_code_label_list_with_options(
        self,
        request: iot_20180120_models.QuerySoundCodeLabelListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySoundCodeLabelListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySoundCodeLabelListResponse(),
            self.do_request('QuerySoundCodeLabelList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_sound_code_label_list_with_options_async(
        self,
        request: iot_20180120_models.QuerySoundCodeLabelListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySoundCodeLabelListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySoundCodeLabelListResponse(),
            await self.do_request_async('QuerySoundCodeLabelList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_sound_code_label_list(
        self,
        request: iot_20180120_models.QuerySoundCodeLabelListRequest,
    ) -> iot_20180120_models.QuerySoundCodeLabelListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_sound_code_label_list_with_options(request, runtime)

    async def query_sound_code_label_list_async(
        self,
        request: iot_20180120_models.QuerySoundCodeLabelListRequest,
    ) -> iot_20180120_models.QuerySoundCodeLabelListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_sound_code_label_list_with_options_async(request, runtime)

    def query_sound_code_list_with_options(
        self,
        request: iot_20180120_models.QuerySoundCodeListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySoundCodeListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySoundCodeListResponse(),
            self.do_request('QuerySoundCodeList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_sound_code_list_with_options_async(
        self,
        request: iot_20180120_models.QuerySoundCodeListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySoundCodeListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySoundCodeListResponse(),
            await self.do_request_async('QuerySoundCodeList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_sound_code_list(
        self,
        request: iot_20180120_models.QuerySoundCodeListRequest,
    ) -> iot_20180120_models.QuerySoundCodeListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_sound_code_list_with_options(request, runtime)

    async def query_sound_code_list_async(
        self,
        request: iot_20180120_models.QuerySoundCodeListRequest,
    ) -> iot_20180120_models.QuerySoundCodeListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_sound_code_list_with_options_async(request, runtime)

    def query_sound_code_schedule_list_with_options(
        self,
        request: iot_20180120_models.QuerySoundCodeScheduleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySoundCodeScheduleListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySoundCodeScheduleListResponse(),
            self.do_request('QuerySoundCodeScheduleList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_sound_code_schedule_list_with_options_async(
        self,
        request: iot_20180120_models.QuerySoundCodeScheduleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySoundCodeScheduleListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySoundCodeScheduleListResponse(),
            await self.do_request_async('QuerySoundCodeScheduleList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_sound_code_schedule_list(
        self,
        request: iot_20180120_models.QuerySoundCodeScheduleListRequest,
    ) -> iot_20180120_models.QuerySoundCodeScheduleListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_sound_code_schedule_list_with_options(request, runtime)

    async def query_sound_code_schedule_list_async(
        self,
        request: iot_20180120_models.QuerySoundCodeScheduleListRequest,
    ) -> iot_20180120_models.QuerySoundCodeScheduleListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_sound_code_schedule_list_with_options_async(request, runtime)

    def query_speech_with_options(
        self,
        request: iot_20180120_models.QuerySpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySpeechResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechResponse(),
            self.do_request('QuerySpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_speech_with_options_async(
        self,
        request: iot_20180120_models.QuerySpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySpeechResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechResponse(),
            await self.do_request_async('QuerySpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_speech(
        self,
        request: iot_20180120_models.QuerySpeechRequest,
    ) -> iot_20180120_models.QuerySpeechResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_speech_with_options(request, runtime)

    async def query_speech_async(
        self,
        request: iot_20180120_models.QuerySpeechRequest,
    ) -> iot_20180120_models.QuerySpeechResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_speech_with_options_async(request, runtime)

    def query_speech_device_with_options(
        self,
        request: iot_20180120_models.QuerySpeechDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySpeechDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechDeviceResponse(),
            self.do_request('QuerySpeechDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_speech_device_with_options_async(
        self,
        request: iot_20180120_models.QuerySpeechDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySpeechDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechDeviceResponse(),
            await self.do_request_async('QuerySpeechDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_speech_device(
        self,
        request: iot_20180120_models.QuerySpeechDeviceRequest,
    ) -> iot_20180120_models.QuerySpeechDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_speech_device_with_options(request, runtime)

    async def query_speech_device_async(
        self,
        request: iot_20180120_models.QuerySpeechDeviceRequest,
    ) -> iot_20180120_models.QuerySpeechDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_speech_device_with_options_async(request, runtime)

    def query_speech_license_device_list_with_options(
        self,
        request: iot_20180120_models.QuerySpeechLicenseDeviceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySpeechLicenseDeviceListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechLicenseDeviceListResponse(),
            self.do_request('QuerySpeechLicenseDeviceList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_speech_license_device_list_with_options_async(
        self,
        request: iot_20180120_models.QuerySpeechLicenseDeviceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySpeechLicenseDeviceListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechLicenseDeviceListResponse(),
            await self.do_request_async('QuerySpeechLicenseDeviceList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_speech_license_device_list(
        self,
        request: iot_20180120_models.QuerySpeechLicenseDeviceListRequest,
    ) -> iot_20180120_models.QuerySpeechLicenseDeviceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_speech_license_device_list_with_options(request, runtime)

    async def query_speech_license_device_list_async(
        self,
        request: iot_20180120_models.QuerySpeechLicenseDeviceListRequest,
    ) -> iot_20180120_models.QuerySpeechLicenseDeviceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_speech_license_device_list_with_options_async(request, runtime)

    def query_speech_list_with_options(
        self,
        request: iot_20180120_models.QuerySpeechListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySpeechListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechListResponse(),
            self.do_request('QuerySpeechList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_speech_list_with_options_async(
        self,
        request: iot_20180120_models.QuerySpeechListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySpeechListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechListResponse(),
            await self.do_request_async('QuerySpeechList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_speech_list(
        self,
        request: iot_20180120_models.QuerySpeechListRequest,
    ) -> iot_20180120_models.QuerySpeechListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_speech_list_with_options(request, runtime)

    async def query_speech_list_async(
        self,
        request: iot_20180120_models.QuerySpeechListRequest,
    ) -> iot_20180120_models.QuerySpeechListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_speech_list_with_options_async(request, runtime)

    def query_speech_push_job_with_options(
        self,
        request: iot_20180120_models.QuerySpeechPushJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySpeechPushJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechPushJobResponse(),
            self.do_request('QuerySpeechPushJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_speech_push_job_with_options_async(
        self,
        request: iot_20180120_models.QuerySpeechPushJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySpeechPushJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechPushJobResponse(),
            await self.do_request_async('QuerySpeechPushJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_speech_push_job(
        self,
        request: iot_20180120_models.QuerySpeechPushJobRequest,
    ) -> iot_20180120_models.QuerySpeechPushJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_speech_push_job_with_options(request, runtime)

    async def query_speech_push_job_async(
        self,
        request: iot_20180120_models.QuerySpeechPushJobRequest,
    ) -> iot_20180120_models.QuerySpeechPushJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_speech_push_job_with_options_async(request, runtime)

    def query_speech_push_job_device_with_options(
        self,
        request: iot_20180120_models.QuerySpeechPushJobDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySpeechPushJobDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechPushJobDeviceResponse(),
            self.do_request('QuerySpeechPushJobDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_speech_push_job_device_with_options_async(
        self,
        request: iot_20180120_models.QuerySpeechPushJobDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySpeechPushJobDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechPushJobDeviceResponse(),
            await self.do_request_async('QuerySpeechPushJobDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_speech_push_job_device(
        self,
        request: iot_20180120_models.QuerySpeechPushJobDeviceRequest,
    ) -> iot_20180120_models.QuerySpeechPushJobDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_speech_push_job_device_with_options(request, runtime)

    async def query_speech_push_job_device_async(
        self,
        request: iot_20180120_models.QuerySpeechPushJobDeviceRequest,
    ) -> iot_20180120_models.QuerySpeechPushJobDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_speech_push_job_device_with_options_async(request, runtime)

    def query_speech_push_job_speech_with_options(
        self,
        request: iot_20180120_models.QuerySpeechPushJobSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySpeechPushJobSpeechResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechPushJobSpeechResponse(),
            self.do_request('QuerySpeechPushJobSpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_speech_push_job_speech_with_options_async(
        self,
        request: iot_20180120_models.QuerySpeechPushJobSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySpeechPushJobSpeechResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechPushJobSpeechResponse(),
            await self.do_request_async('QuerySpeechPushJobSpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_speech_push_job_speech(
        self,
        request: iot_20180120_models.QuerySpeechPushJobSpeechRequest,
    ) -> iot_20180120_models.QuerySpeechPushJobSpeechResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_speech_push_job_speech_with_options(request, runtime)

    async def query_speech_push_job_speech_async(
        self,
        request: iot_20180120_models.QuerySpeechPushJobSpeechRequest,
    ) -> iot_20180120_models.QuerySpeechPushJobSpeechResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_speech_push_job_speech_with_options_async(request, runtime)

    def query_studio_app_domain_list_open_with_options(
        self,
        request: iot_20180120_models.QueryStudioAppDomainListOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryStudioAppDomainListOpenResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryStudioAppDomainListOpenResponse(),
            self.do_request('QueryStudioAppDomainListOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_studio_app_domain_list_open_with_options_async(
        self,
        request: iot_20180120_models.QueryStudioAppDomainListOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryStudioAppDomainListOpenResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryStudioAppDomainListOpenResponse(),
            await self.do_request_async('QueryStudioAppDomainListOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_studio_app_domain_list_open(
        self,
        request: iot_20180120_models.QueryStudioAppDomainListOpenRequest,
    ) -> iot_20180120_models.QueryStudioAppDomainListOpenResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_studio_app_domain_list_open_with_options(request, runtime)

    async def query_studio_app_domain_list_open_async(
        self,
        request: iot_20180120_models.QueryStudioAppDomainListOpenRequest,
    ) -> iot_20180120_models.QueryStudioAppDomainListOpenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_studio_app_domain_list_open_with_options_async(request, runtime)

    def query_studio_app_list_with_options(
        self,
        request: iot_20180120_models.QueryStudioAppListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryStudioAppListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryStudioAppListResponse(),
            self.do_request('QueryStudioAppList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_studio_app_list_with_options_async(
        self,
        request: iot_20180120_models.QueryStudioAppListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryStudioAppListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryStudioAppListResponse(),
            await self.do_request_async('QueryStudioAppList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_studio_app_list(
        self,
        request: iot_20180120_models.QueryStudioAppListRequest,
    ) -> iot_20180120_models.QueryStudioAppListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_studio_app_list_with_options(request, runtime)

    async def query_studio_app_list_async(
        self,
        request: iot_20180120_models.QueryStudioAppListRequest,
    ) -> iot_20180120_models.QueryStudioAppListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_studio_app_list_with_options_async(request, runtime)

    def query_studio_app_page_list_open_with_options(
        self,
        request: iot_20180120_models.QueryStudioAppPageListOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryStudioAppPageListOpenResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryStudioAppPageListOpenResponse(),
            self.do_request('QueryStudioAppPageListOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_studio_app_page_list_open_with_options_async(
        self,
        request: iot_20180120_models.QueryStudioAppPageListOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryStudioAppPageListOpenResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryStudioAppPageListOpenResponse(),
            await self.do_request_async('QueryStudioAppPageListOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_studio_app_page_list_open(
        self,
        request: iot_20180120_models.QueryStudioAppPageListOpenRequest,
    ) -> iot_20180120_models.QueryStudioAppPageListOpenResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_studio_app_page_list_open_with_options(request, runtime)

    async def query_studio_app_page_list_open_async(
        self,
        request: iot_20180120_models.QueryStudioAppPageListOpenRequest,
    ) -> iot_20180120_models.QueryStudioAppPageListOpenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_studio_app_page_list_open_with_options_async(request, runtime)

    def query_studio_project_list_with_options(
        self,
        request: iot_20180120_models.QueryStudioProjectListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryStudioProjectListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryStudioProjectListResponse(),
            self.do_request('QueryStudioProjectList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_studio_project_list_with_options_async(
        self,
        request: iot_20180120_models.QueryStudioProjectListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryStudioProjectListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryStudioProjectListResponse(),
            await self.do_request_async('QueryStudioProjectList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_studio_project_list(
        self,
        request: iot_20180120_models.QueryStudioProjectListRequest,
    ) -> iot_20180120_models.QueryStudioProjectListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_studio_project_list_with_options(request, runtime)

    async def query_studio_project_list_async(
        self,
        request: iot_20180120_models.QueryStudioProjectListRequest,
    ) -> iot_20180120_models.QueryStudioProjectListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_studio_project_list_with_options_async(request, runtime)

    def query_subscribe_relation_with_options(
        self,
        request: iot_20180120_models.QuerySubscribeRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySubscribeRelationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySubscribeRelationResponse(),
            self.do_request('QuerySubscribeRelation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_subscribe_relation_with_options_async(
        self,
        request: iot_20180120_models.QuerySubscribeRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySubscribeRelationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySubscribeRelationResponse(),
            await self.do_request_async('QuerySubscribeRelation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_subscribe_relation(
        self,
        request: iot_20180120_models.QuerySubscribeRelationRequest,
    ) -> iot_20180120_models.QuerySubscribeRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_subscribe_relation_with_options(request, runtime)

    async def query_subscribe_relation_async(
        self,
        request: iot_20180120_models.QuerySubscribeRelationRequest,
    ) -> iot_20180120_models.QuerySubscribeRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_subscribe_relation_with_options_async(request, runtime)

    def query_summary_scene_rule_log_with_options(
        self,
        request: iot_20180120_models.QuerySummarySceneRuleLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySummarySceneRuleLogResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySummarySceneRuleLogResponse(),
            self.do_request('QuerySummarySceneRuleLog', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_summary_scene_rule_log_with_options_async(
        self,
        request: iot_20180120_models.QuerySummarySceneRuleLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySummarySceneRuleLogResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySummarySceneRuleLogResponse(),
            await self.do_request_async('QuerySummarySceneRuleLog', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_summary_scene_rule_log(
        self,
        request: iot_20180120_models.QuerySummarySceneRuleLogRequest,
    ) -> iot_20180120_models.QuerySummarySceneRuleLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_summary_scene_rule_log_with_options(request, runtime)

    async def query_summary_scene_rule_log_async(
        self,
        request: iot_20180120_models.QuerySummarySceneRuleLogRequest,
    ) -> iot_20180120_models.QuerySummarySceneRuleLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_summary_scene_rule_log_with_options_async(request, runtime)

    def query_super_device_group_with_options(
        self,
        request: iot_20180120_models.QuerySuperDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySuperDeviceGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySuperDeviceGroupResponse(),
            self.do_request('QuerySuperDeviceGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_super_device_group_with_options_async(
        self,
        request: iot_20180120_models.QuerySuperDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySuperDeviceGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySuperDeviceGroupResponse(),
            await self.do_request_async('QuerySuperDeviceGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_super_device_group(
        self,
        request: iot_20180120_models.QuerySuperDeviceGroupRequest,
    ) -> iot_20180120_models.QuerySuperDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_super_device_group_with_options(request, runtime)

    async def query_super_device_group_async(
        self,
        request: iot_20180120_models.QuerySuperDeviceGroupRequest,
    ) -> iot_20180120_models.QuerySuperDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_super_device_group_with_options_async(request, runtime)

    def query_task_with_options(
        self,
        request: iot_20180120_models.QueryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryTaskResponse(),
            self.do_request('QueryTask', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_task_with_options_async(
        self,
        request: iot_20180120_models.QueryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryTaskResponse(),
            await self.do_request_async('QueryTask', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_task(
        self,
        request: iot_20180120_models.QueryTaskRequest,
    ) -> iot_20180120_models.QueryTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_task_with_options(request, runtime)

    async def query_task_async(
        self,
        request: iot_20180120_models.QueryTaskRequest,
    ) -> iot_20180120_models.QueryTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_task_with_options_async(request, runtime)

    def query_thing_model_with_options(
        self,
        request: iot_20180120_models.QueryThingModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryThingModelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryThingModelResponse(),
            self.do_request('QueryThingModel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_thing_model_with_options_async(
        self,
        request: iot_20180120_models.QueryThingModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryThingModelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryThingModelResponse(),
            await self.do_request_async('QueryThingModel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_thing_model(
        self,
        request: iot_20180120_models.QueryThingModelRequest,
    ) -> iot_20180120_models.QueryThingModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_thing_model_with_options(request, runtime)

    async def query_thing_model_async(
        self,
        request: iot_20180120_models.QueryThingModelRequest,
    ) -> iot_20180120_models.QueryThingModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_thing_model_with_options_async(request, runtime)

    def query_thing_model_extend_config_with_options(
        self,
        request: iot_20180120_models.QueryThingModelExtendConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryThingModelExtendConfigResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryThingModelExtendConfigResponse(),
            self.do_request('QueryThingModelExtendConfig', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_thing_model_extend_config_with_options_async(
        self,
        request: iot_20180120_models.QueryThingModelExtendConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryThingModelExtendConfigResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryThingModelExtendConfigResponse(),
            await self.do_request_async('QueryThingModelExtendConfig', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_thing_model_extend_config(
        self,
        request: iot_20180120_models.QueryThingModelExtendConfigRequest,
    ) -> iot_20180120_models.QueryThingModelExtendConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_thing_model_extend_config_with_options(request, runtime)

    async def query_thing_model_extend_config_async(
        self,
        request: iot_20180120_models.QueryThingModelExtendConfigRequest,
    ) -> iot_20180120_models.QueryThingModelExtendConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_thing_model_extend_config_with_options_async(request, runtime)

    def query_thing_model_extend_config_published_with_options(
        self,
        request: iot_20180120_models.QueryThingModelExtendConfigPublishedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryThingModelExtendConfigPublishedResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryThingModelExtendConfigPublishedResponse(),
            self.do_request('QueryThingModelExtendConfigPublished', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_thing_model_extend_config_published_with_options_async(
        self,
        request: iot_20180120_models.QueryThingModelExtendConfigPublishedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryThingModelExtendConfigPublishedResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryThingModelExtendConfigPublishedResponse(),
            await self.do_request_async('QueryThingModelExtendConfigPublished', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_thing_model_extend_config_published(
        self,
        request: iot_20180120_models.QueryThingModelExtendConfigPublishedRequest,
    ) -> iot_20180120_models.QueryThingModelExtendConfigPublishedResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_thing_model_extend_config_published_with_options(request, runtime)

    async def query_thing_model_extend_config_published_async(
        self,
        request: iot_20180120_models.QueryThingModelExtendConfigPublishedRequest,
    ) -> iot_20180120_models.QueryThingModelExtendConfigPublishedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_thing_model_extend_config_published_with_options_async(request, runtime)

    def query_thing_model_published_with_options(
        self,
        request: iot_20180120_models.QueryThingModelPublishedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryThingModelPublishedResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryThingModelPublishedResponse(),
            self.do_request('QueryThingModelPublished', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_thing_model_published_with_options_async(
        self,
        request: iot_20180120_models.QueryThingModelPublishedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryThingModelPublishedResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryThingModelPublishedResponse(),
            await self.do_request_async('QueryThingModelPublished', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_thing_model_published(
        self,
        request: iot_20180120_models.QueryThingModelPublishedRequest,
    ) -> iot_20180120_models.QueryThingModelPublishedResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_thing_model_published_with_options(request, runtime)

    async def query_thing_model_published_async(
        self,
        request: iot_20180120_models.QueryThingModelPublishedRequest,
    ) -> iot_20180120_models.QueryThingModelPublishedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_thing_model_published_with_options_async(request, runtime)

    def query_topic_reverse_route_table_with_options(
        self,
        request: iot_20180120_models.QueryTopicReverseRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryTopicReverseRouteTableResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryTopicReverseRouteTableResponse(),
            self.do_request('QueryTopicReverseRouteTable', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_topic_reverse_route_table_with_options_async(
        self,
        request: iot_20180120_models.QueryTopicReverseRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryTopicReverseRouteTableResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryTopicReverseRouteTableResponse(),
            await self.do_request_async('QueryTopicReverseRouteTable', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_topic_reverse_route_table(
        self,
        request: iot_20180120_models.QueryTopicReverseRouteTableRequest,
    ) -> iot_20180120_models.QueryTopicReverseRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_topic_reverse_route_table_with_options(request, runtime)

    async def query_topic_reverse_route_table_async(
        self,
        request: iot_20180120_models.QueryTopicReverseRouteTableRequest,
    ) -> iot_20180120_models.QueryTopicReverseRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_topic_reverse_route_table_with_options_async(request, runtime)

    def query_topic_route_table_with_options(
        self,
        request: iot_20180120_models.QueryTopicRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryTopicRouteTableResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryTopicRouteTableResponse(),
            self.do_request('QueryTopicRouteTable', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_topic_route_table_with_options_async(
        self,
        request: iot_20180120_models.QueryTopicRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryTopicRouteTableResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryTopicRouteTableResponse(),
            await self.do_request_async('QueryTopicRouteTable', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_topic_route_table(
        self,
        request: iot_20180120_models.QueryTopicRouteTableRequest,
    ) -> iot_20180120_models.QueryTopicRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_topic_route_table_with_options(request, runtime)

    async def query_topic_route_table_async(
        self,
        request: iot_20180120_models.QueryTopicRouteTableRequest,
    ) -> iot_20180120_models.QueryTopicRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_topic_route_table_with_options_async(request, runtime)

    def query_vehicle_device_with_options(
        self,
        request: iot_20180120_models.QueryVehicleDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryVehicleDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryVehicleDeviceResponse(),
            self.do_request('QueryVehicleDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def query_vehicle_device_with_options_async(
        self,
        request: iot_20180120_models.QueryVehicleDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryVehicleDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryVehicleDeviceResponse(),
            await self.do_request_async('QueryVehicleDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_vehicle_device(
        self,
        request: iot_20180120_models.QueryVehicleDeviceRequest,
    ) -> iot_20180120_models.QueryVehicleDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_vehicle_device_with_options(request, runtime)

    async def query_vehicle_device_async(
        self,
        request: iot_20180120_models.QueryVehicleDeviceRequest,
    ) -> iot_20180120_models.QueryVehicleDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_vehicle_device_with_options_async(request, runtime)

    def rrpc_with_options(
        self,
        request: iot_20180120_models.RRpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RRpcResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RRpcResponse(),
            self.do_request('RRpc', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def rrpc_with_options_async(
        self,
        request: iot_20180120_models.RRpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RRpcResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RRpcResponse(),
            await self.do_request_async('RRpc', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def rrpc(
        self,
        request: iot_20180120_models.RRpcRequest,
    ) -> iot_20180120_models.RRpcResponse:
        runtime = util_models.RuntimeOptions()
        return self.rrpc_with_options(request, runtime)

    async def rrpc_async(
        self,
        request: iot_20180120_models.RRpcRequest,
    ) -> iot_20180120_models.RRpcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rrpc_with_options_async(request, runtime)

    def re_bind_license_device_with_options(
        self,
        request: iot_20180120_models.ReBindLicenseDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ReBindLicenseDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ReBindLicenseDeviceResponse(),
            self.do_request('ReBindLicenseDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def re_bind_license_device_with_options_async(
        self,
        request: iot_20180120_models.ReBindLicenseDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ReBindLicenseDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ReBindLicenseDeviceResponse(),
            await self.do_request_async('ReBindLicenseDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def re_bind_license_device(
        self,
        request: iot_20180120_models.ReBindLicenseDeviceRequest,
    ) -> iot_20180120_models.ReBindLicenseDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.re_bind_license_device_with_options(request, runtime)

    async def re_bind_license_device_async(
        self,
        request: iot_20180120_models.ReBindLicenseDeviceRequest,
    ) -> iot_20180120_models.ReBindLicenseDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.re_bind_license_device_with_options_async(request, runtime)

    def recognize_car_num_with_options(
        self,
        request: iot_20180120_models.RecognizeCarNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RecognizeCarNumResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RecognizeCarNumResponse(),
            self.do_request('RecognizeCarNum', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def recognize_car_num_with_options_async(
        self,
        request: iot_20180120_models.RecognizeCarNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RecognizeCarNumResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RecognizeCarNumResponse(),
            await self.do_request_async('RecognizeCarNum', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def recognize_car_num(
        self,
        request: iot_20180120_models.RecognizeCarNumRequest,
    ) -> iot_20180120_models.RecognizeCarNumResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_car_num_with_options(request, runtime)

    async def recognize_car_num_async(
        self,
        request: iot_20180120_models.RecognizeCarNumRequest,
    ) -> iot_20180120_models.RecognizeCarNumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_car_num_with_options_async(request, runtime)

    def recognize_picture_general_with_options(
        self,
        request: iot_20180120_models.RecognizePictureGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RecognizePictureGeneralResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RecognizePictureGeneralResponse(),
            self.do_request('RecognizePictureGeneral', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def recognize_picture_general_with_options_async(
        self,
        request: iot_20180120_models.RecognizePictureGeneralRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RecognizePictureGeneralResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RecognizePictureGeneralResponse(),
            await self.do_request_async('RecognizePictureGeneral', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def recognize_picture_general(
        self,
        request: iot_20180120_models.RecognizePictureGeneralRequest,
    ) -> iot_20180120_models.RecognizePictureGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_picture_general_with_options(request, runtime)

    async def recognize_picture_general_async(
        self,
        request: iot_20180120_models.RecognizePictureGeneralRequest,
    ) -> iot_20180120_models.RecognizePictureGeneralResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_picture_general_with_options_async(request, runtime)

    def refresh_device_tunnel_share_password_with_options(
        self,
        request: iot_20180120_models.RefreshDeviceTunnelSharePasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RefreshDeviceTunnelSharePasswordResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RefreshDeviceTunnelSharePasswordResponse(),
            self.do_request('RefreshDeviceTunnelSharePassword', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def refresh_device_tunnel_share_password_with_options_async(
        self,
        request: iot_20180120_models.RefreshDeviceTunnelSharePasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RefreshDeviceTunnelSharePasswordResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RefreshDeviceTunnelSharePasswordResponse(),
            await self.do_request_async('RefreshDeviceTunnelSharePassword', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def refresh_device_tunnel_share_password(
        self,
        request: iot_20180120_models.RefreshDeviceTunnelSharePasswordRequest,
    ) -> iot_20180120_models.RefreshDeviceTunnelSharePasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_device_tunnel_share_password_with_options(request, runtime)

    async def refresh_device_tunnel_share_password_async(
        self,
        request: iot_20180120_models.RefreshDeviceTunnelSharePasswordRequest,
    ) -> iot_20180120_models.RefreshDeviceTunnelSharePasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_device_tunnel_share_password_with_options_async(request, runtime)

    def refresh_studio_app_token_open_with_options(
        self,
        request: iot_20180120_models.RefreshStudioAppTokenOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RefreshStudioAppTokenOpenResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RefreshStudioAppTokenOpenResponse(),
            self.do_request('RefreshStudioAppTokenOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def refresh_studio_app_token_open_with_options_async(
        self,
        request: iot_20180120_models.RefreshStudioAppTokenOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RefreshStudioAppTokenOpenResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RefreshStudioAppTokenOpenResponse(),
            await self.do_request_async('RefreshStudioAppTokenOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def refresh_studio_app_token_open(
        self,
        request: iot_20180120_models.RefreshStudioAppTokenOpenRequest,
    ) -> iot_20180120_models.RefreshStudioAppTokenOpenResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_studio_app_token_open_with_options(request, runtime)

    async def refresh_studio_app_token_open_async(
        self,
        request: iot_20180120_models.RefreshStudioAppTokenOpenRequest,
    ) -> iot_20180120_models.RefreshStudioAppTokenOpenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_studio_app_token_open_with_options_async(request, runtime)

    def register_device_with_options(
        self,
        request: iot_20180120_models.RegisterDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RegisterDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RegisterDeviceResponse(),
            self.do_request('RegisterDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def register_device_with_options_async(
        self,
        request: iot_20180120_models.RegisterDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RegisterDeviceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RegisterDeviceResponse(),
            await self.do_request_async('RegisterDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def register_device(
        self,
        request: iot_20180120_models.RegisterDeviceRequest,
    ) -> iot_20180120_models.RegisterDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_device_with_options(request, runtime)

    async def register_device_async(
        self,
        request: iot_20180120_models.RegisterDeviceRequest,
    ) -> iot_20180120_models.RegisterDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_device_with_options_async(request, runtime)

    def release_edge_driver_version_with_options(
        self,
        request: iot_20180120_models.ReleaseEdgeDriverVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ReleaseEdgeDriverVersionResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ReleaseEdgeDriverVersionResponse(),
            self.do_request('ReleaseEdgeDriverVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def release_edge_driver_version_with_options_async(
        self,
        request: iot_20180120_models.ReleaseEdgeDriverVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ReleaseEdgeDriverVersionResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ReleaseEdgeDriverVersionResponse(),
            await self.do_request_async('ReleaseEdgeDriverVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def release_edge_driver_version(
        self,
        request: iot_20180120_models.ReleaseEdgeDriverVersionRequest,
    ) -> iot_20180120_models.ReleaseEdgeDriverVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_edge_driver_version_with_options(request, runtime)

    async def release_edge_driver_version_async(
        self,
        request: iot_20180120_models.ReleaseEdgeDriverVersionRequest,
    ) -> iot_20180120_models.ReleaseEdgeDriverVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_edge_driver_version_with_options_async(request, runtime)

    def release_product_with_options(
        self,
        request: iot_20180120_models.ReleaseProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ReleaseProductResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ReleaseProductResponse(),
            self.do_request('ReleaseProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def release_product_with_options_async(
        self,
        request: iot_20180120_models.ReleaseProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ReleaseProductResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ReleaseProductResponse(),
            await self.do_request_async('ReleaseProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def release_product(
        self,
        request: iot_20180120_models.ReleaseProductRequest,
    ) -> iot_20180120_models.ReleaseProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_product_with_options(request, runtime)

    async def release_product_async(
        self,
        request: iot_20180120_models.ReleaseProductRequest,
    ) -> iot_20180120_models.ReleaseProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_product_with_options_async(request, runtime)

    def remove_thing_topo_with_options(
        self,
        request: iot_20180120_models.RemoveThingTopoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RemoveThingTopoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RemoveThingTopoResponse(),
            self.do_request('RemoveThingTopo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def remove_thing_topo_with_options_async(
        self,
        request: iot_20180120_models.RemoveThingTopoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RemoveThingTopoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RemoveThingTopoResponse(),
            await self.do_request_async('RemoveThingTopo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def remove_thing_topo(
        self,
        request: iot_20180120_models.RemoveThingTopoRequest,
    ) -> iot_20180120_models.RemoveThingTopoResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_thing_topo_with_options(request, runtime)

    async def remove_thing_topo_async(
        self,
        request: iot_20180120_models.RemoveThingTopoRequest,
    ) -> iot_20180120_models.RemoveThingTopoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_thing_topo_with_options_async(request, runtime)

    def replace_edge_instance_gateway_with_options(
        self,
        request: iot_20180120_models.ReplaceEdgeInstanceGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ReplaceEdgeInstanceGatewayResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ReplaceEdgeInstanceGatewayResponse(),
            self.do_request('ReplaceEdgeInstanceGateway', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def replace_edge_instance_gateway_with_options_async(
        self,
        request: iot_20180120_models.ReplaceEdgeInstanceGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ReplaceEdgeInstanceGatewayResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ReplaceEdgeInstanceGatewayResponse(),
            await self.do_request_async('ReplaceEdgeInstanceGateway', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def replace_edge_instance_gateway(
        self,
        request: iot_20180120_models.ReplaceEdgeInstanceGatewayRequest,
    ) -> iot_20180120_models.ReplaceEdgeInstanceGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.replace_edge_instance_gateway_with_options(request, runtime)

    async def replace_edge_instance_gateway_async(
        self,
        request: iot_20180120_models.ReplaceEdgeInstanceGatewayRequest,
    ) -> iot_20180120_models.ReplaceEdgeInstanceGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.replace_edge_instance_gateway_with_options_async(request, runtime)

    def rerun_job_with_options(
        self,
        request: iot_20180120_models.RerunJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RerunJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RerunJobResponse(),
            self.do_request('RerunJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def rerun_job_with_options_async(
        self,
        request: iot_20180120_models.RerunJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RerunJobResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RerunJobResponse(),
            await self.do_request_async('RerunJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def rerun_job(
        self,
        request: iot_20180120_models.RerunJobRequest,
    ) -> iot_20180120_models.RerunJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.rerun_job_with_options(request, runtime)

    async def rerun_job_async(
        self,
        request: iot_20180120_models.RerunJobRequest,
    ) -> iot_20180120_models.RerunJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rerun_job_with_options_async(request, runtime)

    def reset_consumer_group_position_with_options(
        self,
        request: iot_20180120_models.ResetConsumerGroupPositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ResetConsumerGroupPositionResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ResetConsumerGroupPositionResponse(),
            self.do_request('ResetConsumerGroupPosition', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def reset_consumer_group_position_with_options_async(
        self,
        request: iot_20180120_models.ResetConsumerGroupPositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ResetConsumerGroupPositionResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ResetConsumerGroupPositionResponse(),
            await self.do_request_async('ResetConsumerGroupPosition', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def reset_consumer_group_position(
        self,
        request: iot_20180120_models.ResetConsumerGroupPositionRequest,
    ) -> iot_20180120_models.ResetConsumerGroupPositionResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_consumer_group_position_with_options(request, runtime)

    async def reset_consumer_group_position_async(
        self,
        request: iot_20180120_models.ResetConsumerGroupPositionRequest,
    ) -> iot_20180120_models.ResetConsumerGroupPositionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_consumer_group_position_with_options_async(request, runtime)

    def reset_thing_with_options(
        self,
        request: iot_20180120_models.ResetThingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ResetThingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ResetThingResponse(),
            self.do_request('ResetThing', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def reset_thing_with_options_async(
        self,
        request: iot_20180120_models.ResetThingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ResetThingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ResetThingResponse(),
            await self.do_request_async('ResetThing', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def reset_thing(
        self,
        request: iot_20180120_models.ResetThingRequest,
    ) -> iot_20180120_models.ResetThingResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_thing_with_options(request, runtime)

    async def reset_thing_async(
        self,
        request: iot_20180120_models.ResetThingRequest,
    ) -> iot_20180120_models.ResetThingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_thing_with_options_async(request, runtime)

    def retry_sound_code_label_batch_with_options(
        self,
        request: iot_20180120_models.RetrySoundCodeLabelBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RetrySoundCodeLabelBatchResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RetrySoundCodeLabelBatchResponse(),
            self.do_request('RetrySoundCodeLabelBatch', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def retry_sound_code_label_batch_with_options_async(
        self,
        request: iot_20180120_models.RetrySoundCodeLabelBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RetrySoundCodeLabelBatchResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RetrySoundCodeLabelBatchResponse(),
            await self.do_request_async('RetrySoundCodeLabelBatch', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def retry_sound_code_label_batch(
        self,
        request: iot_20180120_models.RetrySoundCodeLabelBatchRequest,
    ) -> iot_20180120_models.RetrySoundCodeLabelBatchResponse:
        runtime = util_models.RuntimeOptions()
        return self.retry_sound_code_label_batch_with_options(request, runtime)

    async def retry_sound_code_label_batch_async(
        self,
        request: iot_20180120_models.RetrySoundCodeLabelBatchRequest,
    ) -> iot_20180120_models.RetrySoundCodeLabelBatchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retry_sound_code_label_batch_with_options_async(request, runtime)

    def reupgrade_otatask_with_options(
        self,
        request: iot_20180120_models.ReupgradeOTATaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ReupgradeOTATaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ReupgradeOTATaskResponse(),
            self.do_request('ReupgradeOTATask', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def reupgrade_otatask_with_options_async(
        self,
        request: iot_20180120_models.ReupgradeOTATaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ReupgradeOTATaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ReupgradeOTATaskResponse(),
            await self.do_request_async('ReupgradeOTATask', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def reupgrade_otatask(
        self,
        request: iot_20180120_models.ReupgradeOTATaskRequest,
    ) -> iot_20180120_models.ReupgradeOTATaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.reupgrade_otatask_with_options(request, runtime)

    async def reupgrade_otatask_async(
        self,
        request: iot_20180120_models.ReupgradeOTATaskRequest,
    ) -> iot_20180120_models.ReupgradeOTATaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reupgrade_otatask_with_options_async(request, runtime)

    def save_device_prop_with_options(
        self,
        request: iot_20180120_models.SaveDevicePropRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SaveDevicePropResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SaveDevicePropResponse(),
            self.do_request('SaveDeviceProp', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def save_device_prop_with_options_async(
        self,
        request: iot_20180120_models.SaveDevicePropRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SaveDevicePropResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SaveDevicePropResponse(),
            await self.do_request_async('SaveDeviceProp', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def save_device_prop(
        self,
        request: iot_20180120_models.SaveDevicePropRequest,
    ) -> iot_20180120_models.SaveDevicePropResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_device_prop_with_options(request, runtime)

    async def save_device_prop_async(
        self,
        request: iot_20180120_models.SaveDevicePropRequest,
    ) -> iot_20180120_models.SaveDevicePropResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_device_prop_with_options_async(request, runtime)

    def save_script_with_options(
        self,
        request: iot_20180120_models.SaveScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SaveScriptResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SaveScriptResponse(),
            self.do_request('SaveScript', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def save_script_with_options_async(
        self,
        request: iot_20180120_models.SaveScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SaveScriptResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SaveScriptResponse(),
            await self.do_request_async('SaveScript', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def save_script(
        self,
        request: iot_20180120_models.SaveScriptRequest,
    ) -> iot_20180120_models.SaveScriptResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_script_with_options(request, runtime)

    async def save_script_async(
        self,
        request: iot_20180120_models.SaveScriptRequest,
    ) -> iot_20180120_models.SaveScriptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_script_with_options_async(request, runtime)

    def set_device_desired_property_with_options(
        self,
        request: iot_20180120_models.SetDeviceDesiredPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetDeviceDesiredPropertyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SetDeviceDesiredPropertyResponse(),
            self.do_request('SetDeviceDesiredProperty', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_device_desired_property_with_options_async(
        self,
        request: iot_20180120_models.SetDeviceDesiredPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetDeviceDesiredPropertyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SetDeviceDesiredPropertyResponse(),
            await self.do_request_async('SetDeviceDesiredProperty', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_device_desired_property(
        self,
        request: iot_20180120_models.SetDeviceDesiredPropertyRequest,
    ) -> iot_20180120_models.SetDeviceDesiredPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_device_desired_property_with_options(request, runtime)

    async def set_device_desired_property_async(
        self,
        request: iot_20180120_models.SetDeviceDesiredPropertyRequest,
    ) -> iot_20180120_models.SetDeviceDesiredPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_device_desired_property_with_options_async(request, runtime)

    def set_device_group_tags_with_options(
        self,
        request: iot_20180120_models.SetDeviceGroupTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetDeviceGroupTagsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SetDeviceGroupTagsResponse(),
            self.do_request('SetDeviceGroupTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_device_group_tags_with_options_async(
        self,
        request: iot_20180120_models.SetDeviceGroupTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetDeviceGroupTagsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SetDeviceGroupTagsResponse(),
            await self.do_request_async('SetDeviceGroupTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_device_group_tags(
        self,
        request: iot_20180120_models.SetDeviceGroupTagsRequest,
    ) -> iot_20180120_models.SetDeviceGroupTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_device_group_tags_with_options(request, runtime)

    async def set_device_group_tags_async(
        self,
        request: iot_20180120_models.SetDeviceGroupTagsRequest,
    ) -> iot_20180120_models.SetDeviceGroupTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_device_group_tags_with_options_async(request, runtime)

    def set_device_property_with_options(
        self,
        request: iot_20180120_models.SetDevicePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetDevicePropertyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SetDevicePropertyResponse(),
            self.do_request('SetDeviceProperty', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_device_property_with_options_async(
        self,
        request: iot_20180120_models.SetDevicePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetDevicePropertyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SetDevicePropertyResponse(),
            await self.do_request_async('SetDeviceProperty', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_device_property(
        self,
        request: iot_20180120_models.SetDevicePropertyRequest,
    ) -> iot_20180120_models.SetDevicePropertyResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_device_property_with_options(request, runtime)

    async def set_device_property_async(
        self,
        request: iot_20180120_models.SetDevicePropertyRequest,
    ) -> iot_20180120_models.SetDevicePropertyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_device_property_with_options_async(request, runtime)

    def set_devices_property_with_options(
        self,
        request: iot_20180120_models.SetDevicesPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetDevicesPropertyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SetDevicesPropertyResponse(),
            self.do_request('SetDevicesProperty', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_devices_property_with_options_async(
        self,
        request: iot_20180120_models.SetDevicesPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetDevicesPropertyResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SetDevicesPropertyResponse(),
            await self.do_request_async('SetDevicesProperty', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_devices_property(
        self,
        request: iot_20180120_models.SetDevicesPropertyRequest,
    ) -> iot_20180120_models.SetDevicesPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_devices_property_with_options(request, runtime)

    async def set_devices_property_async(
        self,
        request: iot_20180120_models.SetDevicesPropertyRequest,
    ) -> iot_20180120_models.SetDevicesPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_devices_property_with_options_async(request, runtime)

    def set_edge_instance_driver_configs_with_options(
        self,
        request: iot_20180120_models.SetEdgeInstanceDriverConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetEdgeInstanceDriverConfigsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SetEdgeInstanceDriverConfigsResponse(),
            self.do_request('SetEdgeInstanceDriverConfigs', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_edge_instance_driver_configs_with_options_async(
        self,
        request: iot_20180120_models.SetEdgeInstanceDriverConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetEdgeInstanceDriverConfigsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SetEdgeInstanceDriverConfigsResponse(),
            await self.do_request_async('SetEdgeInstanceDriverConfigs', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_edge_instance_driver_configs(
        self,
        request: iot_20180120_models.SetEdgeInstanceDriverConfigsRequest,
    ) -> iot_20180120_models.SetEdgeInstanceDriverConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_edge_instance_driver_configs_with_options(request, runtime)

    async def set_edge_instance_driver_configs_async(
        self,
        request: iot_20180120_models.SetEdgeInstanceDriverConfigsRequest,
    ) -> iot_20180120_models.SetEdgeInstanceDriverConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_edge_instance_driver_configs_with_options_async(request, runtime)

    def set_product_cert_info_with_options(
        self,
        request: iot_20180120_models.SetProductCertInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetProductCertInfoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SetProductCertInfoResponse(),
            self.do_request('SetProductCertInfo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_product_cert_info_with_options_async(
        self,
        request: iot_20180120_models.SetProductCertInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetProductCertInfoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SetProductCertInfoResponse(),
            await self.do_request_async('SetProductCertInfo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_product_cert_info(
        self,
        request: iot_20180120_models.SetProductCertInfoRequest,
    ) -> iot_20180120_models.SetProductCertInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_product_cert_info_with_options(request, runtime)

    async def set_product_cert_info_async(
        self,
        request: iot_20180120_models.SetProductCertInfoRequest,
    ) -> iot_20180120_models.SetProductCertInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_product_cert_info_with_options_async(request, runtime)

    def set_studio_project_cooperation_with_options(
        self,
        request: iot_20180120_models.SetStudioProjectCooperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetStudioProjectCooperationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SetStudioProjectCooperationResponse(),
            self.do_request('SetStudioProjectCooperation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_studio_project_cooperation_with_options_async(
        self,
        request: iot_20180120_models.SetStudioProjectCooperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetStudioProjectCooperationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SetStudioProjectCooperationResponse(),
            await self.do_request_async('SetStudioProjectCooperation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_studio_project_cooperation(
        self,
        request: iot_20180120_models.SetStudioProjectCooperationRequest,
    ) -> iot_20180120_models.SetStudioProjectCooperationResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_studio_project_cooperation_with_options(request, runtime)

    async def set_studio_project_cooperation_async(
        self,
        request: iot_20180120_models.SetStudioProjectCooperationRequest,
    ) -> iot_20180120_models.SetStudioProjectCooperationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_studio_project_cooperation_with_options_async(request, runtime)

    def setup_studio_app_auth_mode_open_with_options(
        self,
        request: iot_20180120_models.SetupStudioAppAuthModeOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetupStudioAppAuthModeOpenResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SetupStudioAppAuthModeOpenResponse(),
            self.do_request('SetupStudioAppAuthModeOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def setup_studio_app_auth_mode_open_with_options_async(
        self,
        request: iot_20180120_models.SetupStudioAppAuthModeOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetupStudioAppAuthModeOpenResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SetupStudioAppAuthModeOpenResponse(),
            await self.do_request_async('SetupStudioAppAuthModeOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def setup_studio_app_auth_mode_open(
        self,
        request: iot_20180120_models.SetupStudioAppAuthModeOpenRequest,
    ) -> iot_20180120_models.SetupStudioAppAuthModeOpenResponse:
        runtime = util_models.RuntimeOptions()
        return self.setup_studio_app_auth_mode_open_with_options(request, runtime)

    async def setup_studio_app_auth_mode_open_async(
        self,
        request: iot_20180120_models.SetupStudioAppAuthModeOpenRequest,
    ) -> iot_20180120_models.SetupStudioAppAuthModeOpenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.setup_studio_app_auth_mode_open_with_options_async(request, runtime)

    def share_speech_by_combination_with_options(
        self,
        request: iot_20180120_models.ShareSpeechByCombinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ShareSpeechByCombinationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ShareSpeechByCombinationResponse(),
            self.do_request('ShareSpeechByCombination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def share_speech_by_combination_with_options_async(
        self,
        request: iot_20180120_models.ShareSpeechByCombinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ShareSpeechByCombinationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ShareSpeechByCombinationResponse(),
            await self.do_request_async('ShareSpeechByCombination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def share_speech_by_combination(
        self,
        request: iot_20180120_models.ShareSpeechByCombinationRequest,
    ) -> iot_20180120_models.ShareSpeechByCombinationResponse:
        runtime = util_models.RuntimeOptions()
        return self.share_speech_by_combination_with_options(request, runtime)

    async def share_speech_by_combination_async(
        self,
        request: iot_20180120_models.ShareSpeechByCombinationRequest,
    ) -> iot_20180120_models.ShareSpeechByCombinationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.share_speech_by_combination_with_options_async(request, runtime)

    def speech_by_combination_with_options(
        self,
        request: iot_20180120_models.SpeechByCombinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SpeechByCombinationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SpeechByCombinationResponse(),
            self.do_request('SpeechByCombination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def speech_by_combination_with_options_async(
        self,
        request: iot_20180120_models.SpeechByCombinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SpeechByCombinationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SpeechByCombinationResponse(),
            await self.do_request_async('SpeechByCombination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def speech_by_combination(
        self,
        request: iot_20180120_models.SpeechByCombinationRequest,
    ) -> iot_20180120_models.SpeechByCombinationResponse:
        runtime = util_models.RuntimeOptions()
        return self.speech_by_combination_with_options(request, runtime)

    async def speech_by_combination_async(
        self,
        request: iot_20180120_models.SpeechByCombinationRequest,
    ) -> iot_20180120_models.SpeechByCombinationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.speech_by_combination_with_options_async(request, runtime)

    def speech_by_synthesis_with_options(
        self,
        request: iot_20180120_models.SpeechBySynthesisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SpeechBySynthesisResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SpeechBySynthesisResponse(),
            self.do_request('SpeechBySynthesis', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def speech_by_synthesis_with_options_async(
        self,
        request: iot_20180120_models.SpeechBySynthesisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SpeechBySynthesisResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SpeechBySynthesisResponse(),
            await self.do_request_async('SpeechBySynthesis', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def speech_by_synthesis(
        self,
        request: iot_20180120_models.SpeechBySynthesisRequest,
    ) -> iot_20180120_models.SpeechBySynthesisResponse:
        runtime = util_models.RuntimeOptions()
        return self.speech_by_synthesis_with_options(request, runtime)

    async def speech_by_synthesis_async(
        self,
        request: iot_20180120_models.SpeechBySynthesisRequest,
    ) -> iot_20180120_models.SpeechBySynthesisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.speech_by_synthesis_with_options_async(request, runtime)

    def start_parser_with_options(
        self,
        request: iot_20180120_models.StartParserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.StartParserResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.StartParserResponse(),
            self.do_request('StartParser', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def start_parser_with_options_async(
        self,
        request: iot_20180120_models.StartParserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.StartParserResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.StartParserResponse(),
            await self.do_request_async('StartParser', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def start_parser(
        self,
        request: iot_20180120_models.StartParserRequest,
    ) -> iot_20180120_models.StartParserResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_parser_with_options(request, runtime)

    async def start_parser_async(
        self,
        request: iot_20180120_models.StartParserRequest,
    ) -> iot_20180120_models.StartParserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_parser_with_options_async(request, runtime)

    def start_rule_with_options(
        self,
        request: iot_20180120_models.StartRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.StartRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.StartRuleResponse(),
            self.do_request('StartRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def start_rule_with_options_async(
        self,
        request: iot_20180120_models.StartRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.StartRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.StartRuleResponse(),
            await self.do_request_async('StartRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def start_rule(
        self,
        request: iot_20180120_models.StartRuleRequest,
    ) -> iot_20180120_models.StartRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_rule_with_options(request, runtime)

    async def start_rule_async(
        self,
        request: iot_20180120_models.StartRuleRequest,
    ) -> iot_20180120_models.StartRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_rule_with_options_async(request, runtime)

    def stop_parser_with_options(
        self,
        request: iot_20180120_models.StopParserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.StopParserResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.StopParserResponse(),
            self.do_request('StopParser', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def stop_parser_with_options_async(
        self,
        request: iot_20180120_models.StopParserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.StopParserResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.StopParserResponse(),
            await self.do_request_async('StopParser', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def stop_parser(
        self,
        request: iot_20180120_models.StopParserRequest,
    ) -> iot_20180120_models.StopParserResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_parser_with_options(request, runtime)

    async def stop_parser_async(
        self,
        request: iot_20180120_models.StopParserRequest,
    ) -> iot_20180120_models.StopParserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_parser_with_options_async(request, runtime)

    def stop_rule_with_options(
        self,
        request: iot_20180120_models.StopRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.StopRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.StopRuleResponse(),
            self.do_request('StopRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def stop_rule_with_options_async(
        self,
        request: iot_20180120_models.StopRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.StopRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.StopRuleResponse(),
            await self.do_request_async('StopRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def stop_rule(
        self,
        request: iot_20180120_models.StopRuleRequest,
    ) -> iot_20180120_models.StopRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_rule_with_options(request, runtime)

    async def stop_rule_async(
        self,
        request: iot_20180120_models.StopRuleRequest,
    ) -> iot_20180120_models.StopRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_rule_with_options_async(request, runtime)

    def subscribe_topic_with_options(
        self,
        request: iot_20180120_models.SubscribeTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SubscribeTopicResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SubscribeTopicResponse(),
            self.do_request('SubscribeTopic', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def subscribe_topic_with_options_async(
        self,
        request: iot_20180120_models.SubscribeTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SubscribeTopicResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SubscribeTopicResponse(),
            await self.do_request_async('SubscribeTopic', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def subscribe_topic(
        self,
        request: iot_20180120_models.SubscribeTopicRequest,
    ) -> iot_20180120_models.SubscribeTopicResponse:
        runtime = util_models.RuntimeOptions()
        return self.subscribe_topic_with_options(request, runtime)

    async def subscribe_topic_async(
        self,
        request: iot_20180120_models.SubscribeTopicRequest,
    ) -> iot_20180120_models.SubscribeTopicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.subscribe_topic_with_options_async(request, runtime)

    def sync_speech_by_combination_with_options(
        self,
        request: iot_20180120_models.SyncSpeechByCombinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SyncSpeechByCombinationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SyncSpeechByCombinationResponse(),
            self.do_request('SyncSpeechByCombination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def sync_speech_by_combination_with_options_async(
        self,
        request: iot_20180120_models.SyncSpeechByCombinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SyncSpeechByCombinationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SyncSpeechByCombinationResponse(),
            await self.do_request_async('SyncSpeechByCombination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def sync_speech_by_combination(
        self,
        request: iot_20180120_models.SyncSpeechByCombinationRequest,
    ) -> iot_20180120_models.SyncSpeechByCombinationResponse:
        runtime = util_models.RuntimeOptions()
        return self.sync_speech_by_combination_with_options(request, runtime)

    async def sync_speech_by_combination_async(
        self,
        request: iot_20180120_models.SyncSpeechByCombinationRequest,
    ) -> iot_20180120_models.SyncSpeechByCombinationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sync_speech_by_combination_with_options_async(request, runtime)

    def test_speech_with_options(
        self,
        tmp: iot_20180120_models.TestSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.TestSpeechResponse:
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.TestSpeechShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.sound_code_config):
            request.sound_code_config_shrink = UtilClient.to_jsonstring(tmp.sound_code_config)
        return TeaCore.from_map(
            iot_20180120_models.TestSpeechResponse(),
            self.do_request('TestSpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def test_speech_with_options_async(
        self,
        tmp: iot_20180120_models.TestSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.TestSpeechResponse:
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.TestSpeechShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.sound_code_config):
            request.sound_code_config_shrink = UtilClient.to_jsonstring(tmp.sound_code_config)
        return TeaCore.from_map(
            iot_20180120_models.TestSpeechResponse(),
            await self.do_request_async('TestSpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def test_speech(
        self,
        request: iot_20180120_models.TestSpeechRequest,
    ) -> iot_20180120_models.TestSpeechResponse:
        runtime = util_models.RuntimeOptions()
        return self.test_speech_with_options(request, runtime)

    async def test_speech_async(
        self,
        request: iot_20180120_models.TestSpeechRequest,
    ) -> iot_20180120_models.TestSpeechResponse:
        runtime = util_models.RuntimeOptions()
        return await self.test_speech_with_options_async(request, runtime)

    def transform_client_id_with_options(
        self,
        request: iot_20180120_models.TransformClientIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.TransformClientIdResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.TransformClientIdResponse(),
            self.do_request('TransformClientId', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def transform_client_id_with_options_async(
        self,
        request: iot_20180120_models.TransformClientIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.TransformClientIdResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.TransformClientIdResponse(),
            await self.do_request_async('TransformClientId', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def transform_client_id(
        self,
        request: iot_20180120_models.TransformClientIdRequest,
    ) -> iot_20180120_models.TransformClientIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.transform_client_id_with_options(request, runtime)

    async def transform_client_id_async(
        self,
        request: iot_20180120_models.TransformClientIdRequest,
    ) -> iot_20180120_models.TransformClientIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transform_client_id_with_options_async(request, runtime)

    def trigger_scene_rule_with_options(
        self,
        request: iot_20180120_models.TriggerSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.TriggerSceneRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.TriggerSceneRuleResponse(),
            self.do_request('TriggerSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def trigger_scene_rule_with_options_async(
        self,
        request: iot_20180120_models.TriggerSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.TriggerSceneRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.TriggerSceneRuleResponse(),
            await self.do_request_async('TriggerSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def trigger_scene_rule(
        self,
        request: iot_20180120_models.TriggerSceneRuleRequest,
    ) -> iot_20180120_models.TriggerSceneRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.trigger_scene_rule_with_options(request, runtime)

    async def trigger_scene_rule_async(
        self,
        request: iot_20180120_models.TriggerSceneRuleRequest,
    ) -> iot_20180120_models.TriggerSceneRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.trigger_scene_rule_with_options_async(request, runtime)

    def unbind_application_from_edge_instance_with_options(
        self,
        request: iot_20180120_models.UnbindApplicationFromEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UnbindApplicationFromEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UnbindApplicationFromEdgeInstanceResponse(),
            self.do_request('UnbindApplicationFromEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def unbind_application_from_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.UnbindApplicationFromEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UnbindApplicationFromEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UnbindApplicationFromEdgeInstanceResponse(),
            await self.do_request_async('UnbindApplicationFromEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def unbind_application_from_edge_instance(
        self,
        request: iot_20180120_models.UnbindApplicationFromEdgeInstanceRequest,
    ) -> iot_20180120_models.UnbindApplicationFromEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_application_from_edge_instance_with_options(request, runtime)

    async def unbind_application_from_edge_instance_async(
        self,
        request: iot_20180120_models.UnbindApplicationFromEdgeInstanceRequest,
    ) -> iot_20180120_models.UnbindApplicationFromEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_application_from_edge_instance_with_options_async(request, runtime)

    def unbind_driver_from_edge_instance_with_options(
        self,
        request: iot_20180120_models.UnbindDriverFromEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UnbindDriverFromEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UnbindDriverFromEdgeInstanceResponse(),
            self.do_request('UnbindDriverFromEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def unbind_driver_from_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.UnbindDriverFromEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UnbindDriverFromEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UnbindDriverFromEdgeInstanceResponse(),
            await self.do_request_async('UnbindDriverFromEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def unbind_driver_from_edge_instance(
        self,
        request: iot_20180120_models.UnbindDriverFromEdgeInstanceRequest,
    ) -> iot_20180120_models.UnbindDriverFromEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_driver_from_edge_instance_with_options(request, runtime)

    async def unbind_driver_from_edge_instance_async(
        self,
        request: iot_20180120_models.UnbindDriverFromEdgeInstanceRequest,
    ) -> iot_20180120_models.UnbindDriverFromEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_driver_from_edge_instance_with_options_async(request, runtime)

    def unbind_license_product_with_options(
        self,
        request: iot_20180120_models.UnbindLicenseProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UnbindLicenseProductResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UnbindLicenseProductResponse(),
            self.do_request('UnbindLicenseProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def unbind_license_product_with_options_async(
        self,
        request: iot_20180120_models.UnbindLicenseProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UnbindLicenseProductResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UnbindLicenseProductResponse(),
            await self.do_request_async('UnbindLicenseProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def unbind_license_product(
        self,
        request: iot_20180120_models.UnbindLicenseProductRequest,
    ) -> iot_20180120_models.UnbindLicenseProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_license_product_with_options(request, runtime)

    async def unbind_license_product_async(
        self,
        request: iot_20180120_models.UnbindLicenseProductRequest,
    ) -> iot_20180120_models.UnbindLicenseProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_license_product_with_options_async(request, runtime)

    def unbind_role_from_edge_instance_with_options(
        self,
        request: iot_20180120_models.UnbindRoleFromEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UnbindRoleFromEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UnbindRoleFromEdgeInstanceResponse(),
            self.do_request('UnbindRoleFromEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def unbind_role_from_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.UnbindRoleFromEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UnbindRoleFromEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UnbindRoleFromEdgeInstanceResponse(),
            await self.do_request_async('UnbindRoleFromEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def unbind_role_from_edge_instance(
        self,
        request: iot_20180120_models.UnbindRoleFromEdgeInstanceRequest,
    ) -> iot_20180120_models.UnbindRoleFromEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_role_from_edge_instance_with_options(request, runtime)

    async def unbind_role_from_edge_instance_async(
        self,
        request: iot_20180120_models.UnbindRoleFromEdgeInstanceRequest,
    ) -> iot_20180120_models.UnbindRoleFromEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_role_from_edge_instance_with_options_async(request, runtime)

    def unbind_scene_rule_from_edge_instance_with_options(
        self,
        request: iot_20180120_models.UnbindSceneRuleFromEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UnbindSceneRuleFromEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UnbindSceneRuleFromEdgeInstanceResponse(),
            self.do_request('UnbindSceneRuleFromEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def unbind_scene_rule_from_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.UnbindSceneRuleFromEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UnbindSceneRuleFromEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UnbindSceneRuleFromEdgeInstanceResponse(),
            await self.do_request_async('UnbindSceneRuleFromEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def unbind_scene_rule_from_edge_instance(
        self,
        request: iot_20180120_models.UnbindSceneRuleFromEdgeInstanceRequest,
    ) -> iot_20180120_models.UnbindSceneRuleFromEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_scene_rule_from_edge_instance_with_options(request, runtime)

    async def unbind_scene_rule_from_edge_instance_async(
        self,
        request: iot_20180120_models.UnbindSceneRuleFromEdgeInstanceRequest,
    ) -> iot_20180120_models.UnbindSceneRuleFromEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_scene_rule_from_edge_instance_with_options_async(request, runtime)

    def update_consumer_group_with_options(
        self,
        request: iot_20180120_models.UpdateConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateConsumerGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateConsumerGroupResponse(),
            self.do_request('UpdateConsumerGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_consumer_group_with_options_async(
        self,
        request: iot_20180120_models.UpdateConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateConsumerGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateConsumerGroupResponse(),
            await self.do_request_async('UpdateConsumerGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_consumer_group(
        self,
        request: iot_20180120_models.UpdateConsumerGroupRequest,
    ) -> iot_20180120_models.UpdateConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_consumer_group_with_options(request, runtime)

    async def update_consumer_group_async(
        self,
        request: iot_20180120_models.UpdateConsumerGroupRequest,
    ) -> iot_20180120_models.UpdateConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_consumer_group_with_options_async(request, runtime)

    def update_destination_with_options(
        self,
        request: iot_20180120_models.UpdateDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateDestinationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateDestinationResponse(),
            self.do_request('UpdateDestination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_destination_with_options_async(
        self,
        request: iot_20180120_models.UpdateDestinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateDestinationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateDestinationResponse(),
            await self.do_request_async('UpdateDestination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_destination(
        self,
        request: iot_20180120_models.UpdateDestinationRequest,
    ) -> iot_20180120_models.UpdateDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_destination_with_options(request, runtime)

    async def update_destination_async(
        self,
        request: iot_20180120_models.UpdateDestinationRequest,
    ) -> iot_20180120_models.UpdateDestinationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_destination_with_options_async(request, runtime)

    def update_device_group_with_options(
        self,
        request: iot_20180120_models.UpdateDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateDeviceGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateDeviceGroupResponse(),
            self.do_request('UpdateDeviceGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_device_group_with_options_async(
        self,
        request: iot_20180120_models.UpdateDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateDeviceGroupResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateDeviceGroupResponse(),
            await self.do_request_async('UpdateDeviceGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_device_group(
        self,
        request: iot_20180120_models.UpdateDeviceGroupRequest,
    ) -> iot_20180120_models.UpdateDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_device_group_with_options(request, runtime)

    async def update_device_group_async(
        self,
        request: iot_20180120_models.UpdateDeviceGroupRequest,
    ) -> iot_20180120_models.UpdateDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_device_group_with_options_async(request, runtime)

    def update_device_shadow_with_options(
        self,
        request: iot_20180120_models.UpdateDeviceShadowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateDeviceShadowResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateDeviceShadowResponse(),
            self.do_request('UpdateDeviceShadow', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_device_shadow_with_options_async(
        self,
        request: iot_20180120_models.UpdateDeviceShadowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateDeviceShadowResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateDeviceShadowResponse(),
            await self.do_request_async('UpdateDeviceShadow', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_device_shadow(
        self,
        request: iot_20180120_models.UpdateDeviceShadowRequest,
    ) -> iot_20180120_models.UpdateDeviceShadowResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_device_shadow_with_options(request, runtime)

    async def update_device_shadow_async(
        self,
        request: iot_20180120_models.UpdateDeviceShadowRequest,
    ) -> iot_20180120_models.UpdateDeviceShadowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_device_shadow_with_options_async(request, runtime)

    def update_edge_driver_version_with_options(
        self,
        request: iot_20180120_models.UpdateEdgeDriverVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateEdgeDriverVersionResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateEdgeDriverVersionResponse(),
            self.do_request('UpdateEdgeDriverVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_edge_driver_version_with_options_async(
        self,
        request: iot_20180120_models.UpdateEdgeDriverVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateEdgeDriverVersionResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateEdgeDriverVersionResponse(),
            await self.do_request_async('UpdateEdgeDriverVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_edge_driver_version(
        self,
        request: iot_20180120_models.UpdateEdgeDriverVersionRequest,
    ) -> iot_20180120_models.UpdateEdgeDriverVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_edge_driver_version_with_options(request, runtime)

    async def update_edge_driver_version_async(
        self,
        request: iot_20180120_models.UpdateEdgeDriverVersionRequest,
    ) -> iot_20180120_models.UpdateEdgeDriverVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_edge_driver_version_with_options_async(request, runtime)

    def update_edge_instance_with_options(
        self,
        request: iot_20180120_models.UpdateEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateEdgeInstanceResponse(),
            self.do_request('UpdateEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.UpdateEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateEdgeInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateEdgeInstanceResponse(),
            await self.do_request_async('UpdateEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_edge_instance(
        self,
        request: iot_20180120_models.UpdateEdgeInstanceRequest,
    ) -> iot_20180120_models.UpdateEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_edge_instance_with_options(request, runtime)

    async def update_edge_instance_async(
        self,
        request: iot_20180120_models.UpdateEdgeInstanceRequest,
    ) -> iot_20180120_models.UpdateEdgeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_edge_instance_with_options_async(request, runtime)

    def update_edge_instance_channel_with_options(
        self,
        request: iot_20180120_models.UpdateEdgeInstanceChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateEdgeInstanceChannelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateEdgeInstanceChannelResponse(),
            self.do_request('UpdateEdgeInstanceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_edge_instance_channel_with_options_async(
        self,
        request: iot_20180120_models.UpdateEdgeInstanceChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateEdgeInstanceChannelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateEdgeInstanceChannelResponse(),
            await self.do_request_async('UpdateEdgeInstanceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_edge_instance_channel(
        self,
        request: iot_20180120_models.UpdateEdgeInstanceChannelRequest,
    ) -> iot_20180120_models.UpdateEdgeInstanceChannelResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_edge_instance_channel_with_options(request, runtime)

    async def update_edge_instance_channel_async(
        self,
        request: iot_20180120_models.UpdateEdgeInstanceChannelRequest,
    ) -> iot_20180120_models.UpdateEdgeInstanceChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_edge_instance_channel_with_options_async(request, runtime)

    def update_edge_instance_message_routing_with_options(
        self,
        request: iot_20180120_models.UpdateEdgeInstanceMessageRoutingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateEdgeInstanceMessageRoutingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateEdgeInstanceMessageRoutingResponse(),
            self.do_request('UpdateEdgeInstanceMessageRouting', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_edge_instance_message_routing_with_options_async(
        self,
        request: iot_20180120_models.UpdateEdgeInstanceMessageRoutingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateEdgeInstanceMessageRoutingResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateEdgeInstanceMessageRoutingResponse(),
            await self.do_request_async('UpdateEdgeInstanceMessageRouting', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_edge_instance_message_routing(
        self,
        request: iot_20180120_models.UpdateEdgeInstanceMessageRoutingRequest,
    ) -> iot_20180120_models.UpdateEdgeInstanceMessageRoutingResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_edge_instance_message_routing_with_options(request, runtime)

    async def update_edge_instance_message_routing_async(
        self,
        request: iot_20180120_models.UpdateEdgeInstanceMessageRoutingRequest,
    ) -> iot_20180120_models.UpdateEdgeInstanceMessageRoutingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_edge_instance_message_routing_with_options_async(request, runtime)

    def update_job_with_options(
        self,
        tmp: iot_20180120_models.UpdateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateJobResponse:
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.UpdateJobShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.rollout_config):
            request.rollout_config_shrink = UtilClient.to_jsonstring(tmp.rollout_config)
        if not UtilClient.is_unset(tmp.timeout_config):
            request.timeout_config_shrink = UtilClient.to_jsonstring(tmp.timeout_config)
        return TeaCore.from_map(
            iot_20180120_models.UpdateJobResponse(),
            self.do_request('UpdateJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_job_with_options_async(
        self,
        tmp: iot_20180120_models.UpdateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateJobResponse:
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.UpdateJobShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.rollout_config):
            request.rollout_config_shrink = UtilClient.to_jsonstring(tmp.rollout_config)
        if not UtilClient.is_unset(tmp.timeout_config):
            request.timeout_config_shrink = UtilClient.to_jsonstring(tmp.timeout_config)
        return TeaCore.from_map(
            iot_20180120_models.UpdateJobResponse(),
            await self.do_request_async('UpdateJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_job(
        self,
        request: iot_20180120_models.UpdateJobRequest,
    ) -> iot_20180120_models.UpdateJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_job_with_options(request, runtime)

    async def update_job_async(
        self,
        request: iot_20180120_models.UpdateJobRequest,
    ) -> iot_20180120_models.UpdateJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_job_with_options_async(request, runtime)

    def update_otamodule_with_options(
        self,
        request: iot_20180120_models.UpdateOTAModuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateOTAModuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateOTAModuleResponse(),
            self.do_request('UpdateOTAModule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_otamodule_with_options_async(
        self,
        request: iot_20180120_models.UpdateOTAModuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateOTAModuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateOTAModuleResponse(),
            await self.do_request_async('UpdateOTAModule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_otamodule(
        self,
        request: iot_20180120_models.UpdateOTAModuleRequest,
    ) -> iot_20180120_models.UpdateOTAModuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_otamodule_with_options(request, runtime)

    async def update_otamodule_async(
        self,
        request: iot_20180120_models.UpdateOTAModuleRequest,
    ) -> iot_20180120_models.UpdateOTAModuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_otamodule_with_options_async(request, runtime)

    def update_parser_with_options(
        self,
        request: iot_20180120_models.UpdateParserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateParserResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateParserResponse(),
            self.do_request('UpdateParser', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_parser_with_options_async(
        self,
        request: iot_20180120_models.UpdateParserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateParserResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateParserResponse(),
            await self.do_request_async('UpdateParser', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_parser(
        self,
        request: iot_20180120_models.UpdateParserRequest,
    ) -> iot_20180120_models.UpdateParserResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_parser_with_options(request, runtime)

    async def update_parser_async(
        self,
        request: iot_20180120_models.UpdateParserRequest,
    ) -> iot_20180120_models.UpdateParserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_parser_with_options_async(request, runtime)

    def update_parser_data_source_with_options(
        self,
        request: iot_20180120_models.UpdateParserDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateParserDataSourceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateParserDataSourceResponse(),
            self.do_request('UpdateParserDataSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_parser_data_source_with_options_async(
        self,
        request: iot_20180120_models.UpdateParserDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateParserDataSourceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateParserDataSourceResponse(),
            await self.do_request_async('UpdateParserDataSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_parser_data_source(
        self,
        request: iot_20180120_models.UpdateParserDataSourceRequest,
    ) -> iot_20180120_models.UpdateParserDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_parser_data_source_with_options(request, runtime)

    async def update_parser_data_source_async(
        self,
        request: iot_20180120_models.UpdateParserDataSourceRequest,
    ) -> iot_20180120_models.UpdateParserDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_parser_data_source_with_options_async(request, runtime)

    def update_product_with_options(
        self,
        request: iot_20180120_models.UpdateProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateProductResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateProductResponse(),
            self.do_request('UpdateProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_product_with_options_async(
        self,
        request: iot_20180120_models.UpdateProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateProductResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateProductResponse(),
            await self.do_request_async('UpdateProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_product(
        self,
        request: iot_20180120_models.UpdateProductRequest,
    ) -> iot_20180120_models.UpdateProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_product_with_options(request, runtime)

    async def update_product_async(
        self,
        request: iot_20180120_models.UpdateProductRequest,
    ) -> iot_20180120_models.UpdateProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_product_with_options_async(request, runtime)

    def update_product_filter_config_with_options(
        self,
        request: iot_20180120_models.UpdateProductFilterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateProductFilterConfigResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateProductFilterConfigResponse(),
            self.do_request('UpdateProductFilterConfig', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_product_filter_config_with_options_async(
        self,
        request: iot_20180120_models.UpdateProductFilterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateProductFilterConfigResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateProductFilterConfigResponse(),
            await self.do_request_async('UpdateProductFilterConfig', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_product_filter_config(
        self,
        request: iot_20180120_models.UpdateProductFilterConfigRequest,
    ) -> iot_20180120_models.UpdateProductFilterConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_product_filter_config_with_options(request, runtime)

    async def update_product_filter_config_async(
        self,
        request: iot_20180120_models.UpdateProductFilterConfigRequest,
    ) -> iot_20180120_models.UpdateProductFilterConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_product_filter_config_with_options_async(request, runtime)

    def update_product_tags_with_options(
        self,
        request: iot_20180120_models.UpdateProductTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateProductTagsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateProductTagsResponse(),
            self.do_request('UpdateProductTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_product_tags_with_options_async(
        self,
        request: iot_20180120_models.UpdateProductTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateProductTagsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateProductTagsResponse(),
            await self.do_request_async('UpdateProductTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_product_tags(
        self,
        request: iot_20180120_models.UpdateProductTagsRequest,
    ) -> iot_20180120_models.UpdateProductTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_product_tags_with_options(request, runtime)

    async def update_product_tags_async(
        self,
        request: iot_20180120_models.UpdateProductTagsRequest,
    ) -> iot_20180120_models.UpdateProductTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_product_tags_with_options_async(request, runtime)

    def update_product_topic_with_options(
        self,
        request: iot_20180120_models.UpdateProductTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateProductTopicResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateProductTopicResponse(),
            self.do_request('UpdateProductTopic', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_product_topic_with_options_async(
        self,
        request: iot_20180120_models.UpdateProductTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateProductTopicResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateProductTopicResponse(),
            await self.do_request_async('UpdateProductTopic', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_product_topic(
        self,
        request: iot_20180120_models.UpdateProductTopicRequest,
    ) -> iot_20180120_models.UpdateProductTopicResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_product_topic_with_options(request, runtime)

    async def update_product_topic_async(
        self,
        request: iot_20180120_models.UpdateProductTopicRequest,
    ) -> iot_20180120_models.UpdateProductTopicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_product_topic_with_options_async(request, runtime)

    def update_rule_with_options(
        self,
        request: iot_20180120_models.UpdateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateRuleResponse(),
            self.do_request('UpdateRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_rule_with_options_async(
        self,
        request: iot_20180120_models.UpdateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateRuleResponse(),
            await self.do_request_async('UpdateRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_rule(
        self,
        request: iot_20180120_models.UpdateRuleRequest,
    ) -> iot_20180120_models.UpdateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_rule_with_options(request, runtime)

    async def update_rule_async(
        self,
        request: iot_20180120_models.UpdateRuleRequest,
    ) -> iot_20180120_models.UpdateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_rule_with_options_async(request, runtime)

    def update_rule_action_with_options(
        self,
        request: iot_20180120_models.UpdateRuleActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateRuleActionResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateRuleActionResponse(),
            self.do_request('UpdateRuleAction', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_rule_action_with_options_async(
        self,
        request: iot_20180120_models.UpdateRuleActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateRuleActionResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateRuleActionResponse(),
            await self.do_request_async('UpdateRuleAction', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_rule_action(
        self,
        request: iot_20180120_models.UpdateRuleActionRequest,
    ) -> iot_20180120_models.UpdateRuleActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_rule_action_with_options(request, runtime)

    async def update_rule_action_async(
        self,
        request: iot_20180120_models.UpdateRuleActionRequest,
    ) -> iot_20180120_models.UpdateRuleActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_rule_action_with_options_async(request, runtime)

    def update_scene_rule_with_options(
        self,
        request: iot_20180120_models.UpdateSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateSceneRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateSceneRuleResponse(),
            self.do_request('UpdateSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_scene_rule_with_options_async(
        self,
        request: iot_20180120_models.UpdateSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateSceneRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateSceneRuleResponse(),
            await self.do_request_async('UpdateSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_scene_rule(
        self,
        request: iot_20180120_models.UpdateSceneRuleRequest,
    ) -> iot_20180120_models.UpdateSceneRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_scene_rule_with_options(request, runtime)

    async def update_scene_rule_async(
        self,
        request: iot_20180120_models.UpdateSceneRuleRequest,
    ) -> iot_20180120_models.UpdateSceneRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_scene_rule_with_options_async(request, runtime)

    def update_schedule_period_with_options(
        self,
        request: iot_20180120_models.UpdateSchedulePeriodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateSchedulePeriodResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateSchedulePeriodResponse(),
            self.do_request('UpdateSchedulePeriod', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_schedule_period_with_options_async(
        self,
        request: iot_20180120_models.UpdateSchedulePeriodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateSchedulePeriodResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateSchedulePeriodResponse(),
            await self.do_request_async('UpdateSchedulePeriod', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_schedule_period(
        self,
        request: iot_20180120_models.UpdateSchedulePeriodRequest,
    ) -> iot_20180120_models.UpdateSchedulePeriodResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_schedule_period_with_options(request, runtime)

    async def update_schedule_period_async(
        self,
        request: iot_20180120_models.UpdateSchedulePeriodRequest,
    ) -> iot_20180120_models.UpdateSchedulePeriodResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_schedule_period_with_options_async(request, runtime)

    def update_sound_code_with_options(
        self,
        request: iot_20180120_models.UpdateSoundCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateSoundCodeResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateSoundCodeResponse(),
            self.do_request('UpdateSoundCode', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_sound_code_with_options_async(
        self,
        request: iot_20180120_models.UpdateSoundCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateSoundCodeResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateSoundCodeResponse(),
            await self.do_request_async('UpdateSoundCode', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_sound_code(
        self,
        request: iot_20180120_models.UpdateSoundCodeRequest,
    ) -> iot_20180120_models.UpdateSoundCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_sound_code_with_options(request, runtime)

    async def update_sound_code_async(
        self,
        request: iot_20180120_models.UpdateSoundCodeRequest,
    ) -> iot_20180120_models.UpdateSoundCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_sound_code_with_options_async(request, runtime)

    def update_sound_code_label_with_options(
        self,
        request: iot_20180120_models.UpdateSoundCodeLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateSoundCodeLabelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateSoundCodeLabelResponse(),
            self.do_request('UpdateSoundCodeLabel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_sound_code_label_with_options_async(
        self,
        request: iot_20180120_models.UpdateSoundCodeLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateSoundCodeLabelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateSoundCodeLabelResponse(),
            await self.do_request_async('UpdateSoundCodeLabel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_sound_code_label(
        self,
        request: iot_20180120_models.UpdateSoundCodeLabelRequest,
    ) -> iot_20180120_models.UpdateSoundCodeLabelResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_sound_code_label_with_options(request, runtime)

    async def update_sound_code_label_async(
        self,
        request: iot_20180120_models.UpdateSoundCodeLabelRequest,
    ) -> iot_20180120_models.UpdateSoundCodeLabelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_sound_code_label_with_options_async(request, runtime)

    def update_sound_code_schedule_with_options(
        self,
        request: iot_20180120_models.UpdateSoundCodeScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateSoundCodeScheduleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateSoundCodeScheduleResponse(),
            self.do_request('UpdateSoundCodeSchedule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_sound_code_schedule_with_options_async(
        self,
        request: iot_20180120_models.UpdateSoundCodeScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateSoundCodeScheduleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateSoundCodeScheduleResponse(),
            await self.do_request_async('UpdateSoundCodeSchedule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_sound_code_schedule(
        self,
        request: iot_20180120_models.UpdateSoundCodeScheduleRequest,
    ) -> iot_20180120_models.UpdateSoundCodeScheduleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_sound_code_schedule_with_options(request, runtime)

    async def update_sound_code_schedule_async(
        self,
        request: iot_20180120_models.UpdateSoundCodeScheduleRequest,
    ) -> iot_20180120_models.UpdateSoundCodeScheduleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_sound_code_schedule_with_options_async(request, runtime)

    def update_speech_with_options(
        self,
        tmp: iot_20180120_models.UpdateSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateSpeechResponse:
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.UpdateSpeechShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.sound_code_config):
            request.sound_code_config_shrink = UtilClient.to_jsonstring(tmp.sound_code_config)
        return TeaCore.from_map(
            iot_20180120_models.UpdateSpeechResponse(),
            self.do_request('UpdateSpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_speech_with_options_async(
        self,
        tmp: iot_20180120_models.UpdateSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateSpeechResponse:
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.UpdateSpeechShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.sound_code_config):
            request.sound_code_config_shrink = UtilClient.to_jsonstring(tmp.sound_code_config)
        return TeaCore.from_map(
            iot_20180120_models.UpdateSpeechResponse(),
            await self.do_request_async('UpdateSpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_speech(
        self,
        request: iot_20180120_models.UpdateSpeechRequest,
    ) -> iot_20180120_models.UpdateSpeechResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_speech_with_options(request, runtime)

    async def update_speech_async(
        self,
        request: iot_20180120_models.UpdateSpeechRequest,
    ) -> iot_20180120_models.UpdateSpeechResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_speech_with_options_async(request, runtime)

    def update_subscribe_relation_with_options(
        self,
        request: iot_20180120_models.UpdateSubscribeRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateSubscribeRelationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateSubscribeRelationResponse(),
            self.do_request('UpdateSubscribeRelation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_subscribe_relation_with_options_async(
        self,
        request: iot_20180120_models.UpdateSubscribeRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateSubscribeRelationResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateSubscribeRelationResponse(),
            await self.do_request_async('UpdateSubscribeRelation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_subscribe_relation(
        self,
        request: iot_20180120_models.UpdateSubscribeRelationRequest,
    ) -> iot_20180120_models.UpdateSubscribeRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_subscribe_relation_with_options(request, runtime)

    async def update_subscribe_relation_async(
        self,
        request: iot_20180120_models.UpdateSubscribeRelationRequest,
    ) -> iot_20180120_models.UpdateSubscribeRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_subscribe_relation_with_options_async(request, runtime)

    def update_thing_model_with_options(
        self,
        request: iot_20180120_models.UpdateThingModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateThingModelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateThingModelResponse(),
            self.do_request('UpdateThingModel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_thing_model_with_options_async(
        self,
        request: iot_20180120_models.UpdateThingModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateThingModelResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateThingModelResponse(),
            await self.do_request_async('UpdateThingModel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_thing_model(
        self,
        request: iot_20180120_models.UpdateThingModelRequest,
    ) -> iot_20180120_models.UpdateThingModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_thing_model_with_options(request, runtime)

    async def update_thing_model_async(
        self,
        request: iot_20180120_models.UpdateThingModelRequest,
    ) -> iot_20180120_models.UpdateThingModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_thing_model_with_options_async(request, runtime)

    def update_thing_script_with_options(
        self,
        request: iot_20180120_models.UpdateThingScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateThingScriptResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateThingScriptResponse(),
            self.do_request('UpdateThingScript', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_thing_script_with_options_async(
        self,
        request: iot_20180120_models.UpdateThingScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateThingScriptResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateThingScriptResponse(),
            await self.do_request_async('UpdateThingScript', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_thing_script(
        self,
        request: iot_20180120_models.UpdateThingScriptRequest,
    ) -> iot_20180120_models.UpdateThingScriptResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_thing_script_with_options(request, runtime)

    async def update_thing_script_async(
        self,
        request: iot_20180120_models.UpdateThingScriptRequest,
    ) -> iot_20180120_models.UpdateThingScriptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_thing_script_with_options_async(request, runtime)

    def write_devices_hot_storage_data_with_options(
        self,
        request: iot_20180120_models.WriteDevicesHotStorageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.WriteDevicesHotStorageDataResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.WriteDevicesHotStorageDataResponse(),
            self.do_request('WriteDevicesHotStorageData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def write_devices_hot_storage_data_with_options_async(
        self,
        request: iot_20180120_models.WriteDevicesHotStorageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.WriteDevicesHotStorageDataResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.WriteDevicesHotStorageDataResponse(),
            await self.do_request_async('WriteDevicesHotStorageData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def write_devices_hot_storage_data(
        self,
        request: iot_20180120_models.WriteDevicesHotStorageDataRequest,
    ) -> iot_20180120_models.WriteDevicesHotStorageDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.write_devices_hot_storage_data_with_options(request, runtime)

    async def write_devices_hot_storage_data_async(
        self,
        request: iot_20180120_models.WriteDevicesHotStorageDataRequest,
    ) -> iot_20180120_models.WriteDevicesHotStorageDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.write_devices_hot_storage_data_with_options_async(request, runtime)

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
