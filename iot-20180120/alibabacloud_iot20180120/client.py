# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_iot20180120 import models as iot_20180120_models
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

    def add_data_for_api_source_with_options(
        self,
        request: iot_20180120_models.AddDataForApiSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.AddDataForApiSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.AddDataForApiSourceResponse(),
            self.do_rpcrequest('AddDataForApiSource', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_data_for_api_source_with_options_async(
        self,
        request: iot_20180120_models.AddDataForApiSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.AddDataForApiSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.AddDataForApiSourceResponse(),
            await self.do_rpcrequest_async('AddDataForApiSource', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def batch_add_device_group_relations_with_options(
        self,
        request: iot_20180120_models.BatchAddDeviceGroupRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchAddDeviceGroupRelationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchAddDeviceGroupRelationsResponse(),
            self.do_rpcrequest('BatchAddDeviceGroupRelations', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_add_device_group_relations_with_options_async(
        self,
        request: iot_20180120_models.BatchAddDeviceGroupRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchAddDeviceGroupRelationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchAddDeviceGroupRelationsResponse(),
            await self.do_rpcrequest_async('BatchAddDeviceGroupRelations', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchAddThingTopoResponse(),
            self.do_rpcrequest('BatchAddThingTopo', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_add_thing_topo_with_options_async(
        self,
        request: iot_20180120_models.BatchAddThingTopoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchAddThingTopoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchAddThingTopoResponse(),
            await self.do_rpcrequest_async('BatchAddThingTopo', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def batch_bind_devices_into_project_with_options(
        self,
        request: iot_20180120_models.BatchBindDevicesIntoProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchBindDevicesIntoProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchBindDevicesIntoProjectResponse(),
            self.do_rpcrequest('BatchBindDevicesIntoProject', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_bind_devices_into_project_with_options_async(
        self,
        request: iot_20180120_models.BatchBindDevicesIntoProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchBindDevicesIntoProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchBindDevicesIntoProjectResponse(),
            await self.do_rpcrequest_async('BatchBindDevicesIntoProject', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def batch_bind_device_to_edge_instance_with_driver_with_options(
        self,
        request: iot_20180120_models.BatchBindDeviceToEdgeInstanceWithDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchBindDeviceToEdgeInstanceWithDriverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchBindDeviceToEdgeInstanceWithDriverResponse(),
            self.do_rpcrequest('BatchBindDeviceToEdgeInstanceWithDriver', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_bind_device_to_edge_instance_with_driver_with_options_async(
        self,
        request: iot_20180120_models.BatchBindDeviceToEdgeInstanceWithDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchBindDeviceToEdgeInstanceWithDriverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchBindDeviceToEdgeInstanceWithDriverResponse(),
            await self.do_rpcrequest_async('BatchBindDeviceToEdgeInstanceWithDriver', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def batch_bind_products_into_project_with_options(
        self,
        request: iot_20180120_models.BatchBindProductsIntoProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchBindProductsIntoProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchBindProductsIntoProjectResponse(),
            self.do_rpcrequest('BatchBindProductsIntoProject', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_bind_products_into_project_with_options_async(
        self,
        request: iot_20180120_models.BatchBindProductsIntoProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchBindProductsIntoProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchBindProductsIntoProjectResponse(),
            await self.do_rpcrequest_async('BatchBindProductsIntoProject', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchCheckDeviceNamesResponse(),
            self.do_rpcrequest('BatchCheckDeviceNames', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_check_device_names_with_options_async(
        self,
        request: iot_20180120_models.BatchCheckDeviceNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchCheckDeviceNamesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchCheckDeviceNamesResponse(),
            await self.do_rpcrequest_async('BatchCheckDeviceNames', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def batch_clear_edge_instance_device_config_with_options(
        self,
        request: iot_20180120_models.BatchClearEdgeInstanceDeviceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchClearEdgeInstanceDeviceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchClearEdgeInstanceDeviceConfigResponse(),
            self.do_rpcrequest('BatchClearEdgeInstanceDeviceConfig', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_clear_edge_instance_device_config_with_options_async(
        self,
        request: iot_20180120_models.BatchClearEdgeInstanceDeviceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchClearEdgeInstanceDeviceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchClearEdgeInstanceDeviceConfigResponse(),
            await self.do_rpcrequest_async('BatchClearEdgeInstanceDeviceConfig', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def batch_delete_device_group_relations_with_options(
        self,
        request: iot_20180120_models.BatchDeleteDeviceGroupRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchDeleteDeviceGroupRelationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchDeleteDeviceGroupRelationsResponse(),
            self.do_rpcrequest('BatchDeleteDeviceGroupRelations', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_delete_device_group_relations_with_options_async(
        self,
        request: iot_20180120_models.BatchDeleteDeviceGroupRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchDeleteDeviceGroupRelationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchDeleteDeviceGroupRelationsResponse(),
            await self.do_rpcrequest_async('BatchDeleteDeviceGroupRelations', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchDeleteEdgeInstanceChannelResponse(),
            self.do_rpcrequest('BatchDeleteEdgeInstanceChannel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_delete_edge_instance_channel_with_options_async(
        self,
        request: iot_20180120_models.BatchDeleteEdgeInstanceChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchDeleteEdgeInstanceChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchDeleteEdgeInstanceChannelResponse(),
            await self.do_rpcrequest_async('BatchDeleteEdgeInstanceChannel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchGetDeviceBindStatusResponse(),
            self.do_rpcrequest('BatchGetDeviceBindStatus', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_get_device_bind_status_with_options_async(
        self,
        request: iot_20180120_models.BatchGetDeviceBindStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchGetDeviceBindStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchGetDeviceBindStatusResponse(),
            await self.do_rpcrequest_async('BatchGetDeviceBindStatus', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchGetDeviceStateResponse(),
            self.do_rpcrequest('BatchGetDeviceState', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_get_device_state_with_options_async(
        self,
        request: iot_20180120_models.BatchGetDeviceStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchGetDeviceStateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchGetDeviceStateResponse(),
            await self.do_rpcrequest_async('BatchGetDeviceState', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeDriverResponse(),
            self.do_rpcrequest('BatchGetEdgeDriver', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_get_edge_driver_with_options_async(
        self,
        request: iot_20180120_models.BatchGetEdgeDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchGetEdgeDriverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeDriverResponse(),
            await self.do_rpcrequest_async('BatchGetEdgeDriver', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceChannelResponse(),
            self.do_rpcrequest('BatchGetEdgeInstanceChannel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_get_edge_instance_channel_with_options_async(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchGetEdgeInstanceChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceChannelResponse(),
            await self.do_rpcrequest_async('BatchGetEdgeInstanceChannel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceDeviceChannelResponse(),
            self.do_rpcrequest('BatchGetEdgeInstanceDeviceChannel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_get_edge_instance_device_channel_with_options_async(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceDeviceChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchGetEdgeInstanceDeviceChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceDeviceChannelResponse(),
            await self.do_rpcrequest_async('BatchGetEdgeInstanceDeviceChannel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceDeviceConfigResponse(),
            self.do_rpcrequest('BatchGetEdgeInstanceDeviceConfig', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_get_edge_instance_device_config_with_options_async(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceDeviceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchGetEdgeInstanceDeviceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceDeviceConfigResponse(),
            await self.do_rpcrequest_async('BatchGetEdgeInstanceDeviceConfig', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceDeviceDriverResponse(),
            self.do_rpcrequest('BatchGetEdgeInstanceDeviceDriver', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_get_edge_instance_device_driver_with_options_async(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceDeviceDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchGetEdgeInstanceDeviceDriverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceDeviceDriverResponse(),
            await self.do_rpcrequest_async('BatchGetEdgeInstanceDeviceDriver', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceDriverConfigsResponse(),
            self.do_rpcrequest('BatchGetEdgeInstanceDriverConfigs', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_get_edge_instance_driver_configs_with_options_async(
        self,
        request: iot_20180120_models.BatchGetEdgeInstanceDriverConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchGetEdgeInstanceDriverConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceDriverConfigsResponse(),
            await self.do_rpcrequest_async('BatchGetEdgeInstanceDriverConfigs', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def batch_pub_with_options(
        self,
        request: iot_20180120_models.BatchPubRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchPubResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchPubResponse(),
            self.do_rpcrequest('BatchPub', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_pub_with_options_async(
        self,
        request: iot_20180120_models.BatchPubRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchPubResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchPubResponse(),
            await self.do_rpcrequest_async('BatchPub', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchQueryDeviceDetailResponse(),
            self.do_rpcrequest('BatchQueryDeviceDetail', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_query_device_detail_with_options_async(
        self,
        request: iot_20180120_models.BatchQueryDeviceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchQueryDeviceDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchQueryDeviceDetailResponse(),
            await self.do_rpcrequest_async('BatchQueryDeviceDetail', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchRegisterDeviceResponse(),
            self.do_rpcrequest('BatchRegisterDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_register_device_with_options_async(
        self,
        request: iot_20180120_models.BatchRegisterDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchRegisterDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchRegisterDeviceResponse(),
            await self.do_rpcrequest_async('BatchRegisterDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchRegisterDeviceWithApplyIdResponse(),
            self.do_rpcrequest('BatchRegisterDeviceWithApplyId', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_register_device_with_apply_id_with_options_async(
        self,
        request: iot_20180120_models.BatchRegisterDeviceWithApplyIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchRegisterDeviceWithApplyIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchRegisterDeviceWithApplyIdResponse(),
            await self.do_rpcrequest_async('BatchRegisterDeviceWithApplyId', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchSetEdgeInstanceDeviceChannelResponse(),
            self.do_rpcrequest('BatchSetEdgeInstanceDeviceChannel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_set_edge_instance_device_channel_with_options_async(
        self,
        request: iot_20180120_models.BatchSetEdgeInstanceDeviceChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchSetEdgeInstanceDeviceChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchSetEdgeInstanceDeviceChannelResponse(),
            await self.do_rpcrequest_async('BatchSetEdgeInstanceDeviceChannel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchSetEdgeInstanceDeviceConfigResponse(),
            self.do_rpcrequest('BatchSetEdgeInstanceDeviceConfig', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_set_edge_instance_device_config_with_options_async(
        self,
        request: iot_20180120_models.BatchSetEdgeInstanceDeviceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchSetEdgeInstanceDeviceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchSetEdgeInstanceDeviceConfigResponse(),
            await self.do_rpcrequest_async('BatchSetEdgeInstanceDeviceConfig', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchUnbindDeviceFromEdgeInstanceResponse(),
            self.do_rpcrequest('BatchUnbindDeviceFromEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_unbind_device_from_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.BatchUnbindDeviceFromEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchUnbindDeviceFromEdgeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchUnbindDeviceFromEdgeInstanceResponse(),
            await self.do_rpcrequest_async('BatchUnbindDeviceFromEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchUnbindProjectDevicesResponse(),
            self.do_rpcrequest('BatchUnbindProjectDevices', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_unbind_project_devices_with_options_async(
        self,
        request: iot_20180120_models.BatchUnbindProjectDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchUnbindProjectDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchUnbindProjectDevicesResponse(),
            await self.do_rpcrequest_async('BatchUnbindProjectDevices', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchUnbindProjectProductsResponse(),
            self.do_rpcrequest('BatchUnbindProjectProducts', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_unbind_project_products_with_options_async(
        self,
        request: iot_20180120_models.BatchUnbindProjectProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchUnbindProjectProductsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchUnbindProjectProductsResponse(),
            await self.do_rpcrequest_async('BatchUnbindProjectProducts', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchUpdateDeviceNicknameResponse(),
            self.do_rpcrequest('BatchUpdateDeviceNickname', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_update_device_nickname_with_options_async(
        self,
        request: iot_20180120_models.BatchUpdateDeviceNicknameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchUpdateDeviceNicknameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchUpdateDeviceNicknameResponse(),
            await self.do_rpcrequest_async('BatchUpdateDeviceNickname', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BindApplicationToEdgeInstanceResponse(),
            self.do_rpcrequest('BindApplicationToEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_application_to_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.BindApplicationToEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BindApplicationToEdgeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BindApplicationToEdgeInstanceResponse(),
            await self.do_rpcrequest_async('BindApplicationToEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BindDriverToEdgeInstanceResponse(),
            self.do_rpcrequest('BindDriverToEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_driver_to_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.BindDriverToEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BindDriverToEdgeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BindDriverToEdgeInstanceResponse(),
            await self.do_rpcrequest_async('BindDriverToEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BindGatewayToEdgeInstanceResponse(),
            self.do_rpcrequest('BindGatewayToEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_gateway_to_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.BindGatewayToEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BindGatewayToEdgeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BindGatewayToEdgeInstanceResponse(),
            await self.do_rpcrequest_async('BindGatewayToEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def bind_role_to_edge_instance_with_options(
        self,
        request: iot_20180120_models.BindRoleToEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BindRoleToEdgeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BindRoleToEdgeInstanceResponse(),
            self.do_rpcrequest('BindRoleToEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_role_to_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.BindRoleToEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BindRoleToEdgeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BindRoleToEdgeInstanceResponse(),
            await self.do_rpcrequest_async('BindRoleToEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BindSceneRuleToEdgeInstanceResponse(),
            self.do_rpcrequest('BindSceneRuleToEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_scene_rule_to_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.BindSceneRuleToEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BindSceneRuleToEdgeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.BindSceneRuleToEdgeInstanceResponse(),
            await self.do_rpcrequest_async('BindSceneRuleToEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CancelJobResponse(),
            self.do_rpcrequest('CancelJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_job_with_options_async(
        self,
        request: iot_20180120_models.CancelJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CancelJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CancelJobResponse(),
            await self.do_rpcrequest_async('CancelJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CancelOTAStrategyByJobResponse(),
            self.do_rpcrequest('CancelOTAStrategyByJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_otastrategy_by_job_with_options_async(
        self,
        request: iot_20180120_models.CancelOTAStrategyByJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CancelOTAStrategyByJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CancelOTAStrategyByJobResponse(),
            await self.do_rpcrequest_async('CancelOTAStrategyByJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CancelOTATaskByDeviceResponse(),
            self.do_rpcrequest('CancelOTATaskByDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_otatask_by_device_with_options_async(
        self,
        request: iot_20180120_models.CancelOTATaskByDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CancelOTATaskByDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CancelOTATaskByDeviceResponse(),
            await self.do_rpcrequest_async('CancelOTATaskByDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CancelOTATaskByJobResponse(),
            self.do_rpcrequest('CancelOTATaskByJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_otatask_by_job_with_options_async(
        self,
        request: iot_20180120_models.CancelOTATaskByJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CancelOTATaskByJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CancelOTATaskByJobResponse(),
            await self.do_rpcrequest_async('CancelOTATaskByJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CancelReleaseProductResponse(),
            self.do_rpcrequest('CancelReleaseProduct', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_release_product_with_options_async(
        self,
        request: iot_20180120_models.CancelReleaseProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CancelReleaseProductResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CancelReleaseProductResponse(),
            await self.do_rpcrequest_async('CancelReleaseProduct', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def clear_edge_instance_driver_configs_with_options(
        self,
        request: iot_20180120_models.ClearEdgeInstanceDriverConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ClearEdgeInstanceDriverConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ClearEdgeInstanceDriverConfigsResponse(),
            self.do_rpcrequest('ClearEdgeInstanceDriverConfigs', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def clear_edge_instance_driver_configs_with_options_async(
        self,
        request: iot_20180120_models.ClearEdgeInstanceDriverConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ClearEdgeInstanceDriverConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ClearEdgeInstanceDriverConfigsResponse(),
            await self.do_rpcrequest_async('ClearEdgeInstanceDriverConfigs', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def close_edge_instance_deployment_with_options(
        self,
        request: iot_20180120_models.CloseEdgeInstanceDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CloseEdgeInstanceDeploymentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CloseEdgeInstanceDeploymentResponse(),
            self.do_rpcrequest('CloseEdgeInstanceDeployment', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def close_edge_instance_deployment_with_options_async(
        self,
        request: iot_20180120_models.CloseEdgeInstanceDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CloseEdgeInstanceDeploymentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CloseEdgeInstanceDeploymentResponse(),
            await self.do_rpcrequest_async('CloseEdgeInstanceDeployment', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ConfirmOTATaskResponse(),
            self.do_rpcrequest('ConfirmOTATask', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def confirm_otatask_with_options_async(
        self,
        request: iot_20180120_models.ConfirmOTATaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ConfirmOTATaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ConfirmOTATaskResponse(),
            await self.do_rpcrequest_async('ConfirmOTATask', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CopyThingModelResponse(),
            self.do_rpcrequest('CopyThingModel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def copy_thing_model_with_options_async(
        self,
        request: iot_20180120_models.CopyThingModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CopyThingModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CopyThingModelResponse(),
            await self.do_rpcrequest_async('CopyThingModel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_consumer_group_with_options(
        self,
        request: iot_20180120_models.CreateConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateConsumerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateConsumerGroupResponse(),
            self.do_rpcrequest('CreateConsumerGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_consumer_group_with_options_async(
        self,
        request: iot_20180120_models.CreateConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateConsumerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateConsumerGroupResponse(),
            await self.do_rpcrequest_async('CreateConsumerGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateConsumerGroupSubscribeRelationResponse(),
            self.do_rpcrequest('CreateConsumerGroupSubscribeRelation', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_consumer_group_subscribe_relation_with_options_async(
        self,
        request: iot_20180120_models.CreateConsumerGroupSubscribeRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateConsumerGroupSubscribeRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateConsumerGroupSubscribeRelationResponse(),
            await self.do_rpcrequest_async('CreateConsumerGroupSubscribeRelation', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateDataAPIServiceResponse(),
            self.do_rpcrequest('CreateDataAPIService', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_data_apiservice_with_options_async(
        self,
        request: iot_20180120_models.CreateDataAPIServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateDataAPIServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateDataAPIServiceResponse(),
            await self.do_rpcrequest_async('CreateDataAPIService', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_device_distribute_job_with_options(
        self,
        request: iot_20180120_models.CreateDeviceDistributeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateDeviceDistributeJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateDeviceDistributeJobResponse(),
            self.do_rpcrequest('CreateDeviceDistributeJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_device_distribute_job_with_options_async(
        self,
        request: iot_20180120_models.CreateDeviceDistributeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateDeviceDistributeJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateDeviceDistributeJobResponse(),
            await self.do_rpcrequest_async('CreateDeviceDistributeJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_device_group_with_options(
        self,
        request: iot_20180120_models.CreateDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateDeviceGroupResponse(),
            self.do_rpcrequest('CreateDeviceGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_device_group_with_options_async(
        self,
        request: iot_20180120_models.CreateDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateDeviceGroupResponse(),
            await self.do_rpcrequest_async('CreateDeviceGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_edge_driver_with_options(
        self,
        request: iot_20180120_models.CreateEdgeDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateEdgeDriverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeDriverResponse(),
            self.do_rpcrequest('CreateEdgeDriver', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_edge_driver_with_options_async(
        self,
        request: iot_20180120_models.CreateEdgeDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateEdgeDriverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeDriverResponse(),
            await self.do_rpcrequest_async('CreateEdgeDriver', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeDriverVersionResponse(),
            self.do_rpcrequest('CreateEdgeDriverVersion', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_edge_driver_version_with_options_async(
        self,
        request: iot_20180120_models.CreateEdgeDriverVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateEdgeDriverVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeDriverVersionResponse(),
            await self.do_rpcrequest_async('CreateEdgeDriverVersion', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeInstanceResponse(),
            self.do_rpcrequest('CreateEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.CreateEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateEdgeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeInstanceResponse(),
            await self.do_rpcrequest_async('CreateEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeInstanceChannelResponse(),
            self.do_rpcrequest('CreateEdgeInstanceChannel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_edge_instance_channel_with_options_async(
        self,
        request: iot_20180120_models.CreateEdgeInstanceChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateEdgeInstanceChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeInstanceChannelResponse(),
            await self.do_rpcrequest_async('CreateEdgeInstanceChannel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeInstanceDeploymentResponse(),
            self.do_rpcrequest('CreateEdgeInstanceDeployment', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_edge_instance_deployment_with_options_async(
        self,
        request: iot_20180120_models.CreateEdgeInstanceDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateEdgeInstanceDeploymentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeInstanceDeploymentResponse(),
            await self.do_rpcrequest_async('CreateEdgeInstanceDeployment', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeInstanceMessageRoutingResponse(),
            self.do_rpcrequest('CreateEdgeInstanceMessageRouting', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_edge_instance_message_routing_with_options_async(
        self,
        request: iot_20180120_models.CreateEdgeInstanceMessageRoutingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateEdgeInstanceMessageRoutingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeInstanceMessageRoutingResponse(),
            await self.do_rpcrequest_async('CreateEdgeInstanceMessageRouting', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeOssPreSignedAddressResponse(),
            self.do_rpcrequest('CreateEdgeOssPreSignedAddress', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_edge_oss_pre_signed_address_with_options_async(
        self,
        request: iot_20180120_models.CreateEdgeOssPreSignedAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateEdgeOssPreSignedAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeOssPreSignedAddressResponse(),
            await self.do_rpcrequest_async('CreateEdgeOssPreSignedAddress', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        request: iot_20180120_models.CreateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateJobResponse(),
            self.do_rpcrequest('CreateJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_job_with_options_async(
        self,
        request: iot_20180120_models.CreateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateJobResponse(),
            await self.do_rpcrequest_async('CreateJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateLoRaNodesTaskResponse(),
            self.do_rpcrequest('CreateLoRaNodesTask', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_lo_ra_nodes_task_with_options_async(
        self,
        request: iot_20180120_models.CreateLoRaNodesTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateLoRaNodesTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateLoRaNodesTaskResponse(),
            await self.do_rpcrequest_async('CreateLoRaNodesTask', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateOTADynamicUpgradeJobResponse(),
            self.do_rpcrequest('CreateOTADynamicUpgradeJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_otadynamic_upgrade_job_with_options_async(
        self,
        request: iot_20180120_models.CreateOTADynamicUpgradeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateOTADynamicUpgradeJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateOTADynamicUpgradeJobResponse(),
            await self.do_rpcrequest_async('CreateOTADynamicUpgradeJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateOTAFirmwareResponse(),
            self.do_rpcrequest('CreateOTAFirmware', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_otafirmware_with_options_async(
        self,
        request: iot_20180120_models.CreateOTAFirmwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateOTAFirmwareResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateOTAFirmwareResponse(),
            await self.do_rpcrequest_async('CreateOTAFirmware', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateOTAModuleResponse(),
            self.do_rpcrequest('CreateOTAModule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_otamodule_with_options_async(
        self,
        request: iot_20180120_models.CreateOTAModuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateOTAModuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateOTAModuleResponse(),
            await self.do_rpcrequest_async('CreateOTAModule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateOTAStaticUpgradeJobResponse(),
            self.do_rpcrequest('CreateOTAStaticUpgradeJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_otastatic_upgrade_job_with_options_async(
        self,
        request: iot_20180120_models.CreateOTAStaticUpgradeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateOTAStaticUpgradeJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateOTAStaticUpgradeJobResponse(),
            await self.do_rpcrequest_async('CreateOTAStaticUpgradeJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateOTAVerifyJobResponse(),
            self.do_rpcrequest('CreateOTAVerifyJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_otaverify_job_with_options_async(
        self,
        request: iot_20180120_models.CreateOTAVerifyJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateOTAVerifyJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateOTAVerifyJobResponse(),
            await self.do_rpcrequest_async('CreateOTAVerifyJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_product_with_options(
        self,
        request: iot_20180120_models.CreateProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateProductResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateProductResponse(),
            self.do_rpcrequest('CreateProduct', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_product_with_options_async(
        self,
        request: iot_20180120_models.CreateProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateProductResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateProductResponse(),
            await self.do_rpcrequest_async('CreateProduct', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateProductDistributeJobResponse(),
            self.do_rpcrequest('CreateProductDistributeJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_product_distribute_job_with_options_async(
        self,
        request: iot_20180120_models.CreateProductDistributeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateProductDistributeJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateProductDistributeJobResponse(),
            await self.do_rpcrequest_async('CreateProductDistributeJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateProductTagsResponse(),
            self.do_rpcrequest('CreateProductTags', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_product_tags_with_options_async(
        self,
        request: iot_20180120_models.CreateProductTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateProductTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateProductTagsResponse(),
            await self.do_rpcrequest_async('CreateProductTags', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateProductTopicResponse(),
            self.do_rpcrequest('CreateProductTopic', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_product_topic_with_options_async(
        self,
        request: iot_20180120_models.CreateProductTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateProductTopicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateProductTopicResponse(),
            await self.do_rpcrequest_async('CreateProductTopic', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateRuleResponse(),
            self.do_rpcrequest('CreateRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_rule_with_options_async(
        self,
        request: iot_20180120_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateRuleResponse(),
            await self.do_rpcrequest_async('CreateRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateRuleActionResponse(),
            self.do_rpcrequest('CreateRuleAction', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_rule_action_with_options_async(
        self,
        request: iot_20180120_models.CreateRuleActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateRuleActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateRuleActionResponse(),
            await self.do_rpcrequest_async('CreateRuleAction', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_ruleng_distribute_job_with_options(
        self,
        request: iot_20180120_models.CreateRulengDistributeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateRulengDistributeJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateRulengDistributeJobResponse(),
            self.do_rpcrequest('CreateRulengDistributeJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ruleng_distribute_job_with_options_async(
        self,
        request: iot_20180120_models.CreateRulengDistributeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateRulengDistributeJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateRulengDistributeJobResponse(),
            await self.do_rpcrequest_async('CreateRulengDistributeJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ruleng_distribute_job(
        self,
        request: iot_20180120_models.CreateRulengDistributeJobRequest,
    ) -> iot_20180120_models.CreateRulengDistributeJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ruleng_distribute_job_with_options(request, runtime)

    async def create_ruleng_distribute_job_async(
        self,
        request: iot_20180120_models.CreateRulengDistributeJobRequest,
    ) -> iot_20180120_models.CreateRulengDistributeJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ruleng_distribute_job_with_options_async(request, runtime)

    def create_scene_rule_with_options(
        self,
        request: iot_20180120_models.CreateSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateSceneRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateSceneRuleResponse(),
            self.do_rpcrequest('CreateSceneRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_scene_rule_with_options_async(
        self,
        request: iot_20180120_models.CreateSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateSceneRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateSceneRuleResponse(),
            await self.do_rpcrequest_async('CreateSceneRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_speech_with_options(
        self,
        request: iot_20180120_models.CreateSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateSpeechResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateSpeechResponse(),
            self.do_rpcrequest('CreateSpeech', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_speech_with_options_async(
        self,
        request: iot_20180120_models.CreateSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateSpeechResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateSpeechResponse(),
            await self.do_rpcrequest_async('CreateSpeech', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateStudioAppDomainOpenResponse(),
            self.do_rpcrequest('CreateStudioAppDomainOpen', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_studio_app_domain_open_with_options_async(
        self,
        request: iot_20180120_models.CreateStudioAppDomainOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateStudioAppDomainOpenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateStudioAppDomainOpenResponse(),
            await self.do_rpcrequest_async('CreateStudioAppDomainOpen', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateSubscribeRelationResponse(),
            self.do_rpcrequest('CreateSubscribeRelation', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_subscribe_relation_with_options_async(
        self,
        request: iot_20180120_models.CreateSubscribeRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateSubscribeRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateSubscribeRelationResponse(),
            await self.do_rpcrequest_async('CreateSubscribeRelation', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateThingModelResponse(),
            self.do_rpcrequest('CreateThingModel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_thing_model_with_options_async(
        self,
        request: iot_20180120_models.CreateThingModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateThingModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateThingModelResponse(),
            await self.do_rpcrequest_async('CreateThingModel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateThingScriptResponse(),
            self.do_rpcrequest('CreateThingScript', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_thing_script_with_options_async(
        self,
        request: iot_20180120_models.CreateThingScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateThingScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateThingScriptResponse(),
            await self.do_rpcrequest_async('CreateThingScript', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateTopicRouteTableResponse(),
            self.do_rpcrequest('CreateTopicRouteTable', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_topic_route_table_with_options_async(
        self,
        request: iot_20180120_models.CreateTopicRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateTopicRouteTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateTopicRouteTableResponse(),
            await self.do_rpcrequest_async('CreateTopicRouteTable', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_consumer_group_with_options(
        self,
        request: iot_20180120_models.DeleteConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteConsumerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteConsumerGroupResponse(),
            self.do_rpcrequest('DeleteConsumerGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_consumer_group_with_options_async(
        self,
        request: iot_20180120_models.DeleteConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteConsumerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteConsumerGroupResponse(),
            await self.do_rpcrequest_async('DeleteConsumerGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteConsumerGroupSubscribeRelationResponse(),
            self.do_rpcrequest('DeleteConsumerGroupSubscribeRelation', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_consumer_group_subscribe_relation_with_options_async(
        self,
        request: iot_20180120_models.DeleteConsumerGroupSubscribeRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteConsumerGroupSubscribeRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteConsumerGroupSubscribeRelationResponse(),
            await self.do_rpcrequest_async('DeleteConsumerGroupSubscribeRelation', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_device_with_options(
        self,
        request: iot_20180120_models.DeleteDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceResponse(),
            self.do_rpcrequest('DeleteDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_device_with_options_async(
        self,
        request: iot_20180120_models.DeleteDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceResponse(),
            await self.do_rpcrequest_async('DeleteDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceDistributeJobResponse(),
            self.do_rpcrequest('DeleteDeviceDistributeJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_device_distribute_job_with_options_async(
        self,
        request: iot_20180120_models.DeleteDeviceDistributeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDeviceDistributeJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceDistributeJobResponse(),
            await self.do_rpcrequest_async('DeleteDeviceDistributeJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_device_file_with_options(
        self,
        request: iot_20180120_models.DeleteDeviceFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDeviceFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceFileResponse(),
            self.do_rpcrequest('DeleteDeviceFile', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_device_file_with_options_async(
        self,
        request: iot_20180120_models.DeleteDeviceFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDeviceFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceFileResponse(),
            await self.do_rpcrequest_async('DeleteDeviceFile', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceGroupResponse(),
            self.do_rpcrequest('DeleteDeviceGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_device_group_with_options_async(
        self,
        request: iot_20180120_models.DeleteDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceGroupResponse(),
            await self.do_rpcrequest_async('DeleteDeviceGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteDevicePropResponse(),
            self.do_rpcrequest('DeleteDeviceProp', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_device_prop_with_options_async(
        self,
        request: iot_20180120_models.DeleteDevicePropRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteDevicePropResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteDevicePropResponse(),
            await self.do_rpcrequest_async('DeleteDeviceProp', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_edge_driver_with_options(
        self,
        request: iot_20180120_models.DeleteEdgeDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteEdgeDriverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteEdgeDriverResponse(),
            self.do_rpcrequest('DeleteEdgeDriver', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_edge_driver_with_options_async(
        self,
        request: iot_20180120_models.DeleteEdgeDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteEdgeDriverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteEdgeDriverResponse(),
            await self.do_rpcrequest_async('DeleteEdgeDriver', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteEdgeDriverVersionResponse(),
            self.do_rpcrequest('DeleteEdgeDriverVersion', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_edge_driver_version_with_options_async(
        self,
        request: iot_20180120_models.DeleteEdgeDriverVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteEdgeDriverVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteEdgeDriverVersionResponse(),
            await self.do_rpcrequest_async('DeleteEdgeDriverVersion', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteEdgeInstanceResponse(),
            self.do_rpcrequest('DeleteEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.DeleteEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteEdgeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteEdgeInstanceResponse(),
            await self.do_rpcrequest_async('DeleteEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteEdgeInstanceMessageRoutingResponse(),
            self.do_rpcrequest('DeleteEdgeInstanceMessageRouting', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_edge_instance_message_routing_with_options_async(
        self,
        request: iot_20180120_models.DeleteEdgeInstanceMessageRoutingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteEdgeInstanceMessageRoutingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteEdgeInstanceMessageRoutingResponse(),
            await self.do_rpcrequest_async('DeleteEdgeInstanceMessageRouting', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteJobResponse(),
            self.do_rpcrequest('DeleteJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_job_with_options_async(
        self,
        request: iot_20180120_models.DeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteJobResponse(),
            await self.do_rpcrequest_async('DeleteJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteOTAFirmwareResponse(),
            self.do_rpcrequest('DeleteOTAFirmware', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_otafirmware_with_options_async(
        self,
        request: iot_20180120_models.DeleteOTAFirmwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteOTAFirmwareResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteOTAFirmwareResponse(),
            await self.do_rpcrequest_async('DeleteOTAFirmware', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteOTAModuleResponse(),
            self.do_rpcrequest('DeleteOTAModule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_otamodule_with_options_async(
        self,
        request: iot_20180120_models.DeleteOTAModuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteOTAModuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteOTAModuleResponse(),
            await self.do_rpcrequest_async('DeleteOTAModule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_product_with_options(
        self,
        request: iot_20180120_models.DeleteProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteProductResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteProductResponse(),
            self.do_rpcrequest('DeleteProduct', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_product_with_options_async(
        self,
        request: iot_20180120_models.DeleteProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteProductResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteProductResponse(),
            await self.do_rpcrequest_async('DeleteProduct', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteProductTagsResponse(),
            self.do_rpcrequest('DeleteProductTags', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_product_tags_with_options_async(
        self,
        request: iot_20180120_models.DeleteProductTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteProductTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteProductTagsResponse(),
            await self.do_rpcrequest_async('DeleteProductTags', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteProductTopicResponse(),
            self.do_rpcrequest('DeleteProductTopic', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_product_topic_with_options_async(
        self,
        request: iot_20180120_models.DeleteProductTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteProductTopicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteProductTopicResponse(),
            await self.do_rpcrequest_async('DeleteProductTopic', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteRuleResponse(),
            self.do_rpcrequest('DeleteRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_rule_with_options_async(
        self,
        request: iot_20180120_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteRuleResponse(),
            await self.do_rpcrequest_async('DeleteRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteRuleActionResponse(),
            self.do_rpcrequest('DeleteRuleAction', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_rule_action_with_options_async(
        self,
        request: iot_20180120_models.DeleteRuleActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteRuleActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteRuleActionResponse(),
            await self.do_rpcrequest_async('DeleteRuleAction', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteSceneRuleResponse(),
            self.do_rpcrequest('DeleteSceneRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_scene_rule_with_options_async(
        self,
        request: iot_20180120_models.DeleteSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteSceneRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteSceneRuleResponse(),
            await self.do_rpcrequest_async('DeleteSceneRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_speech_with_options(
        self,
        request: iot_20180120_models.DeleteSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteSpeechResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteSpeechResponse(),
            self.do_rpcrequest('DeleteSpeech', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_speech_with_options_async(
        self,
        request: iot_20180120_models.DeleteSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteSpeechResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteSpeechResponse(),
            await self.do_rpcrequest_async('DeleteSpeech', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteStudioAppDomainOpenResponse(),
            self.do_rpcrequest('DeleteStudioAppDomainOpen', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_studio_app_domain_open_with_options_async(
        self,
        request: iot_20180120_models.DeleteStudioAppDomainOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteStudioAppDomainOpenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteStudioAppDomainOpenResponse(),
            await self.do_rpcrequest_async('DeleteStudioAppDomainOpen', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteSubscribeRelationResponse(),
            self.do_rpcrequest('DeleteSubscribeRelation', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_subscribe_relation_with_options_async(
        self,
        request: iot_20180120_models.DeleteSubscribeRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteSubscribeRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteSubscribeRelationResponse(),
            await self.do_rpcrequest_async('DeleteSubscribeRelation', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteThingModelResponse(),
            self.do_rpcrequest('DeleteThingModel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_thing_model_with_options_async(
        self,
        request: iot_20180120_models.DeleteThingModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteThingModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteThingModelResponse(),
            await self.do_rpcrequest_async('DeleteThingModel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteTopicRouteTableResponse(),
            self.do_rpcrequest('DeleteTopicRouteTable', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_topic_route_table_with_options_async(
        self,
        request: iot_20180120_models.DeleteTopicRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteTopicRouteTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteTopicRouteTableResponse(),
            await self.do_rpcrequest_async('DeleteTopicRouteTable', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def disable_device_tunnel_with_options(
        self,
        request: iot_20180120_models.DisableDeviceTunnelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DisableDeviceTunnelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DisableDeviceTunnelResponse(),
            self.do_rpcrequest('DisableDeviceTunnel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_device_tunnel_with_options_async(
        self,
        request: iot_20180120_models.DisableDeviceTunnelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DisableDeviceTunnelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DisableDeviceTunnelResponse(),
            await self.do_rpcrequest_async('DisableDeviceTunnel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DisableDeviceTunnelShareResponse(),
            self.do_rpcrequest('DisableDeviceTunnelShare', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_device_tunnel_share_with_options_async(
        self,
        request: iot_20180120_models.DisableDeviceTunnelShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DisableDeviceTunnelShareResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DisableDeviceTunnelShareResponse(),
            await self.do_rpcrequest_async('DisableDeviceTunnelShare', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DisableSceneRuleResponse(),
            self.do_rpcrequest('DisableSceneRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_scene_rule_with_options_async(
        self,
        request: iot_20180120_models.DisableSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DisableSceneRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DisableSceneRuleResponse(),
            await self.do_rpcrequest_async('DisableSceneRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DisableThingResponse(),
            self.do_rpcrequest('DisableThing', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_thing_with_options_async(
        self,
        request: iot_20180120_models.DisableThingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DisableThingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.DisableThingResponse(),
            await self.do_rpcrequest_async('DisableThing', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.EnableDeviceTunnelResponse(),
            self.do_rpcrequest('EnableDeviceTunnel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_device_tunnel_with_options_async(
        self,
        request: iot_20180120_models.EnableDeviceTunnelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.EnableDeviceTunnelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.EnableDeviceTunnelResponse(),
            await self.do_rpcrequest_async('EnableDeviceTunnel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.EnableDeviceTunnelShareResponse(),
            self.do_rpcrequest('EnableDeviceTunnelShare', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_device_tunnel_share_with_options_async(
        self,
        request: iot_20180120_models.EnableDeviceTunnelShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.EnableDeviceTunnelShareResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.EnableDeviceTunnelShareResponse(),
            await self.do_rpcrequest_async('EnableDeviceTunnelShare', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.EnableSceneRuleResponse(),
            self.do_rpcrequest('EnableSceneRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_scene_rule_with_options_async(
        self,
        request: iot_20180120_models.EnableSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.EnableSceneRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.EnableSceneRuleResponse(),
            await self.do_rpcrequest_async('EnableSceneRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.EnableThingResponse(),
            self.do_rpcrequest('EnableThing', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_thing_with_options_async(
        self,
        request: iot_20180120_models.EnableThingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.EnableThingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.EnableThingResponse(),
            await self.do_rpcrequest_async('EnableThing', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GenerateDeviceNameListURLResponse(),
            self.do_rpcrequest('GenerateDeviceNameListURL', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_device_name_list_urlwith_options_async(
        self,
        request: iot_20180120_models.GenerateDeviceNameListURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GenerateDeviceNameListURLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GenerateDeviceNameListURLResponse(),
            await self.do_rpcrequest_async('GenerateDeviceNameListURL', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GenerateFileUploadURLResponse(),
            self.do_rpcrequest('GenerateFileUploadURL', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_file_upload_urlwith_options_async(
        self,
        request: iot_20180120_models.GenerateFileUploadURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GenerateFileUploadURLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GenerateFileUploadURLResponse(),
            await self.do_rpcrequest_async('GenerateFileUploadURL', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GenerateOTAUploadURLResponse(),
            self.do_rpcrequest('GenerateOTAUploadURL', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_otaupload_urlwith_options_async(
        self,
        request: iot_20180120_models.GenerateOTAUploadURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GenerateOTAUploadURLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GenerateOTAUploadURLResponse(),
            await self.do_rpcrequest_async('GenerateOTAUploadURL', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetDataAPIServiceDetailResponse(),
            self.do_rpcrequest('GetDataAPIServiceDetail', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_data_apiservice_detail_with_options_async(
        self,
        request: iot_20180120_models.GetDataAPIServiceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetDataAPIServiceDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetDataAPIServiceDetailResponse(),
            await self.do_rpcrequest_async('GetDataAPIServiceDetail', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_device_shadow_with_options(
        self,
        request: iot_20180120_models.GetDeviceShadowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetDeviceShadowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetDeviceShadowResponse(),
            self.do_rpcrequest('GetDeviceShadow', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_device_shadow_with_options_async(
        self,
        request: iot_20180120_models.GetDeviceShadowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetDeviceShadowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetDeviceShadowResponse(),
            await self.do_rpcrequest_async('GetDeviceShadow', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetDeviceStatusResponse(),
            self.do_rpcrequest('GetDeviceStatus', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_device_status_with_options_async(
        self,
        request: iot_20180120_models.GetDeviceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetDeviceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetDeviceStatusResponse(),
            await self.do_rpcrequest_async('GetDeviceStatus', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetDeviceTunnelShareStatusResponse(),
            self.do_rpcrequest('GetDeviceTunnelShareStatus', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_device_tunnel_share_status_with_options_async(
        self,
        request: iot_20180120_models.GetDeviceTunnelShareStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetDeviceTunnelShareStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetDeviceTunnelShareStatusResponse(),
            await self.do_rpcrequest_async('GetDeviceTunnelShareStatus', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetDeviceTunnelStatusResponse(),
            self.do_rpcrequest('GetDeviceTunnelStatus', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_device_tunnel_status_with_options_async(
        self,
        request: iot_20180120_models.GetDeviceTunnelStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetDeviceTunnelStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetDeviceTunnelStatusResponse(),
            await self.do_rpcrequest_async('GetDeviceTunnelStatus', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_edge_driver_version_with_options(
        self,
        request: iot_20180120_models.GetEdgeDriverVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetEdgeDriverVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetEdgeDriverVersionResponse(),
            self.do_rpcrequest('GetEdgeDriverVersion', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_edge_driver_version_with_options_async(
        self,
        request: iot_20180120_models.GetEdgeDriverVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetEdgeDriverVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetEdgeDriverVersionResponse(),
            await self.do_rpcrequest_async('GetEdgeDriverVersion', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetEdgeInstanceResponse(),
            self.do_rpcrequest('GetEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.GetEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetEdgeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetEdgeInstanceResponse(),
            await self.do_rpcrequest_async('GetEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetEdgeInstanceDeploymentResponse(),
            self.do_rpcrequest('GetEdgeInstanceDeployment', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_edge_instance_deployment_with_options_async(
        self,
        request: iot_20180120_models.GetEdgeInstanceDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetEdgeInstanceDeploymentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetEdgeInstanceDeploymentResponse(),
            await self.do_rpcrequest_async('GetEdgeInstanceDeployment', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetEdgeInstanceMessageRoutingResponse(),
            self.do_rpcrequest('GetEdgeInstanceMessageRouting', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_edge_instance_message_routing_with_options_async(
        self,
        request: iot_20180120_models.GetEdgeInstanceMessageRoutingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetEdgeInstanceMessageRoutingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetEdgeInstanceMessageRoutingResponse(),
            await self.do_rpcrequest_async('GetEdgeInstanceMessageRouting', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetGatewayBySubDeviceResponse(),
            self.do_rpcrequest('GetGatewayBySubDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_gateway_by_sub_device_with_options_async(
        self,
        request: iot_20180120_models.GetGatewayBySubDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetGatewayBySubDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetGatewayBySubDeviceResponse(),
            await self.do_rpcrequest_async('GetGatewayBySubDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetLoraNodesTaskResponse(),
            self.do_rpcrequest('GetLoraNodesTask', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_lora_nodes_task_with_options_async(
        self,
        request: iot_20180120_models.GetLoraNodesTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetLoraNodesTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetLoraNodesTaskResponse(),
            await self.do_rpcrequest_async('GetLoraNodesTask', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_nodes_adding_task_with_options(
        self,
        request: iot_20180120_models.GetNodesAddingTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetNodesAddingTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetNodesAddingTaskResponse(),
            self.do_rpcrequest('GetNodesAddingTask', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_nodes_adding_task_with_options_async(
        self,
        request: iot_20180120_models.GetNodesAddingTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetNodesAddingTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetNodesAddingTaskResponse(),
            await self.do_rpcrequest_async('GetNodesAddingTask', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_nodes_adding_task(
        self,
        request: iot_20180120_models.GetNodesAddingTaskRequest,
    ) -> iot_20180120_models.GetNodesAddingTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_nodes_adding_task_with_options(request, runtime)

    async def get_nodes_adding_task_async(
        self,
        request: iot_20180120_models.GetNodesAddingTaskRequest,
    ) -> iot_20180120_models.GetNodesAddingTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_nodes_adding_task_with_options_async(request, runtime)

    def get_rule_with_options(
        self,
        request: iot_20180120_models.GetRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetRuleResponse(),
            self.do_rpcrequest('GetRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_rule_with_options_async(
        self,
        request: iot_20180120_models.GetRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetRuleResponse(),
            await self.do_rpcrequest_async('GetRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetRuleActionResponse(),
            self.do_rpcrequest('GetRuleAction', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_rule_action_with_options_async(
        self,
        request: iot_20180120_models.GetRuleActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetRuleActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetRuleActionResponse(),
            await self.do_rpcrequest_async('GetRuleAction', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetSceneRuleResponse(),
            self.do_rpcrequest('GetSceneRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_scene_rule_with_options_async(
        self,
        request: iot_20180120_models.GetSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetSceneRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetSceneRuleResponse(),
            await self.do_rpcrequest_async('GetSceneRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_speech_voice_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetSpeechVoiceResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            iot_20180120_models.GetSpeechVoiceResponse(),
            self.do_rpcrequest('GetSpeechVoice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_speech_voice_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetSpeechVoiceResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            iot_20180120_models.GetSpeechVoiceResponse(),
            await self.do_rpcrequest_async('GetSpeechVoice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_speech_voice(self) -> iot_20180120_models.GetSpeechVoiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_speech_voice_with_options(runtime)

    async def get_speech_voice_async(self) -> iot_20180120_models.GetSpeechVoiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_speech_voice_with_options_async(runtime)

    def get_studio_app_token_open_with_options(
        self,
        request: iot_20180120_models.GetStudioAppTokenOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetStudioAppTokenOpenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetStudioAppTokenOpenResponse(),
            self.do_rpcrequest('GetStudioAppTokenOpen', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_studio_app_token_open_with_options_async(
        self,
        request: iot_20180120_models.GetStudioAppTokenOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetStudioAppTokenOpenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetStudioAppTokenOpenResponse(),
            await self.do_rpcrequest_async('GetStudioAppTokenOpen', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetThingModelTslResponse(),
            self.do_rpcrequest('GetThingModelTsl', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_thing_model_tsl_with_options_async(
        self,
        request: iot_20180120_models.GetThingModelTslRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetThingModelTslResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetThingModelTslResponse(),
            await self.do_rpcrequest_async('GetThingModelTsl', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetThingModelTslPublishedResponse(),
            self.do_rpcrequest('GetThingModelTslPublished', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_thing_model_tsl_published_with_options_async(
        self,
        request: iot_20180120_models.GetThingModelTslPublishedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetThingModelTslPublishedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetThingModelTslPublishedResponse(),
            await self.do_rpcrequest_async('GetThingModelTslPublished', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetThingScriptResponse(),
            self.do_rpcrequest('GetThingScript', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_thing_script_with_options_async(
        self,
        request: iot_20180120_models.GetThingScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetThingScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetThingScriptResponse(),
            await self.do_rpcrequest_async('GetThingScript', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetThingTemplateResponse(),
            self.do_rpcrequest('GetThingTemplate', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_thing_template_with_options_async(
        self,
        request: iot_20180120_models.GetThingTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetThingTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetThingTemplateResponse(),
            await self.do_rpcrequest_async('GetThingTemplate', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetThingTopoResponse(),
            self.do_rpcrequest('GetThingTopo', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_thing_topo_with_options_async(
        self,
        request: iot_20180120_models.GetThingTopoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetThingTopoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.GetThingTopoResponse(),
            await self.do_rpcrequest_async('GetThingTopo', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def import_thing_model_tsl_with_options(
        self,
        request: iot_20180120_models.ImportThingModelTslRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ImportThingModelTslResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ImportThingModelTslResponse(),
            self.do_rpcrequest('ImportThingModelTsl', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_thing_model_tsl_with_options_async(
        self,
        request: iot_20180120_models.ImportThingModelTslRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ImportThingModelTslResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ImportThingModelTslResponse(),
            await self.do_rpcrequest_async('ImportThingModelTsl', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.InvokeDataAPIServiceResponse(),
            self.do_rpcrequest('InvokeDataAPIService', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def invoke_data_apiservice_with_options_async(
        self,
        request: iot_20180120_models.InvokeDataAPIServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.InvokeDataAPIServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.InvokeDataAPIServiceResponse(),
            await self.do_rpcrequest_async('InvokeDataAPIService', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.InvokeThingServiceResponse(),
            self.do_rpcrequest('InvokeThingService', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def invoke_thing_service_with_options_async(
        self,
        request: iot_20180120_models.InvokeThingServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.InvokeThingServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.InvokeThingServiceResponse(),
            await self.do_rpcrequest_async('InvokeThingService', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.InvokeThingsServiceResponse(),
            self.do_rpcrequest('InvokeThingsService', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def invoke_things_service_with_options_async(
        self,
        request: iot_20180120_models.InvokeThingsServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.InvokeThingsServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.InvokeThingsServiceResponse(),
            await self.do_rpcrequest_async('InvokeThingsService', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListAnalyticsDataResponse(),
            self.do_rpcrequest('ListAnalyticsData', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_analytics_data_with_options_async(
        self,
        request: iot_20180120_models.ListAnalyticsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListAnalyticsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListAnalyticsDataResponse(),
            await self.do_rpcrequest_async('ListAnalyticsData', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_device_distribute_job_with_options(
        self,
        request: iot_20180120_models.ListDeviceDistributeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListDeviceDistributeJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListDeviceDistributeJobResponse(),
            self.do_rpcrequest('ListDeviceDistributeJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_device_distribute_job_with_options_async(
        self,
        request: iot_20180120_models.ListDeviceDistributeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListDeviceDistributeJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListDeviceDistributeJobResponse(),
            await self.do_rpcrequest_async('ListDeviceDistributeJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListDistributedDeviceResponse(),
            self.do_rpcrequest('ListDistributedDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_distributed_device_with_options_async(
        self,
        request: iot_20180120_models.ListDistributedDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListDistributedDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListDistributedDeviceResponse(),
            await self.do_rpcrequest_async('ListDistributedDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListDistributedProductResponse(),
            self.do_rpcrequest('ListDistributedProduct', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_distributed_product_with_options_async(
        self,
        request: iot_20180120_models.ListDistributedProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListDistributedProductResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListDistributedProductResponse(),
            await self.do_rpcrequest_async('ListDistributedProduct', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListJobResponse(),
            self.do_rpcrequest('ListJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_job_with_options_async(
        self,
        request: iot_20180120_models.ListJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListJobResponse(),
            await self.do_rpcrequest_async('ListJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListOTAFirmwareResponse(),
            self.do_rpcrequest('ListOTAFirmware', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_otafirmware_with_options_async(
        self,
        request: iot_20180120_models.ListOTAFirmwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListOTAFirmwareResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListOTAFirmwareResponse(),
            await self.do_rpcrequest_async('ListOTAFirmware', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListOTAJobByDeviceResponse(),
            self.do_rpcrequest('ListOTAJobByDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_otajob_by_device_with_options_async(
        self,
        request: iot_20180120_models.ListOTAJobByDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListOTAJobByDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListOTAJobByDeviceResponse(),
            await self.do_rpcrequest_async('ListOTAJobByDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListOTAJobByFirmwareResponse(),
            self.do_rpcrequest('ListOTAJobByFirmware', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_otajob_by_firmware_with_options_async(
        self,
        request: iot_20180120_models.ListOTAJobByFirmwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListOTAJobByFirmwareResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListOTAJobByFirmwareResponse(),
            await self.do_rpcrequest_async('ListOTAJobByFirmware', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iot_20180120_models.ListOTAModuleByProductResponse(),
            self.do_rpcrequest('ListOTAModuleByProduct', '2018-01-20', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_otamodule_by_product_with_options_async(
        self,
        request: iot_20180120_models.ListOTAModuleByProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListOTAModuleByProductResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iot_20180120_models.ListOTAModuleByProductResponse(),
            await self.do_rpcrequest_async('ListOTAModuleByProduct', '2018-01-20', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListOTAModuleVersionsByDeviceResponse(),
            self.do_rpcrequest('ListOTAModuleVersionsByDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_otamodule_versions_by_device_with_options_async(
        self,
        request: iot_20180120_models.ListOTAModuleVersionsByDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListOTAModuleVersionsByDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListOTAModuleVersionsByDeviceResponse(),
            await self.do_rpcrequest_async('ListOTAModuleVersionsByDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListOTATaskByJobResponse(),
            self.do_rpcrequest('ListOTATaskByJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_otatask_by_job_with_options_async(
        self,
        request: iot_20180120_models.ListOTATaskByJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListOTATaskByJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListOTATaskByJobResponse(),
            await self.do_rpcrequest_async('ListOTATaskByJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListOTAUnfinishedTaskByDeviceResponse(),
            self.do_rpcrequest('ListOTAUnfinishedTaskByDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_otaunfinished_task_by_device_with_options_async(
        self,
        request: iot_20180120_models.ListOTAUnfinishedTaskByDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListOTAUnfinishedTaskByDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListOTAUnfinishedTaskByDeviceResponse(),
            await self.do_rpcrequest_async('ListOTAUnfinishedTaskByDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_product_by_tags_with_options(
        self,
        request: iot_20180120_models.ListProductByTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListProductByTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListProductByTagsResponse(),
            self.do_rpcrequest('ListProductByTags', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_product_by_tags_with_options_async(
        self,
        request: iot_20180120_models.ListProductByTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListProductByTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListProductByTagsResponse(),
            await self.do_rpcrequest_async('ListProductByTags', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListProductTagsResponse(),
            self.do_rpcrequest('ListProductTags', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_product_tags_with_options_async(
        self,
        request: iot_20180120_models.ListProductTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListProductTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListProductTagsResponse(),
            await self.do_rpcrequest_async('ListProductTags', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListRuleResponse(),
            self.do_rpcrequest('ListRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_rule_with_options_async(
        self,
        request: iot_20180120_models.ListRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListRuleResponse(),
            await self.do_rpcrequest_async('ListRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListRuleActionsResponse(),
            self.do_rpcrequest('ListRuleActions', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_rule_actions_with_options_async(
        self,
        request: iot_20180120_models.ListRuleActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListRuleActionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListRuleActionsResponse(),
            await self.do_rpcrequest_async('ListRuleActions', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        request: iot_20180120_models.ListTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListTaskResponse(),
            self.do_rpcrequest('ListTask', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_task_with_options_async(
        self,
        request: iot_20180120_models.ListTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListTaskResponse(),
            await self.do_rpcrequest_async('ListTask', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_task_by_page_with_options(
        self,
        request: iot_20180120_models.ListTaskByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListTaskByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListTaskByPageResponse(),
            self.do_rpcrequest('ListTaskByPage', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_task_by_page_with_options_async(
        self,
        request: iot_20180120_models.ListTaskByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListTaskByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListTaskByPageResponse(),
            await self.do_rpcrequest_async('ListTaskByPage', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_task_by_page(
        self,
        request: iot_20180120_models.ListTaskByPageRequest,
    ) -> iot_20180120_models.ListTaskByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_task_by_page_with_options(request, runtime)

    async def list_task_by_page_async(
        self,
        request: iot_20180120_models.ListTaskByPageRequest,
    ) -> iot_20180120_models.ListTaskByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_task_by_page_with_options_async(request, runtime)

    def list_thing_model_version_with_options(
        self,
        request: iot_20180120_models.ListThingModelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListThingModelVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListThingModelVersionResponse(),
            self.do_rpcrequest('ListThingModelVersion', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_thing_model_version_with_options_async(
        self,
        request: iot_20180120_models.ListThingModelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListThingModelVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListThingModelVersionResponse(),
            await self.do_rpcrequest_async('ListThingModelVersion', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListThingTemplatesResponse(),
            self.do_rpcrequest('ListThingTemplates', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_thing_templates_with_options_async(
        self,
        request: iot_20180120_models.ListThingTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListThingTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ListThingTemplatesResponse(),
            await self.do_rpcrequest_async('ListThingTemplates', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.NotifyAddThingTopoResponse(),
            self.do_rpcrequest('NotifyAddThingTopo', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def notify_add_thing_topo_with_options_async(
        self,
        request: iot_20180120_models.NotifyAddThingTopoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.NotifyAddThingTopoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.NotifyAddThingTopoResponse(),
            await self.do_rpcrequest_async('NotifyAddThingTopo', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.OpenIotServiceResponse(),
            self.do_rpcrequest('OpenIotService', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_iot_service_with_options_async(
        self,
        request: iot_20180120_models.OpenIotServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.OpenIotServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.OpenIotServiceResponse(),
            await self.do_rpcrequest_async('OpenIotService', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def print_by_template_with_options(
        self,
        request: iot_20180120_models.PrintByTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PrintByTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.PrintByTemplateResponse(),
            self.do_rpcrequest('PrintByTemplate', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def print_by_template_with_options_async(
        self,
        request: iot_20180120_models.PrintByTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PrintByTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.PrintByTemplateResponse(),
            await self.do_rpcrequest_async('PrintByTemplate', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.PubResponse(),
            self.do_rpcrequest('Pub', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def pub_with_options_async(
        self,
        request: iot_20180120_models.PubRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PubResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.PubResponse(),
            await self.do_rpcrequest_async('Pub', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.PubBroadcastResponse(),
            self.do_rpcrequest('PubBroadcast', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def pub_broadcast_with_options_async(
        self,
        request: iot_20180120_models.PubBroadcastRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PubBroadcastResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.PubBroadcastResponse(),
            await self.do_rpcrequest_async('PubBroadcast', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def publish_studio_app_with_options(
        self,
        request: iot_20180120_models.PublishStudioAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PublishStudioAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.PublishStudioAppResponse(),
            self.do_rpcrequest('PublishStudioApp', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def publish_studio_app_with_options_async(
        self,
        request: iot_20180120_models.PublishStudioAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PublishStudioAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.PublishStudioAppResponse(),
            await self.do_rpcrequest_async('PublishStudioApp', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.PublishThingModelResponse(),
            self.do_rpcrequest('PublishThingModel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def publish_thing_model_with_options_async(
        self,
        request: iot_20180120_models.PublishThingModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PublishThingModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.PublishThingModelResponse(),
            await self.do_rpcrequest_async('PublishThingModel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.PushSpeechResponse(),
            self.do_rpcrequest('PushSpeech', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def push_speech_with_options_async(
        self,
        request: iot_20180120_models.PushSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PushSpeechResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.PushSpeechResponse(),
            await self.do_rpcrequest_async('PushSpeech', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_app_device_list_with_options(
        self,
        request: iot_20180120_models.QueryAppDeviceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryAppDeviceListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryAppDeviceListResponse(),
            self.do_rpcrequest('QueryAppDeviceList', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_app_device_list_with_options_async(
        self,
        request: iot_20180120_models.QueryAppDeviceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryAppDeviceListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryAppDeviceListResponse(),
            await self.do_rpcrequest_async('QueryAppDeviceList', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_app_device_list(
        self,
        request: iot_20180120_models.QueryAppDeviceListRequest,
    ) -> iot_20180120_models.QueryAppDeviceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_app_device_list_with_options(request, runtime)

    async def query_app_device_list_async(
        self,
        request: iot_20180120_models.QueryAppDeviceListRequest,
    ) -> iot_20180120_models.QueryAppDeviceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_app_device_list_with_options_async(request, runtime)

    def query_batch_register_device_status_with_options(
        self,
        request: iot_20180120_models.QueryBatchRegisterDeviceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryBatchRegisterDeviceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryBatchRegisterDeviceStatusResponse(),
            self.do_rpcrequest('QueryBatchRegisterDeviceStatus', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_batch_register_device_status_with_options_async(
        self,
        request: iot_20180120_models.QueryBatchRegisterDeviceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryBatchRegisterDeviceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryBatchRegisterDeviceStatusResponse(),
            await self.do_rpcrequest_async('QueryBatchRegisterDeviceStatus', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryCertUrlByApplyIdResponse(),
            self.do_rpcrequest('QueryCertUrlByApplyId', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_cert_url_by_apply_id_with_options_async(
        self,
        request: iot_20180120_models.QueryCertUrlByApplyIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryCertUrlByApplyIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryCertUrlByApplyIdResponse(),
            await self.do_rpcrequest_async('QueryCertUrlByApplyId', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_consumer_group_by_group_id_with_options(
        self,
        request: iot_20180120_models.QueryConsumerGroupByGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryConsumerGroupByGroupIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryConsumerGroupByGroupIdResponse(),
            self.do_rpcrequest('QueryConsumerGroupByGroupId', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_consumer_group_by_group_id_with_options_async(
        self,
        request: iot_20180120_models.QueryConsumerGroupByGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryConsumerGroupByGroupIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryConsumerGroupByGroupIdResponse(),
            await self.do_rpcrequest_async('QueryConsumerGroupByGroupId', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryConsumerGroupListResponse(),
            self.do_rpcrequest('QueryConsumerGroupList', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_consumer_group_list_with_options_async(
        self,
        request: iot_20180120_models.QueryConsumerGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryConsumerGroupListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryConsumerGroupListResponse(),
            await self.do_rpcrequest_async('QueryConsumerGroupList', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryConsumerGroupStatusResponse(),
            self.do_rpcrequest('QueryConsumerGroupStatus', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_consumer_group_status_with_options_async(
        self,
        request: iot_20180120_models.QueryConsumerGroupStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryConsumerGroupStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryConsumerGroupStatusResponse(),
            await self.do_rpcrequest_async('QueryConsumerGroupStatus', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDetailSceneRuleLogResponse(),
            self.do_rpcrequest('QueryDetailSceneRuleLog', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_detail_scene_rule_log_with_options_async(
        self,
        request: iot_20180120_models.QueryDetailSceneRuleLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDetailSceneRuleLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDetailSceneRuleLogResponse(),
            await self.do_rpcrequest_async('QueryDetailSceneRuleLog', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceResponse(),
            self.do_rpcrequest('QueryDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceResponse(),
            await self.do_rpcrequest_async('QueryDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceBySQLResponse(),
            self.do_rpcrequest('QueryDeviceBySQL', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_by_sqlwith_options_async(
        self,
        request: iot_20180120_models.QueryDeviceBySQLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceBySQLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceBySQLResponse(),
            await self.do_rpcrequest_async('QueryDeviceBySQL', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceByStatusResponse(),
            self.do_rpcrequest('QueryDeviceByStatus', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_by_status_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceByStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceByStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceByStatusResponse(),
            await self.do_rpcrequest_async('QueryDeviceByStatus', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceByTagsResponse(),
            self.do_rpcrequest('QueryDeviceByTags', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_by_tags_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceByTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceByTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceByTagsResponse(),
            await self.do_rpcrequest_async('QueryDeviceByTags', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceCertResponse(),
            self.do_rpcrequest('QueryDeviceCert', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_cert_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceCertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceCertResponse(),
            await self.do_rpcrequest_async('QueryDeviceCert', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceDesiredPropertyResponse(),
            self.do_rpcrequest('QueryDeviceDesiredProperty', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_desired_property_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceDesiredPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceDesiredPropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceDesiredPropertyResponse(),
            await self.do_rpcrequest_async('QueryDeviceDesiredProperty', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceDetailResponse(),
            self.do_rpcrequest('QueryDeviceDetail', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_detail_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceDetailResponse(),
            await self.do_rpcrequest_async('QueryDeviceDetail', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceDistributeDetailResponse(),
            self.do_rpcrequest('QueryDeviceDistributeDetail', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_distribute_detail_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceDistributeDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceDistributeDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceDistributeDetailResponse(),
            await self.do_rpcrequest_async('QueryDeviceDistributeDetail', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceDistributeJobResponse(),
            self.do_rpcrequest('QueryDeviceDistributeJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_distribute_job_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceDistributeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceDistributeJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceDistributeJobResponse(),
            await self.do_rpcrequest_async('QueryDeviceDistributeJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceEventDataResponse(),
            self.do_rpcrequest('QueryDeviceEventData', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_event_data_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceEventDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceEventDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceEventDataResponse(),
            await self.do_rpcrequest_async('QueryDeviceEventData', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceFileResponse(),
            self.do_rpcrequest('QueryDeviceFile', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_file_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceFileResponse(),
            await self.do_rpcrequest_async('QueryDeviceFile', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceFileListResponse(),
            self.do_rpcrequest('QueryDeviceFileList', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_file_list_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceFileListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceFileListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceFileListResponse(),
            await self.do_rpcrequest_async('QueryDeviceFileList', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupByDeviceResponse(),
            self.do_rpcrequest('QueryDeviceGroupByDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_group_by_device_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceGroupByDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceGroupByDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupByDeviceResponse(),
            await self.do_rpcrequest_async('QueryDeviceGroupByDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupByTagsResponse(),
            self.do_rpcrequest('QueryDeviceGroupByTags', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_group_by_tags_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceGroupByTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceGroupByTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupByTagsResponse(),
            await self.do_rpcrequest_async('QueryDeviceGroupByTags', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupInfoResponse(),
            self.do_rpcrequest('QueryDeviceGroupInfo', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_group_info_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceGroupInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceGroupInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupInfoResponse(),
            await self.do_rpcrequest_async('QueryDeviceGroupInfo', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupListResponse(),
            self.do_rpcrequest('QueryDeviceGroupList', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_group_list_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceGroupListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupListResponse(),
            await self.do_rpcrequest_async('QueryDeviceGroupList', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupTagListResponse(),
            self.do_rpcrequest('QueryDeviceGroupTagList', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_group_tag_list_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceGroupTagListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceGroupTagListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupTagListResponse(),
            await self.do_rpcrequest_async('QueryDeviceGroupTagList', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceInfoResponse(),
            self.do_rpcrequest('QueryDeviceInfo', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_info_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceInfoResponse(),
            await self.do_rpcrequest_async('QueryDeviceInfo', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceListByDeviceGroupResponse(),
            self.do_rpcrequest('QueryDeviceListByDeviceGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_list_by_device_group_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceListByDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceListByDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceListByDeviceGroupResponse(),
            await self.do_rpcrequest_async('QueryDeviceListByDeviceGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceOriginalEventDataResponse(),
            self.do_rpcrequest('QueryDeviceOriginalEventData', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_original_event_data_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceOriginalEventDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceOriginalEventDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceOriginalEventDataResponse(),
            await self.do_rpcrequest_async('QueryDeviceOriginalEventData', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceOriginalPropertyDataResponse(),
            self.do_rpcrequest('QueryDeviceOriginalPropertyData', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_original_property_data_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceOriginalPropertyDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceOriginalPropertyDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceOriginalPropertyDataResponse(),
            await self.do_rpcrequest_async('QueryDeviceOriginalPropertyData', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceOriginalPropertyStatusResponse(),
            self.do_rpcrequest('QueryDeviceOriginalPropertyStatus', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_original_property_status_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceOriginalPropertyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceOriginalPropertyStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceOriginalPropertyStatusResponse(),
            await self.do_rpcrequest_async('QueryDeviceOriginalPropertyStatus', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceOriginalServiceDataResponse(),
            self.do_rpcrequest('QueryDeviceOriginalServiceData', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_original_service_data_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceOriginalServiceDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceOriginalServiceDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceOriginalServiceDataResponse(),
            await self.do_rpcrequest_async('QueryDeviceOriginalServiceData', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicePropResponse(),
            self.do_rpcrequest('QueryDeviceProp', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_prop_with_options_async(
        self,
        request: iot_20180120_models.QueryDevicePropRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDevicePropResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicePropResponse(),
            await self.do_rpcrequest_async('QueryDeviceProp', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicePropertiesDataResponse(),
            self.do_rpcrequest('QueryDevicePropertiesData', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_properties_data_with_options_async(
        self,
        request: iot_20180120_models.QueryDevicePropertiesDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDevicePropertiesDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicePropertiesDataResponse(),
            await self.do_rpcrequest_async('QueryDevicePropertiesData', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicePropertyDataResponse(),
            self.do_rpcrequest('QueryDevicePropertyData', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_property_data_with_options_async(
        self,
        request: iot_20180120_models.QueryDevicePropertyDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDevicePropertyDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicePropertyDataResponse(),
            await self.do_rpcrequest_async('QueryDevicePropertyData', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicePropertyStatusResponse(),
            self.do_rpcrequest('QueryDevicePropertyStatus', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_property_status_with_options_async(
        self,
        request: iot_20180120_models.QueryDevicePropertyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDevicePropertyStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicePropertyStatusResponse(),
            await self.do_rpcrequest_async('QueryDevicePropertyStatus', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceServiceDataResponse(),
            self.do_rpcrequest('QueryDeviceServiceData', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_service_data_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceServiceDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceServiceDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceServiceDataResponse(),
            await self.do_rpcrequest_async('QueryDeviceServiceData', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_device_statistics_with_options(
        self,
        request: iot_20180120_models.QueryDeviceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceStatisticsResponse(),
            self.do_rpcrequest('QueryDeviceStatistics', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_statistics_with_options_async(
        self,
        request: iot_20180120_models.QueryDeviceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceStatisticsResponse(),
            await self.do_rpcrequest_async('QueryDeviceStatistics', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_edge_driver_with_options(
        self,
        request: iot_20180120_models.QueryEdgeDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeDriverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeDriverResponse(),
            self.do_rpcrequest('QueryEdgeDriver', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_edge_driver_with_options_async(
        self,
        request: iot_20180120_models.QueryEdgeDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeDriverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeDriverResponse(),
            await self.do_rpcrequest_async('QueryEdgeDriver', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeDriverVersionResponse(),
            self.do_rpcrequest('QueryEdgeDriverVersion', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_edge_driver_version_with_options_async(
        self,
        request: iot_20180120_models.QueryEdgeDriverVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeDriverVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeDriverVersionResponse(),
            await self.do_rpcrequest_async('QueryEdgeDriverVersion', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceResponse(),
            self.do_rpcrequest('QueryEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceResponse(),
            await self.do_rpcrequest_async('QueryEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceChannelResponse(),
            self.do_rpcrequest('QueryEdgeInstanceChannel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_edge_instance_channel_with_options_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceChannelResponse(),
            await self.do_rpcrequest_async('QueryEdgeInstanceChannel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceDeviceResponse(),
            self.do_rpcrequest('QueryEdgeInstanceDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_edge_instance_device_with_options_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceDeviceResponse(),
            await self.do_rpcrequest_async('QueryEdgeInstanceDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceDeviceByDriverResponse(),
            self.do_rpcrequest('QueryEdgeInstanceDeviceByDriver', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_edge_instance_device_by_driver_with_options_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceDeviceByDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceDeviceByDriverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceDeviceByDriverResponse(),
            await self.do_rpcrequest_async('QueryEdgeInstanceDeviceByDriver', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceDriverResponse(),
            self.do_rpcrequest('QueryEdgeInstanceDriver', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_edge_instance_driver_with_options_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceDriverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceDriverResponse(),
            await self.do_rpcrequest_async('QueryEdgeInstanceDriver', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceGatewayResponse(),
            self.do_rpcrequest('QueryEdgeInstanceGateway', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_edge_instance_gateway_with_options_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceGatewayResponse(),
            await self.do_rpcrequest_async('QueryEdgeInstanceGateway', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceHistoricDeploymentResponse(),
            self.do_rpcrequest('QueryEdgeInstanceHistoricDeployment', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_edge_instance_historic_deployment_with_options_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceHistoricDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceHistoricDeploymentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceHistoricDeploymentResponse(),
            await self.do_rpcrequest_async('QueryEdgeInstanceHistoricDeployment', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceMessageRoutingResponse(),
            self.do_rpcrequest('QueryEdgeInstanceMessageRouting', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_edge_instance_message_routing_with_options_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceMessageRoutingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceMessageRoutingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceMessageRoutingResponse(),
            await self.do_rpcrequest_async('QueryEdgeInstanceMessageRouting', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceSceneRuleResponse(),
            self.do_rpcrequest('QueryEdgeInstanceSceneRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_edge_instance_scene_rule_with_options_async(
        self,
        request: iot_20180120_models.QueryEdgeInstanceSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceSceneRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceSceneRuleResponse(),
            await self.do_rpcrequest_async('QueryEdgeInstanceSceneRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_job_with_options(
        self,
        request: iot_20180120_models.QueryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryJobResponse(),
            self.do_rpcrequest('QueryJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_job_with_options_async(
        self,
        request: iot_20180120_models.QueryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryJobResponse(),
            await self.do_rpcrequest_async('QueryJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryJobStatisticsResponse(),
            self.do_rpcrequest('QueryJobStatistics', '2018-01-20', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def query_job_statistics_with_options_async(
        self,
        request: iot_20180120_models.QueryJobStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryJobStatisticsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryJobStatisticsResponse(),
            await self.do_rpcrequest_async('QueryJobStatistics', '2018-01-20', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def query_lo_ra_join_permissions_with_options(
        self,
        request: iot_20180120_models.QueryLoRaJoinPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryLoRaJoinPermissionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryLoRaJoinPermissionsResponse(),
            self.do_rpcrequest('QueryLoRaJoinPermissions', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_lo_ra_join_permissions_with_options_async(
        self,
        request: iot_20180120_models.QueryLoRaJoinPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryLoRaJoinPermissionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryLoRaJoinPermissionsResponse(),
            await self.do_rpcrequest_async('QueryLoRaJoinPermissions', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryMessageInfoResponse(),
            self.do_rpcrequest('QueryMessageInfo', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_message_info_with_options_async(
        self,
        request: iot_20180120_models.QueryMessageInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryMessageInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryMessageInfoResponse(),
            await self.do_rpcrequest_async('QueryMessageInfo', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryOTAFirmwareResponse(),
            self.do_rpcrequest('QueryOTAFirmware', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_otafirmware_with_options_async(
        self,
        request: iot_20180120_models.QueryOTAFirmwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryOTAFirmwareResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryOTAFirmwareResponse(),
            await self.do_rpcrequest_async('QueryOTAFirmware', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryOTAJobResponse(),
            self.do_rpcrequest('QueryOTAJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_otajob_with_options_async(
        self,
        request: iot_20180120_models.QueryOTAJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryOTAJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryOTAJobResponse(),
            await self.do_rpcrequest_async('QueryOTAJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryPageByApplyIdResponse(),
            self.do_rpcrequest('QueryPageByApplyId', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_page_by_apply_id_with_options_async(
        self,
        request: iot_20180120_models.QueryPageByApplyIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryPageByApplyIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryPageByApplyIdResponse(),
            await self.do_rpcrequest_async('QueryPageByApplyId', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryProductResponse(),
            self.do_rpcrequest('QueryProduct', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_product_with_options_async(
        self,
        request: iot_20180120_models.QueryProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryProductResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryProductResponse(),
            await self.do_rpcrequest_async('QueryProduct', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryProductCertInfoResponse(),
            self.do_rpcrequest('QueryProductCertInfo', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_product_cert_info_with_options_async(
        self,
        request: iot_20180120_models.QueryProductCertInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryProductCertInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryProductCertInfoResponse(),
            await self.do_rpcrequest_async('QueryProductCertInfo', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryProductListResponse(),
            self.do_rpcrequest('QueryProductList', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_product_list_with_options_async(
        self,
        request: iot_20180120_models.QueryProductListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryProductListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryProductListResponse(),
            await self.do_rpcrequest_async('QueryProductList', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryProductTopicResponse(),
            self.do_rpcrequest('QueryProductTopic', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_product_topic_with_options_async(
        self,
        request: iot_20180120_models.QueryProductTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryProductTopicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryProductTopicResponse(),
            await self.do_rpcrequest_async('QueryProductTopic', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_scene_rule_with_options(
        self,
        request: iot_20180120_models.QuerySceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySceneRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySceneRuleResponse(),
            self.do_rpcrequest('QuerySceneRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_scene_rule_with_options_async(
        self,
        request: iot_20180120_models.QuerySceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySceneRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySceneRuleResponse(),
            await self.do_rpcrequest_async('QuerySceneRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_solution_device_group_page_with_options(
        self,
        request: iot_20180120_models.QuerySolutionDeviceGroupPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySolutionDeviceGroupPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySolutionDeviceGroupPageResponse(),
            self.do_rpcrequest('QuerySolutionDeviceGroupPage', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_solution_device_group_page_with_options_async(
        self,
        request: iot_20180120_models.QuerySolutionDeviceGroupPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySolutionDeviceGroupPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySolutionDeviceGroupPageResponse(),
            await self.do_rpcrequest_async('QuerySolutionDeviceGroupPage', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_speech_with_options(
        self,
        request: iot_20180120_models.QuerySpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySpeechResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechResponse(),
            self.do_rpcrequest('QuerySpeech', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_speech_with_options_async(
        self,
        request: iot_20180120_models.QuerySpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySpeechResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechResponse(),
            await self.do_rpcrequest_async('QuerySpeech', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_speech_list_with_options(
        self,
        request: iot_20180120_models.QuerySpeechListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySpeechListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechListResponse(),
            self.do_rpcrequest('QuerySpeechList', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_speech_list_with_options_async(
        self,
        request: iot_20180120_models.QuerySpeechListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySpeechListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechListResponse(),
            await self.do_rpcrequest_async('QuerySpeechList', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechPushJobResponse(),
            self.do_rpcrequest('QuerySpeechPushJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_speech_push_job_with_options_async(
        self,
        request: iot_20180120_models.QuerySpeechPushJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySpeechPushJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechPushJobResponse(),
            await self.do_rpcrequest_async('QuerySpeechPushJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechPushJobDeviceResponse(),
            self.do_rpcrequest('QuerySpeechPushJobDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_speech_push_job_device_with_options_async(
        self,
        request: iot_20180120_models.QuerySpeechPushJobDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySpeechPushJobDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechPushJobDeviceResponse(),
            await self.do_rpcrequest_async('QuerySpeechPushJobDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechPushJobSpeechResponse(),
            self.do_rpcrequest('QuerySpeechPushJobSpeech', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_speech_push_job_speech_with_options_async(
        self,
        request: iot_20180120_models.QuerySpeechPushJobSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySpeechPushJobSpeechResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechPushJobSpeechResponse(),
            await self.do_rpcrequest_async('QuerySpeechPushJobSpeech', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryStudioAppDomainListOpenResponse(),
            self.do_rpcrequest('QueryStudioAppDomainListOpen', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_studio_app_domain_list_open_with_options_async(
        self,
        request: iot_20180120_models.QueryStudioAppDomainListOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryStudioAppDomainListOpenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryStudioAppDomainListOpenResponse(),
            await self.do_rpcrequest_async('QueryStudioAppDomainListOpen', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryStudioAppListResponse(),
            self.do_rpcrequest('QueryStudioAppList', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_studio_app_list_with_options_async(
        self,
        request: iot_20180120_models.QueryStudioAppListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryStudioAppListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryStudioAppListResponse(),
            await self.do_rpcrequest_async('QueryStudioAppList', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryStudioAppPageListOpenResponse(),
            self.do_rpcrequest('QueryStudioAppPageListOpen', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_studio_app_page_list_open_with_options_async(
        self,
        request: iot_20180120_models.QueryStudioAppPageListOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryStudioAppPageListOpenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryStudioAppPageListOpenResponse(),
            await self.do_rpcrequest_async('QueryStudioAppPageListOpen', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryStudioProjectListResponse(),
            self.do_rpcrequest('QueryStudioProjectList', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_studio_project_list_with_options_async(
        self,
        request: iot_20180120_models.QueryStudioProjectListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryStudioProjectListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryStudioProjectListResponse(),
            await self.do_rpcrequest_async('QueryStudioProjectList', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySubscribeRelationResponse(),
            self.do_rpcrequest('QuerySubscribeRelation', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_subscribe_relation_with_options_async(
        self,
        request: iot_20180120_models.QuerySubscribeRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySubscribeRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySubscribeRelationResponse(),
            await self.do_rpcrequest_async('QuerySubscribeRelation', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySummarySceneRuleLogResponse(),
            self.do_rpcrequest('QuerySummarySceneRuleLog', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_summary_scene_rule_log_with_options_async(
        self,
        request: iot_20180120_models.QuerySummarySceneRuleLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySummarySceneRuleLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySummarySceneRuleLogResponse(),
            await self.do_rpcrequest_async('QuerySummarySceneRuleLog', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySuperDeviceGroupResponse(),
            self.do_rpcrequest('QuerySuperDeviceGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_super_device_group_with_options_async(
        self,
        request: iot_20180120_models.QuerySuperDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySuperDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySuperDeviceGroupResponse(),
            await self.do_rpcrequest_async('QuerySuperDeviceGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryTaskResponse(),
            self.do_rpcrequest('QueryTask', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_task_with_options_async(
        self,
        request: iot_20180120_models.QueryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryTaskResponse(),
            await self.do_rpcrequest_async('QueryTask', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryThingModelResponse(),
            self.do_rpcrequest('QueryThingModel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_thing_model_with_options_async(
        self,
        request: iot_20180120_models.QueryThingModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryThingModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryThingModelResponse(),
            await self.do_rpcrequest_async('QueryThingModel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryThingModelExtendConfigResponse(),
            self.do_rpcrequest('QueryThingModelExtendConfig', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_thing_model_extend_config_with_options_async(
        self,
        request: iot_20180120_models.QueryThingModelExtendConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryThingModelExtendConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryThingModelExtendConfigResponse(),
            await self.do_rpcrequest_async('QueryThingModelExtendConfig', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryThingModelExtendConfigPublishedResponse(),
            self.do_rpcrequest('QueryThingModelExtendConfigPublished', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_thing_model_extend_config_published_with_options_async(
        self,
        request: iot_20180120_models.QueryThingModelExtendConfigPublishedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryThingModelExtendConfigPublishedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryThingModelExtendConfigPublishedResponse(),
            await self.do_rpcrequest_async('QueryThingModelExtendConfigPublished', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryThingModelPublishedResponse(),
            self.do_rpcrequest('QueryThingModelPublished', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_thing_model_published_with_options_async(
        self,
        request: iot_20180120_models.QueryThingModelPublishedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryThingModelPublishedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryThingModelPublishedResponse(),
            await self.do_rpcrequest_async('QueryThingModelPublished', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryTopicReverseRouteTableResponse(),
            self.do_rpcrequest('QueryTopicReverseRouteTable', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_topic_reverse_route_table_with_options_async(
        self,
        request: iot_20180120_models.QueryTopicReverseRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryTopicReverseRouteTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryTopicReverseRouteTableResponse(),
            await self.do_rpcrequest_async('QueryTopicReverseRouteTable', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryTopicRouteTableResponse(),
            self.do_rpcrequest('QueryTopicRouteTable', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_topic_route_table_with_options_async(
        self,
        request: iot_20180120_models.QueryTopicRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryTopicRouteTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryTopicRouteTableResponse(),
            await self.do_rpcrequest_async('QueryTopicRouteTable', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def refresh_device_tunnel_share_password_with_options(
        self,
        request: iot_20180120_models.RefreshDeviceTunnelSharePasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RefreshDeviceTunnelSharePasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.RefreshDeviceTunnelSharePasswordResponse(),
            self.do_rpcrequest('RefreshDeviceTunnelSharePassword', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refresh_device_tunnel_share_password_with_options_async(
        self,
        request: iot_20180120_models.RefreshDeviceTunnelSharePasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RefreshDeviceTunnelSharePasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.RefreshDeviceTunnelSharePasswordResponse(),
            await self.do_rpcrequest_async('RefreshDeviceTunnelSharePassword', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.RefreshStudioAppTokenOpenResponse(),
            self.do_rpcrequest('RefreshStudioAppTokenOpen', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refresh_studio_app_token_open_with_options_async(
        self,
        request: iot_20180120_models.RefreshStudioAppTokenOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RefreshStudioAppTokenOpenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.RefreshStudioAppTokenOpenResponse(),
            await self.do_rpcrequest_async('RefreshStudioAppTokenOpen', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.RegisterDeviceResponse(),
            self.do_rpcrequest('RegisterDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def register_device_with_options_async(
        self,
        request: iot_20180120_models.RegisterDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RegisterDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.RegisterDeviceResponse(),
            await self.do_rpcrequest_async('RegisterDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ReleaseEdgeDriverVersionResponse(),
            self.do_rpcrequest('ReleaseEdgeDriverVersion', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_edge_driver_version_with_options_async(
        self,
        request: iot_20180120_models.ReleaseEdgeDriverVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ReleaseEdgeDriverVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ReleaseEdgeDriverVersionResponse(),
            await self.do_rpcrequest_async('ReleaseEdgeDriverVersion', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ReleaseProductResponse(),
            self.do_rpcrequest('ReleaseProduct', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_product_with_options_async(
        self,
        request: iot_20180120_models.ReleaseProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ReleaseProductResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ReleaseProductResponse(),
            await self.do_rpcrequest_async('ReleaseProduct', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.RemoveThingTopoResponse(),
            self.do_rpcrequest('RemoveThingTopo', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_thing_topo_with_options_async(
        self,
        request: iot_20180120_models.RemoveThingTopoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RemoveThingTopoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.RemoveThingTopoResponse(),
            await self.do_rpcrequest_async('RemoveThingTopo', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ReplaceEdgeInstanceGatewayResponse(),
            self.do_rpcrequest('ReplaceEdgeInstanceGateway', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def replace_edge_instance_gateway_with_options_async(
        self,
        request: iot_20180120_models.ReplaceEdgeInstanceGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ReplaceEdgeInstanceGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ReplaceEdgeInstanceGatewayResponse(),
            await self.do_rpcrequest_async('ReplaceEdgeInstanceGateway', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.RerunJobResponse(),
            self.do_rpcrequest('RerunJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rerun_job_with_options_async(
        self,
        request: iot_20180120_models.RerunJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RerunJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.RerunJobResponse(),
            await self.do_rpcrequest_async('RerunJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ResetConsumerGroupPositionResponse(),
            self.do_rpcrequest('ResetConsumerGroupPosition', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_consumer_group_position_with_options_async(
        self,
        request: iot_20180120_models.ResetConsumerGroupPositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ResetConsumerGroupPositionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ResetConsumerGroupPositionResponse(),
            await self.do_rpcrequest_async('ResetConsumerGroupPosition', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ResetThingResponse(),
            self.do_rpcrequest('ResetThing', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_thing_with_options_async(
        self,
        request: iot_20180120_models.ResetThingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ResetThingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.ResetThingResponse(),
            await self.do_rpcrequest_async('ResetThing', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def r_rpc_with_options(
        self,
        request: iot_20180120_models.RRpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RRpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.RRpcResponse(),
            self.do_rpcrequest('RRpc', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def r_rpc_with_options_async(
        self,
        request: iot_20180120_models.RRpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RRpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.RRpcResponse(),
            await self.do_rpcrequest_async('RRpc', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def r_rpc(
        self,
        request: iot_20180120_models.RRpcRequest,
    ) -> iot_20180120_models.RRpcResponse:
        runtime = util_models.RuntimeOptions()
        return self.r_rpc_with_options(request, runtime)

    async def r_rpc_async(
        self,
        request: iot_20180120_models.RRpcRequest,
    ) -> iot_20180120_models.RRpcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.r_rpc_with_options_async(request, runtime)

    def save_device_prop_with_options(
        self,
        request: iot_20180120_models.SaveDevicePropRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SaveDevicePropResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.SaveDevicePropResponse(),
            self.do_rpcrequest('SaveDeviceProp', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_device_prop_with_options_async(
        self,
        request: iot_20180120_models.SaveDevicePropRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SaveDevicePropResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.SaveDevicePropResponse(),
            await self.do_rpcrequest_async('SaveDeviceProp', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def set_device_desired_property_with_options(
        self,
        request: iot_20180120_models.SetDeviceDesiredPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetDeviceDesiredPropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.SetDeviceDesiredPropertyResponse(),
            self.do_rpcrequest('SetDeviceDesiredProperty', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_device_desired_property_with_options_async(
        self,
        request: iot_20180120_models.SetDeviceDesiredPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetDeviceDesiredPropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.SetDeviceDesiredPropertyResponse(),
            await self.do_rpcrequest_async('SetDeviceDesiredProperty', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.SetDeviceGroupTagsResponse(),
            self.do_rpcrequest('SetDeviceGroupTags', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_device_group_tags_with_options_async(
        self,
        request: iot_20180120_models.SetDeviceGroupTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetDeviceGroupTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.SetDeviceGroupTagsResponse(),
            await self.do_rpcrequest_async('SetDeviceGroupTags', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.SetDevicePropertyResponse(),
            self.do_rpcrequest('SetDeviceProperty', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_device_property_with_options_async(
        self,
        request: iot_20180120_models.SetDevicePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetDevicePropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.SetDevicePropertyResponse(),
            await self.do_rpcrequest_async('SetDeviceProperty', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.SetDevicesPropertyResponse(),
            self.do_rpcrequest('SetDevicesProperty', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_devices_property_with_options_async(
        self,
        request: iot_20180120_models.SetDevicesPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetDevicesPropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.SetDevicesPropertyResponse(),
            await self.do_rpcrequest_async('SetDevicesProperty', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.SetEdgeInstanceDriverConfigsResponse(),
            self.do_rpcrequest('SetEdgeInstanceDriverConfigs', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_edge_instance_driver_configs_with_options_async(
        self,
        request: iot_20180120_models.SetEdgeInstanceDriverConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetEdgeInstanceDriverConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.SetEdgeInstanceDriverConfigsResponse(),
            await self.do_rpcrequest_async('SetEdgeInstanceDriverConfigs', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.SetProductCertInfoResponse(),
            self.do_rpcrequest('SetProductCertInfo', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_product_cert_info_with_options_async(
        self,
        request: iot_20180120_models.SetProductCertInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetProductCertInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.SetProductCertInfoResponse(),
            await self.do_rpcrequest_async('SetProductCertInfo', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.SetStudioProjectCooperationResponse(),
            self.do_rpcrequest('SetStudioProjectCooperation', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_studio_project_cooperation_with_options_async(
        self,
        request: iot_20180120_models.SetStudioProjectCooperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetStudioProjectCooperationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.SetStudioProjectCooperationResponse(),
            await self.do_rpcrequest_async('SetStudioProjectCooperation', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.SetupStudioAppAuthModeOpenResponse(),
            self.do_rpcrequest('SetupStudioAppAuthModeOpen', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def setup_studio_app_auth_mode_open_with_options_async(
        self,
        request: iot_20180120_models.SetupStudioAppAuthModeOpenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SetupStudioAppAuthModeOpenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.SetupStudioAppAuthModeOpenResponse(),
            await self.do_rpcrequest_async('SetupStudioAppAuthModeOpen', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def speech_by_combination_with_options(
        self,
        request: iot_20180120_models.SpeechByCombinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SpeechByCombinationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.SpeechByCombinationResponse(),
            self.do_rpcrequest('SpeechByCombination', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def speech_by_combination_with_options_async(
        self,
        request: iot_20180120_models.SpeechByCombinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SpeechByCombinationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.SpeechByCombinationResponse(),
            await self.do_rpcrequest_async('SpeechByCombination', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def start_cpu_with_options(
        self,
        request: iot_20180120_models.StartCpuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.StartCpuResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.StartCpuResponse(),
            self.do_rpcrequest('StartCpu', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_cpu_with_options_async(
        self,
        request: iot_20180120_models.StartCpuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.StartCpuResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.StartCpuResponse(),
            await self.do_rpcrequest_async('StartCpu', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_cpu(
        self,
        request: iot_20180120_models.StartCpuRequest,
    ) -> iot_20180120_models.StartCpuResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_cpu_with_options(request, runtime)

    async def start_cpu_async(
        self,
        request: iot_20180120_models.StartCpuRequest,
    ) -> iot_20180120_models.StartCpuResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_cpu_with_options_async(request, runtime)

    def start_rule_with_options(
        self,
        request: iot_20180120_models.StartRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.StartRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.StartRuleResponse(),
            self.do_rpcrequest('StartRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_rule_with_options_async(
        self,
        request: iot_20180120_models.StartRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.StartRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.StartRuleResponse(),
            await self.do_rpcrequest_async('StartRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def stop_rule_with_options(
        self,
        request: iot_20180120_models.StopRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.StopRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.StopRuleResponse(),
            self.do_rpcrequest('StopRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_rule_with_options_async(
        self,
        request: iot_20180120_models.StopRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.StopRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.StopRuleResponse(),
            await self.do_rpcrequest_async('StopRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def sync_speech_by_combination_with_options(
        self,
        request: iot_20180120_models.SyncSpeechByCombinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SyncSpeechByCombinationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.SyncSpeechByCombinationResponse(),
            self.do_rpcrequest('SyncSpeechByCombination', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def sync_speech_by_combination_with_options_async(
        self,
        request: iot_20180120_models.SyncSpeechByCombinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SyncSpeechByCombinationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.SyncSpeechByCombinationResponse(),
            await self.do_rpcrequest_async('SyncSpeechByCombination', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        request: iot_20180120_models.TestSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.TestSpeechResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.TestSpeechResponse(),
            self.do_rpcrequest('TestSpeech', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def test_speech_with_options_async(
        self,
        request: iot_20180120_models.TestSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.TestSpeechResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.TestSpeechResponse(),
            await self.do_rpcrequest_async('TestSpeech', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def trigger_scene_rule_with_options(
        self,
        request: iot_20180120_models.TriggerSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.TriggerSceneRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.TriggerSceneRuleResponse(),
            self.do_rpcrequest('TriggerSceneRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def trigger_scene_rule_with_options_async(
        self,
        request: iot_20180120_models.TriggerSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.TriggerSceneRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.TriggerSceneRuleResponse(),
            await self.do_rpcrequest_async('TriggerSceneRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UnbindApplicationFromEdgeInstanceResponse(),
            self.do_rpcrequest('UnbindApplicationFromEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_application_from_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.UnbindApplicationFromEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UnbindApplicationFromEdgeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UnbindApplicationFromEdgeInstanceResponse(),
            await self.do_rpcrequest_async('UnbindApplicationFromEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UnbindDriverFromEdgeInstanceResponse(),
            self.do_rpcrequest('UnbindDriverFromEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_driver_from_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.UnbindDriverFromEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UnbindDriverFromEdgeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UnbindDriverFromEdgeInstanceResponse(),
            await self.do_rpcrequest_async('UnbindDriverFromEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def unbind_role_from_edge_instance_with_options(
        self,
        request: iot_20180120_models.UnbindRoleFromEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UnbindRoleFromEdgeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UnbindRoleFromEdgeInstanceResponse(),
            self.do_rpcrequest('UnbindRoleFromEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_role_from_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.UnbindRoleFromEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UnbindRoleFromEdgeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UnbindRoleFromEdgeInstanceResponse(),
            await self.do_rpcrequest_async('UnbindRoleFromEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UnbindSceneRuleFromEdgeInstanceResponse(),
            self.do_rpcrequest('UnbindSceneRuleFromEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_scene_rule_from_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.UnbindSceneRuleFromEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UnbindSceneRuleFromEdgeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UnbindSceneRuleFromEdgeInstanceResponse(),
            await self.do_rpcrequest_async('UnbindSceneRuleFromEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateConsumerGroupResponse(),
            self.do_rpcrequest('UpdateConsumerGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_consumer_group_with_options_async(
        self,
        request: iot_20180120_models.UpdateConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateConsumerGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateConsumerGroupResponse(),
            await self.do_rpcrequest_async('UpdateConsumerGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_device_group_with_options(
        self,
        request: iot_20180120_models.UpdateDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateDeviceGroupResponse(),
            self.do_rpcrequest('UpdateDeviceGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_device_group_with_options_async(
        self,
        request: iot_20180120_models.UpdateDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateDeviceGroupResponse(),
            await self.do_rpcrequest_async('UpdateDeviceGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateDeviceShadowResponse(),
            self.do_rpcrequest('UpdateDeviceShadow', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_device_shadow_with_options_async(
        self,
        request: iot_20180120_models.UpdateDeviceShadowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateDeviceShadowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateDeviceShadowResponse(),
            await self.do_rpcrequest_async('UpdateDeviceShadow', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateEdgeDriverVersionResponse(),
            self.do_rpcrequest('UpdateEdgeDriverVersion', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_edge_driver_version_with_options_async(
        self,
        request: iot_20180120_models.UpdateEdgeDriverVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateEdgeDriverVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateEdgeDriverVersionResponse(),
            await self.do_rpcrequest_async('UpdateEdgeDriverVersion', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateEdgeInstanceResponse(),
            self.do_rpcrequest('UpdateEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_edge_instance_with_options_async(
        self,
        request: iot_20180120_models.UpdateEdgeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateEdgeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateEdgeInstanceResponse(),
            await self.do_rpcrequest_async('UpdateEdgeInstance', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateEdgeInstanceChannelResponse(),
            self.do_rpcrequest('UpdateEdgeInstanceChannel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_edge_instance_channel_with_options_async(
        self,
        request: iot_20180120_models.UpdateEdgeInstanceChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateEdgeInstanceChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateEdgeInstanceChannelResponse(),
            await self.do_rpcrequest_async('UpdateEdgeInstanceChannel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateEdgeInstanceMessageRoutingResponse(),
            self.do_rpcrequest('UpdateEdgeInstanceMessageRouting', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_edge_instance_message_routing_with_options_async(
        self,
        request: iot_20180120_models.UpdateEdgeInstanceMessageRoutingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateEdgeInstanceMessageRoutingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateEdgeInstanceMessageRoutingResponse(),
            await self.do_rpcrequest_async('UpdateEdgeInstanceMessageRouting', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        request: iot_20180120_models.UpdateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateJobResponse(),
            self.do_rpcrequest('UpdateJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_job_with_options_async(
        self,
        request: iot_20180120_models.UpdateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateJobResponse(),
            await self.do_rpcrequest_async('UpdateJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateOTAModuleResponse(),
            self.do_rpcrequest('UpdateOTAModule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_otamodule_with_options_async(
        self,
        request: iot_20180120_models.UpdateOTAModuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateOTAModuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateOTAModuleResponse(),
            await self.do_rpcrequest_async('UpdateOTAModule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_product_with_options(
        self,
        request: iot_20180120_models.UpdateProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateProductResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateProductResponse(),
            self.do_rpcrequest('UpdateProduct', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_product_with_options_async(
        self,
        request: iot_20180120_models.UpdateProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateProductResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateProductResponse(),
            await self.do_rpcrequest_async('UpdateProduct', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateProductFilterConfigResponse(),
            self.do_rpcrequest('UpdateProductFilterConfig', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_product_filter_config_with_options_async(
        self,
        request: iot_20180120_models.UpdateProductFilterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateProductFilterConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateProductFilterConfigResponse(),
            await self.do_rpcrequest_async('UpdateProductFilterConfig', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateProductTagsResponse(),
            self.do_rpcrequest('UpdateProductTags', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_product_tags_with_options_async(
        self,
        request: iot_20180120_models.UpdateProductTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateProductTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateProductTagsResponse(),
            await self.do_rpcrequest_async('UpdateProductTags', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateProductTopicResponse(),
            self.do_rpcrequest('UpdateProductTopic', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_product_topic_with_options_async(
        self,
        request: iot_20180120_models.UpdateProductTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateProductTopicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateProductTopicResponse(),
            await self.do_rpcrequest_async('UpdateProductTopic', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateRuleResponse(),
            self.do_rpcrequest('UpdateRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_rule_with_options_async(
        self,
        request: iot_20180120_models.UpdateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateRuleResponse(),
            await self.do_rpcrequest_async('UpdateRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateRuleActionResponse(),
            self.do_rpcrequest('UpdateRuleAction', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_rule_action_with_options_async(
        self,
        request: iot_20180120_models.UpdateRuleActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateRuleActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateRuleActionResponse(),
            await self.do_rpcrequest_async('UpdateRuleAction', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateSceneRuleResponse(),
            self.do_rpcrequest('UpdateSceneRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_scene_rule_with_options_async(
        self,
        request: iot_20180120_models.UpdateSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateSceneRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateSceneRuleResponse(),
            await self.do_rpcrequest_async('UpdateSceneRule', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_speech_with_options(
        self,
        request: iot_20180120_models.UpdateSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateSpeechResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateSpeechResponse(),
            self.do_rpcrequest('UpdateSpeech', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_speech_with_options_async(
        self,
        request: iot_20180120_models.UpdateSpeechRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateSpeechResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateSpeechResponse(),
            await self.do_rpcrequest_async('UpdateSpeech', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateSubscribeRelationResponse(),
            self.do_rpcrequest('UpdateSubscribeRelation', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_subscribe_relation_with_options_async(
        self,
        request: iot_20180120_models.UpdateSubscribeRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateSubscribeRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateSubscribeRelationResponse(),
            await self.do_rpcrequest_async('UpdateSubscribeRelation', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateThingModelResponse(),
            self.do_rpcrequest('UpdateThingModel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_thing_model_with_options_async(
        self,
        request: iot_20180120_models.UpdateThingModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateThingModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateThingModelResponse(),
            await self.do_rpcrequest_async('UpdateThingModel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_thing_model_validation_config_with_options(
        self,
        request: iot_20180120_models.UpdateThingModelValidationConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateThingModelValidationConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateThingModelValidationConfigResponse(),
            self.do_rpcrequest('UpdateThingModelValidationConfig', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_thing_model_validation_config_with_options_async(
        self,
        request: iot_20180120_models.UpdateThingModelValidationConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateThingModelValidationConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateThingModelValidationConfigResponse(),
            await self.do_rpcrequest_async('UpdateThingModelValidationConfig', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_thing_model_validation_config(
        self,
        request: iot_20180120_models.UpdateThingModelValidationConfigRequest,
    ) -> iot_20180120_models.UpdateThingModelValidationConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_thing_model_validation_config_with_options(request, runtime)

    async def update_thing_model_validation_config_async(
        self,
        request: iot_20180120_models.UpdateThingModelValidationConfigRequest,
    ) -> iot_20180120_models.UpdateThingModelValidationConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_thing_model_validation_config_with_options_async(request, runtime)

    def update_thing_script_with_options(
        self,
        request: iot_20180120_models.UpdateThingScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateThingScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateThingScriptResponse(),
            self.do_rpcrequest('UpdateThingScript', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_thing_script_with_options_async(
        self,
        request: iot_20180120_models.UpdateThingScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateThingScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateThingScriptResponse(),
            await self.do_rpcrequest_async('UpdateThingScript', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
