# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_linkface20180720 import models as link_face_20180720_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('linkface', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_group_with_options(
        self,
        request: link_face_20180720_models.CreateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.CreateGroupResponse:
        """
        @summary 创建组
        
        @param request: CreateGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.CreateGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.CreateGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def create_group_with_options_async(
        self,
        request: link_face_20180720_models.CreateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.CreateGroupResponse:
        """
        @summary 创建组
        
        @param request: CreateGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.CreateGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.CreateGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_group(
        self,
        request: link_face_20180720_models.CreateGroupRequest,
    ) -> link_face_20180720_models.CreateGroupResponse:
        """
        @summary 创建组
        
        @param request: CreateGroupRequest
        @return: CreateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_group_with_options(request, runtime)

    async def create_group_async(
        self,
        request: link_face_20180720_models.CreateGroupRequest,
    ) -> link_face_20180720_models.CreateGroupResponse:
        """
        @summary 创建组
        
        @param request: CreateGroupRequest
        @return: CreateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_group_with_options_async(request, runtime)

    def delete_device_all_group_with_options(
        self,
        request: link_face_20180720_models.DeleteDeviceAllGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.DeleteDeviceAllGroupResponse:
        """
        @summary 删除设备所在的所有分组
        
        @param request: DeleteDeviceAllGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDeviceAllGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            body['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.product_key):
            body['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDeviceAllGroup',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.DeleteDeviceAllGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.DeleteDeviceAllGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_device_all_group_with_options_async(
        self,
        request: link_face_20180720_models.DeleteDeviceAllGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.DeleteDeviceAllGroupResponse:
        """
        @summary 删除设备所在的所有分组
        
        @param request: DeleteDeviceAllGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDeviceAllGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            body['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.product_key):
            body['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDeviceAllGroup',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.DeleteDeviceAllGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.DeleteDeviceAllGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_device_all_group(
        self,
        request: link_face_20180720_models.DeleteDeviceAllGroupRequest,
    ) -> link_face_20180720_models.DeleteDeviceAllGroupResponse:
        """
        @summary 删除设备所在的所有分组
        
        @param request: DeleteDeviceAllGroupRequest
        @return: DeleteDeviceAllGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_device_all_group_with_options(request, runtime)

    async def delete_device_all_group_async(
        self,
        request: link_face_20180720_models.DeleteDeviceAllGroupRequest,
    ) -> link_face_20180720_models.DeleteDeviceAllGroupResponse:
        """
        @summary 删除设备所在的所有分组
        
        @param request: DeleteDeviceAllGroupRequest
        @return: DeleteDeviceAllGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_all_group_with_options_async(request, runtime)

    def delete_device_group_with_options(
        self,
        request: link_face_20180720_models.DeleteDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.DeleteDeviceGroupResponse:
        """
        @summary 设备设备组
        
        @param request: DeleteDeviceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDeviceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.iot_id):
            body['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.product_key):
            body['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDeviceGroup',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.DeleteDeviceGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.DeleteDeviceGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_device_group_with_options_async(
        self,
        request: link_face_20180720_models.DeleteDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.DeleteDeviceGroupResponse:
        """
        @summary 设备设备组
        
        @param request: DeleteDeviceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDeviceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.iot_id):
            body['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.product_key):
            body['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDeviceGroup',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.DeleteDeviceGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.DeleteDeviceGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_device_group(
        self,
        request: link_face_20180720_models.DeleteDeviceGroupRequest,
    ) -> link_face_20180720_models.DeleteDeviceGroupResponse:
        """
        @summary 设备设备组
        
        @param request: DeleteDeviceGroupRequest
        @return: DeleteDeviceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_device_group_with_options(request, runtime)

    async def delete_device_group_async(
        self,
        request: link_face_20180720_models.DeleteDeviceGroupRequest,
    ) -> link_face_20180720_models.DeleteDeviceGroupResponse:
        """
        @summary 设备设备组
        
        @param request: DeleteDeviceGroupRequest
        @return: DeleteDeviceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_group_with_options_async(request, runtime)

    def delete_face_with_options(
        self,
        request: link_face_20180720_models.DeleteFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.DeleteFaceResponse:
        """
        @summary 删除人脸
        
        @param request: DeleteFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFace',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.DeleteFaceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.DeleteFaceResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_face_with_options_async(
        self,
        request: link_face_20180720_models.DeleteFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.DeleteFaceResponse:
        """
        @summary 删除人脸
        
        @param request: DeleteFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFace',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.DeleteFaceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.DeleteFaceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_face(
        self,
        request: link_face_20180720_models.DeleteFaceRequest,
    ) -> link_face_20180720_models.DeleteFaceResponse:
        """
        @summary 删除人脸
        
        @param request: DeleteFaceRequest
        @return: DeleteFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_face_with_options(request, runtime)

    async def delete_face_async(
        self,
        request: link_face_20180720_models.DeleteFaceRequest,
    ) -> link_face_20180720_models.DeleteFaceResponse:
        """
        @summary 删除人脸
        
        @param request: DeleteFaceRequest
        @return: DeleteFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_with_options_async(request, runtime)

    def delete_group_with_options(
        self,
        request: link_face_20180720_models.DeleteGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.DeleteGroupResponse:
        """
        @summary 删除组
        
        @param request: DeleteGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.DeleteGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.DeleteGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_group_with_options_async(
        self,
        request: link_face_20180720_models.DeleteGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.DeleteGroupResponse:
        """
        @summary 删除组
        
        @param request: DeleteGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.DeleteGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.DeleteGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_group(
        self,
        request: link_face_20180720_models.DeleteGroupRequest,
    ) -> link_face_20180720_models.DeleteGroupResponse:
        """
        @summary 删除组
        
        @param request: DeleteGroupRequest
        @return: DeleteGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_group_with_options(request, runtime)

    async def delete_group_async(
        self,
        request: link_face_20180720_models.DeleteGroupRequest,
    ) -> link_face_20180720_models.DeleteGroupResponse:
        """
        @summary 删除组
        
        @param request: DeleteGroupRequest
        @return: DeleteGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_group_with_options_async(request, runtime)

    def link_face_with_options(
        self,
        request: link_face_20180720_models.LinkFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.LinkFaceResponse:
        """
        @summary 关联人脸
        
        @param request: LinkFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LinkFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LinkFace',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.LinkFaceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.LinkFaceResponse(),
                self.execute(params, req, runtime)
            )

    async def link_face_with_options_async(
        self,
        request: link_face_20180720_models.LinkFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.LinkFaceResponse:
        """
        @summary 关联人脸
        
        @param request: LinkFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LinkFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LinkFace',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.LinkFaceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.LinkFaceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def link_face(
        self,
        request: link_face_20180720_models.LinkFaceRequest,
    ) -> link_face_20180720_models.LinkFaceResponse:
        """
        @summary 关联人脸
        
        @param request: LinkFaceRequest
        @return: LinkFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.link_face_with_options(request, runtime)

    async def link_face_async(
        self,
        request: link_face_20180720_models.LinkFaceRequest,
    ) -> link_face_20180720_models.LinkFaceResponse:
        """
        @summary 关联人脸
        
        @param request: LinkFaceRequest
        @return: LinkFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.link_face_with_options_async(request, runtime)

    def query_add_user_info_with_options(
        self,
        request: link_face_20180720_models.QueryAddUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.QueryAddUserInfoResponse:
        """
        @summary 查询添加的用户信息
        
        @param request: QueryAddUserInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAddUserInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.iot_id):
            body['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.product_key):
            body['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryAddUserInfo',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.QueryAddUserInfoResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.QueryAddUserInfoResponse(),
                self.execute(params, req, runtime)
            )

    async def query_add_user_info_with_options_async(
        self,
        request: link_face_20180720_models.QueryAddUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.QueryAddUserInfoResponse:
        """
        @summary 查询添加的用户信息
        
        @param request: QueryAddUserInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAddUserInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.iot_id):
            body['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.product_key):
            body['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryAddUserInfo',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.QueryAddUserInfoResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.QueryAddUserInfoResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_add_user_info(
        self,
        request: link_face_20180720_models.QueryAddUserInfoRequest,
    ) -> link_face_20180720_models.QueryAddUserInfoResponse:
        """
        @summary 查询添加的用户信息
        
        @param request: QueryAddUserInfoRequest
        @return: QueryAddUserInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_add_user_info_with_options(request, runtime)

    async def query_add_user_info_async(
        self,
        request: link_face_20180720_models.QueryAddUserInfoRequest,
    ) -> link_face_20180720_models.QueryAddUserInfoResponse:
        """
        @summary 查询添加的用户信息
        
        @param request: QueryAddUserInfoRequest
        @return: QueryAddUserInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_add_user_info_with_options_async(request, runtime)

    def query_all_groups_with_options(
        self,
        request: link_face_20180720_models.QueryAllGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.QueryAllGroupsResponse:
        """
        @summary 查询所有分组
        
        @param request: QueryAllGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAllGroupsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryAllGroups',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.QueryAllGroupsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.QueryAllGroupsResponse(),
                self.execute(params, req, runtime)
            )

    async def query_all_groups_with_options_async(
        self,
        request: link_face_20180720_models.QueryAllGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.QueryAllGroupsResponse:
        """
        @summary 查询所有分组
        
        @param request: QueryAllGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAllGroupsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryAllGroups',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.QueryAllGroupsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.QueryAllGroupsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_all_groups(
        self,
        request: link_face_20180720_models.QueryAllGroupsRequest,
    ) -> link_face_20180720_models.QueryAllGroupsResponse:
        """
        @summary 查询所有分组
        
        @param request: QueryAllGroupsRequest
        @return: QueryAllGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_all_groups_with_options(request, runtime)

    async def query_all_groups_async(
        self,
        request: link_face_20180720_models.QueryAllGroupsRequest,
    ) -> link_face_20180720_models.QueryAllGroupsResponse:
        """
        @summary 查询所有分组
        
        @param request: QueryAllGroupsRequest
        @return: QueryAllGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_all_groups_with_options_async(request, runtime)

    def query_authentication_with_options(
        self,
        request: link_face_20180720_models.QueryAuthenticationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.QueryAuthenticationResponse:
        """
        @summary 查询认证
        
        @param request: QueryAuthenticationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAuthenticationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            body['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.license_type):
            body['LicenseType'] = request.license_type
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            body['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryAuthentication',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.QueryAuthenticationResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.QueryAuthenticationResponse(),
                self.execute(params, req, runtime)
            )

    async def query_authentication_with_options_async(
        self,
        request: link_face_20180720_models.QueryAuthenticationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.QueryAuthenticationResponse:
        """
        @summary 查询认证
        
        @param request: QueryAuthenticationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAuthenticationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            body['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.license_type):
            body['LicenseType'] = request.license_type
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            body['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryAuthentication',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.QueryAuthenticationResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.QueryAuthenticationResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_authentication(
        self,
        request: link_face_20180720_models.QueryAuthenticationRequest,
    ) -> link_face_20180720_models.QueryAuthenticationResponse:
        """
        @summary 查询认证
        
        @param request: QueryAuthenticationRequest
        @return: QueryAuthenticationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_authentication_with_options(request, runtime)

    async def query_authentication_async(
        self,
        request: link_face_20180720_models.QueryAuthenticationRequest,
    ) -> link_face_20180720_models.QueryAuthenticationResponse:
        """
        @summary 查询认证
        
        @param request: QueryAuthenticationRequest
        @return: QueryAuthenticationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_authentication_with_options_async(request, runtime)

    def query_face_with_options(
        self,
        request: link_face_20180720_models.QueryFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.QueryFaceResponse:
        """
        @summary 查询人脸
        
        @param request: QueryFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryFace',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.QueryFaceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.QueryFaceResponse(),
                self.execute(params, req, runtime)
            )

    async def query_face_with_options_async(
        self,
        request: link_face_20180720_models.QueryFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.QueryFaceResponse:
        """
        @summary 查询人脸
        
        @param request: QueryFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryFace',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.QueryFaceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.QueryFaceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_face(
        self,
        request: link_face_20180720_models.QueryFaceRequest,
    ) -> link_face_20180720_models.QueryFaceResponse:
        """
        @summary 查询人脸
        
        @param request: QueryFaceRequest
        @return: QueryFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_face_with_options(request, runtime)

    async def query_face_async(
        self,
        request: link_face_20180720_models.QueryFaceRequest,
    ) -> link_face_20180720_models.QueryFaceResponse:
        """
        @summary 查询人脸
        
        @param request: QueryFaceRequest
        @return: QueryFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_face_with_options_async(request, runtime)

    def query_group_users_with_options(
        self,
        request: link_face_20180720_models.QueryGroupUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.QueryGroupUsersResponse:
        """
        @summary 查询分组内用户
        
        @param request: QueryGroupUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryGroupUsersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryGroupUsers',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.QueryGroupUsersResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.QueryGroupUsersResponse(),
                self.execute(params, req, runtime)
            )

    async def query_group_users_with_options_async(
        self,
        request: link_face_20180720_models.QueryGroupUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.QueryGroupUsersResponse:
        """
        @summary 查询分组内用户
        
        @param request: QueryGroupUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryGroupUsersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryGroupUsers',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.QueryGroupUsersResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.QueryGroupUsersResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_group_users(
        self,
        request: link_face_20180720_models.QueryGroupUsersRequest,
    ) -> link_face_20180720_models.QueryGroupUsersResponse:
        """
        @summary 查询分组内用户
        
        @param request: QueryGroupUsersRequest
        @return: QueryGroupUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_group_users_with_options(request, runtime)

    async def query_group_users_async(
        self,
        request: link_face_20180720_models.QueryGroupUsersRequest,
    ) -> link_face_20180720_models.QueryGroupUsersResponse:
        """
        @summary 查询分组内用户
        
        @param request: QueryGroupUsersRequest
        @return: QueryGroupUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_group_users_with_options_async(request, runtime)

    def query_licenses_with_options(
        self,
        request: link_face_20180720_models.QueryLicensesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.QueryLicensesResponse:
        """
        @summary 查询授权
        
        @param request: QueryLicensesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryLicensesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.license_type):
            body['LicenseType'] = request.license_type
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryLicenses',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.QueryLicensesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.QueryLicensesResponse(),
                self.execute(params, req, runtime)
            )

    async def query_licenses_with_options_async(
        self,
        request: link_face_20180720_models.QueryLicensesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.QueryLicensesResponse:
        """
        @summary 查询授权
        
        @param request: QueryLicensesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryLicensesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.license_type):
            body['LicenseType'] = request.license_type
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryLicenses',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.QueryLicensesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.QueryLicensesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_licenses(
        self,
        request: link_face_20180720_models.QueryLicensesRequest,
    ) -> link_face_20180720_models.QueryLicensesResponse:
        """
        @summary 查询授权
        
        @param request: QueryLicensesRequest
        @return: QueryLicensesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_licenses_with_options(request, runtime)

    async def query_licenses_async(
        self,
        request: link_face_20180720_models.QueryLicensesRequest,
    ) -> link_face_20180720_models.QueryLicensesResponse:
        """
        @summary 查询授权
        
        @param request: QueryLicensesRequest
        @return: QueryLicensesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_licenses_with_options_async(request, runtime)

    def query_sync_pic_schedule_with_options(
        self,
        request: link_face_20180720_models.QuerySyncPicScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.QuerySyncPicScheduleResponse:
        """
        @summary 查询同步图片计划
        
        @param request: QuerySyncPicScheduleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySyncPicScheduleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.iot_id):
            body['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.product_key):
            body['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySyncPicSchedule',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.QuerySyncPicScheduleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.QuerySyncPicScheduleResponse(),
                self.execute(params, req, runtime)
            )

    async def query_sync_pic_schedule_with_options_async(
        self,
        request: link_face_20180720_models.QuerySyncPicScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.QuerySyncPicScheduleResponse:
        """
        @summary 查询同步图片计划
        
        @param request: QuerySyncPicScheduleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySyncPicScheduleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.iot_id):
            body['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.product_key):
            body['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySyncPicSchedule',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.QuerySyncPicScheduleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.QuerySyncPicScheduleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_sync_pic_schedule(
        self,
        request: link_face_20180720_models.QuerySyncPicScheduleRequest,
    ) -> link_face_20180720_models.QuerySyncPicScheduleResponse:
        """
        @summary 查询同步图片计划
        
        @param request: QuerySyncPicScheduleRequest
        @return: QuerySyncPicScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sync_pic_schedule_with_options(request, runtime)

    async def query_sync_pic_schedule_async(
        self,
        request: link_face_20180720_models.QuerySyncPicScheduleRequest,
    ) -> link_face_20180720_models.QuerySyncPicScheduleResponse:
        """
        @summary 查询同步图片计划
        
        @param request: QuerySyncPicScheduleRequest
        @return: QuerySyncPicScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sync_pic_schedule_with_options_async(request, runtime)

    def register_face_with_options(
        self,
        request: link_face_20180720_models.RegisterFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.RegisterFaceResponse:
        """
        @summary 注册人脸
        
        @param request: RegisterFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.image):
            body['Image'] = request.image
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_info):
            body['UserInfo'] = request.user_info
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegisterFace',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.RegisterFaceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.RegisterFaceResponse(),
                self.execute(params, req, runtime)
            )

    async def register_face_with_options_async(
        self,
        request: link_face_20180720_models.RegisterFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.RegisterFaceResponse:
        """
        @summary 注册人脸
        
        @param request: RegisterFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.image):
            body['Image'] = request.image
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_info):
            body['UserInfo'] = request.user_info
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegisterFace',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.RegisterFaceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.RegisterFaceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def register_face(
        self,
        request: link_face_20180720_models.RegisterFaceRequest,
    ) -> link_face_20180720_models.RegisterFaceResponse:
        """
        @summary 注册人脸
        
        @param request: RegisterFaceRequest
        @return: RegisterFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.register_face_with_options(request, runtime)

    async def register_face_async(
        self,
        request: link_face_20180720_models.RegisterFaceRequest,
    ) -> link_face_20180720_models.RegisterFaceResponse:
        """
        @summary 注册人脸
        
        @param request: RegisterFaceRequest
        @return: RegisterFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.register_face_with_options_async(request, runtime)

    def search_face_with_options(
        self,
        request: link_face_20180720_models.SearchFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.SearchFaceResponse:
        """
        @summary 搜索人脸
        
        @param request: SearchFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.image):
            body['Image'] = request.image
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchFace',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.SearchFaceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.SearchFaceResponse(),
                self.execute(params, req, runtime)
            )

    async def search_face_with_options_async(
        self,
        request: link_face_20180720_models.SearchFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.SearchFaceResponse:
        """
        @summary 搜索人脸
        
        @param request: SearchFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.image):
            body['Image'] = request.image
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchFace',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.SearchFaceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.SearchFaceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def search_face(
        self,
        request: link_face_20180720_models.SearchFaceRequest,
    ) -> link_face_20180720_models.SearchFaceResponse:
        """
        @summary 搜索人脸
        
        @param request: SearchFaceRequest
        @return: SearchFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_face_with_options(request, runtime)

    async def search_face_async(
        self,
        request: link_face_20180720_models.SearchFaceRequest,
    ) -> link_face_20180720_models.SearchFaceResponse:
        """
        @summary 搜索人脸
        
        @param request: SearchFaceRequest
        @return: SearchFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_face_with_options_async(request, runtime)

    def sync_face_pictures_with_options(
        self,
        request: link_face_20180720_models.SyncFacePicturesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.SyncFacePicturesResponse:
        """
        @summary 同步人脸
        
        @param request: SyncFacePicturesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncFacePicturesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.iot_id):
            body['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.product_key):
            body['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncFacePictures',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.SyncFacePicturesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.SyncFacePicturesResponse(),
                self.execute(params, req, runtime)
            )

    async def sync_face_pictures_with_options_async(
        self,
        request: link_face_20180720_models.SyncFacePicturesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.SyncFacePicturesResponse:
        """
        @summary 同步人脸
        
        @param request: SyncFacePicturesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncFacePicturesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.iot_id):
            body['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.product_key):
            body['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncFacePictures',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.SyncFacePicturesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.SyncFacePicturesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def sync_face_pictures(
        self,
        request: link_face_20180720_models.SyncFacePicturesRequest,
    ) -> link_face_20180720_models.SyncFacePicturesResponse:
        """
        @summary 同步人脸
        
        @param request: SyncFacePicturesRequest
        @return: SyncFacePicturesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.sync_face_pictures_with_options(request, runtime)

    async def sync_face_pictures_async(
        self,
        request: link_face_20180720_models.SyncFacePicturesRequest,
    ) -> link_face_20180720_models.SyncFacePicturesResponse:
        """
        @summary 同步人脸
        
        @param request: SyncFacePicturesRequest
        @return: SyncFacePicturesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.sync_face_pictures_with_options_async(request, runtime)

    def unlink_face_with_options(
        self,
        request: link_face_20180720_models.UnlinkFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.UnlinkFaceResponse:
        """
        @summary 解绑人脸
        
        @param request: UnlinkFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnlinkFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnlinkFace',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.UnlinkFaceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.UnlinkFaceResponse(),
                self.execute(params, req, runtime)
            )

    async def unlink_face_with_options_async(
        self,
        request: link_face_20180720_models.UnlinkFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.UnlinkFaceResponse:
        """
        @summary 解绑人脸
        
        @param request: UnlinkFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnlinkFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnlinkFace',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.UnlinkFaceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.UnlinkFaceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def unlink_face(
        self,
        request: link_face_20180720_models.UnlinkFaceRequest,
    ) -> link_face_20180720_models.UnlinkFaceResponse:
        """
        @summary 解绑人脸
        
        @param request: UnlinkFaceRequest
        @return: UnlinkFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unlink_face_with_options(request, runtime)

    async def unlink_face_async(
        self,
        request: link_face_20180720_models.UnlinkFaceRequest,
    ) -> link_face_20180720_models.UnlinkFaceResponse:
        """
        @summary 解绑人脸
        
        @param request: UnlinkFaceRequest
        @return: UnlinkFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unlink_face_with_options_async(request, runtime)

    def update_face_with_options(
        self,
        request: link_face_20180720_models.UpdateFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.UpdateFaceResponse:
        """
        @summary 更新人脸
        
        @param request: UpdateFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image):
            body['Image'] = request.image
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_info):
            body['UserInfo'] = request.user_info
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFace',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.UpdateFaceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.UpdateFaceResponse(),
                self.execute(params, req, runtime)
            )

    async def update_face_with_options_async(
        self,
        request: link_face_20180720_models.UpdateFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> link_face_20180720_models.UpdateFaceResponse:
        """
        @summary 更新人脸
        
        @param request: UpdateFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image):
            body['Image'] = request.image
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_info):
            body['UserInfo'] = request.user_info
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFace',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                link_face_20180720_models.UpdateFaceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                link_face_20180720_models.UpdateFaceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_face(
        self,
        request: link_face_20180720_models.UpdateFaceRequest,
    ) -> link_face_20180720_models.UpdateFaceResponse:
        """
        @summary 更新人脸
        
        @param request: UpdateFaceRequest
        @return: UpdateFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_face_with_options(request, runtime)

    async def update_face_async(
        self,
        request: link_face_20180720_models.UpdateFaceRequest,
    ) -> link_face_20180720_models.UpdateFaceResponse:
        """
        @summary 更新人脸
        
        @param request: UpdateFaceRequest
        @return: UpdateFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_face_with_options_async(request, runtime)
