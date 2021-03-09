# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

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
            'ap-northeast-2-pop': 'iot.ap-northeast-1.aliyuncs.com',
            'ap-south-1': 'iot.ap-northeast-1.aliyuncs.com',
            'ap-southeast-2': 'iot.ap-northeast-1.aliyuncs.com',
            'ap-southeast-3': 'iot.ap-northeast-1.aliyuncs.com',
            'ap-southeast-5': 'iot.ap-northeast-1.aliyuncs.com',
            'cn-beijing': 'iot.aliyuncs.com',
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
            'cn-north-2-gov-1': 'iot.aliyuncs.com',
            'cn-qingdao': 'iot.aliyuncs.com',
            'cn-qingdao-nebula': 'iot.aliyuncs.com',
            'cn-shanghai-et15-b01': 'iot.aliyuncs.com',
            'cn-shanghai-et2-b01': 'iot.aliyuncs.com',
            'cn-shanghai-finance-1': 'iot.aliyuncs.com',
            'cn-shanghai-inner': 'iot.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'iot.aliyuncs.com',
            'cn-shenzhen': 'iot.aliyuncs.com',
            'cn-shenzhen-finance-1': 'iot.aliyuncs.com',
            'cn-shenzhen-inner': 'iot.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'iot.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'iot.aliyuncs.com',
            'cn-wuhan': 'iot.aliyuncs.com',
            'cn-yushanfang': 'iot.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'iot.aliyuncs.com',
            'cn-zhangjiakou': 'iot.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'iot.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'iot.aliyuncs.com',
            'eu-west-1': 'iot.ap-northeast-1.aliyuncs.com',
            'eu-west-1-oxs': 'iot.ap-northeast-1.aliyuncs.com',
            'me-east-1': 'iot.ap-northeast-1.aliyuncs.com',
            'rus-west-1-pop': 'iot.ap-northeast-1.aliyuncs.com'
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

    def batch_add_device_group_relations_with_options(
        self,
        request: iot_20180120_models.BatchAddDeviceGroupRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchAddDeviceGroupRelationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.BatchAddDeviceGroupRelationsResponse().from_map(
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
        return iot_20180120_models.BatchAddDeviceGroupRelationsResponse().from_map(
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
        return iot_20180120_models.BatchAddThingTopoResponse().from_map(
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
        return iot_20180120_models.BatchAddThingTopoResponse().from_map(
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

    def batch_bind_device_to_edge_instance_with_driver_with_options(
        self,
        request: iot_20180120_models.BatchBindDeviceToEdgeInstanceWithDriverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchBindDeviceToEdgeInstanceWithDriverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.BatchBindDeviceToEdgeInstanceWithDriverResponse().from_map(
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
        return iot_20180120_models.BatchBindDeviceToEdgeInstanceWithDriverResponse().from_map(
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

    def batch_check_device_names_with_options(
        self,
        request: iot_20180120_models.BatchCheckDeviceNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchCheckDeviceNamesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.BatchCheckDeviceNamesResponse().from_map(
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
        return iot_20180120_models.BatchCheckDeviceNamesResponse().from_map(
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
        return iot_20180120_models.BatchClearEdgeInstanceDeviceConfigResponse().from_map(
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
        return iot_20180120_models.BatchClearEdgeInstanceDeviceConfigResponse().from_map(
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
        return iot_20180120_models.BatchDeleteDeviceGroupRelationsResponse().from_map(
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
        return iot_20180120_models.BatchDeleteDeviceGroupRelationsResponse().from_map(
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
        return iot_20180120_models.BatchDeleteEdgeInstanceChannelResponse().from_map(
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
        return iot_20180120_models.BatchDeleteEdgeInstanceChannelResponse().from_map(
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
        return iot_20180120_models.BatchGetDeviceBindStatusResponse().from_map(
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
        return iot_20180120_models.BatchGetDeviceBindStatusResponse().from_map(
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
        return iot_20180120_models.BatchGetDeviceStateResponse().from_map(
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
        return iot_20180120_models.BatchGetDeviceStateResponse().from_map(
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
        return iot_20180120_models.BatchGetEdgeDriverResponse().from_map(
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
        return iot_20180120_models.BatchGetEdgeDriverResponse().from_map(
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
        return iot_20180120_models.BatchGetEdgeInstanceChannelResponse().from_map(
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
        return iot_20180120_models.BatchGetEdgeInstanceChannelResponse().from_map(
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
        return iot_20180120_models.BatchGetEdgeInstanceDeviceChannelResponse().from_map(
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
        return iot_20180120_models.BatchGetEdgeInstanceDeviceChannelResponse().from_map(
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
        return iot_20180120_models.BatchGetEdgeInstanceDeviceConfigResponse().from_map(
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
        return iot_20180120_models.BatchGetEdgeInstanceDeviceConfigResponse().from_map(
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
        return iot_20180120_models.BatchGetEdgeInstanceDeviceDriverResponse().from_map(
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
        return iot_20180120_models.BatchGetEdgeInstanceDeviceDriverResponse().from_map(
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
        return iot_20180120_models.BatchGetEdgeInstanceDriverConfigsResponse().from_map(
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
        return iot_20180120_models.BatchGetEdgeInstanceDriverConfigsResponse().from_map(
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
        return iot_20180120_models.BatchPubResponse().from_map(
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
        return iot_20180120_models.BatchPubResponse().from_map(
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
        return iot_20180120_models.BatchQueryDeviceDetailResponse().from_map(
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
        return iot_20180120_models.BatchQueryDeviceDetailResponse().from_map(
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
        return iot_20180120_models.BatchRegisterDeviceResponse().from_map(
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
        return iot_20180120_models.BatchRegisterDeviceResponse().from_map(
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
        return iot_20180120_models.BatchRegisterDeviceWithApplyIdResponse().from_map(
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
        return iot_20180120_models.BatchRegisterDeviceWithApplyIdResponse().from_map(
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
        return iot_20180120_models.BatchSetEdgeInstanceDeviceChannelResponse().from_map(
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
        return iot_20180120_models.BatchSetEdgeInstanceDeviceChannelResponse().from_map(
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
        return iot_20180120_models.BatchSetEdgeInstanceDeviceConfigResponse().from_map(
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
        return iot_20180120_models.BatchSetEdgeInstanceDeviceConfigResponse().from_map(
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
        return iot_20180120_models.BatchUnbindDeviceFromEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.BatchUnbindDeviceFromEdgeInstanceResponse().from_map(
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

    def batch_update_device_nickname_with_options(
        self,
        request: iot_20180120_models.BatchUpdateDeviceNicknameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.BatchUpdateDeviceNicknameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.BatchUpdateDeviceNicknameResponse().from_map(
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
        return iot_20180120_models.BatchUpdateDeviceNicknameResponse().from_map(
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
        return iot_20180120_models.BindApplicationToEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.BindApplicationToEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.BindDriverToEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.BindDriverToEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.BindGatewayToEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.BindGatewayToEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.BindRoleToEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.BindRoleToEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.BindSceneRuleToEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.BindSceneRuleToEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.CancelJobResponse().from_map(
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
        return iot_20180120_models.CancelJobResponse().from_map(
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
        return iot_20180120_models.CancelOTAStrategyByJobResponse().from_map(
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
        return iot_20180120_models.CancelOTAStrategyByJobResponse().from_map(
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
        return iot_20180120_models.CancelOTATaskByDeviceResponse().from_map(
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
        return iot_20180120_models.CancelOTATaskByDeviceResponse().from_map(
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
        return iot_20180120_models.CancelOTATaskByJobResponse().from_map(
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
        return iot_20180120_models.CancelOTATaskByJobResponse().from_map(
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

    def clear_edge_instance_driver_configs_with_options(
        self,
        request: iot_20180120_models.ClearEdgeInstanceDriverConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ClearEdgeInstanceDriverConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.ClearEdgeInstanceDriverConfigsResponse().from_map(
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
        return iot_20180120_models.ClearEdgeInstanceDriverConfigsResponse().from_map(
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
        return iot_20180120_models.CloseEdgeInstanceDeploymentResponse().from_map(
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
        return iot_20180120_models.CloseEdgeInstanceDeploymentResponse().from_map(
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

    def copy_thing_model_with_options(
        self,
        request: iot_20180120_models.CopyThingModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CopyThingModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.CopyThingModelResponse().from_map(
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
        return iot_20180120_models.CopyThingModelResponse().from_map(
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
        return iot_20180120_models.CreateConsumerGroupResponse().from_map(
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
        return iot_20180120_models.CreateConsumerGroupResponse().from_map(
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
        return iot_20180120_models.CreateConsumerGroupSubscribeRelationResponse().from_map(
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
        return iot_20180120_models.CreateConsumerGroupSubscribeRelationResponse().from_map(
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
        return iot_20180120_models.CreateDataAPIServiceResponse().from_map(
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
        return iot_20180120_models.CreateDataAPIServiceResponse().from_map(
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
        return iot_20180120_models.CreateDeviceDistributeJobResponse().from_map(
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
        return iot_20180120_models.CreateDeviceDistributeJobResponse().from_map(
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
        return iot_20180120_models.CreateDeviceGroupResponse().from_map(
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
        return iot_20180120_models.CreateDeviceGroupResponse().from_map(
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
        return iot_20180120_models.CreateEdgeDriverResponse().from_map(
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
        return iot_20180120_models.CreateEdgeDriverResponse().from_map(
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
        return iot_20180120_models.CreateEdgeDriverVersionResponse().from_map(
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
        return iot_20180120_models.CreateEdgeDriverVersionResponse().from_map(
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
        return iot_20180120_models.CreateEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.CreateEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.CreateEdgeInstanceChannelResponse().from_map(
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
        return iot_20180120_models.CreateEdgeInstanceChannelResponse().from_map(
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
        return iot_20180120_models.CreateEdgeInstanceDeploymentResponse().from_map(
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
        return iot_20180120_models.CreateEdgeInstanceDeploymentResponse().from_map(
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

    def create_edge_oss_pre_signed_address_with_options(
        self,
        request: iot_20180120_models.CreateEdgeOssPreSignedAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateEdgeOssPreSignedAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.CreateEdgeOssPreSignedAddressResponse().from_map(
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
        return iot_20180120_models.CreateEdgeOssPreSignedAddressResponse().from_map(
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
        return iot_20180120_models.CreateJobResponse().from_map(
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
        return iot_20180120_models.CreateJobResponse().from_map(
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
        return iot_20180120_models.CreateLoRaNodesTaskResponse().from_map(
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
        return iot_20180120_models.CreateLoRaNodesTaskResponse().from_map(
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
        return iot_20180120_models.CreateOTADynamicUpgradeJobResponse().from_map(
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
        return iot_20180120_models.CreateOTADynamicUpgradeJobResponse().from_map(
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
        return iot_20180120_models.CreateOTAFirmwareResponse().from_map(
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
        return iot_20180120_models.CreateOTAFirmwareResponse().from_map(
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
        return iot_20180120_models.CreateOTAModuleResponse().from_map(
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
        return iot_20180120_models.CreateOTAModuleResponse().from_map(
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
        return iot_20180120_models.CreateOTAStaticUpgradeJobResponse().from_map(
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
        return iot_20180120_models.CreateOTAStaticUpgradeJobResponse().from_map(
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
        return iot_20180120_models.CreateOTAVerifyJobResponse().from_map(
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
        return iot_20180120_models.CreateOTAVerifyJobResponse().from_map(
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
        return iot_20180120_models.CreateProductResponse().from_map(
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
        return iot_20180120_models.CreateProductResponse().from_map(
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
        return iot_20180120_models.CreateProductDistributeJobResponse().from_map(
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
        return iot_20180120_models.CreateProductDistributeJobResponse().from_map(
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
        return iot_20180120_models.CreateProductTagsResponse().from_map(
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
        return iot_20180120_models.CreateProductTagsResponse().from_map(
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
        return iot_20180120_models.CreateProductTopicResponse().from_map(
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
        return iot_20180120_models.CreateProductTopicResponse().from_map(
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
        return iot_20180120_models.CreateRuleResponse().from_map(
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
        return iot_20180120_models.CreateRuleResponse().from_map(
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
        return iot_20180120_models.CreateRuleActionResponse().from_map(
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
        return iot_20180120_models.CreateRuleActionResponse().from_map(
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
        return iot_20180120_models.CreateRulengDistributeJobResponse().from_map(
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
        return iot_20180120_models.CreateRulengDistributeJobResponse().from_map(
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
        return iot_20180120_models.CreateSceneRuleResponse().from_map(
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
        return iot_20180120_models.CreateSceneRuleResponse().from_map(
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

    def create_subscribe_relation_with_options(
        self,
        request: iot_20180120_models.CreateSubscribeRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.CreateSubscribeRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.CreateSubscribeRelationResponse().from_map(
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
        return iot_20180120_models.CreateSubscribeRelationResponse().from_map(
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
        return iot_20180120_models.CreateThingModelResponse().from_map(
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
        return iot_20180120_models.CreateThingModelResponse().from_map(
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
        return iot_20180120_models.CreateThingScriptResponse().from_map(
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
        return iot_20180120_models.CreateThingScriptResponse().from_map(
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
        return iot_20180120_models.CreateTopicRouteTableResponse().from_map(
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
        return iot_20180120_models.CreateTopicRouteTableResponse().from_map(
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
        return iot_20180120_models.DeleteConsumerGroupResponse().from_map(
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
        return iot_20180120_models.DeleteConsumerGroupResponse().from_map(
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
        return iot_20180120_models.DeleteConsumerGroupSubscribeRelationResponse().from_map(
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
        return iot_20180120_models.DeleteConsumerGroupSubscribeRelationResponse().from_map(
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
        return iot_20180120_models.DeleteDeviceResponse().from_map(
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
        return iot_20180120_models.DeleteDeviceResponse().from_map(
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
        return iot_20180120_models.DeleteDeviceDistributeJobResponse().from_map(
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
        return iot_20180120_models.DeleteDeviceDistributeJobResponse().from_map(
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
        return iot_20180120_models.DeleteDeviceFileResponse().from_map(
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
        return iot_20180120_models.DeleteDeviceFileResponse().from_map(
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
        return iot_20180120_models.DeleteDeviceGroupResponse().from_map(
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
        return iot_20180120_models.DeleteDeviceGroupResponse().from_map(
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
        return iot_20180120_models.DeleteDevicePropResponse().from_map(
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
        return iot_20180120_models.DeleteDevicePropResponse().from_map(
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
        return iot_20180120_models.DeleteEdgeDriverResponse().from_map(
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
        return iot_20180120_models.DeleteEdgeDriverResponse().from_map(
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
        return iot_20180120_models.DeleteEdgeDriverVersionResponse().from_map(
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
        return iot_20180120_models.DeleteEdgeDriverVersionResponse().from_map(
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
        return iot_20180120_models.DeleteEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.DeleteEdgeInstanceResponse().from_map(
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

    def delete_job_with_options(
        self,
        request: iot_20180120_models.DeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.DeleteJobResponse().from_map(
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
        return iot_20180120_models.DeleteJobResponse().from_map(
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
        return iot_20180120_models.DeleteOTAFirmwareResponse().from_map(
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
        return iot_20180120_models.DeleteOTAFirmwareResponse().from_map(
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
        return iot_20180120_models.DeleteOTAModuleResponse().from_map(
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
        return iot_20180120_models.DeleteOTAModuleResponse().from_map(
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
        return iot_20180120_models.DeleteProductResponse().from_map(
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
        return iot_20180120_models.DeleteProductResponse().from_map(
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
        return iot_20180120_models.DeleteProductTagsResponse().from_map(
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
        return iot_20180120_models.DeleteProductTagsResponse().from_map(
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
        return iot_20180120_models.DeleteProductTopicResponse().from_map(
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
        return iot_20180120_models.DeleteProductTopicResponse().from_map(
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
        return iot_20180120_models.DeleteRuleResponse().from_map(
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
        return iot_20180120_models.DeleteRuleResponse().from_map(
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
        return iot_20180120_models.DeleteRuleActionResponse().from_map(
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
        return iot_20180120_models.DeleteRuleActionResponse().from_map(
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
        return iot_20180120_models.DeleteSceneRuleResponse().from_map(
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
        return iot_20180120_models.DeleteSceneRuleResponse().from_map(
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

    def delete_subscribe_relation_with_options(
        self,
        request: iot_20180120_models.DeleteSubscribeRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DeleteSubscribeRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.DeleteSubscribeRelationResponse().from_map(
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
        return iot_20180120_models.DeleteSubscribeRelationResponse().from_map(
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
        return iot_20180120_models.DeleteThingModelResponse().from_map(
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
        return iot_20180120_models.DeleteThingModelResponse().from_map(
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
        return iot_20180120_models.DeleteTopicRouteTableResponse().from_map(
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
        return iot_20180120_models.DeleteTopicRouteTableResponse().from_map(
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

    def disable_scene_rule_with_options(
        self,
        request: iot_20180120_models.DisableSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.DisableSceneRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.DisableSceneRuleResponse().from_map(
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
        return iot_20180120_models.DisableSceneRuleResponse().from_map(
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
        return iot_20180120_models.DisableThingResponse().from_map(
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
        return iot_20180120_models.DisableThingResponse().from_map(
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

    def enable_scene_rule_with_options(
        self,
        request: iot_20180120_models.EnableSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.EnableSceneRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.EnableSceneRuleResponse().from_map(
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
        return iot_20180120_models.EnableSceneRuleResponse().from_map(
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
        return iot_20180120_models.EnableThingResponse().from_map(
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
        return iot_20180120_models.EnableThingResponse().from_map(
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
        return iot_20180120_models.GenerateDeviceNameListURLResponse().from_map(
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
        return iot_20180120_models.GenerateDeviceNameListURLResponse().from_map(
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
        return iot_20180120_models.GenerateFileUploadURLResponse().from_map(
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
        return iot_20180120_models.GenerateFileUploadURLResponse().from_map(
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
        return iot_20180120_models.GenerateOTAUploadURLResponse().from_map(
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
        return iot_20180120_models.GenerateOTAUploadURLResponse().from_map(
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
        return iot_20180120_models.GetDataAPIServiceDetailResponse().from_map(
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
        return iot_20180120_models.GetDataAPIServiceDetailResponse().from_map(
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
        return iot_20180120_models.GetDeviceShadowResponse().from_map(
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
        return iot_20180120_models.GetDeviceShadowResponse().from_map(
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
        return iot_20180120_models.GetDeviceStatusResponse().from_map(
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
        return iot_20180120_models.GetDeviceStatusResponse().from_map(
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

    def get_edge_driver_version_with_options(
        self,
        request: iot_20180120_models.GetEdgeDriverVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetEdgeDriverVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.GetEdgeDriverVersionResponse().from_map(
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
        return iot_20180120_models.GetEdgeDriverVersionResponse().from_map(
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
        return iot_20180120_models.GetEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.GetEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.GetEdgeInstanceDeploymentResponse().from_map(
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
        return iot_20180120_models.GetEdgeInstanceDeploymentResponse().from_map(
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

    def get_gateway_by_sub_device_with_options(
        self,
        request: iot_20180120_models.GetGatewayBySubDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetGatewayBySubDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.GetGatewayBySubDeviceResponse().from_map(
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
        return iot_20180120_models.GetGatewayBySubDeviceResponse().from_map(
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
        return iot_20180120_models.GetLoraNodesTaskResponse().from_map(
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
        return iot_20180120_models.GetLoraNodesTaskResponse().from_map(
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
        return iot_20180120_models.GetNodesAddingTaskResponse().from_map(
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
        return iot_20180120_models.GetNodesAddingTaskResponse().from_map(
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
        return iot_20180120_models.GetRuleResponse().from_map(
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
        return iot_20180120_models.GetRuleResponse().from_map(
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
        return iot_20180120_models.GetRuleActionResponse().from_map(
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
        return iot_20180120_models.GetRuleActionResponse().from_map(
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
        return iot_20180120_models.GetSceneRuleResponse().from_map(
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
        return iot_20180120_models.GetSceneRuleResponse().from_map(
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

    def get_thing_model_tsl_with_options(
        self,
        request: iot_20180120_models.GetThingModelTslRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.GetThingModelTslResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.GetThingModelTslResponse().from_map(
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
        return iot_20180120_models.GetThingModelTslResponse().from_map(
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
        return iot_20180120_models.GetThingModelTslPublishedResponse().from_map(
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
        return iot_20180120_models.GetThingModelTslPublishedResponse().from_map(
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
        return iot_20180120_models.GetThingScriptResponse().from_map(
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
        return iot_20180120_models.GetThingScriptResponse().from_map(
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
        return iot_20180120_models.GetThingTemplateResponse().from_map(
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
        return iot_20180120_models.GetThingTemplateResponse().from_map(
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
        return iot_20180120_models.GetThingTopoResponse().from_map(
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
        return iot_20180120_models.GetThingTopoResponse().from_map(
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
        return iot_20180120_models.ImportThingModelTslResponse().from_map(
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
        return iot_20180120_models.ImportThingModelTslResponse().from_map(
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
        return iot_20180120_models.InvokeDataAPIServiceResponse().from_map(
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
        return iot_20180120_models.InvokeDataAPIServiceResponse().from_map(
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
        return iot_20180120_models.InvokeThingServiceResponse().from_map(
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
        return iot_20180120_models.InvokeThingServiceResponse().from_map(
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
        return iot_20180120_models.InvokeThingsServiceResponse().from_map(
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
        return iot_20180120_models.InvokeThingsServiceResponse().from_map(
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

    def list_device_distribute_job_with_options(
        self,
        request: iot_20180120_models.ListDeviceDistributeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListDeviceDistributeJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.ListDeviceDistributeJobResponse().from_map(
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
        return iot_20180120_models.ListDeviceDistributeJobResponse().from_map(
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
        return iot_20180120_models.ListDistributedDeviceResponse().from_map(
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
        return iot_20180120_models.ListDistributedDeviceResponse().from_map(
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
        return iot_20180120_models.ListDistributedProductResponse().from_map(
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
        return iot_20180120_models.ListDistributedProductResponse().from_map(
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
        return iot_20180120_models.ListJobResponse().from_map(
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
        return iot_20180120_models.ListJobResponse().from_map(
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
        return iot_20180120_models.ListOTAFirmwareResponse().from_map(
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
        return iot_20180120_models.ListOTAFirmwareResponse().from_map(
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
        return iot_20180120_models.ListOTAJobByDeviceResponse().from_map(
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
        return iot_20180120_models.ListOTAJobByDeviceResponse().from_map(
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
        return iot_20180120_models.ListOTAJobByFirmwareResponse().from_map(
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
        return iot_20180120_models.ListOTAJobByFirmwareResponse().from_map(
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
        return iot_20180120_models.ListOTAModuleByProductResponse().from_map(
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
        return iot_20180120_models.ListOTAModuleByProductResponse().from_map(
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
        return iot_20180120_models.ListOTAModuleVersionsByDeviceResponse().from_map(
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
        return iot_20180120_models.ListOTAModuleVersionsByDeviceResponse().from_map(
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
        return iot_20180120_models.ListOTATaskByJobResponse().from_map(
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
        return iot_20180120_models.ListOTATaskByJobResponse().from_map(
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

    def list_product_by_tags_with_options(
        self,
        request: iot_20180120_models.ListProductByTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ListProductByTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.ListProductByTagsResponse().from_map(
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
        return iot_20180120_models.ListProductByTagsResponse().from_map(
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
        return iot_20180120_models.ListProductTagsResponse().from_map(
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
        return iot_20180120_models.ListProductTagsResponse().from_map(
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
        return iot_20180120_models.ListRuleResponse().from_map(
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
        return iot_20180120_models.ListRuleResponse().from_map(
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
        return iot_20180120_models.ListRuleActionsResponse().from_map(
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
        return iot_20180120_models.ListRuleActionsResponse().from_map(
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
        return iot_20180120_models.ListTaskResponse().from_map(
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
        return iot_20180120_models.ListTaskResponse().from_map(
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
        return iot_20180120_models.ListTaskByPageResponse().from_map(
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
        return iot_20180120_models.ListTaskByPageResponse().from_map(
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
        return iot_20180120_models.ListThingModelVersionResponse().from_map(
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
        return iot_20180120_models.ListThingModelVersionResponse().from_map(
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
        return iot_20180120_models.ListThingTemplatesResponse().from_map(
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
        return iot_20180120_models.ListThingTemplatesResponse().from_map(
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
        return iot_20180120_models.NotifyAddThingTopoResponse().from_map(
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
        return iot_20180120_models.NotifyAddThingTopoResponse().from_map(
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
        return iot_20180120_models.OpenIotServiceResponse().from_map(
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
        return iot_20180120_models.OpenIotServiceResponse().from_map(
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

    def pub_with_options(
        self,
        request: iot_20180120_models.PubRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PubResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.PubResponse().from_map(
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
        return iot_20180120_models.PubResponse().from_map(
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
        return iot_20180120_models.PubBroadcastResponse().from_map(
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
        return iot_20180120_models.PubBroadcastResponse().from_map(
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

    def publish_thing_model_with_options(
        self,
        request: iot_20180120_models.PublishThingModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.PublishThingModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.PublishThingModelResponse().from_map(
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
        return iot_20180120_models.PublishThingModelResponse().from_map(
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

    def query_app_device_list_with_options(
        self,
        request: iot_20180120_models.QueryAppDeviceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryAppDeviceListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.QueryAppDeviceListResponse().from_map(
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
        return iot_20180120_models.QueryAppDeviceListResponse().from_map(
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
        return iot_20180120_models.QueryBatchRegisterDeviceStatusResponse().from_map(
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
        return iot_20180120_models.QueryBatchRegisterDeviceStatusResponse().from_map(
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
        return iot_20180120_models.QueryCertUrlByApplyIdResponse().from_map(
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
        return iot_20180120_models.QueryCertUrlByApplyIdResponse().from_map(
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
        return iot_20180120_models.QueryConsumerGroupByGroupIdResponse().from_map(
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
        return iot_20180120_models.QueryConsumerGroupByGroupIdResponse().from_map(
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
        return iot_20180120_models.QueryConsumerGroupListResponse().from_map(
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
        return iot_20180120_models.QueryConsumerGroupListResponse().from_map(
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
        return iot_20180120_models.QueryConsumerGroupStatusResponse().from_map(
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
        return iot_20180120_models.QueryConsumerGroupStatusResponse().from_map(
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
        return iot_20180120_models.QueryDetailSceneRuleLogResponse().from_map(
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
        return iot_20180120_models.QueryDetailSceneRuleLogResponse().from_map(
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
        return iot_20180120_models.QueryDeviceResponse().from_map(
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
        return iot_20180120_models.QueryDeviceResponse().from_map(
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
        return iot_20180120_models.QueryDeviceBySQLResponse().from_map(
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
        return iot_20180120_models.QueryDeviceBySQLResponse().from_map(
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
        return iot_20180120_models.QueryDeviceByStatusResponse().from_map(
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
        return iot_20180120_models.QueryDeviceByStatusResponse().from_map(
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
        return iot_20180120_models.QueryDeviceByTagsResponse().from_map(
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
        return iot_20180120_models.QueryDeviceByTagsResponse().from_map(
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
        return iot_20180120_models.QueryDeviceCertResponse().from_map(
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
        return iot_20180120_models.QueryDeviceCertResponse().from_map(
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
        return iot_20180120_models.QueryDeviceDesiredPropertyResponse().from_map(
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
        return iot_20180120_models.QueryDeviceDesiredPropertyResponse().from_map(
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
        return iot_20180120_models.QueryDeviceDetailResponse().from_map(
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
        return iot_20180120_models.QueryDeviceDetailResponse().from_map(
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
        return iot_20180120_models.QueryDeviceDistributeDetailResponse().from_map(
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
        return iot_20180120_models.QueryDeviceDistributeDetailResponse().from_map(
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
        return iot_20180120_models.QueryDeviceDistributeJobResponse().from_map(
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
        return iot_20180120_models.QueryDeviceDistributeJobResponse().from_map(
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
        return iot_20180120_models.QueryDeviceEventDataResponse().from_map(
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
        return iot_20180120_models.QueryDeviceEventDataResponse().from_map(
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
        return iot_20180120_models.QueryDeviceFileResponse().from_map(
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
        return iot_20180120_models.QueryDeviceFileResponse().from_map(
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
        return iot_20180120_models.QueryDeviceFileListResponse().from_map(
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
        return iot_20180120_models.QueryDeviceFileListResponse().from_map(
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
        return iot_20180120_models.QueryDeviceGroupByDeviceResponse().from_map(
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
        return iot_20180120_models.QueryDeviceGroupByDeviceResponse().from_map(
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
        return iot_20180120_models.QueryDeviceGroupByTagsResponse().from_map(
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
        return iot_20180120_models.QueryDeviceGroupByTagsResponse().from_map(
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
        return iot_20180120_models.QueryDeviceGroupInfoResponse().from_map(
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
        return iot_20180120_models.QueryDeviceGroupInfoResponse().from_map(
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
        return iot_20180120_models.QueryDeviceGroupListResponse().from_map(
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
        return iot_20180120_models.QueryDeviceGroupListResponse().from_map(
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
        return iot_20180120_models.QueryDeviceGroupTagListResponse().from_map(
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
        return iot_20180120_models.QueryDeviceGroupTagListResponse().from_map(
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

    def query_device_list_by_device_group_with_options(
        self,
        request: iot_20180120_models.QueryDeviceListByDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryDeviceListByDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.QueryDeviceListByDeviceGroupResponse().from_map(
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
        return iot_20180120_models.QueryDeviceListByDeviceGroupResponse().from_map(
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
        return iot_20180120_models.QueryDeviceOriginalEventDataResponse().from_map(
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
        return iot_20180120_models.QueryDeviceOriginalEventDataResponse().from_map(
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
        return iot_20180120_models.QueryDeviceOriginalPropertyDataResponse().from_map(
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
        return iot_20180120_models.QueryDeviceOriginalPropertyDataResponse().from_map(
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
        return iot_20180120_models.QueryDeviceOriginalPropertyStatusResponse().from_map(
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
        return iot_20180120_models.QueryDeviceOriginalPropertyStatusResponse().from_map(
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
        return iot_20180120_models.QueryDeviceOriginalServiceDataResponse().from_map(
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
        return iot_20180120_models.QueryDeviceOriginalServiceDataResponse().from_map(
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
        return iot_20180120_models.QueryDevicePropResponse().from_map(
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
        return iot_20180120_models.QueryDevicePropResponse().from_map(
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
        return iot_20180120_models.QueryDevicePropertiesDataResponse().from_map(
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
        return iot_20180120_models.QueryDevicePropertiesDataResponse().from_map(
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
        return iot_20180120_models.QueryDevicePropertyDataResponse().from_map(
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
        return iot_20180120_models.QueryDevicePropertyDataResponse().from_map(
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
        return iot_20180120_models.QueryDevicePropertyStatusResponse().from_map(
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
        return iot_20180120_models.QueryDevicePropertyStatusResponse().from_map(
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
        return iot_20180120_models.QueryDeviceServiceDataResponse().from_map(
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
        return iot_20180120_models.QueryDeviceServiceDataResponse().from_map(
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
        return iot_20180120_models.QueryDeviceStatisticsResponse().from_map(
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
        return iot_20180120_models.QueryDeviceStatisticsResponse().from_map(
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
        return iot_20180120_models.QueryEdgeDriverResponse().from_map(
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
        return iot_20180120_models.QueryEdgeDriverResponse().from_map(
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
        return iot_20180120_models.QueryEdgeDriverVersionResponse().from_map(
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
        return iot_20180120_models.QueryEdgeDriverVersionResponse().from_map(
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
        return iot_20180120_models.QueryEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.QueryEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.QueryEdgeInstanceChannelResponse().from_map(
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
        return iot_20180120_models.QueryEdgeInstanceChannelResponse().from_map(
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
        return iot_20180120_models.QueryEdgeInstanceDeviceResponse().from_map(
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
        return iot_20180120_models.QueryEdgeInstanceDeviceResponse().from_map(
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
        return iot_20180120_models.QueryEdgeInstanceDeviceByDriverResponse().from_map(
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
        return iot_20180120_models.QueryEdgeInstanceDeviceByDriverResponse().from_map(
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
        return iot_20180120_models.QueryEdgeInstanceDriverResponse().from_map(
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
        return iot_20180120_models.QueryEdgeInstanceDriverResponse().from_map(
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
        return iot_20180120_models.QueryEdgeInstanceGatewayResponse().from_map(
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
        return iot_20180120_models.QueryEdgeInstanceGatewayResponse().from_map(
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
        return iot_20180120_models.QueryEdgeInstanceHistoricDeploymentResponse().from_map(
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
        return iot_20180120_models.QueryEdgeInstanceHistoricDeploymentResponse().from_map(
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

    def query_edge_instance_scene_rule_with_options(
        self,
        request: iot_20180120_models.QueryEdgeInstanceSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryEdgeInstanceSceneRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.QueryEdgeInstanceSceneRuleResponse().from_map(
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
        return iot_20180120_models.QueryEdgeInstanceSceneRuleResponse().from_map(
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
        return iot_20180120_models.QueryJobResponse().from_map(
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
        return iot_20180120_models.QueryJobResponse().from_map(
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
        return iot_20180120_models.QueryJobStatisticsResponse().from_map(
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
        return iot_20180120_models.QueryJobStatisticsResponse().from_map(
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
        return iot_20180120_models.QueryLoRaJoinPermissionsResponse().from_map(
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
        return iot_20180120_models.QueryLoRaJoinPermissionsResponse().from_map(
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

    def query_otafirmware_with_options(
        self,
        request: iot_20180120_models.QueryOTAFirmwareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QueryOTAFirmwareResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.QueryOTAFirmwareResponse().from_map(
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
        return iot_20180120_models.QueryOTAFirmwareResponse().from_map(
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
        return iot_20180120_models.QueryOTAJobResponse().from_map(
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
        return iot_20180120_models.QueryOTAJobResponse().from_map(
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
        return iot_20180120_models.QueryPageByApplyIdResponse().from_map(
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
        return iot_20180120_models.QueryPageByApplyIdResponse().from_map(
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
        return iot_20180120_models.QueryProductResponse().from_map(
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
        return iot_20180120_models.QueryProductResponse().from_map(
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
        return iot_20180120_models.QueryProductCertInfoResponse().from_map(
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
        return iot_20180120_models.QueryProductCertInfoResponse().from_map(
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
        return iot_20180120_models.QueryProductListResponse().from_map(
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
        return iot_20180120_models.QueryProductListResponse().from_map(
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
        return iot_20180120_models.QueryProductTopicResponse().from_map(
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
        return iot_20180120_models.QueryProductTopicResponse().from_map(
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
        return iot_20180120_models.QuerySceneRuleResponse().from_map(
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
        return iot_20180120_models.QuerySceneRuleResponse().from_map(
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

    def query_subscribe_relation_with_options(
        self,
        request: iot_20180120_models.QuerySubscribeRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.QuerySubscribeRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.QuerySubscribeRelationResponse().from_map(
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
        return iot_20180120_models.QuerySubscribeRelationResponse().from_map(
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
        return iot_20180120_models.QuerySummarySceneRuleLogResponse().from_map(
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
        return iot_20180120_models.QuerySummarySceneRuleLogResponse().from_map(
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
        return iot_20180120_models.QuerySuperDeviceGroupResponse().from_map(
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
        return iot_20180120_models.QuerySuperDeviceGroupResponse().from_map(
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
        return iot_20180120_models.QueryTaskResponse().from_map(
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
        return iot_20180120_models.QueryTaskResponse().from_map(
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
        return iot_20180120_models.QueryThingModelResponse().from_map(
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
        return iot_20180120_models.QueryThingModelResponse().from_map(
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
        return iot_20180120_models.QueryThingModelExtendConfigResponse().from_map(
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
        return iot_20180120_models.QueryThingModelExtendConfigResponse().from_map(
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
        return iot_20180120_models.QueryThingModelExtendConfigPublishedResponse().from_map(
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
        return iot_20180120_models.QueryThingModelExtendConfigPublishedResponse().from_map(
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
        return iot_20180120_models.QueryThingModelPublishedResponse().from_map(
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
        return iot_20180120_models.QueryThingModelPublishedResponse().from_map(
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
        return iot_20180120_models.QueryTopicReverseRouteTableResponse().from_map(
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
        return iot_20180120_models.QueryTopicReverseRouteTableResponse().from_map(
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
        return iot_20180120_models.QueryTopicRouteTableResponse().from_map(
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
        return iot_20180120_models.QueryTopicRouteTableResponse().from_map(
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

    def register_device_with_options(
        self,
        request: iot_20180120_models.RegisterDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RegisterDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.RegisterDeviceResponse().from_map(
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
        return iot_20180120_models.RegisterDeviceResponse().from_map(
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
        return iot_20180120_models.ReleaseEdgeDriverVersionResponse().from_map(
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
        return iot_20180120_models.ReleaseEdgeDriverVersionResponse().from_map(
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

    def remove_thing_topo_with_options(
        self,
        request: iot_20180120_models.RemoveThingTopoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.RemoveThingTopoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.RemoveThingTopoResponse().from_map(
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
        return iot_20180120_models.RemoveThingTopoResponse().from_map(
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
        return iot_20180120_models.ReplaceEdgeInstanceGatewayResponse().from_map(
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
        return iot_20180120_models.ReplaceEdgeInstanceGatewayResponse().from_map(
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

    def reset_consumer_group_position_with_options(
        self,
        request: iot_20180120_models.ResetConsumerGroupPositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.ResetConsumerGroupPositionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.ResetConsumerGroupPositionResponse().from_map(
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
        return iot_20180120_models.ResetConsumerGroupPositionResponse().from_map(
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
        return iot_20180120_models.ResetThingResponse().from_map(
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
        return iot_20180120_models.ResetThingResponse().from_map(
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
        return iot_20180120_models.RRpcResponse().from_map(
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
        return iot_20180120_models.RRpcResponse().from_map(
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
        return iot_20180120_models.SaveDevicePropResponse().from_map(
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
        return iot_20180120_models.SaveDevicePropResponse().from_map(
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
        return iot_20180120_models.SetDeviceDesiredPropertyResponse().from_map(
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
        return iot_20180120_models.SetDeviceDesiredPropertyResponse().from_map(
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
        return iot_20180120_models.SetDeviceGroupTagsResponse().from_map(
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
        return iot_20180120_models.SetDeviceGroupTagsResponse().from_map(
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
        return iot_20180120_models.SetDevicePropertyResponse().from_map(
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
        return iot_20180120_models.SetDevicePropertyResponse().from_map(
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
        return iot_20180120_models.SetDevicesPropertyResponse().from_map(
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
        return iot_20180120_models.SetDevicesPropertyResponse().from_map(
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
        return iot_20180120_models.SetEdgeInstanceDriverConfigsResponse().from_map(
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
        return iot_20180120_models.SetEdgeInstanceDriverConfigsResponse().from_map(
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
        return iot_20180120_models.SetProductCertInfoResponse().from_map(
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
        return iot_20180120_models.SetProductCertInfoResponse().from_map(
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

    def speech_by_combination_with_options(
        self,
        request: iot_20180120_models.SpeechByCombinationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.SpeechByCombinationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.SpeechByCombinationResponse().from_map(
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
        return iot_20180120_models.SpeechByCombinationResponse().from_map(
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
        return iot_20180120_models.StartCpuResponse().from_map(
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
        return iot_20180120_models.StartCpuResponse().from_map(
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
        return iot_20180120_models.StartRuleResponse().from_map(
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
        return iot_20180120_models.StartRuleResponse().from_map(
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
        return iot_20180120_models.StopRuleResponse().from_map(
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
        return iot_20180120_models.StopRuleResponse().from_map(
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

    def trigger_scene_rule_with_options(
        self,
        request: iot_20180120_models.TriggerSceneRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.TriggerSceneRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.TriggerSceneRuleResponse().from_map(
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
        return iot_20180120_models.TriggerSceneRuleResponse().from_map(
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
        return iot_20180120_models.UnbindApplicationFromEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.UnbindApplicationFromEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.UnbindDriverFromEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.UnbindDriverFromEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.UnbindRoleFromEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.UnbindRoleFromEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.UnbindSceneRuleFromEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.UnbindSceneRuleFromEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.UpdateConsumerGroupResponse().from_map(
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
        return iot_20180120_models.UpdateConsumerGroupResponse().from_map(
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
        return iot_20180120_models.UpdateDeviceGroupResponse().from_map(
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
        return iot_20180120_models.UpdateDeviceGroupResponse().from_map(
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
        return iot_20180120_models.UpdateDeviceShadowResponse().from_map(
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
        return iot_20180120_models.UpdateDeviceShadowResponse().from_map(
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
        return iot_20180120_models.UpdateEdgeDriverVersionResponse().from_map(
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
        return iot_20180120_models.UpdateEdgeDriverVersionResponse().from_map(
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
        return iot_20180120_models.UpdateEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.UpdateEdgeInstanceResponse().from_map(
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
        return iot_20180120_models.UpdateEdgeInstanceChannelResponse().from_map(
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
        return iot_20180120_models.UpdateEdgeInstanceChannelResponse().from_map(
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

    def update_job_with_options(
        self,
        request: iot_20180120_models.UpdateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.UpdateJobResponse().from_map(
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
        return iot_20180120_models.UpdateJobResponse().from_map(
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
        return iot_20180120_models.UpdateOTAModuleResponse().from_map(
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
        return iot_20180120_models.UpdateOTAModuleResponse().from_map(
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
        return iot_20180120_models.UpdateProductResponse().from_map(
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
        return iot_20180120_models.UpdateProductResponse().from_map(
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
        return iot_20180120_models.UpdateProductFilterConfigResponse().from_map(
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
        return iot_20180120_models.UpdateProductFilterConfigResponse().from_map(
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
        return iot_20180120_models.UpdateProductTagsResponse().from_map(
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
        return iot_20180120_models.UpdateProductTagsResponse().from_map(
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
        return iot_20180120_models.UpdateProductTopicResponse().from_map(
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
        return iot_20180120_models.UpdateProductTopicResponse().from_map(
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
        return iot_20180120_models.UpdateRuleResponse().from_map(
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
        return iot_20180120_models.UpdateRuleResponse().from_map(
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
        return iot_20180120_models.UpdateRuleActionResponse().from_map(
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
        return iot_20180120_models.UpdateRuleActionResponse().from_map(
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
        return iot_20180120_models.UpdateSceneRuleResponse().from_map(
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
        return iot_20180120_models.UpdateSceneRuleResponse().from_map(
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

    def update_subscribe_relation_with_options(
        self,
        request: iot_20180120_models.UpdateSubscribeRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iot_20180120_models.UpdateSubscribeRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iot_20180120_models.UpdateSubscribeRelationResponse().from_map(
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
        return iot_20180120_models.UpdateSubscribeRelationResponse().from_map(
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
        return iot_20180120_models.UpdateThingModelResponse().from_map(
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
        return iot_20180120_models.UpdateThingModelResponse().from_map(
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
        return iot_20180120_models.UpdateThingModelValidationConfigResponse().from_map(
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
        return iot_20180120_models.UpdateThingModelValidationConfigResponse().from_map(
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
        return iot_20180120_models.UpdateThingScriptResponse().from_map(
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
        return iot_20180120_models.UpdateThingScriptResponse().from_map(
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
