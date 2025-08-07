# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_notifications20241225 import models as notifications_20241225_models
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
        self._endpoint = self.get_endpoint('notifications', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def del_message_with_options(
        self,
        request: notifications_20241225_models.DelMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> notifications_20241225_models.DelMessageResponse:
        """
        @summary 方法描述：删除消息
        
        @param request: DelMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DelMessageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not UtilClient.is_unset(request.client_source):
            body['ClientSource'] = request.client_source
        if not UtilClient.is_unset(request.cookies):
            body['Cookies'] = request.cookies
        if not UtilClient.is_unset(request.msg_id):
            body['MsgId'] = request.msg_id
        if not UtilClient.is_unset(request.src_url):
            body['SrcUrl'] = request.src_url
        if not UtilClient.is_unset(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not UtilClient.is_unset(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DelMessage',
            version='2024-12-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            notifications_20241225_models.DelMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def del_message_with_options_async(
        self,
        request: notifications_20241225_models.DelMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> notifications_20241225_models.DelMessageResponse:
        """
        @summary 方法描述：删除消息
        
        @param request: DelMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DelMessageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not UtilClient.is_unset(request.client_source):
            body['ClientSource'] = request.client_source
        if not UtilClient.is_unset(request.cookies):
            body['Cookies'] = request.cookies
        if not UtilClient.is_unset(request.msg_id):
            body['MsgId'] = request.msg_id
        if not UtilClient.is_unset(request.src_url):
            body['SrcUrl'] = request.src_url
        if not UtilClient.is_unset(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not UtilClient.is_unset(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DelMessage',
            version='2024-12-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            notifications_20241225_models.DelMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def del_message(
        self,
        request: notifications_20241225_models.DelMessageRequest,
    ) -> notifications_20241225_models.DelMessageResponse:
        """
        @summary 方法描述：删除消息
        
        @param request: DelMessageRequest
        @return: DelMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.del_message_with_options(request, runtime)

    async def del_message_async(
        self,
        request: notifications_20241225_models.DelMessageRequest,
    ) -> notifications_20241225_models.DelMessageResponse:
        """
        @summary 方法描述：删除消息
        
        @param request: DelMessageRequest
        @return: DelMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.del_message_with_options_async(request, runtime)

    def delete_all_message_with_options(
        self,
        request: notifications_20241225_models.DeleteAllMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> notifications_20241225_models.DeleteAllMessageResponse:
        """
        @summary 方法描述：站内信全部删除（逻辑删除）
        
        @param request: DeleteAllMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAllMessageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.client_source):
            body['ClientSource'] = request.client_source
        if not UtilClient.is_unset(request.cookies):
            body['Cookies'] = request.cookies
        if not UtilClient.is_unset(request.src_url):
            body['SrcUrl'] = request.src_url
        if not UtilClient.is_unset(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not UtilClient.is_unset(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAllMessage',
            version='2024-12-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            notifications_20241225_models.DeleteAllMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_all_message_with_options_async(
        self,
        request: notifications_20241225_models.DeleteAllMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> notifications_20241225_models.DeleteAllMessageResponse:
        """
        @summary 方法描述：站内信全部删除（逻辑删除）
        
        @param request: DeleteAllMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAllMessageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.client_source):
            body['ClientSource'] = request.client_source
        if not UtilClient.is_unset(request.cookies):
            body['Cookies'] = request.cookies
        if not UtilClient.is_unset(request.src_url):
            body['SrcUrl'] = request.src_url
        if not UtilClient.is_unset(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not UtilClient.is_unset(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAllMessage',
            version='2024-12-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            notifications_20241225_models.DeleteAllMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_all_message(
        self,
        request: notifications_20241225_models.DeleteAllMessageRequest,
    ) -> notifications_20241225_models.DeleteAllMessageResponse:
        """
        @summary 方法描述：站内信全部删除（逻辑删除）
        
        @param request: DeleteAllMessageRequest
        @return: DeleteAllMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_all_message_with_options(request, runtime)

    async def delete_all_message_async(
        self,
        request: notifications_20241225_models.DeleteAllMessageRequest,
    ) -> notifications_20241225_models.DeleteAllMessageResponse:
        """
        @summary 方法描述：站内信全部删除（逻辑删除）
        
        @param request: DeleteAllMessageRequest
        @return: DeleteAllMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_all_message_with_options_async(request, runtime)

    def read_all_message_with_options(
        self,
        request: notifications_20241225_models.ReadAllMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> notifications_20241225_models.ReadAllMessageResponse:
        """
        @summary 方法描述：分类全部标记为已读，不填则全部标记
        
        @param request: ReadAllMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReadAllMessageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.client_source):
            body['ClientSource'] = request.client_source
        if not UtilClient.is_unset(request.cookies):
            body['Cookies'] = request.cookies
        if not UtilClient.is_unset(request.src_url):
            body['SrcUrl'] = request.src_url
        if not UtilClient.is_unset(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not UtilClient.is_unset(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReadAllMessage',
            version='2024-12-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            notifications_20241225_models.ReadAllMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_all_message_with_options_async(
        self,
        request: notifications_20241225_models.ReadAllMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> notifications_20241225_models.ReadAllMessageResponse:
        """
        @summary 方法描述：分类全部标记为已读，不填则全部标记
        
        @param request: ReadAllMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReadAllMessageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.client_source):
            body['ClientSource'] = request.client_source
        if not UtilClient.is_unset(request.cookies):
            body['Cookies'] = request.cookies
        if not UtilClient.is_unset(request.src_url):
            body['SrcUrl'] = request.src_url
        if not UtilClient.is_unset(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not UtilClient.is_unset(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReadAllMessage',
            version='2024-12-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            notifications_20241225_models.ReadAllMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_all_message(
        self,
        request: notifications_20241225_models.ReadAllMessageRequest,
    ) -> notifications_20241225_models.ReadAllMessageResponse:
        """
        @summary 方法描述：分类全部标记为已读，不填则全部标记
        
        @param request: ReadAllMessageRequest
        @return: ReadAllMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.read_all_message_with_options(request, runtime)

    async def read_all_message_async(
        self,
        request: notifications_20241225_models.ReadAllMessageRequest,
    ) -> notifications_20241225_models.ReadAllMessageResponse:
        """
        @summary 方法描述：分类全部标记为已读，不填则全部标记
        
        @param request: ReadAllMessageRequest
        @return: ReadAllMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.read_all_message_with_options_async(request, runtime)

    def read_class_name_with_options(
        self,
        request: notifications_20241225_models.ReadClassNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> notifications_20241225_models.ReadClassNameResponse:
        """
        @summary 方法描述：获取各分类已读消息数
        
        @param request: ReadClassNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReadClassNameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not UtilClient.is_unset(request.client_source):
            body['ClientSource'] = request.client_source
        if not UtilClient.is_unset(request.cookies):
            body['Cookies'] = request.cookies
        if not UtilClient.is_unset(request.src_url):
            body['SrcUrl'] = request.src_url
        if not UtilClient.is_unset(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not UtilClient.is_unset(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReadClassName',
            version='2024-12-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            notifications_20241225_models.ReadClassNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_class_name_with_options_async(
        self,
        request: notifications_20241225_models.ReadClassNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> notifications_20241225_models.ReadClassNameResponse:
        """
        @summary 方法描述：获取各分类已读消息数
        
        @param request: ReadClassNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReadClassNameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not UtilClient.is_unset(request.client_source):
            body['ClientSource'] = request.client_source
        if not UtilClient.is_unset(request.cookies):
            body['Cookies'] = request.cookies
        if not UtilClient.is_unset(request.src_url):
            body['SrcUrl'] = request.src_url
        if not UtilClient.is_unset(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not UtilClient.is_unset(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReadClassName',
            version='2024-12-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            notifications_20241225_models.ReadClassNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_class_name(
        self,
        request: notifications_20241225_models.ReadClassNameRequest,
    ) -> notifications_20241225_models.ReadClassNameResponse:
        """
        @summary 方法描述：获取各分类已读消息数
        
        @param request: ReadClassNameRequest
        @return: ReadClassNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.read_class_name_with_options(request, runtime)

    async def read_class_name_async(
        self,
        request: notifications_20241225_models.ReadClassNameRequest,
    ) -> notifications_20241225_models.ReadClassNameResponse:
        """
        @summary 方法描述：获取各分类已读消息数
        
        @param request: ReadClassNameRequest
        @return: ReadClassNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.read_class_name_with_options_async(request, runtime)

    def read_message_with_options(
        self,
        request: notifications_20241225_models.ReadMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> notifications_20241225_models.ReadMessageResponse:
        """
        @summary 方法描述：消息标记为已读
        
        @param request: ReadMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReadMessageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not UtilClient.is_unset(request.client_source):
            body['ClientSource'] = request.client_source
        if not UtilClient.is_unset(request.cookies):
            body['Cookies'] = request.cookies
        if not UtilClient.is_unset(request.msg_id):
            body['MsgId'] = request.msg_id
        if not UtilClient.is_unset(request.src_url):
            body['SrcUrl'] = request.src_url
        if not UtilClient.is_unset(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not UtilClient.is_unset(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReadMessage',
            version='2024-12-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            notifications_20241225_models.ReadMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_message_with_options_async(
        self,
        request: notifications_20241225_models.ReadMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> notifications_20241225_models.ReadMessageResponse:
        """
        @summary 方法描述：消息标记为已读
        
        @param request: ReadMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReadMessageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not UtilClient.is_unset(request.client_source):
            body['ClientSource'] = request.client_source
        if not UtilClient.is_unset(request.cookies):
            body['Cookies'] = request.cookies
        if not UtilClient.is_unset(request.msg_id):
            body['MsgId'] = request.msg_id
        if not UtilClient.is_unset(request.src_url):
            body['SrcUrl'] = request.src_url
        if not UtilClient.is_unset(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not UtilClient.is_unset(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReadMessage',
            version='2024-12-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            notifications_20241225_models.ReadMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_message(
        self,
        request: notifications_20241225_models.ReadMessageRequest,
    ) -> notifications_20241225_models.ReadMessageResponse:
        """
        @summary 方法描述：消息标记为已读
        
        @param request: ReadMessageRequest
        @return: ReadMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.read_message_with_options(request, runtime)

    async def read_message_async(
        self,
        request: notifications_20241225_models.ReadMessageRequest,
    ) -> notifications_20241225_models.ReadMessageResponse:
        """
        @summary 方法描述：消息标记为已读
        
        @param request: ReadMessageRequest
        @return: ReadMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.read_message_with_options_async(request, runtime)

    def read_message_content_with_options(
        self,
        request: notifications_20241225_models.ReadMessageContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> notifications_20241225_models.ReadMessageContentResponse:
        """
        @summary 方法描述：获取消息正文
        
        @param request: ReadMessageContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReadMessageContentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.client_source):
            body['ClientSource'] = request.client_source
        if not UtilClient.is_unset(request.cookies):
            body['Cookies'] = request.cookies
        if not UtilClient.is_unset(request.msg_id):
            body['MsgId'] = request.msg_id
        if not UtilClient.is_unset(request.src_url):
            body['SrcUrl'] = request.src_url
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not UtilClient.is_unset(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReadMessageContent',
            version='2024-12-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            notifications_20241225_models.ReadMessageContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_message_content_with_options_async(
        self,
        request: notifications_20241225_models.ReadMessageContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> notifications_20241225_models.ReadMessageContentResponse:
        """
        @summary 方法描述：获取消息正文
        
        @param request: ReadMessageContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReadMessageContentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.client_source):
            body['ClientSource'] = request.client_source
        if not UtilClient.is_unset(request.cookies):
            body['Cookies'] = request.cookies
        if not UtilClient.is_unset(request.msg_id):
            body['MsgId'] = request.msg_id
        if not UtilClient.is_unset(request.src_url):
            body['SrcUrl'] = request.src_url
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not UtilClient.is_unset(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReadMessageContent',
            version='2024-12-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            notifications_20241225_models.ReadMessageContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_message_content(
        self,
        request: notifications_20241225_models.ReadMessageContentRequest,
    ) -> notifications_20241225_models.ReadMessageContentResponse:
        """
        @summary 方法描述：获取消息正文
        
        @param request: ReadMessageContentRequest
        @return: ReadMessageContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.read_message_content_with_options(request, runtime)

    async def read_message_content_async(
        self,
        request: notifications_20241225_models.ReadMessageContentRequest,
    ) -> notifications_20241225_models.ReadMessageContentResponse:
        """
        @summary 方法描述：获取消息正文
        
        @param request: ReadMessageContentRequest
        @return: ReadMessageContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.read_message_content_with_options_async(request, runtime)

    def read_message_list_with_options(
        self,
        request: notifications_20241225_models.ReadMessageListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> notifications_20241225_models.ReadMessageListResponse:
        """
        @summary 方法描述：获取消息列表
        
        @param request: ReadMessageListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReadMessageListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.client_source):
            body['ClientSource'] = request.client_source
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.cookies):
            body['Cookies'] = request.cookies
        if not UtilClient.is_unset(request.loc):
            body['Loc'] = request.loc
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.src_url):
            body['SrcUrl'] = request.src_url
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReadMessageList',
            version='2024-12-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            notifications_20241225_models.ReadMessageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_message_list_with_options_async(
        self,
        request: notifications_20241225_models.ReadMessageListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> notifications_20241225_models.ReadMessageListResponse:
        """
        @summary 方法描述：获取消息列表
        
        @param request: ReadMessageListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReadMessageListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.client_source):
            body['ClientSource'] = request.client_source
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.cookies):
            body['Cookies'] = request.cookies
        if not UtilClient.is_unset(request.loc):
            body['Loc'] = request.loc
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.src_url):
            body['SrcUrl'] = request.src_url
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReadMessageList',
            version='2024-12-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            notifications_20241225_models.ReadMessageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_message_list(
        self,
        request: notifications_20241225_models.ReadMessageListRequest,
    ) -> notifications_20241225_models.ReadMessageListResponse:
        """
        @summary 方法描述：获取消息列表
        
        @param request: ReadMessageListRequest
        @return: ReadMessageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.read_message_list_with_options(request, runtime)

    async def read_message_list_async(
        self,
        request: notifications_20241225_models.ReadMessageListRequest,
    ) -> notifications_20241225_models.ReadMessageListResponse:
        """
        @summary 方法描述：获取消息列表
        
        @param request: ReadMessageListRequest
        @return: ReadMessageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.read_message_list_with_options_async(request, runtime)

    def read_message_new_total_with_options(
        self,
        request: notifications_20241225_models.ReadMessageNewTotalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> notifications_20241225_models.ReadMessageNewTotalResponse:
        """
        @summary 方法描述：获取未读消息总数
        
        @param request: ReadMessageNewTotalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReadMessageNewTotalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not UtilClient.is_unset(request.client_source):
            body['ClientSource'] = request.client_source
        if not UtilClient.is_unset(request.cookies):
            body['Cookies'] = request.cookies
        if not UtilClient.is_unset(request.src_url):
            body['SrcUrl'] = request.src_url
        if not UtilClient.is_unset(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not UtilClient.is_unset(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReadMessageNewTotal',
            version='2024-12-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            notifications_20241225_models.ReadMessageNewTotalResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_message_new_total_with_options_async(
        self,
        request: notifications_20241225_models.ReadMessageNewTotalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> notifications_20241225_models.ReadMessageNewTotalResponse:
        """
        @summary 方法描述：获取未读消息总数
        
        @param request: ReadMessageNewTotalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReadMessageNewTotalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not UtilClient.is_unset(request.client_source):
            body['ClientSource'] = request.client_source
        if not UtilClient.is_unset(request.cookies):
            body['Cookies'] = request.cookies
        if not UtilClient.is_unset(request.src_url):
            body['SrcUrl'] = request.src_url
        if not UtilClient.is_unset(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not UtilClient.is_unset(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReadMessageNewTotal',
            version='2024-12-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            notifications_20241225_models.ReadMessageNewTotalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_message_new_total(
        self,
        request: notifications_20241225_models.ReadMessageNewTotalRequest,
    ) -> notifications_20241225_models.ReadMessageNewTotalResponse:
        """
        @summary 方法描述：获取未读消息总数
        
        @param request: ReadMessageNewTotalRequest
        @return: ReadMessageNewTotalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.read_message_new_total_with_options(request, runtime)

    async def read_message_new_total_async(
        self,
        request: notifications_20241225_models.ReadMessageNewTotalRequest,
    ) -> notifications_20241225_models.ReadMessageNewTotalResponse:
        """
        @summary 方法描述：获取未读消息总数
        
        @param request: ReadMessageNewTotalRequest
        @return: ReadMessageNewTotalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.read_message_new_total_with_options_async(request, runtime)

    def read_num_group_by_class_with_options(
        self,
        request: notifications_20241225_models.ReadNumGroupByClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> notifications_20241225_models.ReadNumGroupByClassResponse:
        """
        @summary 方法描述：获取各分类已读消息数
        
        @param request: ReadNumGroupByClassRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReadNumGroupByClassResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not UtilClient.is_unset(request.client_source):
            body['ClientSource'] = request.client_source
        if not UtilClient.is_unset(request.cookies):
            body['Cookies'] = request.cookies
        if not UtilClient.is_unset(request.src_url):
            body['SrcUrl'] = request.src_url
        if not UtilClient.is_unset(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not UtilClient.is_unset(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReadNumGroupByClass',
            version='2024-12-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            notifications_20241225_models.ReadNumGroupByClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_num_group_by_class_with_options_async(
        self,
        request: notifications_20241225_models.ReadNumGroupByClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> notifications_20241225_models.ReadNumGroupByClassResponse:
        """
        @summary 方法描述：获取各分类已读消息数
        
        @param request: ReadNumGroupByClassRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReadNumGroupByClassResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not UtilClient.is_unset(request.client_source):
            body['ClientSource'] = request.client_source
        if not UtilClient.is_unset(request.cookies):
            body['Cookies'] = request.cookies
        if not UtilClient.is_unset(request.src_url):
            body['SrcUrl'] = request.src_url
        if not UtilClient.is_unset(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not UtilClient.is_unset(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReadNumGroupByClass',
            version='2024-12-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            notifications_20241225_models.ReadNumGroupByClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_num_group_by_class(
        self,
        request: notifications_20241225_models.ReadNumGroupByClassRequest,
    ) -> notifications_20241225_models.ReadNumGroupByClassResponse:
        """
        @summary 方法描述：获取各分类已读消息数
        
        @param request: ReadNumGroupByClassRequest
        @return: ReadNumGroupByClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.read_num_group_by_class_with_options(request, runtime)

    async def read_num_group_by_class_async(
        self,
        request: notifications_20241225_models.ReadNumGroupByClassRequest,
    ) -> notifications_20241225_models.ReadNumGroupByClassResponse:
        """
        @summary 方法描述：获取各分类已读消息数
        
        @param request: ReadNumGroupByClassRequest
        @return: ReadNumGroupByClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.read_num_group_by_class_with_options_async(request, runtime)

    def read_num_group_total_with_options(
        self,
        request: notifications_20241225_models.ReadNumGroupTotalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> notifications_20241225_models.ReadNumGroupTotalResponse:
        """
        @summary 方法描述：获取所有分类下的信息
        
        @param request: ReadNumGroupTotalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReadNumGroupTotalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not UtilClient.is_unset(request.client_source):
            body['ClientSource'] = request.client_source
        if not UtilClient.is_unset(request.cookies):
            body['Cookies'] = request.cookies
        if not UtilClient.is_unset(request.src_url):
            body['SrcUrl'] = request.src_url
        if not UtilClient.is_unset(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReadNumGroupTotal',
            version='2024-12-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            notifications_20241225_models.ReadNumGroupTotalResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_num_group_total_with_options_async(
        self,
        request: notifications_20241225_models.ReadNumGroupTotalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> notifications_20241225_models.ReadNumGroupTotalResponse:
        """
        @summary 方法描述：获取所有分类下的信息
        
        @param request: ReadNumGroupTotalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReadNumGroupTotalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.caller_protocol):
            body['CallerProtocol'] = request.caller_protocol
        if not UtilClient.is_unset(request.client_source):
            body['ClientSource'] = request.client_source
        if not UtilClient.is_unset(request.cookies):
            body['Cookies'] = request.cookies
        if not UtilClient.is_unset(request.src_url):
            body['SrcUrl'] = request.src_url
        if not UtilClient.is_unset(request.tenant_code):
            body['TenantCode'] = request.tenant_code
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.uid_type):
            body['UidType'] = request.uid_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReadNumGroupTotal',
            version='2024-12-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            notifications_20241225_models.ReadNumGroupTotalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_num_group_total(
        self,
        request: notifications_20241225_models.ReadNumGroupTotalRequest,
    ) -> notifications_20241225_models.ReadNumGroupTotalResponse:
        """
        @summary 方法描述：获取所有分类下的信息
        
        @param request: ReadNumGroupTotalRequest
        @return: ReadNumGroupTotalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.read_num_group_total_with_options(request, runtime)

    async def read_num_group_total_async(
        self,
        request: notifications_20241225_models.ReadNumGroupTotalRequest,
    ) -> notifications_20241225_models.ReadNumGroupTotalResponse:
        """
        @summary 方法描述：获取所有分类下的信息
        
        @param request: ReadNumGroupTotalRequest
        @return: ReadNumGroupTotalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.read_num_group_total_with_options_async(request, runtime)
