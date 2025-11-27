# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models
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
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'ap-southeast-1': 'dysmsapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'dysmsapi.ap-southeast-5.aliyuncs.com',
            'cn-beijing': 'dysmsapi-proxy.cn-beijing.aliyuncs.com',
            'cn-hongkong': 'dysmsapi-xman.cn-hongkong.aliyuncs.com',
            'eu-central-1': 'dysmsapi.eu-central-1.aliyuncs.com',
            'us-east-1': 'dysmsapi.us-east-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dysmsapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_ext_code_sign_with_options(
        self,
        request: dysmsapi_20170525_models.AddExtCodeSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.AddExtCodeSignResponse:
        """
        @summary 添加验证码签名信息
        
        @param request: AddExtCodeSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddExtCodeSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ext_code):
            query['ExtCode'] = request.ext_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddExtCodeSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.AddExtCodeSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_ext_code_sign_with_options_async(
        self,
        request: dysmsapi_20170525_models.AddExtCodeSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.AddExtCodeSignResponse:
        """
        @summary 添加验证码签名信息
        
        @param request: AddExtCodeSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddExtCodeSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ext_code):
            query['ExtCode'] = request.ext_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddExtCodeSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.AddExtCodeSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_ext_code_sign(
        self,
        request: dysmsapi_20170525_models.AddExtCodeSignRequest,
    ) -> dysmsapi_20170525_models.AddExtCodeSignResponse:
        """
        @summary 添加验证码签名信息
        
        @param request: AddExtCodeSignRequest
        @return: AddExtCodeSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_ext_code_sign_with_options(request, runtime)

    async def add_ext_code_sign_async(
        self,
        request: dysmsapi_20170525_models.AddExtCodeSignRequest,
    ) -> dysmsapi_20170525_models.AddExtCodeSignResponse:
        """
        @summary 添加验证码签名信息
        
        @param request: AddExtCodeSignRequest
        @return: AddExtCodeSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_ext_code_sign_with_options_async(request, runtime)

    def add_short_url_with_options(
        self,
        request: dysmsapi_20170525_models.AddShortUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.AddShortUrlResponse:
        """
        @summary Creates a short URL.
        
        @description    Before you call this operation, you must register the primary domain name of the source URL in the Short Message Service (SMS) console. After the domain name is registered, you can call this operation to create a short URL. For more information, see [Domain name registration](https://help.aliyun.com/document_detail/302325.html#title-mau-zdh-hd0).
        You can create up to 3,000 short URLs within a natural day.
        After a short URL is generated, a security review is required. Generally, the review takes 10 minutes to 2 hours to complete. Before the security review is passed, the short URL cannot be directly accessed.
        
        @param request: AddShortUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddShortUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.effective_days):
            body['EffectiveDays'] = request.effective_days
        if not UtilClient.is_unset(request.short_url_name):
            body['ShortUrlName'] = request.short_url_name
        if not UtilClient.is_unset(request.source_url):
            body['SourceUrl'] = request.source_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddShortUrl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.AddShortUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_short_url_with_options_async(
        self,
        request: dysmsapi_20170525_models.AddShortUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.AddShortUrlResponse:
        """
        @summary Creates a short URL.
        
        @description    Before you call this operation, you must register the primary domain name of the source URL in the Short Message Service (SMS) console. After the domain name is registered, you can call this operation to create a short URL. For more information, see [Domain name registration](https://help.aliyun.com/document_detail/302325.html#title-mau-zdh-hd0).
        You can create up to 3,000 short URLs within a natural day.
        After a short URL is generated, a security review is required. Generally, the review takes 10 minutes to 2 hours to complete. Before the security review is passed, the short URL cannot be directly accessed.
        
        @param request: AddShortUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddShortUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.effective_days):
            body['EffectiveDays'] = request.effective_days
        if not UtilClient.is_unset(request.short_url_name):
            body['ShortUrlName'] = request.short_url_name
        if not UtilClient.is_unset(request.source_url):
            body['SourceUrl'] = request.source_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddShortUrl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.AddShortUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_short_url(
        self,
        request: dysmsapi_20170525_models.AddShortUrlRequest,
    ) -> dysmsapi_20170525_models.AddShortUrlResponse:
        """
        @summary Creates a short URL.
        
        @description    Before you call this operation, you must register the primary domain name of the source URL in the Short Message Service (SMS) console. After the domain name is registered, you can call this operation to create a short URL. For more information, see [Domain name registration](https://help.aliyun.com/document_detail/302325.html#title-mau-zdh-hd0).
        You can create up to 3,000 short URLs within a natural day.
        After a short URL is generated, a security review is required. Generally, the review takes 10 minutes to 2 hours to complete. Before the security review is passed, the short URL cannot be directly accessed.
        
        @param request: AddShortUrlRequest
        @return: AddShortUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_short_url_with_options(request, runtime)

    async def add_short_url_async(
        self,
        request: dysmsapi_20170525_models.AddShortUrlRequest,
    ) -> dysmsapi_20170525_models.AddShortUrlResponse:
        """
        @summary Creates a short URL.
        
        @description    Before you call this operation, you must register the primary domain name of the source URL in the Short Message Service (SMS) console. After the domain name is registered, you can call this operation to create a short URL. For more information, see [Domain name registration](https://help.aliyun.com/document_detail/302325.html#title-mau-zdh-hd0).
        You can create up to 3,000 short URLs within a natural day.
        After a short URL is generated, a security review is required. Generally, the review takes 10 minutes to 2 hours to complete. Before the security review is passed, the short URL cannot be directly accessed.
        
        @param request: AddShortUrlRequest
        @return: AddShortUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_short_url_with_options_async(request, runtime)

    def add_sms_sign_with_options(
        self,
        request: dysmsapi_20170525_models.AddSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.AddSmsSignResponse:
        """
        @summary Creates a signature.
        
        @description You can call the AddSmsSign operation or use the [Short Message Service (SMS) console](https://dysms.console.aliyun.com/dysms.htm#/overview) to create an SMS signature. The signature must comply with the [SMS signature specifications](https://help.aliyun.com/document_detail/108076.html). You can call the QuerySmsSign operation or use the SMS console to query the review status of the signature.
        For more information, see [Usage notes](https://help.aliyun.com/document_detail/55324.html).
        ### QPS limit
        You can call this operation only once per second. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        >
        You cannot cancel the review of a signature.
        Individual users can create only one verification code signature, and can create only one general-purpose signature within a natural day. If you need to apply for multiple signatures, we recommend that you upgrade your account to an enterprise user.
        If you need to use the same signature for messages sent to recipients both in and outside the Chinese mainland, the signature must be a general-purpose signature.
        If you apply for a signature or message template, you must specify the signature scenario or template type. You must also provide the information of your services, such as a website URL, a domain name with an ICP filing, an application download URL, or the name of your WeChat official account or mini program. For sign-in scenarios, you must also provide an account and password for tests. A detailed description can improve the review efficiency of signatures and templates.
        An SMS signature must undergo a thorough review process before it can be approved for use.
        
        @param request: AddSmsSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddSmsSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sign_source):
            query['SignSource'] = request.sign_source
        if not UtilClient.is_unset(request.sign_type):
            query['SignType'] = request.sign_type
        body = {}
        if not UtilClient.is_unset(request.sign_file_list):
            body['SignFileList'] = request.sign_file_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddSmsSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.AddSmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_sms_sign_with_options_async(
        self,
        request: dysmsapi_20170525_models.AddSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.AddSmsSignResponse:
        """
        @summary Creates a signature.
        
        @description You can call the AddSmsSign operation or use the [Short Message Service (SMS) console](https://dysms.console.aliyun.com/dysms.htm#/overview) to create an SMS signature. The signature must comply with the [SMS signature specifications](https://help.aliyun.com/document_detail/108076.html). You can call the QuerySmsSign operation or use the SMS console to query the review status of the signature.
        For more information, see [Usage notes](https://help.aliyun.com/document_detail/55324.html).
        ### QPS limit
        You can call this operation only once per second. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        >
        You cannot cancel the review of a signature.
        Individual users can create only one verification code signature, and can create only one general-purpose signature within a natural day. If you need to apply for multiple signatures, we recommend that you upgrade your account to an enterprise user.
        If you need to use the same signature for messages sent to recipients both in and outside the Chinese mainland, the signature must be a general-purpose signature.
        If you apply for a signature or message template, you must specify the signature scenario or template type. You must also provide the information of your services, such as a website URL, a domain name with an ICP filing, an application download URL, or the name of your WeChat official account or mini program. For sign-in scenarios, you must also provide an account and password for tests. A detailed description can improve the review efficiency of signatures and templates.
        An SMS signature must undergo a thorough review process before it can be approved for use.
        
        @param request: AddSmsSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddSmsSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sign_source):
            query['SignSource'] = request.sign_source
        if not UtilClient.is_unset(request.sign_type):
            query['SignType'] = request.sign_type
        body = {}
        if not UtilClient.is_unset(request.sign_file_list):
            body['SignFileList'] = request.sign_file_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddSmsSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.AddSmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_sms_sign(
        self,
        request: dysmsapi_20170525_models.AddSmsSignRequest,
    ) -> dysmsapi_20170525_models.AddSmsSignResponse:
        """
        @summary Creates a signature.
        
        @description You can call the AddSmsSign operation or use the [Short Message Service (SMS) console](https://dysms.console.aliyun.com/dysms.htm#/overview) to create an SMS signature. The signature must comply with the [SMS signature specifications](https://help.aliyun.com/document_detail/108076.html). You can call the QuerySmsSign operation or use the SMS console to query the review status of the signature.
        For more information, see [Usage notes](https://help.aliyun.com/document_detail/55324.html).
        ### QPS limit
        You can call this operation only once per second. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        >
        You cannot cancel the review of a signature.
        Individual users can create only one verification code signature, and can create only one general-purpose signature within a natural day. If you need to apply for multiple signatures, we recommend that you upgrade your account to an enterprise user.
        If you need to use the same signature for messages sent to recipients both in and outside the Chinese mainland, the signature must be a general-purpose signature.
        If you apply for a signature or message template, you must specify the signature scenario or template type. You must also provide the information of your services, such as a website URL, a domain name with an ICP filing, an application download URL, or the name of your WeChat official account or mini program. For sign-in scenarios, you must also provide an account and password for tests. A detailed description can improve the review efficiency of signatures and templates.
        An SMS signature must undergo a thorough review process before it can be approved for use.
        
        @param request: AddSmsSignRequest
        @return: AddSmsSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_sms_sign_with_options(request, runtime)

    async def add_sms_sign_async(
        self,
        request: dysmsapi_20170525_models.AddSmsSignRequest,
    ) -> dysmsapi_20170525_models.AddSmsSignResponse:
        """
        @summary Creates a signature.
        
        @description You can call the AddSmsSign operation or use the [Short Message Service (SMS) console](https://dysms.console.aliyun.com/dysms.htm#/overview) to create an SMS signature. The signature must comply with the [SMS signature specifications](https://help.aliyun.com/document_detail/108076.html). You can call the QuerySmsSign operation or use the SMS console to query the review status of the signature.
        For more information, see [Usage notes](https://help.aliyun.com/document_detail/55324.html).
        ### QPS limit
        You can call this operation only once per second. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        >
        You cannot cancel the review of a signature.
        Individual users can create only one verification code signature, and can create only one general-purpose signature within a natural day. If you need to apply for multiple signatures, we recommend that you upgrade your account to an enterprise user.
        If you need to use the same signature for messages sent to recipients both in and outside the Chinese mainland, the signature must be a general-purpose signature.
        If you apply for a signature or message template, you must specify the signature scenario or template type. You must also provide the information of your services, such as a website URL, a domain name with an ICP filing, an application download URL, or the name of your WeChat official account or mini program. For sign-in scenarios, you must also provide an account and password for tests. A detailed description can improve the review efficiency of signatures and templates.
        An SMS signature must undergo a thorough review process before it can be approved for use.
        
        @param request: AddSmsSignRequest
        @return: AddSmsSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_sms_sign_with_options_async(request, runtime)

    def add_sms_template_with_options(
        self,
        request: dysmsapi_20170525_models.AddSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.AddSmsTemplateResponse:
        """
        @deprecated OpenAPI AddSmsTemplate is deprecated, please use Dysmsapi::2017-05-25::CreateSmsTemplate instead.
        
        @summary Creates a message template.
        
        @description You can call the operation or use the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview) to apply for a message template. The template must comply with the [message template specifications](https://help.aliyun.com/document_detail/108253.html). You can call the [QuerySmsTemplate](https://help.aliyun.com/document_detail/419289.html) operation or use the Alibaba Cloud SMS console to check whether the message template is approved.
        >
        Message templates pending approval can be withdrawn. You can withdraw a message template pending approval on the Message Templates tab in the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview).
        Message templates that have been approved can be deleted, and cannot be modified. You can delete a message template pending approval on the Message Templates tab in the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview).
        If you call the AddSmsTemplate operation, you can apply for a maximum of 100 message templates in a calendar day. After you apply for a message template, we recommend that you wait for at least 30 seconds before you apply for another one. If you use the Alibaba Cloud SMS console, you can apply for an unlimited number of message templates.
        Messages sent to the Chinese mainland and messages sent to countries or regions outside the Chinese mainland use separate message templates. Create message templates based on your needs.
        If you apply for a signature or message template, you must specify the signature scenario or template type. You must also provide the information of your services, such as a website URL, a domain name with an ICP filing, an application download URL, or the name of your WeChat official account or mini program. For sign-in scenarios, you must also provide an account and password for tests. A detailed description can improve the review efficiency of signatures and templates.
        A signature must undergo a thorough review process before it can be approved for use. For more information, see [Usage notes](https://help.aliyun.com/document_detail/55324.html).
        ### QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddSmsTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddSmsTemplateResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_content):
            query['TemplateContent'] = request.template_content
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.AddSmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_sms_template_with_options_async(
        self,
        request: dysmsapi_20170525_models.AddSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.AddSmsTemplateResponse:
        """
        @deprecated OpenAPI AddSmsTemplate is deprecated, please use Dysmsapi::2017-05-25::CreateSmsTemplate instead.
        
        @summary Creates a message template.
        
        @description You can call the operation or use the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview) to apply for a message template. The template must comply with the [message template specifications](https://help.aliyun.com/document_detail/108253.html). You can call the [QuerySmsTemplate](https://help.aliyun.com/document_detail/419289.html) operation or use the Alibaba Cloud SMS console to check whether the message template is approved.
        >
        Message templates pending approval can be withdrawn. You can withdraw a message template pending approval on the Message Templates tab in the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview).
        Message templates that have been approved can be deleted, and cannot be modified. You can delete a message template pending approval on the Message Templates tab in the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview).
        If you call the AddSmsTemplate operation, you can apply for a maximum of 100 message templates in a calendar day. After you apply for a message template, we recommend that you wait for at least 30 seconds before you apply for another one. If you use the Alibaba Cloud SMS console, you can apply for an unlimited number of message templates.
        Messages sent to the Chinese mainland and messages sent to countries or regions outside the Chinese mainland use separate message templates. Create message templates based on your needs.
        If you apply for a signature or message template, you must specify the signature scenario or template type. You must also provide the information of your services, such as a website URL, a domain name with an ICP filing, an application download URL, or the name of your WeChat official account or mini program. For sign-in scenarios, you must also provide an account and password for tests. A detailed description can improve the review efficiency of signatures and templates.
        A signature must undergo a thorough review process before it can be approved for use. For more information, see [Usage notes](https://help.aliyun.com/document_detail/55324.html).
        ### QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddSmsTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddSmsTemplateResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_content):
            query['TemplateContent'] = request.template_content
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.AddSmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_sms_template(
        self,
        request: dysmsapi_20170525_models.AddSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.AddSmsTemplateResponse:
        """
        @deprecated OpenAPI AddSmsTemplate is deprecated, please use Dysmsapi::2017-05-25::CreateSmsTemplate instead.
        
        @summary Creates a message template.
        
        @description You can call the operation or use the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview) to apply for a message template. The template must comply with the [message template specifications](https://help.aliyun.com/document_detail/108253.html). You can call the [QuerySmsTemplate](https://help.aliyun.com/document_detail/419289.html) operation or use the Alibaba Cloud SMS console to check whether the message template is approved.
        >
        Message templates pending approval can be withdrawn. You can withdraw a message template pending approval on the Message Templates tab in the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview).
        Message templates that have been approved can be deleted, and cannot be modified. You can delete a message template pending approval on the Message Templates tab in the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview).
        If you call the AddSmsTemplate operation, you can apply for a maximum of 100 message templates in a calendar day. After you apply for a message template, we recommend that you wait for at least 30 seconds before you apply for another one. If you use the Alibaba Cloud SMS console, you can apply for an unlimited number of message templates.
        Messages sent to the Chinese mainland and messages sent to countries or regions outside the Chinese mainland use separate message templates. Create message templates based on your needs.
        If you apply for a signature or message template, you must specify the signature scenario or template type. You must also provide the information of your services, such as a website URL, a domain name with an ICP filing, an application download URL, or the name of your WeChat official account or mini program. For sign-in scenarios, you must also provide an account and password for tests. A detailed description can improve the review efficiency of signatures and templates.
        A signature must undergo a thorough review process before it can be approved for use. For more information, see [Usage notes](https://help.aliyun.com/document_detail/55324.html).
        ### QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddSmsTemplateRequest
        @return: AddSmsTemplateResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.add_sms_template_with_options(request, runtime)

    async def add_sms_template_async(
        self,
        request: dysmsapi_20170525_models.AddSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.AddSmsTemplateResponse:
        """
        @deprecated OpenAPI AddSmsTemplate is deprecated, please use Dysmsapi::2017-05-25::CreateSmsTemplate instead.
        
        @summary Creates a message template.
        
        @description You can call the operation or use the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview) to apply for a message template. The template must comply with the [message template specifications](https://help.aliyun.com/document_detail/108253.html). You can call the [QuerySmsTemplate](https://help.aliyun.com/document_detail/419289.html) operation or use the Alibaba Cloud SMS console to check whether the message template is approved.
        >
        Message templates pending approval can be withdrawn. You can withdraw a message template pending approval on the Message Templates tab in the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview).
        Message templates that have been approved can be deleted, and cannot be modified. You can delete a message template pending approval on the Message Templates tab in the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview).
        If you call the AddSmsTemplate operation, you can apply for a maximum of 100 message templates in a calendar day. After you apply for a message template, we recommend that you wait for at least 30 seconds before you apply for another one. If you use the Alibaba Cloud SMS console, you can apply for an unlimited number of message templates.
        Messages sent to the Chinese mainland and messages sent to countries or regions outside the Chinese mainland use separate message templates. Create message templates based on your needs.
        If you apply for a signature or message template, you must specify the signature scenario or template type. You must also provide the information of your services, such as a website URL, a domain name with an ICP filing, an application download URL, or the name of your WeChat official account or mini program. For sign-in scenarios, you must also provide an account and password for tests. A detailed description can improve the review efficiency of signatures and templates.
        A signature must undergo a thorough review process before it can be approved for use. For more information, see [Usage notes](https://help.aliyun.com/document_detail/55324.html).
        ### QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddSmsTemplateRequest
        @return: AddSmsTemplateResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_sms_template_with_options_async(request, runtime)

    def change_signature_qualification_with_options(
        self,
        request: dysmsapi_20170525_models.ChangeSignatureQualificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.ChangeSignatureQualificationResponse:
        """
        @summary 更换签名的资质和授权书
        
        @param request: ChangeSignatureQualificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeSignatureQualificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_letter_id):
            query['AuthorizationLetterId'] = request.authorization_letter_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.signature_name):
            query['SignatureName'] = request.signature_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeSignatureQualification',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.ChangeSignatureQualificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_signature_qualification_with_options_async(
        self,
        request: dysmsapi_20170525_models.ChangeSignatureQualificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.ChangeSignatureQualificationResponse:
        """
        @summary 更换签名的资质和授权书
        
        @param request: ChangeSignatureQualificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeSignatureQualificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_letter_id):
            query['AuthorizationLetterId'] = request.authorization_letter_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.signature_name):
            query['SignatureName'] = request.signature_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeSignatureQualification',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.ChangeSignatureQualificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_signature_qualification(
        self,
        request: dysmsapi_20170525_models.ChangeSignatureQualificationRequest,
    ) -> dysmsapi_20170525_models.ChangeSignatureQualificationResponse:
        """
        @summary 更换签名的资质和授权书
        
        @param request: ChangeSignatureQualificationRequest
        @return: ChangeSignatureQualificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_signature_qualification_with_options(request, runtime)

    async def change_signature_qualification_async(
        self,
        request: dysmsapi_20170525_models.ChangeSignatureQualificationRequest,
    ) -> dysmsapi_20170525_models.ChangeSignatureQualificationResponse:
        """
        @summary 更换签名的资质和授权书
        
        @param request: ChangeSignatureQualificationRequest
        @return: ChangeSignatureQualificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_signature_qualification_with_options_async(request, runtime)

    def check_mobiles_card_support_with_options(
        self,
        request: dysmsapi_20170525_models.CheckMobilesCardSupportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.CheckMobilesCardSupportResponse:
        """
        @summary Checks whether a mobile phone number can receive card messages.
        
        @description ### QPS limit
        You can call this operation up to 2,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CheckMobilesCardSupportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckMobilesCardSupportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mobiles):
            query['Mobiles'] = request.mobiles
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckMobilesCardSupport',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.CheckMobilesCardSupportResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_mobiles_card_support_with_options_async(
        self,
        request: dysmsapi_20170525_models.CheckMobilesCardSupportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.CheckMobilesCardSupportResponse:
        """
        @summary Checks whether a mobile phone number can receive card messages.
        
        @description ### QPS limit
        You can call this operation up to 2,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CheckMobilesCardSupportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckMobilesCardSupportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mobiles):
            query['Mobiles'] = request.mobiles
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckMobilesCardSupport',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.CheckMobilesCardSupportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_mobiles_card_support(
        self,
        request: dysmsapi_20170525_models.CheckMobilesCardSupportRequest,
    ) -> dysmsapi_20170525_models.CheckMobilesCardSupportResponse:
        """
        @summary Checks whether a mobile phone number can receive card messages.
        
        @description ### QPS limit
        You can call this operation up to 2,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CheckMobilesCardSupportRequest
        @return: CheckMobilesCardSupportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_mobiles_card_support_with_options(request, runtime)

    async def check_mobiles_card_support_async(
        self,
        request: dysmsapi_20170525_models.CheckMobilesCardSupportRequest,
    ) -> dysmsapi_20170525_models.CheckMobilesCardSupportResponse:
        """
        @summary Checks whether a mobile phone number can receive card messages.
        
        @description ### QPS limit
        You can call this operation up to 2,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CheckMobilesCardSupportRequest
        @return: CheckMobilesCardSupportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_mobiles_card_support_with_options_async(request, runtime)

    def conversion_data_intl_with_options(
        self,
        request: dysmsapi_20170525_models.ConversionDataIntlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.ConversionDataIntlResponse:
        """
        @summary Sends conversion rate information to Alibaba Cloud SMS.
        
        @param request: ConversionDataIntlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConversionDataIntlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conversion_rate):
            query['ConversionRate'] = request.conversion_rate
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.report_time):
            query['ReportTime'] = request.report_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConversionDataIntl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.ConversionDataIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def conversion_data_intl_with_options_async(
        self,
        request: dysmsapi_20170525_models.ConversionDataIntlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.ConversionDataIntlResponse:
        """
        @summary Sends conversion rate information to Alibaba Cloud SMS.
        
        @param request: ConversionDataIntlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConversionDataIntlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conversion_rate):
            query['ConversionRate'] = request.conversion_rate
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.report_time):
            query['ReportTime'] = request.report_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConversionDataIntl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.ConversionDataIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def conversion_data_intl(
        self,
        request: dysmsapi_20170525_models.ConversionDataIntlRequest,
    ) -> dysmsapi_20170525_models.ConversionDataIntlResponse:
        """
        @summary Sends conversion rate information to Alibaba Cloud SMS.
        
        @param request: ConversionDataIntlRequest
        @return: ConversionDataIntlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.conversion_data_intl_with_options(request, runtime)

    async def conversion_data_intl_async(
        self,
        request: dysmsapi_20170525_models.ConversionDataIntlRequest,
    ) -> dysmsapi_20170525_models.ConversionDataIntlResponse:
        """
        @summary Sends conversion rate information to Alibaba Cloud SMS.
        
        @param request: ConversionDataIntlRequest
        @return: ConversionDataIntlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.conversion_data_intl_with_options_async(request, runtime)

    def create_card_sms_template_with_options(
        self,
        tmp_req: dysmsapi_20170525_models.CreateCardSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.CreateCardSmsTemplateResponse:
        """
        @summary Creates a card message template.
        
        @description    The CreateCardSmsTemplate operation saves the card message template information, submits it to the mobile phone manufacturer for approval, and returns the message template ID.
        If the type of the message template is not supported or events that are not supported by the mobile phone manufacturer are specified, the template is not submitted. For more information, see [Supported message templates](https://help.aliyun.com/document_detail/434611.html).
        For information about sample card message templates, see [Sample card message templates](https://help.aliyun.com/document_detail/435361.html).
        ### QPS limit
        You can call this operation up to 300 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param tmp_req: CreateCardSmsTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCardSmsTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysmsapi_20170525_models.CreateCardSmsTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.template):
            request.template_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not UtilClient.is_unset(request.factorys):
            query['Factorys'] = request.factorys
        if not UtilClient.is_unset(request.memo):
            query['Memo'] = request.memo
        if not UtilClient.is_unset(request.template_shrink):
            query['Template'] = request.template_shrink
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCardSmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.CreateCardSmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_card_sms_template_with_options_async(
        self,
        tmp_req: dysmsapi_20170525_models.CreateCardSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.CreateCardSmsTemplateResponse:
        """
        @summary Creates a card message template.
        
        @description    The CreateCardSmsTemplate operation saves the card message template information, submits it to the mobile phone manufacturer for approval, and returns the message template ID.
        If the type of the message template is not supported or events that are not supported by the mobile phone manufacturer are specified, the template is not submitted. For more information, see [Supported message templates](https://help.aliyun.com/document_detail/434611.html).
        For information about sample card message templates, see [Sample card message templates](https://help.aliyun.com/document_detail/435361.html).
        ### QPS limit
        You can call this operation up to 300 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param tmp_req: CreateCardSmsTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCardSmsTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysmsapi_20170525_models.CreateCardSmsTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.template):
            request.template_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template, 'Template', 'json')
        query = {}
        if not UtilClient.is_unset(request.factorys):
            query['Factorys'] = request.factorys
        if not UtilClient.is_unset(request.memo):
            query['Memo'] = request.memo
        if not UtilClient.is_unset(request.template_shrink):
            query['Template'] = request.template_shrink
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCardSmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.CreateCardSmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_card_sms_template(
        self,
        request: dysmsapi_20170525_models.CreateCardSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.CreateCardSmsTemplateResponse:
        """
        @summary Creates a card message template.
        
        @description    The CreateCardSmsTemplate operation saves the card message template information, submits it to the mobile phone manufacturer for approval, and returns the message template ID.
        If the type of the message template is not supported or events that are not supported by the mobile phone manufacturer are specified, the template is not submitted. For more information, see [Supported message templates](https://help.aliyun.com/document_detail/434611.html).
        For information about sample card message templates, see [Sample card message templates](https://help.aliyun.com/document_detail/435361.html).
        ### QPS limit
        You can call this operation up to 300 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateCardSmsTemplateRequest
        @return: CreateCardSmsTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_card_sms_template_with_options(request, runtime)

    async def create_card_sms_template_async(
        self,
        request: dysmsapi_20170525_models.CreateCardSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.CreateCardSmsTemplateResponse:
        """
        @summary Creates a card message template.
        
        @description    The CreateCardSmsTemplate operation saves the card message template information, submits it to the mobile phone manufacturer for approval, and returns the message template ID.
        If the type of the message template is not supported or events that are not supported by the mobile phone manufacturer are specified, the template is not submitted. For more information, see [Supported message templates](https://help.aliyun.com/document_detail/434611.html).
        For information about sample card message templates, see [Sample card message templates](https://help.aliyun.com/document_detail/435361.html).
        ### QPS limit
        You can call this operation up to 300 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateCardSmsTemplateRequest
        @return: CreateCardSmsTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_card_sms_template_with_options_async(request, runtime)

    def create_smart_short_url_with_options(
        self,
        request: dysmsapi_20170525_models.CreateSmartShortUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.CreateSmartShortUrlResponse:
        """
        @summary 创建短链
        
        @param request: CreateSmartShortUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmartShortUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_numbers):
            query['PhoneNumbers'] = request.phone_numbers
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_url):
            query['SourceUrl'] = request.source_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmartShortUrl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.CreateSmartShortUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_smart_short_url_with_options_async(
        self,
        request: dysmsapi_20170525_models.CreateSmartShortUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.CreateSmartShortUrlResponse:
        """
        @summary 创建短链
        
        @param request: CreateSmartShortUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmartShortUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_numbers):
            query['PhoneNumbers'] = request.phone_numbers
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_url):
            query['SourceUrl'] = request.source_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmartShortUrl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.CreateSmartShortUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_smart_short_url(
        self,
        request: dysmsapi_20170525_models.CreateSmartShortUrlRequest,
    ) -> dysmsapi_20170525_models.CreateSmartShortUrlResponse:
        """
        @summary 创建短链
        
        @param request: CreateSmartShortUrlRequest
        @return: CreateSmartShortUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_smart_short_url_with_options(request, runtime)

    async def create_smart_short_url_async(
        self,
        request: dysmsapi_20170525_models.CreateSmartShortUrlRequest,
    ) -> dysmsapi_20170525_models.CreateSmartShortUrlResponse:
        """
        @summary 创建短链
        
        @param request: CreateSmartShortUrlRequest
        @return: CreateSmartShortUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_smart_short_url_with_options_async(request, runtime)

    def create_sms_authorization_letter_with_options(
        self,
        tmp_req: dysmsapi_20170525_models.CreateSmsAuthorizationLetterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.CreateSmsAuthorizationLetterResponse:
        """
        @summary 创建委托授权书
        
        @param tmp_req: CreateSmsAuthorizationLetterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsAuthorizationLetterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysmsapi_20170525_models.CreateSmsAuthorizationLetterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sign_list):
            request.sign_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sign_list, 'SignList', 'json')
        query = {}
        if not UtilClient.is_unset(request.authorization):
            query['Authorization'] = request.authorization
        if not UtilClient.is_unset(request.authorization_letter_exp_date):
            query['AuthorizationLetterExpDate'] = request.authorization_letter_exp_date
        if not UtilClient.is_unset(request.authorization_letter_name):
            query['AuthorizationLetterName'] = request.authorization_letter_name
        if not UtilClient.is_unset(request.authorization_letter_pic):
            query['AuthorizationLetterPic'] = request.authorization_letter_pic
        if not UtilClient.is_unset(request.organization_code):
            query['OrganizationCode'] = request.organization_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.proxy_authorization):
            query['ProxyAuthorization'] = request.proxy_authorization
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_list_shrink):
            query['SignList'] = request.sign_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmsAuthorizationLetter',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.CreateSmsAuthorizationLetterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sms_authorization_letter_with_options_async(
        self,
        tmp_req: dysmsapi_20170525_models.CreateSmsAuthorizationLetterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.CreateSmsAuthorizationLetterResponse:
        """
        @summary 创建委托授权书
        
        @param tmp_req: CreateSmsAuthorizationLetterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsAuthorizationLetterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysmsapi_20170525_models.CreateSmsAuthorizationLetterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sign_list):
            request.sign_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sign_list, 'SignList', 'json')
        query = {}
        if not UtilClient.is_unset(request.authorization):
            query['Authorization'] = request.authorization
        if not UtilClient.is_unset(request.authorization_letter_exp_date):
            query['AuthorizationLetterExpDate'] = request.authorization_letter_exp_date
        if not UtilClient.is_unset(request.authorization_letter_name):
            query['AuthorizationLetterName'] = request.authorization_letter_name
        if not UtilClient.is_unset(request.authorization_letter_pic):
            query['AuthorizationLetterPic'] = request.authorization_letter_pic
        if not UtilClient.is_unset(request.organization_code):
            query['OrganizationCode'] = request.organization_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.proxy_authorization):
            query['ProxyAuthorization'] = request.proxy_authorization
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_list_shrink):
            query['SignList'] = request.sign_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmsAuthorizationLetter',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.CreateSmsAuthorizationLetterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sms_authorization_letter(
        self,
        request: dysmsapi_20170525_models.CreateSmsAuthorizationLetterRequest,
    ) -> dysmsapi_20170525_models.CreateSmsAuthorizationLetterResponse:
        """
        @summary 创建委托授权书
        
        @param request: CreateSmsAuthorizationLetterRequest
        @return: CreateSmsAuthorizationLetterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sms_authorization_letter_with_options(request, runtime)

    async def create_sms_authorization_letter_async(
        self,
        request: dysmsapi_20170525_models.CreateSmsAuthorizationLetterRequest,
    ) -> dysmsapi_20170525_models.CreateSmsAuthorizationLetterResponse:
        """
        @summary 创建委托授权书
        
        @param request: CreateSmsAuthorizationLetterRequest
        @return: CreateSmsAuthorizationLetterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_sms_authorization_letter_with_options_async(request, runtime)

    def create_sms_sign_with_options(
        self,
        tmp_req: dysmsapi_20170525_models.CreateSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.CreateSmsSignResponse:
        """
        @summary Create SMS Signature
        
        @description - For details about the announcement of changes to the new and original interfaces, see [Announcement on Updates to SMS Service Signature & Template Interfaces](https://help.aliyun.com/zh/sms/product-overview/announcement-on-sms-service-update-signature-template-interface).
        - Individual authenticated users can apply for one formal signature per natural day under the same Alibaba Cloud account, while enterprise authenticated users have no current restrictions. For details on the differences in rights between individual and enterprise users, please refer to [User Guide](https://help.aliyun.com/zh/sms/user-guide/usage-notes?spm).
        - Signature information applied through the interface will be synchronized in the SMS service console. For operations related to signatures in the console, see [SMS Signatures](https://help.aliyun.com/zh/sms/user-guide/create-signatures?spm).
        - After submitting the signature application, you can query the signature review status and details via the [GetSmsSign](https://help.aliyun.com/zh/sms/developer-reference/api-dysmsapi-2017-05-25-getsmssign?spm) interface. You can also [Configure Receipt Messages](https://help.aliyun.com/zh/sms/developer-reference/configure-delivery-receipts-1?spm) and obtain signature review status messages through SignSmsReport.
        
        @param tmp_req: CreateSmsSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsSignResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysmsapi_20170525_models.CreateSmsSignShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.more_data):
            request.more_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.more_data, 'MoreData', 'json')
        query = {}
        if not UtilClient.is_unset(request.apply_scene_content):
            query['ApplySceneContent'] = request.apply_scene_content
        if not UtilClient.is_unset(request.authorization_letter_id):
            query['AuthorizationLetterId'] = request.authorization_letter_id
        if not UtilClient.is_unset(request.more_data_shrink):
            query['MoreData'] = request.more_data_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sign_source):
            query['SignSource'] = request.sign_source
        if not UtilClient.is_unset(request.sign_type):
            query['SignType'] = request.sign_type
        if not UtilClient.is_unset(request.third_party):
            query['ThirdParty'] = request.third_party
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmsSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.CreateSmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sms_sign_with_options_async(
        self,
        tmp_req: dysmsapi_20170525_models.CreateSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.CreateSmsSignResponse:
        """
        @summary Create SMS Signature
        
        @description - For details about the announcement of changes to the new and original interfaces, see [Announcement on Updates to SMS Service Signature & Template Interfaces](https://help.aliyun.com/zh/sms/product-overview/announcement-on-sms-service-update-signature-template-interface).
        - Individual authenticated users can apply for one formal signature per natural day under the same Alibaba Cloud account, while enterprise authenticated users have no current restrictions. For details on the differences in rights between individual and enterprise users, please refer to [User Guide](https://help.aliyun.com/zh/sms/user-guide/usage-notes?spm).
        - Signature information applied through the interface will be synchronized in the SMS service console. For operations related to signatures in the console, see [SMS Signatures](https://help.aliyun.com/zh/sms/user-guide/create-signatures?spm).
        - After submitting the signature application, you can query the signature review status and details via the [GetSmsSign](https://help.aliyun.com/zh/sms/developer-reference/api-dysmsapi-2017-05-25-getsmssign?spm) interface. You can also [Configure Receipt Messages](https://help.aliyun.com/zh/sms/developer-reference/configure-delivery-receipts-1?spm) and obtain signature review status messages through SignSmsReport.
        
        @param tmp_req: CreateSmsSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsSignResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysmsapi_20170525_models.CreateSmsSignShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.more_data):
            request.more_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.more_data, 'MoreData', 'json')
        query = {}
        if not UtilClient.is_unset(request.apply_scene_content):
            query['ApplySceneContent'] = request.apply_scene_content
        if not UtilClient.is_unset(request.authorization_letter_id):
            query['AuthorizationLetterId'] = request.authorization_letter_id
        if not UtilClient.is_unset(request.more_data_shrink):
            query['MoreData'] = request.more_data_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sign_source):
            query['SignSource'] = request.sign_source
        if not UtilClient.is_unset(request.sign_type):
            query['SignType'] = request.sign_type
        if not UtilClient.is_unset(request.third_party):
            query['ThirdParty'] = request.third_party
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmsSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.CreateSmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sms_sign(
        self,
        request: dysmsapi_20170525_models.CreateSmsSignRequest,
    ) -> dysmsapi_20170525_models.CreateSmsSignResponse:
        """
        @summary Create SMS Signature
        
        @description - For details about the announcement of changes to the new and original interfaces, see [Announcement on Updates to SMS Service Signature & Template Interfaces](https://help.aliyun.com/zh/sms/product-overview/announcement-on-sms-service-update-signature-template-interface).
        - Individual authenticated users can apply for one formal signature per natural day under the same Alibaba Cloud account, while enterprise authenticated users have no current restrictions. For details on the differences in rights between individual and enterprise users, please refer to [User Guide](https://help.aliyun.com/zh/sms/user-guide/usage-notes?spm).
        - Signature information applied through the interface will be synchronized in the SMS service console. For operations related to signatures in the console, see [SMS Signatures](https://help.aliyun.com/zh/sms/user-guide/create-signatures?spm).
        - After submitting the signature application, you can query the signature review status and details via the [GetSmsSign](https://help.aliyun.com/zh/sms/developer-reference/api-dysmsapi-2017-05-25-getsmssign?spm) interface. You can also [Configure Receipt Messages](https://help.aliyun.com/zh/sms/developer-reference/configure-delivery-receipts-1?spm) and obtain signature review status messages through SignSmsReport.
        
        @param request: CreateSmsSignRequest
        @return: CreateSmsSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sms_sign_with_options(request, runtime)

    async def create_sms_sign_async(
        self,
        request: dysmsapi_20170525_models.CreateSmsSignRequest,
    ) -> dysmsapi_20170525_models.CreateSmsSignResponse:
        """
        @summary Create SMS Signature
        
        @description - For details about the announcement of changes to the new and original interfaces, see [Announcement on Updates to SMS Service Signature & Template Interfaces](https://help.aliyun.com/zh/sms/product-overview/announcement-on-sms-service-update-signature-template-interface).
        - Individual authenticated users can apply for one formal signature per natural day under the same Alibaba Cloud account, while enterprise authenticated users have no current restrictions. For details on the differences in rights between individual and enterprise users, please refer to [User Guide](https://help.aliyun.com/zh/sms/user-guide/usage-notes?spm).
        - Signature information applied through the interface will be synchronized in the SMS service console. For operations related to signatures in the console, see [SMS Signatures](https://help.aliyun.com/zh/sms/user-guide/create-signatures?spm).
        - After submitting the signature application, you can query the signature review status and details via the [GetSmsSign](https://help.aliyun.com/zh/sms/developer-reference/api-dysmsapi-2017-05-25-getsmssign?spm) interface. You can also [Configure Receipt Messages](https://help.aliyun.com/zh/sms/developer-reference/configure-delivery-receipts-1?spm) and obtain signature review status messages through SignSmsReport.
        
        @param request: CreateSmsSignRequest
        @return: CreateSmsSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_sms_sign_with_options_async(request, runtime)

    def create_sms_template_with_options(
        self,
        tmp_req: dysmsapi_20170525_models.CreateSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.CreateSmsTemplateResponse:
        """
        @summary Create SMS Template
        
        @description - For details about the changes of this new interface compared to the original one, please refer to [Announcement on the Update of SMS Service Signature & Template Interfaces](https://help.aliyun.com/zh/sms/product-overview/announcement-on-sms-service-update-signature-template-interface).
        - It is recommended to apply for SMS templates via the API with at least a 30-second interval between each request.
        - The template information applied through the API will be synchronized in the SMS service console. For operations related to templates in the console, please refer to SMS Templates.
        - After submitting the template application, you can query the audit status and details using the GetSmsTemplate interface. You can also configure delivery receipts to obtain the audit status messages via TemplateSmsReport.
        - Domestic SMS templates are not interchangeable with international/Hong Kong, Macao, and Taiwan SMS templates. Please apply for templates based on your business scenario.
        - Only enterprise-verified users can apply for promotional messages and international/Hong Kong, Macao, and Taiwan messages. For differences in rights between personal and enterprise users, please refer to Usage Instructions.
        
        @param tmp_req: CreateSmsTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysmsapi_20170525_models.CreateSmsTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.more_data):
            request.more_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.more_data, 'MoreData', 'json')
        query = {}
        if not UtilClient.is_unset(request.apply_scene_content):
            query['ApplySceneContent'] = request.apply_scene_content
        if not UtilClient.is_unset(request.intl_type):
            query['IntlType'] = request.intl_type
        if not UtilClient.is_unset(request.more_data_shrink):
            query['MoreData'] = request.more_data_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.related_sign_name):
            query['RelatedSignName'] = request.related_sign_name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_content):
            query['TemplateContent'] = request.template_content
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_rule):
            query['TemplateRule'] = request.template_rule
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        if not UtilClient.is_unset(request.traffic_driving):
            query['TrafficDriving'] = request.traffic_driving
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.CreateSmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sms_template_with_options_async(
        self,
        tmp_req: dysmsapi_20170525_models.CreateSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.CreateSmsTemplateResponse:
        """
        @summary Create SMS Template
        
        @description - For details about the changes of this new interface compared to the original one, please refer to [Announcement on the Update of SMS Service Signature & Template Interfaces](https://help.aliyun.com/zh/sms/product-overview/announcement-on-sms-service-update-signature-template-interface).
        - It is recommended to apply for SMS templates via the API with at least a 30-second interval between each request.
        - The template information applied through the API will be synchronized in the SMS service console. For operations related to templates in the console, please refer to SMS Templates.
        - After submitting the template application, you can query the audit status and details using the GetSmsTemplate interface. You can also configure delivery receipts to obtain the audit status messages via TemplateSmsReport.
        - Domestic SMS templates are not interchangeable with international/Hong Kong, Macao, and Taiwan SMS templates. Please apply for templates based on your business scenario.
        - Only enterprise-verified users can apply for promotional messages and international/Hong Kong, Macao, and Taiwan messages. For differences in rights between personal and enterprise users, please refer to Usage Instructions.
        
        @param tmp_req: CreateSmsTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysmsapi_20170525_models.CreateSmsTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.more_data):
            request.more_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.more_data, 'MoreData', 'json')
        query = {}
        if not UtilClient.is_unset(request.apply_scene_content):
            query['ApplySceneContent'] = request.apply_scene_content
        if not UtilClient.is_unset(request.intl_type):
            query['IntlType'] = request.intl_type
        if not UtilClient.is_unset(request.more_data_shrink):
            query['MoreData'] = request.more_data_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.related_sign_name):
            query['RelatedSignName'] = request.related_sign_name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_content):
            query['TemplateContent'] = request.template_content
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_rule):
            query['TemplateRule'] = request.template_rule
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        if not UtilClient.is_unset(request.traffic_driving):
            query['TrafficDriving'] = request.traffic_driving
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.CreateSmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sms_template(
        self,
        request: dysmsapi_20170525_models.CreateSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.CreateSmsTemplateResponse:
        """
        @summary Create SMS Template
        
        @description - For details about the changes of this new interface compared to the original one, please refer to [Announcement on the Update of SMS Service Signature & Template Interfaces](https://help.aliyun.com/zh/sms/product-overview/announcement-on-sms-service-update-signature-template-interface).
        - It is recommended to apply for SMS templates via the API with at least a 30-second interval between each request.
        - The template information applied through the API will be synchronized in the SMS service console. For operations related to templates in the console, please refer to SMS Templates.
        - After submitting the template application, you can query the audit status and details using the GetSmsTemplate interface. You can also configure delivery receipts to obtain the audit status messages via TemplateSmsReport.
        - Domestic SMS templates are not interchangeable with international/Hong Kong, Macao, and Taiwan SMS templates. Please apply for templates based on your business scenario.
        - Only enterprise-verified users can apply for promotional messages and international/Hong Kong, Macao, and Taiwan messages. For differences in rights between personal and enterprise users, please refer to Usage Instructions.
        
        @param request: CreateSmsTemplateRequest
        @return: CreateSmsTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sms_template_with_options(request, runtime)

    async def create_sms_template_async(
        self,
        request: dysmsapi_20170525_models.CreateSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.CreateSmsTemplateResponse:
        """
        @summary Create SMS Template
        
        @description - For details about the changes of this new interface compared to the original one, please refer to [Announcement on the Update of SMS Service Signature & Template Interfaces](https://help.aliyun.com/zh/sms/product-overview/announcement-on-sms-service-update-signature-template-interface).
        - It is recommended to apply for SMS templates via the API with at least a 30-second interval between each request.
        - The template information applied through the API will be synchronized in the SMS service console. For operations related to templates in the console, please refer to SMS Templates.
        - After submitting the template application, you can query the audit status and details using the GetSmsTemplate interface. You can also configure delivery receipts to obtain the audit status messages via TemplateSmsReport.
        - Domestic SMS templates are not interchangeable with international/Hong Kong, Macao, and Taiwan SMS templates. Please apply for templates based on your business scenario.
        - Only enterprise-verified users can apply for promotional messages and international/Hong Kong, Macao, and Taiwan messages. For differences in rights between personal and enterprise users, please refer to Usage Instructions.
        
        @param request: CreateSmsTemplateRequest
        @return: CreateSmsTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_sms_template_with_options_async(request, runtime)

    def delete_ext_code_sign_with_options(
        self,
        request: dysmsapi_20170525_models.DeleteExtCodeSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.DeleteExtCodeSignResponse:
        """
        @summary 删除验证码签名
        
        @param request: DeleteExtCodeSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExtCodeSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ext_code):
            query['ExtCode'] = request.ext_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExtCodeSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.DeleteExtCodeSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ext_code_sign_with_options_async(
        self,
        request: dysmsapi_20170525_models.DeleteExtCodeSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.DeleteExtCodeSignResponse:
        """
        @summary 删除验证码签名
        
        @param request: DeleteExtCodeSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExtCodeSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ext_code):
            query['ExtCode'] = request.ext_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExtCodeSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.DeleteExtCodeSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ext_code_sign(
        self,
        request: dysmsapi_20170525_models.DeleteExtCodeSignRequest,
    ) -> dysmsapi_20170525_models.DeleteExtCodeSignResponse:
        """
        @summary 删除验证码签名
        
        @param request: DeleteExtCodeSignRequest
        @return: DeleteExtCodeSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_ext_code_sign_with_options(request, runtime)

    async def delete_ext_code_sign_async(
        self,
        request: dysmsapi_20170525_models.DeleteExtCodeSignRequest,
    ) -> dysmsapi_20170525_models.DeleteExtCodeSignResponse:
        """
        @summary 删除验证码签名
        
        @param request: DeleteExtCodeSignRequest
        @return: DeleteExtCodeSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_ext_code_sign_with_options_async(request, runtime)

    def delete_short_url_with_options(
        self,
        request: dysmsapi_20170525_models.DeleteShortUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.DeleteShortUrlResponse:
        """
        @summary Deletes a short URL. After you delete a short URL, it cannot be changed to its original state.
        
        @description ### QPS limits
        You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteShortUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteShortUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.source_url):
            body['SourceUrl'] = request.source_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteShortUrl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.DeleteShortUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_short_url_with_options_async(
        self,
        request: dysmsapi_20170525_models.DeleteShortUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.DeleteShortUrlResponse:
        """
        @summary Deletes a short URL. After you delete a short URL, it cannot be changed to its original state.
        
        @description ### QPS limits
        You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteShortUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteShortUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.source_url):
            body['SourceUrl'] = request.source_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteShortUrl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.DeleteShortUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_short_url(
        self,
        request: dysmsapi_20170525_models.DeleteShortUrlRequest,
    ) -> dysmsapi_20170525_models.DeleteShortUrlResponse:
        """
        @summary Deletes a short URL. After you delete a short URL, it cannot be changed to its original state.
        
        @description ### QPS limits
        You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteShortUrlRequest
        @return: DeleteShortUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_short_url_with_options(request, runtime)

    async def delete_short_url_async(
        self,
        request: dysmsapi_20170525_models.DeleteShortUrlRequest,
    ) -> dysmsapi_20170525_models.DeleteShortUrlResponse:
        """
        @summary Deletes a short URL. After you delete a short URL, it cannot be changed to its original state.
        
        @description ### QPS limits
        You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteShortUrlRequest
        @return: DeleteShortUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_short_url_with_options_async(request, runtime)

    def delete_sms_qualification_with_options(
        self,
        request: dysmsapi_20170525_models.DeleteSmsQualificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.DeleteSmsQualificationResponse:
        """
        @summary 删除资质对客openAPI
        
        @param request: DeleteSmsQualificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSmsQualificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_group_id):
            query['QualificationGroupId'] = request.qualification_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmsQualification',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.DeleteSmsQualificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sms_qualification_with_options_async(
        self,
        request: dysmsapi_20170525_models.DeleteSmsQualificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.DeleteSmsQualificationResponse:
        """
        @summary 删除资质对客openAPI
        
        @param request: DeleteSmsQualificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSmsQualificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_group_id):
            query['QualificationGroupId'] = request.qualification_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmsQualification',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.DeleteSmsQualificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sms_qualification(
        self,
        request: dysmsapi_20170525_models.DeleteSmsQualificationRequest,
    ) -> dysmsapi_20170525_models.DeleteSmsQualificationResponse:
        """
        @summary 删除资质对客openAPI
        
        @param request: DeleteSmsQualificationRequest
        @return: DeleteSmsQualificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_sms_qualification_with_options(request, runtime)

    async def delete_sms_qualification_async(
        self,
        request: dysmsapi_20170525_models.DeleteSmsQualificationRequest,
    ) -> dysmsapi_20170525_models.DeleteSmsQualificationResponse:
        """
        @summary 删除资质对客openAPI
        
        @param request: DeleteSmsQualificationRequest
        @return: DeleteSmsQualificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_sms_qualification_with_options_async(request, runtime)

    def delete_sms_sign_with_options(
        self,
        request: dysmsapi_20170525_models.DeleteSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.DeleteSmsSignResponse:
        """
        @summary Deletes a signature.
        
        @description    You cannot delete a signature that has not been approved.
        After you delete a signature, you cannot recover it. Proceed with caution.
        ### QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteSmsSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSmsSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmsSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.DeleteSmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sms_sign_with_options_async(
        self,
        request: dysmsapi_20170525_models.DeleteSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.DeleteSmsSignResponse:
        """
        @summary Deletes a signature.
        
        @description    You cannot delete a signature that has not been approved.
        After you delete a signature, you cannot recover it. Proceed with caution.
        ### QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteSmsSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSmsSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmsSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.DeleteSmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sms_sign(
        self,
        request: dysmsapi_20170525_models.DeleteSmsSignRequest,
    ) -> dysmsapi_20170525_models.DeleteSmsSignResponse:
        """
        @summary Deletes a signature.
        
        @description    You cannot delete a signature that has not been approved.
        After you delete a signature, you cannot recover it. Proceed with caution.
        ### QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteSmsSignRequest
        @return: DeleteSmsSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_sms_sign_with_options(request, runtime)

    async def delete_sms_sign_async(
        self,
        request: dysmsapi_20170525_models.DeleteSmsSignRequest,
    ) -> dysmsapi_20170525_models.DeleteSmsSignResponse:
        """
        @summary Deletes a signature.
        
        @description    You cannot delete a signature that has not been approved.
        After you delete a signature, you cannot recover it. Proceed with caution.
        ### QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteSmsSignRequest
        @return: DeleteSmsSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_sms_sign_with_options_async(request, runtime)

    def delete_sms_template_with_options(
        self,
        request: dysmsapi_20170525_models.DeleteSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.DeleteSmsTemplateResponse:
        """
        @summary Deletes a message template.
        
        @description    Message templates pending approval can be withdrawn. You can delete a message template pending approval on the Message Templates tab in the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview).
        Message templates that have been approved can be deleted, and cannot be modified. You can delete a message template pending approval on the Message Templates tab in the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview).
        You cannot recover deleted message templates. Proceed with caution.
        ### QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteSmsTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSmsTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.DeleteSmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sms_template_with_options_async(
        self,
        request: dysmsapi_20170525_models.DeleteSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.DeleteSmsTemplateResponse:
        """
        @summary Deletes a message template.
        
        @description    Message templates pending approval can be withdrawn. You can delete a message template pending approval on the Message Templates tab in the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview).
        Message templates that have been approved can be deleted, and cannot be modified. You can delete a message template pending approval on the Message Templates tab in the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview).
        You cannot recover deleted message templates. Proceed with caution.
        ### QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteSmsTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSmsTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.DeleteSmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sms_template(
        self,
        request: dysmsapi_20170525_models.DeleteSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.DeleteSmsTemplateResponse:
        """
        @summary Deletes a message template.
        
        @description    Message templates pending approval can be withdrawn. You can delete a message template pending approval on the Message Templates tab in the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview).
        Message templates that have been approved can be deleted, and cannot be modified. You can delete a message template pending approval on the Message Templates tab in the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview).
        You cannot recover deleted message templates. Proceed with caution.
        ### QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteSmsTemplateRequest
        @return: DeleteSmsTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_sms_template_with_options(request, runtime)

    async def delete_sms_template_async(
        self,
        request: dysmsapi_20170525_models.DeleteSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.DeleteSmsTemplateResponse:
        """
        @summary Deletes a message template.
        
        @description    Message templates pending approval can be withdrawn. You can delete a message template pending approval on the Message Templates tab in the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview).
        Message templates that have been approved can be deleted, and cannot be modified. You can delete a message template pending approval on the Message Templates tab in the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview).
        You cannot recover deleted message templates. Proceed with caution.
        ### QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteSmsTemplateRequest
        @return: DeleteSmsTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_sms_template_with_options_async(request, runtime)

    def get_card_sms_details_with_options(
        self,
        request: dysmsapi_20170525_models.GetCardSmsDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.GetCardSmsDetailsResponse:
        """
        @summary Query card sending details
        
        @param request: GetCardSmsDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCardSmsDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_card_id):
            query['BizCardId'] = request.biz_card_id
        if not UtilClient.is_unset(request.biz_digit_id):
            query['BizDigitId'] = request.biz_digit_id
        if not UtilClient.is_unset(request.biz_sms_id):
            query['BizSmsId'] = request.biz_sms_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_date):
            query['SendDate'] = request.send_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCardSmsDetails',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.GetCardSmsDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_card_sms_details_with_options_async(
        self,
        request: dysmsapi_20170525_models.GetCardSmsDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.GetCardSmsDetailsResponse:
        """
        @summary Query card sending details
        
        @param request: GetCardSmsDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCardSmsDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_card_id):
            query['BizCardId'] = request.biz_card_id
        if not UtilClient.is_unset(request.biz_digit_id):
            query['BizDigitId'] = request.biz_digit_id
        if not UtilClient.is_unset(request.biz_sms_id):
            query['BizSmsId'] = request.biz_sms_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_date):
            query['SendDate'] = request.send_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCardSmsDetails',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.GetCardSmsDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_card_sms_details(
        self,
        request: dysmsapi_20170525_models.GetCardSmsDetailsRequest,
    ) -> dysmsapi_20170525_models.GetCardSmsDetailsResponse:
        """
        @summary Query card sending details
        
        @param request: GetCardSmsDetailsRequest
        @return: GetCardSmsDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_card_sms_details_with_options(request, runtime)

    async def get_card_sms_details_async(
        self,
        request: dysmsapi_20170525_models.GetCardSmsDetailsRequest,
    ) -> dysmsapi_20170525_models.GetCardSmsDetailsResponse:
        """
        @summary Query card sending details
        
        @param request: GetCardSmsDetailsRequest
        @return: GetCardSmsDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_card_sms_details_with_options_async(request, runtime)

    def get_card_sms_link_with_options(
        self,
        request: dysmsapi_20170525_models.GetCardSmsLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.GetCardSmsLinkResponse:
        """
        @summary Queries the short URLs of a card messages template.
        
        @description ### QPS limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetCardSmsLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCardSmsLinkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.card_code_type):
            query['CardCodeType'] = request.card_code_type
        if not UtilClient.is_unset(request.card_link_type):
            query['CardLinkType'] = request.card_link_type
        if not UtilClient.is_unset(request.card_template_code):
            query['CardTemplateCode'] = request.card_template_code
        if not UtilClient.is_unset(request.card_template_param_json):
            query['CardTemplateParamJson'] = request.card_template_param_json
        if not UtilClient.is_unset(request.custom_short_code_json):
            query['CustomShortCodeJson'] = request.custom_short_code_json
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.phone_number_json):
            query['PhoneNumberJson'] = request.phone_number_json
        if not UtilClient.is_unset(request.sign_name_json):
            query['SignNameJson'] = request.sign_name_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCardSmsLink',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.GetCardSmsLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_card_sms_link_with_options_async(
        self,
        request: dysmsapi_20170525_models.GetCardSmsLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.GetCardSmsLinkResponse:
        """
        @summary Queries the short URLs of a card messages template.
        
        @description ### QPS limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetCardSmsLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCardSmsLinkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.card_code_type):
            query['CardCodeType'] = request.card_code_type
        if not UtilClient.is_unset(request.card_link_type):
            query['CardLinkType'] = request.card_link_type
        if not UtilClient.is_unset(request.card_template_code):
            query['CardTemplateCode'] = request.card_template_code
        if not UtilClient.is_unset(request.card_template_param_json):
            query['CardTemplateParamJson'] = request.card_template_param_json
        if not UtilClient.is_unset(request.custom_short_code_json):
            query['CustomShortCodeJson'] = request.custom_short_code_json
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.phone_number_json):
            query['PhoneNumberJson'] = request.phone_number_json
        if not UtilClient.is_unset(request.sign_name_json):
            query['SignNameJson'] = request.sign_name_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCardSmsLink',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.GetCardSmsLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_card_sms_link(
        self,
        request: dysmsapi_20170525_models.GetCardSmsLinkRequest,
    ) -> dysmsapi_20170525_models.GetCardSmsLinkResponse:
        """
        @summary Queries the short URLs of a card messages template.
        
        @description ### QPS limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetCardSmsLinkRequest
        @return: GetCardSmsLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_card_sms_link_with_options(request, runtime)

    async def get_card_sms_link_async(
        self,
        request: dysmsapi_20170525_models.GetCardSmsLinkRequest,
    ) -> dysmsapi_20170525_models.GetCardSmsLinkResponse:
        """
        @summary Queries the short URLs of a card messages template.
        
        @description ### QPS limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetCardSmsLinkRequest
        @return: GetCardSmsLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_card_sms_link_with_options_async(request, runtime)

    def get_media_resource_id_with_options(
        self,
        request: dysmsapi_20170525_models.GetMediaResourceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.GetMediaResourceIdResponse:
        """
        @summary Converts a resource uploaded to the specified Object Storage Service (OSS) bucket for unified management. Then, a resource ID is returned. You can manage the resource based on the ID.
        
        @description ### QPS limit
        You can call this operation up to 300 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetMediaResourceIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMediaResourceIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extend_info):
            query['ExtendInfo'] = request.extend_info
        if not UtilClient.is_unset(request.file_size):
            query['FileSize'] = request.file_size
        if not UtilClient.is_unset(request.memo):
            query['Memo'] = request.memo
        if not UtilClient.is_unset(request.oss_key):
            query['OssKey'] = request.oss_key
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMediaResourceId',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.GetMediaResourceIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_media_resource_id_with_options_async(
        self,
        request: dysmsapi_20170525_models.GetMediaResourceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.GetMediaResourceIdResponse:
        """
        @summary Converts a resource uploaded to the specified Object Storage Service (OSS) bucket for unified management. Then, a resource ID is returned. You can manage the resource based on the ID.
        
        @description ### QPS limit
        You can call this operation up to 300 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetMediaResourceIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMediaResourceIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extend_info):
            query['ExtendInfo'] = request.extend_info
        if not UtilClient.is_unset(request.file_size):
            query['FileSize'] = request.file_size
        if not UtilClient.is_unset(request.memo):
            query['Memo'] = request.memo
        if not UtilClient.is_unset(request.oss_key):
            query['OssKey'] = request.oss_key
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMediaResourceId',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.GetMediaResourceIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_media_resource_id(
        self,
        request: dysmsapi_20170525_models.GetMediaResourceIdRequest,
    ) -> dysmsapi_20170525_models.GetMediaResourceIdResponse:
        """
        @summary Converts a resource uploaded to the specified Object Storage Service (OSS) bucket for unified management. Then, a resource ID is returned. You can manage the resource based on the ID.
        
        @description ### QPS limit
        You can call this operation up to 300 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetMediaResourceIdRequest
        @return: GetMediaResourceIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_media_resource_id_with_options(request, runtime)

    async def get_media_resource_id_async(
        self,
        request: dysmsapi_20170525_models.GetMediaResourceIdRequest,
    ) -> dysmsapi_20170525_models.GetMediaResourceIdResponse:
        """
        @summary Converts a resource uploaded to the specified Object Storage Service (OSS) bucket for unified management. Then, a resource ID is returned. You can manage the resource based on the ID.
        
        @description ### QPS limit
        You can call this operation up to 300 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetMediaResourceIdRequest
        @return: GetMediaResourceIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_media_resource_id_with_options_async(request, runtime)

    def get_ossinfo_for_card_template_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.GetOSSInfoForCardTemplateResponse:
        """
        @summary Queries the OSS configuration information about card messages.
        
        @description Resources such as images and videos used for card message templates can be uploaded to Object Storage Service (OSS) buckets for storage. For more information, see [Upload files to OSS](https://help.aliyun.com/document_detail/437303.html).
        ### QPS limit
        You can call this operation up to 300 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetOSSInfoForCardTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOSSInfoForCardTemplateResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetOSSInfoForCardTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.GetOSSInfoForCardTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ossinfo_for_card_template_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.GetOSSInfoForCardTemplateResponse:
        """
        @summary Queries the OSS configuration information about card messages.
        
        @description Resources such as images and videos used for card message templates can be uploaded to Object Storage Service (OSS) buckets for storage. For more information, see [Upload files to OSS](https://help.aliyun.com/document_detail/437303.html).
        ### QPS limit
        You can call this operation up to 300 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetOSSInfoForCardTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOSSInfoForCardTemplateResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetOSSInfoForCardTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.GetOSSInfoForCardTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ossinfo_for_card_template(self) -> dysmsapi_20170525_models.GetOSSInfoForCardTemplateResponse:
        """
        @summary Queries the OSS configuration information about card messages.
        
        @description Resources such as images and videos used for card message templates can be uploaded to Object Storage Service (OSS) buckets for storage. For more information, see [Upload files to OSS](https://help.aliyun.com/document_detail/437303.html).
        ### QPS limit
        You can call this operation up to 300 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @return: GetOSSInfoForCardTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ossinfo_for_card_template_with_options(runtime)

    async def get_ossinfo_for_card_template_async(self) -> dysmsapi_20170525_models.GetOSSInfoForCardTemplateResponse:
        """
        @summary Queries the OSS configuration information about card messages.
        
        @description Resources such as images and videos used for card message templates can be uploaded to Object Storage Service (OSS) buckets for storage. For more information, see [Upload files to OSS](https://help.aliyun.com/document_detail/437303.html).
        ### QPS limit
        You can call this operation up to 300 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @return: GetOSSInfoForCardTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ossinfo_for_card_template_with_options_async(runtime)

    def get_ossinfo_for_upload_file_with_options(
        self,
        request: dysmsapi_20170525_models.GetOSSInfoForUploadFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.GetOSSInfoForUploadFileResponse:
        """
        @summary SMS File Upload, Get Authorization Info
        
        @description - When creating signatures or templates, you can upload materials such as login pages with links, backend page screenshots, software copyrights, supplementary agreements, etc. This helps the review personnel understand your business details. If there are multiple materials, they can be combined into one file, supporting png, jpg, jpeg, doc, docx, pdf formats.
        - For additional materials needed when creating signatures or templates, you can upload them to the OSS file system for storage. For file upload operations, refer to [OSS File Upload](https://help.aliyun.com/zh/sms/upload-files-through-oss).
        
        @param request: GetOSSInfoForUploadFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOSSInfoForUploadFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOSSInfoForUploadFile',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.GetOSSInfoForUploadFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ossinfo_for_upload_file_with_options_async(
        self,
        request: dysmsapi_20170525_models.GetOSSInfoForUploadFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.GetOSSInfoForUploadFileResponse:
        """
        @summary SMS File Upload, Get Authorization Info
        
        @description - When creating signatures or templates, you can upload materials such as login pages with links, backend page screenshots, software copyrights, supplementary agreements, etc. This helps the review personnel understand your business details. If there are multiple materials, they can be combined into one file, supporting png, jpg, jpeg, doc, docx, pdf formats.
        - For additional materials needed when creating signatures or templates, you can upload them to the OSS file system for storage. For file upload operations, refer to [OSS File Upload](https://help.aliyun.com/zh/sms/upload-files-through-oss).
        
        @param request: GetOSSInfoForUploadFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOSSInfoForUploadFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOSSInfoForUploadFile',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.GetOSSInfoForUploadFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ossinfo_for_upload_file(
        self,
        request: dysmsapi_20170525_models.GetOSSInfoForUploadFileRequest,
    ) -> dysmsapi_20170525_models.GetOSSInfoForUploadFileResponse:
        """
        @summary SMS File Upload, Get Authorization Info
        
        @description - When creating signatures or templates, you can upload materials such as login pages with links, backend page screenshots, software copyrights, supplementary agreements, etc. This helps the review personnel understand your business details. If there are multiple materials, they can be combined into one file, supporting png, jpg, jpeg, doc, docx, pdf formats.
        - For additional materials needed when creating signatures or templates, you can upload them to the OSS file system for storage. For file upload operations, refer to [OSS File Upload](https://help.aliyun.com/zh/sms/upload-files-through-oss).
        
        @param request: GetOSSInfoForUploadFileRequest
        @return: GetOSSInfoForUploadFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ossinfo_for_upload_file_with_options(request, runtime)

    async def get_ossinfo_for_upload_file_async(
        self,
        request: dysmsapi_20170525_models.GetOSSInfoForUploadFileRequest,
    ) -> dysmsapi_20170525_models.GetOSSInfoForUploadFileResponse:
        """
        @summary SMS File Upload, Get Authorization Info
        
        @description - When creating signatures or templates, you can upload materials such as login pages with links, backend page screenshots, software copyrights, supplementary agreements, etc. This helps the review personnel understand your business details. If there are multiple materials, they can be combined into one file, supporting png, jpg, jpeg, doc, docx, pdf formats.
        - For additional materials needed when creating signatures or templates, you can upload them to the OSS file system for storage. For file upload operations, refer to [OSS File Upload](https://help.aliyun.com/zh/sms/upload-files-through-oss).
        
        @param request: GetOSSInfoForUploadFileRequest
        @return: GetOSSInfoForUploadFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ossinfo_for_upload_file_with_options_async(request, runtime)

    def get_qualification_oss_info_with_options(
        self,
        request: dysmsapi_20170525_models.GetQualificationOssInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.GetQualificationOssInfoResponse:
        """
        @summary 上传文件获取oss配置
        
        @param request: GetQualificationOssInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQualificationOssInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQualificationOssInfo',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.GetQualificationOssInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_qualification_oss_info_with_options_async(
        self,
        request: dysmsapi_20170525_models.GetQualificationOssInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.GetQualificationOssInfoResponse:
        """
        @summary 上传文件获取oss配置
        
        @param request: GetQualificationOssInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQualificationOssInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQualificationOssInfo',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.GetQualificationOssInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_qualification_oss_info(
        self,
        request: dysmsapi_20170525_models.GetQualificationOssInfoRequest,
    ) -> dysmsapi_20170525_models.GetQualificationOssInfoResponse:
        """
        @summary 上传文件获取oss配置
        
        @param request: GetQualificationOssInfoRequest
        @return: GetQualificationOssInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_qualification_oss_info_with_options(request, runtime)

    async def get_qualification_oss_info_async(
        self,
        request: dysmsapi_20170525_models.GetQualificationOssInfoRequest,
    ) -> dysmsapi_20170525_models.GetQualificationOssInfoResponse:
        """
        @summary 上传文件获取oss配置
        
        @param request: GetQualificationOssInfoRequest
        @return: GetQualificationOssInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_qualification_oss_info_with_options_async(request, runtime)

    def get_sms_ocr_oss_info_with_options(
        self,
        request: dysmsapi_20170525_models.GetSmsOcrOssInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.GetSmsOcrOssInfoResponse:
        """
        @summary 获取OCR的OSS信息
        
        @param request: GetSmsOcrOssInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSmsOcrOssInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSmsOcrOssInfo',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.GetSmsOcrOssInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sms_ocr_oss_info_with_options_async(
        self,
        request: dysmsapi_20170525_models.GetSmsOcrOssInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.GetSmsOcrOssInfoResponse:
        """
        @summary 获取OCR的OSS信息
        
        @param request: GetSmsOcrOssInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSmsOcrOssInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSmsOcrOssInfo',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.GetSmsOcrOssInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sms_ocr_oss_info(
        self,
        request: dysmsapi_20170525_models.GetSmsOcrOssInfoRequest,
    ) -> dysmsapi_20170525_models.GetSmsOcrOssInfoResponse:
        """
        @summary 获取OCR的OSS信息
        
        @param request: GetSmsOcrOssInfoRequest
        @return: GetSmsOcrOssInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_sms_ocr_oss_info_with_options(request, runtime)

    async def get_sms_ocr_oss_info_async(
        self,
        request: dysmsapi_20170525_models.GetSmsOcrOssInfoRequest,
    ) -> dysmsapi_20170525_models.GetSmsOcrOssInfoResponse:
        """
        @summary 获取OCR的OSS信息
        
        @param request: GetSmsOcrOssInfoRequest
        @return: GetSmsOcrOssInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_sms_ocr_oss_info_with_options_async(request, runtime)

    def get_sms_sign_with_options(
        self,
        request: dysmsapi_20170525_models.GetSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.GetSmsSignResponse:
        """
        @summary Query SMS Signature Details
        
        @description - For details about the changes of this new interface and the original one, please refer to [Announcement on the Update of SMS Signature & Template Interfaces](https://help.aliyun.com/zh/sms/product-overview/announcement-on-sms-service-update-signature-template-interface).
        - Review Time: Generally, after submitting the signature, Alibaba Cloud expects to complete the review within 2 hours (Review Business Hours: Monday to Sunday 9:00~21:00, with legal holidays postponed). It is recommended to submit your application before 18:00.
        - If the signature fails the review, the reason for the failure will be returned. Please refer to [Handling Suggestions for Failed SMS Reviews](https://help.aliyun.com/zh/sms/user-guide/causes-of-application-failures-and-suggestions?spm), invoke the [UpdateSmsSign](https://help.aliyun.com/zh/sms/developer-reference/api-dysmsapi-2017-05-25-updatesmssign?spm) API, or modify the unapproved SMS signature on the [Signature Management](https://dysms.console.aliyun.com/domestic/text/sign) page.
        
        @param request: GetSmsSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSmsSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSmsSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.GetSmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sms_sign_with_options_async(
        self,
        request: dysmsapi_20170525_models.GetSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.GetSmsSignResponse:
        """
        @summary Query SMS Signature Details
        
        @description - For details about the changes of this new interface and the original one, please refer to [Announcement on the Update of SMS Signature & Template Interfaces](https://help.aliyun.com/zh/sms/product-overview/announcement-on-sms-service-update-signature-template-interface).
        - Review Time: Generally, after submitting the signature, Alibaba Cloud expects to complete the review within 2 hours (Review Business Hours: Monday to Sunday 9:00~21:00, with legal holidays postponed). It is recommended to submit your application before 18:00.
        - If the signature fails the review, the reason for the failure will be returned. Please refer to [Handling Suggestions for Failed SMS Reviews](https://help.aliyun.com/zh/sms/user-guide/causes-of-application-failures-and-suggestions?spm), invoke the [UpdateSmsSign](https://help.aliyun.com/zh/sms/developer-reference/api-dysmsapi-2017-05-25-updatesmssign?spm) API, or modify the unapproved SMS signature on the [Signature Management](https://dysms.console.aliyun.com/domestic/text/sign) page.
        
        @param request: GetSmsSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSmsSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSmsSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.GetSmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sms_sign(
        self,
        request: dysmsapi_20170525_models.GetSmsSignRequest,
    ) -> dysmsapi_20170525_models.GetSmsSignResponse:
        """
        @summary Query SMS Signature Details
        
        @description - For details about the changes of this new interface and the original one, please refer to [Announcement on the Update of SMS Signature & Template Interfaces](https://help.aliyun.com/zh/sms/product-overview/announcement-on-sms-service-update-signature-template-interface).
        - Review Time: Generally, after submitting the signature, Alibaba Cloud expects to complete the review within 2 hours (Review Business Hours: Monday to Sunday 9:00~21:00, with legal holidays postponed). It is recommended to submit your application before 18:00.
        - If the signature fails the review, the reason for the failure will be returned. Please refer to [Handling Suggestions for Failed SMS Reviews](https://help.aliyun.com/zh/sms/user-guide/causes-of-application-failures-and-suggestions?spm), invoke the [UpdateSmsSign](https://help.aliyun.com/zh/sms/developer-reference/api-dysmsapi-2017-05-25-updatesmssign?spm) API, or modify the unapproved SMS signature on the [Signature Management](https://dysms.console.aliyun.com/domestic/text/sign) page.
        
        @param request: GetSmsSignRequest
        @return: GetSmsSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_sms_sign_with_options(request, runtime)

    async def get_sms_sign_async(
        self,
        request: dysmsapi_20170525_models.GetSmsSignRequest,
    ) -> dysmsapi_20170525_models.GetSmsSignResponse:
        """
        @summary Query SMS Signature Details
        
        @description - For details about the changes of this new interface and the original one, please refer to [Announcement on the Update of SMS Signature & Template Interfaces](https://help.aliyun.com/zh/sms/product-overview/announcement-on-sms-service-update-signature-template-interface).
        - Review Time: Generally, after submitting the signature, Alibaba Cloud expects to complete the review within 2 hours (Review Business Hours: Monday to Sunday 9:00~21:00, with legal holidays postponed). It is recommended to submit your application before 18:00.
        - If the signature fails the review, the reason for the failure will be returned. Please refer to [Handling Suggestions for Failed SMS Reviews](https://help.aliyun.com/zh/sms/user-guide/causes-of-application-failures-and-suggestions?spm), invoke the [UpdateSmsSign](https://help.aliyun.com/zh/sms/developer-reference/api-dysmsapi-2017-05-25-updatesmssign?spm) API, or modify the unapproved SMS signature on the [Signature Management](https://dysms.console.aliyun.com/domestic/text/sign) page.
        
        @param request: GetSmsSignRequest
        @return: GetSmsSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_sms_sign_with_options_async(request, runtime)

    def get_sms_template_with_options(
        self,
        request: dysmsapi_20170525_models.GetSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.GetSmsTemplateResponse:
        """
        @summary Query Text SMS Template Details
        
        @description - For details about the announcement of changes to the new and original interfaces, see [Announcement on Updates to SMS Service Signature & Template Interfaces](https://help.aliyun.com/zh/sms/product-overview/announcement-on-sms-service-update-signature-template-interface).
        - Review Time: Under normal circumstances, Alibaba Cloud expects to complete the review within 2 hours after template submission (review working hours: Monday to Sunday 9:00~21:00, with statutory holidays postponed). It is recommended to submit your application before 18:00.
        - If the template fails the review, the reason for the failure will be returned. Please refer to [Handling Suggestions for Failed SMS Reviews](https://help.aliyun.com/zh/sms/user-guide/causes-of-application-failures-and-suggestions?spm=a2c4g.11186623.0.0.41fd339f3bPSCQ), invoke the [ModifySmsTemplate](https://help.aliyun.com/zh/sms/developer-reference/api-dysmsapi-2017-05-25-modifysmstemplate?spm=a2c4g.11186623.0.0.5b1f6e8bQloFit) API or modify the SMS template on the [Template Management](https://dysms.console.aliyun.com/domestic/text/template) page.
        - The current QuerySmsTemplate interface queries the audit details of a single template by template code. The [QuerySmsTemplateList](https://help.aliyun.com/zh/sms/developer-reference/api-dysmsapi-2017-05-25-querysmstemplatelist?spm=a2c4g.11186623.0.0.24086e8bO8cFn4) interface can query the template details of all templates under your current account.
        
        @param request: GetSmsTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSmsTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.GetSmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sms_template_with_options_async(
        self,
        request: dysmsapi_20170525_models.GetSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.GetSmsTemplateResponse:
        """
        @summary Query Text SMS Template Details
        
        @description - For details about the announcement of changes to the new and original interfaces, see [Announcement on Updates to SMS Service Signature & Template Interfaces](https://help.aliyun.com/zh/sms/product-overview/announcement-on-sms-service-update-signature-template-interface).
        - Review Time: Under normal circumstances, Alibaba Cloud expects to complete the review within 2 hours after template submission (review working hours: Monday to Sunday 9:00~21:00, with statutory holidays postponed). It is recommended to submit your application before 18:00.
        - If the template fails the review, the reason for the failure will be returned. Please refer to [Handling Suggestions for Failed SMS Reviews](https://help.aliyun.com/zh/sms/user-guide/causes-of-application-failures-and-suggestions?spm=a2c4g.11186623.0.0.41fd339f3bPSCQ), invoke the [ModifySmsTemplate](https://help.aliyun.com/zh/sms/developer-reference/api-dysmsapi-2017-05-25-modifysmstemplate?spm=a2c4g.11186623.0.0.5b1f6e8bQloFit) API or modify the SMS template on the [Template Management](https://dysms.console.aliyun.com/domestic/text/template) page.
        - The current QuerySmsTemplate interface queries the audit details of a single template by template code. The [QuerySmsTemplateList](https://help.aliyun.com/zh/sms/developer-reference/api-dysmsapi-2017-05-25-querysmstemplatelist?spm=a2c4g.11186623.0.0.24086e8bO8cFn4) interface can query the template details of all templates under your current account.
        
        @param request: GetSmsTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSmsTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.GetSmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sms_template(
        self,
        request: dysmsapi_20170525_models.GetSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.GetSmsTemplateResponse:
        """
        @summary Query Text SMS Template Details
        
        @description - For details about the announcement of changes to the new and original interfaces, see [Announcement on Updates to SMS Service Signature & Template Interfaces](https://help.aliyun.com/zh/sms/product-overview/announcement-on-sms-service-update-signature-template-interface).
        - Review Time: Under normal circumstances, Alibaba Cloud expects to complete the review within 2 hours after template submission (review working hours: Monday to Sunday 9:00~21:00, with statutory holidays postponed). It is recommended to submit your application before 18:00.
        - If the template fails the review, the reason for the failure will be returned. Please refer to [Handling Suggestions for Failed SMS Reviews](https://help.aliyun.com/zh/sms/user-guide/causes-of-application-failures-and-suggestions?spm=a2c4g.11186623.0.0.41fd339f3bPSCQ), invoke the [ModifySmsTemplate](https://help.aliyun.com/zh/sms/developer-reference/api-dysmsapi-2017-05-25-modifysmstemplate?spm=a2c4g.11186623.0.0.5b1f6e8bQloFit) API or modify the SMS template on the [Template Management](https://dysms.console.aliyun.com/domestic/text/template) page.
        - The current QuerySmsTemplate interface queries the audit details of a single template by template code. The [QuerySmsTemplateList](https://help.aliyun.com/zh/sms/developer-reference/api-dysmsapi-2017-05-25-querysmstemplatelist?spm=a2c4g.11186623.0.0.24086e8bO8cFn4) interface can query the template details of all templates under your current account.
        
        @param request: GetSmsTemplateRequest
        @return: GetSmsTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_sms_template_with_options(request, runtime)

    async def get_sms_template_async(
        self,
        request: dysmsapi_20170525_models.GetSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.GetSmsTemplateResponse:
        """
        @summary Query Text SMS Template Details
        
        @description - For details about the announcement of changes to the new and original interfaces, see [Announcement on Updates to SMS Service Signature & Template Interfaces](https://help.aliyun.com/zh/sms/product-overview/announcement-on-sms-service-update-signature-template-interface).
        - Review Time: Under normal circumstances, Alibaba Cloud expects to complete the review within 2 hours after template submission (review working hours: Monday to Sunday 9:00~21:00, with statutory holidays postponed). It is recommended to submit your application before 18:00.
        - If the template fails the review, the reason for the failure will be returned. Please refer to [Handling Suggestions for Failed SMS Reviews](https://help.aliyun.com/zh/sms/user-guide/causes-of-application-failures-and-suggestions?spm=a2c4g.11186623.0.0.41fd339f3bPSCQ), invoke the [ModifySmsTemplate](https://help.aliyun.com/zh/sms/developer-reference/api-dysmsapi-2017-05-25-modifysmstemplate?spm=a2c4g.11186623.0.0.5b1f6e8bQloFit) API or modify the SMS template on the [Template Management](https://dysms.console.aliyun.com/domestic/text/template) page.
        - The current QuerySmsTemplate interface queries the audit details of a single template by template code. The [QuerySmsTemplateList](https://help.aliyun.com/zh/sms/developer-reference/api-dysmsapi-2017-05-25-querysmstemplatelist?spm=a2c4g.11186623.0.0.24086e8bO8cFn4) interface can query the template details of all templates under your current account.
        
        @param request: GetSmsTemplateRequest
        @return: GetSmsTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_sms_template_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: dysmsapi_20170525_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of a message template.
        
        @description ### QPS limit
        You can call this operation up to 50 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: dysmsapi_20170525_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of a message template.
        
        @description ### QPS limit
        You can call this operation up to 50 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: dysmsapi_20170525_models.ListTagResourcesRequest,
    ) -> dysmsapi_20170525_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of a message template.
        
        @description ### QPS limit
        You can call this operation up to 50 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: dysmsapi_20170525_models.ListTagResourcesRequest,
    ) -> dysmsapi_20170525_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of a message template.
        
        @description ### QPS limit
        You can call this operation up to 50 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_sms_sign_with_options(
        self,
        request: dysmsapi_20170525_models.ModifySmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.ModifySmsSignResponse:
        """
        @summary Modifies a rejected signature and submit it for approval. Signatures that are pending approval or have been approved cannot be modified.
        
        @description You can call the operation or use the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview) to modify an existing signature and submit the signature for approval. The signature must comply with the [signature specifications](https://help.aliyun.com/document_detail/108076.html).
        For more information, see [Usage notes](https://help.aliyun.com/document_detail/55324.html).
        ### QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        >
        Signatures pending approval cannot be modified.
        You cannot modify a signature after it is approved. If you no longer need the signature, you can delete it.
        If you are an individual user, you cannot apply for a new signature on the same day that your signature is rejected or deleted. We recommend that you modify the rejected signature and submit it again.
        
        @param request: ModifySmsSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySmsSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sign_source):
            query['SignSource'] = request.sign_source
        if not UtilClient.is_unset(request.sign_type):
            query['SignType'] = request.sign_type
        body = {}
        if not UtilClient.is_unset(request.sign_file_list):
            body['SignFileList'] = request.sign_file_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifySmsSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.ModifySmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sms_sign_with_options_async(
        self,
        request: dysmsapi_20170525_models.ModifySmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.ModifySmsSignResponse:
        """
        @summary Modifies a rejected signature and submit it for approval. Signatures that are pending approval or have been approved cannot be modified.
        
        @description You can call the operation or use the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview) to modify an existing signature and submit the signature for approval. The signature must comply with the [signature specifications](https://help.aliyun.com/document_detail/108076.html).
        For more information, see [Usage notes](https://help.aliyun.com/document_detail/55324.html).
        ### QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        >
        Signatures pending approval cannot be modified.
        You cannot modify a signature after it is approved. If you no longer need the signature, you can delete it.
        If you are an individual user, you cannot apply for a new signature on the same day that your signature is rejected or deleted. We recommend that you modify the rejected signature and submit it again.
        
        @param request: ModifySmsSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySmsSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sign_source):
            query['SignSource'] = request.sign_source
        if not UtilClient.is_unset(request.sign_type):
            query['SignType'] = request.sign_type
        body = {}
        if not UtilClient.is_unset(request.sign_file_list):
            body['SignFileList'] = request.sign_file_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifySmsSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.ModifySmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sms_sign(
        self,
        request: dysmsapi_20170525_models.ModifySmsSignRequest,
    ) -> dysmsapi_20170525_models.ModifySmsSignResponse:
        """
        @summary Modifies a rejected signature and submit it for approval. Signatures that are pending approval or have been approved cannot be modified.
        
        @description You can call the operation or use the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview) to modify an existing signature and submit the signature for approval. The signature must comply with the [signature specifications](https://help.aliyun.com/document_detail/108076.html).
        For more information, see [Usage notes](https://help.aliyun.com/document_detail/55324.html).
        ### QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        >
        Signatures pending approval cannot be modified.
        You cannot modify a signature after it is approved. If you no longer need the signature, you can delete it.
        If you are an individual user, you cannot apply for a new signature on the same day that your signature is rejected or deleted. We recommend that you modify the rejected signature and submit it again.
        
        @param request: ModifySmsSignRequest
        @return: ModifySmsSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_sms_sign_with_options(request, runtime)

    async def modify_sms_sign_async(
        self,
        request: dysmsapi_20170525_models.ModifySmsSignRequest,
    ) -> dysmsapi_20170525_models.ModifySmsSignResponse:
        """
        @summary Modifies a rejected signature and submit it for approval. Signatures that are pending approval or have been approved cannot be modified.
        
        @description You can call the operation or use the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm#/overview) to modify an existing signature and submit the signature for approval. The signature must comply with the [signature specifications](https://help.aliyun.com/document_detail/108076.html).
        For more information, see [Usage notes](https://help.aliyun.com/document_detail/55324.html).
        ### QPS limits
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        >
        Signatures pending approval cannot be modified.
        You cannot modify a signature after it is approved. If you no longer need the signature, you can delete it.
        If you are an individual user, you cannot apply for a new signature on the same day that your signature is rejected or deleted. We recommend that you modify the rejected signature and submit it again.
        
        @param request: ModifySmsSignRequest
        @return: ModifySmsSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_sms_sign_with_options_async(request, runtime)

    def modify_sms_template_with_options(
        self,
        request: dysmsapi_20170525_models.ModifySmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.ModifySmsTemplateResponse:
        """
        @deprecated OpenAPI ModifySmsTemplate is deprecated, please use Dysmsapi::2017-05-25::UpdateSmsTemplate instead.
        
        @summary Modifies the information of an unapproved message template and submits it for review again.
        
        @description After you apply for a message template, if the template fails to pass the review, you can call this operation to modify the template and submit the template again. You can call this operation to modify only a template for a specific message type.
        The template content must comply with the [SMS template specifications](https://help.aliyun.com/document_detail/108253.html).
        For more information, see [Usage notes](https://help.aliyun.com/document_detail/55324.html).
        ### QPS limit
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifySmsTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySmsTemplateResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_content):
            query['TemplateContent'] = request.template_content
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.ModifySmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sms_template_with_options_async(
        self,
        request: dysmsapi_20170525_models.ModifySmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.ModifySmsTemplateResponse:
        """
        @deprecated OpenAPI ModifySmsTemplate is deprecated, please use Dysmsapi::2017-05-25::UpdateSmsTemplate instead.
        
        @summary Modifies the information of an unapproved message template and submits it for review again.
        
        @description After you apply for a message template, if the template fails to pass the review, you can call this operation to modify the template and submit the template again. You can call this operation to modify only a template for a specific message type.
        The template content must comply with the [SMS template specifications](https://help.aliyun.com/document_detail/108253.html).
        For more information, see [Usage notes](https://help.aliyun.com/document_detail/55324.html).
        ### QPS limit
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifySmsTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySmsTemplateResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_content):
            query['TemplateContent'] = request.template_content
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.ModifySmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sms_template(
        self,
        request: dysmsapi_20170525_models.ModifySmsTemplateRequest,
    ) -> dysmsapi_20170525_models.ModifySmsTemplateResponse:
        """
        @deprecated OpenAPI ModifySmsTemplate is deprecated, please use Dysmsapi::2017-05-25::UpdateSmsTemplate instead.
        
        @summary Modifies the information of an unapproved message template and submits it for review again.
        
        @description After you apply for a message template, if the template fails to pass the review, you can call this operation to modify the template and submit the template again. You can call this operation to modify only a template for a specific message type.
        The template content must comply with the [SMS template specifications](https://help.aliyun.com/document_detail/108253.html).
        For more information, see [Usage notes](https://help.aliyun.com/document_detail/55324.html).
        ### QPS limit
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifySmsTemplateRequest
        @return: ModifySmsTemplateResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_sms_template_with_options(request, runtime)

    async def modify_sms_template_async(
        self,
        request: dysmsapi_20170525_models.ModifySmsTemplateRequest,
    ) -> dysmsapi_20170525_models.ModifySmsTemplateResponse:
        """
        @deprecated OpenAPI ModifySmsTemplate is deprecated, please use Dysmsapi::2017-05-25::UpdateSmsTemplate instead.
        
        @summary Modifies the information of an unapproved message template and submits it for review again.
        
        @description After you apply for a message template, if the template fails to pass the review, you can call this operation to modify the template and submit the template again. You can call this operation to modify only a template for a specific message type.
        The template content must comply with the [SMS template specifications](https://help.aliyun.com/document_detail/108253.html).
        For more information, see [Usage notes](https://help.aliyun.com/document_detail/55324.html).
        ### QPS limit
        You can call this operation up to 1,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifySmsTemplateRequest
        @return: ModifySmsTemplateResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_sms_template_with_options_async(request, runtime)

    def query_card_sms_template_with_options(
        self,
        request: dysmsapi_20170525_models.QueryCardSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QueryCardSmsTemplateResponse:
        """
        @summary Queries the review status of a message template.
        
        @description ### QPS limit
        You can call this operation up to 300 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryCardSmsTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCardSmsTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCardSmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QueryCardSmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_card_sms_template_with_options_async(
        self,
        request: dysmsapi_20170525_models.QueryCardSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QueryCardSmsTemplateResponse:
        """
        @summary Queries the review status of a message template.
        
        @description ### QPS limit
        You can call this operation up to 300 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryCardSmsTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCardSmsTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCardSmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QueryCardSmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_card_sms_template(
        self,
        request: dysmsapi_20170525_models.QueryCardSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.QueryCardSmsTemplateResponse:
        """
        @summary Queries the review status of a message template.
        
        @description ### QPS limit
        You can call this operation up to 300 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryCardSmsTemplateRequest
        @return: QueryCardSmsTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_card_sms_template_with_options(request, runtime)

    async def query_card_sms_template_async(
        self,
        request: dysmsapi_20170525_models.QueryCardSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.QueryCardSmsTemplateResponse:
        """
        @summary Queries the review status of a message template.
        
        @description ### QPS limit
        You can call this operation up to 300 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryCardSmsTemplateRequest
        @return: QueryCardSmsTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_card_sms_template_with_options_async(request, runtime)

    def query_card_sms_template_report_with_options(
        self,
        request: dysmsapi_20170525_models.QueryCardSmsTemplateReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QueryCardSmsTemplateReportResponse:
        """
        @summary Queries sent card messages.
        
        @description ### QPS limit
        You can call this operation up to 300 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryCardSmsTemplateReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCardSmsTemplateReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template_codes):
            query['TemplateCodes'] = request.template_codes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCardSmsTemplateReport',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QueryCardSmsTemplateReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_card_sms_template_report_with_options_async(
        self,
        request: dysmsapi_20170525_models.QueryCardSmsTemplateReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QueryCardSmsTemplateReportResponse:
        """
        @summary Queries sent card messages.
        
        @description ### QPS limit
        You can call this operation up to 300 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryCardSmsTemplateReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCardSmsTemplateReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template_codes):
            query['TemplateCodes'] = request.template_codes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCardSmsTemplateReport',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QueryCardSmsTemplateReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_card_sms_template_report(
        self,
        request: dysmsapi_20170525_models.QueryCardSmsTemplateReportRequest,
    ) -> dysmsapi_20170525_models.QueryCardSmsTemplateReportResponse:
        """
        @summary Queries sent card messages.
        
        @description ### QPS limit
        You can call this operation up to 300 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryCardSmsTemplateReportRequest
        @return: QueryCardSmsTemplateReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_card_sms_template_report_with_options(request, runtime)

    async def query_card_sms_template_report_async(
        self,
        request: dysmsapi_20170525_models.QueryCardSmsTemplateReportRequest,
    ) -> dysmsapi_20170525_models.QueryCardSmsTemplateReportResponse:
        """
        @summary Queries sent card messages.
        
        @description ### QPS limit
        You can call this operation up to 300 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryCardSmsTemplateReportRequest
        @return: QueryCardSmsTemplateReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_card_sms_template_report_with_options_async(request, runtime)

    def query_ext_code_sign_with_options(
        self,
        request: dysmsapi_20170525_models.QueryExtCodeSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QueryExtCodeSignResponse:
        """
        @summary 查询验证码签名
        
        @param request: QueryExtCodeSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryExtCodeSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ext_code):
            query['ExtCode'] = request.ext_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryExtCodeSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QueryExtCodeSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ext_code_sign_with_options_async(
        self,
        request: dysmsapi_20170525_models.QueryExtCodeSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QueryExtCodeSignResponse:
        """
        @summary 查询验证码签名
        
        @param request: QueryExtCodeSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryExtCodeSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ext_code):
            query['ExtCode'] = request.ext_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryExtCodeSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QueryExtCodeSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ext_code_sign(
        self,
        request: dysmsapi_20170525_models.QueryExtCodeSignRequest,
    ) -> dysmsapi_20170525_models.QueryExtCodeSignResponse:
        """
        @summary 查询验证码签名
        
        @param request: QueryExtCodeSignRequest
        @return: QueryExtCodeSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_ext_code_sign_with_options(request, runtime)

    async def query_ext_code_sign_async(
        self,
        request: dysmsapi_20170525_models.QueryExtCodeSignRequest,
    ) -> dysmsapi_20170525_models.QueryExtCodeSignResponse:
        """
        @summary 查询验证码签名
        
        @param request: QueryExtCodeSignRequest
        @return: QueryExtCodeSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_ext_code_sign_with_options_async(request, runtime)

    def query_mobiles_card_support_with_options(
        self,
        tmp_req: dysmsapi_20170525_models.QueryMobilesCardSupportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QueryMobilesCardSupportResponse:
        """
        @summary Checks whether a mobile phone number can receive card messages.
        
        @param tmp_req: QueryMobilesCardSupportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMobilesCardSupportResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysmsapi_20170525_models.QueryMobilesCardSupportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.mobiles):
            request.mobiles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.mobiles, 'Mobiles', 'json')
        query = {}
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.mobiles_shrink):
            query['Mobiles'] = request.mobiles_shrink
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMobilesCardSupport',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QueryMobilesCardSupportResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mobiles_card_support_with_options_async(
        self,
        tmp_req: dysmsapi_20170525_models.QueryMobilesCardSupportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QueryMobilesCardSupportResponse:
        """
        @summary Checks whether a mobile phone number can receive card messages.
        
        @param tmp_req: QueryMobilesCardSupportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMobilesCardSupportResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysmsapi_20170525_models.QueryMobilesCardSupportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.mobiles):
            request.mobiles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.mobiles, 'Mobiles', 'json')
        query = {}
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.mobiles_shrink):
            query['Mobiles'] = request.mobiles_shrink
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMobilesCardSupport',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QueryMobilesCardSupportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mobiles_card_support(
        self,
        request: dysmsapi_20170525_models.QueryMobilesCardSupportRequest,
    ) -> dysmsapi_20170525_models.QueryMobilesCardSupportResponse:
        """
        @summary Checks whether a mobile phone number can receive card messages.
        
        @param request: QueryMobilesCardSupportRequest
        @return: QueryMobilesCardSupportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_mobiles_card_support_with_options(request, runtime)

    async def query_mobiles_card_support_async(
        self,
        request: dysmsapi_20170525_models.QueryMobilesCardSupportRequest,
    ) -> dysmsapi_20170525_models.QueryMobilesCardSupportResponse:
        """
        @summary Checks whether a mobile phone number can receive card messages.
        
        @param request: QueryMobilesCardSupportRequest
        @return: QueryMobilesCardSupportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_mobiles_card_support_with_options_async(request, runtime)

    def query_page_smart_short_url_log_with_options(
        self,
        request: dysmsapi_20170525_models.QueryPageSmartShortUrlLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QueryPageSmartShortUrlLogResponse:
        """
        @summary 点击明细查询
        
        @param request: QueryPageSmartShortUrlLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPageSmartShortUrlLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_date_end):
            query['CreateDateEnd'] = request.create_date_end
        if not UtilClient.is_unset(request.create_date_start):
            query['CreateDateStart'] = request.create_date_start
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.short_url):
            query['ShortUrl'] = request.short_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPageSmartShortUrlLog',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QueryPageSmartShortUrlLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_page_smart_short_url_log_with_options_async(
        self,
        request: dysmsapi_20170525_models.QueryPageSmartShortUrlLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QueryPageSmartShortUrlLogResponse:
        """
        @summary 点击明细查询
        
        @param request: QueryPageSmartShortUrlLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPageSmartShortUrlLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_date_end):
            query['CreateDateEnd'] = request.create_date_end
        if not UtilClient.is_unset(request.create_date_start):
            query['CreateDateStart'] = request.create_date_start
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.short_url):
            query['ShortUrl'] = request.short_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPageSmartShortUrlLog',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QueryPageSmartShortUrlLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_page_smart_short_url_log(
        self,
        request: dysmsapi_20170525_models.QueryPageSmartShortUrlLogRequest,
    ) -> dysmsapi_20170525_models.QueryPageSmartShortUrlLogResponse:
        """
        @summary 点击明细查询
        
        @param request: QueryPageSmartShortUrlLogRequest
        @return: QueryPageSmartShortUrlLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_page_smart_short_url_log_with_options(request, runtime)

    async def query_page_smart_short_url_log_async(
        self,
        request: dysmsapi_20170525_models.QueryPageSmartShortUrlLogRequest,
    ) -> dysmsapi_20170525_models.QueryPageSmartShortUrlLogResponse:
        """
        @summary 点击明细查询
        
        @param request: QueryPageSmartShortUrlLogRequest
        @return: QueryPageSmartShortUrlLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_page_smart_short_url_log_with_options_async(request, runtime)

    def query_send_details_with_options(
        self,
        request: dysmsapi_20170525_models.QuerySendDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySendDetailsResponse:
        """
        @summary Queries the information about a message.
        
        @param request: QuerySendDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySendDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_date):
            query['SendDate'] = request.send_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySendDetails',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySendDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_send_details_with_options_async(
        self,
        request: dysmsapi_20170525_models.QuerySendDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySendDetailsResponse:
        """
        @summary Queries the information about a message.
        
        @param request: QuerySendDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySendDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_date):
            query['SendDate'] = request.send_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySendDetails',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySendDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_send_details(
        self,
        request: dysmsapi_20170525_models.QuerySendDetailsRequest,
    ) -> dysmsapi_20170525_models.QuerySendDetailsResponse:
        """
        @summary Queries the information about a message.
        
        @param request: QuerySendDetailsRequest
        @return: QuerySendDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_send_details_with_options(request, runtime)

    async def query_send_details_async(
        self,
        request: dysmsapi_20170525_models.QuerySendDetailsRequest,
    ) -> dysmsapi_20170525_models.QuerySendDetailsResponse:
        """
        @summary Queries the information about a message.
        
        @param request: QuerySendDetailsRequest
        @return: QuerySendDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_send_details_with_options_async(request, runtime)

    def query_send_statistics_with_options(
        self,
        request: dysmsapi_20170525_models.QuerySendStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySendStatisticsResponse:
        """
        @summary Queries message delivery details.
        
        @description You can call the operation to query message delivery details, including the number of delivered messages, the number of messages with delivery receipts, and the time that a message is sent. If a large number of messages are sent on the specified date, you can specify the number of items displayed on each page and the number of pages to view the details by page.
        ### QPS limits
        You can call this operation up to 20 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QuerySendStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySendStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.is_globe):
            query['IsGlobe'] = request.is_globe
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySendStatistics',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySendStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_send_statistics_with_options_async(
        self,
        request: dysmsapi_20170525_models.QuerySendStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySendStatisticsResponse:
        """
        @summary Queries message delivery details.
        
        @description You can call the operation to query message delivery details, including the number of delivered messages, the number of messages with delivery receipts, and the time that a message is sent. If a large number of messages are sent on the specified date, you can specify the number of items displayed on each page and the number of pages to view the details by page.
        ### QPS limits
        You can call this operation up to 20 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QuerySendStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySendStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.is_globe):
            query['IsGlobe'] = request.is_globe
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySendStatistics',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySendStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_send_statistics(
        self,
        request: dysmsapi_20170525_models.QuerySendStatisticsRequest,
    ) -> dysmsapi_20170525_models.QuerySendStatisticsResponse:
        """
        @summary Queries message delivery details.
        
        @description You can call the operation to query message delivery details, including the number of delivered messages, the number of messages with delivery receipts, and the time that a message is sent. If a large number of messages are sent on the specified date, you can specify the number of items displayed on each page and the number of pages to view the details by page.
        ### QPS limits
        You can call this operation up to 20 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QuerySendStatisticsRequest
        @return: QuerySendStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_send_statistics_with_options(request, runtime)

    async def query_send_statistics_async(
        self,
        request: dysmsapi_20170525_models.QuerySendStatisticsRequest,
    ) -> dysmsapi_20170525_models.QuerySendStatisticsResponse:
        """
        @summary Queries message delivery details.
        
        @description You can call the operation to query message delivery details, including the number of delivered messages, the number of messages with delivery receipts, and the time that a message is sent. If a large number of messages are sent on the specified date, you can specify the number of items displayed on each page and the number of pages to view the details by page.
        ### QPS limits
        You can call this operation up to 20 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QuerySendStatisticsRequest
        @return: QuerySendStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_send_statistics_with_options_async(request, runtime)

    def query_short_url_with_options(
        self,
        request: dysmsapi_20170525_models.QueryShortUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QueryShortUrlResponse:
        """
        @summary Queries the status of a short URL.
        
        @description ### QPS limits
        You can call this operation up to 20 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryShortUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryShortUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.short_url):
            body['ShortUrl'] = request.short_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryShortUrl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QueryShortUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_short_url_with_options_async(
        self,
        request: dysmsapi_20170525_models.QueryShortUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QueryShortUrlResponse:
        """
        @summary Queries the status of a short URL.
        
        @description ### QPS limits
        You can call this operation up to 20 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryShortUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryShortUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.short_url):
            body['ShortUrl'] = request.short_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryShortUrl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QueryShortUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_short_url(
        self,
        request: dysmsapi_20170525_models.QueryShortUrlRequest,
    ) -> dysmsapi_20170525_models.QueryShortUrlResponse:
        """
        @summary Queries the status of a short URL.
        
        @description ### QPS limits
        You can call this operation up to 20 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryShortUrlRequest
        @return: QueryShortUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_short_url_with_options(request, runtime)

    async def query_short_url_async(
        self,
        request: dysmsapi_20170525_models.QueryShortUrlRequest,
    ) -> dysmsapi_20170525_models.QueryShortUrlResponse:
        """
        @summary Queries the status of a short URL.
        
        @description ### QPS limits
        You can call this operation up to 20 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QueryShortUrlRequest
        @return: QueryShortUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_short_url_with_options_async(request, runtime)

    def query_single_sms_qualification_with_options(
        self,
        request: dysmsapi_20170525_models.QuerySingleSmsQualificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySingleSmsQualificationResponse:
        """
        @summary 查询单个资质详情
        
        @param request: QuerySingleSmsQualificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySingleSmsQualificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_group_id):
            query['QualificationGroupId'] = request.qualification_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySingleSmsQualification',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySingleSmsQualificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_single_sms_qualification_with_options_async(
        self,
        request: dysmsapi_20170525_models.QuerySingleSmsQualificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySingleSmsQualificationResponse:
        """
        @summary 查询单个资质详情
        
        @param request: QuerySingleSmsQualificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySingleSmsQualificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_group_id):
            query['QualificationGroupId'] = request.qualification_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySingleSmsQualification',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySingleSmsQualificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_single_sms_qualification(
        self,
        request: dysmsapi_20170525_models.QuerySingleSmsQualificationRequest,
    ) -> dysmsapi_20170525_models.QuerySingleSmsQualificationResponse:
        """
        @summary 查询单个资质详情
        
        @param request: QuerySingleSmsQualificationRequest
        @return: QuerySingleSmsQualificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_single_sms_qualification_with_options(request, runtime)

    async def query_single_sms_qualification_async(
        self,
        request: dysmsapi_20170525_models.QuerySingleSmsQualificationRequest,
    ) -> dysmsapi_20170525_models.QuerySingleSmsQualificationResponse:
        """
        @summary 查询单个资质详情
        
        @param request: QuerySingleSmsQualificationRequest
        @return: QuerySingleSmsQualificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_single_sms_qualification_with_options_async(request, runtime)

    def query_sms_authorization_letter_with_options(
        self,
        tmp_req: dysmsapi_20170525_models.QuerySmsAuthorizationLetterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySmsAuthorizationLetterResponse:
        """
        @summary 查询委托授权书
        
        @param tmp_req: QuerySmsAuthorizationLetterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsAuthorizationLetterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysmsapi_20170525_models.QuerySmsAuthorizationLetterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.authorization_letter_id_list):
            request.authorization_letter_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.authorization_letter_id_list, 'AuthorizationLetterIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.authorization_letter_id_list_shrink):
            query['AuthorizationLetterIdList'] = request.authorization_letter_id_list_shrink
        if not UtilClient.is_unset(request.organization_code):
            query['OrganizationCode'] = request.organization_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsAuthorizationLetter',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySmsAuthorizationLetterResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_authorization_letter_with_options_async(
        self,
        tmp_req: dysmsapi_20170525_models.QuerySmsAuthorizationLetterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySmsAuthorizationLetterResponse:
        """
        @summary 查询委托授权书
        
        @param tmp_req: QuerySmsAuthorizationLetterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsAuthorizationLetterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysmsapi_20170525_models.QuerySmsAuthorizationLetterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.authorization_letter_id_list):
            request.authorization_letter_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.authorization_letter_id_list, 'AuthorizationLetterIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.authorization_letter_id_list_shrink):
            query['AuthorizationLetterIdList'] = request.authorization_letter_id_list_shrink
        if not UtilClient.is_unset(request.organization_code):
            query['OrganizationCode'] = request.organization_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsAuthorizationLetter',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySmsAuthorizationLetterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_authorization_letter(
        self,
        request: dysmsapi_20170525_models.QuerySmsAuthorizationLetterRequest,
    ) -> dysmsapi_20170525_models.QuerySmsAuthorizationLetterResponse:
        """
        @summary 查询委托授权书
        
        @param request: QuerySmsAuthorizationLetterRequest
        @return: QuerySmsAuthorizationLetterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_authorization_letter_with_options(request, runtime)

    async def query_sms_authorization_letter_async(
        self,
        request: dysmsapi_20170525_models.QuerySmsAuthorizationLetterRequest,
    ) -> dysmsapi_20170525_models.QuerySmsAuthorizationLetterResponse:
        """
        @summary 查询委托授权书
        
        @param request: QuerySmsAuthorizationLetterRequest
        @return: QuerySmsAuthorizationLetterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_authorization_letter_with_options_async(request, runtime)

    def query_sms_qualification_record_with_options(
        self,
        request: dysmsapi_20170525_models.QuerySmsQualificationRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySmsQualificationRecordResponse:
        """
        @summary 查询资质审核列表页
        
        @param request: QuerySmsQualificationRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsQualificationRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.company_name):
            query['CompanyName'] = request.company_name
        if not UtilClient.is_unset(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.qualification_group_name):
            query['QualificationGroupName'] = request.qualification_group_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.use_by_self):
            query['UseBySelf'] = request.use_by_self
        if not UtilClient.is_unset(request.work_order_id):
            query['WorkOrderId'] = request.work_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsQualificationRecord',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySmsQualificationRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_qualification_record_with_options_async(
        self,
        request: dysmsapi_20170525_models.QuerySmsQualificationRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySmsQualificationRecordResponse:
        """
        @summary 查询资质审核列表页
        
        @param request: QuerySmsQualificationRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsQualificationRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.company_name):
            query['CompanyName'] = request.company_name
        if not UtilClient.is_unset(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.qualification_group_name):
            query['QualificationGroupName'] = request.qualification_group_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.use_by_self):
            query['UseBySelf'] = request.use_by_self
        if not UtilClient.is_unset(request.work_order_id):
            query['WorkOrderId'] = request.work_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsQualificationRecord',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySmsQualificationRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_qualification_record(
        self,
        request: dysmsapi_20170525_models.QuerySmsQualificationRecordRequest,
    ) -> dysmsapi_20170525_models.QuerySmsQualificationRecordResponse:
        """
        @summary 查询资质审核列表页
        
        @param request: QuerySmsQualificationRecordRequest
        @return: QuerySmsQualificationRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_qualification_record_with_options(request, runtime)

    async def query_sms_qualification_record_async(
        self,
        request: dysmsapi_20170525_models.QuerySmsQualificationRecordRequest,
    ) -> dysmsapi_20170525_models.QuerySmsQualificationRecordResponse:
        """
        @summary 查询资质审核列表页
        
        @param request: QuerySmsQualificationRecordRequest
        @return: QuerySmsQualificationRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_qualification_record_with_options_async(request, runtime)

    def query_sms_sign_with_options(
        self,
        request: dysmsapi_20170525_models.QuerySmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySmsSignResponse:
        """
        @summary Queries the status of a signature.
        
        @description After you apply for an SMS signature, you can query its status by using the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm) or calling the operation. If the signature is rejected, you can modify the signature based on the reason why it is rejected.
        ### QPS limits
        You can call this API operation up to 500 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QuerySmsSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_sign_with_options_async(
        self,
        request: dysmsapi_20170525_models.QuerySmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySmsSignResponse:
        """
        @summary Queries the status of a signature.
        
        @description After you apply for an SMS signature, you can query its status by using the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm) or calling the operation. If the signature is rejected, you can modify the signature based on the reason why it is rejected.
        ### QPS limits
        You can call this API operation up to 500 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QuerySmsSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_sign(
        self,
        request: dysmsapi_20170525_models.QuerySmsSignRequest,
    ) -> dysmsapi_20170525_models.QuerySmsSignResponse:
        """
        @summary Queries the status of a signature.
        
        @description After you apply for an SMS signature, you can query its status by using the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm) or calling the operation. If the signature is rejected, you can modify the signature based on the reason why it is rejected.
        ### QPS limits
        You can call this API operation up to 500 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QuerySmsSignRequest
        @return: QuerySmsSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_sign_with_options(request, runtime)

    async def query_sms_sign_async(
        self,
        request: dysmsapi_20170525_models.QuerySmsSignRequest,
    ) -> dysmsapi_20170525_models.QuerySmsSignResponse:
        """
        @summary Queries the status of a signature.
        
        @description After you apply for an SMS signature, you can query its status by using the [Alibaba Cloud SMS console](https://dysms.console.aliyun.com/dysms.htm) or calling the operation. If the signature is rejected, you can modify the signature based on the reason why it is rejected.
        ### QPS limits
        You can call this API operation up to 500 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QuerySmsSignRequest
        @return: QuerySmsSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_sign_with_options_async(request, runtime)

    def query_sms_sign_list_with_options(
        self,
        request: dysmsapi_20170525_models.QuerySmsSignListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySmsSignListResponse:
        """
        @summary Queries message signatures by page.
        
        @description You can call this operation to query the details of message signatures, including the name, creation time, and approval status of each signature. If a message template is rejected, the reason is returned. Modify the message signature based on the reason.
        ### QPS limit
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QuerySmsSignListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSignListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSignList',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySmsSignListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_sign_list_with_options_async(
        self,
        request: dysmsapi_20170525_models.QuerySmsSignListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySmsSignListResponse:
        """
        @summary Queries message signatures by page.
        
        @description You can call this operation to query the details of message signatures, including the name, creation time, and approval status of each signature. If a message template is rejected, the reason is returned. Modify the message signature based on the reason.
        ### QPS limit
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QuerySmsSignListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSignListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSignList',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySmsSignListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_sign_list(
        self,
        request: dysmsapi_20170525_models.QuerySmsSignListRequest,
    ) -> dysmsapi_20170525_models.QuerySmsSignListResponse:
        """
        @summary Queries message signatures by page.
        
        @description You can call this operation to query the details of message signatures, including the name, creation time, and approval status of each signature. If a message template is rejected, the reason is returned. Modify the message signature based on the reason.
        ### QPS limit
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QuerySmsSignListRequest
        @return: QuerySmsSignListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_sign_list_with_options(request, runtime)

    async def query_sms_sign_list_async(
        self,
        request: dysmsapi_20170525_models.QuerySmsSignListRequest,
    ) -> dysmsapi_20170525_models.QuerySmsSignListResponse:
        """
        @summary Queries message signatures by page.
        
        @description You can call this operation to query the details of message signatures, including the name, creation time, and approval status of each signature. If a message template is rejected, the reason is returned. Modify the message signature based on the reason.
        ### QPS limit
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QuerySmsSignListRequest
        @return: QuerySmsSignListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_sign_list_with_options_async(request, runtime)

    def query_sms_template_with_options(
        self,
        request: dysmsapi_20170525_models.QuerySmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySmsTemplateResponse:
        """
        @deprecated OpenAPI QuerySmsTemplate is deprecated, please use Dysmsapi::2017-05-25::GetSmsTemplate instead.
        
        @summary Queries the approval status of a message template.
        
        @description After you create a message template, you can call this operation to query the approval status of the template. If a message template is rejected, the reason is returned. Modify the message template based on the reason.
        ### QPS limit
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QuerySmsTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsTemplateResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_template_with_options_async(
        self,
        request: dysmsapi_20170525_models.QuerySmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySmsTemplateResponse:
        """
        @deprecated OpenAPI QuerySmsTemplate is deprecated, please use Dysmsapi::2017-05-25::GetSmsTemplate instead.
        
        @summary Queries the approval status of a message template.
        
        @description After you create a message template, you can call this operation to query the approval status of the template. If a message template is rejected, the reason is returned. Modify the message template based on the reason.
        ### QPS limit
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QuerySmsTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsTemplateResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_template(
        self,
        request: dysmsapi_20170525_models.QuerySmsTemplateRequest,
    ) -> dysmsapi_20170525_models.QuerySmsTemplateResponse:
        """
        @deprecated OpenAPI QuerySmsTemplate is deprecated, please use Dysmsapi::2017-05-25::GetSmsTemplate instead.
        
        @summary Queries the approval status of a message template.
        
        @description After you create a message template, you can call this operation to query the approval status of the template. If a message template is rejected, the reason is returned. Modify the message template based on the reason.
        ### QPS limit
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QuerySmsTemplateRequest
        @return: QuerySmsTemplateResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_template_with_options(request, runtime)

    async def query_sms_template_async(
        self,
        request: dysmsapi_20170525_models.QuerySmsTemplateRequest,
    ) -> dysmsapi_20170525_models.QuerySmsTemplateResponse:
        """
        @deprecated OpenAPI QuerySmsTemplate is deprecated, please use Dysmsapi::2017-05-25::GetSmsTemplate instead.
        
        @summary Queries the approval status of a message template.
        
        @description After you create a message template, you can call this operation to query the approval status of the template. If a message template is rejected, the reason is returned. Modify the message template based on the reason.
        ### QPS limit
        You can call this operation up to 5,000 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QuerySmsTemplateRequest
        @return: QuerySmsTemplateResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_template_with_options_async(request, runtime)

    def query_sms_template_list_with_options(
        self,
        request: dysmsapi_20170525_models.QuerySmsTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySmsTemplateListResponse:
        """
        @summary Queries message templates.
        
        @description You can call this operation to query the details of message templates, including the name, creation time, and approval status of each template. If a message template is rejected, the reason is returned. Modify the message template based on the reason.
        ### QPS limit
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QuerySmsTemplateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsTemplateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsTemplateList',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySmsTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_template_list_with_options_async(
        self,
        request: dysmsapi_20170525_models.QuerySmsTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.QuerySmsTemplateListResponse:
        """
        @summary Queries message templates.
        
        @description You can call this operation to query the details of message templates, including the name, creation time, and approval status of each template. If a message template is rejected, the reason is returned. Modify the message template based on the reason.
        ### QPS limit
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QuerySmsTemplateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsTemplateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsTemplateList',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySmsTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_template_list(
        self,
        request: dysmsapi_20170525_models.QuerySmsTemplateListRequest,
    ) -> dysmsapi_20170525_models.QuerySmsTemplateListResponse:
        """
        @summary Queries message templates.
        
        @description You can call this operation to query the details of message templates, including the name, creation time, and approval status of each template. If a message template is rejected, the reason is returned. Modify the message template based on the reason.
        ### QPS limit
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QuerySmsTemplateListRequest
        @return: QuerySmsTemplateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_template_list_with_options(request, runtime)

    async def query_sms_template_list_async(
        self,
        request: dysmsapi_20170525_models.QuerySmsTemplateListRequest,
    ) -> dysmsapi_20170525_models.QuerySmsTemplateListResponse:
        """
        @summary Queries message templates.
        
        @description You can call this operation to query the details of message templates, including the name, creation time, and approval status of each template. If a message template is rejected, the reason is returned. Modify the message template based on the reason.
        ### QPS limit
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: QuerySmsTemplateListRequest
        @return: QuerySmsTemplateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_template_list_with_options_async(request, runtime)

    def required_phone_code_with_options(
        self,
        request: dysmsapi_20170525_models.RequiredPhoneCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.RequiredPhoneCodeResponse:
        """
        @summary 验证手机验证码
        
        @param request: RequiredPhoneCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RequiredPhoneCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no):
            query['PhoneNo'] = request.phone_no
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RequiredPhoneCode',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.RequiredPhoneCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def required_phone_code_with_options_async(
        self,
        request: dysmsapi_20170525_models.RequiredPhoneCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.RequiredPhoneCodeResponse:
        """
        @summary 验证手机验证码
        
        @param request: RequiredPhoneCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RequiredPhoneCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no):
            query['PhoneNo'] = request.phone_no
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RequiredPhoneCode',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.RequiredPhoneCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def required_phone_code(
        self,
        request: dysmsapi_20170525_models.RequiredPhoneCodeRequest,
    ) -> dysmsapi_20170525_models.RequiredPhoneCodeResponse:
        """
        @summary 验证手机验证码
        
        @param request: RequiredPhoneCodeRequest
        @return: RequiredPhoneCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.required_phone_code_with_options(request, runtime)

    async def required_phone_code_async(
        self,
        request: dysmsapi_20170525_models.RequiredPhoneCodeRequest,
    ) -> dysmsapi_20170525_models.RequiredPhoneCodeResponse:
        """
        @summary 验证手机验证码
        
        @param request: RequiredPhoneCodeRequest
        @return: RequiredPhoneCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.required_phone_code_with_options_async(request, runtime)

    def send_batch_card_sms_with_options(
        self,
        request: dysmsapi_20170525_models.SendBatchCardSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SendBatchCardSmsResponse:
        """
        @summary Sends multiple card messages at a time.
        
        @description You can call the operation to send multiple card messages to a maximum of mobile phone numbers at a time. Different signatures and rollback settings can be specified for the mobile phone numbers.
        ### QPS limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: SendBatchCardSmsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendBatchCardSmsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.card_template_code):
            query['CardTemplateCode'] = request.card_template_code
        if not UtilClient.is_unset(request.card_template_param_json):
            query['CardTemplateParamJson'] = request.card_template_param_json
        if not UtilClient.is_unset(request.digital_template_code):
            query['DigitalTemplateCode'] = request.digital_template_code
        if not UtilClient.is_unset(request.digital_template_param_json):
            query['DigitalTemplateParamJson'] = request.digital_template_param_json
        if not UtilClient.is_unset(request.fallback_type):
            query['FallbackType'] = request.fallback_type
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.phone_number_json):
            query['PhoneNumberJson'] = request.phone_number_json
        if not UtilClient.is_unset(request.sign_name_json):
            query['SignNameJson'] = request.sign_name_json
        if not UtilClient.is_unset(request.sms_template_code):
            query['SmsTemplateCode'] = request.sms_template_code
        if not UtilClient.is_unset(request.sms_template_param_json):
            query['SmsTemplateParamJson'] = request.sms_template_param_json
        if not UtilClient.is_unset(request.sms_up_extend_code_json):
            query['SmsUpExtendCodeJson'] = request.sms_up_extend_code_json
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param_json):
            query['TemplateParamJson'] = request.template_param_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendBatchCardSms',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SendBatchCardSmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_batch_card_sms_with_options_async(
        self,
        request: dysmsapi_20170525_models.SendBatchCardSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SendBatchCardSmsResponse:
        """
        @summary Sends multiple card messages at a time.
        
        @description You can call the operation to send multiple card messages to a maximum of mobile phone numbers at a time. Different signatures and rollback settings can be specified for the mobile phone numbers.
        ### QPS limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: SendBatchCardSmsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendBatchCardSmsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.card_template_code):
            query['CardTemplateCode'] = request.card_template_code
        if not UtilClient.is_unset(request.card_template_param_json):
            query['CardTemplateParamJson'] = request.card_template_param_json
        if not UtilClient.is_unset(request.digital_template_code):
            query['DigitalTemplateCode'] = request.digital_template_code
        if not UtilClient.is_unset(request.digital_template_param_json):
            query['DigitalTemplateParamJson'] = request.digital_template_param_json
        if not UtilClient.is_unset(request.fallback_type):
            query['FallbackType'] = request.fallback_type
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.phone_number_json):
            query['PhoneNumberJson'] = request.phone_number_json
        if not UtilClient.is_unset(request.sign_name_json):
            query['SignNameJson'] = request.sign_name_json
        if not UtilClient.is_unset(request.sms_template_code):
            query['SmsTemplateCode'] = request.sms_template_code
        if not UtilClient.is_unset(request.sms_template_param_json):
            query['SmsTemplateParamJson'] = request.sms_template_param_json
        if not UtilClient.is_unset(request.sms_up_extend_code_json):
            query['SmsUpExtendCodeJson'] = request.sms_up_extend_code_json
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param_json):
            query['TemplateParamJson'] = request.template_param_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendBatchCardSms',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SendBatchCardSmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_batch_card_sms(
        self,
        request: dysmsapi_20170525_models.SendBatchCardSmsRequest,
    ) -> dysmsapi_20170525_models.SendBatchCardSmsResponse:
        """
        @summary Sends multiple card messages at a time.
        
        @description You can call the operation to send multiple card messages to a maximum of mobile phone numbers at a time. Different signatures and rollback settings can be specified for the mobile phone numbers.
        ### QPS limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: SendBatchCardSmsRequest
        @return: SendBatchCardSmsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_batch_card_sms_with_options(request, runtime)

    async def send_batch_card_sms_async(
        self,
        request: dysmsapi_20170525_models.SendBatchCardSmsRequest,
    ) -> dysmsapi_20170525_models.SendBatchCardSmsResponse:
        """
        @summary Sends multiple card messages at a time.
        
        @description You can call the operation to send multiple card messages to a maximum of mobile phone numbers at a time. Different signatures and rollback settings can be specified for the mobile phone numbers.
        ### QPS limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: SendBatchCardSmsRequest
        @return: SendBatchCardSmsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_batch_card_sms_with_options_async(request, runtime)

    def send_batch_sms_with_options(
        self,
        request: dysmsapi_20170525_models.SendBatchSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SendBatchSmsResponse:
        """
        @summary Uses a single message template and multiple signatures to send messages to multiple recipients.
        
        @description You can call the operation to send messages to a maximum of 100 recipients at a time.
        
        @param request: SendBatchSmsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendBatchSmsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        body = {}
        if not UtilClient.is_unset(request.phone_number_json):
            body['PhoneNumberJson'] = request.phone_number_json
        if not UtilClient.is_unset(request.sign_name_json):
            body['SignNameJson'] = request.sign_name_json
        if not UtilClient.is_unset(request.sms_up_extend_code_json):
            body['SmsUpExtendCodeJson'] = request.sms_up_extend_code_json
        if not UtilClient.is_unset(request.template_param_json):
            body['TemplateParamJson'] = request.template_param_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendBatchSms',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SendBatchSmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_batch_sms_with_options_async(
        self,
        request: dysmsapi_20170525_models.SendBatchSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SendBatchSmsResponse:
        """
        @summary Uses a single message template and multiple signatures to send messages to multiple recipients.
        
        @description You can call the operation to send messages to a maximum of 100 recipients at a time.
        
        @param request: SendBatchSmsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendBatchSmsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        body = {}
        if not UtilClient.is_unset(request.phone_number_json):
            body['PhoneNumberJson'] = request.phone_number_json
        if not UtilClient.is_unset(request.sign_name_json):
            body['SignNameJson'] = request.sign_name_json
        if not UtilClient.is_unset(request.sms_up_extend_code_json):
            body['SmsUpExtendCodeJson'] = request.sms_up_extend_code_json
        if not UtilClient.is_unset(request.template_param_json):
            body['TemplateParamJson'] = request.template_param_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendBatchSms',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SendBatchSmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_batch_sms(
        self,
        request: dysmsapi_20170525_models.SendBatchSmsRequest,
    ) -> dysmsapi_20170525_models.SendBatchSmsResponse:
        """
        @summary Uses a single message template and multiple signatures to send messages to multiple recipients.
        
        @description You can call the operation to send messages to a maximum of 100 recipients at a time.
        
        @param request: SendBatchSmsRequest
        @return: SendBatchSmsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_batch_sms_with_options(request, runtime)

    async def send_batch_sms_async(
        self,
        request: dysmsapi_20170525_models.SendBatchSmsRequest,
    ) -> dysmsapi_20170525_models.SendBatchSmsResponse:
        """
        @summary Uses a single message template and multiple signatures to send messages to multiple recipients.
        
        @description You can call the operation to send messages to a maximum of 100 recipients at a time.
        
        @param request: SendBatchSmsRequest
        @return: SendBatchSmsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_batch_sms_with_options_async(request, runtime)

    def send_card_sms_with_options(
        self,
        request: dysmsapi_20170525_models.SendCardSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SendCardSmsResponse:
        """
        @summary Sends a card message.
        
        @description    Make sure that the message template that you want to use has been approved. If the mobile phone number of a recipient does not support card messages, the SendCardSms operation allows the rollback feature to ensure successful delivery.
        When you call the SendCardSms operation to send card messages, the operation checks whether the mobile phone numbers of the recipients support card messages. If the mobile phone numbers do not support card messages, you can specify whether to enable rollback. Otherwise, the card message cannot be delivered.
        ### QPS limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: SendCardSmsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendCardSmsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.card_objects):
            query['CardObjects'] = request.card_objects
        if not UtilClient.is_unset(request.card_template_code):
            query['CardTemplateCode'] = request.card_template_code
        if not UtilClient.is_unset(request.digital_template_code):
            query['DigitalTemplateCode'] = request.digital_template_code
        if not UtilClient.is_unset(request.digital_template_param):
            query['DigitalTemplateParam'] = request.digital_template_param
        if not UtilClient.is_unset(request.fallback_type):
            query['FallbackType'] = request.fallback_type
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sms_template_code):
            query['SmsTemplateCode'] = request.sms_template_code
        if not UtilClient.is_unset(request.sms_template_param):
            query['SmsTemplateParam'] = request.sms_template_param
        if not UtilClient.is_unset(request.sms_up_extend_code):
            query['SmsUpExtendCode'] = request.sms_up_extend_code
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param):
            query['TemplateParam'] = request.template_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendCardSms',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SendCardSmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_card_sms_with_options_async(
        self,
        request: dysmsapi_20170525_models.SendCardSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SendCardSmsResponse:
        """
        @summary Sends a card message.
        
        @description    Make sure that the message template that you want to use has been approved. If the mobile phone number of a recipient does not support card messages, the SendCardSms operation allows the rollback feature to ensure successful delivery.
        When you call the SendCardSms operation to send card messages, the operation checks whether the mobile phone numbers of the recipients support card messages. If the mobile phone numbers do not support card messages, you can specify whether to enable rollback. Otherwise, the card message cannot be delivered.
        ### QPS limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: SendCardSmsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendCardSmsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.card_objects):
            query['CardObjects'] = request.card_objects
        if not UtilClient.is_unset(request.card_template_code):
            query['CardTemplateCode'] = request.card_template_code
        if not UtilClient.is_unset(request.digital_template_code):
            query['DigitalTemplateCode'] = request.digital_template_code
        if not UtilClient.is_unset(request.digital_template_param):
            query['DigitalTemplateParam'] = request.digital_template_param
        if not UtilClient.is_unset(request.fallback_type):
            query['FallbackType'] = request.fallback_type
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sms_template_code):
            query['SmsTemplateCode'] = request.sms_template_code
        if not UtilClient.is_unset(request.sms_template_param):
            query['SmsTemplateParam'] = request.sms_template_param
        if not UtilClient.is_unset(request.sms_up_extend_code):
            query['SmsUpExtendCode'] = request.sms_up_extend_code
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param):
            query['TemplateParam'] = request.template_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendCardSms',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SendCardSmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_card_sms(
        self,
        request: dysmsapi_20170525_models.SendCardSmsRequest,
    ) -> dysmsapi_20170525_models.SendCardSmsResponse:
        """
        @summary Sends a card message.
        
        @description    Make sure that the message template that you want to use has been approved. If the mobile phone number of a recipient does not support card messages, the SendCardSms operation allows the rollback feature to ensure successful delivery.
        When you call the SendCardSms operation to send card messages, the operation checks whether the mobile phone numbers of the recipients support card messages. If the mobile phone numbers do not support card messages, you can specify whether to enable rollback. Otherwise, the card message cannot be delivered.
        ### QPS limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: SendCardSmsRequest
        @return: SendCardSmsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_card_sms_with_options(request, runtime)

    async def send_card_sms_async(
        self,
        request: dysmsapi_20170525_models.SendCardSmsRequest,
    ) -> dysmsapi_20170525_models.SendCardSmsResponse:
        """
        @summary Sends a card message.
        
        @description    Make sure that the message template that you want to use has been approved. If the mobile phone number of a recipient does not support card messages, the SendCardSms operation allows the rollback feature to ensure successful delivery.
        When you call the SendCardSms operation to send card messages, the operation checks whether the mobile phone numbers of the recipients support card messages. If the mobile phone numbers do not support card messages, you can specify whether to enable rollback. Otherwise, the card message cannot be delivered.
        ### QPS limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: SendCardSmsRequest
        @return: SendCardSmsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_card_sms_with_options_async(request, runtime)

    def send_logistics_sms_with_options(
        self,
        request: dysmsapi_20170525_models.SendLogisticsSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SendLogisticsSmsResponse:
        """
        @summary 发送物流短信
        
        @param request: SendLogisticsSmsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendLogisticsSmsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.express_company_code):
            query['ExpressCompanyCode'] = request.express_company_code
        if not UtilClient.is_unset(request.mail_no):
            query['MailNo'] = request.mail_no
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.platform_company_code):
            query['PlatformCompanyCode'] = request.platform_company_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param):
            query['TemplateParam'] = request.template_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendLogisticsSms',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SendLogisticsSmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_logistics_sms_with_options_async(
        self,
        request: dysmsapi_20170525_models.SendLogisticsSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SendLogisticsSmsResponse:
        """
        @summary 发送物流短信
        
        @param request: SendLogisticsSmsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendLogisticsSmsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.express_company_code):
            query['ExpressCompanyCode'] = request.express_company_code
        if not UtilClient.is_unset(request.mail_no):
            query['MailNo'] = request.mail_no
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.platform_company_code):
            query['PlatformCompanyCode'] = request.platform_company_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param):
            query['TemplateParam'] = request.template_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendLogisticsSms',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SendLogisticsSmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_logistics_sms(
        self,
        request: dysmsapi_20170525_models.SendLogisticsSmsRequest,
    ) -> dysmsapi_20170525_models.SendLogisticsSmsResponse:
        """
        @summary 发送物流短信
        
        @param request: SendLogisticsSmsRequest
        @return: SendLogisticsSmsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_logistics_sms_with_options(request, runtime)

    async def send_logistics_sms_async(
        self,
        request: dysmsapi_20170525_models.SendLogisticsSmsRequest,
    ) -> dysmsapi_20170525_models.SendLogisticsSmsResponse:
        """
        @summary 发送物流短信
        
        @param request: SendLogisticsSmsRequest
        @return: SendLogisticsSmsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_logistics_sms_with_options_async(request, runtime)

    def send_sms_with_options(
        self,
        request: dysmsapi_20170525_models.SendSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SendSmsResponse:
        """
        @summary Sends a message. Before you call this operation, submit a message signature and message template, and make sure that the signature and template are approved.
        
        @description    This operation is mainly used to send a single message. In special scenarios, you can send multiple messages with the same content to a maximum of 1,000 mobile numbers. Note that group sending may be delayed.
        To send messages with different signatures and template content to multiple mobile numbers in a single request, call the [SendBatchSms](https://help.aliyun.com/document_detail/102364.html) operation.
        You are charged for using Alibaba Cloud Short Message Service (SMS) based on the amount of messages sent. For more information, see [Pricing](https://www.aliyun.com/price/product#/sms/detail).
        If your verification code signature and general-purpose signature have the same name, the system uses the general-purpose signature to send messages by default.
        
        @param request: SendSmsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendSmsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_numbers):
            query['PhoneNumbers'] = request.phone_numbers
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sms_up_extend_code):
            query['SmsUpExtendCode'] = request.sms_up_extend_code
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param):
            query['TemplateParam'] = request.template_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendSms',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SendSmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_sms_with_options_async(
        self,
        request: dysmsapi_20170525_models.SendSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SendSmsResponse:
        """
        @summary Sends a message. Before you call this operation, submit a message signature and message template, and make sure that the signature and template are approved.
        
        @description    This operation is mainly used to send a single message. In special scenarios, you can send multiple messages with the same content to a maximum of 1,000 mobile numbers. Note that group sending may be delayed.
        To send messages with different signatures and template content to multiple mobile numbers in a single request, call the [SendBatchSms](https://help.aliyun.com/document_detail/102364.html) operation.
        You are charged for using Alibaba Cloud Short Message Service (SMS) based on the amount of messages sent. For more information, see [Pricing](https://www.aliyun.com/price/product#/sms/detail).
        If your verification code signature and general-purpose signature have the same name, the system uses the general-purpose signature to send messages by default.
        
        @param request: SendSmsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendSmsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.out_id):
            query['OutId'] = request.out_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_numbers):
            query['PhoneNumbers'] = request.phone_numbers
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sms_up_extend_code):
            query['SmsUpExtendCode'] = request.sms_up_extend_code
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param):
            query['TemplateParam'] = request.template_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendSms',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SendSmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_sms(
        self,
        request: dysmsapi_20170525_models.SendSmsRequest,
    ) -> dysmsapi_20170525_models.SendSmsResponse:
        """
        @summary Sends a message. Before you call this operation, submit a message signature and message template, and make sure that the signature and template are approved.
        
        @description    This operation is mainly used to send a single message. In special scenarios, you can send multiple messages with the same content to a maximum of 1,000 mobile numbers. Note that group sending may be delayed.
        To send messages with different signatures and template content to multiple mobile numbers in a single request, call the [SendBatchSms](https://help.aliyun.com/document_detail/102364.html) operation.
        You are charged for using Alibaba Cloud Short Message Service (SMS) based on the amount of messages sent. For more information, see [Pricing](https://www.aliyun.com/price/product#/sms/detail).
        If your verification code signature and general-purpose signature have the same name, the system uses the general-purpose signature to send messages by default.
        
        @param request: SendSmsRequest
        @return: SendSmsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_sms_with_options(request, runtime)

    async def send_sms_async(
        self,
        request: dysmsapi_20170525_models.SendSmsRequest,
    ) -> dysmsapi_20170525_models.SendSmsResponse:
        """
        @summary Sends a message. Before you call this operation, submit a message signature and message template, and make sure that the signature and template are approved.
        
        @description    This operation is mainly used to send a single message. In special scenarios, you can send multiple messages with the same content to a maximum of 1,000 mobile numbers. Note that group sending may be delayed.
        To send messages with different signatures and template content to multiple mobile numbers in a single request, call the [SendBatchSms](https://help.aliyun.com/document_detail/102364.html) operation.
        You are charged for using Alibaba Cloud Short Message Service (SMS) based on the amount of messages sent. For more information, see [Pricing](https://www.aliyun.com/price/product#/sms/detail).
        If your verification code signature and general-purpose signature have the same name, the system uses the general-purpose signature to send messages by default.
        
        @param request: SendSmsRequest
        @return: SendSmsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_sms_with_options_async(request, runtime)

    def sms_conversion_intl_with_options(
        self,
        request: dysmsapi_20170525_models.SmsConversionIntlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SmsConversionIntlResponse:
        """
        @summary Reports the status of an OTP message to Alibaba Cloud SMS.
        
        @description Metrics:
        Requested OTP messages
        Verified OTP messages
        An OTP conversion rate is calculated based on the following formula: OTP conversion rate = Number of verified OTP messages/Number of requested OTP messages.
        > If you call the SmsConversion operation to query OTP conversion rates, your business may be affected. We recommend that you perform the following operations: 1. Call the SmsConversion operation in an asynchronous manner by configuring queues or events. 2. Manually degrade your services or use a circuit breaker to automatically degrade services.
        
        @param request: SmsConversionIntlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SmsConversionIntlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conversion_time):
            query['ConversionTime'] = request.conversion_time
        if not UtilClient.is_unset(request.delivered):
            query['Delivered'] = request.delivered
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SmsConversionIntl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SmsConversionIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def sms_conversion_intl_with_options_async(
        self,
        request: dysmsapi_20170525_models.SmsConversionIntlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SmsConversionIntlResponse:
        """
        @summary Reports the status of an OTP message to Alibaba Cloud SMS.
        
        @description Metrics:
        Requested OTP messages
        Verified OTP messages
        An OTP conversion rate is calculated based on the following formula: OTP conversion rate = Number of verified OTP messages/Number of requested OTP messages.
        > If you call the SmsConversion operation to query OTP conversion rates, your business may be affected. We recommend that you perform the following operations: 1. Call the SmsConversion operation in an asynchronous manner by configuring queues or events. 2. Manually degrade your services or use a circuit breaker to automatically degrade services.
        
        @param request: SmsConversionIntlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SmsConversionIntlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conversion_time):
            query['ConversionTime'] = request.conversion_time
        if not UtilClient.is_unset(request.delivered):
            query['Delivered'] = request.delivered
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SmsConversionIntl',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SmsConversionIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sms_conversion_intl(
        self,
        request: dysmsapi_20170525_models.SmsConversionIntlRequest,
    ) -> dysmsapi_20170525_models.SmsConversionIntlResponse:
        """
        @summary Reports the status of an OTP message to Alibaba Cloud SMS.
        
        @description Metrics:
        Requested OTP messages
        Verified OTP messages
        An OTP conversion rate is calculated based on the following formula: OTP conversion rate = Number of verified OTP messages/Number of requested OTP messages.
        > If you call the SmsConversion operation to query OTP conversion rates, your business may be affected. We recommend that you perform the following operations: 1. Call the SmsConversion operation in an asynchronous manner by configuring queues or events. 2. Manually degrade your services or use a circuit breaker to automatically degrade services.
        
        @param request: SmsConversionIntlRequest
        @return: SmsConversionIntlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.sms_conversion_intl_with_options(request, runtime)

    async def sms_conversion_intl_async(
        self,
        request: dysmsapi_20170525_models.SmsConversionIntlRequest,
    ) -> dysmsapi_20170525_models.SmsConversionIntlResponse:
        """
        @summary Reports the status of an OTP message to Alibaba Cloud SMS.
        
        @description Metrics:
        Requested OTP messages
        Verified OTP messages
        An OTP conversion rate is calculated based on the following formula: OTP conversion rate = Number of verified OTP messages/Number of requested OTP messages.
        > If you call the SmsConversion operation to query OTP conversion rates, your business may be affected. We recommend that you perform the following operations: 1. Call the SmsConversion operation in an asynchronous manner by configuring queues or events. 2. Manually degrade your services or use a circuit breaker to automatically degrade services.
        
        @param request: SmsConversionIntlRequest
        @return: SmsConversionIntlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.sms_conversion_intl_with_options_async(request, runtime)

    def submit_sms_qualification_with_options(
        self,
        tmp_req: dysmsapi_20170525_models.SubmitSmsQualificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SubmitSmsQualificationResponse:
        """
        @summary 创建资质对客openAPI
        
        @param tmp_req: SubmitSmsQualificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitSmsQualificationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysmsapi_20170525_models.SubmitSmsQualificationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.business_license_pics):
            request.business_license_pics_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.business_license_pics, 'BusinessLicensePics', 'json')
        if not UtilClient.is_unset(tmp_req.other_files):
            request.other_files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.other_files, 'OtherFiles', 'json')
        query = {}
        if not UtilClient.is_unset(request.admin_idcard_exp_date):
            query['AdminIDCardExpDate'] = request.admin_idcard_exp_date
        if not UtilClient.is_unset(request.admin_idcard_front_face):
            query['AdminIDCardFrontFace'] = request.admin_idcard_front_face
        if not UtilClient.is_unset(request.admin_idcard_no):
            query['AdminIDCardNo'] = request.admin_idcard_no
        if not UtilClient.is_unset(request.admin_idcard_pic):
            query['AdminIDCardPic'] = request.admin_idcard_pic
        if not UtilClient.is_unset(request.admin_idcard_type):
            query['AdminIDCardType'] = request.admin_idcard_type
        if not UtilClient.is_unset(request.admin_name):
            query['AdminName'] = request.admin_name
        if not UtilClient.is_unset(request.admin_phone_no):
            query['AdminPhoneNo'] = request.admin_phone_no
        if not UtilClient.is_unset(request.business_license_pics_shrink):
            query['BusinessLicensePics'] = request.business_license_pics_shrink
        if not UtilClient.is_unset(request.bussiness_license_exp_date):
            query['BussinessLicenseExpDate'] = request.bussiness_license_exp_date
        if not UtilClient.is_unset(request.certify_code):
            query['CertifyCode'] = request.certify_code
        if not UtilClient.is_unset(request.company_name):
            query['CompanyName'] = request.company_name
        if not UtilClient.is_unset(request.company_type):
            query['CompanyType'] = request.company_type
        if not UtilClient.is_unset(request.legal_person_idcard_no):
            query['LegalPersonIDCardNo'] = request.legal_person_idcard_no
        if not UtilClient.is_unset(request.legal_person_idcard_type):
            query['LegalPersonIDCardType'] = request.legal_person_idcard_type
        if not UtilClient.is_unset(request.legal_person_id_card_back_side):
            query['LegalPersonIdCardBackSide'] = request.legal_person_id_card_back_side
        if not UtilClient.is_unset(request.legal_person_id_card_eff_time):
            query['LegalPersonIdCardEffTime'] = request.legal_person_id_card_eff_time
        if not UtilClient.is_unset(request.legal_person_id_card_front_side):
            query['LegalPersonIdCardFrontSide'] = request.legal_person_id_card_front_side
        if not UtilClient.is_unset(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not UtilClient.is_unset(request.organization_code):
            query['OrganizationCode'] = request.organization_code
        if not UtilClient.is_unset(request.other_files_shrink):
            query['OtherFiles'] = request.other_files_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_name):
            query['QualificationName'] = request.qualification_name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.use_by_self):
            query['UseBySelf'] = request.use_by_self
        if not UtilClient.is_unset(request.whether_share):
            query['WhetherShare'] = request.whether_share
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSmsQualification',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SubmitSmsQualificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_sms_qualification_with_options_async(
        self,
        tmp_req: dysmsapi_20170525_models.SubmitSmsQualificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.SubmitSmsQualificationResponse:
        """
        @summary 创建资质对客openAPI
        
        @param tmp_req: SubmitSmsQualificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitSmsQualificationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysmsapi_20170525_models.SubmitSmsQualificationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.business_license_pics):
            request.business_license_pics_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.business_license_pics, 'BusinessLicensePics', 'json')
        if not UtilClient.is_unset(tmp_req.other_files):
            request.other_files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.other_files, 'OtherFiles', 'json')
        query = {}
        if not UtilClient.is_unset(request.admin_idcard_exp_date):
            query['AdminIDCardExpDate'] = request.admin_idcard_exp_date
        if not UtilClient.is_unset(request.admin_idcard_front_face):
            query['AdminIDCardFrontFace'] = request.admin_idcard_front_face
        if not UtilClient.is_unset(request.admin_idcard_no):
            query['AdminIDCardNo'] = request.admin_idcard_no
        if not UtilClient.is_unset(request.admin_idcard_pic):
            query['AdminIDCardPic'] = request.admin_idcard_pic
        if not UtilClient.is_unset(request.admin_idcard_type):
            query['AdminIDCardType'] = request.admin_idcard_type
        if not UtilClient.is_unset(request.admin_name):
            query['AdminName'] = request.admin_name
        if not UtilClient.is_unset(request.admin_phone_no):
            query['AdminPhoneNo'] = request.admin_phone_no
        if not UtilClient.is_unset(request.business_license_pics_shrink):
            query['BusinessLicensePics'] = request.business_license_pics_shrink
        if not UtilClient.is_unset(request.bussiness_license_exp_date):
            query['BussinessLicenseExpDate'] = request.bussiness_license_exp_date
        if not UtilClient.is_unset(request.certify_code):
            query['CertifyCode'] = request.certify_code
        if not UtilClient.is_unset(request.company_name):
            query['CompanyName'] = request.company_name
        if not UtilClient.is_unset(request.company_type):
            query['CompanyType'] = request.company_type
        if not UtilClient.is_unset(request.legal_person_idcard_no):
            query['LegalPersonIDCardNo'] = request.legal_person_idcard_no
        if not UtilClient.is_unset(request.legal_person_idcard_type):
            query['LegalPersonIDCardType'] = request.legal_person_idcard_type
        if not UtilClient.is_unset(request.legal_person_id_card_back_side):
            query['LegalPersonIdCardBackSide'] = request.legal_person_id_card_back_side
        if not UtilClient.is_unset(request.legal_person_id_card_eff_time):
            query['LegalPersonIdCardEffTime'] = request.legal_person_id_card_eff_time
        if not UtilClient.is_unset(request.legal_person_id_card_front_side):
            query['LegalPersonIdCardFrontSide'] = request.legal_person_id_card_front_side
        if not UtilClient.is_unset(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not UtilClient.is_unset(request.organization_code):
            query['OrganizationCode'] = request.organization_code
        if not UtilClient.is_unset(request.other_files_shrink):
            query['OtherFiles'] = request.other_files_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_name):
            query['QualificationName'] = request.qualification_name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.use_by_self):
            query['UseBySelf'] = request.use_by_self
        if not UtilClient.is_unset(request.whether_share):
            query['WhetherShare'] = request.whether_share
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSmsQualification',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SubmitSmsQualificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_sms_qualification(
        self,
        request: dysmsapi_20170525_models.SubmitSmsQualificationRequest,
    ) -> dysmsapi_20170525_models.SubmitSmsQualificationResponse:
        """
        @summary 创建资质对客openAPI
        
        @param request: SubmitSmsQualificationRequest
        @return: SubmitSmsQualificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_sms_qualification_with_options(request, runtime)

    async def submit_sms_qualification_async(
        self,
        request: dysmsapi_20170525_models.SubmitSmsQualificationRequest,
    ) -> dysmsapi_20170525_models.SubmitSmsQualificationResponse:
        """
        @summary 创建资质对客openAPI
        
        @param request: SubmitSmsQualificationRequest
        @return: SubmitSmsQualificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_sms_qualification_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: dysmsapi_20170525_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.TagResourcesResponse:
        """
        @summary Attaches tags to a message template.
        
        @description ### QPS limit
        You can call this operation up to 50 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: dysmsapi_20170525_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.TagResourcesResponse:
        """
        @summary Attaches tags to a message template.
        
        @description ### QPS limit
        You can call this operation up to 50 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: dysmsapi_20170525_models.TagResourcesRequest,
    ) -> dysmsapi_20170525_models.TagResourcesResponse:
        """
        @summary Attaches tags to a message template.
        
        @description ### QPS limit
        You can call this operation up to 50 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: dysmsapi_20170525_models.TagResourcesRequest,
    ) -> dysmsapi_20170525_models.TagResourcesResponse:
        """
        @summary Attaches tags to a message template.
        
        @description ### QPS limit
        You can call this operation up to 50 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: dysmsapi_20170525_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.UntagResourcesResponse:
        """
        @summary Deletes tags from a message template.
        
        @description ### QPS limit
        You can call this operation up to 50 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: dysmsapi_20170525_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.UntagResourcesResponse:
        """
        @summary Deletes tags from a message template.
        
        @description ### QPS limit
        You can call this operation up to 50 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: dysmsapi_20170525_models.UntagResourcesRequest,
    ) -> dysmsapi_20170525_models.UntagResourcesResponse:
        """
        @summary Deletes tags from a message template.
        
        @description ### QPS limit
        You can call this operation up to 50 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: dysmsapi_20170525_models.UntagResourcesRequest,
    ) -> dysmsapi_20170525_models.UntagResourcesResponse:
        """
        @summary Deletes tags from a message template.
        
        @description ### QPS limit
        You can call this operation up to 50 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_ext_code_sign_with_options(
        self,
        request: dysmsapi_20170525_models.UpdateExtCodeSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.UpdateExtCodeSignResponse:
        """
        @summary 修改验证码签名
        
        @param request: UpdateExtCodeSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExtCodeSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.exist_ext_code):
            query['ExistExtCode'] = request.exist_ext_code
        if not UtilClient.is_unset(request.new_ext_code):
            query['NewExtCode'] = request.new_ext_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateExtCodeSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.UpdateExtCodeSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ext_code_sign_with_options_async(
        self,
        request: dysmsapi_20170525_models.UpdateExtCodeSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.UpdateExtCodeSignResponse:
        """
        @summary 修改验证码签名
        
        @param request: UpdateExtCodeSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExtCodeSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.exist_ext_code):
            query['ExistExtCode'] = request.exist_ext_code
        if not UtilClient.is_unset(request.new_ext_code):
            query['NewExtCode'] = request.new_ext_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateExtCodeSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.UpdateExtCodeSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ext_code_sign(
        self,
        request: dysmsapi_20170525_models.UpdateExtCodeSignRequest,
    ) -> dysmsapi_20170525_models.UpdateExtCodeSignResponse:
        """
        @summary 修改验证码签名
        
        @param request: UpdateExtCodeSignRequest
        @return: UpdateExtCodeSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_ext_code_sign_with_options(request, runtime)

    async def update_ext_code_sign_async(
        self,
        request: dysmsapi_20170525_models.UpdateExtCodeSignRequest,
    ) -> dysmsapi_20170525_models.UpdateExtCodeSignResponse:
        """
        @summary 修改验证码签名
        
        @param request: UpdateExtCodeSignRequest
        @return: UpdateExtCodeSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_ext_code_sign_with_options_async(request, runtime)

    def update_sms_qualification_with_options(
        self,
        tmp_req: dysmsapi_20170525_models.UpdateSmsQualificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.UpdateSmsQualificationResponse:
        """
        @summary 修改资质对客openAPI
        
        @param tmp_req: UpdateSmsQualificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSmsQualificationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysmsapi_20170525_models.UpdateSmsQualificationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.business_license_pics):
            request.business_license_pics_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.business_license_pics, 'BusinessLicensePics', 'json')
        if not UtilClient.is_unset(tmp_req.other_files):
            request.other_files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.other_files, 'OtherFiles', 'json')
        query = {}
        if not UtilClient.is_unset(request.admin_idcard_exp_date):
            query['AdminIDCardExpDate'] = request.admin_idcard_exp_date
        if not UtilClient.is_unset(request.admin_idcard_front_face):
            query['AdminIDCardFrontFace'] = request.admin_idcard_front_face
        if not UtilClient.is_unset(request.admin_idcard_no):
            query['AdminIDCardNo'] = request.admin_idcard_no
        if not UtilClient.is_unset(request.admin_idcard_pic):
            query['AdminIDCardPic'] = request.admin_idcard_pic
        if not UtilClient.is_unset(request.admin_idcard_type):
            query['AdminIDCardType'] = request.admin_idcard_type
        if not UtilClient.is_unset(request.admin_name):
            query['AdminName'] = request.admin_name
        if not UtilClient.is_unset(request.admin_phone_no):
            query['AdminPhoneNo'] = request.admin_phone_no
        if not UtilClient.is_unset(request.business_license_pics_shrink):
            query['BusinessLicensePics'] = request.business_license_pics_shrink
        if not UtilClient.is_unset(request.bussiness_license_exp_date):
            query['BussinessLicenseExpDate'] = request.bussiness_license_exp_date
        if not UtilClient.is_unset(request.certify_code):
            query['CertifyCode'] = request.certify_code
        if not UtilClient.is_unset(request.company_name):
            query['CompanyName'] = request.company_name
        if not UtilClient.is_unset(request.legal_person_idcard_no):
            query['LegalPersonIDCardNo'] = request.legal_person_idcard_no
        if not UtilClient.is_unset(request.legal_person_idcard_type):
            query['LegalPersonIDCardType'] = request.legal_person_idcard_type
        if not UtilClient.is_unset(request.legal_person_id_card_back_side):
            query['LegalPersonIdCardBackSide'] = request.legal_person_id_card_back_side
        if not UtilClient.is_unset(request.legal_person_id_card_eff_time):
            query['LegalPersonIdCardEffTime'] = request.legal_person_id_card_eff_time
        if not UtilClient.is_unset(request.legal_person_id_card_front_side):
            query['LegalPersonIdCardFrontSide'] = request.legal_person_id_card_front_side
        if not UtilClient.is_unset(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.other_files_shrink):
            query['OtherFiles'] = request.other_files_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_group_id):
            query['QualificationGroupId'] = request.qualification_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmsQualification',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.UpdateSmsQualificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sms_qualification_with_options_async(
        self,
        tmp_req: dysmsapi_20170525_models.UpdateSmsQualificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.UpdateSmsQualificationResponse:
        """
        @summary 修改资质对客openAPI
        
        @param tmp_req: UpdateSmsQualificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSmsQualificationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysmsapi_20170525_models.UpdateSmsQualificationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.business_license_pics):
            request.business_license_pics_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.business_license_pics, 'BusinessLicensePics', 'json')
        if not UtilClient.is_unset(tmp_req.other_files):
            request.other_files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.other_files, 'OtherFiles', 'json')
        query = {}
        if not UtilClient.is_unset(request.admin_idcard_exp_date):
            query['AdminIDCardExpDate'] = request.admin_idcard_exp_date
        if not UtilClient.is_unset(request.admin_idcard_front_face):
            query['AdminIDCardFrontFace'] = request.admin_idcard_front_face
        if not UtilClient.is_unset(request.admin_idcard_no):
            query['AdminIDCardNo'] = request.admin_idcard_no
        if not UtilClient.is_unset(request.admin_idcard_pic):
            query['AdminIDCardPic'] = request.admin_idcard_pic
        if not UtilClient.is_unset(request.admin_idcard_type):
            query['AdminIDCardType'] = request.admin_idcard_type
        if not UtilClient.is_unset(request.admin_name):
            query['AdminName'] = request.admin_name
        if not UtilClient.is_unset(request.admin_phone_no):
            query['AdminPhoneNo'] = request.admin_phone_no
        if not UtilClient.is_unset(request.business_license_pics_shrink):
            query['BusinessLicensePics'] = request.business_license_pics_shrink
        if not UtilClient.is_unset(request.bussiness_license_exp_date):
            query['BussinessLicenseExpDate'] = request.bussiness_license_exp_date
        if not UtilClient.is_unset(request.certify_code):
            query['CertifyCode'] = request.certify_code
        if not UtilClient.is_unset(request.company_name):
            query['CompanyName'] = request.company_name
        if not UtilClient.is_unset(request.legal_person_idcard_no):
            query['LegalPersonIDCardNo'] = request.legal_person_idcard_no
        if not UtilClient.is_unset(request.legal_person_idcard_type):
            query['LegalPersonIDCardType'] = request.legal_person_idcard_type
        if not UtilClient.is_unset(request.legal_person_id_card_back_side):
            query['LegalPersonIdCardBackSide'] = request.legal_person_id_card_back_side
        if not UtilClient.is_unset(request.legal_person_id_card_eff_time):
            query['LegalPersonIdCardEffTime'] = request.legal_person_id_card_eff_time
        if not UtilClient.is_unset(request.legal_person_id_card_front_side):
            query['LegalPersonIdCardFrontSide'] = request.legal_person_id_card_front_side
        if not UtilClient.is_unset(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.other_files_shrink):
            query['OtherFiles'] = request.other_files_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_group_id):
            query['QualificationGroupId'] = request.qualification_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmsQualification',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.UpdateSmsQualificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sms_qualification(
        self,
        request: dysmsapi_20170525_models.UpdateSmsQualificationRequest,
    ) -> dysmsapi_20170525_models.UpdateSmsQualificationResponse:
        """
        @summary 修改资质对客openAPI
        
        @param request: UpdateSmsQualificationRequest
        @return: UpdateSmsQualificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_sms_qualification_with_options(request, runtime)

    async def update_sms_qualification_async(
        self,
        request: dysmsapi_20170525_models.UpdateSmsQualificationRequest,
    ) -> dysmsapi_20170525_models.UpdateSmsQualificationResponse:
        """
        @summary 修改资质对客openAPI
        
        @param request: UpdateSmsQualificationRequest
        @return: UpdateSmsQualificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_sms_qualification_with_options_async(request, runtime)

    def update_sms_sign_with_options(
        self,
        tmp_req: dysmsapi_20170525_models.UpdateSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.UpdateSmsSignResponse:
        """
        @summary Update Text SMS Signature
        
        @description - For details about the changes of this new interface and the original one, please refer to [Announcement on the Update of SMS Signature & Template Interfaces](https://help.aliyun.com/zh/sms/product-overview/announcement-on-sms-service-update-signature-template-interface).
        - Only signatures that have not passed the review can be modified. Please refer to [Handling Suggestions for Failed SMS Reviews](https://help.aliyun.com/zh/sms/user-guide/causes-of-application-failures-and-suggestions?spm) and call this interface to modify and resubmit for review after modification.
        - Signature information applied through the interface will be synchronized in the SMS service console. For operations related to signatures in the console, please see [SMS Signatures](https://help.aliyun.com/zh/sms/user-guide/create-signatures?spm).
        
        @param tmp_req: UpdateSmsSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSmsSignResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysmsapi_20170525_models.UpdateSmsSignShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.more_data):
            request.more_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.more_data, 'MoreData', 'json')
        query = {}
        if not UtilClient.is_unset(request.apply_scene_content):
            query['ApplySceneContent'] = request.apply_scene_content
        if not UtilClient.is_unset(request.authorization_letter_id):
            query['AuthorizationLetterId'] = request.authorization_letter_id
        if not UtilClient.is_unset(request.more_data_shrink):
            query['MoreData'] = request.more_data_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sign_source):
            query['SignSource'] = request.sign_source
        if not UtilClient.is_unset(request.sign_type):
            query['SignType'] = request.sign_type
        if not UtilClient.is_unset(request.third_party):
            query['ThirdParty'] = request.third_party
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmsSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.UpdateSmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sms_sign_with_options_async(
        self,
        tmp_req: dysmsapi_20170525_models.UpdateSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.UpdateSmsSignResponse:
        """
        @summary Update Text SMS Signature
        
        @description - For details about the changes of this new interface and the original one, please refer to [Announcement on the Update of SMS Signature & Template Interfaces](https://help.aliyun.com/zh/sms/product-overview/announcement-on-sms-service-update-signature-template-interface).
        - Only signatures that have not passed the review can be modified. Please refer to [Handling Suggestions for Failed SMS Reviews](https://help.aliyun.com/zh/sms/user-guide/causes-of-application-failures-and-suggestions?spm) and call this interface to modify and resubmit for review after modification.
        - Signature information applied through the interface will be synchronized in the SMS service console. For operations related to signatures in the console, please see [SMS Signatures](https://help.aliyun.com/zh/sms/user-guide/create-signatures?spm).
        
        @param tmp_req: UpdateSmsSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSmsSignResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysmsapi_20170525_models.UpdateSmsSignShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.more_data):
            request.more_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.more_data, 'MoreData', 'json')
        query = {}
        if not UtilClient.is_unset(request.apply_scene_content):
            query['ApplySceneContent'] = request.apply_scene_content
        if not UtilClient.is_unset(request.authorization_letter_id):
            query['AuthorizationLetterId'] = request.authorization_letter_id
        if not UtilClient.is_unset(request.more_data_shrink):
            query['MoreData'] = request.more_data_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sign_source):
            query['SignSource'] = request.sign_source
        if not UtilClient.is_unset(request.sign_type):
            query['SignType'] = request.sign_type
        if not UtilClient.is_unset(request.third_party):
            query['ThirdParty'] = request.third_party
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmsSign',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.UpdateSmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sms_sign(
        self,
        request: dysmsapi_20170525_models.UpdateSmsSignRequest,
    ) -> dysmsapi_20170525_models.UpdateSmsSignResponse:
        """
        @summary Update Text SMS Signature
        
        @description - For details about the changes of this new interface and the original one, please refer to [Announcement on the Update of SMS Signature & Template Interfaces](https://help.aliyun.com/zh/sms/product-overview/announcement-on-sms-service-update-signature-template-interface).
        - Only signatures that have not passed the review can be modified. Please refer to [Handling Suggestions for Failed SMS Reviews](https://help.aliyun.com/zh/sms/user-guide/causes-of-application-failures-and-suggestions?spm) and call this interface to modify and resubmit for review after modification.
        - Signature information applied through the interface will be synchronized in the SMS service console. For operations related to signatures in the console, please see [SMS Signatures](https://help.aliyun.com/zh/sms/user-guide/create-signatures?spm).
        
        @param request: UpdateSmsSignRequest
        @return: UpdateSmsSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_sms_sign_with_options(request, runtime)

    async def update_sms_sign_async(
        self,
        request: dysmsapi_20170525_models.UpdateSmsSignRequest,
    ) -> dysmsapi_20170525_models.UpdateSmsSignResponse:
        """
        @summary Update Text SMS Signature
        
        @description - For details about the changes of this new interface and the original one, please refer to [Announcement on the Update of SMS Signature & Template Interfaces](https://help.aliyun.com/zh/sms/product-overview/announcement-on-sms-service-update-signature-template-interface).
        - Only signatures that have not passed the review can be modified. Please refer to [Handling Suggestions for Failed SMS Reviews](https://help.aliyun.com/zh/sms/user-guide/causes-of-application-failures-and-suggestions?spm) and call this interface to modify and resubmit for review after modification.
        - Signature information applied through the interface will be synchronized in the SMS service console. For operations related to signatures in the console, please see [SMS Signatures](https://help.aliyun.com/zh/sms/user-guide/create-signatures?spm).
        
        @param request: UpdateSmsSignRequest
        @return: UpdateSmsSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_sms_sign_with_options_async(request, runtime)

    def update_sms_template_with_options(
        self,
        tmp_req: dysmsapi_20170525_models.UpdateSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.UpdateSmsTemplateResponse:
        """
        @summary Update Text SMS Template
        
        @description - For details about the changes of this new interface compared to the original one, please refer to [Announcement on SMS Service Update: Signature & Template Interfaces](https://help.aliyun.com/zh/sms/product-overview/announcement-on-sms-service-update-signature-template-interface).
        - Only templates that have not passed the review can be modified. Please refer to [Handling Suggestions for Failed SMS Template Reviews](https://help.aliyun.com/zh/sms/user-guide/causes-of-application-failures-and-suggestions?spm=a2c4g.11186623.0.0.4bf5561ajcFtMQ) and call this interface to modify and resubmit for review.
        - Modifications made through the interface will be synchronized in the SMS service console. For related operations on templates in the console, see [SMS Templates](https://help.aliyun.com/zh/sms/user-guide/message-templates/?spm=a2c4g.11186623.0.0.35a947464Itaxp).
        ### QPS Limit
        The single-user QPS limit for this interface is 1000 times/second. Exceeding this limit will result in API throttling, which may impact your business. Please make calls reasonably.
        
        @param tmp_req: UpdateSmsTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSmsTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysmsapi_20170525_models.UpdateSmsTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.more_data):
            request.more_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.more_data, 'MoreData', 'json')
        query = {}
        if not UtilClient.is_unset(request.apply_scene_content):
            query['ApplySceneContent'] = request.apply_scene_content
        if not UtilClient.is_unset(request.intl_type):
            query['IntlType'] = request.intl_type
        if not UtilClient.is_unset(request.more_data_shrink):
            query['MoreData'] = request.more_data_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.related_sign_name):
            query['RelatedSignName'] = request.related_sign_name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_content):
            query['TemplateContent'] = request.template_content
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_rule):
            query['TemplateRule'] = request.template_rule
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        if not UtilClient.is_unset(request.traffic_driving):
            query['TrafficDriving'] = request.traffic_driving
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.UpdateSmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sms_template_with_options_async(
        self,
        tmp_req: dysmsapi_20170525_models.UpdateSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.UpdateSmsTemplateResponse:
        """
        @summary Update Text SMS Template
        
        @description - For details about the changes of this new interface compared to the original one, please refer to [Announcement on SMS Service Update: Signature & Template Interfaces](https://help.aliyun.com/zh/sms/product-overview/announcement-on-sms-service-update-signature-template-interface).
        - Only templates that have not passed the review can be modified. Please refer to [Handling Suggestions for Failed SMS Template Reviews](https://help.aliyun.com/zh/sms/user-guide/causes-of-application-failures-and-suggestions?spm=a2c4g.11186623.0.0.4bf5561ajcFtMQ) and call this interface to modify and resubmit for review.
        - Modifications made through the interface will be synchronized in the SMS service console. For related operations on templates in the console, see [SMS Templates](https://help.aliyun.com/zh/sms/user-guide/message-templates/?spm=a2c4g.11186623.0.0.35a947464Itaxp).
        ### QPS Limit
        The single-user QPS limit for this interface is 1000 times/second. Exceeding this limit will result in API throttling, which may impact your business. Please make calls reasonably.
        
        @param tmp_req: UpdateSmsTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSmsTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysmsapi_20170525_models.UpdateSmsTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.more_data):
            request.more_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.more_data, 'MoreData', 'json')
        query = {}
        if not UtilClient.is_unset(request.apply_scene_content):
            query['ApplySceneContent'] = request.apply_scene_content
        if not UtilClient.is_unset(request.intl_type):
            query['IntlType'] = request.intl_type
        if not UtilClient.is_unset(request.more_data_shrink):
            query['MoreData'] = request.more_data_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.related_sign_name):
            query['RelatedSignName'] = request.related_sign_name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_content):
            query['TemplateContent'] = request.template_content
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_rule):
            query['TemplateRule'] = request.template_rule
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        if not UtilClient.is_unset(request.traffic_driving):
            query['TrafficDriving'] = request.traffic_driving
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmsTemplate',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.UpdateSmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sms_template(
        self,
        request: dysmsapi_20170525_models.UpdateSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.UpdateSmsTemplateResponse:
        """
        @summary Update Text SMS Template
        
        @description - For details about the changes of this new interface compared to the original one, please refer to [Announcement on SMS Service Update: Signature & Template Interfaces](https://help.aliyun.com/zh/sms/product-overview/announcement-on-sms-service-update-signature-template-interface).
        - Only templates that have not passed the review can be modified. Please refer to [Handling Suggestions for Failed SMS Template Reviews](https://help.aliyun.com/zh/sms/user-guide/causes-of-application-failures-and-suggestions?spm=a2c4g.11186623.0.0.4bf5561ajcFtMQ) and call this interface to modify and resubmit for review.
        - Modifications made through the interface will be synchronized in the SMS service console. For related operations on templates in the console, see [SMS Templates](https://help.aliyun.com/zh/sms/user-guide/message-templates/?spm=a2c4g.11186623.0.0.35a947464Itaxp).
        ### QPS Limit
        The single-user QPS limit for this interface is 1000 times/second. Exceeding this limit will result in API throttling, which may impact your business. Please make calls reasonably.
        
        @param request: UpdateSmsTemplateRequest
        @return: UpdateSmsTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_sms_template_with_options(request, runtime)

    async def update_sms_template_async(
        self,
        request: dysmsapi_20170525_models.UpdateSmsTemplateRequest,
    ) -> dysmsapi_20170525_models.UpdateSmsTemplateResponse:
        """
        @summary Update Text SMS Template
        
        @description - For details about the changes of this new interface compared to the original one, please refer to [Announcement on SMS Service Update: Signature & Template Interfaces](https://help.aliyun.com/zh/sms/product-overview/announcement-on-sms-service-update-signature-template-interface).
        - Only templates that have not passed the review can be modified. Please refer to [Handling Suggestions for Failed SMS Template Reviews](https://help.aliyun.com/zh/sms/user-guide/causes-of-application-failures-and-suggestions?spm=a2c4g.11186623.0.0.4bf5561ajcFtMQ) and call this interface to modify and resubmit for review.
        - Modifications made through the interface will be synchronized in the SMS service console. For related operations on templates in the console, see [SMS Templates](https://help.aliyun.com/zh/sms/user-guide/message-templates/?spm=a2c4g.11186623.0.0.35a947464Itaxp).
        ### QPS Limit
        The single-user QPS limit for this interface is 1000 times/second. Exceeding this limit will result in API throttling, which may impact your business. Please make calls reasonably.
        
        @param request: UpdateSmsTemplateRequest
        @return: UpdateSmsTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_sms_template_with_options_async(request, runtime)

    def valid_phone_code_with_options(
        self,
        request: dysmsapi_20170525_models.ValidPhoneCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.ValidPhoneCodeResponse:
        """
        @summary 发送手机验证码
        
        @param request: ValidPhoneCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidPhoneCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certify_code):
            query['CertifyCode'] = request.certify_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no):
            query['PhoneNo'] = request.phone_no
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidPhoneCode',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.ValidPhoneCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def valid_phone_code_with_options_async(
        self,
        request: dysmsapi_20170525_models.ValidPhoneCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.ValidPhoneCodeResponse:
        """
        @summary 发送手机验证码
        
        @param request: ValidPhoneCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidPhoneCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certify_code):
            query['CertifyCode'] = request.certify_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no):
            query['PhoneNo'] = request.phone_no
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidPhoneCode',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.ValidPhoneCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def valid_phone_code(
        self,
        request: dysmsapi_20170525_models.ValidPhoneCodeRequest,
    ) -> dysmsapi_20170525_models.ValidPhoneCodeResponse:
        """
        @summary 发送手机验证码
        
        @param request: ValidPhoneCodeRequest
        @return: ValidPhoneCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.valid_phone_code_with_options(request, runtime)

    async def valid_phone_code_async(
        self,
        request: dysmsapi_20170525_models.ValidPhoneCodeRequest,
    ) -> dysmsapi_20170525_models.ValidPhoneCodeResponse:
        """
        @summary 发送手机验证码
        
        @param request: ValidPhoneCodeRequest
        @return: ValidPhoneCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.valid_phone_code_with_options_async(request, runtime)

    def verify_logistics_sms_mail_no_with_options(
        self,
        request: dysmsapi_20170525_models.VerifyLogisticsSmsMailNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.VerifyLogisticsSmsMailNoResponse:
        """
        @summary 物流短信运单号校验
        
        @param request: VerifyLogisticsSmsMailNoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyLogisticsSmsMailNoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.express_company_code):
            query['ExpressCompanyCode'] = request.express_company_code
        if not UtilClient.is_unset(request.mail_no):
            query['MailNo'] = request.mail_no
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.platform_company_code):
            query['PlatformCompanyCode'] = request.platform_company_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyLogisticsSmsMailNo',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.VerifyLogisticsSmsMailNoResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_logistics_sms_mail_no_with_options_async(
        self,
        request: dysmsapi_20170525_models.VerifyLogisticsSmsMailNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysmsapi_20170525_models.VerifyLogisticsSmsMailNoResponse:
        """
        @summary 物流短信运单号校验
        
        @param request: VerifyLogisticsSmsMailNoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyLogisticsSmsMailNoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.express_company_code):
            query['ExpressCompanyCode'] = request.express_company_code
        if not UtilClient.is_unset(request.mail_no):
            query['MailNo'] = request.mail_no
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.platform_company_code):
            query['PlatformCompanyCode'] = request.platform_company_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyLogisticsSmsMailNo',
            version='2017-05-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.VerifyLogisticsSmsMailNoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_logistics_sms_mail_no(
        self,
        request: dysmsapi_20170525_models.VerifyLogisticsSmsMailNoRequest,
    ) -> dysmsapi_20170525_models.VerifyLogisticsSmsMailNoResponse:
        """
        @summary 物流短信运单号校验
        
        @param request: VerifyLogisticsSmsMailNoRequest
        @return: VerifyLogisticsSmsMailNoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_logistics_sms_mail_no_with_options(request, runtime)

    async def verify_logistics_sms_mail_no_async(
        self,
        request: dysmsapi_20170525_models.VerifyLogisticsSmsMailNoRequest,
    ) -> dysmsapi_20170525_models.VerifyLogisticsSmsMailNoResponse:
        """
        @summary 物流短信运单号校验
        
        @param request: VerifyLogisticsSmsMailNoRequest
        @return: VerifyLogisticsSmsMailNoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_logistics_sms_mail_no_with_options_async(request, runtime)
