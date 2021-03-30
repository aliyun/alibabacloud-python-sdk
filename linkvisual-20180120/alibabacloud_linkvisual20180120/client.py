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
        query['IotId'] = request.iot_id
        query['PlanId'] = request.plan_id
        query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddEventRecordPlanDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['PlanId'] = request.plan_id
        query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddEventRecordPlanDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['DeviceGroupName'] = request.device_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddFaceDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['DeviceGroupName'] = request.device_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddFaceDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['IotInstanceId'] = request.iot_instance_id
        query['ProductKey'] = request.product_key
        query['DeviceName'] = request.device_name
        query['DeviceGroupId'] = request.device_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddFaceDeviceToDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['IotInstanceId'] = request.iot_instance_id
        query['ProductKey'] = request.product_key
        query['DeviceName'] = request.device_name
        query['DeviceGroupId'] = request.device_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddFaceDeviceToDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['FacePicUrl'] = request.face_pic_url
        query['CustomUserId'] = request.custom_user_id
        query['Name'] = request.name
        query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddFaceUser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['FacePicUrl'] = request.face_pic_url
        query['CustomUserId'] = request.custom_user_id
        query['Name'] = request.name
        query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddFaceUser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['UserGroupName'] = request.user_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddFaceUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['UserGroupName'] = request.user_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddFaceUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['IotInstanceId'] = request.iot_instance_id
        query['UserGroupId'] = request.user_group_id
        query['DeviceGroupId'] = request.device_group_id
        query['Relation'] = request.relation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddFaceUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['IotInstanceId'] = request.iot_instance_id
        query['UserGroupId'] = request.user_group_id
        query['DeviceGroupId'] = request.device_group_id
        query['Relation'] = request.relation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddFaceUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['UserId'] = request.user_id
        query['FacePicUrl'] = request.face_pic_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddFaceUserPicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['UserId'] = request.user_id
        query['FacePicUrl'] = request.face_pic_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddFaceUserPicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['UserId'] = request.user_id
        query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddFaceUserToUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['UserId'] = request.user_id
        query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddFaceUserToUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['PlanId'] = request.plan_id
        query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddRecordPlanDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['PlanId'] = request.plan_id
        query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddRecordPlanDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def bind_aiplan_with_devices_with_options(
        self,
        request: linkvisual_20180120_models.BindAIPlanWithDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.BindAIPlanWithDevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PlanId'] = request.plan_id
        query['IotIdList'] = request.iot_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BindAIPlanWithDevices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.BindAIPlanWithDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_aiplan_with_devices_with_options_async(
        self,
        request: linkvisual_20180120_models.BindAIPlanWithDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.BindAIPlanWithDevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PlanId'] = request.plan_id
        query['IotIdList'] = request.iot_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BindAIPlanWithDevices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.BindAIPlanWithDevicesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AppInstanceId'] = request.app_instance_id
        query['IotInstanceId'] = request.iot_instance_id
        query['DeviceIotIds'] = request.device_iot_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BindPictureSearchAppWithDevices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['AppInstanceId'] = request.app_instance_id
        query['IotInstanceId'] = request.iot_instance_id
        query['DeviceIotIds'] = request.device_iot_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BindPictureSearchAppWithDevices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['IotInstanceId'] = request.iot_instance_id
        query['UserId'] = request.user_id
        query['ProductKey'] = request.product_key
        query['DeviceName'] = request.device_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckFaceUserDoExistOnDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['IotInstanceId'] = request.iot_instance_id
        query['UserId'] = request.user_id
        query['ProductKey'] = request.product_key
        query['DeviceName'] = request.device_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckFaceUserDoExistOnDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['IotInstanceId'] = request.iot_instance_id
        query['ProductKey'] = request.product_key
        query['DeviceName'] = request.device_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ClearFaceDeviceDB',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['IotInstanceId'] = request.iot_instance_id
        query['ProductKey'] = request.product_key
        query['DeviceName'] = request.device_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ClearFaceDeviceDB',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def config_aiaction_with_options(
        self,
        request: linkvisual_20180120_models.ConfigAIActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.ConfigAIActionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ActionId'] = request.action_id
        query['AlgoConfig'] = request.algo_config
        query['DataTypeConfigList'] = request.data_type_config_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ConfigAIAction',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.ConfigAIActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_aiaction_with_options_async(
        self,
        request: linkvisual_20180120_models.ConfigAIActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.ConfigAIActionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ActionId'] = request.action_id
        query['AlgoConfig'] = request.algo_config
        query['DataTypeConfigList'] = request.data_type_config_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ConfigAIAction',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.ConfigAIActionResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AppTemplateId'] = request.app_template_id
        query['AppTemplateVersion'] = request.app_template_version
        query['Level'] = request.level
        query['Name'] = request.name
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAIApp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateAIAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aiapp_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateAIAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateAIAppResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppTemplateId'] = request.app_template_id
        query['AppTemplateVersion'] = request.app_template_version
        query['Level'] = request.level
        query['Name'] = request.name
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAIApp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateAIAppResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AppId'] = request.app_id
        query['PlanTemplateId'] = request.plan_template_id
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAIPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateAIPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aiplan_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateAIPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateAIPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['PlanTemplateId'] = request.plan_template_id
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAIPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateAIPlanResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Name'] = request.name
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAlgorithm',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateAlgorithmResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_algorithm_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateAlgorithmResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAlgorithm',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateAlgorithmResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['IotId'] = request.iot_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDevicePurifyJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateDevicePurifyJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_device_purify_job_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateDevicePurifyJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateDevicePurifyJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IotId'] = request.iot_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDevicePurifyJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateDevicePurifyJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PlanId'] = request.plan_id
        query['Utc'] = request.utc
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDevicePurifyJobByPlanId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateDevicePurifyJobByPlanIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_device_purify_job_by_plan_id_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateDevicePurifyJobByPlanIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateDevicePurifyJobByPlanIdResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PlanId'] = request.plan_id
        query['Utc'] = request.utc
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDevicePurifyJobByPlanId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateDevicePurifyJobByPlanIdResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['IotId'] = request.iot_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDevicePurifyPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateDevicePurifyPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_device_purify_plan_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateDevicePurifyPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateDevicePurifyPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IotId'] = request.iot_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDevicePurifyPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateDevicePurifyPlanResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Name'] = request.name
        query['EventTypes'] = request.event_types
        query['PreRecordDuration'] = request.pre_record_duration
        query['RecordDuration'] = request.record_duration
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateEventRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Name'] = request.name
        query['EventTypes'] = request.event_types
        query['PreRecordDuration'] = request.pre_record_duration
        query['RecordDuration'] = request.record_duration
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateEventRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def create_model_with_options(
        self,
        request: linkvisual_20180120_models.CreateModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateModelResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AlgorithmId'] = request.algorithm_id
        query['Name'] = request.name
        query['ModelPackageStandard'] = request.model_package_standard
        query['Hardware'] = request.hardware
        query['UploadModelPath'] = request.upload_model_path
        query['NeedEncrypt'] = request.need_encrypt
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateModel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_with_options_async(
        self,
        request: linkvisual_20180120_models.CreateModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateModelResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AlgorithmId'] = request.algorithm_id
        query['Name'] = request.name
        query['ModelPackageStandard'] = request.model_package_standard
        query['Hardware'] = request.hardware
        query['UploadModelPath'] = request.upload_model_path
        query['NeedEncrypt'] = request.need_encrypt
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateModel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateModelResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Name'] = request.name
        query['Desc'] = request.desc
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreatePictureSearchApp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Name'] = request.name
        query['Desc'] = request.desc
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreatePictureSearchApp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['AppInstanceId'] = request.app_instance_id
        query['SearchPicUrl'] = request.search_pic_url
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Threshold'] = request.threshold
        query['BodyThreshold'] = request.body_threshold
        query['PictureSearchType'] = request.picture_search_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreatePictureSearchJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['AppInstanceId'] = request.app_instance_id
        query['SearchPicUrl'] = request.search_pic_url
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Threshold'] = request.threshold
        query['BodyThreshold'] = request.body_threshold
        query['PictureSearchType'] = request.picture_search_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreatePictureSearchJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def create_record_plan_with_options(
        self,
        request: linkvisual_20180120_models.CreateRecordPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateRecordPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Name'] = request.name
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def create_time_template_with_options(
        self,
        request: linkvisual_20180120_models.CreateTimeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.CreateTimeTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['AllDay'] = request.all_day
        query['TimeSections'] = request.time_sections
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateTimeTemplate',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Name'] = request.name
        query['AllDay'] = request.all_day
        query['TimeSections'] = request.time_sections
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateTimeTemplate',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def delete_algorithm_with_options(
        self,
        request: linkvisual_20180120_models.DeleteAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteAlgorithmResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AlgorithmId'] = request.algorithm_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAlgorithm',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteAlgorithmResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_algorithm_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteAlgorithmResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AlgorithmId'] = request.algorithm_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAlgorithm',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteAlgorithmResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteEventRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteEventRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteEventRecordPlanDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteEventRecordPlanDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['DeviceGroupId'] = request.device_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFaceDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['DeviceGroupId'] = request.device_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFaceDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFaceUser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFaceUser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFaceUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFaceUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['ControlId'] = request.control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFaceUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['ControlId'] = request.control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFaceUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['UserId'] = request.user_id
        query['FacePicMd5'] = request.face_pic_md_5
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFaceUserPicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['UserId'] = request.user_id
        query['FacePicMd5'] = request.face_pic_md_5
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFaceUserPicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def delete_model_with_options(
        self,
        request: linkvisual_20180120_models.DeleteModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteModelResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ModelId'] = request.model_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteModel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_with_options_async(
        self,
        request: linkvisual_20180120_models.DeleteModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteModelResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ModelId'] = request.model_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteModel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteModelResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteRecordPlanDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteRecordPlanDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def delete_time_template_with_options(
        self,
        request: linkvisual_20180120_models.DeleteTimeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeleteTimeTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteTimeTemplate',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteTimeTemplate',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def deploy_model_batch_with_options(
        self,
        request: linkvisual_20180120_models.DeployModelBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeployModelBatchResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ModelId'] = request.model_id
        query['DeviceList'] = request.device_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeployModelBatch',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeployModelBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_model_batch_with_options_async(
        self,
        request: linkvisual_20180120_models.DeployModelBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.DeployModelBatchResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ModelId'] = request.model_id
        query['DeviceList'] = request.device_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeployModelBatch',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeployModelBatchResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FacePicUrl'] = request.face_pic_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetectUserFaceByUrl',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['FacePicUrl'] = request.face_pic_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetectUserFaceByUrl',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def get_aiaction_with_options(
        self,
        request: linkvisual_20180120_models.GetAIActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetAIActionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ActionId'] = request.action_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAIAction',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetAIActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aiaction_with_options_async(
        self,
        request: linkvisual_20180120_models.GetAIActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetAIActionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ActionId'] = request.action_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAIAction',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetAIActionResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Algo'] = request.algo
        query['AlgoAction'] = request.algo_action
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAIActionConfig',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetAIActionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aiaction_config_with_options_async(
        self,
        request: linkvisual_20180120_models.GetAIActionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetAIActionConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Algo'] = request.algo
        query['AlgoAction'] = request.algo_action
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAIActionConfig',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetAIActionConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAIApp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetAIAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aiapp_with_options_async(
        self,
        request: linkvisual_20180120_models.GetAIAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetAIAppResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAIApp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetAIAppResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAIJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetAIJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aijob_with_options_async(
        self,
        request: linkvisual_20180120_models.GetAIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetAIJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAIJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetAIJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAIPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetAIPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aiplan_with_options_async(
        self,
        request: linkvisual_20180120_models.GetAIPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetAIPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAIPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetAIPlanResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AlgorithmId'] = request.algorithm_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAlgorithmDetailById',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetAlgorithmDetailByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_algorithm_detail_by_id_with_options_async(
        self,
        request: linkvisual_20180120_models.GetAlgorithmDetailByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetAlgorithmDetailByIdResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AlgorithmId'] = request.algorithm_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAlgorithmDetailById',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetAlgorithmDetailByIdResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAlgorithmDetailByName',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetAlgorithmDetailByNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_algorithm_detail_by_name_with_options_async(
        self,
        request: linkvisual_20180120_models.GetAlgorithmDetailByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetAlgorithmDetailByNameResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAlgorithmDetailByName',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetAlgorithmDetailByNameResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDevicePurifyJobByJobId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetDevicePurifyJobByJobIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_purify_job_by_job_id_with_options_async(
        self,
        request: linkvisual_20180120_models.GetDevicePurifyJobByJobIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetDevicePurifyJobByJobIdResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDevicePurifyJobByJobId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetDevicePurifyJobByJobIdResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AlgorithmId'] = request.algorithm_id
        query['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetModelDetail',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetModelDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_detail_with_options_async(
        self,
        request: linkvisual_20180120_models.GetModelDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetModelDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AlgorithmId'] = request.algorithm_id
        query['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetModelDetail',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetModelDetailResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ModelId'] = request.model_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetModelDetailById',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetModelDetailByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_detail_by_id_with_options_async(
        self,
        request: linkvisual_20180120_models.GetModelDetailByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetModelDetailByIdResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ModelId'] = request.model_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetModelDetailById',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetModelDetailByIdResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AlgorithmId'] = request.algorithm_id
        query['Hardware'] = request.hardware
        query['ModelPackageStandard'] = request.model_package_standard
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetModelOssPolicy',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetModelOssPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_oss_policy_with_options_async(
        self,
        request: linkvisual_20180120_models.GetModelOssPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetModelOssPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AlgorithmId'] = request.algorithm_id
        query['Hardware'] = request.hardware
        query['ModelPackageStandard'] = request.model_package_standard
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetModelOssPolicy',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetModelOssPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['VectorIdList'] = request.vector_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetPictureInfoWithVectorIds',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetPictureInfoWithVectorIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_picture_info_with_vector_ids_with_options_async(
        self,
        request: linkvisual_20180120_models.GetPictureInfoWithVectorIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetPictureInfoWithVectorIdsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['VectorIdList'] = request.vector_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetPictureInfoWithVectorIds',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetPictureInfoWithVectorIdsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_picture_search_job_status_with_options(
        self,
        request: linkvisual_20180120_models.GetPictureSearchJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetPictureSearchJobStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppInstanceId'] = request.app_instance_id
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetPictureSearchJobStatus',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['AppInstanceId'] = request.app_instance_id
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetPictureSearchJobStatus',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def get_picture_with_vector_id_with_options(
        self,
        request: linkvisual_20180120_models.GetPictureWithVectorIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetPictureWithVectorIdResponse:
        UtilClient.validate_model(request)
        query = {}
        query['VectorId'] = request.vector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetPictureWithVectorId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetPictureWithVectorIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_picture_with_vector_id_with_options_async(
        self,
        request: linkvisual_20180120_models.GetPictureWithVectorIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.GetPictureWithVectorIdResponse:
        UtilClient.validate_model(request)
        query = {}
        query['VectorId'] = request.vector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetPictureWithVectorId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetPictureWithVectorIdResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['NamePattern'] = request.name_pattern
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAlgorithmsByPage',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.ListAlgorithmsByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_algorithms_by_page_with_options_async(
        self,
        request: linkvisual_20180120_models.ListAlgorithmsByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.ListAlgorithmsByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['NamePattern'] = request.name_pattern
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAlgorithmsByPage',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.ListAlgorithmsByPageResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ModelId'] = request.model_id
        query['DeviceList'] = request.device_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListDeployTaskByModelIdAndDevices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.ListDeployTaskByModelIdAndDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deploy_task_by_model_id_and_devices_with_options_async(
        self,
        request: linkvisual_20180120_models.ListDeployTaskByModelIdAndDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.ListDeployTaskByModelIdAndDevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ModelId'] = request.model_id
        query['DeviceList'] = request.device_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListDeployTaskByModelIdAndDevices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.ListDeployTaskByModelIdAndDevicesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListDeployTaskByPage',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.ListDeployTaskByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deploy_task_by_page_with_options_async(
        self,
        request: linkvisual_20180120_models.ListDeployTaskByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.ListDeployTaskByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListDeployTaskByPage',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.ListDeployTaskByPageResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AlgorithmId'] = request.algorithm_id
        query['SizeType'] = request.size_type
        query['ModelPackageStandard'] = request.model_package_standard
        query['Hardware'] = request.hardware
        query['NamePattern'] = request.name_pattern
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListModelsByPage',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.ListModelsByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_models_by_page_with_options_async(
        self,
        request: linkvisual_20180120_models.ListModelsByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.ListModelsByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AlgorithmId'] = request.algorithm_id
        query['SizeType'] = request.size_type
        query['ModelPackageStandard'] = request.model_package_standard
        query['Hardware'] = request.hardware
        query['NamePattern'] = request.name_pattern
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListModelsByPage',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.ListModelsByPageResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AlgorithmName'] = request.algorithm_name
        query['SizeType'] = request.size_type
        query['ModelPackageStandard'] = request.model_package_standard
        query['Hardware'] = request.hardware
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListModelVersionsByPage',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.ListModelVersionsByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_model_versions_by_page_with_options_async(
        self,
        request: linkvisual_20180120_models.ListModelVersionsByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.ListModelVersionsByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AlgorithmName'] = request.algorithm_name
        query['SizeType'] = request.size_type
        query['ModelPackageStandard'] = request.model_package_standard
        query['Hardware'] = request.hardware
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListModelVersionsByPage',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.ListModelVersionsByPageResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AppInstanceId'] = request.app_instance_id
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        query['SearchPicUrl'] = request.search_pic_url
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Threshold'] = request.threshold
        query['ContainPicUrl'] = request.contain_pic_url
        query['PictureSearchType'] = request.picture_search_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PictureSearchPicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['AppInstanceId'] = request.app_instance_id
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        query['SearchPicUrl'] = request.search_pic_url
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Threshold'] = request.threshold
        query['ContainPicUrl'] = request.contain_pic_url
        query['PictureSearchType'] = request.picture_search_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PictureSearchPicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def query_aiaction_with_options(
        self,
        request: linkvisual_20180120_models.QueryAIActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryAIActionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryAIAction',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryAIActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_aiaction_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryAIActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryAIActionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryAIAction',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryAIActionResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryAIApp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryAIAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_aiapp_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryAIAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryAIAppResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryAIApp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryAIAppResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ActionId'] = request.action_id
        query['IotId'] = request.iot_id
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryAIJobs',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryAIJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_aijobs_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryAIJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryAIJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ActionId'] = request.action_id
        query['IotId'] = request.iot_id
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryAIJobs',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryAIJobsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AppId'] = request.app_id
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryAIPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryAIPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_aiplan_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryAIPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryAIPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryAIPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryAIPlanResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AppTemplateId'] = request.app_template_id
        query['AppVersion'] = request.app_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryAIPlanTemplates',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryAIPlanTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_aiplan_templates_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryAIPlanTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryAIPlanTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppTemplateId'] = request.app_template_id
        query['AppVersion'] = request.app_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryAIPlanTemplates',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryAIPlanTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['IotId'] = request.iot_id
        query['EventType'] = request.event_type
        query['BeginTime'] = request.begin_time
        query['EndTime'] = request.end_time
        query['CurrentPage'] = request.current_page
        query['PageSize'] = request.page_size
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDeviceEvent',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['EventType'] = request.event_type
        query['BeginTime'] = request.begin_time
        query['EndTime'] = request.end_time
        query['CurrentPage'] = request.current_page
        query['PageSize'] = request.page_size
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDeviceEvent',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['EventId'] = request.event_id
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDeviceEventPicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['EventId'] = request.event_id
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDeviceEventPicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['EventId'] = request.event_id
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDeviceEventRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['EventId'] = request.event_id
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDeviceEventRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def query_device_file_vod_with_options(
        self,
        request: linkvisual_20180120_models.QueryDeviceFileVodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDeviceFileVodResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IotId'] = request.iot_id
        query['FileName'] = request.file_name
        query['ShouldEncrypt'] = request.should_encrypt
        query['EncryptType'] = request.encrypt_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDeviceFileVod',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDeviceFileVodResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_file_vod_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryDeviceFileVodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDeviceFileVodResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IotId'] = request.iot_id
        query['FileName'] = request.file_name
        query['ShouldEncrypt'] = request.should_encrypt
        query['EncryptType'] = request.encrypt_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDeviceFileVod',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDeviceFileVodResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['IotId'] = request.iot_id
        query['CaptureId'] = request.capture_id
        query['PictureType'] = request.picture_type
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDevicePictureFile',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['CaptureId'] = request.capture_id
        query['PictureType'] = request.picture_type
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDevicePictureFile',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDevicePictureLifeCycle',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDevicePictureLifeCycle',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def query_device_purify_jobs_with_options(
        self,
        request: linkvisual_20180120_models.QueryDevicePurifyJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDevicePurifyJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IotId'] = request.iot_id
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDevicePurifyJobs',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDevicePurifyJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_purify_jobs_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryDevicePurifyJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDevicePurifyJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IotId'] = request.iot_id
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDevicePurifyJobs',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDevicePurifyJobsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDevicePurifyPlanByPlanId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDevicePurifyPlanByPlanIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_purify_plan_by_plan_id_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryDevicePurifyPlanByPlanIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDevicePurifyPlanByPlanIdResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDevicePurifyPlanByPlanId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDevicePurifyPlanByPlanIdResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['IotId'] = request.iot_id
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDevicePurifyPlans',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDevicePurifyPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_device_purify_plans_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryDevicePurifyPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryDevicePurifyPlansResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IotId'] = request.iot_id
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDevicePurifyPlans',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDevicePurifyPlansResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['DeviceList'] = request.device_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDeviceRecordLifeCycle',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DeviceList'] = request.device_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDeviceRecordLifeCycle',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['FileName'] = request.file_name
        query['Scheme'] = request.scheme
        query['SeekTime'] = request.seek_time
        query['IotInstanceId'] = request.iot_instance_id
        query['IotId'] = request.iot_id
        query['PlayUnLimited'] = request.play_un_limited
        query['EncryptType'] = request.encrypt_type
        query['ShouldEncrypt'] = request.should_encrypt
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDeviceVodUrl',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['FileName'] = request.file_name
        query['Scheme'] = request.scheme
        query['SeekTime'] = request.seek_time
        query['IotInstanceId'] = request.iot_instance_id
        query['IotId'] = request.iot_id
        query['PlayUnLimited'] = request.play_un_limited
        query['EncryptType'] = request.encrypt_type
        query['ShouldEncrypt'] = request.should_encrypt
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDeviceVodUrl',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['EndTime'] = request.end_time
        query['Scheme'] = request.scheme
        query['SeekTime'] = request.seek_time
        query['IotInstanceId'] = request.iot_instance_id
        query['BeginTime'] = request.begin_time
        query['IotId'] = request.iot_id
        query['PlayUnLimited'] = request.play_un_limited
        query['EncryptType'] = request.encrypt_type
        query['ShouldEncrypt'] = request.should_encrypt
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDeviceVodUrlByTime',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['EndTime'] = request.end_time
        query['Scheme'] = request.scheme
        query['SeekTime'] = request.seek_time
        query['IotInstanceId'] = request.iot_instance_id
        query['BeginTime'] = request.begin_time
        query['IotId'] = request.iot_id
        query['PlayUnLimited'] = request.play_un_limited
        query['EncryptType'] = request.encrypt_type
        query['ShouldEncrypt'] = request.should_encrypt
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryDeviceVodUrlByTime',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryEventRecordPlanDetail',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryEventRecordPlanDetail',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryEventRecordPlanDeviceByDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryEventRecordPlanDeviceByDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['PlanId'] = request.plan_id
        query['CurrentPage'] = request.current_page
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryEventRecordPlanDeviceByPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['PlanId'] = request.plan_id
        query['CurrentPage'] = request.current_page
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryEventRecordPlanDeviceByPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['CurrentPage'] = request.current_page
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryEventRecordPlans',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['CurrentPage'] = request.current_page
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryEventRecordPlans',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['IotInstanceId'] = request.iot_instance_id
        query['PageSize'] = request.page_size
        query['PageNo'] = request.page_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFaceAllDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['IotInstanceId'] = request.iot_instance_id
        query['PageSize'] = request.page_size
        query['PageNo'] = request.page_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFaceAllDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['PageSize'] = request.page_size
        query['PageNo'] = request.page_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFaceAllUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['PageSize'] = request.page_size
        query['PageNo'] = request.page_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFaceAllUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['PageSize'] = request.page_size
        query['PageNo'] = request.page_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFaceAllUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['PageSize'] = request.page_size
        query['PageNo'] = request.page_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFaceAllUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['UserGroupId'] = request.user_group_id
        query['PageSize'] = request.page_size
        query['PageNo'] = request.page_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFaceAllUserIdsByGroupId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['UserGroupId'] = request.user_group_id
        query['PageSize'] = request.page_size
        query['PageNo'] = request.page_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFaceAllUserIdsByGroupId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFaceCustomUserIdByUserId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFaceCustomUserIdByUserId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['IotInstanceId'] = request.iot_instance_id
        query['ProductKey'] = request.product_key
        query['DeviceName'] = request.device_name
        query['PageSize'] = request.page_size
        query['PageNo'] = request.page_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFaceDeviceGroupsByDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['IotInstanceId'] = request.iot_instance_id
        query['ProductKey'] = request.product_key
        query['DeviceName'] = request.device_name
        query['PageSize'] = request.page_size
        query['PageNo'] = request.page_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFaceDeviceGroupsByDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFaceUser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFaceUser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def query_face_user_group_with_options(
        self,
        request: linkvisual_20180120_models.QueryFaceUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryFaceUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IsolationId'] = request.isolation_id
        query['UserId'] = request.user_id
        query['PageSize'] = request.page_size
        query['PageNo'] = request.page_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFaceUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['UserId'] = request.user_id
        query['PageSize'] = request.page_size
        query['PageNo'] = request.page_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFaceUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['ControlId'] = request.control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFaceUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['ControlId'] = request.control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFaceUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['CustomUserId'] = request.custom_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFaceUserIdByCustomUserId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['CustomUserId'] = request.custom_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFaceUserIdByCustomUserId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def query_iot_ids_by_aiplan_with_options(
        self,
        request: linkvisual_20180120_models.QueryIotIdsByAIPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryIotIdsByAIPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PlanId'] = request.plan_id
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryIotIdsByAIPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryIotIdsByAIPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_iot_ids_by_aiplan_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryIotIdsByAIPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryIotIdsByAIPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PlanId'] = request.plan_id
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryIotIdsByAIPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryIotIdsByAIPlanResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Scheme'] = request.scheme
        query['IotInstanceId'] = request.iot_instance_id
        query['StreamType'] = request.stream_type
        query['CacheDuration'] = request.cache_duration
        query['IotId'] = request.iot_id
        query['ShouldEncrypt'] = request.should_encrypt
        query['PlayUnLimited'] = request.play_un_limited
        query['EncryptType'] = request.encrypt_type
        query['ForceIFrame'] = request.force_iframe
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryLiveStreaming',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Scheme'] = request.scheme
        query['IotInstanceId'] = request.iot_instance_id
        query['StreamType'] = request.stream_type
        query['CacheDuration'] = request.cache_duration
        query['IotId'] = request.iot_id
        query['ShouldEncrypt'] = request.should_encrypt
        query['PlayUnLimited'] = request.play_un_limited
        query['EncryptType'] = request.encrypt_type
        query['ForceIFrame'] = request.force_iframe
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryLiveStreaming',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def query_month_record_with_options(
        self,
        request: linkvisual_20180120_models.QueryMonthRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryMonthRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IotId'] = request.iot_id
        query['Month'] = request.month
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMonthRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['Month'] = request.month
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMonthRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['BeginTime'] = request.begin_time
        query['EndTime'] = request.end_time
        query['CurrentPage'] = request.current_page
        query['PageSize'] = request.page_size
        query['PictureType'] = request.picture_type
        query['PictureSource'] = request.picture_source
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryPictureFiles',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['BeginTime'] = request.begin_time
        query['EndTime'] = request.end_time
        query['CurrentPage'] = request.current_page
        query['PageSize'] = request.page_size
        query['PictureType'] = request.picture_type
        query['PictureSource'] = request.picture_source
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryPictureFiles',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['AppInstanceId'] = request.app_instance_id
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryPictureSearchAiboxes',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['AppInstanceId'] = request.app_instance_id
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryPictureSearchAiboxes',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def query_picture_search_app_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryPictureSearchAppResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryPictureSearchApp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryPictureSearchAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_picture_search_app_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryPictureSearchAppResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryPictureSearchApp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryPictureSearchAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_picture_search_app(self) -> linkvisual_20180120_models.QueryPictureSearchAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_picture_search_app_with_options(runtime)

    async def query_picture_search_app_async(self) -> linkvisual_20180120_models.QueryPictureSearchAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_picture_search_app_with_options_async(runtime)

    def query_picture_search_apps_with_options(
        self,
        request: linkvisual_20180120_models.QueryPictureSearchAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryPictureSearchAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryPictureSearchApps',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryPictureSearchApps',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['AppInstanceId'] = request.app_instance_id
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryPictureSearchDevices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['AppInstanceId'] = request.app_instance_id
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryPictureSearchDevices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['AppInstanceId'] = request.app_instance_id
        query['JobStatus'] = request.job_status
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryPictureSearchJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['AppInstanceId'] = request.app_instance_id
        query['JobStatus'] = request.job_status
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryPictureSearchJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['AppInstanceId'] = request.app_instance_id
        query['JobId'] = request.job_id
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryPictureSearchJobResult',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['AppInstanceId'] = request.app_instance_id
        query['JobId'] = request.job_id
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryPictureSearchJobResult',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['StreamType'] = request.stream_type
        query['BeginTime'] = request.begin_time
        query['EndTime'] = request.end_time
        query['RecordType'] = request.record_type
        query['CurrentPage'] = request.current_page
        query['PageSize'] = request.page_size
        query['NeedSnapshot'] = request.need_snapshot
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['StreamType'] = request.stream_type
        query['BeginTime'] = request.begin_time
        query['EndTime'] = request.end_time
        query['RecordType'] = request.record_type
        query['CurrentPage'] = request.current_page
        query['PageSize'] = request.page_size
        query['NeedSnapshot'] = request.need_snapshot
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['RecordId'] = request.record_id
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRecordByRecordId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['RecordId'] = request.record_id
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRecordByRecordId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def query_record_plan_detail_with_options(
        self,
        request: linkvisual_20180120_models.QueryRecordPlanDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryRecordPlanDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRecordPlanDetail',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRecordPlanDetail',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRecordPlanDeviceByDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRecordPlanDeviceByDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['PlanId'] = request.plan_id
        query['CurrentPage'] = request.current_page
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRecordPlanDeviceByPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['PlanId'] = request.plan_id
        query['CurrentPage'] = request.current_page
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRecordPlanDeviceByPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['CurrentPage'] = request.current_page
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRecordPlans',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['CurrentPage'] = request.current_page
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRecordPlans',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['FileName'] = request.file_name
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRecordUrl',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['FileName'] = request.file_name
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryRecordUrl',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def query_standard_aiapp_templates_with_options(
        self,
        request: linkvisual_20180120_models.QueryStandardAIAppTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryStandardAIAppTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryStandardAIAppTemplates',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryStandardAIAppTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_standard_aiapp_templates_with_options_async(
        self,
        request: linkvisual_20180120_models.QueryStandardAIAppTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryStandardAIAppTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryStandardAIAppTemplates',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryStandardAIAppTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryTimeTemplate',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['PageSize'] = request.page_size
        query['CurrentPage'] = request.current_page
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryTimeTemplate',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryTimeTemplateDetail',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryTimeTemplateDetail',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def query_voice_intercom_with_options(
        self,
        request: linkvisual_20180120_models.QueryVoiceIntercomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.QueryVoiceIntercomResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IotId'] = request.iot_id
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryVoiceIntercom',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryVoiceIntercom',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def remove_aiapp_with_options(
        self,
        request: linkvisual_20180120_models.RemoveAIAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.RemoveAIAppResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveAIApp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.RemoveAIAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_aiapp_with_options_async(
        self,
        request: linkvisual_20180120_models.RemoveAIAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.RemoveAIAppResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveAIApp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.RemoveAIAppResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveAIPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.RemoveAIPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_aiplan_with_options_async(
        self,
        request: linkvisual_20180120_models.RemoveAIPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.RemoveAIPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveAIPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.RemoveAIPlanResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveDevicePurifyPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.RemoveDevicePurifyPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_device_purify_plan_with_options_async(
        self,
        request: linkvisual_20180120_models.RemoveDevicePurifyPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.RemoveDevicePurifyPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveDevicePurifyPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.RemoveDevicePurifyPlanResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['IsolationId'] = request.isolation_id
        query['IotInstanceId'] = request.iot_instance_id
        query['ProductKey'] = request.product_key
        query['DeviceName'] = request.device_name
        query['DeviceGroupId'] = request.device_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveFaceDeviceFromDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['IotInstanceId'] = request.iot_instance_id
        query['ProductKey'] = request.product_key
        query['DeviceName'] = request.device_name
        query['DeviceGroupId'] = request.device_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveFaceDeviceFromDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['UserId'] = request.user_id
        query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveFaceUserFromUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['UserId'] = request.user_id
        query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveFaceUserFromUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['Day'] = request.day
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDevicePictureLifeCycle',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['Day'] = request.day
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDevicePictureLifeCycle',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['Day'] = request.day
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDeviceRecordLifeCycle',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['Day'] = request.day
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDeviceRecordLifeCycle',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['StreamType'] = request.stream_type
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopLiveStreaming',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['StreamType'] = request.stream_type
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopLiveStreaming',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopTriggeredRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopTriggeredRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def trigger_capture_picture_with_options(
        self,
        request: linkvisual_20180120_models.TriggerCapturePictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.TriggerCapturePictureResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IotId'] = request.iot_id
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TriggerCapturePicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TriggerCapturePicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['StreamType'] = request.stream_type
        query['PreRecordDuration'] = request.pre_record_duration
        query['RecordDuration'] = request.record_duration
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TriggerRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IotId'] = request.iot_id
        query['StreamType'] = request.stream_type
        query['PreRecordDuration'] = request.pre_record_duration
        query['RecordDuration'] = request.record_duration
        query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TriggerRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def unbind_aiplan_with_devices_with_options(
        self,
        request: linkvisual_20180120_models.UnbindAIPlanWithDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UnbindAIPlanWithDevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PlanId'] = request.plan_id
        query['IotIdList'] = request.iot_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnbindAIPlanWithDevices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UnbindAIPlanWithDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_aiplan_with_devices_with_options_async(
        self,
        request: linkvisual_20180120_models.UnbindAIPlanWithDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UnbindAIPlanWithDevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PlanId'] = request.plan_id
        query['IotIdList'] = request.iot_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnbindAIPlanWithDevices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UnbindAIPlanWithDevicesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AppInstanceId'] = request.app_instance_id
        query['IotInstanceId'] = request.iot_instance_id
        query['DeviceIotIds'] = request.device_iot_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnbindPictureSearchAppWithDevices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['AppInstanceId'] = request.app_instance_id
        query['IotInstanceId'] = request.iot_instance_id
        query['DeviceIotIds'] = request.device_iot_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnbindPictureSearchAppWithDevices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def update_aiapp_with_options(
        self,
        request: linkvisual_20180120_models.UpdateAIAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateAIAppResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['Level'] = request.level
        query['Name'] = request.name
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAIApp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateAIAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_aiapp_with_options_async(
        self,
        request: linkvisual_20180120_models.UpdateAIAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateAIAppResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['Level'] = request.level
        query['Name'] = request.name
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAIApp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateAIAppResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PlanId'] = request.plan_id
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAIPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateAIPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_aiplan_with_options_async(
        self,
        request: linkvisual_20180120_models.UpdateAIPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateAIPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PlanId'] = request.plan_id
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAIPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateAIPlanResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PlanId'] = request.plan_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDevicePurifyPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateDevicePurifyPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_device_purify_plan_with_options_async(
        self,
        request: linkvisual_20180120_models.UpdateDevicePurifyPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateDevicePurifyPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PlanId'] = request.plan_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDevicePurifyPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateDevicePurifyPlanResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PlanId'] = request.plan_id
        query['Name'] = request.name
        query['EventTypes'] = request.event_types
        query['PreRecordDuration'] = request.pre_record_duration
        query['RecordDuration'] = request.record_duration
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateEventRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['PlanId'] = request.plan_id
        query['Name'] = request.name
        query['EventTypes'] = request.event_types
        query['PreRecordDuration'] = request.pre_record_duration
        query['RecordDuration'] = request.record_duration
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateEventRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['UserId'] = request.user_id
        query['Name'] = request.name
        query['Params'] = request.params
        query['FacePicUrl'] = request.face_pic_url
        query['CustomUserId'] = request.custom_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateFaceUser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['UserId'] = request.user_id
        query['Name'] = request.name
        query['Params'] = request.params
        query['FacePicUrl'] = request.face_pic_url
        query['CustomUserId'] = request.custom_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateFaceUser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['ControlId'] = request.control_id
        query['Relation'] = request.relation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateFaceUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['IsolationId'] = request.isolation_id
        query['ControlId'] = request.control_id
        query['Relation'] = request.relation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateFaceUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def update_model_with_options(
        self,
        request: linkvisual_20180120_models.UpdateModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateModelResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ModelId'] = request.model_id
        query['Name'] = request.name
        query['Hardware'] = request.hardware
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateModel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_model_with_options_async(
        self,
        request: linkvisual_20180120_models.UpdateModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateModelResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ModelId'] = request.model_id
        query['Name'] = request.name
        query['Hardware'] = request.hardware
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateModel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateModelResponse(),
            await self.call_api_async(params, req, runtime)
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

    def update_picture_search_app_with_options(
        self,
        request: linkvisual_20180120_models.UpdatePictureSearchAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdatePictureSearchAppResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppInstanceId'] = request.app_instance_id
        query['Name'] = request.name
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdatePictureSearchApp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['AppInstanceId'] = request.app_instance_id
        query['Name'] = request.name
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdatePictureSearchApp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['PlanId'] = request.plan_id
        query['Name'] = request.name
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['PlanId'] = request.plan_id
        query['Name'] = request.name
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def update_time_template_with_options(
        self,
        request: linkvisual_20180120_models.UpdateTimeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkvisual_20180120_models.UpdateTimeTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['TemplateId'] = request.template_id
        query['Name'] = request.name
        query['AllDay'] = request.all_day
        query['TimeSections'] = request.time_sections
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateTimeTemplate',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['TemplateId'] = request.template_id
        query['Name'] = request.name
        query['AllDay'] = request.all_day
        query['TimeSections'] = request.time_sections
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateTimeTemplate',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
