# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_linkvisual20180120 import models as linkvisual_20180120_models
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
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddEventRecordPlanDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddEventRecordPlanDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_event_record_plan_device_with_options_async(
        self,
        request: linkvisual_20180120_models.AddEventRecordPlanDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddEventRecordPlanDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddEventRecordPlanDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddEventRecordPlanDeviceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.device_group_name):
            query['DeviceGroupName'] = request.device_group_name
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFaceDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddFaceDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_face_device_group_with_options_async(
        self,
        request: linkvisual_20180120_models.AddFaceDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddFaceDeviceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_group_name):
            query['DeviceGroupName'] = request.device_group_name
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFaceDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddFaceDeviceGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFaceDeviceToDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddFaceDeviceToDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_face_device_to_device_group_with_options_async(
        self,
        request: linkvisual_20180120_models.AddFaceDeviceToDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddFaceDeviceToDeviceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFaceDeviceToDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddFaceDeviceToDeviceGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not UtilClient.is_unset(request.face_pic_url):
            query['FacePicUrl'] = request.face_pic_url
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFaceUser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddFaceUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_face_user_with_options_async(
        self,
        request: linkvisual_20180120_models.AddFaceUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddFaceUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not UtilClient.is_unset(request.face_pic_url):
            query['FacePicUrl'] = request.face_pic_url
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFaceUser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddFaceUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFaceUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddFaceUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_face_user_group_with_options_async(
        self,
        request: linkvisual_20180120_models.AddFaceUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddFaceUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFaceUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddFaceUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.relation):
            query['Relation'] = request.relation
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFaceUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddFaceUserGroupAndDeviceGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_face_user_group_and_device_group_relation_with_options_async(
        self,
        request: linkvisual_20180120_models.AddFaceUserGroupAndDeviceGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddFaceUserGroupAndDeviceGroupRelationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.relation):
            query['Relation'] = request.relation
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFaceUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddFaceUserGroupAndDeviceGroupRelationResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.face_pic_url):
            query['FacePicUrl'] = request.face_pic_url
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFaceUserPicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddFaceUserPictureResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_face_user_picture_with_options_async(
        self,
        request: linkvisual_20180120_models.AddFaceUserPictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddFaceUserPictureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.face_pic_url):
            query['FacePicUrl'] = request.face_pic_url
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFaceUserPicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddFaceUserPictureResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFaceUserToUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddFaceUserToUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_face_user_to_user_group_with_options_async(
        self,
        request: linkvisual_20180120_models.AddFaceUserToUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddFaceUserToUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFaceUserToUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddFaceUserToUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRecordPlanDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddRecordPlanDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_record_plan_device_with_options_async(
        self,
        request: linkvisual_20180120_models.AddRecordPlanDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.AddRecordPlanDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRecordPlanDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddRecordPlanDeviceResponse(),
            await self.call_api_async(params, req, runtime)
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

    def batch_query_vision_device_info_with_options(
        self,
        request: linkvisual_20180120_models.BatchQueryVisionDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.BatchQueryVisionDeviceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name_list):
            query['DeviceNameList'] = request.device_name_list
        if not UtilClient.is_unset(request.iot_id_list):
            query['IotIdList'] = request.iot_id_list
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchQueryVisionDeviceInfo',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.BatchQueryVisionDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_query_vision_device_info_with_options_async(
        self,
        request: linkvisual_20180120_models.BatchQueryVisionDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.BatchQueryVisionDeviceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name_list):
            query['DeviceNameList'] = request.device_name_list
        if not UtilClient.is_unset(request.iot_id_list):
            query['IotIdList'] = request.iot_id_list
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchQueryVisionDeviceInfo',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.BatchQueryVisionDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_query_vision_device_info(
        self,
        request: linkvisual_20180120_models.BatchQueryVisionDeviceInfoRequest,
    ) -> linkvisual_20180120_models.BatchQueryVisionDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_query_vision_device_info_with_options(request, runtime)

    async def batch_query_vision_device_info_async(
        self,
        request: linkvisual_20180120_models.BatchQueryVisionDeviceInfoRequest,
    ) -> linkvisual_20180120_models.BatchQueryVisionDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_query_vision_device_info_with_options_async(request, runtime)

    def bind_picture_search_app_with_devices_with_options(
        self,
        request: linkvisual_20180120_models.BindPictureSearchAppWithDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.BindPictureSearchAppWithDevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.device_iot_ids):
            query['DeviceIotIds'] = request.device_iot_ids
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindPictureSearchAppWithDevices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.BindPictureSearchAppWithDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_picture_search_app_with_devices_with_options_async(
        self,
        request: linkvisual_20180120_models.BindPictureSearchAppWithDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.BindPictureSearchAppWithDevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.device_iot_ids):
            query['DeviceIotIds'] = request.device_iot_ids
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindPictureSearchAppWithDevices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.BindPictureSearchAppWithDevicesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckFaceUserDoExistOnDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CheckFaceUserDoExistOnDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_face_user_do_exist_on_device_with_options_async(
        self,
        request: linkvisual_20180120_models.CheckFaceUserDoExistOnDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CheckFaceUserDoExistOnDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckFaceUserDoExistOnDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CheckFaceUserDoExistOnDeviceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearFaceDeviceDB',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.ClearFaceDeviceDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_face_device_dbwith_options_async(
        self,
        request: linkvisual_20180120_models.ClearFaceDeviceDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.ClearFaceDeviceDBResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearFaceDeviceDB',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.ClearFaceDeviceDBResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_event_record_plan_with_options(
        self,
        request: linkvisual_20180120_models.CreateEventRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateEventRecordPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_types):
            query['EventTypes'] = request.event_types
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not UtilClient.is_unset(request.record_duration):
            query['RecordDuration'] = request.record_duration
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEventRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateEventRecordPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_event_record_plan_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateEventRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateEventRecordPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_types):
            query['EventTypes'] = request.event_types
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not UtilClient.is_unset(request.record_duration):
            query['RecordDuration'] = request.record_duration
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEventRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateEventRecordPlanResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_gb_device_with_options(
        self,
        request: linkvisual_20180120_models.CreateGbDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateGbDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_type):
            query['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.gb_id):
            query['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.media_net_protocol):
            query['MediaNetProtocol'] = request.media_net_protocol
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.sub_product_key):
            query['SubProductKey'] = request.sub_product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGbDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateGbDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gb_device_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateGbDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateGbDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_type):
            query['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.gb_id):
            query['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.media_net_protocol):
            query['MediaNetProtocol'] = request.media_net_protocol
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.sub_product_key):
            query['SubProductKey'] = request.sub_product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGbDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateGbDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gb_device(
        self,
        request: linkvisual_20180120_models.CreateGbDeviceRequest,
    ) -> linkvisual_20180120_models.CreateGbDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_gb_device_with_options(request, runtime)

    async def create_gb_device_async(
        self,
        request: linkvisual_20180120_models.CreateGbDeviceRequest,
    ) -> linkvisual_20180120_models.CreateGbDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_gb_device_with_options_async(request, runtime)

    def create_local_file_upload_job_with_options(
        self,
        request: linkvisual_20180120_models.CreateLocalFileUploadJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateLocalFileUploadJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.time_slot):
            query['TimeSlot'] = request.time_slot
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLocalFileUploadJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateLocalFileUploadJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_local_file_upload_job_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateLocalFileUploadJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateLocalFileUploadJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.time_slot):
            query['TimeSlot'] = request.time_slot
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLocalFileUploadJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateLocalFileUploadJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_local_file_upload_job(
        self,
        request: linkvisual_20180120_models.CreateLocalFileUploadJobRequest,
    ) -> linkvisual_20180120_models.CreateLocalFileUploadJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_local_file_upload_job_with_options(request, runtime)

    async def create_local_file_upload_job_async(
        self,
        request: linkvisual_20180120_models.CreateLocalFileUploadJobRequest,
    ) -> linkvisual_20180120_models.CreateLocalFileUploadJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_local_file_upload_job_with_options_async(request, runtime)

    def create_local_record_download_by_time_job_with_options(
        self,
        request: linkvisual_20180120_models.CreateLocalRecordDownloadByTimeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateLocalRecordDownloadByTimeJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLocalRecordDownloadByTimeJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateLocalRecordDownloadByTimeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_local_record_download_by_time_job_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateLocalRecordDownloadByTimeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateLocalRecordDownloadByTimeJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLocalRecordDownloadByTimeJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateLocalRecordDownloadByTimeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_local_record_download_by_time_job(
        self,
        request: linkvisual_20180120_models.CreateLocalRecordDownloadByTimeJobRequest,
    ) -> linkvisual_20180120_models.CreateLocalRecordDownloadByTimeJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_local_record_download_by_time_job_with_options(request, runtime)

    async def create_local_record_download_by_time_job_async(
        self,
        request: linkvisual_20180120_models.CreateLocalRecordDownloadByTimeJobRequest,
    ) -> linkvisual_20180120_models.CreateLocalRecordDownloadByTimeJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_local_record_download_by_time_job_with_options_async(request, runtime)

    def create_picture_search_app_with_options(
        self,
        request: linkvisual_20180120_models.CreatePictureSearchAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreatePictureSearchAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePictureSearchApp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreatePictureSearchAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_picture_search_app_with_options_async(
        self,
        request: linkvisual_20180120_models.CreatePictureSearchAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreatePictureSearchAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePictureSearchApp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreatePictureSearchAppResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_picture_search_job_with_options(
        self,
        request: linkvisual_20180120_models.CreatePictureSearchJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreatePictureSearchJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.body_threshold):
            query['BodyThreshold'] = request.body_threshold
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.picture_search_type):
            query['PictureSearchType'] = request.picture_search_type
        if not UtilClient.is_unset(request.search_pic_url):
            query['SearchPicUrl'] = request.search_pic_url
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePictureSearchJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreatePictureSearchJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_picture_search_job_with_options_async(
        self,
        request: linkvisual_20180120_models.CreatePictureSearchJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreatePictureSearchJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.body_threshold):
            query['BodyThreshold'] = request.body_threshold
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.picture_search_type):
            query['PictureSearchType'] = request.picture_search_type
        if not UtilClient.is_unset(request.search_pic_url):
            query['SearchPicUrl'] = request.search_pic_url
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePictureSearchJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreatePictureSearchJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_picture_search_job(
        self,
        request: linkvisual_20180120_models.CreatePictureSearchJobRequest,
    ) -> linkvisual_20180120_models.CreatePictureSearchJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_picture_search_job_with_options(request, runtime)

    async def create_picture_search_job_async(
        self,
        request: linkvisual_20180120_models.CreatePictureSearchJobRequest,
    ) -> linkvisual_20180120_models.CreatePictureSearchJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_picture_search_job_with_options_async(request, runtime)

    def create_record_download_by_time_job_with_options(
        self,
        request: linkvisual_20180120_models.CreateRecordDownloadByTimeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateRecordDownloadByTimeJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.record_type):
            query['RecordType'] = request.record_type
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRecordDownloadByTimeJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateRecordDownloadByTimeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_record_download_by_time_job_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateRecordDownloadByTimeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateRecordDownloadByTimeJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.record_type):
            query['RecordType'] = request.record_type
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRecordDownloadByTimeJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateRecordDownloadByTimeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_record_download_by_time_job(
        self,
        request: linkvisual_20180120_models.CreateRecordDownloadByTimeJobRequest,
    ) -> linkvisual_20180120_models.CreateRecordDownloadByTimeJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_record_download_by_time_job_with_options(request, runtime)

    async def create_record_download_by_time_job_async(
        self,
        request: linkvisual_20180120_models.CreateRecordDownloadByTimeJobRequest,
    ) -> linkvisual_20180120_models.CreateRecordDownloadByTimeJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_record_download_by_time_job_with_options_async(request, runtime)

    def create_record_plan_with_options(
        self,
        request: linkvisual_20180120_models.CreateRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateRecordPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateRecordPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_record_plan_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateRecordPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateRecordPlanResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_rtmp_device_with_options(
        self,
        request: linkvisual_20180120_models.CreateRtmpDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateRtmpDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.pull_auth_key):
            query['PullAuthKey'] = request.pull_auth_key
        if not UtilClient.is_unset(request.pull_key_expire_time):
            query['PullKeyExpireTime'] = request.pull_key_expire_time
        if not UtilClient.is_unset(request.push_auth_key):
            query['PushAuthKey'] = request.push_auth_key
        if not UtilClient.is_unset(request.push_key_expire_time):
            query['PushKeyExpireTime'] = request.push_key_expire_time
        if not UtilClient.is_unset(request.sub_stream_name):
            query['SubStreamName'] = request.sub_stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRtmpDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateRtmpDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rtmp_device_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateRtmpDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateRtmpDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.pull_auth_key):
            query['PullAuthKey'] = request.pull_auth_key
        if not UtilClient.is_unset(request.pull_key_expire_time):
            query['PullKeyExpireTime'] = request.pull_key_expire_time
        if not UtilClient.is_unset(request.push_auth_key):
            query['PushAuthKey'] = request.push_auth_key
        if not UtilClient.is_unset(request.push_key_expire_time):
            query['PushKeyExpireTime'] = request.push_key_expire_time
        if not UtilClient.is_unset(request.sub_stream_name):
            query['SubStreamName'] = request.sub_stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRtmpDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateRtmpDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rtmp_device(
        self,
        request: linkvisual_20180120_models.CreateRtmpDeviceRequest,
    ) -> linkvisual_20180120_models.CreateRtmpDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_rtmp_device_with_options(request, runtime)

    async def create_rtmp_device_async(
        self,
        request: linkvisual_20180120_models.CreateRtmpDeviceRequest,
    ) -> linkvisual_20180120_models.CreateRtmpDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_rtmp_device_with_options_async(request, runtime)

    def create_stream_push_job_with_options(
        self,
        request: linkvisual_20180120_models.CreateStreamPushJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateStreamPushJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.push_url):
            query['PushUrl'] = request.push_url
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStreamPushJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateStreamPushJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_stream_push_job_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateStreamPushJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateStreamPushJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.push_url):
            query['PushUrl'] = request.push_url
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStreamPushJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateStreamPushJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_stream_push_job(
        self,
        request: linkvisual_20180120_models.CreateStreamPushJobRequest,
    ) -> linkvisual_20180120_models.CreateStreamPushJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_stream_push_job_with_options(request, runtime)

    async def create_stream_push_job_async(
        self,
        request: linkvisual_20180120_models.CreateStreamPushJobRequest,
    ) -> linkvisual_20180120_models.CreateStreamPushJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_stream_push_job_with_options_async(request, runtime)

    def create_stream_snapshot_job_with_options(
        self,
        request: linkvisual_20180120_models.CreateStreamSnapshotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateStreamSnapshotJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.snapshot_interval):
            query['SnapshotInterval'] = request.snapshot_interval
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStreamSnapshotJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateStreamSnapshotJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_stream_snapshot_job_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateStreamSnapshotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateStreamSnapshotJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.snapshot_interval):
            query['SnapshotInterval'] = request.snapshot_interval
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStreamSnapshotJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateStreamSnapshotJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_stream_snapshot_job(
        self,
        request: linkvisual_20180120_models.CreateStreamSnapshotJobRequest,
    ) -> linkvisual_20180120_models.CreateStreamSnapshotJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_stream_snapshot_job_with_options(request, runtime)

    async def create_stream_snapshot_job_async(
        self,
        request: linkvisual_20180120_models.CreateStreamSnapshotJobRequest,
    ) -> linkvisual_20180120_models.CreateStreamSnapshotJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_stream_snapshot_job_with_options_async(request, runtime)

    def create_time_template_with_options(
        self,
        request: linkvisual_20180120_models.CreateTimeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateTimeTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_day):
            query['AllDay'] = request.all_day
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.time_sections):
            query['TimeSections'] = request.time_sections
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTimeTemplate',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateTimeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_time_template_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateTimeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateTimeTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_day):
            query['AllDay'] = request.all_day
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.time_sections):
            query['TimeSections'] = request.time_sections
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTimeTemplate',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateTimeTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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

    def delete_event_record_plan_with_options(
        self,
        request: linkvisual_20180120_models.DeleteEventRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteEventRecordPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEventRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteEventRecordPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_record_plan_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteEventRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteEventRecordPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEventRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteEventRecordPlanResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEventRecordPlanDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteEventRecordPlanDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_record_plan_device_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteEventRecordPlanDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteEventRecordPlanDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEventRecordPlanDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteEventRecordPlanDeviceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFaceDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteFaceDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_face_device_group_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteFaceDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteFaceDeviceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFaceDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteFaceDeviceGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFaceUser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteFaceUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_face_user_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteFaceUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteFaceUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFaceUser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteFaceUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFaceUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteFaceUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_face_user_group_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteFaceUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteFaceUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFaceUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteFaceUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.control_id):
            query['ControlId'] = request.control_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFaceUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteFaceUserGroupAndDeviceGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_face_user_group_and_device_group_relation_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteFaceUserGroupAndDeviceGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteFaceUserGroupAndDeviceGroupRelationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.control_id):
            query['ControlId'] = request.control_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFaceUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteFaceUserGroupAndDeviceGroupRelationResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.face_pic_md_5):
            query['FacePicMd5'] = request.face_pic_md_5
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFaceUserPicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteFaceUserPictureResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_face_user_picture_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteFaceUserPictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteFaceUserPictureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.face_pic_md_5):
            query['FacePicMd5'] = request.face_pic_md_5
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFaceUserPicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteFaceUserPictureResponse(),
            await self.call_api_async(params, req, runtime)
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

    def delete_gb_device_with_options(
        self,
        request: linkvisual_20180120_models.DeleteGbDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteGbDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGbDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteGbDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gb_device_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteGbDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteGbDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGbDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteGbDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gb_device(
        self,
        request: linkvisual_20180120_models.DeleteGbDeviceRequest,
    ) -> linkvisual_20180120_models.DeleteGbDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_gb_device_with_options(request, runtime)

    async def delete_gb_device_async(
        self,
        request: linkvisual_20180120_models.DeleteGbDeviceRequest,
    ) -> linkvisual_20180120_models.DeleteGbDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_gb_device_with_options_async(request, runtime)

    def delete_local_file_upload_job_with_options(
        self,
        request: linkvisual_20180120_models.DeleteLocalFileUploadJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteLocalFileUploadJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLocalFileUploadJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteLocalFileUploadJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_local_file_upload_job_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteLocalFileUploadJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteLocalFileUploadJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLocalFileUploadJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteLocalFileUploadJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_local_file_upload_job(
        self,
        request: linkvisual_20180120_models.DeleteLocalFileUploadJobRequest,
    ) -> linkvisual_20180120_models.DeleteLocalFileUploadJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_local_file_upload_job_with_options(request, runtime)

    async def delete_local_file_upload_job_async(
        self,
        request: linkvisual_20180120_models.DeleteLocalFileUploadJobRequest,
    ) -> linkvisual_20180120_models.DeleteLocalFileUploadJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_local_file_upload_job_with_options_async(request, runtime)

    def delete_picture_with_options(
        self,
        request: linkvisual_20180120_models.DeletePictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeletePictureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.picture_id_list):
            query['PictureIdList'] = request.picture_id_list
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeletePictureResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_picture_with_options_async(
        self,
        request: linkvisual_20180120_models.DeletePictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeletePictureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.picture_id_list):
            query['PictureIdList'] = request.picture_id_list
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeletePictureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_picture(
        self,
        request: linkvisual_20180120_models.DeletePictureRequest,
    ) -> linkvisual_20180120_models.DeletePictureResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_picture_with_options(request, runtime)

    async def delete_picture_async(
        self,
        request: linkvisual_20180120_models.DeletePictureRequest,
    ) -> linkvisual_20180120_models.DeletePictureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_picture_with_options_async(request, runtime)

    def delete_record_with_options(
        self,
        request: linkvisual_20180120_models.DeleteRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.file_name_list):
            query['FileNameList'] = request.file_name_list
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_record_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.file_name_list):
            query['FileNameList'] = request.file_name_list
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_record(
        self,
        request: linkvisual_20180120_models.DeleteRecordRequest,
    ) -> linkvisual_20180120_models.DeleteRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_record_with_options(request, runtime)

    async def delete_record_async(
        self,
        request: linkvisual_20180120_models.DeleteRecordRequest,
    ) -> linkvisual_20180120_models.DeleteRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_record_with_options_async(request, runtime)

    def delete_record_plan_with_options(
        self,
        request: linkvisual_20180120_models.DeleteRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteRecordPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteRecordPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_record_plan_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteRecordPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteRecordPlanResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRecordPlanDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteRecordPlanDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_record_plan_device_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteRecordPlanDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteRecordPlanDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRecordPlanDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteRecordPlanDeviceResponse(),
            await self.call_api_async(params, req, runtime)
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

    def delete_rtmp_device_with_options(
        self,
        request: linkvisual_20180120_models.DeleteRtmpDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteRtmpDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRtmpDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteRtmpDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rtmp_device_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteRtmpDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteRtmpDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRtmpDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteRtmpDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rtmp_device(
        self,
        request: linkvisual_20180120_models.DeleteRtmpDeviceRequest,
    ) -> linkvisual_20180120_models.DeleteRtmpDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_rtmp_device_with_options(request, runtime)

    async def delete_rtmp_device_async(
        self,
        request: linkvisual_20180120_models.DeleteRtmpDeviceRequest,
    ) -> linkvisual_20180120_models.DeleteRtmpDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_rtmp_device_with_options_async(request, runtime)

    def delete_rtmp_key_with_options(
        self,
        request: linkvisual_20180120_models.DeleteRtmpKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteRtmpKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRtmpKey',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteRtmpKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rtmp_key_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteRtmpKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteRtmpKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRtmpKey',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteRtmpKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rtmp_key(
        self,
        request: linkvisual_20180120_models.DeleteRtmpKeyRequest,
    ) -> linkvisual_20180120_models.DeleteRtmpKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_rtmp_key_with_options(request, runtime)

    async def delete_rtmp_key_async(
        self,
        request: linkvisual_20180120_models.DeleteRtmpKeyRequest,
    ) -> linkvisual_20180120_models.DeleteRtmpKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_rtmp_key_with_options_async(request, runtime)

    def delete_stream_push_job_with_options(
        self,
        request: linkvisual_20180120_models.DeleteStreamPushJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteStreamPushJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStreamPushJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteStreamPushJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_stream_push_job_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteStreamPushJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteStreamPushJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStreamPushJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteStreamPushJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_stream_push_job(
        self,
        request: linkvisual_20180120_models.DeleteStreamPushJobRequest,
    ) -> linkvisual_20180120_models.DeleteStreamPushJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_stream_push_job_with_options(request, runtime)

    async def delete_stream_push_job_async(
        self,
        request: linkvisual_20180120_models.DeleteStreamPushJobRequest,
    ) -> linkvisual_20180120_models.DeleteStreamPushJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_stream_push_job_with_options_async(request, runtime)

    def delete_stream_snapshot_job_with_options(
        self,
        request: linkvisual_20180120_models.DeleteStreamSnapshotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteStreamSnapshotJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStreamSnapshotJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteStreamSnapshotJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_stream_snapshot_job_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteStreamSnapshotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteStreamSnapshotJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStreamSnapshotJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteStreamSnapshotJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_stream_snapshot_job(
        self,
        request: linkvisual_20180120_models.DeleteStreamSnapshotJobRequest,
    ) -> linkvisual_20180120_models.DeleteStreamSnapshotJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_stream_snapshot_job_with_options(request, runtime)

    async def delete_stream_snapshot_job_async(
        self,
        request: linkvisual_20180120_models.DeleteStreamSnapshotJobRequest,
    ) -> linkvisual_20180120_models.DeleteStreamSnapshotJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_stream_snapshot_job_with_options_async(request, runtime)

    def delete_time_template_with_options(
        self,
        request: linkvisual_20180120_models.DeleteTimeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteTimeTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTimeTemplate',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteTimeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_time_template_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteTimeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteTimeTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTimeTemplate',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteTimeTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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

    def detect_user_face_by_url_with_options(
        self,
        request: linkvisual_20180120_models.DetectUserFaceByUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DetectUserFaceByUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.face_pic_url):
            query['FacePicUrl'] = request.face_pic_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectUserFaceByUrl',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DetectUserFaceByUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_user_face_by_url_with_options_async(
        self,
        request: linkvisual_20180120_models.DetectUserFaceByUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DetectUserFaceByUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.face_pic_url):
            query['FacePicUrl'] = request.face_pic_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectUserFaceByUrl',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DetectUserFaceByUrlResponse(),
            await self.call_api_async(params, req, runtime)
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

    def enable_gb_sub_device_with_options(
        self,
        request: linkvisual_20180120_models.EnableGbSubDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.EnableGbSubDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.sub_device_id):
            query['SubDeviceId'] = request.sub_device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableGbSubDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.EnableGbSubDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_gb_sub_device_with_options_async(
        self,
        request: linkvisual_20180120_models.EnableGbSubDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.EnableGbSubDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.sub_device_id):
            query['SubDeviceId'] = request.sub_device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableGbSubDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.EnableGbSubDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_gb_sub_device(
        self,
        request: linkvisual_20180120_models.EnableGbSubDeviceRequest,
    ) -> linkvisual_20180120_models.EnableGbSubDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_gb_sub_device_with_options(request, runtime)

    async def enable_gb_sub_device_async(
        self,
        request: linkvisual_20180120_models.EnableGbSubDeviceRequest,
    ) -> linkvisual_20180120_models.EnableGbSubDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_gb_sub_device_with_options_async(request, runtime)

    def get_picture_search_job_status_with_options(
        self,
        request: linkvisual_20180120_models.GetPictureSearchJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetPictureSearchJobStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPictureSearchJobStatus',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetPictureSearchJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_picture_search_job_status_with_options_async(
        self,
        request: linkvisual_20180120_models.GetPictureSearchJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetPictureSearchJobStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPictureSearchJobStatus',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetPictureSearchJobStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_picture_search_job_status(
        self,
        request: linkvisual_20180120_models.GetPictureSearchJobStatusRequest,
    ) -> linkvisual_20180120_models.GetPictureSearchJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_picture_search_job_status_with_options(request, runtime)

    async def get_picture_search_job_status_async(
        self,
        request: linkvisual_20180120_models.GetPictureSearchJobStatusRequest,
    ) -> linkvisual_20180120_models.GetPictureSearchJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_picture_search_job_status_with_options_async(request, runtime)

    def picture_search_picture_with_options(
        self,
        request: linkvisual_20180120_models.PictureSearchPictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.PictureSearchPictureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.contain_pic_url):
            query['ContainPicUrl'] = request.contain_pic_url
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.picture_search_type):
            query['PictureSearchType'] = request.picture_search_type
        if not UtilClient.is_unset(request.search_pic_url):
            query['SearchPicUrl'] = request.search_pic_url
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PictureSearchPicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.PictureSearchPictureResponse(),
            self.call_api(params, req, runtime)
        )

    async def picture_search_picture_with_options_async(
        self,
        request: linkvisual_20180120_models.PictureSearchPictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.PictureSearchPictureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.contain_pic_url):
            query['ContainPicUrl'] = request.contain_pic_url
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.picture_search_type):
            query['PictureSearchType'] = request.picture_search_type
        if not UtilClient.is_unset(request.search_pic_url):
            query['SearchPicUrl'] = request.search_pic_url
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PictureSearchPicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.PictureSearchPictureResponse(),
            await self.call_api_async(params, req, runtime)
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

    def query_car_process_events_with_options(
        self,
        request: linkvisual_20180120_models.QueryCarProcessEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryCarProcessEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.area_index):
            query['AreaIndex'] = request.area_index
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.plate_no):
            query['PlateNo'] = request.plate_no
        if not UtilClient.is_unset(request.sub_device_name):
            query['SubDeviceName'] = request.sub_device_name
        if not UtilClient.is_unset(request.sub_iot_id):
            query['SubIotId'] = request.sub_iot_id
        if not UtilClient.is_unset(request.sub_product_key):
            query['SubProductKey'] = request.sub_product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCarProcessEvents',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryCarProcessEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_car_process_events_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryCarProcessEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryCarProcessEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.area_index):
            query['AreaIndex'] = request.area_index
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.plate_no):
            query['PlateNo'] = request.plate_no
        if not UtilClient.is_unset(request.sub_device_name):
            query['SubDeviceName'] = request.sub_device_name
        if not UtilClient.is_unset(request.sub_iot_id):
            query['SubIotId'] = request.sub_iot_id
        if not UtilClient.is_unset(request.sub_product_key):
            query['SubProductKey'] = request.sub_product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCarProcessEvents',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryCarProcessEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_car_process_events(
        self,
        request: linkvisual_20180120_models.QueryCarProcessEventsRequest,
    ) -> linkvisual_20180120_models.QueryCarProcessEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_car_process_events_with_options(request, runtime)

    async def query_car_process_events_async(
        self,
        request: linkvisual_20180120_models.QueryCarProcessEventsRequest,
    ) -> linkvisual_20180120_models.QueryCarProcessEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_car_process_events_with_options_async(request, runtime)

    def query_device_event_with_options(
        self,
        request: linkvisual_20180120_models.QueryDeviceEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDeviceEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceEvent',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDeviceEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_event_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryDeviceEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDeviceEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceEvent',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDeviceEventResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceEventPicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDeviceEventPictureResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_event_picture_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryDeviceEventPictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDeviceEventPictureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceEventPicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDeviceEventPictureResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceEventRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDeviceEventRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_event_record_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryDeviceEventRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDeviceEventRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceEventRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDeviceEventRecordResponse(),
            await self.call_api_async(params, req, runtime)
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

    def query_device_picture_by_list_with_options(
        self,
        request: linkvisual_20180120_models.QueryDevicePictureByListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDevicePictureByListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.picture_id_list):
            query['PictureIdList'] = request.picture_id_list
        if not UtilClient.is_unset(request.picture_type):
            query['PictureType'] = request.picture_type
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.thumb_width):
            query['ThumbWidth'] = request.thumb_width
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDevicePictureByList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDevicePictureByListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_picture_by_list_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryDevicePictureByListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDevicePictureByListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.picture_id_list):
            query['PictureIdList'] = request.picture_id_list
        if not UtilClient.is_unset(request.picture_type):
            query['PictureType'] = request.picture_type
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.thumb_width):
            query['ThumbWidth'] = request.thumb_width
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDevicePictureByList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDevicePictureByListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_device_picture_by_list(
        self,
        request: linkvisual_20180120_models.QueryDevicePictureByListRequest,
    ) -> linkvisual_20180120_models.QueryDevicePictureByListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_picture_by_list_with_options(request, runtime)

    async def query_device_picture_by_list_async(
        self,
        request: linkvisual_20180120_models.QueryDevicePictureByListRequest,
    ) -> linkvisual_20180120_models.QueryDevicePictureByListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_picture_by_list_with_options_async(request, runtime)

    def query_device_picture_file_with_options(
        self,
        request: linkvisual_20180120_models.QueryDevicePictureFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDevicePictureFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.capture_id):
            query['CaptureId'] = request.capture_id
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.picture_type):
            query['PictureType'] = request.picture_type
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.thumb_width):
            query['ThumbWidth'] = request.thumb_width
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDevicePictureFile',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDevicePictureFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_picture_file_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryDevicePictureFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDevicePictureFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.capture_id):
            query['CaptureId'] = request.capture_id
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.picture_type):
            query['PictureType'] = request.picture_type
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.thumb_width):
            query['ThumbWidth'] = request.thumb_width
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDevicePictureFile',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDevicePictureFileResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDevicePictureLifeCycle',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDevicePictureLifeCycleResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_picture_life_cycle_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryDevicePictureLifeCycleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDevicePictureLifeCycleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDevicePictureLifeCycle',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDevicePictureLifeCycleResponse(),
            await self.call_api_async(params, req, runtime)
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

    def query_device_record_life_cycle_with_options(
        self,
        request: linkvisual_20180120_models.QueryDeviceRecordLifeCycleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDeviceRecordLifeCycleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_list):
            query['DeviceList'] = request.device_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceRecordLifeCycle',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDeviceRecordLifeCycleResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_record_life_cycle_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryDeviceRecordLifeCycleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDeviceRecordLifeCycleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_list):
            query['DeviceList'] = request.device_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceRecordLifeCycle',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDeviceRecordLifeCycleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.enable_stun):
            query['EnableStun'] = request.enable_stun
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.play_un_limited):
            query['PlayUnLimited'] = request.play_un_limited
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.scheme):
            query['Scheme'] = request.scheme
        if not UtilClient.is_unset(request.seek_time):
            query['SeekTime'] = request.seek_time
        if not UtilClient.is_unset(request.should_encrypt):
            query['ShouldEncrypt'] = request.should_encrypt
        if not UtilClient.is_unset(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceVodUrl',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDeviceVodUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_vod_url_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryDeviceVodUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDeviceVodUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.enable_stun):
            query['EnableStun'] = request.enable_stun
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.play_un_limited):
            query['PlayUnLimited'] = request.play_un_limited
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.scheme):
            query['Scheme'] = request.scheme
        if not UtilClient.is_unset(request.seek_time):
            query['SeekTime'] = request.seek_time
        if not UtilClient.is_unset(request.should_encrypt):
            query['ShouldEncrypt'] = request.should_encrypt
        if not UtilClient.is_unset(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceVodUrl',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDeviceVodUrlResponse(),
            await self.call_api_async(params, req, runtime)
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

    def query_device_vod_url_by_time_with_options(
        self,
        request: linkvisual_20180120_models.QueryDeviceVodUrlByTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDeviceVodUrlByTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.enable_stun):
            query['EnableStun'] = request.enable_stun
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.play_un_limited):
            query['PlayUnLimited'] = request.play_un_limited
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.scheme):
            query['Scheme'] = request.scheme
        if not UtilClient.is_unset(request.seek_time):
            query['SeekTime'] = request.seek_time
        if not UtilClient.is_unset(request.should_encrypt):
            query['ShouldEncrypt'] = request.should_encrypt
        if not UtilClient.is_unset(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceVodUrlByTime',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDeviceVodUrlByTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_vod_url_by_time_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryDeviceVodUrlByTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDeviceVodUrlByTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.enable_stun):
            query['EnableStun'] = request.enable_stun
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.play_un_limited):
            query['PlayUnLimited'] = request.play_un_limited
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.scheme):
            query['Scheme'] = request.scheme
        if not UtilClient.is_unset(request.seek_time):
            query['SeekTime'] = request.seek_time
        if not UtilClient.is_unset(request.should_encrypt):
            query['ShouldEncrypt'] = request.should_encrypt
        if not UtilClient.is_unset(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceVodUrlByTime',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDeviceVodUrlByTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_device_vod_url_by_time(
        self,
        request: linkvisual_20180120_models.QueryDeviceVodUrlByTimeRequest,
    ) -> linkvisual_20180120_models.QueryDeviceVodUrlByTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_device_vod_url_by_time_with_options(request, runtime)

    async def query_device_vod_url_by_time_async(
        self,
        request: linkvisual_20180120_models.QueryDeviceVodUrlByTimeRequest,
    ) -> linkvisual_20180120_models.QueryDeviceVodUrlByTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_device_vod_url_by_time_with_options_async(request, runtime)

    def query_event_record_plan_detail_with_options(
        self,
        request: linkvisual_20180120_models.QueryEventRecordPlanDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryEventRecordPlanDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEventRecordPlanDetail',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryEventRecordPlanDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_event_record_plan_detail_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryEventRecordPlanDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryEventRecordPlanDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEventRecordPlanDetail',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryEventRecordPlanDetailResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEventRecordPlanDeviceByDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryEventRecordPlanDeviceByDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_event_record_plan_device_by_device_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryEventRecordPlanDeviceByDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryEventRecordPlanDeviceByDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEventRecordPlanDeviceByDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryEventRecordPlanDeviceByDeviceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEventRecordPlanDeviceByPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryEventRecordPlanDeviceByPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_event_record_plan_device_by_plan_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryEventRecordPlanDeviceByPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryEventRecordPlanDeviceByPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEventRecordPlanDeviceByPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryEventRecordPlanDeviceByPlanResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEventRecordPlans',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryEventRecordPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_event_record_plans_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryEventRecordPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryEventRecordPlansResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEventRecordPlans',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryEventRecordPlansResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceAllDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceAllDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_all_device_group_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryFaceAllDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceAllDeviceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceAllDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceAllDeviceGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceAllUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceAllUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_all_user_group_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryFaceAllUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceAllUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceAllUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceAllUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceAllUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceAllUserGroupAndDeviceGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_all_user_group_and_device_group_relation_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryFaceAllUserGroupAndDeviceGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceAllUserGroupAndDeviceGroupRelationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceAllUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceAllUserGroupAndDeviceGroupRelationResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceAllUserIdsByGroupId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceAllUserIdsByGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_all_user_ids_by_group_id_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryFaceAllUserIdsByGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceAllUserIdsByGroupIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceAllUserIdsByGroupId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceAllUserIdsByGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceCustomUserIdByUserId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceCustomUserIdByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_custom_user_id_by_user_id_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryFaceCustomUserIdByUserIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceCustomUserIdByUserIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceCustomUserIdByUserId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceCustomUserIdByUserIdResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceDeviceGroupsByDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceDeviceGroupsByDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_device_groups_by_device_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryFaceDeviceGroupsByDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceDeviceGroupsByDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceDeviceGroupsByDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceDeviceGroupsByDeviceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceUser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_user_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryFaceUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceUser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceUserResponse(),
            await self.call_api_async(params, req, runtime)
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

    def query_face_user_batch_with_options(
        self,
        request: linkvisual_20180120_models.QueryFaceUserBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceUserBatchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceUserBatch',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceUserBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_user_batch_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryFaceUserBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceUserBatchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceUserBatch',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceUserBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_face_user_batch(
        self,
        request: linkvisual_20180120_models.QueryFaceUserBatchRequest,
    ) -> linkvisual_20180120_models.QueryFaceUserBatchResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_face_user_batch_with_options(request, runtime)

    async def query_face_user_batch_async(
        self,
        request: linkvisual_20180120_models.QueryFaceUserBatchRequest,
    ) -> linkvisual_20180120_models.QueryFaceUserBatchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_face_user_batch_with_options_async(request, runtime)

    def query_face_user_by_name_with_options(
        self,
        request: linkvisual_20180120_models.QueryFaceUserByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceUserByNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceUserByName',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceUserByNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_user_by_name_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryFaceUserByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceUserByNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceUserByName',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceUserByNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_face_user_by_name(
        self,
        request: linkvisual_20180120_models.QueryFaceUserByNameRequest,
    ) -> linkvisual_20180120_models.QueryFaceUserByNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_face_user_by_name_with_options(request, runtime)

    async def query_face_user_by_name_async(
        self,
        request: linkvisual_20180120_models.QueryFaceUserByNameRequest,
    ) -> linkvisual_20180120_models.QueryFaceUserByNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_face_user_by_name_with_options_async(request, runtime)

    def query_face_user_group_with_options(
        self,
        request: linkvisual_20180120_models.QueryFaceUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_user_group_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryFaceUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.control_id):
            query['ControlId'] = request.control_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceUserGroupAndDeviceGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_user_group_and_device_group_relation_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryFaceUserGroupAndDeviceGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceUserGroupAndDeviceGroupRelationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.control_id):
            query['ControlId'] = request.control_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceUserGroupAndDeviceGroupRelationResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceUserIdByCustomUserId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceUserIdByCustomUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_user_id_by_custom_user_id_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryFaceUserIdByCustomUserIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceUserIdByCustomUserIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceUserIdByCustomUserId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceUserIdByCustomUserIdResponse(),
            await self.call_api_async(params, req, runtime)
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

    def query_gb_sub_device_list_with_options(
        self,
        request: linkvisual_20180120_models.QueryGbSubDeviceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryGbSubDeviceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_start):
            query['PageStart'] = request.page_start
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGbSubDeviceList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryGbSubDeviceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_gb_sub_device_list_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryGbSubDeviceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryGbSubDeviceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_start):
            query['PageStart'] = request.page_start
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGbSubDeviceList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryGbSubDeviceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_gb_sub_device_list(
        self,
        request: linkvisual_20180120_models.QueryGbSubDeviceListRequest,
    ) -> linkvisual_20180120_models.QueryGbSubDeviceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_gb_sub_device_list_with_options(request, runtime)

    async def query_gb_sub_device_list_async(
        self,
        request: linkvisual_20180120_models.QueryGbSubDeviceListRequest,
    ) -> linkvisual_20180120_models.QueryGbSubDeviceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_gb_sub_device_list_with_options_async(request, runtime)

    def query_live_streaming_with_options(
        self,
        request: linkvisual_20180120_models.QueryLiveStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryLiveStreamingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_duration):
            query['CacheDuration'] = request.cache_duration
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.enable_stun):
            query['EnableStun'] = request.enable_stun
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.force_iframe):
            query['ForceIFrame'] = request.force_iframe
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.play_un_limited):
            query['PlayUnLimited'] = request.play_un_limited
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.scheme):
            query['Scheme'] = request.scheme
        if not UtilClient.is_unset(request.should_encrypt):
            query['ShouldEncrypt'] = request.should_encrypt
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        if not UtilClient.is_unset(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryLiveStreaming',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryLiveStreamingResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_live_streaming_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryLiveStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryLiveStreamingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_duration):
            query['CacheDuration'] = request.cache_duration
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.enable_stun):
            query['EnableStun'] = request.enable_stun
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.force_iframe):
            query['ForceIFrame'] = request.force_iframe
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.play_un_limited):
            query['PlayUnLimited'] = request.play_un_limited
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.scheme):
            query['Scheme'] = request.scheme
        if not UtilClient.is_unset(request.should_encrypt):
            query['ShouldEncrypt'] = request.should_encrypt
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        if not UtilClient.is_unset(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryLiveStreaming',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryLiveStreamingResponse(),
            await self.call_api_async(params, req, runtime)
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

    def query_local_file_upload_job_with_options(
        self,
        request: linkvisual_20180120_models.QueryLocalFileUploadJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryLocalFileUploadJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryLocalFileUploadJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryLocalFileUploadJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_local_file_upload_job_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryLocalFileUploadJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryLocalFileUploadJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryLocalFileUploadJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryLocalFileUploadJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_local_file_upload_job(
        self,
        request: linkvisual_20180120_models.QueryLocalFileUploadJobRequest,
    ) -> linkvisual_20180120_models.QueryLocalFileUploadJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_local_file_upload_job_with_options(request, runtime)

    async def query_local_file_upload_job_async(
        self,
        request: linkvisual_20180120_models.QueryLocalFileUploadJobRequest,
    ) -> linkvisual_20180120_models.QueryLocalFileUploadJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_local_file_upload_job_with_options_async(request, runtime)

    def query_month_record_with_options(
        self,
        request: linkvisual_20180120_models.QueryMonthRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryMonthRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.month):
            query['Month'] = request.month
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMonthRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryMonthRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_month_record_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryMonthRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryMonthRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.month):
            query['Month'] = request.month
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMonthRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryMonthRecordResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.picture_source):
            query['PictureSource'] = request.picture_source
        if not UtilClient.is_unset(request.picture_type):
            query['PictureType'] = request.picture_type
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPictureFiles',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryPictureFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_picture_files_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryPictureFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryPictureFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.picture_source):
            query['PictureSource'] = request.picture_source
        if not UtilClient.is_unset(request.picture_type):
            query['PictureType'] = request.picture_type
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPictureFiles',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryPictureFilesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPictureSearchAiboxes',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryPictureSearchAiboxesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_picture_search_aiboxes_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchAiboxesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryPictureSearchAiboxesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPictureSearchAiboxes',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryPictureSearchAiboxesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def query_picture_search_apps_with_options(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryPictureSearchAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPictureSearchApps',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryPictureSearchAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_picture_search_apps_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryPictureSearchAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPictureSearchApps',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryPictureSearchAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_picture_search_apps(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchAppsRequest,
    ) -> linkvisual_20180120_models.QueryPictureSearchAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_picture_search_apps_with_options(request, runtime)

    async def query_picture_search_apps_async(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchAppsRequest,
    ) -> linkvisual_20180120_models.QueryPictureSearchAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_picture_search_apps_with_options_async(request, runtime)

    def query_picture_search_devices_with_options(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryPictureSearchDevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPictureSearchDevices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryPictureSearchDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_picture_search_devices_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryPictureSearchDevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPictureSearchDevices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryPictureSearchDevicesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def query_picture_search_job_with_options(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryPictureSearchJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.job_status):
            query['JobStatus'] = request.job_status
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPictureSearchJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryPictureSearchJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_picture_search_job_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryPictureSearchJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.job_status):
            query['JobStatus'] = request.job_status
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPictureSearchJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryPictureSearchJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_picture_search_job(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchJobRequest,
    ) -> linkvisual_20180120_models.QueryPictureSearchJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_picture_search_job_with_options(request, runtime)

    async def query_picture_search_job_async(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchJobRequest,
    ) -> linkvisual_20180120_models.QueryPictureSearchJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_picture_search_job_with_options_async(request, runtime)

    def query_picture_search_job_result_with_options(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryPictureSearchJobResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPictureSearchJobResult',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryPictureSearchJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_picture_search_job_result_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryPictureSearchJobResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPictureSearchJobResult',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryPictureSearchJobResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_picture_search_job_result(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchJobResultRequest,
    ) -> linkvisual_20180120_models.QueryPictureSearchJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_picture_search_job_result_with_options(request, runtime)

    async def query_picture_search_job_result_async(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchJobResultRequest,
    ) -> linkvisual_20180120_models.QueryPictureSearchJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_picture_search_job_result_with_options_async(request, runtime)

    def query_record_with_options(
        self,
        request: linkvisual_20180120_models.QueryRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.need_snapshot):
            query['NeedSnapshot'] = request.need_snapshot
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.record_type):
            query['RecordType'] = request.record_type
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_record_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.need_snapshot):
            query['NeedSnapshot'] = request.need_snapshot
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.record_type):
            query['RecordType'] = request.record_type
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordByRecordId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordByRecordIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_record_by_record_id_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryRecordByRecordIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordByRecordIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordByRecordId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordByRecordIdResponse(),
            await self.call_api_async(params, req, runtime)
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

    def query_record_download_job_by_id_with_options(
        self,
        request: linkvisual_20180120_models.QueryRecordDownloadJobByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordDownloadJobByIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordDownloadJobById',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordDownloadJobByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_record_download_job_by_id_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryRecordDownloadJobByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordDownloadJobByIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordDownloadJobById',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordDownloadJobByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_record_download_job_by_id(
        self,
        request: linkvisual_20180120_models.QueryRecordDownloadJobByIdRequest,
    ) -> linkvisual_20180120_models.QueryRecordDownloadJobByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_record_download_job_by_id_with_options(request, runtime)

    async def query_record_download_job_by_id_async(
        self,
        request: linkvisual_20180120_models.QueryRecordDownloadJobByIdRequest,
    ) -> linkvisual_20180120_models.QueryRecordDownloadJobByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_record_download_job_by_id_with_options_async(request, runtime)

    def query_record_download_job_list_with_options(
        self,
        request: linkvisual_20180120_models.QueryRecordDownloadJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordDownloadJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordDownloadJobList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordDownloadJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_record_download_job_list_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryRecordDownloadJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordDownloadJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordDownloadJobList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordDownloadJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_record_download_job_list(
        self,
        request: linkvisual_20180120_models.QueryRecordDownloadJobListRequest,
    ) -> linkvisual_20180120_models.QueryRecordDownloadJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_record_download_job_list_with_options(request, runtime)

    async def query_record_download_job_list_async(
        self,
        request: linkvisual_20180120_models.QueryRecordDownloadJobListRequest,
    ) -> linkvisual_20180120_models.QueryRecordDownloadJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_record_download_job_list_with_options_async(request, runtime)

    def query_record_download_url_with_options(
        self,
        request: linkvisual_20180120_models.QueryRecordDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordDownloadUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordDownloadUrl',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_record_download_url_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryRecordDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordDownloadUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordDownloadUrl',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_record_download_url(
        self,
        request: linkvisual_20180120_models.QueryRecordDownloadUrlRequest,
    ) -> linkvisual_20180120_models.QueryRecordDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_record_download_url_with_options(request, runtime)

    async def query_record_download_url_async(
        self,
        request: linkvisual_20180120_models.QueryRecordDownloadUrlRequest,
    ) -> linkvisual_20180120_models.QueryRecordDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_record_download_url_with_options_async(request, runtime)

    def query_record_plan_detail_with_options(
        self,
        request: linkvisual_20180120_models.QueryRecordPlanDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordPlanDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordPlanDetail',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordPlanDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_record_plan_detail_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryRecordPlanDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordPlanDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordPlanDetail',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordPlanDetailResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordPlanDeviceByDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordPlanDeviceByDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_record_plan_device_by_device_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryRecordPlanDeviceByDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordPlanDeviceByDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordPlanDeviceByDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordPlanDeviceByDeviceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordPlanDeviceByPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordPlanDeviceByPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_record_plan_device_by_plan_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryRecordPlanDeviceByPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordPlanDeviceByPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordPlanDeviceByPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordPlanDeviceByPlanResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordPlans',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_record_plans_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryRecordPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordPlansResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordPlans',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordPlansResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.seek_time):
            query['SeekTime'] = request.seek_time
        if not UtilClient.is_unset(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordUrl',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_record_url_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryRecordUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.seek_time):
            query['SeekTime'] = request.seek_time
        if not UtilClient.is_unset(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordUrl',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordUrlResponse(),
            await self.call_api_async(params, req, runtime)
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

    def query_record_url_by_time_with_options(
        self,
        request: linkvisual_20180120_models.QueryRecordUrlByTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordUrlByTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        if not UtilClient.is_unset(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordUrlByTime',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordUrlByTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_record_url_by_time_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryRecordUrlByTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordUrlByTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        if not UtilClient.is_unset(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordUrlByTime',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordUrlByTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_record_url_by_time(
        self,
        request: linkvisual_20180120_models.QueryRecordUrlByTimeRequest,
    ) -> linkvisual_20180120_models.QueryRecordUrlByTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_record_url_by_time_with_options(request, runtime)

    async def query_record_url_by_time_async(
        self,
        request: linkvisual_20180120_models.QueryRecordUrlByTimeRequest,
    ) -> linkvisual_20180120_models.QueryRecordUrlByTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_record_url_by_time_with_options_async(request, runtime)

    def query_rtmp_key_with_options(
        self,
        request: linkvisual_20180120_models.QueryRtmpKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRtmpKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRtmpKey',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRtmpKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_rtmp_key_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryRtmpKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRtmpKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRtmpKey',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRtmpKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_rtmp_key(
        self,
        request: linkvisual_20180120_models.QueryRtmpKeyRequest,
    ) -> linkvisual_20180120_models.QueryRtmpKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_rtmp_key_with_options(request, runtime)

    async def query_rtmp_key_async(
        self,
        request: linkvisual_20180120_models.QueryRtmpKeyRequest,
    ) -> linkvisual_20180120_models.QueryRtmpKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_rtmp_key_with_options_async(request, runtime)

    def query_stream_push_job_with_options(
        self,
        request: linkvisual_20180120_models.QueryStreamPushJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryStreamPushJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStreamPushJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryStreamPushJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_stream_push_job_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryStreamPushJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryStreamPushJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStreamPushJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryStreamPushJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_stream_push_job(
        self,
        request: linkvisual_20180120_models.QueryStreamPushJobRequest,
    ) -> linkvisual_20180120_models.QueryStreamPushJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_stream_push_job_with_options(request, runtime)

    async def query_stream_push_job_async(
        self,
        request: linkvisual_20180120_models.QueryStreamPushJobRequest,
    ) -> linkvisual_20180120_models.QueryStreamPushJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_stream_push_job_with_options_async(request, runtime)

    def query_stream_push_job_list_with_options(
        self,
        request: linkvisual_20180120_models.QueryStreamPushJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryStreamPushJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStreamPushJobList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryStreamPushJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_stream_push_job_list_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryStreamPushJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryStreamPushJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStreamPushJobList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryStreamPushJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_stream_push_job_list(
        self,
        request: linkvisual_20180120_models.QueryStreamPushJobListRequest,
    ) -> linkvisual_20180120_models.QueryStreamPushJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_stream_push_job_list_with_options(request, runtime)

    async def query_stream_push_job_list_async(
        self,
        request: linkvisual_20180120_models.QueryStreamPushJobListRequest,
    ) -> linkvisual_20180120_models.QueryStreamPushJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_stream_push_job_list_with_options_async(request, runtime)

    def query_stream_snapshot_job_with_options(
        self,
        request: linkvisual_20180120_models.QueryStreamSnapshotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryStreamSnapshotJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStreamSnapshotJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryStreamSnapshotJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_stream_snapshot_job_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryStreamSnapshotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryStreamSnapshotJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStreamSnapshotJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryStreamSnapshotJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_stream_snapshot_job(
        self,
        request: linkvisual_20180120_models.QueryStreamSnapshotJobRequest,
    ) -> linkvisual_20180120_models.QueryStreamSnapshotJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_stream_snapshot_job_with_options(request, runtime)

    async def query_stream_snapshot_job_async(
        self,
        request: linkvisual_20180120_models.QueryStreamSnapshotJobRequest,
    ) -> linkvisual_20180120_models.QueryStreamSnapshotJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_stream_snapshot_job_with_options_async(request, runtime)

    def query_time_template_with_options(
        self,
        request: linkvisual_20180120_models.QueryTimeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryTimeTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTimeTemplate',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryTimeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_time_template_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryTimeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryTimeTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTimeTemplate',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryTimeTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTimeTemplateDetail',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryTimeTemplateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_time_template_detail_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryTimeTemplateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryTimeTemplateDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTimeTemplateDetail',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryTimeTemplateDetailResponse(),
            await self.call_api_async(params, req, runtime)
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

    def query_vision_device_info_with_options(
        self,
        request: linkvisual_20180120_models.QueryVisionDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryVisionDeviceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryVisionDeviceInfo',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryVisionDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_vision_device_info_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryVisionDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryVisionDeviceInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryVisionDeviceInfo',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryVisionDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_vision_device_info(
        self,
        request: linkvisual_20180120_models.QueryVisionDeviceInfoRequest,
    ) -> linkvisual_20180120_models.QueryVisionDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_vision_device_info_with_options(request, runtime)

    async def query_vision_device_info_async(
        self,
        request: linkvisual_20180120_models.QueryVisionDeviceInfoRequest,
    ) -> linkvisual_20180120_models.QueryVisionDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_vision_device_info_with_options_async(request, runtime)

    def query_voice_intercom_with_options(
        self,
        request: linkvisual_20180120_models.QueryVoiceIntercomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryVoiceIntercomResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.scheme):
            query['Scheme'] = request.scheme
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryVoiceIntercom',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryVoiceIntercomResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_voice_intercom_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryVoiceIntercomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryVoiceIntercomResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.scheme):
            query['Scheme'] = request.scheme
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryVoiceIntercom',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryVoiceIntercomResponse(),
            await self.call_api_async(params, req, runtime)
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

    def refresh_gb_sub_device_list_with_options(
        self,
        request: linkvisual_20180120_models.RefreshGbSubDeviceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.RefreshGbSubDeviceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshGbSubDeviceList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.RefreshGbSubDeviceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_gb_sub_device_list_with_options_async(
        self,
        request: linkvisual_20180120_models.RefreshGbSubDeviceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.RefreshGbSubDeviceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshGbSubDeviceList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.RefreshGbSubDeviceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_gb_sub_device_list(
        self,
        request: linkvisual_20180120_models.RefreshGbSubDeviceListRequest,
    ) -> linkvisual_20180120_models.RefreshGbSubDeviceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_gb_sub_device_list_with_options(request, runtime)

    async def refresh_gb_sub_device_list_async(
        self,
        request: linkvisual_20180120_models.RefreshGbSubDeviceListRequest,
    ) -> linkvisual_20180120_models.RefreshGbSubDeviceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_gb_sub_device_list_with_options_async(request, runtime)

    def remove_face_device_from_device_group_with_options(
        self,
        request: linkvisual_20180120_models.RemoveFaceDeviceFromDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.RemoveFaceDeviceFromDeviceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveFaceDeviceFromDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.RemoveFaceDeviceFromDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_face_device_from_device_group_with_options_async(
        self,
        request: linkvisual_20180120_models.RemoveFaceDeviceFromDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.RemoveFaceDeviceFromDeviceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveFaceDeviceFromDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.RemoveFaceDeviceFromDeviceGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveFaceUserFromUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.RemoveFaceUserFromUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_face_user_from_user_group_with_options_async(
        self,
        request: linkvisual_20180120_models.RemoveFaceUserFromUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.RemoveFaceUserFromUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveFaceUserFromUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.RemoveFaceUserFromUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.day):
            query['Day'] = request.day
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDevicePictureLifeCycle',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.SetDevicePictureLifeCycleResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_device_picture_life_cycle_with_options_async(
        self,
        request: linkvisual_20180120_models.SetDevicePictureLifeCycleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.SetDevicePictureLifeCycleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.day):
            query['Day'] = request.day
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDevicePictureLifeCycle',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.SetDevicePictureLifeCycleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.day):
            query['Day'] = request.day
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDeviceRecordLifeCycle',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.SetDeviceRecordLifeCycleResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_device_record_life_cycle_with_options_async(
        self,
        request: linkvisual_20180120_models.SetDeviceRecordLifeCycleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.SetDeviceRecordLifeCycleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.day):
            query['Day'] = request.day
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDeviceRecordLifeCycle',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.SetDeviceRecordLifeCycleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopLiveStreaming',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.StopLiveStreamingResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_live_streaming_with_options_async(
        self,
        request: linkvisual_20180120_models.StopLiveStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.StopLiveStreamingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopLiveStreaming',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.StopLiveStreamingResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopTriggeredRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.StopTriggeredRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_triggered_record_with_options_async(
        self,
        request: linkvisual_20180120_models.StopTriggeredRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.StopTriggeredRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopTriggeredRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.StopTriggeredRecordResponse(),
            await self.call_api_async(params, req, runtime)
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

    def transfer_device_instance_with_options(
        self,
        request: linkvisual_20180120_models.TransferDeviceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.TransferDeviceInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name_list):
            query['DeviceNameList'] = request.device_name_list
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not UtilClient.is_unset(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferDeviceInstance',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.TransferDeviceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_device_instance_with_options_async(
        self,
        request: linkvisual_20180120_models.TransferDeviceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.TransferDeviceInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name_list):
            query['DeviceNameList'] = request.device_name_list
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not UtilClient.is_unset(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferDeviceInstance',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.TransferDeviceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_device_instance(
        self,
        request: linkvisual_20180120_models.TransferDeviceInstanceRequest,
    ) -> linkvisual_20180120_models.TransferDeviceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.transfer_device_instance_with_options(request, runtime)

    async def transfer_device_instance_async(
        self,
        request: linkvisual_20180120_models.TransferDeviceInstanceRequest,
    ) -> linkvisual_20180120_models.TransferDeviceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transfer_device_instance_with_options_async(request, runtime)

    def trigger_capture_picture_with_options(
        self,
        request: linkvisual_20180120_models.TriggerCapturePictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.TriggerCapturePictureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerCapturePicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.TriggerCapturePictureResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_capture_picture_with_options_async(
        self,
        request: linkvisual_20180120_models.TriggerCapturePictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.TriggerCapturePictureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerCapturePicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.TriggerCapturePictureResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.record_duration):
            query['RecordDuration'] = request.record_duration
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.TriggerRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_record_with_options_async(
        self,
        request: linkvisual_20180120_models.TriggerRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.TriggerRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.record_duration):
            query['RecordDuration'] = request.record_duration
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.TriggerRecordResponse(),
            await self.call_api_async(params, req, runtime)
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

    def unbind_picture_search_app_with_devices_with_options(
        self,
        request: linkvisual_20180120_models.UnbindPictureSearchAppWithDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UnbindPictureSearchAppWithDevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.device_iot_ids):
            query['DeviceIotIds'] = request.device_iot_ids
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindPictureSearchAppWithDevices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UnbindPictureSearchAppWithDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_picture_search_app_with_devices_with_options_async(
        self,
        request: linkvisual_20180120_models.UnbindPictureSearchAppWithDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UnbindPictureSearchAppWithDevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.device_iot_ids):
            query['DeviceIotIds'] = request.device_iot_ids
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindPictureSearchAppWithDevices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UnbindPictureSearchAppWithDevicesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def update_event_record_plan_with_options(
        self,
        request: linkvisual_20180120_models.UpdateEventRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateEventRecordPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_types):
            query['EventTypes'] = request.event_types
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not UtilClient.is_unset(request.record_duration):
            query['RecordDuration'] = request.record_duration
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEventRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateEventRecordPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_event_record_plan_with_options_async(
        self,
        request: linkvisual_20180120_models.UpdateEventRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateEventRecordPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_types):
            query['EventTypes'] = request.event_types
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not UtilClient.is_unset(request.record_duration):
            query['RecordDuration'] = request.record_duration
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEventRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateEventRecordPlanResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not UtilClient.is_unset(request.face_pic_url):
            query['FacePicUrl'] = request.face_pic_url
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFaceUser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateFaceUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_face_user_with_options_async(
        self,
        request: linkvisual_20180120_models.UpdateFaceUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateFaceUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not UtilClient.is_unset(request.face_pic_url):
            query['FacePicUrl'] = request.face_pic_url
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFaceUser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateFaceUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.control_id):
            query['ControlId'] = request.control_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.relation):
            query['Relation'] = request.relation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFaceUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateFaceUserGroupAndDeviceGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_face_user_group_and_device_group_relation_with_options_async(
        self,
        request: linkvisual_20180120_models.UpdateFaceUserGroupAndDeviceGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateFaceUserGroupAndDeviceGroupRelationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.control_id):
            query['ControlId'] = request.control_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.relation):
            query['Relation'] = request.relation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFaceUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateFaceUserGroupAndDeviceGroupRelationResponse(),
            await self.call_api_async(params, req, runtime)
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

    def update_gb_device_with_options(
        self,
        request: linkvisual_20180120_models.UpdateGbDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateGbDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.gb_id):
            query['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGbDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateGbDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gb_device_with_options_async(
        self,
        request: linkvisual_20180120_models.UpdateGbDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateGbDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.gb_id):
            query['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGbDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateGbDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gb_device(
        self,
        request: linkvisual_20180120_models.UpdateGbDeviceRequest,
    ) -> linkvisual_20180120_models.UpdateGbDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_gb_device_with_options(request, runtime)

    async def update_gb_device_async(
        self,
        request: linkvisual_20180120_models.UpdateGbDeviceRequest,
    ) -> linkvisual_20180120_models.UpdateGbDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_gb_device_with_options_async(request, runtime)

    def update_instance_internet_protocol_with_options(
        self,
        request: linkvisual_20180120_models.UpdateInstanceInternetProtocolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateInstanceInternetProtocolResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceInternetProtocol',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateInstanceInternetProtocolResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_internet_protocol_with_options_async(
        self,
        request: linkvisual_20180120_models.UpdateInstanceInternetProtocolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateInstanceInternetProtocolResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceInternetProtocol',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateInstanceInternetProtocolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_internet_protocol(
        self,
        request: linkvisual_20180120_models.UpdateInstanceInternetProtocolRequest,
    ) -> linkvisual_20180120_models.UpdateInstanceInternetProtocolResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_instance_internet_protocol_with_options(request, runtime)

    async def update_instance_internet_protocol_async(
        self,
        request: linkvisual_20180120_models.UpdateInstanceInternetProtocolRequest,
    ) -> linkvisual_20180120_models.UpdateInstanceInternetProtocolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_internet_protocol_with_options_async(request, runtime)

    def update_picture_search_app_with_options(
        self,
        request: linkvisual_20180120_models.UpdatePictureSearchAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdatePictureSearchAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePictureSearchApp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdatePictureSearchAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_picture_search_app_with_options_async(
        self,
        request: linkvisual_20180120_models.UpdatePictureSearchAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdatePictureSearchAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePictureSearchApp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdatePictureSearchAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_picture_search_app(
        self,
        request: linkvisual_20180120_models.UpdatePictureSearchAppRequest,
    ) -> linkvisual_20180120_models.UpdatePictureSearchAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_picture_search_app_with_options(request, runtime)

    async def update_picture_search_app_async(
        self,
        request: linkvisual_20180120_models.UpdatePictureSearchAppRequest,
    ) -> linkvisual_20180120_models.UpdatePictureSearchAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_picture_search_app_with_options_async(request, runtime)

    def update_record_plan_with_options(
        self,
        request: linkvisual_20180120_models.UpdateRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateRecordPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateRecordPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_record_plan_with_options_async(
        self,
        request: linkvisual_20180120_models.UpdateRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateRecordPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateRecordPlanResponse(),
            await self.call_api_async(params, req, runtime)
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

    def update_rtmp_key_with_options(
        self,
        request: linkvisual_20180120_models.UpdateRtmpKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateRtmpKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.pull_auth_key):
            query['PullAuthKey'] = request.pull_auth_key
        if not UtilClient.is_unset(request.pull_key_expire_time):
            query['PullKeyExpireTime'] = request.pull_key_expire_time
        if not UtilClient.is_unset(request.push_auth_key):
            query['PushAuthKey'] = request.push_auth_key
        if not UtilClient.is_unset(request.push_key_expire_time):
            query['PushKeyExpireTime'] = request.push_key_expire_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRtmpKey',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateRtmpKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rtmp_key_with_options_async(
        self,
        request: linkvisual_20180120_models.UpdateRtmpKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateRtmpKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.pull_auth_key):
            query['PullAuthKey'] = request.pull_auth_key
        if not UtilClient.is_unset(request.pull_key_expire_time):
            query['PullKeyExpireTime'] = request.pull_key_expire_time
        if not UtilClient.is_unset(request.push_auth_key):
            query['PushAuthKey'] = request.push_auth_key
        if not UtilClient.is_unset(request.push_key_expire_time):
            query['PushKeyExpireTime'] = request.push_key_expire_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRtmpKey',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateRtmpKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rtmp_key(
        self,
        request: linkvisual_20180120_models.UpdateRtmpKeyRequest,
    ) -> linkvisual_20180120_models.UpdateRtmpKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_rtmp_key_with_options(request, runtime)

    async def update_rtmp_key_async(
        self,
        request: linkvisual_20180120_models.UpdateRtmpKeyRequest,
    ) -> linkvisual_20180120_models.UpdateRtmpKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_rtmp_key_with_options_async(request, runtime)

    def update_time_template_with_options(
        self,
        request: linkvisual_20180120_models.UpdateTimeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateTimeTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_day):
            query['AllDay'] = request.all_day
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.time_sections):
            query['TimeSections'] = request.time_sections
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTimeTemplate',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateTimeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_time_template_with_options_async(
        self,
        request: linkvisual_20180120_models.UpdateTimeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateTimeTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_day):
            query['AllDay'] = request.all_day
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.time_sections):
            query['TimeSections'] = request.time_sections
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTimeTemplate',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateTimeTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
