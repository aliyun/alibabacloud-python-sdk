# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_linkvisual20180120 import models as linkvisual_20180120_models
from alibabacloud_tea_util import models as util_models


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
            'ap-northeast-1': 'linkvisual.aliyuncs.com',
            'ap-northeast-2-pop': 'linkvisual.aliyuncs.com',
            'ap-south-1': 'linkvisual.aliyuncs.com',
            'ap-southeast-1': 'linkvisual.aliyuncs.com',
            'ap-southeast-2': 'linkvisual.aliyuncs.com',
            'ap-southeast-3': 'linkvisual.aliyuncs.com',
            'ap-southeast-5': 'linkvisual.aliyuncs.com',
            'cn-beijing': 'linkvisual.aliyuncs.com',
            'cn-beijing-finance-1': 'linkvisual.aliyuncs.com',
            'cn-beijing-finance-pop': 'linkvisual.aliyuncs.com',
            'cn-beijing-gov-1': 'linkvisual.aliyuncs.com',
            'cn-beijing-nu16-b01': 'linkvisual.aliyuncs.com',
            'cn-chengdu': 'linkvisual.aliyuncs.com',
            'cn-edge-1': 'linkvisual.aliyuncs.com',
            'cn-fujian': 'linkvisual.aliyuncs.com',
            'cn-haidian-cm12-c01': 'linkvisual.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'linkvisual.aliyuncs.com',
            'cn-hangzhou-finance': 'linkvisual.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'linkvisual.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'linkvisual.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'linkvisual.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'linkvisual.aliyuncs.com',
            'cn-hangzhou-test-306': 'linkvisual.aliyuncs.com',
            'cn-hongkong': 'linkvisual.aliyuncs.com',
            'cn-hongkong-finance-pop': 'linkvisual.aliyuncs.com',
            'cn-huhehaote': 'linkvisual.aliyuncs.com',
            'cn-north-2-gov-1': 'linkvisual.aliyuncs.com',
            'cn-qingdao': 'linkvisual.aliyuncs.com',
            'cn-qingdao-nebula': 'linkvisual.aliyuncs.com',
            'cn-shanghai-et15-b01': 'linkvisual.aliyuncs.com',
            'cn-shanghai-et2-b01': 'linkvisual.aliyuncs.com',
            'cn-shanghai-finance-1': 'linkvisual.aliyuncs.com',
            'cn-shanghai-inner': 'linkvisual.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'linkvisual.aliyuncs.com',
            'cn-shenzhen': 'linkvisual.aliyuncs.com',
            'cn-shenzhen-finance-1': 'linkvisual.aliyuncs.com',
            'cn-shenzhen-inner': 'linkvisual.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'linkvisual.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'linkvisual.aliyuncs.com',
            'cn-wuhan': 'linkvisual.aliyuncs.com',
            'cn-yushanfang': 'linkvisual.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'linkvisual.aliyuncs.com',
            'cn-zhangjiakou': 'linkvisual.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'linkvisual.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'linkvisual.aliyuncs.com',
            'eu-central-1': 'linkvisual.aliyuncs.com',
            'eu-west-1': 'linkvisual.aliyuncs.com',
            'eu-west-1-oxs': 'linkvisual.aliyuncs.com',
            'me-east-1': 'linkvisual.aliyuncs.com',
            'rus-west-1-pop': 'linkvisual.aliyuncs.com',
            'us-east-1': 'linkvisual.aliyuncs.com',
            'us-west-1': 'linkvisual.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('linkvisual', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_event_record_plan_device_with_options(
        self,
        request: linkvisual_20180120_models.AddEventRecordPlanDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddEventRecordPlanDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.AddEventRecordPlanDeviceResponse().from_map(
            self.do_rpcrequest('AddEventRecordPlanDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_event_record_plan_device_with_options_async(
        self,
        request: linkvisual_20180120_models.AddEventRecordPlanDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddEventRecordPlanDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.AddEventRecordPlanDeviceResponse().from_map(
            await self.do_rpcrequest_async('AddEventRecordPlanDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_event_record_plan_device(
        self,
        request: linkvisual_20180120_models.AddEventRecordPlanDeviceRequest,
    ) -> linkvisual_20180120_models.AddEventRecordPlanDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_event_record_plan_device_with_options(request, runtime)

    async def add_event_record_plan_device_async(
        self,
        request: linkvisual_20180120_models.AddEventRecordPlanDeviceRequest,
    ) -> linkvisual_20180120_models.AddEventRecordPlanDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_event_record_plan_device_with_options_async(request, runtime)

    def add_face_device_group_with_options(
        self,
        request: linkvisual_20180120_models.AddFaceDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddFaceDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.AddFaceDeviceGroupResponse().from_map(
            self.do_rpcrequest('AddFaceDeviceGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_face_device_group_with_options_async(
        self,
        request: linkvisual_20180120_models.AddFaceDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddFaceDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.AddFaceDeviceGroupResponse().from_map(
            await self.do_rpcrequest_async('AddFaceDeviceGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_face_device_group(
        self,
        request: linkvisual_20180120_models.AddFaceDeviceGroupRequest,
    ) -> linkvisual_20180120_models.AddFaceDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_face_device_group_with_options(request, runtime)

    async def add_face_device_group_async(
        self,
        request: linkvisual_20180120_models.AddFaceDeviceGroupRequest,
    ) -> linkvisual_20180120_models.AddFaceDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_face_device_group_with_options_async(request, runtime)

    def add_face_device_to_device_group_with_options(
        self,
        request: linkvisual_20180120_models.AddFaceDeviceToDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddFaceDeviceToDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.AddFaceDeviceToDeviceGroupResponse().from_map(
            self.do_rpcrequest('AddFaceDeviceToDeviceGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_face_device_to_device_group_with_options_async(
        self,
        request: linkvisual_20180120_models.AddFaceDeviceToDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddFaceDeviceToDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.AddFaceDeviceToDeviceGroupResponse().from_map(
            await self.do_rpcrequest_async('AddFaceDeviceToDeviceGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_face_device_to_device_group(
        self,
        request: linkvisual_20180120_models.AddFaceDeviceToDeviceGroupRequest,
    ) -> linkvisual_20180120_models.AddFaceDeviceToDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_face_device_to_device_group_with_options(request, runtime)

    async def add_face_device_to_device_group_async(
        self,
        request: linkvisual_20180120_models.AddFaceDeviceToDeviceGroupRequest,
    ) -> linkvisual_20180120_models.AddFaceDeviceToDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_face_device_to_device_group_with_options_async(request, runtime)

    def add_face_user_with_options(
        self,
        request: linkvisual_20180120_models.AddFaceUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddFaceUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.AddFaceUserResponse().from_map(
            self.do_rpcrequest('AddFaceUser', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_face_user_with_options_async(
        self,
        request: linkvisual_20180120_models.AddFaceUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddFaceUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.AddFaceUserResponse().from_map(
            await self.do_rpcrequest_async('AddFaceUser', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_face_user(
        self,
        request: linkvisual_20180120_models.AddFaceUserRequest,
    ) -> linkvisual_20180120_models.AddFaceUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_face_user_with_options(request, runtime)

    async def add_face_user_async(
        self,
        request: linkvisual_20180120_models.AddFaceUserRequest,
    ) -> linkvisual_20180120_models.AddFaceUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_face_user_with_options_async(request, runtime)

    def add_face_user_group_with_options(
        self,
        request: linkvisual_20180120_models.AddFaceUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddFaceUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.AddFaceUserGroupResponse().from_map(
            self.do_rpcrequest('AddFaceUserGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_face_user_group_with_options_async(
        self,
        request: linkvisual_20180120_models.AddFaceUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddFaceUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.AddFaceUserGroupResponse().from_map(
            await self.do_rpcrequest_async('AddFaceUserGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_face_user_group(
        self,
        request: linkvisual_20180120_models.AddFaceUserGroupRequest,
    ) -> linkvisual_20180120_models.AddFaceUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_face_user_group_with_options(request, runtime)

    async def add_face_user_group_async(
        self,
        request: linkvisual_20180120_models.AddFaceUserGroupRequest,
    ) -> linkvisual_20180120_models.AddFaceUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_face_user_group_with_options_async(request, runtime)

    def add_face_user_group_and_device_group_relation_with_options(
        self,
        request: linkvisual_20180120_models.AddFaceUserGroupAndDeviceGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddFaceUserGroupAndDeviceGroupRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.AddFaceUserGroupAndDeviceGroupRelationResponse().from_map(
            self.do_rpcrequest('AddFaceUserGroupAndDeviceGroupRelation', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_face_user_group_and_device_group_relation_with_options_async(
        self,
        request: linkvisual_20180120_models.AddFaceUserGroupAndDeviceGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddFaceUserGroupAndDeviceGroupRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.AddFaceUserGroupAndDeviceGroupRelationResponse().from_map(
            await self.do_rpcrequest_async('AddFaceUserGroupAndDeviceGroupRelation', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_face_user_group_and_device_group_relation(
        self,
        request: linkvisual_20180120_models.AddFaceUserGroupAndDeviceGroupRelationRequest,
    ) -> linkvisual_20180120_models.AddFaceUserGroupAndDeviceGroupRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_face_user_group_and_device_group_relation_with_options(request, runtime)

    async def add_face_user_group_and_device_group_relation_async(
        self,
        request: linkvisual_20180120_models.AddFaceUserGroupAndDeviceGroupRelationRequest,
    ) -> linkvisual_20180120_models.AddFaceUserGroupAndDeviceGroupRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_face_user_group_and_device_group_relation_with_options_async(request, runtime)

    def add_face_user_picture_with_options(
        self,
        request: linkvisual_20180120_models.AddFaceUserPictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddFaceUserPictureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.AddFaceUserPictureResponse().from_map(
            self.do_rpcrequest('AddFaceUserPicture', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_face_user_picture_with_options_async(
        self,
        request: linkvisual_20180120_models.AddFaceUserPictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddFaceUserPictureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.AddFaceUserPictureResponse().from_map(
            await self.do_rpcrequest_async('AddFaceUserPicture', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_face_user_picture(
        self,
        request: linkvisual_20180120_models.AddFaceUserPictureRequest,
    ) -> linkvisual_20180120_models.AddFaceUserPictureResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_face_user_picture_with_options(request, runtime)

    async def add_face_user_picture_async(
        self,
        request: linkvisual_20180120_models.AddFaceUserPictureRequest,
    ) -> linkvisual_20180120_models.AddFaceUserPictureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_face_user_picture_with_options_async(request, runtime)

    def add_face_user_to_user_group_with_options(
        self,
        request: linkvisual_20180120_models.AddFaceUserToUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddFaceUserToUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.AddFaceUserToUserGroupResponse().from_map(
            self.do_rpcrequest('AddFaceUserToUserGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_face_user_to_user_group_with_options_async(
        self,
        request: linkvisual_20180120_models.AddFaceUserToUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddFaceUserToUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.AddFaceUserToUserGroupResponse().from_map(
            await self.do_rpcrequest_async('AddFaceUserToUserGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_face_user_to_user_group(
        self,
        request: linkvisual_20180120_models.AddFaceUserToUserGroupRequest,
    ) -> linkvisual_20180120_models.AddFaceUserToUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_face_user_to_user_group_with_options(request, runtime)

    async def add_face_user_to_user_group_async(
        self,
        request: linkvisual_20180120_models.AddFaceUserToUserGroupRequest,
    ) -> linkvisual_20180120_models.AddFaceUserToUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_face_user_to_user_group_with_options_async(request, runtime)

    def add_record_plan_device_with_options(
        self,
        request: linkvisual_20180120_models.AddRecordPlanDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddRecordPlanDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.AddRecordPlanDeviceResponse().from_map(
            self.do_rpcrequest('AddRecordPlanDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_record_plan_device_with_options_async(
        self,
        request: linkvisual_20180120_models.AddRecordPlanDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddRecordPlanDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.AddRecordPlanDeviceResponse().from_map(
            await self.do_rpcrequest_async('AddRecordPlanDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_record_plan_device(
        self,
        request: linkvisual_20180120_models.AddRecordPlanDeviceRequest,
    ) -> linkvisual_20180120_models.AddRecordPlanDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_record_plan_device_with_options(request, runtime)

    async def add_record_plan_device_async(
        self,
        request: linkvisual_20180120_models.AddRecordPlanDeviceRequest,
    ) -> linkvisual_20180120_models.AddRecordPlanDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_record_plan_device_with_options_async(request, runtime)

    def bind_aiplan_with_devices_with_options(
        self,
        request: linkvisual_20180120_models.BindAIPlanWithDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.BindAIPlanWithDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.BindAIPlanWithDevicesResponse().from_map(
            self.do_rpcrequest('BindAIPlanWithDevices', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_aiplan_with_devices_with_options_async(
        self,
        request: linkvisual_20180120_models.BindAIPlanWithDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.BindAIPlanWithDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.BindAIPlanWithDevicesResponse().from_map(
            await self.do_rpcrequest_async('BindAIPlanWithDevices', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_aiplan_with_devices(
        self,
        request: linkvisual_20180120_models.BindAIPlanWithDevicesRequest,
    ) -> linkvisual_20180120_models.BindAIPlanWithDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_aiplan_with_devices_with_options(request, runtime)

    async def bind_aiplan_with_devices_async(
        self,
        request: linkvisual_20180120_models.BindAIPlanWithDevicesRequest,
    ) -> linkvisual_20180120_models.BindAIPlanWithDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_aiplan_with_devices_with_options_async(request, runtime)

    def bind_picture_search_app_with_devices_with_options(
        self,
        request: linkvisual_20180120_models.BindPictureSearchAppWithDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.BindPictureSearchAppWithDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.BindPictureSearchAppWithDevicesResponse().from_map(
            self.do_rpcrequest('BindPictureSearchAppWithDevices', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_picture_search_app_with_devices_with_options_async(
        self,
        request: linkvisual_20180120_models.BindPictureSearchAppWithDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.BindPictureSearchAppWithDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.BindPictureSearchAppWithDevicesResponse().from_map(
            await self.do_rpcrequest_async('BindPictureSearchAppWithDevices', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_picture_search_app_with_devices(
        self,
        request: linkvisual_20180120_models.BindPictureSearchAppWithDevicesRequest,
    ) -> linkvisual_20180120_models.BindPictureSearchAppWithDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_picture_search_app_with_devices_with_options(request, runtime)

    async def bind_picture_search_app_with_devices_async(
        self,
        request: linkvisual_20180120_models.BindPictureSearchAppWithDevicesRequest,
    ) -> linkvisual_20180120_models.BindPictureSearchAppWithDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_picture_search_app_with_devices_with_options_async(request, runtime)

    def check_face_user_do_exist_on_device_with_options(
        self,
        request: linkvisual_20180120_models.CheckFaceUserDoExistOnDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CheckFaceUserDoExistOnDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.CheckFaceUserDoExistOnDeviceResponse().from_map(
            self.do_rpcrequest('CheckFaceUserDoExistOnDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_face_user_do_exist_on_device_with_options_async(
        self,
        request: linkvisual_20180120_models.CheckFaceUserDoExistOnDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CheckFaceUserDoExistOnDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.CheckFaceUserDoExistOnDeviceResponse().from_map(
            await self.do_rpcrequest_async('CheckFaceUserDoExistOnDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_face_user_do_exist_on_device(
        self,
        request: linkvisual_20180120_models.CheckFaceUserDoExistOnDeviceRequest,
    ) -> linkvisual_20180120_models.CheckFaceUserDoExistOnDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_face_user_do_exist_on_device_with_options(request, runtime)

    async def check_face_user_do_exist_on_device_async(
        self,
        request: linkvisual_20180120_models.CheckFaceUserDoExistOnDeviceRequest,
    ) -> linkvisual_20180120_models.CheckFaceUserDoExistOnDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_face_user_do_exist_on_device_with_options_async(request, runtime)

    def clear_face_device_dbwith_options(
        self,
        request: linkvisual_20180120_models.ClearFaceDeviceDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.ClearFaceDeviceDBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.ClearFaceDeviceDBResponse().from_map(
            self.do_rpcrequest('ClearFaceDeviceDB', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def clear_face_device_dbwith_options_async(
        self,
        request: linkvisual_20180120_models.ClearFaceDeviceDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.ClearFaceDeviceDBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.ClearFaceDeviceDBResponse().from_map(
            await self.do_rpcrequest_async('ClearFaceDeviceDB', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clear_face_device_db(
        self,
        request: linkvisual_20180120_models.ClearFaceDeviceDBRequest,
    ) -> linkvisual_20180120_models.ClearFaceDeviceDBResponse:
        runtime = util_models.RuntimeOptions()
        return self.clear_face_device_dbwith_options(request, runtime)

    async def clear_face_device_db_async(
        self,
        request: linkvisual_20180120_models.ClearFaceDeviceDBRequest,
    ) -> linkvisual_20180120_models.ClearFaceDeviceDBResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clear_face_device_dbwith_options_async(request, runtime)

    def config_aiaction_with_options(
        self,
        request: linkvisual_20180120_models.ConfigAIActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.ConfigAIActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.ConfigAIActionResponse().from_map(
            self.do_rpcrequest('ConfigAIAction', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_aiaction_with_options_async(
        self,
        request: linkvisual_20180120_models.ConfigAIActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.ConfigAIActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.ConfigAIActionResponse().from_map(
            await self.do_rpcrequest_async('ConfigAIAction', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_aiaction(
        self,
        request: linkvisual_20180120_models.ConfigAIActionRequest,
    ) -> linkvisual_20180120_models.ConfigAIActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_aiaction_with_options(request, runtime)

    async def config_aiaction_async(
        self,
        request: linkvisual_20180120_models.ConfigAIActionRequest,
    ) -> linkvisual_20180120_models.ConfigAIActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_aiaction_with_options_async(request, runtime)

    def create_aiapp_with_options(
        self,
        request: linkvisual_20180120_models.CreateAIAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateAIAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.CreateAIAppResponse().from_map(
            self.do_rpcrequest('CreateAIApp', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_aiapp_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateAIAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateAIAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.CreateAIAppResponse().from_map(
            await self.do_rpcrequest_async('CreateAIApp', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_aiapp(
        self,
        request: linkvisual_20180120_models.CreateAIAppRequest,
    ) -> linkvisual_20180120_models.CreateAIAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_aiapp_with_options(request, runtime)

    async def create_aiapp_async(
        self,
        request: linkvisual_20180120_models.CreateAIAppRequest,
    ) -> linkvisual_20180120_models.CreateAIAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_aiapp_with_options_async(request, runtime)

    def create_aiplan_with_options(
        self,
        request: linkvisual_20180120_models.CreateAIPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateAIPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.CreateAIPlanResponse().from_map(
            self.do_rpcrequest('CreateAIPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_aiplan_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateAIPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateAIPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.CreateAIPlanResponse().from_map(
            await self.do_rpcrequest_async('CreateAIPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_aiplan(
        self,
        request: linkvisual_20180120_models.CreateAIPlanRequest,
    ) -> linkvisual_20180120_models.CreateAIPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_aiplan_with_options(request, runtime)

    async def create_aiplan_async(
        self,
        request: linkvisual_20180120_models.CreateAIPlanRequest,
    ) -> linkvisual_20180120_models.CreateAIPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_aiplan_with_options_async(request, runtime)

    def create_algorithm_with_options(
        self,
        request: linkvisual_20180120_models.CreateAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.CreateAlgorithmResponse().from_map(
            self.do_rpcrequest('CreateAlgorithm', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_algorithm_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.CreateAlgorithmResponse().from_map(
            await self.do_rpcrequest_async('CreateAlgorithm', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_algorithm(
        self,
        request: linkvisual_20180120_models.CreateAlgorithmRequest,
    ) -> linkvisual_20180120_models.CreateAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_algorithm_with_options(request, runtime)

    async def create_algorithm_async(
        self,
        request: linkvisual_20180120_models.CreateAlgorithmRequest,
    ) -> linkvisual_20180120_models.CreateAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_algorithm_with_options_async(request, runtime)

    def create_device_purify_job_with_options(
        self,
        request: linkvisual_20180120_models.CreateDevicePurifyJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateDevicePurifyJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.CreateDevicePurifyJobResponse().from_map(
            self.do_rpcrequest('CreateDevicePurifyJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_device_purify_job_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateDevicePurifyJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateDevicePurifyJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.CreateDevicePurifyJobResponse().from_map(
            await self.do_rpcrequest_async('CreateDevicePurifyJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_device_purify_job(
        self,
        request: linkvisual_20180120_models.CreateDevicePurifyJobRequest,
    ) -> linkvisual_20180120_models.CreateDevicePurifyJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_device_purify_job_with_options(request, runtime)

    async def create_device_purify_job_async(
        self,
        request: linkvisual_20180120_models.CreateDevicePurifyJobRequest,
    ) -> linkvisual_20180120_models.CreateDevicePurifyJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_device_purify_job_with_options_async(request, runtime)

    def create_device_purify_job_by_plan_id_with_options(
        self,
        request: linkvisual_20180120_models.CreateDevicePurifyJobByPlanIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateDevicePurifyJobByPlanIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.CreateDevicePurifyJobByPlanIdResponse().from_map(
            self.do_rpcrequest('CreateDevicePurifyJobByPlanId', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_device_purify_job_by_plan_id_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateDevicePurifyJobByPlanIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateDevicePurifyJobByPlanIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.CreateDevicePurifyJobByPlanIdResponse().from_map(
            await self.do_rpcrequest_async('CreateDevicePurifyJobByPlanId', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_device_purify_job_by_plan_id(
        self,
        request: linkvisual_20180120_models.CreateDevicePurifyJobByPlanIdRequest,
    ) -> linkvisual_20180120_models.CreateDevicePurifyJobByPlanIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_device_purify_job_by_plan_id_with_options(request, runtime)

    async def create_device_purify_job_by_plan_id_async(
        self,
        request: linkvisual_20180120_models.CreateDevicePurifyJobByPlanIdRequest,
    ) -> linkvisual_20180120_models.CreateDevicePurifyJobByPlanIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_device_purify_job_by_plan_id_with_options_async(request, runtime)

    def create_device_purify_plan_with_options(
        self,
        request: linkvisual_20180120_models.CreateDevicePurifyPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateDevicePurifyPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.CreateDevicePurifyPlanResponse().from_map(
            self.do_rpcrequest('CreateDevicePurifyPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_device_purify_plan_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateDevicePurifyPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateDevicePurifyPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.CreateDevicePurifyPlanResponse().from_map(
            await self.do_rpcrequest_async('CreateDevicePurifyPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_device_purify_plan(
        self,
        request: linkvisual_20180120_models.CreateDevicePurifyPlanRequest,
    ) -> linkvisual_20180120_models.CreateDevicePurifyPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_device_purify_plan_with_options(request, runtime)

    async def create_device_purify_plan_async(
        self,
        request: linkvisual_20180120_models.CreateDevicePurifyPlanRequest,
    ) -> linkvisual_20180120_models.CreateDevicePurifyPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_device_purify_plan_with_options_async(request, runtime)

    def create_event_record_plan_with_options(
        self,
        request: linkvisual_20180120_models.CreateEventRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateEventRecordPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.CreateEventRecordPlanResponse().from_map(
            self.do_rpcrequest('CreateEventRecordPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_event_record_plan_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateEventRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateEventRecordPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.CreateEventRecordPlanResponse().from_map(
            await self.do_rpcrequest_async('CreateEventRecordPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_event_record_plan(
        self,
        request: linkvisual_20180120_models.CreateEventRecordPlanRequest,
    ) -> linkvisual_20180120_models.CreateEventRecordPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_event_record_plan_with_options(request, runtime)

    async def create_event_record_plan_async(
        self,
        request: linkvisual_20180120_models.CreateEventRecordPlanRequest,
    ) -> linkvisual_20180120_models.CreateEventRecordPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_event_record_plan_with_options_async(request, runtime)

    def create_model_with_options(
        self,
        request: linkvisual_20180120_models.CreateModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.CreateModelResponse().from_map(
            self.do_rpcrequest('CreateModel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_model_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.CreateModelResponse().from_map(
            await self.do_rpcrequest_async('CreateModel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_model(
        self,
        request: linkvisual_20180120_models.CreateModelRequest,
    ) -> linkvisual_20180120_models.CreateModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_model_with_options(request, runtime)

    async def create_model_async(
        self,
        request: linkvisual_20180120_models.CreateModelRequest,
    ) -> linkvisual_20180120_models.CreateModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_model_with_options_async(request, runtime)

    def create_picture_search_app_with_options(
        self,
        request: linkvisual_20180120_models.CreatePictureSearchAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreatePictureSearchAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.CreatePictureSearchAppResponse().from_map(
            self.do_rpcrequest('CreatePictureSearchApp', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_picture_search_app_with_options_async(
        self,
        request: linkvisual_20180120_models.CreatePictureSearchAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreatePictureSearchAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.CreatePictureSearchAppResponse().from_map(
            await self.do_rpcrequest_async('CreatePictureSearchApp', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_picture_search_app(
        self,
        request: linkvisual_20180120_models.CreatePictureSearchAppRequest,
    ) -> linkvisual_20180120_models.CreatePictureSearchAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_picture_search_app_with_options(request, runtime)

    async def create_picture_search_app_async(
        self,
        request: linkvisual_20180120_models.CreatePictureSearchAppRequest,
    ) -> linkvisual_20180120_models.CreatePictureSearchAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_picture_search_app_with_options_async(request, runtime)

    def create_record_plan_with_options(
        self,
        request: linkvisual_20180120_models.CreateRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateRecordPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.CreateRecordPlanResponse().from_map(
            self.do_rpcrequest('CreateRecordPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_record_plan_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateRecordPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.CreateRecordPlanResponse().from_map(
            await self.do_rpcrequest_async('CreateRecordPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_record_plan(
        self,
        request: linkvisual_20180120_models.CreateRecordPlanRequest,
    ) -> linkvisual_20180120_models.CreateRecordPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_record_plan_with_options(request, runtime)

    async def create_record_plan_async(
        self,
        request: linkvisual_20180120_models.CreateRecordPlanRequest,
    ) -> linkvisual_20180120_models.CreateRecordPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_record_plan_with_options_async(request, runtime)

    def create_time_template_with_options(
        self,
        request: linkvisual_20180120_models.CreateTimeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateTimeTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.CreateTimeTemplateResponse().from_map(
            self.do_rpcrequest('CreateTimeTemplate', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_time_template_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateTimeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateTimeTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.CreateTimeTemplateResponse().from_map(
            await self.do_rpcrequest_async('CreateTimeTemplate', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_time_template(
        self,
        request: linkvisual_20180120_models.CreateTimeTemplateRequest,
    ) -> linkvisual_20180120_models.CreateTimeTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_time_template_with_options(request, runtime)

    async def create_time_template_async(
        self,
        request: linkvisual_20180120_models.CreateTimeTemplateRequest,
    ) -> linkvisual_20180120_models.CreateTimeTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_time_template_with_options_async(request, runtime)

    def delete_algorithm_with_options(
        self,
        request: linkvisual_20180120_models.DeleteAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeleteAlgorithmResponse().from_map(
            self.do_rpcrequest('DeleteAlgorithm', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_algorithm_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeleteAlgorithmResponse().from_map(
            await self.do_rpcrequest_async('DeleteAlgorithm', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_algorithm(
        self,
        request: linkvisual_20180120_models.DeleteAlgorithmRequest,
    ) -> linkvisual_20180120_models.DeleteAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_algorithm_with_options(request, runtime)

    async def delete_algorithm_async(
        self,
        request: linkvisual_20180120_models.DeleteAlgorithmRequest,
    ) -> linkvisual_20180120_models.DeleteAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_algorithm_with_options_async(request, runtime)

    def delete_event_record_plan_with_options(
        self,
        request: linkvisual_20180120_models.DeleteEventRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteEventRecordPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeleteEventRecordPlanResponse().from_map(
            self.do_rpcrequest('DeleteEventRecordPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_event_record_plan_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteEventRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteEventRecordPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeleteEventRecordPlanResponse().from_map(
            await self.do_rpcrequest_async('DeleteEventRecordPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_event_record_plan(
        self,
        request: linkvisual_20180120_models.DeleteEventRecordPlanRequest,
    ) -> linkvisual_20180120_models.DeleteEventRecordPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_event_record_plan_with_options(request, runtime)

    async def delete_event_record_plan_async(
        self,
        request: linkvisual_20180120_models.DeleteEventRecordPlanRequest,
    ) -> linkvisual_20180120_models.DeleteEventRecordPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_event_record_plan_with_options_async(request, runtime)

    def delete_event_record_plan_device_with_options(
        self,
        request: linkvisual_20180120_models.DeleteEventRecordPlanDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteEventRecordPlanDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeleteEventRecordPlanDeviceResponse().from_map(
            self.do_rpcrequest('DeleteEventRecordPlanDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_event_record_plan_device_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteEventRecordPlanDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteEventRecordPlanDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeleteEventRecordPlanDeviceResponse().from_map(
            await self.do_rpcrequest_async('DeleteEventRecordPlanDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_event_record_plan_device(
        self,
        request: linkvisual_20180120_models.DeleteEventRecordPlanDeviceRequest,
    ) -> linkvisual_20180120_models.DeleteEventRecordPlanDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_event_record_plan_device_with_options(request, runtime)

    async def delete_event_record_plan_device_async(
        self,
        request: linkvisual_20180120_models.DeleteEventRecordPlanDeviceRequest,
    ) -> linkvisual_20180120_models.DeleteEventRecordPlanDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_event_record_plan_device_with_options_async(request, runtime)

    def delete_face_device_group_with_options(
        self,
        request: linkvisual_20180120_models.DeleteFaceDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteFaceDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeleteFaceDeviceGroupResponse().from_map(
            self.do_rpcrequest('DeleteFaceDeviceGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_face_device_group_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteFaceDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteFaceDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeleteFaceDeviceGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteFaceDeviceGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_face_device_group(
        self,
        request: linkvisual_20180120_models.DeleteFaceDeviceGroupRequest,
    ) -> linkvisual_20180120_models.DeleteFaceDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_face_device_group_with_options(request, runtime)

    async def delete_face_device_group_async(
        self,
        request: linkvisual_20180120_models.DeleteFaceDeviceGroupRequest,
    ) -> linkvisual_20180120_models.DeleteFaceDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_device_group_with_options_async(request, runtime)

    def delete_face_user_with_options(
        self,
        request: linkvisual_20180120_models.DeleteFaceUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteFaceUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeleteFaceUserResponse().from_map(
            self.do_rpcrequest('DeleteFaceUser', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_face_user_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteFaceUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteFaceUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeleteFaceUserResponse().from_map(
            await self.do_rpcrequest_async('DeleteFaceUser', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_face_user(
        self,
        request: linkvisual_20180120_models.DeleteFaceUserRequest,
    ) -> linkvisual_20180120_models.DeleteFaceUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_face_user_with_options(request, runtime)

    async def delete_face_user_async(
        self,
        request: linkvisual_20180120_models.DeleteFaceUserRequest,
    ) -> linkvisual_20180120_models.DeleteFaceUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_user_with_options_async(request, runtime)

    def delete_face_user_group_with_options(
        self,
        request: linkvisual_20180120_models.DeleteFaceUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteFaceUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeleteFaceUserGroupResponse().from_map(
            self.do_rpcrequest('DeleteFaceUserGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_face_user_group_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteFaceUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteFaceUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeleteFaceUserGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteFaceUserGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_face_user_group(
        self,
        request: linkvisual_20180120_models.DeleteFaceUserGroupRequest,
    ) -> linkvisual_20180120_models.DeleteFaceUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_face_user_group_with_options(request, runtime)

    async def delete_face_user_group_async(
        self,
        request: linkvisual_20180120_models.DeleteFaceUserGroupRequest,
    ) -> linkvisual_20180120_models.DeleteFaceUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_user_group_with_options_async(request, runtime)

    def delete_face_user_group_and_device_group_relation_with_options(
        self,
        request: linkvisual_20180120_models.DeleteFaceUserGroupAndDeviceGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteFaceUserGroupAndDeviceGroupRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeleteFaceUserGroupAndDeviceGroupRelationResponse().from_map(
            self.do_rpcrequest('DeleteFaceUserGroupAndDeviceGroupRelation', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_face_user_group_and_device_group_relation_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteFaceUserGroupAndDeviceGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteFaceUserGroupAndDeviceGroupRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeleteFaceUserGroupAndDeviceGroupRelationResponse().from_map(
            await self.do_rpcrequest_async('DeleteFaceUserGroupAndDeviceGroupRelation', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_face_user_group_and_device_group_relation(
        self,
        request: linkvisual_20180120_models.DeleteFaceUserGroupAndDeviceGroupRelationRequest,
    ) -> linkvisual_20180120_models.DeleteFaceUserGroupAndDeviceGroupRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_face_user_group_and_device_group_relation_with_options(request, runtime)

    async def delete_face_user_group_and_device_group_relation_async(
        self,
        request: linkvisual_20180120_models.DeleteFaceUserGroupAndDeviceGroupRelationRequest,
    ) -> linkvisual_20180120_models.DeleteFaceUserGroupAndDeviceGroupRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_user_group_and_device_group_relation_with_options_async(request, runtime)

    def delete_face_user_picture_with_options(
        self,
        request: linkvisual_20180120_models.DeleteFaceUserPictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteFaceUserPictureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeleteFaceUserPictureResponse().from_map(
            self.do_rpcrequest('DeleteFaceUserPicture', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_face_user_picture_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteFaceUserPictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteFaceUserPictureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeleteFaceUserPictureResponse().from_map(
            await self.do_rpcrequest_async('DeleteFaceUserPicture', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_face_user_picture(
        self,
        request: linkvisual_20180120_models.DeleteFaceUserPictureRequest,
    ) -> linkvisual_20180120_models.DeleteFaceUserPictureResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_face_user_picture_with_options(request, runtime)

    async def delete_face_user_picture_async(
        self,
        request: linkvisual_20180120_models.DeleteFaceUserPictureRequest,
    ) -> linkvisual_20180120_models.DeleteFaceUserPictureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_user_picture_with_options_async(request, runtime)

    def delete_model_with_options(
        self,
        request: linkvisual_20180120_models.DeleteModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeleteModelResponse().from_map(
            self.do_rpcrequest('DeleteModel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_model_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeleteModelResponse().from_map(
            await self.do_rpcrequest_async('DeleteModel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_model(
        self,
        request: linkvisual_20180120_models.DeleteModelRequest,
    ) -> linkvisual_20180120_models.DeleteModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_model_with_options(request, runtime)

    async def delete_model_async(
        self,
        request: linkvisual_20180120_models.DeleteModelRequest,
    ) -> linkvisual_20180120_models.DeleteModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_model_with_options_async(request, runtime)

    def delete_record_plan_with_options(
        self,
        request: linkvisual_20180120_models.DeleteRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteRecordPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeleteRecordPlanResponse().from_map(
            self.do_rpcrequest('DeleteRecordPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_record_plan_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteRecordPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeleteRecordPlanResponse().from_map(
            await self.do_rpcrequest_async('DeleteRecordPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_record_plan(
        self,
        request: linkvisual_20180120_models.DeleteRecordPlanRequest,
    ) -> linkvisual_20180120_models.DeleteRecordPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_record_plan_with_options(request, runtime)

    async def delete_record_plan_async(
        self,
        request: linkvisual_20180120_models.DeleteRecordPlanRequest,
    ) -> linkvisual_20180120_models.DeleteRecordPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_record_plan_with_options_async(request, runtime)

    def delete_record_plan_device_with_options(
        self,
        request: linkvisual_20180120_models.DeleteRecordPlanDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteRecordPlanDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeleteRecordPlanDeviceResponse().from_map(
            self.do_rpcrequest('DeleteRecordPlanDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_record_plan_device_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteRecordPlanDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteRecordPlanDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeleteRecordPlanDeviceResponse().from_map(
            await self.do_rpcrequest_async('DeleteRecordPlanDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_record_plan_device(
        self,
        request: linkvisual_20180120_models.DeleteRecordPlanDeviceRequest,
    ) -> linkvisual_20180120_models.DeleteRecordPlanDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_record_plan_device_with_options(request, runtime)

    async def delete_record_plan_device_async(
        self,
        request: linkvisual_20180120_models.DeleteRecordPlanDeviceRequest,
    ) -> linkvisual_20180120_models.DeleteRecordPlanDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_record_plan_device_with_options_async(request, runtime)

    def delete_time_template_with_options(
        self,
        request: linkvisual_20180120_models.DeleteTimeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteTimeTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeleteTimeTemplateResponse().from_map(
            self.do_rpcrequest('DeleteTimeTemplate', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_time_template_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteTimeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteTimeTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeleteTimeTemplateResponse().from_map(
            await self.do_rpcrequest_async('DeleteTimeTemplate', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_time_template(
        self,
        request: linkvisual_20180120_models.DeleteTimeTemplateRequest,
    ) -> linkvisual_20180120_models.DeleteTimeTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_time_template_with_options(request, runtime)

    async def delete_time_template_async(
        self,
        request: linkvisual_20180120_models.DeleteTimeTemplateRequest,
    ) -> linkvisual_20180120_models.DeleteTimeTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_time_template_with_options_async(request, runtime)

    def deploy_model_batch_with_options(
        self,
        request: linkvisual_20180120_models.DeployModelBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeployModelBatchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeployModelBatchResponse().from_map(
            self.do_rpcrequest('DeployModelBatch', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deploy_model_batch_with_options_async(
        self,
        request: linkvisual_20180120_models.DeployModelBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeployModelBatchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DeployModelBatchResponse().from_map(
            await self.do_rpcrequest_async('DeployModelBatch', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deploy_model_batch(
        self,
        request: linkvisual_20180120_models.DeployModelBatchRequest,
    ) -> linkvisual_20180120_models.DeployModelBatchResponse:
        runtime = util_models.RuntimeOptions()
        return self.deploy_model_batch_with_options(request, runtime)

    async def deploy_model_batch_async(
        self,
        request: linkvisual_20180120_models.DeployModelBatchRequest,
    ) -> linkvisual_20180120_models.DeployModelBatchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deploy_model_batch_with_options_async(request, runtime)

    def detect_user_face_by_url_with_options(
        self,
        request: linkvisual_20180120_models.DetectUserFaceByUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DetectUserFaceByUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DetectUserFaceByUrlResponse().from_map(
            self.do_rpcrequest('DetectUserFaceByUrl', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_user_face_by_url_with_options_async(
        self,
        request: linkvisual_20180120_models.DetectUserFaceByUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DetectUserFaceByUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.DetectUserFaceByUrlResponse().from_map(
            await self.do_rpcrequest_async('DetectUserFaceByUrl', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_user_face_by_url(
        self,
        request: linkvisual_20180120_models.DetectUserFaceByUrlRequest,
    ) -> linkvisual_20180120_models.DetectUserFaceByUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_user_face_by_url_with_options(request, runtime)

    async def detect_user_face_by_url_async(
        self,
        request: linkvisual_20180120_models.DetectUserFaceByUrlRequest,
    ) -> linkvisual_20180120_models.DetectUserFaceByUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_user_face_by_url_with_options_async(request, runtime)

    def get_aiaction_with_options(
        self,
        request: linkvisual_20180120_models.GetAIActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetAIActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetAIActionResponse().from_map(
            self.do_rpcrequest('GetAIAction', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_aiaction_with_options_async(
        self,
        request: linkvisual_20180120_models.GetAIActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetAIActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetAIActionResponse().from_map(
            await self.do_rpcrequest_async('GetAIAction', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_aiaction(
        self,
        request: linkvisual_20180120_models.GetAIActionRequest,
    ) -> linkvisual_20180120_models.GetAIActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aiaction_with_options(request, runtime)

    async def get_aiaction_async(
        self,
        request: linkvisual_20180120_models.GetAIActionRequest,
    ) -> linkvisual_20180120_models.GetAIActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aiaction_with_options_async(request, runtime)

    def get_aiaction_config_with_options(
        self,
        request: linkvisual_20180120_models.GetAIActionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetAIActionConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetAIActionConfigResponse().from_map(
            self.do_rpcrequest('GetAIActionConfig', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_aiaction_config_with_options_async(
        self,
        request: linkvisual_20180120_models.GetAIActionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetAIActionConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetAIActionConfigResponse().from_map(
            await self.do_rpcrequest_async('GetAIActionConfig', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_aiaction_config(
        self,
        request: linkvisual_20180120_models.GetAIActionConfigRequest,
    ) -> linkvisual_20180120_models.GetAIActionConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aiaction_config_with_options(request, runtime)

    async def get_aiaction_config_async(
        self,
        request: linkvisual_20180120_models.GetAIActionConfigRequest,
    ) -> linkvisual_20180120_models.GetAIActionConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aiaction_config_with_options_async(request, runtime)

    def get_aiapp_with_options(
        self,
        request: linkvisual_20180120_models.GetAIAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetAIAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetAIAppResponse().from_map(
            self.do_rpcrequest('GetAIApp', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_aiapp_with_options_async(
        self,
        request: linkvisual_20180120_models.GetAIAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetAIAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetAIAppResponse().from_map(
            await self.do_rpcrequest_async('GetAIApp', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_aiapp(
        self,
        request: linkvisual_20180120_models.GetAIAppRequest,
    ) -> linkvisual_20180120_models.GetAIAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aiapp_with_options(request, runtime)

    async def get_aiapp_async(
        self,
        request: linkvisual_20180120_models.GetAIAppRequest,
    ) -> linkvisual_20180120_models.GetAIAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aiapp_with_options_async(request, runtime)

    def get_aijob_with_options(
        self,
        request: linkvisual_20180120_models.GetAIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetAIJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetAIJobResponse().from_map(
            self.do_rpcrequest('GetAIJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_aijob_with_options_async(
        self,
        request: linkvisual_20180120_models.GetAIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetAIJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetAIJobResponse().from_map(
            await self.do_rpcrequest_async('GetAIJob', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_aijob(
        self,
        request: linkvisual_20180120_models.GetAIJobRequest,
    ) -> linkvisual_20180120_models.GetAIJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aijob_with_options(request, runtime)

    async def get_aijob_async(
        self,
        request: linkvisual_20180120_models.GetAIJobRequest,
    ) -> linkvisual_20180120_models.GetAIJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aijob_with_options_async(request, runtime)

    def get_aiplan_with_options(
        self,
        request: linkvisual_20180120_models.GetAIPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetAIPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetAIPlanResponse().from_map(
            self.do_rpcrequest('GetAIPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_aiplan_with_options_async(
        self,
        request: linkvisual_20180120_models.GetAIPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetAIPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetAIPlanResponse().from_map(
            await self.do_rpcrequest_async('GetAIPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_aiplan(
        self,
        request: linkvisual_20180120_models.GetAIPlanRequest,
    ) -> linkvisual_20180120_models.GetAIPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aiplan_with_options(request, runtime)

    async def get_aiplan_async(
        self,
        request: linkvisual_20180120_models.GetAIPlanRequest,
    ) -> linkvisual_20180120_models.GetAIPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aiplan_with_options_async(request, runtime)

    def get_algorithm_detail_by_id_with_options(
        self,
        request: linkvisual_20180120_models.GetAlgorithmDetailByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetAlgorithmDetailByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetAlgorithmDetailByIdResponse().from_map(
            self.do_rpcrequest('GetAlgorithmDetailById', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_algorithm_detail_by_id_with_options_async(
        self,
        request: linkvisual_20180120_models.GetAlgorithmDetailByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetAlgorithmDetailByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetAlgorithmDetailByIdResponse().from_map(
            await self.do_rpcrequest_async('GetAlgorithmDetailById', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_algorithm_detail_by_id(
        self,
        request: linkvisual_20180120_models.GetAlgorithmDetailByIdRequest,
    ) -> linkvisual_20180120_models.GetAlgorithmDetailByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_algorithm_detail_by_id_with_options(request, runtime)

    async def get_algorithm_detail_by_id_async(
        self,
        request: linkvisual_20180120_models.GetAlgorithmDetailByIdRequest,
    ) -> linkvisual_20180120_models.GetAlgorithmDetailByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_algorithm_detail_by_id_with_options_async(request, runtime)

    def get_algorithm_detail_by_name_with_options(
        self,
        request: linkvisual_20180120_models.GetAlgorithmDetailByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetAlgorithmDetailByNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetAlgorithmDetailByNameResponse().from_map(
            self.do_rpcrequest('GetAlgorithmDetailByName', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_algorithm_detail_by_name_with_options_async(
        self,
        request: linkvisual_20180120_models.GetAlgorithmDetailByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetAlgorithmDetailByNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetAlgorithmDetailByNameResponse().from_map(
            await self.do_rpcrequest_async('GetAlgorithmDetailByName', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_algorithm_detail_by_name(
        self,
        request: linkvisual_20180120_models.GetAlgorithmDetailByNameRequest,
    ) -> linkvisual_20180120_models.GetAlgorithmDetailByNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_algorithm_detail_by_name_with_options(request, runtime)

    async def get_algorithm_detail_by_name_async(
        self,
        request: linkvisual_20180120_models.GetAlgorithmDetailByNameRequest,
    ) -> linkvisual_20180120_models.GetAlgorithmDetailByNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_algorithm_detail_by_name_with_options_async(request, runtime)

    def get_device_purify_job_by_job_id_with_options(
        self,
        request: linkvisual_20180120_models.GetDevicePurifyJobByJobIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetDevicePurifyJobByJobIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetDevicePurifyJobByJobIdResponse().from_map(
            self.do_rpcrequest('GetDevicePurifyJobByJobId', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_device_purify_job_by_job_id_with_options_async(
        self,
        request: linkvisual_20180120_models.GetDevicePurifyJobByJobIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetDevicePurifyJobByJobIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetDevicePurifyJobByJobIdResponse().from_map(
            await self.do_rpcrequest_async('GetDevicePurifyJobByJobId', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_device_purify_job_by_job_id(
        self,
        request: linkvisual_20180120_models.GetDevicePurifyJobByJobIdRequest,
    ) -> linkvisual_20180120_models.GetDevicePurifyJobByJobIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_purify_job_by_job_id_with_options(request, runtime)

    async def get_device_purify_job_by_job_id_async(
        self,
        request: linkvisual_20180120_models.GetDevicePurifyJobByJobIdRequest,
    ) -> linkvisual_20180120_models.GetDevicePurifyJobByJobIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_purify_job_by_job_id_with_options_async(request, runtime)

    def get_model_detail_with_options(
        self,
        request: linkvisual_20180120_models.GetModelDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetModelDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetModelDetailResponse().from_map(
            self.do_rpcrequest('GetModelDetail', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_model_detail_with_options_async(
        self,
        request: linkvisual_20180120_models.GetModelDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetModelDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetModelDetailResponse().from_map(
            await self.do_rpcrequest_async('GetModelDetail', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_model_detail(
        self,
        request: linkvisual_20180120_models.GetModelDetailRequest,
    ) -> linkvisual_20180120_models.GetModelDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_model_detail_with_options(request, runtime)

    async def get_model_detail_async(
        self,
        request: linkvisual_20180120_models.GetModelDetailRequest,
    ) -> linkvisual_20180120_models.GetModelDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_model_detail_with_options_async(request, runtime)

    def get_model_detail_by_id_with_options(
        self,
        request: linkvisual_20180120_models.GetModelDetailByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetModelDetailByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetModelDetailByIdResponse().from_map(
            self.do_rpcrequest('GetModelDetailById', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_model_detail_by_id_with_options_async(
        self,
        request: linkvisual_20180120_models.GetModelDetailByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetModelDetailByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetModelDetailByIdResponse().from_map(
            await self.do_rpcrequest_async('GetModelDetailById', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_model_detail_by_id(
        self,
        request: linkvisual_20180120_models.GetModelDetailByIdRequest,
    ) -> linkvisual_20180120_models.GetModelDetailByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_model_detail_by_id_with_options(request, runtime)

    async def get_model_detail_by_id_async(
        self,
        request: linkvisual_20180120_models.GetModelDetailByIdRequest,
    ) -> linkvisual_20180120_models.GetModelDetailByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_model_detail_by_id_with_options_async(request, runtime)

    def get_model_oss_policy_with_options(
        self,
        request: linkvisual_20180120_models.GetModelOssPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetModelOssPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetModelOssPolicyResponse().from_map(
            self.do_rpcrequest('GetModelOssPolicy', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_model_oss_policy_with_options_async(
        self,
        request: linkvisual_20180120_models.GetModelOssPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetModelOssPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetModelOssPolicyResponse().from_map(
            await self.do_rpcrequest_async('GetModelOssPolicy', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_model_oss_policy(
        self,
        request: linkvisual_20180120_models.GetModelOssPolicyRequest,
    ) -> linkvisual_20180120_models.GetModelOssPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_model_oss_policy_with_options(request, runtime)

    async def get_model_oss_policy_async(
        self,
        request: linkvisual_20180120_models.GetModelOssPolicyRequest,
    ) -> linkvisual_20180120_models.GetModelOssPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_model_oss_policy_with_options_async(request, runtime)

    def get_picture_info_with_vector_ids_with_options(
        self,
        request: linkvisual_20180120_models.GetPictureInfoWithVectorIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetPictureInfoWithVectorIdsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetPictureInfoWithVectorIdsResponse().from_map(
            self.do_rpcrequest('GetPictureInfoWithVectorIds', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_picture_info_with_vector_ids_with_options_async(
        self,
        request: linkvisual_20180120_models.GetPictureInfoWithVectorIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetPictureInfoWithVectorIdsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetPictureInfoWithVectorIdsResponse().from_map(
            await self.do_rpcrequest_async('GetPictureInfoWithVectorIds', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_picture_info_with_vector_ids(
        self,
        request: linkvisual_20180120_models.GetPictureInfoWithVectorIdsRequest,
    ) -> linkvisual_20180120_models.GetPictureInfoWithVectorIdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_picture_info_with_vector_ids_with_options(request, runtime)

    async def get_picture_info_with_vector_ids_async(
        self,
        request: linkvisual_20180120_models.GetPictureInfoWithVectorIdsRequest,
    ) -> linkvisual_20180120_models.GetPictureInfoWithVectorIdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_picture_info_with_vector_ids_with_options_async(request, runtime)

    def get_picture_with_vector_id_with_options(
        self,
        request: linkvisual_20180120_models.GetPictureWithVectorIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetPictureWithVectorIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetPictureWithVectorIdResponse().from_map(
            self.do_rpcrequest('GetPictureWithVectorId', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_picture_with_vector_id_with_options_async(
        self,
        request: linkvisual_20180120_models.GetPictureWithVectorIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetPictureWithVectorIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.GetPictureWithVectorIdResponse().from_map(
            await self.do_rpcrequest_async('GetPictureWithVectorId', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_picture_with_vector_id(
        self,
        request: linkvisual_20180120_models.GetPictureWithVectorIdRequest,
    ) -> linkvisual_20180120_models.GetPictureWithVectorIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_picture_with_vector_id_with_options(request, runtime)

    async def get_picture_with_vector_id_async(
        self,
        request: linkvisual_20180120_models.GetPictureWithVectorIdRequest,
    ) -> linkvisual_20180120_models.GetPictureWithVectorIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_picture_with_vector_id_with_options_async(request, runtime)

    def list_algorithms_by_page_with_options(
        self,
        request: linkvisual_20180120_models.ListAlgorithmsByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.ListAlgorithmsByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.ListAlgorithmsByPageResponse().from_map(
            self.do_rpcrequest('ListAlgorithmsByPage', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_algorithms_by_page_with_options_async(
        self,
        request: linkvisual_20180120_models.ListAlgorithmsByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.ListAlgorithmsByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.ListAlgorithmsByPageResponse().from_map(
            await self.do_rpcrequest_async('ListAlgorithmsByPage', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_algorithms_by_page(
        self,
        request: linkvisual_20180120_models.ListAlgorithmsByPageRequest,
    ) -> linkvisual_20180120_models.ListAlgorithmsByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_algorithms_by_page_with_options(request, runtime)

    async def list_algorithms_by_page_async(
        self,
        request: linkvisual_20180120_models.ListAlgorithmsByPageRequest,
    ) -> linkvisual_20180120_models.ListAlgorithmsByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_algorithms_by_page_with_options_async(request, runtime)

    def list_deploy_task_by_model_id_and_devices_with_options(
        self,
        request: linkvisual_20180120_models.ListDeployTaskByModelIdAndDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.ListDeployTaskByModelIdAndDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.ListDeployTaskByModelIdAndDevicesResponse().from_map(
            self.do_rpcrequest('ListDeployTaskByModelIdAndDevices', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_deploy_task_by_model_id_and_devices_with_options_async(
        self,
        request: linkvisual_20180120_models.ListDeployTaskByModelIdAndDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.ListDeployTaskByModelIdAndDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.ListDeployTaskByModelIdAndDevicesResponse().from_map(
            await self.do_rpcrequest_async('ListDeployTaskByModelIdAndDevices', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_deploy_task_by_model_id_and_devices(
        self,
        request: linkvisual_20180120_models.ListDeployTaskByModelIdAndDevicesRequest,
    ) -> linkvisual_20180120_models.ListDeployTaskByModelIdAndDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_deploy_task_by_model_id_and_devices_with_options(request, runtime)

    async def list_deploy_task_by_model_id_and_devices_async(
        self,
        request: linkvisual_20180120_models.ListDeployTaskByModelIdAndDevicesRequest,
    ) -> linkvisual_20180120_models.ListDeployTaskByModelIdAndDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_deploy_task_by_model_id_and_devices_with_options_async(request, runtime)

    def list_deploy_task_by_page_with_options(
        self,
        request: linkvisual_20180120_models.ListDeployTaskByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.ListDeployTaskByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.ListDeployTaskByPageResponse().from_map(
            self.do_rpcrequest('ListDeployTaskByPage', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_deploy_task_by_page_with_options_async(
        self,
        request: linkvisual_20180120_models.ListDeployTaskByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.ListDeployTaskByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.ListDeployTaskByPageResponse().from_map(
            await self.do_rpcrequest_async('ListDeployTaskByPage', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_deploy_task_by_page(
        self,
        request: linkvisual_20180120_models.ListDeployTaskByPageRequest,
    ) -> linkvisual_20180120_models.ListDeployTaskByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_deploy_task_by_page_with_options(request, runtime)

    async def list_deploy_task_by_page_async(
        self,
        request: linkvisual_20180120_models.ListDeployTaskByPageRequest,
    ) -> linkvisual_20180120_models.ListDeployTaskByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_deploy_task_by_page_with_options_async(request, runtime)

    def list_models_by_page_with_options(
        self,
        request: linkvisual_20180120_models.ListModelsByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.ListModelsByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.ListModelsByPageResponse().from_map(
            self.do_rpcrequest('ListModelsByPage', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_models_by_page_with_options_async(
        self,
        request: linkvisual_20180120_models.ListModelsByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.ListModelsByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.ListModelsByPageResponse().from_map(
            await self.do_rpcrequest_async('ListModelsByPage', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_models_by_page(
        self,
        request: linkvisual_20180120_models.ListModelsByPageRequest,
    ) -> linkvisual_20180120_models.ListModelsByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_models_by_page_with_options(request, runtime)

    async def list_models_by_page_async(
        self,
        request: linkvisual_20180120_models.ListModelsByPageRequest,
    ) -> linkvisual_20180120_models.ListModelsByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_models_by_page_with_options_async(request, runtime)

    def list_model_versions_by_page_with_options(
        self,
        request: linkvisual_20180120_models.ListModelVersionsByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.ListModelVersionsByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.ListModelVersionsByPageResponse().from_map(
            self.do_rpcrequest('ListModelVersionsByPage', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_model_versions_by_page_with_options_async(
        self,
        request: linkvisual_20180120_models.ListModelVersionsByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.ListModelVersionsByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.ListModelVersionsByPageResponse().from_map(
            await self.do_rpcrequest_async('ListModelVersionsByPage', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_model_versions_by_page(
        self,
        request: linkvisual_20180120_models.ListModelVersionsByPageRequest,
    ) -> linkvisual_20180120_models.ListModelVersionsByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_model_versions_by_page_with_options(request, runtime)

    async def list_model_versions_by_page_async(
        self,
        request: linkvisual_20180120_models.ListModelVersionsByPageRequest,
    ) -> linkvisual_20180120_models.ListModelVersionsByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_model_versions_by_page_with_options_async(request, runtime)

    def picture_search_picture_with_options(
        self,
        request: linkvisual_20180120_models.PictureSearchPictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.PictureSearchPictureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.PictureSearchPictureResponse().from_map(
            self.do_rpcrequest('PictureSearchPicture', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def picture_search_picture_with_options_async(
        self,
        request: linkvisual_20180120_models.PictureSearchPictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.PictureSearchPictureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.PictureSearchPictureResponse().from_map(
            await self.do_rpcrequest_async('PictureSearchPicture', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def picture_search_picture(
        self,
        request: linkvisual_20180120_models.PictureSearchPictureRequest,
    ) -> linkvisual_20180120_models.PictureSearchPictureResponse:
        runtime = util_models.RuntimeOptions()
        return self.picture_search_picture_with_options(request, runtime)

    async def picture_search_picture_async(
        self,
        request: linkvisual_20180120_models.PictureSearchPictureRequest,
    ) -> linkvisual_20180120_models.PictureSearchPictureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.picture_search_picture_with_options_async(request, runtime)

    def query_aiaction_with_options(
        self,
        request: linkvisual_20180120_models.QueryAIActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryAIActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryAIActionResponse().from_map(
            self.do_rpcrequest('QueryAIAction', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_aiaction_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryAIActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryAIActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryAIActionResponse().from_map(
            await self.do_rpcrequest_async('QueryAIAction', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_aiaction(
        self,
        request: linkvisual_20180120_models.QueryAIActionRequest,
    ) -> linkvisual_20180120_models.QueryAIActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_aiaction_with_options(request, runtime)

    async def query_aiaction_async(
        self,
        request: linkvisual_20180120_models.QueryAIActionRequest,
    ) -> linkvisual_20180120_models.QueryAIActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_aiaction_with_options_async(request, runtime)

    def query_aiapp_with_options(
        self,
        request: linkvisual_20180120_models.QueryAIAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryAIAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryAIAppResponse().from_map(
            self.do_rpcrequest('QueryAIApp', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_aiapp_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryAIAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryAIAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryAIAppResponse().from_map(
            await self.do_rpcrequest_async('QueryAIApp', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_aiapp(
        self,
        request: linkvisual_20180120_models.QueryAIAppRequest,
    ) -> linkvisual_20180120_models.QueryAIAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_aiapp_with_options(request, runtime)

    async def query_aiapp_async(
        self,
        request: linkvisual_20180120_models.QueryAIAppRequest,
    ) -> linkvisual_20180120_models.QueryAIAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_aiapp_with_options_async(request, runtime)

    def query_aijobs_with_options(
        self,
        request: linkvisual_20180120_models.QueryAIJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryAIJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryAIJobsResponse().from_map(
            self.do_rpcrequest('QueryAIJobs', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_aijobs_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryAIJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryAIJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryAIJobsResponse().from_map(
            await self.do_rpcrequest_async('QueryAIJobs', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_aijobs(
        self,
        request: linkvisual_20180120_models.QueryAIJobsRequest,
    ) -> linkvisual_20180120_models.QueryAIJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_aijobs_with_options(request, runtime)

    async def query_aijobs_async(
        self,
        request: linkvisual_20180120_models.QueryAIJobsRequest,
    ) -> linkvisual_20180120_models.QueryAIJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_aijobs_with_options_async(request, runtime)

    def query_aiplan_with_options(
        self,
        request: linkvisual_20180120_models.QueryAIPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryAIPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryAIPlanResponse().from_map(
            self.do_rpcrequest('QueryAIPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_aiplan_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryAIPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryAIPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryAIPlanResponse().from_map(
            await self.do_rpcrequest_async('QueryAIPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_aiplan(
        self,
        request: linkvisual_20180120_models.QueryAIPlanRequest,
    ) -> linkvisual_20180120_models.QueryAIPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_aiplan_with_options(request, runtime)

    async def query_aiplan_async(
        self,
        request: linkvisual_20180120_models.QueryAIPlanRequest,
    ) -> linkvisual_20180120_models.QueryAIPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_aiplan_with_options_async(request, runtime)

    def query_aiplan_templates_with_options(
        self,
        request: linkvisual_20180120_models.QueryAIPlanTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryAIPlanTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryAIPlanTemplatesResponse().from_map(
            self.do_rpcrequest('QueryAIPlanTemplates', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_aiplan_templates_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryAIPlanTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryAIPlanTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryAIPlanTemplatesResponse().from_map(
            await self.do_rpcrequest_async('QueryAIPlanTemplates', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_aiplan_templates(
        self,
        request: linkvisual_20180120_models.QueryAIPlanTemplatesRequest,
    ) -> linkvisual_20180120_models.QueryAIPlanTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_aiplan_templates_with_options(request, runtime)

    async def query_aiplan_templates_async(
        self,
        request: linkvisual_20180120_models.QueryAIPlanTemplatesRequest,
    ) -> linkvisual_20180120_models.QueryAIPlanTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_aiplan_templates_with_options_async(request, runtime)

    def query_device_event_with_options(
        self,
        request: linkvisual_20180120_models.QueryDeviceEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDeviceEventResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryDeviceEventResponse().from_map(
            self.do_rpcrequest('QueryDeviceEvent', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_event_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryDeviceEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDeviceEventResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryDeviceEventResponse().from_map(
            await self.do_rpcrequest_async('QueryDeviceEvent', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_device_event(
        self,
        request: linkvisual_20180120_models.QueryDeviceEventRequest,
    ) -> linkvisual_20180120_models.QueryDeviceEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_event_with_options(request, runtime)

    async def query_device_event_async(
        self,
        request: linkvisual_20180120_models.QueryDeviceEventRequest,
    ) -> linkvisual_20180120_models.QueryDeviceEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_event_with_options_async(request, runtime)

    def query_device_event_picture_with_options(
        self,
        request: linkvisual_20180120_models.QueryDeviceEventPictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDeviceEventPictureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryDeviceEventPictureResponse().from_map(
            self.do_rpcrequest('QueryDeviceEventPicture', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_event_picture_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryDeviceEventPictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDeviceEventPictureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryDeviceEventPictureResponse().from_map(
            await self.do_rpcrequest_async('QueryDeviceEventPicture', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_device_event_picture(
        self,
        request: linkvisual_20180120_models.QueryDeviceEventPictureRequest,
    ) -> linkvisual_20180120_models.QueryDeviceEventPictureResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_event_picture_with_options(request, runtime)

    async def query_device_event_picture_async(
        self,
        request: linkvisual_20180120_models.QueryDeviceEventPictureRequest,
    ) -> linkvisual_20180120_models.QueryDeviceEventPictureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_event_picture_with_options_async(request, runtime)

    def query_device_event_record_with_options(
        self,
        request: linkvisual_20180120_models.QueryDeviceEventRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDeviceEventRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryDeviceEventRecordResponse().from_map(
            self.do_rpcrequest('QueryDeviceEventRecord', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_event_record_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryDeviceEventRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDeviceEventRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryDeviceEventRecordResponse().from_map(
            await self.do_rpcrequest_async('QueryDeviceEventRecord', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_device_event_record(
        self,
        request: linkvisual_20180120_models.QueryDeviceEventRecordRequest,
    ) -> linkvisual_20180120_models.QueryDeviceEventRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_event_record_with_options(request, runtime)

    async def query_device_event_record_async(
        self,
        request: linkvisual_20180120_models.QueryDeviceEventRecordRequest,
    ) -> linkvisual_20180120_models.QueryDeviceEventRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_event_record_with_options_async(request, runtime)

    def query_device_file_vod_with_options(
        self,
        request: linkvisual_20180120_models.QueryDeviceFileVodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDeviceFileVodResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryDeviceFileVodResponse().from_map(
            self.do_rpcrequest('QueryDeviceFileVod', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_file_vod_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryDeviceFileVodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDeviceFileVodResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryDeviceFileVodResponse().from_map(
            await self.do_rpcrequest_async('QueryDeviceFileVod', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_device_file_vod(
        self,
        request: linkvisual_20180120_models.QueryDeviceFileVodRequest,
    ) -> linkvisual_20180120_models.QueryDeviceFileVodResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_file_vod_with_options(request, runtime)

    async def query_device_file_vod_async(
        self,
        request: linkvisual_20180120_models.QueryDeviceFileVodRequest,
    ) -> linkvisual_20180120_models.QueryDeviceFileVodResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_file_vod_with_options_async(request, runtime)

    def query_device_picture_file_with_options(
        self,
        request: linkvisual_20180120_models.QueryDevicePictureFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDevicePictureFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryDevicePictureFileResponse().from_map(
            self.do_rpcrequest('QueryDevicePictureFile', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_picture_file_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryDevicePictureFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDevicePictureFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryDevicePictureFileResponse().from_map(
            await self.do_rpcrequest_async('QueryDevicePictureFile', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_device_picture_file(
        self,
        request: linkvisual_20180120_models.QueryDevicePictureFileRequest,
    ) -> linkvisual_20180120_models.QueryDevicePictureFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_picture_file_with_options(request, runtime)

    async def query_device_picture_file_async(
        self,
        request: linkvisual_20180120_models.QueryDevicePictureFileRequest,
    ) -> linkvisual_20180120_models.QueryDevicePictureFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_picture_file_with_options_async(request, runtime)

    def query_device_picture_life_cycle_with_options(
        self,
        request: linkvisual_20180120_models.QueryDevicePictureLifeCycleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDevicePictureLifeCycleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryDevicePictureLifeCycleResponse().from_map(
            self.do_rpcrequest('QueryDevicePictureLifeCycle', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_picture_life_cycle_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryDevicePictureLifeCycleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDevicePictureLifeCycleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryDevicePictureLifeCycleResponse().from_map(
            await self.do_rpcrequest_async('QueryDevicePictureLifeCycle', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_device_picture_life_cycle(
        self,
        request: linkvisual_20180120_models.QueryDevicePictureLifeCycleRequest,
    ) -> linkvisual_20180120_models.QueryDevicePictureLifeCycleResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_picture_life_cycle_with_options(request, runtime)

    async def query_device_picture_life_cycle_async(
        self,
        request: linkvisual_20180120_models.QueryDevicePictureLifeCycleRequest,
    ) -> linkvisual_20180120_models.QueryDevicePictureLifeCycleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_picture_life_cycle_with_options_async(request, runtime)

    def query_device_purify_jobs_with_options(
        self,
        request: linkvisual_20180120_models.QueryDevicePurifyJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDevicePurifyJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryDevicePurifyJobsResponse().from_map(
            self.do_rpcrequest('QueryDevicePurifyJobs', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_purify_jobs_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryDevicePurifyJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDevicePurifyJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryDevicePurifyJobsResponse().from_map(
            await self.do_rpcrequest_async('QueryDevicePurifyJobs', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_device_purify_jobs(
        self,
        request: linkvisual_20180120_models.QueryDevicePurifyJobsRequest,
    ) -> linkvisual_20180120_models.QueryDevicePurifyJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_purify_jobs_with_options(request, runtime)

    async def query_device_purify_jobs_async(
        self,
        request: linkvisual_20180120_models.QueryDevicePurifyJobsRequest,
    ) -> linkvisual_20180120_models.QueryDevicePurifyJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_purify_jobs_with_options_async(request, runtime)

    def query_device_purify_plan_by_plan_id_with_options(
        self,
        request: linkvisual_20180120_models.QueryDevicePurifyPlanByPlanIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDevicePurifyPlanByPlanIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryDevicePurifyPlanByPlanIdResponse().from_map(
            self.do_rpcrequest('QueryDevicePurifyPlanByPlanId', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_purify_plan_by_plan_id_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryDevicePurifyPlanByPlanIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDevicePurifyPlanByPlanIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryDevicePurifyPlanByPlanIdResponse().from_map(
            await self.do_rpcrequest_async('QueryDevicePurifyPlanByPlanId', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_device_purify_plan_by_plan_id(
        self,
        request: linkvisual_20180120_models.QueryDevicePurifyPlanByPlanIdRequest,
    ) -> linkvisual_20180120_models.QueryDevicePurifyPlanByPlanIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_purify_plan_by_plan_id_with_options(request, runtime)

    async def query_device_purify_plan_by_plan_id_async(
        self,
        request: linkvisual_20180120_models.QueryDevicePurifyPlanByPlanIdRequest,
    ) -> linkvisual_20180120_models.QueryDevicePurifyPlanByPlanIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_purify_plan_by_plan_id_with_options_async(request, runtime)

    def query_device_purify_plans_with_options(
        self,
        request: linkvisual_20180120_models.QueryDevicePurifyPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDevicePurifyPlansResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryDevicePurifyPlansResponse().from_map(
            self.do_rpcrequest('QueryDevicePurifyPlans', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_purify_plans_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryDevicePurifyPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDevicePurifyPlansResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryDevicePurifyPlansResponse().from_map(
            await self.do_rpcrequest_async('QueryDevicePurifyPlans', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_device_purify_plans(
        self,
        request: linkvisual_20180120_models.QueryDevicePurifyPlansRequest,
    ) -> linkvisual_20180120_models.QueryDevicePurifyPlansResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_purify_plans_with_options(request, runtime)

    async def query_device_purify_plans_async(
        self,
        request: linkvisual_20180120_models.QueryDevicePurifyPlansRequest,
    ) -> linkvisual_20180120_models.QueryDevicePurifyPlansResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_purify_plans_with_options_async(request, runtime)

    def query_device_record_life_cycle_with_options(
        self,
        request: linkvisual_20180120_models.QueryDeviceRecordLifeCycleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDeviceRecordLifeCycleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryDeviceRecordLifeCycleResponse().from_map(
            self.do_rpcrequest('QueryDeviceRecordLifeCycle', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_record_life_cycle_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryDeviceRecordLifeCycleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDeviceRecordLifeCycleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryDeviceRecordLifeCycleResponse().from_map(
            await self.do_rpcrequest_async('QueryDeviceRecordLifeCycle', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_device_record_life_cycle(
        self,
        request: linkvisual_20180120_models.QueryDeviceRecordLifeCycleRequest,
    ) -> linkvisual_20180120_models.QueryDeviceRecordLifeCycleResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_record_life_cycle_with_options(request, runtime)

    async def query_device_record_life_cycle_async(
        self,
        request: linkvisual_20180120_models.QueryDeviceRecordLifeCycleRequest,
    ) -> linkvisual_20180120_models.QueryDeviceRecordLifeCycleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_record_life_cycle_with_options_async(request, runtime)

    def query_device_vod_url_with_options(
        self,
        request: linkvisual_20180120_models.QueryDeviceVodUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDeviceVodUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryDeviceVodUrlResponse().from_map(
            self.do_rpcrequest('QueryDeviceVodUrl', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_device_vod_url_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryDeviceVodUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDeviceVodUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryDeviceVodUrlResponse().from_map(
            await self.do_rpcrequest_async('QueryDeviceVodUrl', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_device_vod_url(
        self,
        request: linkvisual_20180120_models.QueryDeviceVodUrlRequest,
    ) -> linkvisual_20180120_models.QueryDeviceVodUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_vod_url_with_options(request, runtime)

    async def query_device_vod_url_async(
        self,
        request: linkvisual_20180120_models.QueryDeviceVodUrlRequest,
    ) -> linkvisual_20180120_models.QueryDeviceVodUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_vod_url_with_options_async(request, runtime)

    def query_event_record_plan_detail_with_options(
        self,
        request: linkvisual_20180120_models.QueryEventRecordPlanDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryEventRecordPlanDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryEventRecordPlanDetailResponse().from_map(
            self.do_rpcrequest('QueryEventRecordPlanDetail', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_event_record_plan_detail_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryEventRecordPlanDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryEventRecordPlanDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryEventRecordPlanDetailResponse().from_map(
            await self.do_rpcrequest_async('QueryEventRecordPlanDetail', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_event_record_plan_detail(
        self,
        request: linkvisual_20180120_models.QueryEventRecordPlanDetailRequest,
    ) -> linkvisual_20180120_models.QueryEventRecordPlanDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_event_record_plan_detail_with_options(request, runtime)

    async def query_event_record_plan_detail_async(
        self,
        request: linkvisual_20180120_models.QueryEventRecordPlanDetailRequest,
    ) -> linkvisual_20180120_models.QueryEventRecordPlanDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_event_record_plan_detail_with_options_async(request, runtime)

    def query_event_record_plan_device_by_device_with_options(
        self,
        request: linkvisual_20180120_models.QueryEventRecordPlanDeviceByDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryEventRecordPlanDeviceByDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryEventRecordPlanDeviceByDeviceResponse().from_map(
            self.do_rpcrequest('QueryEventRecordPlanDeviceByDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_event_record_plan_device_by_device_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryEventRecordPlanDeviceByDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryEventRecordPlanDeviceByDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryEventRecordPlanDeviceByDeviceResponse().from_map(
            await self.do_rpcrequest_async('QueryEventRecordPlanDeviceByDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_event_record_plan_device_by_device(
        self,
        request: linkvisual_20180120_models.QueryEventRecordPlanDeviceByDeviceRequest,
    ) -> linkvisual_20180120_models.QueryEventRecordPlanDeviceByDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_event_record_plan_device_by_device_with_options(request, runtime)

    async def query_event_record_plan_device_by_device_async(
        self,
        request: linkvisual_20180120_models.QueryEventRecordPlanDeviceByDeviceRequest,
    ) -> linkvisual_20180120_models.QueryEventRecordPlanDeviceByDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_event_record_plan_device_by_device_with_options_async(request, runtime)

    def query_event_record_plan_device_by_plan_with_options(
        self,
        request: linkvisual_20180120_models.QueryEventRecordPlanDeviceByPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryEventRecordPlanDeviceByPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryEventRecordPlanDeviceByPlanResponse().from_map(
            self.do_rpcrequest('QueryEventRecordPlanDeviceByPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_event_record_plan_device_by_plan_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryEventRecordPlanDeviceByPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryEventRecordPlanDeviceByPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryEventRecordPlanDeviceByPlanResponse().from_map(
            await self.do_rpcrequest_async('QueryEventRecordPlanDeviceByPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_event_record_plan_device_by_plan(
        self,
        request: linkvisual_20180120_models.QueryEventRecordPlanDeviceByPlanRequest,
    ) -> linkvisual_20180120_models.QueryEventRecordPlanDeviceByPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_event_record_plan_device_by_plan_with_options(request, runtime)

    async def query_event_record_plan_device_by_plan_async(
        self,
        request: linkvisual_20180120_models.QueryEventRecordPlanDeviceByPlanRequest,
    ) -> linkvisual_20180120_models.QueryEventRecordPlanDeviceByPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_event_record_plan_device_by_plan_with_options_async(request, runtime)

    def query_event_record_plans_with_options(
        self,
        request: linkvisual_20180120_models.QueryEventRecordPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryEventRecordPlansResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryEventRecordPlansResponse().from_map(
            self.do_rpcrequest('QueryEventRecordPlans', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_event_record_plans_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryEventRecordPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryEventRecordPlansResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryEventRecordPlansResponse().from_map(
            await self.do_rpcrequest_async('QueryEventRecordPlans', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_event_record_plans(
        self,
        request: linkvisual_20180120_models.QueryEventRecordPlansRequest,
    ) -> linkvisual_20180120_models.QueryEventRecordPlansResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_event_record_plans_with_options(request, runtime)

    async def query_event_record_plans_async(
        self,
        request: linkvisual_20180120_models.QueryEventRecordPlansRequest,
    ) -> linkvisual_20180120_models.QueryEventRecordPlansResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_event_record_plans_with_options_async(request, runtime)

    def query_face_all_device_group_with_options(
        self,
        request: linkvisual_20180120_models.QueryFaceAllDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceAllDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryFaceAllDeviceGroupResponse().from_map(
            self.do_rpcrequest('QueryFaceAllDeviceGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_face_all_device_group_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryFaceAllDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceAllDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryFaceAllDeviceGroupResponse().from_map(
            await self.do_rpcrequest_async('QueryFaceAllDeviceGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_face_all_device_group(
        self,
        request: linkvisual_20180120_models.QueryFaceAllDeviceGroupRequest,
    ) -> linkvisual_20180120_models.QueryFaceAllDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_face_all_device_group_with_options(request, runtime)

    async def query_face_all_device_group_async(
        self,
        request: linkvisual_20180120_models.QueryFaceAllDeviceGroupRequest,
    ) -> linkvisual_20180120_models.QueryFaceAllDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_face_all_device_group_with_options_async(request, runtime)

    def query_face_all_user_group_with_options(
        self,
        request: linkvisual_20180120_models.QueryFaceAllUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceAllUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryFaceAllUserGroupResponse().from_map(
            self.do_rpcrequest('QueryFaceAllUserGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_face_all_user_group_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryFaceAllUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceAllUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryFaceAllUserGroupResponse().from_map(
            await self.do_rpcrequest_async('QueryFaceAllUserGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_face_all_user_group(
        self,
        request: linkvisual_20180120_models.QueryFaceAllUserGroupRequest,
    ) -> linkvisual_20180120_models.QueryFaceAllUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_face_all_user_group_with_options(request, runtime)

    async def query_face_all_user_group_async(
        self,
        request: linkvisual_20180120_models.QueryFaceAllUserGroupRequest,
    ) -> linkvisual_20180120_models.QueryFaceAllUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_face_all_user_group_with_options_async(request, runtime)

    def query_face_all_user_group_and_device_group_relation_with_options(
        self,
        request: linkvisual_20180120_models.QueryFaceAllUserGroupAndDeviceGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceAllUserGroupAndDeviceGroupRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryFaceAllUserGroupAndDeviceGroupRelationResponse().from_map(
            self.do_rpcrequest('QueryFaceAllUserGroupAndDeviceGroupRelation', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_face_all_user_group_and_device_group_relation_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryFaceAllUserGroupAndDeviceGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceAllUserGroupAndDeviceGroupRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryFaceAllUserGroupAndDeviceGroupRelationResponse().from_map(
            await self.do_rpcrequest_async('QueryFaceAllUserGroupAndDeviceGroupRelation', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_face_all_user_group_and_device_group_relation(
        self,
        request: linkvisual_20180120_models.QueryFaceAllUserGroupAndDeviceGroupRelationRequest,
    ) -> linkvisual_20180120_models.QueryFaceAllUserGroupAndDeviceGroupRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_face_all_user_group_and_device_group_relation_with_options(request, runtime)

    async def query_face_all_user_group_and_device_group_relation_async(
        self,
        request: linkvisual_20180120_models.QueryFaceAllUserGroupAndDeviceGroupRelationRequest,
    ) -> linkvisual_20180120_models.QueryFaceAllUserGroupAndDeviceGroupRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_face_all_user_group_and_device_group_relation_with_options_async(request, runtime)

    def query_face_all_user_ids_by_group_id_with_options(
        self,
        request: linkvisual_20180120_models.QueryFaceAllUserIdsByGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceAllUserIdsByGroupIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryFaceAllUserIdsByGroupIdResponse().from_map(
            self.do_rpcrequest('QueryFaceAllUserIdsByGroupId', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_face_all_user_ids_by_group_id_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryFaceAllUserIdsByGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceAllUserIdsByGroupIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryFaceAllUserIdsByGroupIdResponse().from_map(
            await self.do_rpcrequest_async('QueryFaceAllUserIdsByGroupId', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_face_all_user_ids_by_group_id(
        self,
        request: linkvisual_20180120_models.QueryFaceAllUserIdsByGroupIdRequest,
    ) -> linkvisual_20180120_models.QueryFaceAllUserIdsByGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_face_all_user_ids_by_group_id_with_options(request, runtime)

    async def query_face_all_user_ids_by_group_id_async(
        self,
        request: linkvisual_20180120_models.QueryFaceAllUserIdsByGroupIdRequest,
    ) -> linkvisual_20180120_models.QueryFaceAllUserIdsByGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_face_all_user_ids_by_group_id_with_options_async(request, runtime)

    def query_face_custom_user_id_by_user_id_with_options(
        self,
        request: linkvisual_20180120_models.QueryFaceCustomUserIdByUserIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceCustomUserIdByUserIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryFaceCustomUserIdByUserIdResponse().from_map(
            self.do_rpcrequest('QueryFaceCustomUserIdByUserId', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_face_custom_user_id_by_user_id_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryFaceCustomUserIdByUserIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceCustomUserIdByUserIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryFaceCustomUserIdByUserIdResponse().from_map(
            await self.do_rpcrequest_async('QueryFaceCustomUserIdByUserId', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_face_custom_user_id_by_user_id(
        self,
        request: linkvisual_20180120_models.QueryFaceCustomUserIdByUserIdRequest,
    ) -> linkvisual_20180120_models.QueryFaceCustomUserIdByUserIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_face_custom_user_id_by_user_id_with_options(request, runtime)

    async def query_face_custom_user_id_by_user_id_async(
        self,
        request: linkvisual_20180120_models.QueryFaceCustomUserIdByUserIdRequest,
    ) -> linkvisual_20180120_models.QueryFaceCustomUserIdByUserIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_face_custom_user_id_by_user_id_with_options_async(request, runtime)

    def query_face_device_groups_by_device_with_options(
        self,
        request: linkvisual_20180120_models.QueryFaceDeviceGroupsByDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceDeviceGroupsByDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryFaceDeviceGroupsByDeviceResponse().from_map(
            self.do_rpcrequest('QueryFaceDeviceGroupsByDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_face_device_groups_by_device_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryFaceDeviceGroupsByDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceDeviceGroupsByDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryFaceDeviceGroupsByDeviceResponse().from_map(
            await self.do_rpcrequest_async('QueryFaceDeviceGroupsByDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_face_device_groups_by_device(
        self,
        request: linkvisual_20180120_models.QueryFaceDeviceGroupsByDeviceRequest,
    ) -> linkvisual_20180120_models.QueryFaceDeviceGroupsByDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_face_device_groups_by_device_with_options(request, runtime)

    async def query_face_device_groups_by_device_async(
        self,
        request: linkvisual_20180120_models.QueryFaceDeviceGroupsByDeviceRequest,
    ) -> linkvisual_20180120_models.QueryFaceDeviceGroupsByDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_face_device_groups_by_device_with_options_async(request, runtime)

    def query_face_user_with_options(
        self,
        request: linkvisual_20180120_models.QueryFaceUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryFaceUserResponse().from_map(
            self.do_rpcrequest('QueryFaceUser', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_face_user_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryFaceUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryFaceUserResponse().from_map(
            await self.do_rpcrequest_async('QueryFaceUser', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_face_user(
        self,
        request: linkvisual_20180120_models.QueryFaceUserRequest,
    ) -> linkvisual_20180120_models.QueryFaceUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_face_user_with_options(request, runtime)

    async def query_face_user_async(
        self,
        request: linkvisual_20180120_models.QueryFaceUserRequest,
    ) -> linkvisual_20180120_models.QueryFaceUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_face_user_with_options_async(request, runtime)

    def query_face_user_group_with_options(
        self,
        request: linkvisual_20180120_models.QueryFaceUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryFaceUserGroupResponse().from_map(
            self.do_rpcrequest('QueryFaceUserGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_face_user_group_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryFaceUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryFaceUserGroupResponse().from_map(
            await self.do_rpcrequest_async('QueryFaceUserGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_face_user_group(
        self,
        request: linkvisual_20180120_models.QueryFaceUserGroupRequest,
    ) -> linkvisual_20180120_models.QueryFaceUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_face_user_group_with_options(request, runtime)

    async def query_face_user_group_async(
        self,
        request: linkvisual_20180120_models.QueryFaceUserGroupRequest,
    ) -> linkvisual_20180120_models.QueryFaceUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_face_user_group_with_options_async(request, runtime)

    def query_face_user_group_and_device_group_relation_with_options(
        self,
        request: linkvisual_20180120_models.QueryFaceUserGroupAndDeviceGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceUserGroupAndDeviceGroupRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryFaceUserGroupAndDeviceGroupRelationResponse().from_map(
            self.do_rpcrequest('QueryFaceUserGroupAndDeviceGroupRelation', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_face_user_group_and_device_group_relation_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryFaceUserGroupAndDeviceGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceUserGroupAndDeviceGroupRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryFaceUserGroupAndDeviceGroupRelationResponse().from_map(
            await self.do_rpcrequest_async('QueryFaceUserGroupAndDeviceGroupRelation', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_face_user_group_and_device_group_relation(
        self,
        request: linkvisual_20180120_models.QueryFaceUserGroupAndDeviceGroupRelationRequest,
    ) -> linkvisual_20180120_models.QueryFaceUserGroupAndDeviceGroupRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_face_user_group_and_device_group_relation_with_options(request, runtime)

    async def query_face_user_group_and_device_group_relation_async(
        self,
        request: linkvisual_20180120_models.QueryFaceUserGroupAndDeviceGroupRelationRequest,
    ) -> linkvisual_20180120_models.QueryFaceUserGroupAndDeviceGroupRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_face_user_group_and_device_group_relation_with_options_async(request, runtime)

    def query_face_user_id_by_custom_user_id_with_options(
        self,
        request: linkvisual_20180120_models.QueryFaceUserIdByCustomUserIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceUserIdByCustomUserIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryFaceUserIdByCustomUserIdResponse().from_map(
            self.do_rpcrequest('QueryFaceUserIdByCustomUserId', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_face_user_id_by_custom_user_id_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryFaceUserIdByCustomUserIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceUserIdByCustomUserIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryFaceUserIdByCustomUserIdResponse().from_map(
            await self.do_rpcrequest_async('QueryFaceUserIdByCustomUserId', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_face_user_id_by_custom_user_id(
        self,
        request: linkvisual_20180120_models.QueryFaceUserIdByCustomUserIdRequest,
    ) -> linkvisual_20180120_models.QueryFaceUserIdByCustomUserIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_face_user_id_by_custom_user_id_with_options(request, runtime)

    async def query_face_user_id_by_custom_user_id_async(
        self,
        request: linkvisual_20180120_models.QueryFaceUserIdByCustomUserIdRequest,
    ) -> linkvisual_20180120_models.QueryFaceUserIdByCustomUserIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_face_user_id_by_custom_user_id_with_options_async(request, runtime)

    def query_iot_ids_by_aiplan_with_options(
        self,
        request: linkvisual_20180120_models.QueryIotIdsByAIPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryIotIdsByAIPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryIotIdsByAIPlanResponse().from_map(
            self.do_rpcrequest('QueryIotIdsByAIPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_iot_ids_by_aiplan_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryIotIdsByAIPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryIotIdsByAIPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryIotIdsByAIPlanResponse().from_map(
            await self.do_rpcrequest_async('QueryIotIdsByAIPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_iot_ids_by_aiplan(
        self,
        request: linkvisual_20180120_models.QueryIotIdsByAIPlanRequest,
    ) -> linkvisual_20180120_models.QueryIotIdsByAIPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_iot_ids_by_aiplan_with_options(request, runtime)

    async def query_iot_ids_by_aiplan_async(
        self,
        request: linkvisual_20180120_models.QueryIotIdsByAIPlanRequest,
    ) -> linkvisual_20180120_models.QueryIotIdsByAIPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_iot_ids_by_aiplan_with_options_async(request, runtime)

    def query_live_streaming_with_options(
        self,
        request: linkvisual_20180120_models.QueryLiveStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryLiveStreamingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryLiveStreamingResponse().from_map(
            self.do_rpcrequest('QueryLiveStreaming', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_live_streaming_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryLiveStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryLiveStreamingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryLiveStreamingResponse().from_map(
            await self.do_rpcrequest_async('QueryLiveStreaming', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_live_streaming(
        self,
        request: linkvisual_20180120_models.QueryLiveStreamingRequest,
    ) -> linkvisual_20180120_models.QueryLiveStreamingResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_live_streaming_with_options(request, runtime)

    async def query_live_streaming_async(
        self,
        request: linkvisual_20180120_models.QueryLiveStreamingRequest,
    ) -> linkvisual_20180120_models.QueryLiveStreamingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_live_streaming_with_options_async(request, runtime)

    def query_month_record_with_options(
        self,
        request: linkvisual_20180120_models.QueryMonthRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryMonthRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryMonthRecordResponse().from_map(
            self.do_rpcrequest('QueryMonthRecord', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_month_record_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryMonthRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryMonthRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryMonthRecordResponse().from_map(
            await self.do_rpcrequest_async('QueryMonthRecord', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_month_record(
        self,
        request: linkvisual_20180120_models.QueryMonthRecordRequest,
    ) -> linkvisual_20180120_models.QueryMonthRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_month_record_with_options(request, runtime)

    async def query_month_record_async(
        self,
        request: linkvisual_20180120_models.QueryMonthRecordRequest,
    ) -> linkvisual_20180120_models.QueryMonthRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_month_record_with_options_async(request, runtime)

    def query_picture_files_with_options(
        self,
        request: linkvisual_20180120_models.QueryPictureFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryPictureFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryPictureFilesResponse().from_map(
            self.do_rpcrequest('QueryPictureFiles', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_picture_files_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryPictureFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryPictureFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryPictureFilesResponse().from_map(
            await self.do_rpcrequest_async('QueryPictureFiles', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_picture_files(
        self,
        request: linkvisual_20180120_models.QueryPictureFilesRequest,
    ) -> linkvisual_20180120_models.QueryPictureFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_picture_files_with_options(request, runtime)

    async def query_picture_files_async(
        self,
        request: linkvisual_20180120_models.QueryPictureFilesRequest,
    ) -> linkvisual_20180120_models.QueryPictureFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_picture_files_with_options_async(request, runtime)

    def query_picture_search_aiboxes_with_options(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchAiboxesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryPictureSearchAiboxesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryPictureSearchAiboxesResponse().from_map(
            self.do_rpcrequest('QueryPictureSearchAiboxes', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_picture_search_aiboxes_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchAiboxesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryPictureSearchAiboxesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryPictureSearchAiboxesResponse().from_map(
            await self.do_rpcrequest_async('QueryPictureSearchAiboxes', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_picture_search_aiboxes(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchAiboxesRequest,
    ) -> linkvisual_20180120_models.QueryPictureSearchAiboxesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_picture_search_aiboxes_with_options(request, runtime)

    async def query_picture_search_aiboxes_async(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchAiboxesRequest,
    ) -> linkvisual_20180120_models.QueryPictureSearchAiboxesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_picture_search_aiboxes_with_options_async(request, runtime)

    def query_picture_search_app_with_options(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryPictureSearchAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryPictureSearchAppResponse().from_map(
            self.do_rpcrequest('QueryPictureSearchApp', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_picture_search_app_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryPictureSearchAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryPictureSearchAppResponse().from_map(
            await self.do_rpcrequest_async('QueryPictureSearchApp', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_picture_search_app(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchAppRequest,
    ) -> linkvisual_20180120_models.QueryPictureSearchAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_picture_search_app_with_options(request, runtime)

    async def query_picture_search_app_async(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchAppRequest,
    ) -> linkvisual_20180120_models.QueryPictureSearchAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_picture_search_app_with_options_async(request, runtime)

    def query_picture_search_devices_with_options(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryPictureSearchDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryPictureSearchDevicesResponse().from_map(
            self.do_rpcrequest('QueryPictureSearchDevices', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_picture_search_devices_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryPictureSearchDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryPictureSearchDevicesResponse().from_map(
            await self.do_rpcrequest_async('QueryPictureSearchDevices', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_picture_search_devices(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchDevicesRequest,
    ) -> linkvisual_20180120_models.QueryPictureSearchDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_picture_search_devices_with_options(request, runtime)

    async def query_picture_search_devices_async(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchDevicesRequest,
    ) -> linkvisual_20180120_models.QueryPictureSearchDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_picture_search_devices_with_options_async(request, runtime)

    def query_record_with_options(
        self,
        request: linkvisual_20180120_models.QueryRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryRecordResponse().from_map(
            self.do_rpcrequest('QueryRecord', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_record_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryRecordResponse().from_map(
            await self.do_rpcrequest_async('QueryRecord', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_record(
        self,
        request: linkvisual_20180120_models.QueryRecordRequest,
    ) -> linkvisual_20180120_models.QueryRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_record_with_options(request, runtime)

    async def query_record_async(
        self,
        request: linkvisual_20180120_models.QueryRecordRequest,
    ) -> linkvisual_20180120_models.QueryRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_record_with_options_async(request, runtime)

    def query_record_by_record_id_with_options(
        self,
        request: linkvisual_20180120_models.QueryRecordByRecordIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordByRecordIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryRecordByRecordIdResponse().from_map(
            self.do_rpcrequest('QueryRecordByRecordId', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_record_by_record_id_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryRecordByRecordIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordByRecordIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryRecordByRecordIdResponse().from_map(
            await self.do_rpcrequest_async('QueryRecordByRecordId', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_record_by_record_id(
        self,
        request: linkvisual_20180120_models.QueryRecordByRecordIdRequest,
    ) -> linkvisual_20180120_models.QueryRecordByRecordIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_record_by_record_id_with_options(request, runtime)

    async def query_record_by_record_id_async(
        self,
        request: linkvisual_20180120_models.QueryRecordByRecordIdRequest,
    ) -> linkvisual_20180120_models.QueryRecordByRecordIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_record_by_record_id_with_options_async(request, runtime)

    def query_record_plan_detail_with_options(
        self,
        request: linkvisual_20180120_models.QueryRecordPlanDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordPlanDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryRecordPlanDetailResponse().from_map(
            self.do_rpcrequest('QueryRecordPlanDetail', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_record_plan_detail_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryRecordPlanDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordPlanDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryRecordPlanDetailResponse().from_map(
            await self.do_rpcrequest_async('QueryRecordPlanDetail', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_record_plan_detail(
        self,
        request: linkvisual_20180120_models.QueryRecordPlanDetailRequest,
    ) -> linkvisual_20180120_models.QueryRecordPlanDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_record_plan_detail_with_options(request, runtime)

    async def query_record_plan_detail_async(
        self,
        request: linkvisual_20180120_models.QueryRecordPlanDetailRequest,
    ) -> linkvisual_20180120_models.QueryRecordPlanDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_record_plan_detail_with_options_async(request, runtime)

    def query_record_plan_device_by_device_with_options(
        self,
        request: linkvisual_20180120_models.QueryRecordPlanDeviceByDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordPlanDeviceByDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryRecordPlanDeviceByDeviceResponse().from_map(
            self.do_rpcrequest('QueryRecordPlanDeviceByDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_record_plan_device_by_device_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryRecordPlanDeviceByDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordPlanDeviceByDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryRecordPlanDeviceByDeviceResponse().from_map(
            await self.do_rpcrequest_async('QueryRecordPlanDeviceByDevice', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_record_plan_device_by_device(
        self,
        request: linkvisual_20180120_models.QueryRecordPlanDeviceByDeviceRequest,
    ) -> linkvisual_20180120_models.QueryRecordPlanDeviceByDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_record_plan_device_by_device_with_options(request, runtime)

    async def query_record_plan_device_by_device_async(
        self,
        request: linkvisual_20180120_models.QueryRecordPlanDeviceByDeviceRequest,
    ) -> linkvisual_20180120_models.QueryRecordPlanDeviceByDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_record_plan_device_by_device_with_options_async(request, runtime)

    def query_record_plan_device_by_plan_with_options(
        self,
        request: linkvisual_20180120_models.QueryRecordPlanDeviceByPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordPlanDeviceByPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryRecordPlanDeviceByPlanResponse().from_map(
            self.do_rpcrequest('QueryRecordPlanDeviceByPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_record_plan_device_by_plan_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryRecordPlanDeviceByPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordPlanDeviceByPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryRecordPlanDeviceByPlanResponse().from_map(
            await self.do_rpcrequest_async('QueryRecordPlanDeviceByPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_record_plan_device_by_plan(
        self,
        request: linkvisual_20180120_models.QueryRecordPlanDeviceByPlanRequest,
    ) -> linkvisual_20180120_models.QueryRecordPlanDeviceByPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_record_plan_device_by_plan_with_options(request, runtime)

    async def query_record_plan_device_by_plan_async(
        self,
        request: linkvisual_20180120_models.QueryRecordPlanDeviceByPlanRequest,
    ) -> linkvisual_20180120_models.QueryRecordPlanDeviceByPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_record_plan_device_by_plan_with_options_async(request, runtime)

    def query_record_plans_with_options(
        self,
        request: linkvisual_20180120_models.QueryRecordPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordPlansResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryRecordPlansResponse().from_map(
            self.do_rpcrequest('QueryRecordPlans', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_record_plans_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryRecordPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordPlansResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryRecordPlansResponse().from_map(
            await self.do_rpcrequest_async('QueryRecordPlans', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_record_plans(
        self,
        request: linkvisual_20180120_models.QueryRecordPlansRequest,
    ) -> linkvisual_20180120_models.QueryRecordPlansResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_record_plans_with_options(request, runtime)

    async def query_record_plans_async(
        self,
        request: linkvisual_20180120_models.QueryRecordPlansRequest,
    ) -> linkvisual_20180120_models.QueryRecordPlansResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_record_plans_with_options_async(request, runtime)

    def query_record_url_with_options(
        self,
        request: linkvisual_20180120_models.QueryRecordUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryRecordUrlResponse().from_map(
            self.do_rpcrequest('QueryRecordUrl', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_record_url_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryRecordUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryRecordUrlResponse().from_map(
            await self.do_rpcrequest_async('QueryRecordUrl', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_record_url(
        self,
        request: linkvisual_20180120_models.QueryRecordUrlRequest,
    ) -> linkvisual_20180120_models.QueryRecordUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_record_url_with_options(request, runtime)

    async def query_record_url_async(
        self,
        request: linkvisual_20180120_models.QueryRecordUrlRequest,
    ) -> linkvisual_20180120_models.QueryRecordUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_record_url_with_options_async(request, runtime)

    def query_standard_aiapp_templates_with_options(
        self,
        request: linkvisual_20180120_models.QueryStandardAIAppTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryStandardAIAppTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryStandardAIAppTemplatesResponse().from_map(
            self.do_rpcrequest('QueryStandardAIAppTemplates', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_standard_aiapp_templates_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryStandardAIAppTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryStandardAIAppTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryStandardAIAppTemplatesResponse().from_map(
            await self.do_rpcrequest_async('QueryStandardAIAppTemplates', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_standard_aiapp_templates(
        self,
        request: linkvisual_20180120_models.QueryStandardAIAppTemplatesRequest,
    ) -> linkvisual_20180120_models.QueryStandardAIAppTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_standard_aiapp_templates_with_options(request, runtime)

    async def query_standard_aiapp_templates_async(
        self,
        request: linkvisual_20180120_models.QueryStandardAIAppTemplatesRequest,
    ) -> linkvisual_20180120_models.QueryStandardAIAppTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_standard_aiapp_templates_with_options_async(request, runtime)

    def query_time_template_with_options(
        self,
        request: linkvisual_20180120_models.QueryTimeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryTimeTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryTimeTemplateResponse().from_map(
            self.do_rpcrequest('QueryTimeTemplate', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_time_template_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryTimeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryTimeTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryTimeTemplateResponse().from_map(
            await self.do_rpcrequest_async('QueryTimeTemplate', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_time_template(
        self,
        request: linkvisual_20180120_models.QueryTimeTemplateRequest,
    ) -> linkvisual_20180120_models.QueryTimeTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_time_template_with_options(request, runtime)

    async def query_time_template_async(
        self,
        request: linkvisual_20180120_models.QueryTimeTemplateRequest,
    ) -> linkvisual_20180120_models.QueryTimeTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_time_template_with_options_async(request, runtime)

    def query_time_template_detail_with_options(
        self,
        request: linkvisual_20180120_models.QueryTimeTemplateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryTimeTemplateDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryTimeTemplateDetailResponse().from_map(
            self.do_rpcrequest('QueryTimeTemplateDetail', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_time_template_detail_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryTimeTemplateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryTimeTemplateDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryTimeTemplateDetailResponse().from_map(
            await self.do_rpcrequest_async('QueryTimeTemplateDetail', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_time_template_detail(
        self,
        request: linkvisual_20180120_models.QueryTimeTemplateDetailRequest,
    ) -> linkvisual_20180120_models.QueryTimeTemplateDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_time_template_detail_with_options(request, runtime)

    async def query_time_template_detail_async(
        self,
        request: linkvisual_20180120_models.QueryTimeTemplateDetailRequest,
    ) -> linkvisual_20180120_models.QueryTimeTemplateDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_time_template_detail_with_options_async(request, runtime)

    def query_voice_intercom_with_options(
        self,
        request: linkvisual_20180120_models.QueryVoiceIntercomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryVoiceIntercomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryVoiceIntercomResponse().from_map(
            self.do_rpcrequest('QueryVoiceIntercom', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_voice_intercom_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryVoiceIntercomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryVoiceIntercomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.QueryVoiceIntercomResponse().from_map(
            await self.do_rpcrequest_async('QueryVoiceIntercom', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_voice_intercom(
        self,
        request: linkvisual_20180120_models.QueryVoiceIntercomRequest,
    ) -> linkvisual_20180120_models.QueryVoiceIntercomResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_voice_intercom_with_options(request, runtime)

    async def query_voice_intercom_async(
        self,
        request: linkvisual_20180120_models.QueryVoiceIntercomRequest,
    ) -> linkvisual_20180120_models.QueryVoiceIntercomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_voice_intercom_with_options_async(request, runtime)

    def remove_aiapp_with_options(
        self,
        request: linkvisual_20180120_models.RemoveAIAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.RemoveAIAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.RemoveAIAppResponse().from_map(
            self.do_rpcrequest('RemoveAIApp', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_aiapp_with_options_async(
        self,
        request: linkvisual_20180120_models.RemoveAIAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.RemoveAIAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.RemoveAIAppResponse().from_map(
            await self.do_rpcrequest_async('RemoveAIApp', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_aiapp(
        self,
        request: linkvisual_20180120_models.RemoveAIAppRequest,
    ) -> linkvisual_20180120_models.RemoveAIAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_aiapp_with_options(request, runtime)

    async def remove_aiapp_async(
        self,
        request: linkvisual_20180120_models.RemoveAIAppRequest,
    ) -> linkvisual_20180120_models.RemoveAIAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_aiapp_with_options_async(request, runtime)

    def remove_aiplan_with_options(
        self,
        request: linkvisual_20180120_models.RemoveAIPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.RemoveAIPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.RemoveAIPlanResponse().from_map(
            self.do_rpcrequest('RemoveAIPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_aiplan_with_options_async(
        self,
        request: linkvisual_20180120_models.RemoveAIPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.RemoveAIPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.RemoveAIPlanResponse().from_map(
            await self.do_rpcrequest_async('RemoveAIPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_aiplan(
        self,
        request: linkvisual_20180120_models.RemoveAIPlanRequest,
    ) -> linkvisual_20180120_models.RemoveAIPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_aiplan_with_options(request, runtime)

    async def remove_aiplan_async(
        self,
        request: linkvisual_20180120_models.RemoveAIPlanRequest,
    ) -> linkvisual_20180120_models.RemoveAIPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_aiplan_with_options_async(request, runtime)

    def remove_device_purify_plan_with_options(
        self,
        request: linkvisual_20180120_models.RemoveDevicePurifyPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.RemoveDevicePurifyPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.RemoveDevicePurifyPlanResponse().from_map(
            self.do_rpcrequest('RemoveDevicePurifyPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_device_purify_plan_with_options_async(
        self,
        request: linkvisual_20180120_models.RemoveDevicePurifyPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.RemoveDevicePurifyPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.RemoveDevicePurifyPlanResponse().from_map(
            await self.do_rpcrequest_async('RemoveDevicePurifyPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_device_purify_plan(
        self,
        request: linkvisual_20180120_models.RemoveDevicePurifyPlanRequest,
    ) -> linkvisual_20180120_models.RemoveDevicePurifyPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_device_purify_plan_with_options(request, runtime)

    async def remove_device_purify_plan_async(
        self,
        request: linkvisual_20180120_models.RemoveDevicePurifyPlanRequest,
    ) -> linkvisual_20180120_models.RemoveDevicePurifyPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_device_purify_plan_with_options_async(request, runtime)

    def remove_face_device_from_device_group_with_options(
        self,
        request: linkvisual_20180120_models.RemoveFaceDeviceFromDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.RemoveFaceDeviceFromDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.RemoveFaceDeviceFromDeviceGroupResponse().from_map(
            self.do_rpcrequest('RemoveFaceDeviceFromDeviceGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_face_device_from_device_group_with_options_async(
        self,
        request: linkvisual_20180120_models.RemoveFaceDeviceFromDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.RemoveFaceDeviceFromDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.RemoveFaceDeviceFromDeviceGroupResponse().from_map(
            await self.do_rpcrequest_async('RemoveFaceDeviceFromDeviceGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_face_device_from_device_group(
        self,
        request: linkvisual_20180120_models.RemoveFaceDeviceFromDeviceGroupRequest,
    ) -> linkvisual_20180120_models.RemoveFaceDeviceFromDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_face_device_from_device_group_with_options(request, runtime)

    async def remove_face_device_from_device_group_async(
        self,
        request: linkvisual_20180120_models.RemoveFaceDeviceFromDeviceGroupRequest,
    ) -> linkvisual_20180120_models.RemoveFaceDeviceFromDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_face_device_from_device_group_with_options_async(request, runtime)

    def remove_face_user_from_user_group_with_options(
        self,
        request: linkvisual_20180120_models.RemoveFaceUserFromUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.RemoveFaceUserFromUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.RemoveFaceUserFromUserGroupResponse().from_map(
            self.do_rpcrequest('RemoveFaceUserFromUserGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_face_user_from_user_group_with_options_async(
        self,
        request: linkvisual_20180120_models.RemoveFaceUserFromUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.RemoveFaceUserFromUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.RemoveFaceUserFromUserGroupResponse().from_map(
            await self.do_rpcrequest_async('RemoveFaceUserFromUserGroup', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_face_user_from_user_group(
        self,
        request: linkvisual_20180120_models.RemoveFaceUserFromUserGroupRequest,
    ) -> linkvisual_20180120_models.RemoveFaceUserFromUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_face_user_from_user_group_with_options(request, runtime)

    async def remove_face_user_from_user_group_async(
        self,
        request: linkvisual_20180120_models.RemoveFaceUserFromUserGroupRequest,
    ) -> linkvisual_20180120_models.RemoveFaceUserFromUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_face_user_from_user_group_with_options_async(request, runtime)

    def set_device_picture_life_cycle_with_options(
        self,
        request: linkvisual_20180120_models.SetDevicePictureLifeCycleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.SetDevicePictureLifeCycleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.SetDevicePictureLifeCycleResponse().from_map(
            self.do_rpcrequest('SetDevicePictureLifeCycle', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_device_picture_life_cycle_with_options_async(
        self,
        request: linkvisual_20180120_models.SetDevicePictureLifeCycleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.SetDevicePictureLifeCycleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.SetDevicePictureLifeCycleResponse().from_map(
            await self.do_rpcrequest_async('SetDevicePictureLifeCycle', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_device_picture_life_cycle(
        self,
        request: linkvisual_20180120_models.SetDevicePictureLifeCycleRequest,
    ) -> linkvisual_20180120_models.SetDevicePictureLifeCycleResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_device_picture_life_cycle_with_options(request, runtime)

    async def set_device_picture_life_cycle_async(
        self,
        request: linkvisual_20180120_models.SetDevicePictureLifeCycleRequest,
    ) -> linkvisual_20180120_models.SetDevicePictureLifeCycleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_device_picture_life_cycle_with_options_async(request, runtime)

    def set_device_record_life_cycle_with_options(
        self,
        request: linkvisual_20180120_models.SetDeviceRecordLifeCycleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.SetDeviceRecordLifeCycleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.SetDeviceRecordLifeCycleResponse().from_map(
            self.do_rpcrequest('SetDeviceRecordLifeCycle', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_device_record_life_cycle_with_options_async(
        self,
        request: linkvisual_20180120_models.SetDeviceRecordLifeCycleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.SetDeviceRecordLifeCycleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.SetDeviceRecordLifeCycleResponse().from_map(
            await self.do_rpcrequest_async('SetDeviceRecordLifeCycle', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_device_record_life_cycle(
        self,
        request: linkvisual_20180120_models.SetDeviceRecordLifeCycleRequest,
    ) -> linkvisual_20180120_models.SetDeviceRecordLifeCycleResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_device_record_life_cycle_with_options(request, runtime)

    async def set_device_record_life_cycle_async(
        self,
        request: linkvisual_20180120_models.SetDeviceRecordLifeCycleRequest,
    ) -> linkvisual_20180120_models.SetDeviceRecordLifeCycleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_device_record_life_cycle_with_options_async(request, runtime)

    def stop_live_streaming_with_options(
        self,
        request: linkvisual_20180120_models.StopLiveStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.StopLiveStreamingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.StopLiveStreamingResponse().from_map(
            self.do_rpcrequest('StopLiveStreaming', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_live_streaming_with_options_async(
        self,
        request: linkvisual_20180120_models.StopLiveStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.StopLiveStreamingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.StopLiveStreamingResponse().from_map(
            await self.do_rpcrequest_async('StopLiveStreaming', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_live_streaming(
        self,
        request: linkvisual_20180120_models.StopLiveStreamingRequest,
    ) -> linkvisual_20180120_models.StopLiveStreamingResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_live_streaming_with_options(request, runtime)

    async def stop_live_streaming_async(
        self,
        request: linkvisual_20180120_models.StopLiveStreamingRequest,
    ) -> linkvisual_20180120_models.StopLiveStreamingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_live_streaming_with_options_async(request, runtime)

    def stop_triggered_record_with_options(
        self,
        request: linkvisual_20180120_models.StopTriggeredRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.StopTriggeredRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.StopTriggeredRecordResponse().from_map(
            self.do_rpcrequest('StopTriggeredRecord', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_triggered_record_with_options_async(
        self,
        request: linkvisual_20180120_models.StopTriggeredRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.StopTriggeredRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.StopTriggeredRecordResponse().from_map(
            await self.do_rpcrequest_async('StopTriggeredRecord', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_triggered_record(
        self,
        request: linkvisual_20180120_models.StopTriggeredRecordRequest,
    ) -> linkvisual_20180120_models.StopTriggeredRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_triggered_record_with_options(request, runtime)

    async def stop_triggered_record_async(
        self,
        request: linkvisual_20180120_models.StopTriggeredRecordRequest,
    ) -> linkvisual_20180120_models.StopTriggeredRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_triggered_record_with_options_async(request, runtime)

    def trigger_capture_picture_with_options(
        self,
        request: linkvisual_20180120_models.TriggerCapturePictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.TriggerCapturePictureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.TriggerCapturePictureResponse().from_map(
            self.do_rpcrequest('TriggerCapturePicture', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def trigger_capture_picture_with_options_async(
        self,
        request: linkvisual_20180120_models.TriggerCapturePictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.TriggerCapturePictureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.TriggerCapturePictureResponse().from_map(
            await self.do_rpcrequest_async('TriggerCapturePicture', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def trigger_capture_picture(
        self,
        request: linkvisual_20180120_models.TriggerCapturePictureRequest,
    ) -> linkvisual_20180120_models.TriggerCapturePictureResponse:
        runtime = util_models.RuntimeOptions()
        return self.trigger_capture_picture_with_options(request, runtime)

    async def trigger_capture_picture_async(
        self,
        request: linkvisual_20180120_models.TriggerCapturePictureRequest,
    ) -> linkvisual_20180120_models.TriggerCapturePictureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.trigger_capture_picture_with_options_async(request, runtime)

    def trigger_record_with_options(
        self,
        request: linkvisual_20180120_models.TriggerRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.TriggerRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.TriggerRecordResponse().from_map(
            self.do_rpcrequest('TriggerRecord', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def trigger_record_with_options_async(
        self,
        request: linkvisual_20180120_models.TriggerRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.TriggerRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.TriggerRecordResponse().from_map(
            await self.do_rpcrequest_async('TriggerRecord', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def trigger_record(
        self,
        request: linkvisual_20180120_models.TriggerRecordRequest,
    ) -> linkvisual_20180120_models.TriggerRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.trigger_record_with_options(request, runtime)

    async def trigger_record_async(
        self,
        request: linkvisual_20180120_models.TriggerRecordRequest,
    ) -> linkvisual_20180120_models.TriggerRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.trigger_record_with_options_async(request, runtime)

    def unbind_aiplan_with_devices_with_options(
        self,
        request: linkvisual_20180120_models.UnbindAIPlanWithDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UnbindAIPlanWithDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.UnbindAIPlanWithDevicesResponse().from_map(
            self.do_rpcrequest('UnbindAIPlanWithDevices', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_aiplan_with_devices_with_options_async(
        self,
        request: linkvisual_20180120_models.UnbindAIPlanWithDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UnbindAIPlanWithDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.UnbindAIPlanWithDevicesResponse().from_map(
            await self.do_rpcrequest_async('UnbindAIPlanWithDevices', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_aiplan_with_devices(
        self,
        request: linkvisual_20180120_models.UnbindAIPlanWithDevicesRequest,
    ) -> linkvisual_20180120_models.UnbindAIPlanWithDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_aiplan_with_devices_with_options(request, runtime)

    async def unbind_aiplan_with_devices_async(
        self,
        request: linkvisual_20180120_models.UnbindAIPlanWithDevicesRequest,
    ) -> linkvisual_20180120_models.UnbindAIPlanWithDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_aiplan_with_devices_with_options_async(request, runtime)

    def unbind_picture_search_app_with_devices_with_options(
        self,
        request: linkvisual_20180120_models.UnbindPictureSearchAppWithDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UnbindPictureSearchAppWithDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.UnbindPictureSearchAppWithDevicesResponse().from_map(
            self.do_rpcrequest('UnbindPictureSearchAppWithDevices', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_picture_search_app_with_devices_with_options_async(
        self,
        request: linkvisual_20180120_models.UnbindPictureSearchAppWithDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UnbindPictureSearchAppWithDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.UnbindPictureSearchAppWithDevicesResponse().from_map(
            await self.do_rpcrequest_async('UnbindPictureSearchAppWithDevices', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_picture_search_app_with_devices(
        self,
        request: linkvisual_20180120_models.UnbindPictureSearchAppWithDevicesRequest,
    ) -> linkvisual_20180120_models.UnbindPictureSearchAppWithDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_picture_search_app_with_devices_with_options(request, runtime)

    async def unbind_picture_search_app_with_devices_async(
        self,
        request: linkvisual_20180120_models.UnbindPictureSearchAppWithDevicesRequest,
    ) -> linkvisual_20180120_models.UnbindPictureSearchAppWithDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_picture_search_app_with_devices_with_options_async(request, runtime)

    def update_aiapp_with_options(
        self,
        request: linkvisual_20180120_models.UpdateAIAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateAIAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.UpdateAIAppResponse().from_map(
            self.do_rpcrequest('UpdateAIApp', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_aiapp_with_options_async(
        self,
        request: linkvisual_20180120_models.UpdateAIAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateAIAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.UpdateAIAppResponse().from_map(
            await self.do_rpcrequest_async('UpdateAIApp', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_aiapp(
        self,
        request: linkvisual_20180120_models.UpdateAIAppRequest,
    ) -> linkvisual_20180120_models.UpdateAIAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_aiapp_with_options(request, runtime)

    async def update_aiapp_async(
        self,
        request: linkvisual_20180120_models.UpdateAIAppRequest,
    ) -> linkvisual_20180120_models.UpdateAIAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_aiapp_with_options_async(request, runtime)

    def update_aiplan_with_options(
        self,
        request: linkvisual_20180120_models.UpdateAIPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateAIPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.UpdateAIPlanResponse().from_map(
            self.do_rpcrequest('UpdateAIPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_aiplan_with_options_async(
        self,
        request: linkvisual_20180120_models.UpdateAIPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateAIPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.UpdateAIPlanResponse().from_map(
            await self.do_rpcrequest_async('UpdateAIPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_aiplan(
        self,
        request: linkvisual_20180120_models.UpdateAIPlanRequest,
    ) -> linkvisual_20180120_models.UpdateAIPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_aiplan_with_options(request, runtime)

    async def update_aiplan_async(
        self,
        request: linkvisual_20180120_models.UpdateAIPlanRequest,
    ) -> linkvisual_20180120_models.UpdateAIPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_aiplan_with_options_async(request, runtime)

    def update_device_purify_plan_with_options(
        self,
        request: linkvisual_20180120_models.UpdateDevicePurifyPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateDevicePurifyPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.UpdateDevicePurifyPlanResponse().from_map(
            self.do_rpcrequest('UpdateDevicePurifyPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_device_purify_plan_with_options_async(
        self,
        request: linkvisual_20180120_models.UpdateDevicePurifyPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateDevicePurifyPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.UpdateDevicePurifyPlanResponse().from_map(
            await self.do_rpcrequest_async('UpdateDevicePurifyPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_device_purify_plan(
        self,
        request: linkvisual_20180120_models.UpdateDevicePurifyPlanRequest,
    ) -> linkvisual_20180120_models.UpdateDevicePurifyPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_device_purify_plan_with_options(request, runtime)

    async def update_device_purify_plan_async(
        self,
        request: linkvisual_20180120_models.UpdateDevicePurifyPlanRequest,
    ) -> linkvisual_20180120_models.UpdateDevicePurifyPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_device_purify_plan_with_options_async(request, runtime)

    def update_event_record_plan_with_options(
        self,
        request: linkvisual_20180120_models.UpdateEventRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateEventRecordPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.UpdateEventRecordPlanResponse().from_map(
            self.do_rpcrequest('UpdateEventRecordPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_event_record_plan_with_options_async(
        self,
        request: linkvisual_20180120_models.UpdateEventRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateEventRecordPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.UpdateEventRecordPlanResponse().from_map(
            await self.do_rpcrequest_async('UpdateEventRecordPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_event_record_plan(
        self,
        request: linkvisual_20180120_models.UpdateEventRecordPlanRequest,
    ) -> linkvisual_20180120_models.UpdateEventRecordPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_event_record_plan_with_options(request, runtime)

    async def update_event_record_plan_async(
        self,
        request: linkvisual_20180120_models.UpdateEventRecordPlanRequest,
    ) -> linkvisual_20180120_models.UpdateEventRecordPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_event_record_plan_with_options_async(request, runtime)

    def update_face_user_with_options(
        self,
        request: linkvisual_20180120_models.UpdateFaceUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateFaceUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.UpdateFaceUserResponse().from_map(
            self.do_rpcrequest('UpdateFaceUser', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_face_user_with_options_async(
        self,
        request: linkvisual_20180120_models.UpdateFaceUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateFaceUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.UpdateFaceUserResponse().from_map(
            await self.do_rpcrequest_async('UpdateFaceUser', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_face_user(
        self,
        request: linkvisual_20180120_models.UpdateFaceUserRequest,
    ) -> linkvisual_20180120_models.UpdateFaceUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_face_user_with_options(request, runtime)

    async def update_face_user_async(
        self,
        request: linkvisual_20180120_models.UpdateFaceUserRequest,
    ) -> linkvisual_20180120_models.UpdateFaceUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_face_user_with_options_async(request, runtime)

    def update_face_user_group_and_device_group_relation_with_options(
        self,
        request: linkvisual_20180120_models.UpdateFaceUserGroupAndDeviceGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateFaceUserGroupAndDeviceGroupRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.UpdateFaceUserGroupAndDeviceGroupRelationResponse().from_map(
            self.do_rpcrequest('UpdateFaceUserGroupAndDeviceGroupRelation', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_face_user_group_and_device_group_relation_with_options_async(
        self,
        request: linkvisual_20180120_models.UpdateFaceUserGroupAndDeviceGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateFaceUserGroupAndDeviceGroupRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.UpdateFaceUserGroupAndDeviceGroupRelationResponse().from_map(
            await self.do_rpcrequest_async('UpdateFaceUserGroupAndDeviceGroupRelation', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_face_user_group_and_device_group_relation(
        self,
        request: linkvisual_20180120_models.UpdateFaceUserGroupAndDeviceGroupRelationRequest,
    ) -> linkvisual_20180120_models.UpdateFaceUserGroupAndDeviceGroupRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_face_user_group_and_device_group_relation_with_options(request, runtime)

    async def update_face_user_group_and_device_group_relation_async(
        self,
        request: linkvisual_20180120_models.UpdateFaceUserGroupAndDeviceGroupRelationRequest,
    ) -> linkvisual_20180120_models.UpdateFaceUserGroupAndDeviceGroupRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_face_user_group_and_device_group_relation_with_options_async(request, runtime)

    def update_model_with_options(
        self,
        request: linkvisual_20180120_models.UpdateModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.UpdateModelResponse().from_map(
            self.do_rpcrequest('UpdateModel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_model_with_options_async(
        self,
        request: linkvisual_20180120_models.UpdateModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.UpdateModelResponse().from_map(
            await self.do_rpcrequest_async('UpdateModel', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_model(
        self,
        request: linkvisual_20180120_models.UpdateModelRequest,
    ) -> linkvisual_20180120_models.UpdateModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_model_with_options(request, runtime)

    async def update_model_async(
        self,
        request: linkvisual_20180120_models.UpdateModelRequest,
    ) -> linkvisual_20180120_models.UpdateModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_model_with_options_async(request, runtime)

    def update_record_plan_with_options(
        self,
        request: linkvisual_20180120_models.UpdateRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateRecordPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.UpdateRecordPlanResponse().from_map(
            self.do_rpcrequest('UpdateRecordPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_record_plan_with_options_async(
        self,
        request: linkvisual_20180120_models.UpdateRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateRecordPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.UpdateRecordPlanResponse().from_map(
            await self.do_rpcrequest_async('UpdateRecordPlan', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_record_plan(
        self,
        request: linkvisual_20180120_models.UpdateRecordPlanRequest,
    ) -> linkvisual_20180120_models.UpdateRecordPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_record_plan_with_options(request, runtime)

    async def update_record_plan_async(
        self,
        request: linkvisual_20180120_models.UpdateRecordPlanRequest,
    ) -> linkvisual_20180120_models.UpdateRecordPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_record_plan_with_options_async(request, runtime)

    def update_time_template_with_options(
        self,
        request: linkvisual_20180120_models.UpdateTimeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateTimeTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.UpdateTimeTemplateResponse().from_map(
            self.do_rpcrequest('UpdateTimeTemplate', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_time_template_with_options_async(
        self,
        request: linkvisual_20180120_models.UpdateTimeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateTimeTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return linkvisual_20180120_models.UpdateTimeTemplateResponse().from_map(
            await self.do_rpcrequest_async('UpdateTimeTemplate', '2018-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_time_template(
        self,
        request: linkvisual_20180120_models.UpdateTimeTemplateRequest,
    ) -> linkvisual_20180120_models.UpdateTimeTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_time_template_with_options(request, runtime)

    async def update_time_template_async(
        self,
        request: linkvisual_20180120_models.UpdateTimeTemplateRequest,
    ) -> linkvisual_20180120_models.UpdateTimeTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_time_template_with_options_async(request, runtime)
