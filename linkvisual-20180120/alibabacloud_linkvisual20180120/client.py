# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_linkvisual20180120 import models as main_models
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_event_record_plan_device_with_options(
        self,
        request: main_models.AddEventRecordPlanDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddEventRecordPlanDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddEventRecordPlanDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddEventRecordPlanDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_event_record_plan_device_with_options_async(
        self,
        request: main_models.AddEventRecordPlanDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddEventRecordPlanDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddEventRecordPlanDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddEventRecordPlanDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_event_record_plan_device(
        self,
        request: main_models.AddEventRecordPlanDeviceRequest,
    ) -> main_models.AddEventRecordPlanDeviceResponse:
        runtime = RuntimeOptions()
        return self.add_event_record_plan_device_with_options(request, runtime)

    async def add_event_record_plan_device_async(
        self,
        request: main_models.AddEventRecordPlanDeviceRequest,
    ) -> main_models.AddEventRecordPlanDeviceResponse:
        runtime = RuntimeOptions()
        return await self.add_event_record_plan_device_with_options_async(request, runtime)

    def add_face_device_group_with_options(
        self,
        request: main_models.AddFaceDeviceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddFaceDeviceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_group_name):
            query['DeviceGroupName'] = request.device_group_name
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddFaceDeviceGroup',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFaceDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_face_device_group_with_options_async(
        self,
        request: main_models.AddFaceDeviceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddFaceDeviceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_group_name):
            query['DeviceGroupName'] = request.device_group_name
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddFaceDeviceGroup',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFaceDeviceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_face_device_group(
        self,
        request: main_models.AddFaceDeviceGroupRequest,
    ) -> main_models.AddFaceDeviceGroupResponse:
        runtime = RuntimeOptions()
        return self.add_face_device_group_with_options(request, runtime)

    async def add_face_device_group_async(
        self,
        request: main_models.AddFaceDeviceGroupRequest,
    ) -> main_models.AddFaceDeviceGroupResponse:
        runtime = RuntimeOptions()
        return await self.add_face_device_group_with_options_async(request, runtime)

    def add_face_device_to_device_group_with_options(
        self,
        request: main_models.AddFaceDeviceToDeviceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddFaceDeviceToDeviceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddFaceDeviceToDeviceGroup',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFaceDeviceToDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_face_device_to_device_group_with_options_async(
        self,
        request: main_models.AddFaceDeviceToDeviceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddFaceDeviceToDeviceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddFaceDeviceToDeviceGroup',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFaceDeviceToDeviceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_face_device_to_device_group(
        self,
        request: main_models.AddFaceDeviceToDeviceGroupRequest,
    ) -> main_models.AddFaceDeviceToDeviceGroupResponse:
        runtime = RuntimeOptions()
        return self.add_face_device_to_device_group_with_options(request, runtime)

    async def add_face_device_to_device_group_async(
        self,
        request: main_models.AddFaceDeviceToDeviceGroupRequest,
    ) -> main_models.AddFaceDeviceToDeviceGroupResponse:
        runtime = RuntimeOptions()
        return await self.add_face_device_to_device_group_with_options_async(request, runtime)

    def add_face_user_with_options(
        self,
        request: main_models.AddFaceUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddFaceUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not DaraCore.is_null(request.face_pic_url):
            query['FacePicUrl'] = request.face_pic_url
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddFaceUser',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFaceUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_face_user_with_options_async(
        self,
        request: main_models.AddFaceUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddFaceUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not DaraCore.is_null(request.face_pic_url):
            query['FacePicUrl'] = request.face_pic_url
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddFaceUser',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFaceUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_face_user(
        self,
        request: main_models.AddFaceUserRequest,
    ) -> main_models.AddFaceUserResponse:
        runtime = RuntimeOptions()
        return self.add_face_user_with_options(request, runtime)

    async def add_face_user_async(
        self,
        request: main_models.AddFaceUserRequest,
    ) -> main_models.AddFaceUserResponse:
        runtime = RuntimeOptions()
        return await self.add_face_user_with_options_async(request, runtime)

    def add_face_user_group_with_options(
        self,
        request: main_models.AddFaceUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddFaceUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddFaceUserGroup',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFaceUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_face_user_group_with_options_async(
        self,
        request: main_models.AddFaceUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddFaceUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddFaceUserGroup',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFaceUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_face_user_group(
        self,
        request: main_models.AddFaceUserGroupRequest,
    ) -> main_models.AddFaceUserGroupResponse:
        runtime = RuntimeOptions()
        return self.add_face_user_group_with_options(request, runtime)

    async def add_face_user_group_async(
        self,
        request: main_models.AddFaceUserGroupRequest,
    ) -> main_models.AddFaceUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.add_face_user_group_with_options_async(request, runtime)

    def add_face_user_group_and_device_group_relation_with_options(
        self,
        request: main_models.AddFaceUserGroupAndDeviceGroupRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddFaceUserGroupAndDeviceGroupRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.relation):
            query['Relation'] = request.relation
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddFaceUserGroupAndDeviceGroupRelation',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFaceUserGroupAndDeviceGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_face_user_group_and_device_group_relation_with_options_async(
        self,
        request: main_models.AddFaceUserGroupAndDeviceGroupRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddFaceUserGroupAndDeviceGroupRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.relation):
            query['Relation'] = request.relation
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddFaceUserGroupAndDeviceGroupRelation',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFaceUserGroupAndDeviceGroupRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_face_user_group_and_device_group_relation(
        self,
        request: main_models.AddFaceUserGroupAndDeviceGroupRelationRequest,
    ) -> main_models.AddFaceUserGroupAndDeviceGroupRelationResponse:
        runtime = RuntimeOptions()
        return self.add_face_user_group_and_device_group_relation_with_options(request, runtime)

    async def add_face_user_group_and_device_group_relation_async(
        self,
        request: main_models.AddFaceUserGroupAndDeviceGroupRelationRequest,
    ) -> main_models.AddFaceUserGroupAndDeviceGroupRelationResponse:
        runtime = RuntimeOptions()
        return await self.add_face_user_group_and_device_group_relation_with_options_async(request, runtime)

    def add_face_user_picture_with_options(
        self,
        request: main_models.AddFaceUserPictureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddFaceUserPictureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.face_pic_url):
            query['FacePicUrl'] = request.face_pic_url
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddFaceUserPicture',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFaceUserPictureResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_face_user_picture_with_options_async(
        self,
        request: main_models.AddFaceUserPictureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddFaceUserPictureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.face_pic_url):
            query['FacePicUrl'] = request.face_pic_url
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddFaceUserPicture',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFaceUserPictureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_face_user_picture(
        self,
        request: main_models.AddFaceUserPictureRequest,
    ) -> main_models.AddFaceUserPictureResponse:
        runtime = RuntimeOptions()
        return self.add_face_user_picture_with_options(request, runtime)

    async def add_face_user_picture_async(
        self,
        request: main_models.AddFaceUserPictureRequest,
    ) -> main_models.AddFaceUserPictureResponse:
        runtime = RuntimeOptions()
        return await self.add_face_user_picture_with_options_async(request, runtime)

    def add_face_user_to_user_group_with_options(
        self,
        request: main_models.AddFaceUserToUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddFaceUserToUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddFaceUserToUserGroup',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFaceUserToUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_face_user_to_user_group_with_options_async(
        self,
        request: main_models.AddFaceUserToUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddFaceUserToUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddFaceUserToUserGroup',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFaceUserToUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_face_user_to_user_group(
        self,
        request: main_models.AddFaceUserToUserGroupRequest,
    ) -> main_models.AddFaceUserToUserGroupResponse:
        runtime = RuntimeOptions()
        return self.add_face_user_to_user_group_with_options(request, runtime)

    async def add_face_user_to_user_group_async(
        self,
        request: main_models.AddFaceUserToUserGroupRequest,
    ) -> main_models.AddFaceUserToUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.add_face_user_to_user_group_with_options_async(request, runtime)

    def add_record_plan_device_with_options(
        self,
        request: main_models.AddRecordPlanDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddRecordPlanDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddRecordPlanDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddRecordPlanDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_record_plan_device_with_options_async(
        self,
        request: main_models.AddRecordPlanDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddRecordPlanDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddRecordPlanDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddRecordPlanDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_record_plan_device(
        self,
        request: main_models.AddRecordPlanDeviceRequest,
    ) -> main_models.AddRecordPlanDeviceResponse:
        runtime = RuntimeOptions()
        return self.add_record_plan_device_with_options(request, runtime)

    async def add_record_plan_device_async(
        self,
        request: main_models.AddRecordPlanDeviceRequest,
    ) -> main_models.AddRecordPlanDeviceResponse:
        runtime = RuntimeOptions()
        return await self.add_record_plan_device_with_options_async(request, runtime)

    def batch_query_vision_device_info_with_options(
        self,
        request: main_models.BatchQueryVisionDeviceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchQueryVisionDeviceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name_list):
            query['DeviceNameList'] = request.device_name_list
        if not DaraCore.is_null(request.iot_id_list):
            query['IotIdList'] = request.iot_id_list
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchQueryVisionDeviceInfo',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchQueryVisionDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_query_vision_device_info_with_options_async(
        self,
        request: main_models.BatchQueryVisionDeviceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchQueryVisionDeviceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name_list):
            query['DeviceNameList'] = request.device_name_list
        if not DaraCore.is_null(request.iot_id_list):
            query['IotIdList'] = request.iot_id_list
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchQueryVisionDeviceInfo',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchQueryVisionDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_query_vision_device_info(
        self,
        request: main_models.BatchQueryVisionDeviceInfoRequest,
    ) -> main_models.BatchQueryVisionDeviceInfoResponse:
        runtime = RuntimeOptions()
        return self.batch_query_vision_device_info_with_options(request, runtime)

    async def batch_query_vision_device_info_async(
        self,
        request: main_models.BatchQueryVisionDeviceInfoRequest,
    ) -> main_models.BatchQueryVisionDeviceInfoResponse:
        runtime = RuntimeOptions()
        return await self.batch_query_vision_device_info_with_options_async(request, runtime)

    def bind_picture_search_app_with_devices_with_options(
        self,
        request: main_models.BindPictureSearchAppWithDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindPictureSearchAppWithDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.device_iot_ids):
            query['DeviceIotIds'] = request.device_iot_ids
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindPictureSearchAppWithDevices',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindPictureSearchAppWithDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_picture_search_app_with_devices_with_options_async(
        self,
        request: main_models.BindPictureSearchAppWithDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindPictureSearchAppWithDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.device_iot_ids):
            query['DeviceIotIds'] = request.device_iot_ids
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindPictureSearchAppWithDevices',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindPictureSearchAppWithDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_picture_search_app_with_devices(
        self,
        request: main_models.BindPictureSearchAppWithDevicesRequest,
    ) -> main_models.BindPictureSearchAppWithDevicesResponse:
        runtime = RuntimeOptions()
        return self.bind_picture_search_app_with_devices_with_options(request, runtime)

    async def bind_picture_search_app_with_devices_async(
        self,
        request: main_models.BindPictureSearchAppWithDevicesRequest,
    ) -> main_models.BindPictureSearchAppWithDevicesResponse:
        runtime = RuntimeOptions()
        return await self.bind_picture_search_app_with_devices_with_options_async(request, runtime)

    def check_face_user_do_exist_on_device_with_options(
        self,
        request: main_models.CheckFaceUserDoExistOnDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckFaceUserDoExistOnDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckFaceUserDoExistOnDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckFaceUserDoExistOnDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_face_user_do_exist_on_device_with_options_async(
        self,
        request: main_models.CheckFaceUserDoExistOnDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckFaceUserDoExistOnDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckFaceUserDoExistOnDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckFaceUserDoExistOnDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_face_user_do_exist_on_device(
        self,
        request: main_models.CheckFaceUserDoExistOnDeviceRequest,
    ) -> main_models.CheckFaceUserDoExistOnDeviceResponse:
        runtime = RuntimeOptions()
        return self.check_face_user_do_exist_on_device_with_options(request, runtime)

    async def check_face_user_do_exist_on_device_async(
        self,
        request: main_models.CheckFaceUserDoExistOnDeviceRequest,
    ) -> main_models.CheckFaceUserDoExistOnDeviceResponse:
        runtime = RuntimeOptions()
        return await self.check_face_user_do_exist_on_device_with_options_async(request, runtime)

    def clear_face_device_dbwith_options(
        self,
        request: main_models.ClearFaceDeviceDBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ClearFaceDeviceDBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ClearFaceDeviceDB',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClearFaceDeviceDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_face_device_dbwith_options_async(
        self,
        request: main_models.ClearFaceDeviceDBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ClearFaceDeviceDBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ClearFaceDeviceDB',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClearFaceDeviceDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clear_face_device_db(
        self,
        request: main_models.ClearFaceDeviceDBRequest,
    ) -> main_models.ClearFaceDeviceDBResponse:
        runtime = RuntimeOptions()
        return self.clear_face_device_dbwith_options(request, runtime)

    async def clear_face_device_db_async(
        self,
        request: main_models.ClearFaceDeviceDBRequest,
    ) -> main_models.ClearFaceDeviceDBResponse:
        runtime = RuntimeOptions()
        return await self.clear_face_device_dbwith_options_async(request, runtime)

    def create_event_record_plan_with_options(
        self,
        request: main_models.CreateEventRecordPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEventRecordPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_types):
            query['EventTypes'] = request.event_types
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not DaraCore.is_null(request.record_duration):
            query['RecordDuration'] = request.record_duration
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateEventRecordPlan',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEventRecordPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_event_record_plan_with_options_async(
        self,
        request: main_models.CreateEventRecordPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEventRecordPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_types):
            query['EventTypes'] = request.event_types
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not DaraCore.is_null(request.record_duration):
            query['RecordDuration'] = request.record_duration
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateEventRecordPlan',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEventRecordPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_event_record_plan(
        self,
        request: main_models.CreateEventRecordPlanRequest,
    ) -> main_models.CreateEventRecordPlanResponse:
        runtime = RuntimeOptions()
        return self.create_event_record_plan_with_options(request, runtime)

    async def create_event_record_plan_async(
        self,
        request: main_models.CreateEventRecordPlanRequest,
    ) -> main_models.CreateEventRecordPlanResponse:
        runtime = RuntimeOptions()
        return await self.create_event_record_plan_with_options_async(request, runtime)

    def create_gb_device_with_options(
        self,
        request: main_models.CreateGbDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGbDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.device_type):
            query['DeviceType'] = request.device_type
        if not DaraCore.is_null(request.gb_id):
            query['GbId'] = request.gb_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.media_net_protocol):
            query['MediaNetProtocol'] = request.media_net_protocol
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.sub_product_key):
            query['SubProductKey'] = request.sub_product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGbDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGbDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gb_device_with_options_async(
        self,
        request: main_models.CreateGbDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGbDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.device_type):
            query['DeviceType'] = request.device_type
        if not DaraCore.is_null(request.gb_id):
            query['GbId'] = request.gb_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.media_net_protocol):
            query['MediaNetProtocol'] = request.media_net_protocol
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.sub_product_key):
            query['SubProductKey'] = request.sub_product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGbDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGbDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gb_device(
        self,
        request: main_models.CreateGbDeviceRequest,
    ) -> main_models.CreateGbDeviceResponse:
        runtime = RuntimeOptions()
        return self.create_gb_device_with_options(request, runtime)

    async def create_gb_device_async(
        self,
        request: main_models.CreateGbDeviceRequest,
    ) -> main_models.CreateGbDeviceResponse:
        runtime = RuntimeOptions()
        return await self.create_gb_device_with_options_async(request, runtime)

    def create_local_file_upload_job_with_options(
        self,
        request: main_models.CreateLocalFileUploadJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLocalFileUploadJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.time_slot):
            query['TimeSlot'] = request.time_slot
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLocalFileUploadJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLocalFileUploadJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_local_file_upload_job_with_options_async(
        self,
        request: main_models.CreateLocalFileUploadJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLocalFileUploadJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.time_slot):
            query['TimeSlot'] = request.time_slot
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLocalFileUploadJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLocalFileUploadJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_local_file_upload_job(
        self,
        request: main_models.CreateLocalFileUploadJobRequest,
    ) -> main_models.CreateLocalFileUploadJobResponse:
        runtime = RuntimeOptions()
        return self.create_local_file_upload_job_with_options(request, runtime)

    async def create_local_file_upload_job_async(
        self,
        request: main_models.CreateLocalFileUploadJobRequest,
    ) -> main_models.CreateLocalFileUploadJobResponse:
        runtime = RuntimeOptions()
        return await self.create_local_file_upload_job_with_options_async(request, runtime)

    def create_local_record_download_by_time_job_with_options(
        self,
        request: main_models.CreateLocalRecordDownloadByTimeJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLocalRecordDownloadByTimeJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.speed):
            query['Speed'] = request.speed
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLocalRecordDownloadByTimeJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLocalRecordDownloadByTimeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_local_record_download_by_time_job_with_options_async(
        self,
        request: main_models.CreateLocalRecordDownloadByTimeJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLocalRecordDownloadByTimeJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.speed):
            query['Speed'] = request.speed
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLocalRecordDownloadByTimeJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLocalRecordDownloadByTimeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_local_record_download_by_time_job(
        self,
        request: main_models.CreateLocalRecordDownloadByTimeJobRequest,
    ) -> main_models.CreateLocalRecordDownloadByTimeJobResponse:
        runtime = RuntimeOptions()
        return self.create_local_record_download_by_time_job_with_options(request, runtime)

    async def create_local_record_download_by_time_job_async(
        self,
        request: main_models.CreateLocalRecordDownloadByTimeJobRequest,
    ) -> main_models.CreateLocalRecordDownloadByTimeJobResponse:
        runtime = RuntimeOptions()
        return await self.create_local_record_download_by_time_job_with_options_async(request, runtime)

    def create_picture_search_app_with_options(
        self,
        request: main_models.CreatePictureSearchAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePictureSearchAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePictureSearchApp',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePictureSearchAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_picture_search_app_with_options_async(
        self,
        request: main_models.CreatePictureSearchAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePictureSearchAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePictureSearchApp',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePictureSearchAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_picture_search_app(
        self,
        request: main_models.CreatePictureSearchAppRequest,
    ) -> main_models.CreatePictureSearchAppResponse:
        runtime = RuntimeOptions()
        return self.create_picture_search_app_with_options(request, runtime)

    async def create_picture_search_app_async(
        self,
        request: main_models.CreatePictureSearchAppRequest,
    ) -> main_models.CreatePictureSearchAppResponse:
        runtime = RuntimeOptions()
        return await self.create_picture_search_app_with_options_async(request, runtime)

    def create_picture_search_job_with_options(
        self,
        request: main_models.CreatePictureSearchJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePictureSearchJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.body_threshold):
            query['BodyThreshold'] = request.body_threshold
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.picture_search_type):
            query['PictureSearchType'] = request.picture_search_type
        if not DaraCore.is_null(request.search_pic_url):
            query['SearchPicUrl'] = request.search_pic_url
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePictureSearchJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePictureSearchJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_picture_search_job_with_options_async(
        self,
        request: main_models.CreatePictureSearchJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePictureSearchJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.body_threshold):
            query['BodyThreshold'] = request.body_threshold
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.picture_search_type):
            query['PictureSearchType'] = request.picture_search_type
        if not DaraCore.is_null(request.search_pic_url):
            query['SearchPicUrl'] = request.search_pic_url
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePictureSearchJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePictureSearchJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_picture_search_job(
        self,
        request: main_models.CreatePictureSearchJobRequest,
    ) -> main_models.CreatePictureSearchJobResponse:
        runtime = RuntimeOptions()
        return self.create_picture_search_job_with_options(request, runtime)

    async def create_picture_search_job_async(
        self,
        request: main_models.CreatePictureSearchJobRequest,
    ) -> main_models.CreatePictureSearchJobResponse:
        runtime = RuntimeOptions()
        return await self.create_picture_search_job_with_options_async(request, runtime)

    def create_record_download_by_time_job_with_options(
        self,
        request: main_models.CreateRecordDownloadByTimeJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRecordDownloadByTimeJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.record_type):
            query['RecordType'] = request.record_type
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRecordDownloadByTimeJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRecordDownloadByTimeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_record_download_by_time_job_with_options_async(
        self,
        request: main_models.CreateRecordDownloadByTimeJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRecordDownloadByTimeJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.record_type):
            query['RecordType'] = request.record_type
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRecordDownloadByTimeJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRecordDownloadByTimeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_record_download_by_time_job(
        self,
        request: main_models.CreateRecordDownloadByTimeJobRequest,
    ) -> main_models.CreateRecordDownloadByTimeJobResponse:
        runtime = RuntimeOptions()
        return self.create_record_download_by_time_job_with_options(request, runtime)

    async def create_record_download_by_time_job_async(
        self,
        request: main_models.CreateRecordDownloadByTimeJobRequest,
    ) -> main_models.CreateRecordDownloadByTimeJobResponse:
        runtime = RuntimeOptions()
        return await self.create_record_download_by_time_job_with_options_async(request, runtime)

    def create_record_plan_with_options(
        self,
        request: main_models.CreateRecordPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRecordPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRecordPlan',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRecordPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_record_plan_with_options_async(
        self,
        request: main_models.CreateRecordPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRecordPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRecordPlan',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRecordPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_record_plan(
        self,
        request: main_models.CreateRecordPlanRequest,
    ) -> main_models.CreateRecordPlanResponse:
        runtime = RuntimeOptions()
        return self.create_record_plan_with_options(request, runtime)

    async def create_record_plan_async(
        self,
        request: main_models.CreateRecordPlanRequest,
    ) -> main_models.CreateRecordPlanResponse:
        runtime = RuntimeOptions()
        return await self.create_record_plan_with_options_async(request, runtime)

    def create_rtmp_device_with_options(
        self,
        request: main_models.CreateRtmpDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRtmpDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.pull_auth_key):
            query['PullAuthKey'] = request.pull_auth_key
        if not DaraCore.is_null(request.pull_key_expire_time):
            query['PullKeyExpireTime'] = request.pull_key_expire_time
        if not DaraCore.is_null(request.push_auth_key):
            query['PushAuthKey'] = request.push_auth_key
        if not DaraCore.is_null(request.push_key_expire_time):
            query['PushKeyExpireTime'] = request.push_key_expire_time
        if not DaraCore.is_null(request.sub_stream_name):
            query['SubStreamName'] = request.sub_stream_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRtmpDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRtmpDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rtmp_device_with_options_async(
        self,
        request: main_models.CreateRtmpDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRtmpDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.pull_auth_key):
            query['PullAuthKey'] = request.pull_auth_key
        if not DaraCore.is_null(request.pull_key_expire_time):
            query['PullKeyExpireTime'] = request.pull_key_expire_time
        if not DaraCore.is_null(request.push_auth_key):
            query['PushAuthKey'] = request.push_auth_key
        if not DaraCore.is_null(request.push_key_expire_time):
            query['PushKeyExpireTime'] = request.push_key_expire_time
        if not DaraCore.is_null(request.sub_stream_name):
            query['SubStreamName'] = request.sub_stream_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRtmpDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRtmpDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rtmp_device(
        self,
        request: main_models.CreateRtmpDeviceRequest,
    ) -> main_models.CreateRtmpDeviceResponse:
        runtime = RuntimeOptions()
        return self.create_rtmp_device_with_options(request, runtime)

    async def create_rtmp_device_async(
        self,
        request: main_models.CreateRtmpDeviceRequest,
    ) -> main_models.CreateRtmpDeviceResponse:
        runtime = RuntimeOptions()
        return await self.create_rtmp_device_with_options_async(request, runtime)

    def create_stream_push_job_with_options(
        self,
        request: main_models.CreateStreamPushJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStreamPushJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.push_url):
            query['PushUrl'] = request.push_url
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateStreamPushJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStreamPushJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_stream_push_job_with_options_async(
        self,
        request: main_models.CreateStreamPushJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStreamPushJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.push_url):
            query['PushUrl'] = request.push_url
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateStreamPushJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStreamPushJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_stream_push_job(
        self,
        request: main_models.CreateStreamPushJobRequest,
    ) -> main_models.CreateStreamPushJobResponse:
        runtime = RuntimeOptions()
        return self.create_stream_push_job_with_options(request, runtime)

    async def create_stream_push_job_async(
        self,
        request: main_models.CreateStreamPushJobRequest,
    ) -> main_models.CreateStreamPushJobResponse:
        runtime = RuntimeOptions()
        return await self.create_stream_push_job_with_options_async(request, runtime)

    def create_stream_snapshot_job_with_options(
        self,
        request: main_models.CreateStreamSnapshotJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStreamSnapshotJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.snapshot_interval):
            query['SnapshotInterval'] = request.snapshot_interval
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateStreamSnapshotJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStreamSnapshotJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_stream_snapshot_job_with_options_async(
        self,
        request: main_models.CreateStreamSnapshotJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStreamSnapshotJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.snapshot_interval):
            query['SnapshotInterval'] = request.snapshot_interval
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateStreamSnapshotJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStreamSnapshotJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_stream_snapshot_job(
        self,
        request: main_models.CreateStreamSnapshotJobRequest,
    ) -> main_models.CreateStreamSnapshotJobResponse:
        runtime = RuntimeOptions()
        return self.create_stream_snapshot_job_with_options(request, runtime)

    async def create_stream_snapshot_job_async(
        self,
        request: main_models.CreateStreamSnapshotJobRequest,
    ) -> main_models.CreateStreamSnapshotJobResponse:
        runtime = RuntimeOptions()
        return await self.create_stream_snapshot_job_with_options_async(request, runtime)

    def create_time_template_with_options(
        self,
        request: main_models.CreateTimeTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTimeTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all_day):
            query['AllDay'] = request.all_day
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.time_sections):
            query['TimeSections'] = request.time_sections
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTimeTemplate',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTimeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_time_template_with_options_async(
        self,
        request: main_models.CreateTimeTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTimeTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all_day):
            query['AllDay'] = request.all_day
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.time_sections):
            query['TimeSections'] = request.time_sections
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTimeTemplate',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTimeTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_time_template(
        self,
        request: main_models.CreateTimeTemplateRequest,
    ) -> main_models.CreateTimeTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_time_template_with_options(request, runtime)

    async def create_time_template_async(
        self,
        request: main_models.CreateTimeTemplateRequest,
    ) -> main_models.CreateTimeTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_time_template_with_options_async(request, runtime)

    def delete_event_record_plan_with_options(
        self,
        request: main_models.DeleteEventRecordPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEventRecordPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEventRecordPlan',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEventRecordPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_record_plan_with_options_async(
        self,
        request: main_models.DeleteEventRecordPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEventRecordPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEventRecordPlan',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEventRecordPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_event_record_plan(
        self,
        request: main_models.DeleteEventRecordPlanRequest,
    ) -> main_models.DeleteEventRecordPlanResponse:
        runtime = RuntimeOptions()
        return self.delete_event_record_plan_with_options(request, runtime)

    async def delete_event_record_plan_async(
        self,
        request: main_models.DeleteEventRecordPlanRequest,
    ) -> main_models.DeleteEventRecordPlanResponse:
        runtime = RuntimeOptions()
        return await self.delete_event_record_plan_with_options_async(request, runtime)

    def delete_event_record_plan_device_with_options(
        self,
        request: main_models.DeleteEventRecordPlanDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEventRecordPlanDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEventRecordPlanDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEventRecordPlanDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_record_plan_device_with_options_async(
        self,
        request: main_models.DeleteEventRecordPlanDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEventRecordPlanDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEventRecordPlanDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEventRecordPlanDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_event_record_plan_device(
        self,
        request: main_models.DeleteEventRecordPlanDeviceRequest,
    ) -> main_models.DeleteEventRecordPlanDeviceResponse:
        runtime = RuntimeOptions()
        return self.delete_event_record_plan_device_with_options(request, runtime)

    async def delete_event_record_plan_device_async(
        self,
        request: main_models.DeleteEventRecordPlanDeviceRequest,
    ) -> main_models.DeleteEventRecordPlanDeviceResponse:
        runtime = RuntimeOptions()
        return await self.delete_event_record_plan_device_with_options_async(request, runtime)

    def delete_face_device_group_with_options(
        self,
        request: main_models.DeleteFaceDeviceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFaceDeviceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFaceDeviceGroup',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFaceDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_face_device_group_with_options_async(
        self,
        request: main_models.DeleteFaceDeviceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFaceDeviceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFaceDeviceGroup',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFaceDeviceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_face_device_group(
        self,
        request: main_models.DeleteFaceDeviceGroupRequest,
    ) -> main_models.DeleteFaceDeviceGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_face_device_group_with_options(request, runtime)

    async def delete_face_device_group_async(
        self,
        request: main_models.DeleteFaceDeviceGroupRequest,
    ) -> main_models.DeleteFaceDeviceGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_face_device_group_with_options_async(request, runtime)

    def delete_face_user_with_options(
        self,
        request: main_models.DeleteFaceUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFaceUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFaceUser',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFaceUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_face_user_with_options_async(
        self,
        request: main_models.DeleteFaceUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFaceUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFaceUser',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFaceUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_face_user(
        self,
        request: main_models.DeleteFaceUserRequest,
    ) -> main_models.DeleteFaceUserResponse:
        runtime = RuntimeOptions()
        return self.delete_face_user_with_options(request, runtime)

    async def delete_face_user_async(
        self,
        request: main_models.DeleteFaceUserRequest,
    ) -> main_models.DeleteFaceUserResponse:
        runtime = RuntimeOptions()
        return await self.delete_face_user_with_options_async(request, runtime)

    def delete_face_user_group_with_options(
        self,
        request: main_models.DeleteFaceUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFaceUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFaceUserGroup',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFaceUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_face_user_group_with_options_async(
        self,
        request: main_models.DeleteFaceUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFaceUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFaceUserGroup',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFaceUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_face_user_group(
        self,
        request: main_models.DeleteFaceUserGroupRequest,
    ) -> main_models.DeleteFaceUserGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_face_user_group_with_options(request, runtime)

    async def delete_face_user_group_async(
        self,
        request: main_models.DeleteFaceUserGroupRequest,
    ) -> main_models.DeleteFaceUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_face_user_group_with_options_async(request, runtime)

    def delete_face_user_group_and_device_group_relation_with_options(
        self,
        request: main_models.DeleteFaceUserGroupAndDeviceGroupRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFaceUserGroupAndDeviceGroupRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.control_id):
            query['ControlId'] = request.control_id
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFaceUserGroupAndDeviceGroupRelation',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFaceUserGroupAndDeviceGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_face_user_group_and_device_group_relation_with_options_async(
        self,
        request: main_models.DeleteFaceUserGroupAndDeviceGroupRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFaceUserGroupAndDeviceGroupRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.control_id):
            query['ControlId'] = request.control_id
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFaceUserGroupAndDeviceGroupRelation',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFaceUserGroupAndDeviceGroupRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_face_user_group_and_device_group_relation(
        self,
        request: main_models.DeleteFaceUserGroupAndDeviceGroupRelationRequest,
    ) -> main_models.DeleteFaceUserGroupAndDeviceGroupRelationResponse:
        runtime = RuntimeOptions()
        return self.delete_face_user_group_and_device_group_relation_with_options(request, runtime)

    async def delete_face_user_group_and_device_group_relation_async(
        self,
        request: main_models.DeleteFaceUserGroupAndDeviceGroupRelationRequest,
    ) -> main_models.DeleteFaceUserGroupAndDeviceGroupRelationResponse:
        runtime = RuntimeOptions()
        return await self.delete_face_user_group_and_device_group_relation_with_options_async(request, runtime)

    def delete_face_user_picture_with_options(
        self,
        request: main_models.DeleteFaceUserPictureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFaceUserPictureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.face_pic_md_5):
            query['FacePicMd5'] = request.face_pic_md_5
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFaceUserPicture',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFaceUserPictureResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_face_user_picture_with_options_async(
        self,
        request: main_models.DeleteFaceUserPictureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFaceUserPictureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.face_pic_md_5):
            query['FacePicMd5'] = request.face_pic_md_5
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFaceUserPicture',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFaceUserPictureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_face_user_picture(
        self,
        request: main_models.DeleteFaceUserPictureRequest,
    ) -> main_models.DeleteFaceUserPictureResponse:
        runtime = RuntimeOptions()
        return self.delete_face_user_picture_with_options(request, runtime)

    async def delete_face_user_picture_async(
        self,
        request: main_models.DeleteFaceUserPictureRequest,
    ) -> main_models.DeleteFaceUserPictureResponse:
        runtime = RuntimeOptions()
        return await self.delete_face_user_picture_with_options_async(request, runtime)

    def delete_gb_device_with_options(
        self,
        request: main_models.DeleteGbDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGbDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGbDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGbDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gb_device_with_options_async(
        self,
        request: main_models.DeleteGbDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGbDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGbDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGbDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gb_device(
        self,
        request: main_models.DeleteGbDeviceRequest,
    ) -> main_models.DeleteGbDeviceResponse:
        runtime = RuntimeOptions()
        return self.delete_gb_device_with_options(request, runtime)

    async def delete_gb_device_async(
        self,
        request: main_models.DeleteGbDeviceRequest,
    ) -> main_models.DeleteGbDeviceResponse:
        runtime = RuntimeOptions()
        return await self.delete_gb_device_with_options_async(request, runtime)

    def delete_local_file_upload_job_with_options(
        self,
        request: main_models.DeleteLocalFileUploadJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLocalFileUploadJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLocalFileUploadJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLocalFileUploadJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_local_file_upload_job_with_options_async(
        self,
        request: main_models.DeleteLocalFileUploadJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLocalFileUploadJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLocalFileUploadJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLocalFileUploadJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_local_file_upload_job(
        self,
        request: main_models.DeleteLocalFileUploadJobRequest,
    ) -> main_models.DeleteLocalFileUploadJobResponse:
        runtime = RuntimeOptions()
        return self.delete_local_file_upload_job_with_options(request, runtime)

    async def delete_local_file_upload_job_async(
        self,
        request: main_models.DeleteLocalFileUploadJobRequest,
    ) -> main_models.DeleteLocalFileUploadJobResponse:
        runtime = RuntimeOptions()
        return await self.delete_local_file_upload_job_with_options_async(request, runtime)

    def delete_picture_with_options(
        self,
        request: main_models.DeletePictureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePictureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.picture_id_list):
            query['PictureIdList'] = request.picture_id_list
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePicture',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePictureResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_picture_with_options_async(
        self,
        request: main_models.DeletePictureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePictureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.picture_id_list):
            query['PictureIdList'] = request.picture_id_list
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePicture',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePictureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_picture(
        self,
        request: main_models.DeletePictureRequest,
    ) -> main_models.DeletePictureResponse:
        runtime = RuntimeOptions()
        return self.delete_picture_with_options(request, runtime)

    async def delete_picture_async(
        self,
        request: main_models.DeletePictureRequest,
    ) -> main_models.DeletePictureResponse:
        runtime = RuntimeOptions()
        return await self.delete_picture_with_options_async(request, runtime)

    def delete_record_with_options(
        self,
        request: main_models.DeleteRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.file_name_list):
            query['FileNameList'] = request.file_name_list
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRecord',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_record_with_options_async(
        self,
        request: main_models.DeleteRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.file_name_list):
            query['FileNameList'] = request.file_name_list
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRecord',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_record(
        self,
        request: main_models.DeleteRecordRequest,
    ) -> main_models.DeleteRecordResponse:
        runtime = RuntimeOptions()
        return self.delete_record_with_options(request, runtime)

    async def delete_record_async(
        self,
        request: main_models.DeleteRecordRequest,
    ) -> main_models.DeleteRecordResponse:
        runtime = RuntimeOptions()
        return await self.delete_record_with_options_async(request, runtime)

    def delete_record_plan_with_options(
        self,
        request: main_models.DeleteRecordPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRecordPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRecordPlan',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRecordPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_record_plan_with_options_async(
        self,
        request: main_models.DeleteRecordPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRecordPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRecordPlan',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRecordPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_record_plan(
        self,
        request: main_models.DeleteRecordPlanRequest,
    ) -> main_models.DeleteRecordPlanResponse:
        runtime = RuntimeOptions()
        return self.delete_record_plan_with_options(request, runtime)

    async def delete_record_plan_async(
        self,
        request: main_models.DeleteRecordPlanRequest,
    ) -> main_models.DeleteRecordPlanResponse:
        runtime = RuntimeOptions()
        return await self.delete_record_plan_with_options_async(request, runtime)

    def delete_record_plan_device_with_options(
        self,
        request: main_models.DeleteRecordPlanDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRecordPlanDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRecordPlanDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRecordPlanDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_record_plan_device_with_options_async(
        self,
        request: main_models.DeleteRecordPlanDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRecordPlanDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRecordPlanDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRecordPlanDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_record_plan_device(
        self,
        request: main_models.DeleteRecordPlanDeviceRequest,
    ) -> main_models.DeleteRecordPlanDeviceResponse:
        runtime = RuntimeOptions()
        return self.delete_record_plan_device_with_options(request, runtime)

    async def delete_record_plan_device_async(
        self,
        request: main_models.DeleteRecordPlanDeviceRequest,
    ) -> main_models.DeleteRecordPlanDeviceResponse:
        runtime = RuntimeOptions()
        return await self.delete_record_plan_device_with_options_async(request, runtime)

    def delete_rtmp_device_with_options(
        self,
        request: main_models.DeleteRtmpDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRtmpDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRtmpDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRtmpDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rtmp_device_with_options_async(
        self,
        request: main_models.DeleteRtmpDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRtmpDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRtmpDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRtmpDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rtmp_device(
        self,
        request: main_models.DeleteRtmpDeviceRequest,
    ) -> main_models.DeleteRtmpDeviceResponse:
        runtime = RuntimeOptions()
        return self.delete_rtmp_device_with_options(request, runtime)

    async def delete_rtmp_device_async(
        self,
        request: main_models.DeleteRtmpDeviceRequest,
    ) -> main_models.DeleteRtmpDeviceResponse:
        runtime = RuntimeOptions()
        return await self.delete_rtmp_device_with_options_async(request, runtime)

    def delete_rtmp_key_with_options(
        self,
        request: main_models.DeleteRtmpKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRtmpKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRtmpKey',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRtmpKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rtmp_key_with_options_async(
        self,
        request: main_models.DeleteRtmpKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRtmpKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRtmpKey',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRtmpKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rtmp_key(
        self,
        request: main_models.DeleteRtmpKeyRequest,
    ) -> main_models.DeleteRtmpKeyResponse:
        runtime = RuntimeOptions()
        return self.delete_rtmp_key_with_options(request, runtime)

    async def delete_rtmp_key_async(
        self,
        request: main_models.DeleteRtmpKeyRequest,
    ) -> main_models.DeleteRtmpKeyResponse:
        runtime = RuntimeOptions()
        return await self.delete_rtmp_key_with_options_async(request, runtime)

    def delete_stream_push_job_with_options(
        self,
        request: main_models.DeleteStreamPushJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStreamPushJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStreamPushJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStreamPushJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_stream_push_job_with_options_async(
        self,
        request: main_models.DeleteStreamPushJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStreamPushJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStreamPushJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStreamPushJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_stream_push_job(
        self,
        request: main_models.DeleteStreamPushJobRequest,
    ) -> main_models.DeleteStreamPushJobResponse:
        runtime = RuntimeOptions()
        return self.delete_stream_push_job_with_options(request, runtime)

    async def delete_stream_push_job_async(
        self,
        request: main_models.DeleteStreamPushJobRequest,
    ) -> main_models.DeleteStreamPushJobResponse:
        runtime = RuntimeOptions()
        return await self.delete_stream_push_job_with_options_async(request, runtime)

    def delete_stream_snapshot_job_with_options(
        self,
        request: main_models.DeleteStreamSnapshotJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStreamSnapshotJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStreamSnapshotJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStreamSnapshotJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_stream_snapshot_job_with_options_async(
        self,
        request: main_models.DeleteStreamSnapshotJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStreamSnapshotJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStreamSnapshotJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStreamSnapshotJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_stream_snapshot_job(
        self,
        request: main_models.DeleteStreamSnapshotJobRequest,
    ) -> main_models.DeleteStreamSnapshotJobResponse:
        runtime = RuntimeOptions()
        return self.delete_stream_snapshot_job_with_options(request, runtime)

    async def delete_stream_snapshot_job_async(
        self,
        request: main_models.DeleteStreamSnapshotJobRequest,
    ) -> main_models.DeleteStreamSnapshotJobResponse:
        runtime = RuntimeOptions()
        return await self.delete_stream_snapshot_job_with_options_async(request, runtime)

    def delete_time_template_with_options(
        self,
        request: main_models.DeleteTimeTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTimeTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTimeTemplate',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTimeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_time_template_with_options_async(
        self,
        request: main_models.DeleteTimeTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTimeTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTimeTemplate',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTimeTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_time_template(
        self,
        request: main_models.DeleteTimeTemplateRequest,
    ) -> main_models.DeleteTimeTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_time_template_with_options(request, runtime)

    async def delete_time_template_async(
        self,
        request: main_models.DeleteTimeTemplateRequest,
    ) -> main_models.DeleteTimeTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_time_template_with_options_async(request, runtime)

    def enable_gb_sub_device_with_options(
        self,
        request: main_models.EnableGbSubDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableGbSubDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.sub_device_id):
            query['SubDeviceId'] = request.sub_device_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableGbSubDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableGbSubDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_gb_sub_device_with_options_async(
        self,
        request: main_models.EnableGbSubDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableGbSubDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.sub_device_id):
            query['SubDeviceId'] = request.sub_device_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableGbSubDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableGbSubDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_gb_sub_device(
        self,
        request: main_models.EnableGbSubDeviceRequest,
    ) -> main_models.EnableGbSubDeviceResponse:
        runtime = RuntimeOptions()
        return self.enable_gb_sub_device_with_options(request, runtime)

    async def enable_gb_sub_device_async(
        self,
        request: main_models.EnableGbSubDeviceRequest,
    ) -> main_models.EnableGbSubDeviceResponse:
        runtime = RuntimeOptions()
        return await self.enable_gb_sub_device_with_options_async(request, runtime)

    def get_picture_search_job_status_with_options(
        self,
        request: main_models.GetPictureSearchJobStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPictureSearchJobStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPictureSearchJobStatus',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPictureSearchJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_picture_search_job_status_with_options_async(
        self,
        request: main_models.GetPictureSearchJobStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPictureSearchJobStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPictureSearchJobStatus',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPictureSearchJobStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_picture_search_job_status(
        self,
        request: main_models.GetPictureSearchJobStatusRequest,
    ) -> main_models.GetPictureSearchJobStatusResponse:
        runtime = RuntimeOptions()
        return self.get_picture_search_job_status_with_options(request, runtime)

    async def get_picture_search_job_status_async(
        self,
        request: main_models.GetPictureSearchJobStatusRequest,
    ) -> main_models.GetPictureSearchJobStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_picture_search_job_status_with_options_async(request, runtime)

    def picture_search_picture_with_options(
        self,
        request: main_models.PictureSearchPictureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PictureSearchPictureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.contain_pic_url):
            query['ContainPicUrl'] = request.contain_pic_url
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.picture_search_type):
            query['PictureSearchType'] = request.picture_search_type
        if not DaraCore.is_null(request.search_pic_url):
            query['SearchPicUrl'] = request.search_pic_url
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PictureSearchPicture',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PictureSearchPictureResponse(),
            self.call_api(params, req, runtime)
        )

    async def picture_search_picture_with_options_async(
        self,
        request: main_models.PictureSearchPictureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PictureSearchPictureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.contain_pic_url):
            query['ContainPicUrl'] = request.contain_pic_url
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.picture_search_type):
            query['PictureSearchType'] = request.picture_search_type
        if not DaraCore.is_null(request.search_pic_url):
            query['SearchPicUrl'] = request.search_pic_url
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PictureSearchPicture',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PictureSearchPictureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def picture_search_picture(
        self,
        request: main_models.PictureSearchPictureRequest,
    ) -> main_models.PictureSearchPictureResponse:
        runtime = RuntimeOptions()
        return self.picture_search_picture_with_options(request, runtime)

    async def picture_search_picture_async(
        self,
        request: main_models.PictureSearchPictureRequest,
    ) -> main_models.PictureSearchPictureResponse:
        runtime = RuntimeOptions()
        return await self.picture_search_picture_with_options_async(request, runtime)

    def query_car_process_events_with_options(
        self,
        request: main_models.QueryCarProcessEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCarProcessEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_type):
            query['ActionType'] = request.action_type
        if not DaraCore.is_null(request.area_index):
            query['AreaIndex'] = request.area_index
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.plate_no):
            query['PlateNo'] = request.plate_no
        if not DaraCore.is_null(request.sub_device_name):
            query['SubDeviceName'] = request.sub_device_name
        if not DaraCore.is_null(request.sub_iot_id):
            query['SubIotId'] = request.sub_iot_id
        if not DaraCore.is_null(request.sub_product_key):
            query['SubProductKey'] = request.sub_product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCarProcessEvents',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCarProcessEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_car_process_events_with_options_async(
        self,
        request: main_models.QueryCarProcessEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCarProcessEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_type):
            query['ActionType'] = request.action_type
        if not DaraCore.is_null(request.area_index):
            query['AreaIndex'] = request.area_index
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.plate_no):
            query['PlateNo'] = request.plate_no
        if not DaraCore.is_null(request.sub_device_name):
            query['SubDeviceName'] = request.sub_device_name
        if not DaraCore.is_null(request.sub_iot_id):
            query['SubIotId'] = request.sub_iot_id
        if not DaraCore.is_null(request.sub_product_key):
            query['SubProductKey'] = request.sub_product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCarProcessEvents',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCarProcessEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_car_process_events(
        self,
        request: main_models.QueryCarProcessEventsRequest,
    ) -> main_models.QueryCarProcessEventsResponse:
        runtime = RuntimeOptions()
        return self.query_car_process_events_with_options(request, runtime)

    async def query_car_process_events_async(
        self,
        request: main_models.QueryCarProcessEventsRequest,
    ) -> main_models.QueryCarProcessEventsResponse:
        runtime = RuntimeOptions()
        return await self.query_car_process_events_with_options_async(request, runtime)

    def query_device_event_with_options(
        self,
        request: main_models.QueryDeviceEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDeviceEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDeviceEvent',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDeviceEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_event_with_options_async(
        self,
        request: main_models.QueryDeviceEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDeviceEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDeviceEvent',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDeviceEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_device_event(
        self,
        request: main_models.QueryDeviceEventRequest,
    ) -> main_models.QueryDeviceEventResponse:
        runtime = RuntimeOptions()
        return self.query_device_event_with_options(request, runtime)

    async def query_device_event_async(
        self,
        request: main_models.QueryDeviceEventRequest,
    ) -> main_models.QueryDeviceEventResponse:
        runtime = RuntimeOptions()
        return await self.query_device_event_with_options_async(request, runtime)

    def query_device_event_picture_with_options(
        self,
        request: main_models.QueryDeviceEventPictureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDeviceEventPictureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDeviceEventPicture',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDeviceEventPictureResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_event_picture_with_options_async(
        self,
        request: main_models.QueryDeviceEventPictureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDeviceEventPictureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDeviceEventPicture',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDeviceEventPictureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_device_event_picture(
        self,
        request: main_models.QueryDeviceEventPictureRequest,
    ) -> main_models.QueryDeviceEventPictureResponse:
        runtime = RuntimeOptions()
        return self.query_device_event_picture_with_options(request, runtime)

    async def query_device_event_picture_async(
        self,
        request: main_models.QueryDeviceEventPictureRequest,
    ) -> main_models.QueryDeviceEventPictureResponse:
        runtime = RuntimeOptions()
        return await self.query_device_event_picture_with_options_async(request, runtime)

    def query_device_event_record_with_options(
        self,
        request: main_models.QueryDeviceEventRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDeviceEventRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDeviceEventRecord',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDeviceEventRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_event_record_with_options_async(
        self,
        request: main_models.QueryDeviceEventRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDeviceEventRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDeviceEventRecord',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDeviceEventRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_device_event_record(
        self,
        request: main_models.QueryDeviceEventRecordRequest,
    ) -> main_models.QueryDeviceEventRecordResponse:
        runtime = RuntimeOptions()
        return self.query_device_event_record_with_options(request, runtime)

    async def query_device_event_record_async(
        self,
        request: main_models.QueryDeviceEventRecordRequest,
    ) -> main_models.QueryDeviceEventRecordResponse:
        runtime = RuntimeOptions()
        return await self.query_device_event_record_with_options_async(request, runtime)

    def query_device_picture_by_list_with_options(
        self,
        request: main_models.QueryDevicePictureByListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDevicePictureByListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.picture_id_list):
            query['PictureIdList'] = request.picture_id_list
        if not DaraCore.is_null(request.picture_type):
            query['PictureType'] = request.picture_type
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.thumb_width):
            query['ThumbWidth'] = request.thumb_width
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDevicePictureByList',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDevicePictureByListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_picture_by_list_with_options_async(
        self,
        request: main_models.QueryDevicePictureByListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDevicePictureByListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.picture_id_list):
            query['PictureIdList'] = request.picture_id_list
        if not DaraCore.is_null(request.picture_type):
            query['PictureType'] = request.picture_type
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.thumb_width):
            query['ThumbWidth'] = request.thumb_width
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDevicePictureByList',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDevicePictureByListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_device_picture_by_list(
        self,
        request: main_models.QueryDevicePictureByListRequest,
    ) -> main_models.QueryDevicePictureByListResponse:
        runtime = RuntimeOptions()
        return self.query_device_picture_by_list_with_options(request, runtime)

    async def query_device_picture_by_list_async(
        self,
        request: main_models.QueryDevicePictureByListRequest,
    ) -> main_models.QueryDevicePictureByListResponse:
        runtime = RuntimeOptions()
        return await self.query_device_picture_by_list_with_options_async(request, runtime)

    def query_device_picture_file_with_options(
        self,
        request: main_models.QueryDevicePictureFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDevicePictureFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.capture_id):
            query['CaptureId'] = request.capture_id
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.picture_type):
            query['PictureType'] = request.picture_type
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.thumb_width):
            query['ThumbWidth'] = request.thumb_width
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDevicePictureFile',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDevicePictureFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_picture_file_with_options_async(
        self,
        request: main_models.QueryDevicePictureFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDevicePictureFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.capture_id):
            query['CaptureId'] = request.capture_id
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.picture_type):
            query['PictureType'] = request.picture_type
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.thumb_width):
            query['ThumbWidth'] = request.thumb_width
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDevicePictureFile',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDevicePictureFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_device_picture_file(
        self,
        request: main_models.QueryDevicePictureFileRequest,
    ) -> main_models.QueryDevicePictureFileResponse:
        runtime = RuntimeOptions()
        return self.query_device_picture_file_with_options(request, runtime)

    async def query_device_picture_file_async(
        self,
        request: main_models.QueryDevicePictureFileRequest,
    ) -> main_models.QueryDevicePictureFileResponse:
        runtime = RuntimeOptions()
        return await self.query_device_picture_file_with_options_async(request, runtime)

    def query_device_picture_life_cycle_with_options(
        self,
        request: main_models.QueryDevicePictureLifeCycleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDevicePictureLifeCycleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDevicePictureLifeCycle',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDevicePictureLifeCycleResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_picture_life_cycle_with_options_async(
        self,
        request: main_models.QueryDevicePictureLifeCycleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDevicePictureLifeCycleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDevicePictureLifeCycle',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDevicePictureLifeCycleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_device_picture_life_cycle(
        self,
        request: main_models.QueryDevicePictureLifeCycleRequest,
    ) -> main_models.QueryDevicePictureLifeCycleResponse:
        runtime = RuntimeOptions()
        return self.query_device_picture_life_cycle_with_options(request, runtime)

    async def query_device_picture_life_cycle_async(
        self,
        request: main_models.QueryDevicePictureLifeCycleRequest,
    ) -> main_models.QueryDevicePictureLifeCycleResponse:
        runtime = RuntimeOptions()
        return await self.query_device_picture_life_cycle_with_options_async(request, runtime)

    def query_device_record_life_cycle_with_options(
        self,
        request: main_models.QueryDeviceRecordLifeCycleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDeviceRecordLifeCycleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_list):
            query['DeviceList'] = request.device_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDeviceRecordLifeCycle',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDeviceRecordLifeCycleResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_record_life_cycle_with_options_async(
        self,
        request: main_models.QueryDeviceRecordLifeCycleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDeviceRecordLifeCycleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_list):
            query['DeviceList'] = request.device_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDeviceRecordLifeCycle',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDeviceRecordLifeCycleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_device_record_life_cycle(
        self,
        request: main_models.QueryDeviceRecordLifeCycleRequest,
    ) -> main_models.QueryDeviceRecordLifeCycleResponse:
        runtime = RuntimeOptions()
        return self.query_device_record_life_cycle_with_options(request, runtime)

    async def query_device_record_life_cycle_async(
        self,
        request: main_models.QueryDeviceRecordLifeCycleRequest,
    ) -> main_models.QueryDeviceRecordLifeCycleResponse:
        runtime = RuntimeOptions()
        return await self.query_device_record_life_cycle_with_options_async(request, runtime)

    def query_device_vod_url_with_options(
        self,
        request: main_models.QueryDeviceVodUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDeviceVodUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.enable_stun):
            query['EnableStun'] = request.enable_stun
        if not DaraCore.is_null(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.play_un_limited):
            query['PlayUnLimited'] = request.play_un_limited
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.scheme):
            query['Scheme'] = request.scheme
        if not DaraCore.is_null(request.seek_time):
            query['SeekTime'] = request.seek_time
        if not DaraCore.is_null(request.should_encrypt):
            query['ShouldEncrypt'] = request.should_encrypt
        if not DaraCore.is_null(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDeviceVodUrl',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDeviceVodUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_vod_url_with_options_async(
        self,
        request: main_models.QueryDeviceVodUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDeviceVodUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.enable_stun):
            query['EnableStun'] = request.enable_stun
        if not DaraCore.is_null(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.play_un_limited):
            query['PlayUnLimited'] = request.play_un_limited
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.scheme):
            query['Scheme'] = request.scheme
        if not DaraCore.is_null(request.seek_time):
            query['SeekTime'] = request.seek_time
        if not DaraCore.is_null(request.should_encrypt):
            query['ShouldEncrypt'] = request.should_encrypt
        if not DaraCore.is_null(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDeviceVodUrl',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDeviceVodUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_device_vod_url(
        self,
        request: main_models.QueryDeviceVodUrlRequest,
    ) -> main_models.QueryDeviceVodUrlResponse:
        runtime = RuntimeOptions()
        return self.query_device_vod_url_with_options(request, runtime)

    async def query_device_vod_url_async(
        self,
        request: main_models.QueryDeviceVodUrlRequest,
    ) -> main_models.QueryDeviceVodUrlResponse:
        runtime = RuntimeOptions()
        return await self.query_device_vod_url_with_options_async(request, runtime)

    def query_device_vod_url_by_time_with_options(
        self,
        request: main_models.QueryDeviceVodUrlByTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDeviceVodUrlByTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.enable_stun):
            query['EnableStun'] = request.enable_stun
        if not DaraCore.is_null(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.play_un_limited):
            query['PlayUnLimited'] = request.play_un_limited
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.scheme):
            query['Scheme'] = request.scheme
        if not DaraCore.is_null(request.seek_time):
            query['SeekTime'] = request.seek_time
        if not DaraCore.is_null(request.should_encrypt):
            query['ShouldEncrypt'] = request.should_encrypt
        if not DaraCore.is_null(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDeviceVodUrlByTime',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDeviceVodUrlByTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_vod_url_by_time_with_options_async(
        self,
        request: main_models.QueryDeviceVodUrlByTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDeviceVodUrlByTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.enable_stun):
            query['EnableStun'] = request.enable_stun
        if not DaraCore.is_null(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.play_un_limited):
            query['PlayUnLimited'] = request.play_un_limited
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.scheme):
            query['Scheme'] = request.scheme
        if not DaraCore.is_null(request.seek_time):
            query['SeekTime'] = request.seek_time
        if not DaraCore.is_null(request.should_encrypt):
            query['ShouldEncrypt'] = request.should_encrypt
        if not DaraCore.is_null(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDeviceVodUrlByTime',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDeviceVodUrlByTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_device_vod_url_by_time(
        self,
        request: main_models.QueryDeviceVodUrlByTimeRequest,
    ) -> main_models.QueryDeviceVodUrlByTimeResponse:
        runtime = RuntimeOptions()
        return self.query_device_vod_url_by_time_with_options(request, runtime)

    async def query_device_vod_url_by_time_async(
        self,
        request: main_models.QueryDeviceVodUrlByTimeRequest,
    ) -> main_models.QueryDeviceVodUrlByTimeResponse:
        runtime = RuntimeOptions()
        return await self.query_device_vod_url_by_time_with_options_async(request, runtime)

    def query_event_record_plan_detail_with_options(
        self,
        request: main_models.QueryEventRecordPlanDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEventRecordPlanDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEventRecordPlanDetail',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEventRecordPlanDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_event_record_plan_detail_with_options_async(
        self,
        request: main_models.QueryEventRecordPlanDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEventRecordPlanDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEventRecordPlanDetail',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEventRecordPlanDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_event_record_plan_detail(
        self,
        request: main_models.QueryEventRecordPlanDetailRequest,
    ) -> main_models.QueryEventRecordPlanDetailResponse:
        runtime = RuntimeOptions()
        return self.query_event_record_plan_detail_with_options(request, runtime)

    async def query_event_record_plan_detail_async(
        self,
        request: main_models.QueryEventRecordPlanDetailRequest,
    ) -> main_models.QueryEventRecordPlanDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_event_record_plan_detail_with_options_async(request, runtime)

    def query_event_record_plan_device_by_device_with_options(
        self,
        request: main_models.QueryEventRecordPlanDeviceByDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEventRecordPlanDeviceByDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEventRecordPlanDeviceByDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEventRecordPlanDeviceByDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_event_record_plan_device_by_device_with_options_async(
        self,
        request: main_models.QueryEventRecordPlanDeviceByDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEventRecordPlanDeviceByDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEventRecordPlanDeviceByDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEventRecordPlanDeviceByDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_event_record_plan_device_by_device(
        self,
        request: main_models.QueryEventRecordPlanDeviceByDeviceRequest,
    ) -> main_models.QueryEventRecordPlanDeviceByDeviceResponse:
        runtime = RuntimeOptions()
        return self.query_event_record_plan_device_by_device_with_options(request, runtime)

    async def query_event_record_plan_device_by_device_async(
        self,
        request: main_models.QueryEventRecordPlanDeviceByDeviceRequest,
    ) -> main_models.QueryEventRecordPlanDeviceByDeviceResponse:
        runtime = RuntimeOptions()
        return await self.query_event_record_plan_device_by_device_with_options_async(request, runtime)

    def query_event_record_plan_device_by_plan_with_options(
        self,
        request: main_models.QueryEventRecordPlanDeviceByPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEventRecordPlanDeviceByPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEventRecordPlanDeviceByPlan',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEventRecordPlanDeviceByPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_event_record_plan_device_by_plan_with_options_async(
        self,
        request: main_models.QueryEventRecordPlanDeviceByPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEventRecordPlanDeviceByPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEventRecordPlanDeviceByPlan',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEventRecordPlanDeviceByPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_event_record_plan_device_by_plan(
        self,
        request: main_models.QueryEventRecordPlanDeviceByPlanRequest,
    ) -> main_models.QueryEventRecordPlanDeviceByPlanResponse:
        runtime = RuntimeOptions()
        return self.query_event_record_plan_device_by_plan_with_options(request, runtime)

    async def query_event_record_plan_device_by_plan_async(
        self,
        request: main_models.QueryEventRecordPlanDeviceByPlanRequest,
    ) -> main_models.QueryEventRecordPlanDeviceByPlanResponse:
        runtime = RuntimeOptions()
        return await self.query_event_record_plan_device_by_plan_with_options_async(request, runtime)

    def query_event_record_plans_with_options(
        self,
        request: main_models.QueryEventRecordPlansRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEventRecordPlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEventRecordPlans',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEventRecordPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_event_record_plans_with_options_async(
        self,
        request: main_models.QueryEventRecordPlansRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEventRecordPlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEventRecordPlans',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEventRecordPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_event_record_plans(
        self,
        request: main_models.QueryEventRecordPlansRequest,
    ) -> main_models.QueryEventRecordPlansResponse:
        runtime = RuntimeOptions()
        return self.query_event_record_plans_with_options(request, runtime)

    async def query_event_record_plans_async(
        self,
        request: main_models.QueryEventRecordPlansRequest,
    ) -> main_models.QueryEventRecordPlansResponse:
        runtime = RuntimeOptions()
        return await self.query_event_record_plans_with_options_async(request, runtime)

    def query_face_all_device_group_with_options(
        self,
        request: main_models.QueryFaceAllDeviceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceAllDeviceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceAllDeviceGroup',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceAllDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_all_device_group_with_options_async(
        self,
        request: main_models.QueryFaceAllDeviceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceAllDeviceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceAllDeviceGroup',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceAllDeviceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_face_all_device_group(
        self,
        request: main_models.QueryFaceAllDeviceGroupRequest,
    ) -> main_models.QueryFaceAllDeviceGroupResponse:
        runtime = RuntimeOptions()
        return self.query_face_all_device_group_with_options(request, runtime)

    async def query_face_all_device_group_async(
        self,
        request: main_models.QueryFaceAllDeviceGroupRequest,
    ) -> main_models.QueryFaceAllDeviceGroupResponse:
        runtime = RuntimeOptions()
        return await self.query_face_all_device_group_with_options_async(request, runtime)

    def query_face_all_user_group_with_options(
        self,
        request: main_models.QueryFaceAllUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceAllUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceAllUserGroup',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceAllUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_all_user_group_with_options_async(
        self,
        request: main_models.QueryFaceAllUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceAllUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceAllUserGroup',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceAllUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_face_all_user_group(
        self,
        request: main_models.QueryFaceAllUserGroupRequest,
    ) -> main_models.QueryFaceAllUserGroupResponse:
        runtime = RuntimeOptions()
        return self.query_face_all_user_group_with_options(request, runtime)

    async def query_face_all_user_group_async(
        self,
        request: main_models.QueryFaceAllUserGroupRequest,
    ) -> main_models.QueryFaceAllUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.query_face_all_user_group_with_options_async(request, runtime)

    def query_face_all_user_group_and_device_group_relation_with_options(
        self,
        request: main_models.QueryFaceAllUserGroupAndDeviceGroupRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceAllUserGroupAndDeviceGroupRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceAllUserGroupAndDeviceGroupRelation',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceAllUserGroupAndDeviceGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_all_user_group_and_device_group_relation_with_options_async(
        self,
        request: main_models.QueryFaceAllUserGroupAndDeviceGroupRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceAllUserGroupAndDeviceGroupRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceAllUserGroupAndDeviceGroupRelation',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceAllUserGroupAndDeviceGroupRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_face_all_user_group_and_device_group_relation(
        self,
        request: main_models.QueryFaceAllUserGroupAndDeviceGroupRelationRequest,
    ) -> main_models.QueryFaceAllUserGroupAndDeviceGroupRelationResponse:
        runtime = RuntimeOptions()
        return self.query_face_all_user_group_and_device_group_relation_with_options(request, runtime)

    async def query_face_all_user_group_and_device_group_relation_async(
        self,
        request: main_models.QueryFaceAllUserGroupAndDeviceGroupRelationRequest,
    ) -> main_models.QueryFaceAllUserGroupAndDeviceGroupRelationResponse:
        runtime = RuntimeOptions()
        return await self.query_face_all_user_group_and_device_group_relation_with_options_async(request, runtime)

    def query_face_all_user_ids_by_group_id_with_options(
        self,
        request: main_models.QueryFaceAllUserIdsByGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceAllUserIdsByGroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceAllUserIdsByGroupId',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceAllUserIdsByGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_all_user_ids_by_group_id_with_options_async(
        self,
        request: main_models.QueryFaceAllUserIdsByGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceAllUserIdsByGroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceAllUserIdsByGroupId',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceAllUserIdsByGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_face_all_user_ids_by_group_id(
        self,
        request: main_models.QueryFaceAllUserIdsByGroupIdRequest,
    ) -> main_models.QueryFaceAllUserIdsByGroupIdResponse:
        runtime = RuntimeOptions()
        return self.query_face_all_user_ids_by_group_id_with_options(request, runtime)

    async def query_face_all_user_ids_by_group_id_async(
        self,
        request: main_models.QueryFaceAllUserIdsByGroupIdRequest,
    ) -> main_models.QueryFaceAllUserIdsByGroupIdResponse:
        runtime = RuntimeOptions()
        return await self.query_face_all_user_ids_by_group_id_with_options_async(request, runtime)

    def query_face_custom_user_id_by_user_id_with_options(
        self,
        request: main_models.QueryFaceCustomUserIdByUserIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceCustomUserIdByUserIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceCustomUserIdByUserId',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceCustomUserIdByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_custom_user_id_by_user_id_with_options_async(
        self,
        request: main_models.QueryFaceCustomUserIdByUserIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceCustomUserIdByUserIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceCustomUserIdByUserId',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceCustomUserIdByUserIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_face_custom_user_id_by_user_id(
        self,
        request: main_models.QueryFaceCustomUserIdByUserIdRequest,
    ) -> main_models.QueryFaceCustomUserIdByUserIdResponse:
        runtime = RuntimeOptions()
        return self.query_face_custom_user_id_by_user_id_with_options(request, runtime)

    async def query_face_custom_user_id_by_user_id_async(
        self,
        request: main_models.QueryFaceCustomUserIdByUserIdRequest,
    ) -> main_models.QueryFaceCustomUserIdByUserIdResponse:
        runtime = RuntimeOptions()
        return await self.query_face_custom_user_id_by_user_id_with_options_async(request, runtime)

    def query_face_device_groups_by_device_with_options(
        self,
        request: main_models.QueryFaceDeviceGroupsByDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceDeviceGroupsByDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceDeviceGroupsByDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceDeviceGroupsByDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_device_groups_by_device_with_options_async(
        self,
        request: main_models.QueryFaceDeviceGroupsByDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceDeviceGroupsByDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceDeviceGroupsByDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceDeviceGroupsByDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_face_device_groups_by_device(
        self,
        request: main_models.QueryFaceDeviceGroupsByDeviceRequest,
    ) -> main_models.QueryFaceDeviceGroupsByDeviceResponse:
        runtime = RuntimeOptions()
        return self.query_face_device_groups_by_device_with_options(request, runtime)

    async def query_face_device_groups_by_device_async(
        self,
        request: main_models.QueryFaceDeviceGroupsByDeviceRequest,
    ) -> main_models.QueryFaceDeviceGroupsByDeviceResponse:
        runtime = RuntimeOptions()
        return await self.query_face_device_groups_by_device_with_options_async(request, runtime)

    def query_face_user_with_options(
        self,
        request: main_models.QueryFaceUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceUser',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_user_with_options_async(
        self,
        request: main_models.QueryFaceUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceUser',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_face_user(
        self,
        request: main_models.QueryFaceUserRequest,
    ) -> main_models.QueryFaceUserResponse:
        runtime = RuntimeOptions()
        return self.query_face_user_with_options(request, runtime)

    async def query_face_user_async(
        self,
        request: main_models.QueryFaceUserRequest,
    ) -> main_models.QueryFaceUserResponse:
        runtime = RuntimeOptions()
        return await self.query_face_user_with_options_async(request, runtime)

    def query_face_user_batch_with_options(
        self,
        request: main_models.QueryFaceUserBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceUserBatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceUserBatch',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceUserBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_user_batch_with_options_async(
        self,
        request: main_models.QueryFaceUserBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceUserBatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceUserBatch',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceUserBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_face_user_batch(
        self,
        request: main_models.QueryFaceUserBatchRequest,
    ) -> main_models.QueryFaceUserBatchResponse:
        runtime = RuntimeOptions()
        return self.query_face_user_batch_with_options(request, runtime)

    async def query_face_user_batch_async(
        self,
        request: main_models.QueryFaceUserBatchRequest,
    ) -> main_models.QueryFaceUserBatchResponse:
        runtime = RuntimeOptions()
        return await self.query_face_user_batch_with_options_async(request, runtime)

    def query_face_user_by_name_with_options(
        self,
        request: main_models.QueryFaceUserByNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceUserByNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceUserByName',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceUserByNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_user_by_name_with_options_async(
        self,
        request: main_models.QueryFaceUserByNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceUserByNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceUserByName',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceUserByNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_face_user_by_name(
        self,
        request: main_models.QueryFaceUserByNameRequest,
    ) -> main_models.QueryFaceUserByNameResponse:
        runtime = RuntimeOptions()
        return self.query_face_user_by_name_with_options(request, runtime)

    async def query_face_user_by_name_async(
        self,
        request: main_models.QueryFaceUserByNameRequest,
    ) -> main_models.QueryFaceUserByNameResponse:
        runtime = RuntimeOptions()
        return await self.query_face_user_by_name_with_options_async(request, runtime)

    def query_face_user_group_with_options(
        self,
        request: main_models.QueryFaceUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceUserGroup',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_user_group_with_options_async(
        self,
        request: main_models.QueryFaceUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceUserGroup',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_face_user_group(
        self,
        request: main_models.QueryFaceUserGroupRequest,
    ) -> main_models.QueryFaceUserGroupResponse:
        runtime = RuntimeOptions()
        return self.query_face_user_group_with_options(request, runtime)

    async def query_face_user_group_async(
        self,
        request: main_models.QueryFaceUserGroupRequest,
    ) -> main_models.QueryFaceUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.query_face_user_group_with_options_async(request, runtime)

    def query_face_user_group_and_device_group_relation_with_options(
        self,
        request: main_models.QueryFaceUserGroupAndDeviceGroupRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceUserGroupAndDeviceGroupRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.control_id):
            query['ControlId'] = request.control_id
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceUserGroupAndDeviceGroupRelation',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceUserGroupAndDeviceGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_user_group_and_device_group_relation_with_options_async(
        self,
        request: main_models.QueryFaceUserGroupAndDeviceGroupRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceUserGroupAndDeviceGroupRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.control_id):
            query['ControlId'] = request.control_id
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceUserGroupAndDeviceGroupRelation',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceUserGroupAndDeviceGroupRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_face_user_group_and_device_group_relation(
        self,
        request: main_models.QueryFaceUserGroupAndDeviceGroupRelationRequest,
    ) -> main_models.QueryFaceUserGroupAndDeviceGroupRelationResponse:
        runtime = RuntimeOptions()
        return self.query_face_user_group_and_device_group_relation_with_options(request, runtime)

    async def query_face_user_group_and_device_group_relation_async(
        self,
        request: main_models.QueryFaceUserGroupAndDeviceGroupRelationRequest,
    ) -> main_models.QueryFaceUserGroupAndDeviceGroupRelationResponse:
        runtime = RuntimeOptions()
        return await self.query_face_user_group_and_device_group_relation_with_options_async(request, runtime)

    def query_face_user_id_by_custom_user_id_with_options(
        self,
        request: main_models.QueryFaceUserIdByCustomUserIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceUserIdByCustomUserIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceUserIdByCustomUserId',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceUserIdByCustomUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_user_id_by_custom_user_id_with_options_async(
        self,
        request: main_models.QueryFaceUserIdByCustomUserIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFaceUserIdByCustomUserIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFaceUserIdByCustomUserId',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFaceUserIdByCustomUserIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_face_user_id_by_custom_user_id(
        self,
        request: main_models.QueryFaceUserIdByCustomUserIdRequest,
    ) -> main_models.QueryFaceUserIdByCustomUserIdResponse:
        runtime = RuntimeOptions()
        return self.query_face_user_id_by_custom_user_id_with_options(request, runtime)

    async def query_face_user_id_by_custom_user_id_async(
        self,
        request: main_models.QueryFaceUserIdByCustomUserIdRequest,
    ) -> main_models.QueryFaceUserIdByCustomUserIdResponse:
        runtime = RuntimeOptions()
        return await self.query_face_user_id_by_custom_user_id_with_options_async(request, runtime)

    def query_gb_sub_device_list_with_options(
        self,
        request: main_models.QueryGbSubDeviceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryGbSubDeviceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.page_start):
            query['PageStart'] = request.page_start
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryGbSubDeviceList',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryGbSubDeviceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_gb_sub_device_list_with_options_async(
        self,
        request: main_models.QueryGbSubDeviceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryGbSubDeviceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.page_start):
            query['PageStart'] = request.page_start
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryGbSubDeviceList',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryGbSubDeviceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_gb_sub_device_list(
        self,
        request: main_models.QueryGbSubDeviceListRequest,
    ) -> main_models.QueryGbSubDeviceListResponse:
        runtime = RuntimeOptions()
        return self.query_gb_sub_device_list_with_options(request, runtime)

    async def query_gb_sub_device_list_async(
        self,
        request: main_models.QueryGbSubDeviceListRequest,
    ) -> main_models.QueryGbSubDeviceListResponse:
        runtime = RuntimeOptions()
        return await self.query_gb_sub_device_list_with_options_async(request, runtime)

    def query_live_streaming_with_options(
        self,
        request: main_models.QueryLiveStreamingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryLiveStreamingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cache_duration):
            query['CacheDuration'] = request.cache_duration
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.enable_stun):
            query['EnableStun'] = request.enable_stun
        if not DaraCore.is_null(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not DaraCore.is_null(request.force_iframe):
            query['ForceIFrame'] = request.force_iframe
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.play_un_limited):
            query['PlayUnLimited'] = request.play_un_limited
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.scheme):
            query['Scheme'] = request.scheme
        if not DaraCore.is_null(request.should_encrypt):
            query['ShouldEncrypt'] = request.should_encrypt
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        if not DaraCore.is_null(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryLiveStreaming',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryLiveStreamingResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_live_streaming_with_options_async(
        self,
        request: main_models.QueryLiveStreamingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryLiveStreamingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cache_duration):
            query['CacheDuration'] = request.cache_duration
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.enable_stun):
            query['EnableStun'] = request.enable_stun
        if not DaraCore.is_null(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not DaraCore.is_null(request.force_iframe):
            query['ForceIFrame'] = request.force_iframe
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.play_un_limited):
            query['PlayUnLimited'] = request.play_un_limited
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.scheme):
            query['Scheme'] = request.scheme
        if not DaraCore.is_null(request.should_encrypt):
            query['ShouldEncrypt'] = request.should_encrypt
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        if not DaraCore.is_null(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryLiveStreaming',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryLiveStreamingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_live_streaming(
        self,
        request: main_models.QueryLiveStreamingRequest,
    ) -> main_models.QueryLiveStreamingResponse:
        runtime = RuntimeOptions()
        return self.query_live_streaming_with_options(request, runtime)

    async def query_live_streaming_async(
        self,
        request: main_models.QueryLiveStreamingRequest,
    ) -> main_models.QueryLiveStreamingResponse:
        runtime = RuntimeOptions()
        return await self.query_live_streaming_with_options_async(request, runtime)

    def query_local_file_upload_job_with_options(
        self,
        request: main_models.QueryLocalFileUploadJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryLocalFileUploadJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryLocalFileUploadJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryLocalFileUploadJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_local_file_upload_job_with_options_async(
        self,
        request: main_models.QueryLocalFileUploadJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryLocalFileUploadJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryLocalFileUploadJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryLocalFileUploadJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_local_file_upload_job(
        self,
        request: main_models.QueryLocalFileUploadJobRequest,
    ) -> main_models.QueryLocalFileUploadJobResponse:
        runtime = RuntimeOptions()
        return self.query_local_file_upload_job_with_options(request, runtime)

    async def query_local_file_upload_job_async(
        self,
        request: main_models.QueryLocalFileUploadJobRequest,
    ) -> main_models.QueryLocalFileUploadJobResponse:
        runtime = RuntimeOptions()
        return await self.query_local_file_upload_job_with_options_async(request, runtime)

    def query_month_record_with_options(
        self,
        request: main_models.QueryMonthRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMonthRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.month):
            query['Month'] = request.month
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMonthRecord',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMonthRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_month_record_with_options_async(
        self,
        request: main_models.QueryMonthRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMonthRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.month):
            query['Month'] = request.month
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMonthRecord',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMonthRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_month_record(
        self,
        request: main_models.QueryMonthRecordRequest,
    ) -> main_models.QueryMonthRecordResponse:
        runtime = RuntimeOptions()
        return self.query_month_record_with_options(request, runtime)

    async def query_month_record_async(
        self,
        request: main_models.QueryMonthRecordRequest,
    ) -> main_models.QueryMonthRecordResponse:
        runtime = RuntimeOptions()
        return await self.query_month_record_with_options_async(request, runtime)

    def query_picture_files_with_options(
        self,
        request: main_models.QueryPictureFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPictureFilesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.picture_source):
            query['PictureSource'] = request.picture_source
        if not DaraCore.is_null(request.picture_type):
            query['PictureType'] = request.picture_type
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPictureFiles',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPictureFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_picture_files_with_options_async(
        self,
        request: main_models.QueryPictureFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPictureFilesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.picture_source):
            query['PictureSource'] = request.picture_source
        if not DaraCore.is_null(request.picture_type):
            query['PictureType'] = request.picture_type
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPictureFiles',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPictureFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_picture_files(
        self,
        request: main_models.QueryPictureFilesRequest,
    ) -> main_models.QueryPictureFilesResponse:
        runtime = RuntimeOptions()
        return self.query_picture_files_with_options(request, runtime)

    async def query_picture_files_async(
        self,
        request: main_models.QueryPictureFilesRequest,
    ) -> main_models.QueryPictureFilesResponse:
        runtime = RuntimeOptions()
        return await self.query_picture_files_with_options_async(request, runtime)

    def query_picture_search_aiboxes_with_options(
        self,
        request: main_models.QueryPictureSearchAiboxesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPictureSearchAiboxesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPictureSearchAiboxes',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPictureSearchAiboxesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_picture_search_aiboxes_with_options_async(
        self,
        request: main_models.QueryPictureSearchAiboxesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPictureSearchAiboxesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPictureSearchAiboxes',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPictureSearchAiboxesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_picture_search_aiboxes(
        self,
        request: main_models.QueryPictureSearchAiboxesRequest,
    ) -> main_models.QueryPictureSearchAiboxesResponse:
        runtime = RuntimeOptions()
        return self.query_picture_search_aiboxes_with_options(request, runtime)

    async def query_picture_search_aiboxes_async(
        self,
        request: main_models.QueryPictureSearchAiboxesRequest,
    ) -> main_models.QueryPictureSearchAiboxesResponse:
        runtime = RuntimeOptions()
        return await self.query_picture_search_aiboxes_with_options_async(request, runtime)

    def query_picture_search_apps_with_options(
        self,
        request: main_models.QueryPictureSearchAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPictureSearchAppsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPictureSearchApps',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPictureSearchAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_picture_search_apps_with_options_async(
        self,
        request: main_models.QueryPictureSearchAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPictureSearchAppsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPictureSearchApps',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPictureSearchAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_picture_search_apps(
        self,
        request: main_models.QueryPictureSearchAppsRequest,
    ) -> main_models.QueryPictureSearchAppsResponse:
        runtime = RuntimeOptions()
        return self.query_picture_search_apps_with_options(request, runtime)

    async def query_picture_search_apps_async(
        self,
        request: main_models.QueryPictureSearchAppsRequest,
    ) -> main_models.QueryPictureSearchAppsResponse:
        runtime = RuntimeOptions()
        return await self.query_picture_search_apps_with_options_async(request, runtime)

    def query_picture_search_devices_with_options(
        self,
        request: main_models.QueryPictureSearchDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPictureSearchDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPictureSearchDevices',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPictureSearchDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_picture_search_devices_with_options_async(
        self,
        request: main_models.QueryPictureSearchDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPictureSearchDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPictureSearchDevices',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPictureSearchDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_picture_search_devices(
        self,
        request: main_models.QueryPictureSearchDevicesRequest,
    ) -> main_models.QueryPictureSearchDevicesResponse:
        runtime = RuntimeOptions()
        return self.query_picture_search_devices_with_options(request, runtime)

    async def query_picture_search_devices_async(
        self,
        request: main_models.QueryPictureSearchDevicesRequest,
    ) -> main_models.QueryPictureSearchDevicesResponse:
        runtime = RuntimeOptions()
        return await self.query_picture_search_devices_with_options_async(request, runtime)

    def query_picture_search_job_with_options(
        self,
        request: main_models.QueryPictureSearchJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPictureSearchJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.job_status):
            query['JobStatus'] = request.job_status
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPictureSearchJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPictureSearchJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_picture_search_job_with_options_async(
        self,
        request: main_models.QueryPictureSearchJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPictureSearchJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.job_status):
            query['JobStatus'] = request.job_status
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPictureSearchJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPictureSearchJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_picture_search_job(
        self,
        request: main_models.QueryPictureSearchJobRequest,
    ) -> main_models.QueryPictureSearchJobResponse:
        runtime = RuntimeOptions()
        return self.query_picture_search_job_with_options(request, runtime)

    async def query_picture_search_job_async(
        self,
        request: main_models.QueryPictureSearchJobRequest,
    ) -> main_models.QueryPictureSearchJobResponse:
        runtime = RuntimeOptions()
        return await self.query_picture_search_job_with_options_async(request, runtime)

    def query_picture_search_job_result_with_options(
        self,
        request: main_models.QueryPictureSearchJobResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPictureSearchJobResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPictureSearchJobResult',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPictureSearchJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_picture_search_job_result_with_options_async(
        self,
        request: main_models.QueryPictureSearchJobResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPictureSearchJobResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPictureSearchJobResult',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPictureSearchJobResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_picture_search_job_result(
        self,
        request: main_models.QueryPictureSearchJobResultRequest,
    ) -> main_models.QueryPictureSearchJobResultResponse:
        runtime = RuntimeOptions()
        return self.query_picture_search_job_result_with_options(request, runtime)

    async def query_picture_search_job_result_async(
        self,
        request: main_models.QueryPictureSearchJobResultRequest,
    ) -> main_models.QueryPictureSearchJobResultResponse:
        runtime = RuntimeOptions()
        return await self.query_picture_search_job_result_with_options_async(request, runtime)

    def query_record_with_options(
        self,
        request: main_models.QueryRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.need_snapshot):
            query['NeedSnapshot'] = request.need_snapshot
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.record_type):
            query['RecordType'] = request.record_type
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecord',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_record_with_options_async(
        self,
        request: main_models.QueryRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.need_snapshot):
            query['NeedSnapshot'] = request.need_snapshot
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.record_type):
            query['RecordType'] = request.record_type
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecord',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_record(
        self,
        request: main_models.QueryRecordRequest,
    ) -> main_models.QueryRecordResponse:
        runtime = RuntimeOptions()
        return self.query_record_with_options(request, runtime)

    async def query_record_async(
        self,
        request: main_models.QueryRecordRequest,
    ) -> main_models.QueryRecordResponse:
        runtime = RuntimeOptions()
        return await self.query_record_with_options_async(request, runtime)

    def query_record_by_record_id_with_options(
        self,
        request: main_models.QueryRecordByRecordIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecordByRecordIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecordByRecordId',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecordByRecordIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_record_by_record_id_with_options_async(
        self,
        request: main_models.QueryRecordByRecordIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecordByRecordIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecordByRecordId',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecordByRecordIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_record_by_record_id(
        self,
        request: main_models.QueryRecordByRecordIdRequest,
    ) -> main_models.QueryRecordByRecordIdResponse:
        runtime = RuntimeOptions()
        return self.query_record_by_record_id_with_options(request, runtime)

    async def query_record_by_record_id_async(
        self,
        request: main_models.QueryRecordByRecordIdRequest,
    ) -> main_models.QueryRecordByRecordIdResponse:
        runtime = RuntimeOptions()
        return await self.query_record_by_record_id_with_options_async(request, runtime)

    def query_record_download_job_by_id_with_options(
        self,
        request: main_models.QueryRecordDownloadJobByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecordDownloadJobByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecordDownloadJobById',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecordDownloadJobByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_record_download_job_by_id_with_options_async(
        self,
        request: main_models.QueryRecordDownloadJobByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecordDownloadJobByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecordDownloadJobById',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecordDownloadJobByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_record_download_job_by_id(
        self,
        request: main_models.QueryRecordDownloadJobByIdRequest,
    ) -> main_models.QueryRecordDownloadJobByIdResponse:
        runtime = RuntimeOptions()
        return self.query_record_download_job_by_id_with_options(request, runtime)

    async def query_record_download_job_by_id_async(
        self,
        request: main_models.QueryRecordDownloadJobByIdRequest,
    ) -> main_models.QueryRecordDownloadJobByIdResponse:
        runtime = RuntimeOptions()
        return await self.query_record_download_job_by_id_with_options_async(request, runtime)

    def query_record_download_job_list_with_options(
        self,
        request: main_models.QueryRecordDownloadJobListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecordDownloadJobListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecordDownloadJobList',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecordDownloadJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_record_download_job_list_with_options_async(
        self,
        request: main_models.QueryRecordDownloadJobListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecordDownloadJobListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecordDownloadJobList',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecordDownloadJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_record_download_job_list(
        self,
        request: main_models.QueryRecordDownloadJobListRequest,
    ) -> main_models.QueryRecordDownloadJobListResponse:
        runtime = RuntimeOptions()
        return self.query_record_download_job_list_with_options(request, runtime)

    async def query_record_download_job_list_async(
        self,
        request: main_models.QueryRecordDownloadJobListRequest,
    ) -> main_models.QueryRecordDownloadJobListResponse:
        runtime = RuntimeOptions()
        return await self.query_record_download_job_list_with_options_async(request, runtime)

    def query_record_download_url_with_options(
        self,
        request: main_models.QueryRecordDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecordDownloadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecordDownloadUrl',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecordDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_record_download_url_with_options_async(
        self,
        request: main_models.QueryRecordDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecordDownloadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecordDownloadUrl',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecordDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_record_download_url(
        self,
        request: main_models.QueryRecordDownloadUrlRequest,
    ) -> main_models.QueryRecordDownloadUrlResponse:
        runtime = RuntimeOptions()
        return self.query_record_download_url_with_options(request, runtime)

    async def query_record_download_url_async(
        self,
        request: main_models.QueryRecordDownloadUrlRequest,
    ) -> main_models.QueryRecordDownloadUrlResponse:
        runtime = RuntimeOptions()
        return await self.query_record_download_url_with_options_async(request, runtime)

    def query_record_plan_detail_with_options(
        self,
        request: main_models.QueryRecordPlanDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecordPlanDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecordPlanDetail',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecordPlanDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_record_plan_detail_with_options_async(
        self,
        request: main_models.QueryRecordPlanDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecordPlanDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecordPlanDetail',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecordPlanDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_record_plan_detail(
        self,
        request: main_models.QueryRecordPlanDetailRequest,
    ) -> main_models.QueryRecordPlanDetailResponse:
        runtime = RuntimeOptions()
        return self.query_record_plan_detail_with_options(request, runtime)

    async def query_record_plan_detail_async(
        self,
        request: main_models.QueryRecordPlanDetailRequest,
    ) -> main_models.QueryRecordPlanDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_record_plan_detail_with_options_async(request, runtime)

    def query_record_plan_device_by_device_with_options(
        self,
        request: main_models.QueryRecordPlanDeviceByDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecordPlanDeviceByDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecordPlanDeviceByDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecordPlanDeviceByDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_record_plan_device_by_device_with_options_async(
        self,
        request: main_models.QueryRecordPlanDeviceByDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecordPlanDeviceByDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecordPlanDeviceByDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecordPlanDeviceByDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_record_plan_device_by_device(
        self,
        request: main_models.QueryRecordPlanDeviceByDeviceRequest,
    ) -> main_models.QueryRecordPlanDeviceByDeviceResponse:
        runtime = RuntimeOptions()
        return self.query_record_plan_device_by_device_with_options(request, runtime)

    async def query_record_plan_device_by_device_async(
        self,
        request: main_models.QueryRecordPlanDeviceByDeviceRequest,
    ) -> main_models.QueryRecordPlanDeviceByDeviceResponse:
        runtime = RuntimeOptions()
        return await self.query_record_plan_device_by_device_with_options_async(request, runtime)

    def query_record_plan_device_by_plan_with_options(
        self,
        request: main_models.QueryRecordPlanDeviceByPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecordPlanDeviceByPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecordPlanDeviceByPlan',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecordPlanDeviceByPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_record_plan_device_by_plan_with_options_async(
        self,
        request: main_models.QueryRecordPlanDeviceByPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecordPlanDeviceByPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecordPlanDeviceByPlan',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecordPlanDeviceByPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_record_plan_device_by_plan(
        self,
        request: main_models.QueryRecordPlanDeviceByPlanRequest,
    ) -> main_models.QueryRecordPlanDeviceByPlanResponse:
        runtime = RuntimeOptions()
        return self.query_record_plan_device_by_plan_with_options(request, runtime)

    async def query_record_plan_device_by_plan_async(
        self,
        request: main_models.QueryRecordPlanDeviceByPlanRequest,
    ) -> main_models.QueryRecordPlanDeviceByPlanResponse:
        runtime = RuntimeOptions()
        return await self.query_record_plan_device_by_plan_with_options_async(request, runtime)

    def query_record_plans_with_options(
        self,
        request: main_models.QueryRecordPlansRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecordPlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecordPlans',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecordPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_record_plans_with_options_async(
        self,
        request: main_models.QueryRecordPlansRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecordPlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecordPlans',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecordPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_record_plans(
        self,
        request: main_models.QueryRecordPlansRequest,
    ) -> main_models.QueryRecordPlansResponse:
        runtime = RuntimeOptions()
        return self.query_record_plans_with_options(request, runtime)

    async def query_record_plans_async(
        self,
        request: main_models.QueryRecordPlansRequest,
    ) -> main_models.QueryRecordPlansResponse:
        runtime = RuntimeOptions()
        return await self.query_record_plans_with_options_async(request, runtime)

    def query_record_url_with_options(
        self,
        request: main_models.QueryRecordUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecordUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.seek_time):
            query['SeekTime'] = request.seek_time
        if not DaraCore.is_null(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecordUrl',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecordUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_record_url_with_options_async(
        self,
        request: main_models.QueryRecordUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecordUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.seek_time):
            query['SeekTime'] = request.seek_time
        if not DaraCore.is_null(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecordUrl',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecordUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_record_url(
        self,
        request: main_models.QueryRecordUrlRequest,
    ) -> main_models.QueryRecordUrlResponse:
        runtime = RuntimeOptions()
        return self.query_record_url_with_options(request, runtime)

    async def query_record_url_async(
        self,
        request: main_models.QueryRecordUrlRequest,
    ) -> main_models.QueryRecordUrlResponse:
        runtime = RuntimeOptions()
        return await self.query_record_url_with_options_async(request, runtime)

    def query_record_url_by_time_with_options(
        self,
        request: main_models.QueryRecordUrlByTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecordUrlByTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        if not DaraCore.is_null(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecordUrlByTime',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecordUrlByTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_record_url_by_time_with_options_async(
        self,
        request: main_models.QueryRecordUrlByTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecordUrlByTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        if not DaraCore.is_null(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecordUrlByTime',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecordUrlByTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_record_url_by_time(
        self,
        request: main_models.QueryRecordUrlByTimeRequest,
    ) -> main_models.QueryRecordUrlByTimeResponse:
        runtime = RuntimeOptions()
        return self.query_record_url_by_time_with_options(request, runtime)

    async def query_record_url_by_time_async(
        self,
        request: main_models.QueryRecordUrlByTimeRequest,
    ) -> main_models.QueryRecordUrlByTimeResponse:
        runtime = RuntimeOptions()
        return await self.query_record_url_by_time_with_options_async(request, runtime)

    def query_rtmp_key_with_options(
        self,
        request: main_models.QueryRtmpKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRtmpKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRtmpKey',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRtmpKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_rtmp_key_with_options_async(
        self,
        request: main_models.QueryRtmpKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRtmpKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRtmpKey',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRtmpKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_rtmp_key(
        self,
        request: main_models.QueryRtmpKeyRequest,
    ) -> main_models.QueryRtmpKeyResponse:
        runtime = RuntimeOptions()
        return self.query_rtmp_key_with_options(request, runtime)

    async def query_rtmp_key_async(
        self,
        request: main_models.QueryRtmpKeyRequest,
    ) -> main_models.QueryRtmpKeyResponse:
        runtime = RuntimeOptions()
        return await self.query_rtmp_key_with_options_async(request, runtime)

    def query_stream_push_job_with_options(
        self,
        request: main_models.QueryStreamPushJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryStreamPushJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryStreamPushJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryStreamPushJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_stream_push_job_with_options_async(
        self,
        request: main_models.QueryStreamPushJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryStreamPushJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryStreamPushJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryStreamPushJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_stream_push_job(
        self,
        request: main_models.QueryStreamPushJobRequest,
    ) -> main_models.QueryStreamPushJobResponse:
        runtime = RuntimeOptions()
        return self.query_stream_push_job_with_options(request, runtime)

    async def query_stream_push_job_async(
        self,
        request: main_models.QueryStreamPushJobRequest,
    ) -> main_models.QueryStreamPushJobResponse:
        runtime = RuntimeOptions()
        return await self.query_stream_push_job_with_options_async(request, runtime)

    def query_stream_push_job_list_with_options(
        self,
        request: main_models.QueryStreamPushJobListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryStreamPushJobListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryStreamPushJobList',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryStreamPushJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_stream_push_job_list_with_options_async(
        self,
        request: main_models.QueryStreamPushJobListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryStreamPushJobListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryStreamPushJobList',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryStreamPushJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_stream_push_job_list(
        self,
        request: main_models.QueryStreamPushJobListRequest,
    ) -> main_models.QueryStreamPushJobListResponse:
        runtime = RuntimeOptions()
        return self.query_stream_push_job_list_with_options(request, runtime)

    async def query_stream_push_job_list_async(
        self,
        request: main_models.QueryStreamPushJobListRequest,
    ) -> main_models.QueryStreamPushJobListResponse:
        runtime = RuntimeOptions()
        return await self.query_stream_push_job_list_with_options_async(request, runtime)

    def query_stream_snapshot_job_with_options(
        self,
        request: main_models.QueryStreamSnapshotJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryStreamSnapshotJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryStreamSnapshotJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryStreamSnapshotJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_stream_snapshot_job_with_options_async(
        self,
        request: main_models.QueryStreamSnapshotJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryStreamSnapshotJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryStreamSnapshotJob',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryStreamSnapshotJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_stream_snapshot_job(
        self,
        request: main_models.QueryStreamSnapshotJobRequest,
    ) -> main_models.QueryStreamSnapshotJobResponse:
        runtime = RuntimeOptions()
        return self.query_stream_snapshot_job_with_options(request, runtime)

    async def query_stream_snapshot_job_async(
        self,
        request: main_models.QueryStreamSnapshotJobRequest,
    ) -> main_models.QueryStreamSnapshotJobResponse:
        runtime = RuntimeOptions()
        return await self.query_stream_snapshot_job_with_options_async(request, runtime)

    def query_time_template_with_options(
        self,
        request: main_models.QueryTimeTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTimeTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTimeTemplate',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTimeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_time_template_with_options_async(
        self,
        request: main_models.QueryTimeTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTimeTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTimeTemplate',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTimeTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_time_template(
        self,
        request: main_models.QueryTimeTemplateRequest,
    ) -> main_models.QueryTimeTemplateResponse:
        runtime = RuntimeOptions()
        return self.query_time_template_with_options(request, runtime)

    async def query_time_template_async(
        self,
        request: main_models.QueryTimeTemplateRequest,
    ) -> main_models.QueryTimeTemplateResponse:
        runtime = RuntimeOptions()
        return await self.query_time_template_with_options_async(request, runtime)

    def query_time_template_detail_with_options(
        self,
        request: main_models.QueryTimeTemplateDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTimeTemplateDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTimeTemplateDetail',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTimeTemplateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_time_template_detail_with_options_async(
        self,
        request: main_models.QueryTimeTemplateDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTimeTemplateDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTimeTemplateDetail',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTimeTemplateDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_time_template_detail(
        self,
        request: main_models.QueryTimeTemplateDetailRequest,
    ) -> main_models.QueryTimeTemplateDetailResponse:
        runtime = RuntimeOptions()
        return self.query_time_template_detail_with_options(request, runtime)

    async def query_time_template_detail_async(
        self,
        request: main_models.QueryTimeTemplateDetailRequest,
    ) -> main_models.QueryTimeTemplateDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_time_template_detail_with_options_async(request, runtime)

    def query_vision_device_info_with_options(
        self,
        request: main_models.QueryVisionDeviceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryVisionDeviceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryVisionDeviceInfo',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryVisionDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_vision_device_info_with_options_async(
        self,
        request: main_models.QueryVisionDeviceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryVisionDeviceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryVisionDeviceInfo',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryVisionDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_vision_device_info(
        self,
        request: main_models.QueryVisionDeviceInfoRequest,
    ) -> main_models.QueryVisionDeviceInfoResponse:
        runtime = RuntimeOptions()
        return self.query_vision_device_info_with_options(request, runtime)

    async def query_vision_device_info_async(
        self,
        request: main_models.QueryVisionDeviceInfoRequest,
    ) -> main_models.QueryVisionDeviceInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_vision_device_info_with_options_async(request, runtime)

    def query_voice_intercom_with_options(
        self,
        request: main_models.QueryVoiceIntercomRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryVoiceIntercomResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.scheme):
            query['Scheme'] = request.scheme
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryVoiceIntercom',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryVoiceIntercomResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_voice_intercom_with_options_async(
        self,
        request: main_models.QueryVoiceIntercomRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryVoiceIntercomResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.scheme):
            query['Scheme'] = request.scheme
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryVoiceIntercom',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryVoiceIntercomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_voice_intercom(
        self,
        request: main_models.QueryVoiceIntercomRequest,
    ) -> main_models.QueryVoiceIntercomResponse:
        runtime = RuntimeOptions()
        return self.query_voice_intercom_with_options(request, runtime)

    async def query_voice_intercom_async(
        self,
        request: main_models.QueryVoiceIntercomRequest,
    ) -> main_models.QueryVoiceIntercomResponse:
        runtime = RuntimeOptions()
        return await self.query_voice_intercom_with_options_async(request, runtime)

    def refresh_gb_sub_device_list_with_options(
        self,
        request: main_models.RefreshGbSubDeviceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshGbSubDeviceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshGbSubDeviceList',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshGbSubDeviceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_gb_sub_device_list_with_options_async(
        self,
        request: main_models.RefreshGbSubDeviceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshGbSubDeviceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshGbSubDeviceList',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshGbSubDeviceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_gb_sub_device_list(
        self,
        request: main_models.RefreshGbSubDeviceListRequest,
    ) -> main_models.RefreshGbSubDeviceListResponse:
        runtime = RuntimeOptions()
        return self.refresh_gb_sub_device_list_with_options(request, runtime)

    async def refresh_gb_sub_device_list_async(
        self,
        request: main_models.RefreshGbSubDeviceListRequest,
    ) -> main_models.RefreshGbSubDeviceListResponse:
        runtime = RuntimeOptions()
        return await self.refresh_gb_sub_device_list_with_options_async(request, runtime)

    def remove_face_device_from_device_group_with_options(
        self,
        request: main_models.RemoveFaceDeviceFromDeviceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveFaceDeviceFromDeviceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveFaceDeviceFromDeviceGroup',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveFaceDeviceFromDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_face_device_from_device_group_with_options_async(
        self,
        request: main_models.RemoveFaceDeviceFromDeviceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveFaceDeviceFromDeviceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveFaceDeviceFromDeviceGroup',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveFaceDeviceFromDeviceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_face_device_from_device_group(
        self,
        request: main_models.RemoveFaceDeviceFromDeviceGroupRequest,
    ) -> main_models.RemoveFaceDeviceFromDeviceGroupResponse:
        runtime = RuntimeOptions()
        return self.remove_face_device_from_device_group_with_options(request, runtime)

    async def remove_face_device_from_device_group_async(
        self,
        request: main_models.RemoveFaceDeviceFromDeviceGroupRequest,
    ) -> main_models.RemoveFaceDeviceFromDeviceGroupResponse:
        runtime = RuntimeOptions()
        return await self.remove_face_device_from_device_group_with_options_async(request, runtime)

    def remove_face_user_from_user_group_with_options(
        self,
        request: main_models.RemoveFaceUserFromUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveFaceUserFromUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveFaceUserFromUserGroup',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveFaceUserFromUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_face_user_from_user_group_with_options_async(
        self,
        request: main_models.RemoveFaceUserFromUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveFaceUserFromUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveFaceUserFromUserGroup',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveFaceUserFromUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_face_user_from_user_group(
        self,
        request: main_models.RemoveFaceUserFromUserGroupRequest,
    ) -> main_models.RemoveFaceUserFromUserGroupResponse:
        runtime = RuntimeOptions()
        return self.remove_face_user_from_user_group_with_options(request, runtime)

    async def remove_face_user_from_user_group_async(
        self,
        request: main_models.RemoveFaceUserFromUserGroupRequest,
    ) -> main_models.RemoveFaceUserFromUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.remove_face_user_from_user_group_with_options_async(request, runtime)

    def set_device_picture_life_cycle_with_options(
        self,
        request: main_models.SetDevicePictureLifeCycleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDevicePictureLifeCycleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.day):
            query['Day'] = request.day
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDevicePictureLifeCycle',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDevicePictureLifeCycleResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_device_picture_life_cycle_with_options_async(
        self,
        request: main_models.SetDevicePictureLifeCycleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDevicePictureLifeCycleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.day):
            query['Day'] = request.day
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDevicePictureLifeCycle',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDevicePictureLifeCycleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_device_picture_life_cycle(
        self,
        request: main_models.SetDevicePictureLifeCycleRequest,
    ) -> main_models.SetDevicePictureLifeCycleResponse:
        runtime = RuntimeOptions()
        return self.set_device_picture_life_cycle_with_options(request, runtime)

    async def set_device_picture_life_cycle_async(
        self,
        request: main_models.SetDevicePictureLifeCycleRequest,
    ) -> main_models.SetDevicePictureLifeCycleResponse:
        runtime = RuntimeOptions()
        return await self.set_device_picture_life_cycle_with_options_async(request, runtime)

    def set_device_record_life_cycle_with_options(
        self,
        request: main_models.SetDeviceRecordLifeCycleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDeviceRecordLifeCycleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.day):
            query['Day'] = request.day
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDeviceRecordLifeCycle',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDeviceRecordLifeCycleResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_device_record_life_cycle_with_options_async(
        self,
        request: main_models.SetDeviceRecordLifeCycleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDeviceRecordLifeCycleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.day):
            query['Day'] = request.day
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDeviceRecordLifeCycle',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDeviceRecordLifeCycleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_device_record_life_cycle(
        self,
        request: main_models.SetDeviceRecordLifeCycleRequest,
    ) -> main_models.SetDeviceRecordLifeCycleResponse:
        runtime = RuntimeOptions()
        return self.set_device_record_life_cycle_with_options(request, runtime)

    async def set_device_record_life_cycle_async(
        self,
        request: main_models.SetDeviceRecordLifeCycleRequest,
    ) -> main_models.SetDeviceRecordLifeCycleResponse:
        runtime = RuntimeOptions()
        return await self.set_device_record_life_cycle_with_options_async(request, runtime)

    def stop_live_streaming_with_options(
        self,
        request: main_models.StopLiveStreamingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopLiveStreamingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopLiveStreaming',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopLiveStreamingResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_live_streaming_with_options_async(
        self,
        request: main_models.StopLiveStreamingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopLiveStreamingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopLiveStreaming',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopLiveStreamingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_live_streaming(
        self,
        request: main_models.StopLiveStreamingRequest,
    ) -> main_models.StopLiveStreamingResponse:
        runtime = RuntimeOptions()
        return self.stop_live_streaming_with_options(request, runtime)

    async def stop_live_streaming_async(
        self,
        request: main_models.StopLiveStreamingRequest,
    ) -> main_models.StopLiveStreamingResponse:
        runtime = RuntimeOptions()
        return await self.stop_live_streaming_with_options_async(request, runtime)

    def stop_triggered_record_with_options(
        self,
        request: main_models.StopTriggeredRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopTriggeredRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopTriggeredRecord',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopTriggeredRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_triggered_record_with_options_async(
        self,
        request: main_models.StopTriggeredRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopTriggeredRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopTriggeredRecord',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopTriggeredRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_triggered_record(
        self,
        request: main_models.StopTriggeredRecordRequest,
    ) -> main_models.StopTriggeredRecordResponse:
        runtime = RuntimeOptions()
        return self.stop_triggered_record_with_options(request, runtime)

    async def stop_triggered_record_async(
        self,
        request: main_models.StopTriggeredRecordRequest,
    ) -> main_models.StopTriggeredRecordResponse:
        runtime = RuntimeOptions()
        return await self.stop_triggered_record_with_options_async(request, runtime)

    def transfer_device_instance_with_options(
        self,
        request: main_models.TransferDeviceInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferDeviceInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name_list):
            query['DeviceNameList'] = request.device_name_list
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not DaraCore.is_null(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransferDeviceInstance',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferDeviceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_device_instance_with_options_async(
        self,
        request: main_models.TransferDeviceInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferDeviceInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name_list):
            query['DeviceNameList'] = request.device_name_list
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not DaraCore.is_null(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransferDeviceInstance',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferDeviceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_device_instance(
        self,
        request: main_models.TransferDeviceInstanceRequest,
    ) -> main_models.TransferDeviceInstanceResponse:
        runtime = RuntimeOptions()
        return self.transfer_device_instance_with_options(request, runtime)

    async def transfer_device_instance_async(
        self,
        request: main_models.TransferDeviceInstanceRequest,
    ) -> main_models.TransferDeviceInstanceResponse:
        runtime = RuntimeOptions()
        return await self.transfer_device_instance_with_options_async(request, runtime)

    def trigger_capture_picture_with_options(
        self,
        request: main_models.TriggerCapturePictureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TriggerCapturePictureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TriggerCapturePicture',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TriggerCapturePictureResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_capture_picture_with_options_async(
        self,
        request: main_models.TriggerCapturePictureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TriggerCapturePictureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TriggerCapturePicture',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TriggerCapturePictureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trigger_capture_picture(
        self,
        request: main_models.TriggerCapturePictureRequest,
    ) -> main_models.TriggerCapturePictureResponse:
        runtime = RuntimeOptions()
        return self.trigger_capture_picture_with_options(request, runtime)

    async def trigger_capture_picture_async(
        self,
        request: main_models.TriggerCapturePictureRequest,
    ) -> main_models.TriggerCapturePictureResponse:
        runtime = RuntimeOptions()
        return await self.trigger_capture_picture_with_options_async(request, runtime)

    def trigger_record_with_options(
        self,
        request: main_models.TriggerRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TriggerRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.record_duration):
            query['RecordDuration'] = request.record_duration
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TriggerRecord',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TriggerRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_record_with_options_async(
        self,
        request: main_models.TriggerRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TriggerRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.record_duration):
            query['RecordDuration'] = request.record_duration
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TriggerRecord',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TriggerRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trigger_record(
        self,
        request: main_models.TriggerRecordRequest,
    ) -> main_models.TriggerRecordResponse:
        runtime = RuntimeOptions()
        return self.trigger_record_with_options(request, runtime)

    async def trigger_record_async(
        self,
        request: main_models.TriggerRecordRequest,
    ) -> main_models.TriggerRecordResponse:
        runtime = RuntimeOptions()
        return await self.trigger_record_with_options_async(request, runtime)

    def unbind_picture_search_app_with_devices_with_options(
        self,
        request: main_models.UnbindPictureSearchAppWithDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindPictureSearchAppWithDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.device_iot_ids):
            query['DeviceIotIds'] = request.device_iot_ids
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindPictureSearchAppWithDevices',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindPictureSearchAppWithDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_picture_search_app_with_devices_with_options_async(
        self,
        request: main_models.UnbindPictureSearchAppWithDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindPictureSearchAppWithDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.device_iot_ids):
            query['DeviceIotIds'] = request.device_iot_ids
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindPictureSearchAppWithDevices',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindPictureSearchAppWithDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_picture_search_app_with_devices(
        self,
        request: main_models.UnbindPictureSearchAppWithDevicesRequest,
    ) -> main_models.UnbindPictureSearchAppWithDevicesResponse:
        runtime = RuntimeOptions()
        return self.unbind_picture_search_app_with_devices_with_options(request, runtime)

    async def unbind_picture_search_app_with_devices_async(
        self,
        request: main_models.UnbindPictureSearchAppWithDevicesRequest,
    ) -> main_models.UnbindPictureSearchAppWithDevicesResponse:
        runtime = RuntimeOptions()
        return await self.unbind_picture_search_app_with_devices_with_options_async(request, runtime)

    def update_event_record_plan_with_options(
        self,
        request: main_models.UpdateEventRecordPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEventRecordPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_types):
            query['EventTypes'] = request.event_types
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not DaraCore.is_null(request.record_duration):
            query['RecordDuration'] = request.record_duration
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEventRecordPlan',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEventRecordPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_event_record_plan_with_options_async(
        self,
        request: main_models.UpdateEventRecordPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEventRecordPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_types):
            query['EventTypes'] = request.event_types
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not DaraCore.is_null(request.record_duration):
            query['RecordDuration'] = request.record_duration
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEventRecordPlan',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEventRecordPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_event_record_plan(
        self,
        request: main_models.UpdateEventRecordPlanRequest,
    ) -> main_models.UpdateEventRecordPlanResponse:
        runtime = RuntimeOptions()
        return self.update_event_record_plan_with_options(request, runtime)

    async def update_event_record_plan_async(
        self,
        request: main_models.UpdateEventRecordPlanRequest,
    ) -> main_models.UpdateEventRecordPlanResponse:
        runtime = RuntimeOptions()
        return await self.update_event_record_plan_with_options_async(request, runtime)

    def update_face_user_with_options(
        self,
        request: main_models.UpdateFaceUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFaceUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not DaraCore.is_null(request.face_pic_url):
            query['FacePicUrl'] = request.face_pic_url
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFaceUser',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFaceUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_face_user_with_options_async(
        self,
        request: main_models.UpdateFaceUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFaceUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not DaraCore.is_null(request.face_pic_url):
            query['FacePicUrl'] = request.face_pic_url
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFaceUser',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFaceUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_face_user(
        self,
        request: main_models.UpdateFaceUserRequest,
    ) -> main_models.UpdateFaceUserResponse:
        runtime = RuntimeOptions()
        return self.update_face_user_with_options(request, runtime)

    async def update_face_user_async(
        self,
        request: main_models.UpdateFaceUserRequest,
    ) -> main_models.UpdateFaceUserResponse:
        runtime = RuntimeOptions()
        return await self.update_face_user_with_options_async(request, runtime)

    def update_face_user_group_and_device_group_relation_with_options(
        self,
        request: main_models.UpdateFaceUserGroupAndDeviceGroupRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFaceUserGroupAndDeviceGroupRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.control_id):
            query['ControlId'] = request.control_id
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.relation):
            query['Relation'] = request.relation
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFaceUserGroupAndDeviceGroupRelation',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFaceUserGroupAndDeviceGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_face_user_group_and_device_group_relation_with_options_async(
        self,
        request: main_models.UpdateFaceUserGroupAndDeviceGroupRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFaceUserGroupAndDeviceGroupRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.control_id):
            query['ControlId'] = request.control_id
        if not DaraCore.is_null(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not DaraCore.is_null(request.relation):
            query['Relation'] = request.relation
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFaceUserGroupAndDeviceGroupRelation',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFaceUserGroupAndDeviceGroupRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_face_user_group_and_device_group_relation(
        self,
        request: main_models.UpdateFaceUserGroupAndDeviceGroupRelationRequest,
    ) -> main_models.UpdateFaceUserGroupAndDeviceGroupRelationResponse:
        runtime = RuntimeOptions()
        return self.update_face_user_group_and_device_group_relation_with_options(request, runtime)

    async def update_face_user_group_and_device_group_relation_async(
        self,
        request: main_models.UpdateFaceUserGroupAndDeviceGroupRelationRequest,
    ) -> main_models.UpdateFaceUserGroupAndDeviceGroupRelationResponse:
        runtime = RuntimeOptions()
        return await self.update_face_user_group_and_device_group_relation_with_options_async(request, runtime)

    def update_gb_device_with_options(
        self,
        request: main_models.UpdateGbDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGbDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.gb_id):
            query['GbId'] = request.gb_id
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGbDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGbDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gb_device_with_options_async(
        self,
        request: main_models.UpdateGbDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGbDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.gb_id):
            query['GbId'] = request.gb_id
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGbDevice',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGbDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gb_device(
        self,
        request: main_models.UpdateGbDeviceRequest,
    ) -> main_models.UpdateGbDeviceResponse:
        runtime = RuntimeOptions()
        return self.update_gb_device_with_options(request, runtime)

    async def update_gb_device_async(
        self,
        request: main_models.UpdateGbDeviceRequest,
    ) -> main_models.UpdateGbDeviceResponse:
        runtime = RuntimeOptions()
        return await self.update_gb_device_with_options_async(request, runtime)

    def update_instance_internet_protocol_with_options(
        self,
        request: main_models.UpdateInstanceInternetProtocolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceInternetProtocolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceInternetProtocol',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceInternetProtocolResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_internet_protocol_with_options_async(
        self,
        request: main_models.UpdateInstanceInternetProtocolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceInternetProtocolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceInternetProtocol',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceInternetProtocolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_internet_protocol(
        self,
        request: main_models.UpdateInstanceInternetProtocolRequest,
    ) -> main_models.UpdateInstanceInternetProtocolResponse:
        runtime = RuntimeOptions()
        return self.update_instance_internet_protocol_with_options(request, runtime)

    async def update_instance_internet_protocol_async(
        self,
        request: main_models.UpdateInstanceInternetProtocolRequest,
    ) -> main_models.UpdateInstanceInternetProtocolResponse:
        runtime = RuntimeOptions()
        return await self.update_instance_internet_protocol_with_options_async(request, runtime)

    def update_picture_search_app_with_options(
        self,
        request: main_models.UpdatePictureSearchAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePictureSearchAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePictureSearchApp',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePictureSearchAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_picture_search_app_with_options_async(
        self,
        request: main_models.UpdatePictureSearchAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePictureSearchAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePictureSearchApp',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePictureSearchAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_picture_search_app(
        self,
        request: main_models.UpdatePictureSearchAppRequest,
    ) -> main_models.UpdatePictureSearchAppResponse:
        runtime = RuntimeOptions()
        return self.update_picture_search_app_with_options(request, runtime)

    async def update_picture_search_app_async(
        self,
        request: main_models.UpdatePictureSearchAppRequest,
    ) -> main_models.UpdatePictureSearchAppResponse:
        runtime = RuntimeOptions()
        return await self.update_picture_search_app_with_options_async(request, runtime)

    def update_record_plan_with_options(
        self,
        request: main_models.UpdateRecordPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecordPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecordPlan',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecordPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_record_plan_with_options_async(
        self,
        request: main_models.UpdateRecordPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecordPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecordPlan',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecordPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_record_plan(
        self,
        request: main_models.UpdateRecordPlanRequest,
    ) -> main_models.UpdateRecordPlanResponse:
        runtime = RuntimeOptions()
        return self.update_record_plan_with_options(request, runtime)

    async def update_record_plan_async(
        self,
        request: main_models.UpdateRecordPlanRequest,
    ) -> main_models.UpdateRecordPlanResponse:
        runtime = RuntimeOptions()
        return await self.update_record_plan_with_options_async(request, runtime)

    def update_rtmp_key_with_options(
        self,
        request: main_models.UpdateRtmpKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRtmpKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.pull_auth_key):
            query['PullAuthKey'] = request.pull_auth_key
        if not DaraCore.is_null(request.pull_key_expire_time):
            query['PullKeyExpireTime'] = request.pull_key_expire_time
        if not DaraCore.is_null(request.push_auth_key):
            query['PushAuthKey'] = request.push_auth_key
        if not DaraCore.is_null(request.push_key_expire_time):
            query['PushKeyExpireTime'] = request.push_key_expire_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRtmpKey',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRtmpKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rtmp_key_with_options_async(
        self,
        request: main_models.UpdateRtmpKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRtmpKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_name):
            query['DeviceName'] = request.device_name
        if not DaraCore.is_null(request.iot_id):
            query['IotId'] = request.iot_id
        if not DaraCore.is_null(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not DaraCore.is_null(request.product_key):
            query['ProductKey'] = request.product_key
        if not DaraCore.is_null(request.pull_auth_key):
            query['PullAuthKey'] = request.pull_auth_key
        if not DaraCore.is_null(request.pull_key_expire_time):
            query['PullKeyExpireTime'] = request.pull_key_expire_time
        if not DaraCore.is_null(request.push_auth_key):
            query['PushAuthKey'] = request.push_auth_key
        if not DaraCore.is_null(request.push_key_expire_time):
            query['PushKeyExpireTime'] = request.push_key_expire_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRtmpKey',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRtmpKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rtmp_key(
        self,
        request: main_models.UpdateRtmpKeyRequest,
    ) -> main_models.UpdateRtmpKeyResponse:
        runtime = RuntimeOptions()
        return self.update_rtmp_key_with_options(request, runtime)

    async def update_rtmp_key_async(
        self,
        request: main_models.UpdateRtmpKeyRequest,
    ) -> main_models.UpdateRtmpKeyResponse:
        runtime = RuntimeOptions()
        return await self.update_rtmp_key_with_options_async(request, runtime)

    def update_time_template_with_options(
        self,
        request: main_models.UpdateTimeTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTimeTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all_day):
            query['AllDay'] = request.all_day
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.time_sections):
            query['TimeSections'] = request.time_sections
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTimeTemplate',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTimeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_time_template_with_options_async(
        self,
        request: main_models.UpdateTimeTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTimeTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all_day):
            query['AllDay'] = request.all_day
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.time_sections):
            query['TimeSections'] = request.time_sections
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTimeTemplate',
            version = '2018-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTimeTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_time_template(
        self,
        request: main_models.UpdateTimeTemplateRequest,
    ) -> main_models.UpdateTimeTemplateResponse:
        runtime = RuntimeOptions()
        return self.update_time_template_with_options(request, runtime)

    async def update_time_template_async(
        self,
        request: main_models.UpdateTimeTemplateRequest,
    ) -> main_models.UpdateTimeTemplateResponse:
        runtime = RuntimeOptions()
        return await self.update_time_template_with_options_async(request, runtime)
