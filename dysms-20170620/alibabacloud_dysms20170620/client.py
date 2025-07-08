# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dysms20170620 import models as dysms_20170620_models
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
        self._endpoint = self.get_endpoint('dysms', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_domain_with_options(
        self,
        request: dysms_20170620_models.AddDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.AddDomainResponse:
        """
        @param request: AddDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
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
            action='AddDomain',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.AddDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_domain_with_options_async(
        self,
        request: dysms_20170620_models.AddDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.AddDomainResponse:
        """
        @param request: AddDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
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
            action='AddDomain',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.AddDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_domain(
        self,
        request: dysms_20170620_models.AddDomainRequest,
    ) -> dysms_20170620_models.AddDomainResponse:
        """
        @param request: AddDomainRequest
        @return: AddDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_domain_with_options(request, runtime)

    async def add_domain_async(
        self,
        request: dysms_20170620_models.AddDomainRequest,
    ) -> dysms_20170620_models.AddDomainResponse:
        """
        @param request: AddDomainRequest
        @return: AddDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_domain_with_options_async(request, runtime)

    def add_domain_new_with_options(
        self,
        request: dysms_20170620_models.AddDomainNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.AddDomainNewResponse:
        """
        @param request: AddDomainNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDomainNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDomainNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.AddDomainNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_domain_new_with_options_async(
        self,
        request: dysms_20170620_models.AddDomainNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.AddDomainNewResponse:
        """
        @param request: AddDomainNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDomainNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDomainNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.AddDomainNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_domain_new(
        self,
        request: dysms_20170620_models.AddDomainNewRequest,
    ) -> dysms_20170620_models.AddDomainNewResponse:
        """
        @param request: AddDomainNewRequest
        @return: AddDomainNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_domain_new_with_options(request, runtime)

    async def add_domain_new_async(
        self,
        request: dysms_20170620_models.AddDomainNewRequest,
    ) -> dysms_20170620_models.AddDomainNewResponse:
        """
        @param request: AddDomainNewRequest
        @return: AddDomainNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_domain_new_with_options_async(request, runtime)

    def apply_export_sms_send_record_new_with_options(
        self,
        request: dysms_20170620_models.ApplyExportSmsSendRecordNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.ApplyExportSmsSendRecordNewResponse:
        """
        @param request: ApplyExportSmsSendRecordNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyExportSmsSendRecordNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.error_code):
            query['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.real_time_data_flag):
            query['RealTimeDataFlag'] = request.real_time_data_flag
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_date):
            query['SendDate'] = request.send_date
        if not UtilClient.is_unset(request.send_status):
            query['SendStatus'] = request.send_status
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyExportSmsSendRecordNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.ApplyExportSmsSendRecordNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_export_sms_send_record_new_with_options_async(
        self,
        request: dysms_20170620_models.ApplyExportSmsSendRecordNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.ApplyExportSmsSendRecordNewResponse:
        """
        @param request: ApplyExportSmsSendRecordNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyExportSmsSendRecordNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.error_code):
            query['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.real_time_data_flag):
            query['RealTimeDataFlag'] = request.real_time_data_flag
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_date):
            query['SendDate'] = request.send_date
        if not UtilClient.is_unset(request.send_status):
            query['SendStatus'] = request.send_status
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyExportSmsSendRecordNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.ApplyExportSmsSendRecordNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_export_sms_send_record_new(
        self,
        request: dysms_20170620_models.ApplyExportSmsSendRecordNewRequest,
    ) -> dysms_20170620_models.ApplyExportSmsSendRecordNewResponse:
        """
        @param request: ApplyExportSmsSendRecordNewRequest
        @return: ApplyExportSmsSendRecordNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.apply_export_sms_send_record_new_with_options(request, runtime)

    async def apply_export_sms_send_record_new_async(
        self,
        request: dysms_20170620_models.ApplyExportSmsSendRecordNewRequest,
    ) -> dysms_20170620_models.ApplyExportSmsSendRecordNewResponse:
        """
        @param request: ApplyExportSmsSendRecordNewRequest
        @return: ApplyExportSmsSendRecordNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.apply_export_sms_send_record_new_with_options_async(request, runtime)

    def batch_create_sms_sign_with_options(
        self,
        tmp_req: dysms_20170620_models.BatchCreateSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.BatchCreateSmsSignResponse:
        """
        @summary 批量创建签名
        
        @param tmp_req: BatchCreateSmsSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCreateSmsSignResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysms_20170620_models.BatchCreateSmsSignShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.column_index_mapping_rule):
            request.column_index_mapping_rule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.column_index_mapping_rule, 'ColumnIndexMappingRule', 'json')
        if not UtilClient.is_unset(tmp_req.more_data):
            request.more_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.more_data, 'MoreData', 'json')
        query = {}
        if not UtilClient.is_unset(request.column_index_mapping_rule_shrink):
            query['ColumnIndexMappingRule'] = request.column_index_mapping_rule_shrink
        if not UtilClient.is_unset(request.extend_message):
            query['ExtendMessage'] = request.extend_message
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.more_data_shrink):
            query['MoreData'] = request.more_data_shrink
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.oss_keys):
            query['OssKeys'] = request.oss_keys
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.sign_oss_key):
            query['SignOssKey'] = request.sign_oss_key
        if not UtilClient.is_unset(request.user_view_file_name):
            query['UserViewFileName'] = request.user_view_file_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchCreateSmsSign',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.BatchCreateSmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_create_sms_sign_with_options_async(
        self,
        tmp_req: dysms_20170620_models.BatchCreateSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.BatchCreateSmsSignResponse:
        """
        @summary 批量创建签名
        
        @param tmp_req: BatchCreateSmsSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCreateSmsSignResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysms_20170620_models.BatchCreateSmsSignShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.column_index_mapping_rule):
            request.column_index_mapping_rule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.column_index_mapping_rule, 'ColumnIndexMappingRule', 'json')
        if not UtilClient.is_unset(tmp_req.more_data):
            request.more_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.more_data, 'MoreData', 'json')
        query = {}
        if not UtilClient.is_unset(request.column_index_mapping_rule_shrink):
            query['ColumnIndexMappingRule'] = request.column_index_mapping_rule_shrink
        if not UtilClient.is_unset(request.extend_message):
            query['ExtendMessage'] = request.extend_message
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.more_data_shrink):
            query['MoreData'] = request.more_data_shrink
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.oss_keys):
            query['OssKeys'] = request.oss_keys
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.sign_oss_key):
            query['SignOssKey'] = request.sign_oss_key
        if not UtilClient.is_unset(request.user_view_file_name):
            query['UserViewFileName'] = request.user_view_file_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchCreateSmsSign',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.BatchCreateSmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_create_sms_sign(
        self,
        request: dysms_20170620_models.BatchCreateSmsSignRequest,
    ) -> dysms_20170620_models.BatchCreateSmsSignResponse:
        """
        @summary 批量创建签名
        
        @param request: BatchCreateSmsSignRequest
        @return: BatchCreateSmsSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_create_sms_sign_with_options(request, runtime)

    async def batch_create_sms_sign_async(
        self,
        request: dysms_20170620_models.BatchCreateSmsSignRequest,
    ) -> dysms_20170620_models.BatchCreateSmsSignResponse:
        """
        @summary 批量创建签名
        
        @param request: BatchCreateSmsSignRequest
        @return: BatchCreateSmsSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_create_sms_sign_with_options_async(request, runtime)

    def batch_delete_export_send_record_new_with_options(
        self,
        request: dysms_20170620_models.BatchDeleteExportSendRecordNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.BatchDeleteExportSendRecordNewResponse:
        """
        @param request: BatchDeleteExportSendRecordNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteExportSendRecordNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteExportSendRecordNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.BatchDeleteExportSendRecordNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_export_send_record_new_with_options_async(
        self,
        request: dysms_20170620_models.BatchDeleteExportSendRecordNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.BatchDeleteExportSendRecordNewResponse:
        """
        @param request: BatchDeleteExportSendRecordNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteExportSendRecordNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteExportSendRecordNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.BatchDeleteExportSendRecordNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_export_send_record_new(
        self,
        request: dysms_20170620_models.BatchDeleteExportSendRecordNewRequest,
    ) -> dysms_20170620_models.BatchDeleteExportSendRecordNewResponse:
        """
        @param request: BatchDeleteExportSendRecordNewRequest
        @return: BatchDeleteExportSendRecordNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_export_send_record_new_with_options(request, runtime)

    async def batch_delete_export_send_record_new_async(
        self,
        request: dysms_20170620_models.BatchDeleteExportSendRecordNewRequest,
    ) -> dysms_20170620_models.BatchDeleteExportSendRecordNewResponse:
        """
        @param request: BatchDeleteExportSendRecordNewRequest
        @return: BatchDeleteExportSendRecordNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_export_send_record_new_with_options_async(request, runtime)

    def batch_delete_task_new_with_options(
        self,
        request: dysms_20170620_models.BatchDeleteTaskNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.BatchDeleteTaskNewResponse:
        """
        @param request: BatchDeleteTaskNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteTaskNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteTaskNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.BatchDeleteTaskNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_task_new_with_options_async(
        self,
        request: dysms_20170620_models.BatchDeleteTaskNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.BatchDeleteTaskNewResponse:
        """
        @param request: BatchDeleteTaskNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteTaskNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteTaskNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.BatchDeleteTaskNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_task_new(
        self,
        request: dysms_20170620_models.BatchDeleteTaskNewRequest,
    ) -> dysms_20170620_models.BatchDeleteTaskNewResponse:
        """
        @param request: BatchDeleteTaskNewRequest
        @return: BatchDeleteTaskNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_task_new_with_options(request, runtime)

    async def batch_delete_task_new_async(
        self,
        request: dysms_20170620_models.BatchDeleteTaskNewRequest,
    ) -> dysms_20170620_models.BatchDeleteTaskNewResponse:
        """
        @param request: BatchDeleteTaskNewRequest
        @return: BatchDeleteTaskNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_task_new_with_options_async(request, runtime)

    def calculate_sms_length_new_with_options(
        self,
        request: dysms_20170620_models.CalculateSmsLengthNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CalculateSmsLengthNewResponse:
        """
        @param request: CalculateSmsLengthNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CalculateSmsLengthNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sms_content):
            query['SmsContent'] = request.sms_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CalculateSmsLengthNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CalculateSmsLengthNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def calculate_sms_length_new_with_options_async(
        self,
        request: dysms_20170620_models.CalculateSmsLengthNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CalculateSmsLengthNewResponse:
        """
        @param request: CalculateSmsLengthNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CalculateSmsLengthNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sms_content):
            query['SmsContent'] = request.sms_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CalculateSmsLengthNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CalculateSmsLengthNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def calculate_sms_length_new(
        self,
        request: dysms_20170620_models.CalculateSmsLengthNewRequest,
    ) -> dysms_20170620_models.CalculateSmsLengthNewResponse:
        """
        @param request: CalculateSmsLengthNewRequest
        @return: CalculateSmsLengthNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.calculate_sms_length_new_with_options(request, runtime)

    async def calculate_sms_length_new_async(
        self,
        request: dysms_20170620_models.CalculateSmsLengthNewRequest,
    ) -> dysms_20170620_models.CalculateSmsLengthNewResponse:
        """
        @param request: CalculateSmsLengthNewRequest
        @return: CalculateSmsLengthNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.calculate_sms_length_new_with_options_async(request, runtime)

    def cancel_sms_sign_with_options(
        self,
        request: dysms_20170620_models.CancelSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CancelSmsSignResponse:
        """
        @summary 签名取消审核
        
        @param request: CancelSmsSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelSmsSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.signature_code):
            query['SignatureCode'] = request.signature_code
        if not UtilClient.is_unset(request.signature_id):
            query['SignatureId'] = request.signature_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelSmsSign',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CancelSmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_sms_sign_with_options_async(
        self,
        request: dysms_20170620_models.CancelSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CancelSmsSignResponse:
        """
        @summary 签名取消审核
        
        @param request: CancelSmsSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelSmsSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.signature_code):
            query['SignatureCode'] = request.signature_code
        if not UtilClient.is_unset(request.signature_id):
            query['SignatureId'] = request.signature_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelSmsSign',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CancelSmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_sms_sign(
        self,
        request: dysms_20170620_models.CancelSmsSignRequest,
    ) -> dysms_20170620_models.CancelSmsSignResponse:
        """
        @summary 签名取消审核
        
        @param request: CancelSmsSignRequest
        @return: CancelSmsSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_sms_sign_with_options(request, runtime)

    async def cancel_sms_sign_async(
        self,
        request: dysms_20170620_models.CancelSmsSignRequest,
    ) -> dysms_20170620_models.CancelSmsSignResponse:
        """
        @summary 签名取消审核
        
        @param request: CancelSmsSignRequest
        @return: CancelSmsSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_sms_sign_with_options_async(request, runtime)

    def cancel_sms_template_with_options(
        self,
        request: dysms_20170620_models.CancelSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CancelSmsTemplateResponse:
        """
        @param request: CancelSmsTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelSmsTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
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
            action='CancelSmsTemplate',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CancelSmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_sms_template_with_options_async(
        self,
        request: dysms_20170620_models.CancelSmsTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CancelSmsTemplateResponse:
        """
        @param request: CancelSmsTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelSmsTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
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
            action='CancelSmsTemplate',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CancelSmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_sms_template(
        self,
        request: dysms_20170620_models.CancelSmsTemplateRequest,
    ) -> dysms_20170620_models.CancelSmsTemplateResponse:
        """
        @param request: CancelSmsTemplateRequest
        @return: CancelSmsTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_sms_template_with_options(request, runtime)

    async def cancel_sms_template_async(
        self,
        request: dysms_20170620_models.CancelSmsTemplateRequest,
    ) -> dysms_20170620_models.CancelSmsTemplateResponse:
        """
        @param request: CancelSmsTemplateRequest
        @return: CancelSmsTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_sms_template_with_options_async(request, runtime)

    def cancel_sms_template_new_with_options(
        self,
        request: dysms_20170620_models.CancelSmsTemplateNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CancelSmsTemplateNewResponse:
        """
        @param request: CancelSmsTemplateNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelSmsTemplateNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.intelligent_approval):
            query['IntelligentApproval'] = request.intelligent_approval
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
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
            action='CancelSmsTemplateNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CancelSmsTemplateNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_sms_template_new_with_options_async(
        self,
        request: dysms_20170620_models.CancelSmsTemplateNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CancelSmsTemplateNewResponse:
        """
        @param request: CancelSmsTemplateNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelSmsTemplateNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.intelligent_approval):
            query['IntelligentApproval'] = request.intelligent_approval
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
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
            action='CancelSmsTemplateNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CancelSmsTemplateNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_sms_template_new(
        self,
        request: dysms_20170620_models.CancelSmsTemplateNewRequest,
    ) -> dysms_20170620_models.CancelSmsTemplateNewResponse:
        """
        @param request: CancelSmsTemplateNewRequest
        @return: CancelSmsTemplateNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_sms_template_new_with_options(request, runtime)

    async def cancel_sms_template_new_async(
        self,
        request: dysms_20170620_models.CancelSmsTemplateNewRequest,
    ) -> dysms_20170620_models.CancelSmsTemplateNewResponse:
        """
        @param request: CancelSmsTemplateNewRequest
        @return: CancelSmsTemplateNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_sms_template_new_with_options_async(request, runtime)

    def check_sms_sign_new_with_options(
        self,
        request: dysms_20170620_models.CheckSmsSignNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CheckSmsSignNewResponse:
        """
        @param request: CheckSmsSignNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckSmsSignNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckSmsSignNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CheckSmsSignNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_sms_sign_new_with_options_async(
        self,
        request: dysms_20170620_models.CheckSmsSignNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CheckSmsSignNewResponse:
        """
        @param request: CheckSmsSignNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckSmsSignNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckSmsSignNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CheckSmsSignNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_sms_sign_new(
        self,
        request: dysms_20170620_models.CheckSmsSignNewRequest,
    ) -> dysms_20170620_models.CheckSmsSignNewResponse:
        """
        @param request: CheckSmsSignNewRequest
        @return: CheckSmsSignNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_sms_sign_new_with_options(request, runtime)

    async def check_sms_sign_new_async(
        self,
        request: dysms_20170620_models.CheckSmsSignNewRequest,
    ) -> dysms_20170620_models.CheckSmsSignNewResponse:
        """
        @param request: CheckSmsSignNewRequest
        @return: CheckSmsSignNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_sms_sign_new_with_options_async(request, runtime)

    def create_alicom_product_with_options(
        self,
        request: dysms_20170620_models.CreateAlicomProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateAlicomProductResponse:
        """
        @param request: CreateAlicomProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAlicomProductResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bus_offer):
            query['BusOffer'] = request.bus_offer
        if not UtilClient.is_unset(request.bus_offers):
            query['BusOffers'] = request.bus_offers
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAlicomProduct',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateAlicomProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alicom_product_with_options_async(
        self,
        request: dysms_20170620_models.CreateAlicomProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateAlicomProductResponse:
        """
        @param request: CreateAlicomProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAlicomProductResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bus_offer):
            query['BusOffer'] = request.bus_offer
        if not UtilClient.is_unset(request.bus_offers):
            query['BusOffers'] = request.bus_offers
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAlicomProduct',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateAlicomProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alicom_product(
        self,
        request: dysms_20170620_models.CreateAlicomProductRequest,
    ) -> dysms_20170620_models.CreateAlicomProductResponse:
        """
        @param request: CreateAlicomProductRequest
        @return: CreateAlicomProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_alicom_product_with_options(request, runtime)

    async def create_alicom_product_async(
        self,
        request: dysms_20170620_models.CreateAlicomProductRequest,
    ) -> dysms_20170620_models.CreateAlicomProductResponse:
        """
        @param request: CreateAlicomProductRequest
        @return: CreateAlicomProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_alicom_product_with_options_async(request, runtime)

    def create_authorization_with_options(
        self,
        request: dysms_20170620_models.CreateAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateAuthorizationResponse:
        """
        @summary 创建授权
        
        @param request: CreateAuthorizationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAuthorizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorize_code):
            query['AuthorizeCode'] = request.authorize_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAuthorization',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_authorization_with_options_async(
        self,
        request: dysms_20170620_models.CreateAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateAuthorizationResponse:
        """
        @summary 创建授权
        
        @param request: CreateAuthorizationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAuthorizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorize_code):
            query['AuthorizeCode'] = request.authorize_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAuthorization',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_authorization(
        self,
        request: dysms_20170620_models.CreateAuthorizationRequest,
    ) -> dysms_20170620_models.CreateAuthorizationResponse:
        """
        @summary 创建授权
        
        @param request: CreateAuthorizationRequest
        @return: CreateAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_authorization_with_options(request, runtime)

    async def create_authorization_async(
        self,
        request: dysms_20170620_models.CreateAuthorizationRequest,
    ) -> dysms_20170620_models.CreateAuthorizationResponse:
        """
        @summary 创建授权
        
        @param request: CreateAuthorizationRequest
        @return: CreateAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_authorization_with_options_async(request, runtime)

    def create_card_message_callback_with_options(
        self,
        request: dysms_20170620_models.CreateCardMessageCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateCardMessageCallbackResponse:
        """
        @summary 创建消息回调
        
        @param request: CreateCardMessageCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCardMessageCallbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCardMessageCallback',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateCardMessageCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_card_message_callback_with_options_async(
        self,
        request: dysms_20170620_models.CreateCardMessageCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateCardMessageCallbackResponse:
        """
        @summary 创建消息回调
        
        @param request: CreateCardMessageCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCardMessageCallbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCardMessageCallback',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateCardMessageCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_card_message_callback(
        self,
        request: dysms_20170620_models.CreateCardMessageCallbackRequest,
    ) -> dysms_20170620_models.CreateCardMessageCallbackResponse:
        """
        @summary 创建消息回调
        
        @param request: CreateCardMessageCallbackRequest
        @return: CreateCardMessageCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_card_message_callback_with_options(request, runtime)

    async def create_card_message_callback_async(
        self,
        request: dysms_20170620_models.CreateCardMessageCallbackRequest,
    ) -> dysms_20170620_models.CreateCardMessageCallbackResponse:
        """
        @summary 创建消息回调
        
        @param request: CreateCardMessageCallbackRequest
        @return: CreateCardMessageCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_card_message_callback_with_options_async(request, runtime)

    def create_card_message_queue_with_options(
        self,
        request: dysms_20170620_models.CreateCardMessageQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateCardMessageQueueResponse:
        """
        @summary 创建mns
        
        @param request: CreateCardMessageQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCardMessageQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.queue_type):
            query['QueueType'] = request.queue_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCardMessageQueue',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateCardMessageQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_card_message_queue_with_options_async(
        self,
        request: dysms_20170620_models.CreateCardMessageQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateCardMessageQueueResponse:
        """
        @summary 创建mns
        
        @param request: CreateCardMessageQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCardMessageQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.queue_type):
            query['QueueType'] = request.queue_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCardMessageQueue',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateCardMessageQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_card_message_queue(
        self,
        request: dysms_20170620_models.CreateCardMessageQueueRequest,
    ) -> dysms_20170620_models.CreateCardMessageQueueResponse:
        """
        @summary 创建mns
        
        @param request: CreateCardMessageQueueRequest
        @return: CreateCardMessageQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_card_message_queue_with_options(request, runtime)

    async def create_card_message_queue_async(
        self,
        request: dysms_20170620_models.CreateCardMessageQueueRequest,
    ) -> dysms_20170620_models.CreateCardMessageQueueResponse:
        """
        @summary 创建mns
        
        @param request: CreateCardMessageQueueRequest
        @return: CreateCardMessageQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_card_message_queue_with_options_async(request, runtime)

    def create_digital_sms_template_new_with_options(
        self,
        request: dysms_20170620_models.CreateDigitalSmsTemplateNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateDigitalSmsTemplateNewResponse:
        """
        @param request: CreateDigitalSmsTemplateNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDigitalSmsTemplateNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.content_oss_keys):
            query['ContentOssKeys'] = request.content_oss_keys
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDigitalSmsTemplateNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateDigitalSmsTemplateNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_digital_sms_template_new_with_options_async(
        self,
        request: dysms_20170620_models.CreateDigitalSmsTemplateNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateDigitalSmsTemplateNewResponse:
        """
        @param request: CreateDigitalSmsTemplateNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDigitalSmsTemplateNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.content_oss_keys):
            query['ContentOssKeys'] = request.content_oss_keys
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDigitalSmsTemplateNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateDigitalSmsTemplateNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_digital_sms_template_new(
        self,
        request: dysms_20170620_models.CreateDigitalSmsTemplateNewRequest,
    ) -> dysms_20170620_models.CreateDigitalSmsTemplateNewResponse:
        """
        @param request: CreateDigitalSmsTemplateNewRequest
        @return: CreateDigitalSmsTemplateNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_digital_sms_template_new_with_options(request, runtime)

    async def create_digital_sms_template_new_async(
        self,
        request: dysms_20170620_models.CreateDigitalSmsTemplateNewRequest,
    ) -> dysms_20170620_models.CreateDigitalSmsTemplateNewResponse:
        """
        @param request: CreateDigitalSmsTemplateNewRequest
        @return: CreateDigitalSmsTemplateNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_digital_sms_template_new_with_options_async(request, runtime)

    def create_file_by_biz_with_options(
        self,
        request: dysms_20170620_models.CreateFileByBizRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateFileByBizResponse:
        """
        @deprecated OpenAPI CreateFileByBiz is deprecated
        
        @param request: CreateFileByBizRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFileByBizResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFileByBiz',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateFileByBizResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_file_by_biz_with_options_async(
        self,
        request: dysms_20170620_models.CreateFileByBizRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateFileByBizResponse:
        """
        @deprecated OpenAPI CreateFileByBiz is deprecated
        
        @param request: CreateFileByBizRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFileByBizResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFileByBiz',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateFileByBizResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_file_by_biz(
        self,
        request: dysms_20170620_models.CreateFileByBizRequest,
    ) -> dysms_20170620_models.CreateFileByBizResponse:
        """
        @deprecated OpenAPI CreateFileByBiz is deprecated
        
        @param request: CreateFileByBizRequest
        @return: CreateFileByBizResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.create_file_by_biz_with_options(request, runtime)

    async def create_file_by_biz_async(
        self,
        request: dysms_20170620_models.CreateFileByBizRequest,
    ) -> dysms_20170620_models.CreateFileByBizResponse:
        """
        @deprecated OpenAPI CreateFileByBiz is deprecated
        
        @param request: CreateFileByBizRequest
        @return: CreateFileByBizResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_file_by_biz_with_options_async(request, runtime)

    def create_flow_limit_with_options(
        self,
        request: dysms_20170620_models.CreateFlowLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateFlowLimitResponse:
        """
        @param request: CreateFlowLimitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFlowLimitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.daily_limit):
            query['DailyLimit'] = request.daily_limit
        if not UtilClient.is_unset(request.hour_limit):
            query['HourLimit'] = request.hour_limit
        if not UtilClient.is_unset(request.minute_limit):
            query['MinuteLimit'] = request.minute_limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowLimit',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateFlowLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_limit_with_options_async(
        self,
        request: dysms_20170620_models.CreateFlowLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateFlowLimitResponse:
        """
        @param request: CreateFlowLimitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFlowLimitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.daily_limit):
            query['DailyLimit'] = request.daily_limit
        if not UtilClient.is_unset(request.hour_limit):
            query['HourLimit'] = request.hour_limit
        if not UtilClient.is_unset(request.minute_limit):
            query['MinuteLimit'] = request.minute_limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowLimit',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateFlowLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_flow_limit(
        self,
        request: dysms_20170620_models.CreateFlowLimitRequest,
    ) -> dysms_20170620_models.CreateFlowLimitResponse:
        """
        @param request: CreateFlowLimitRequest
        @return: CreateFlowLimitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_flow_limit_with_options(request, runtime)

    async def create_flow_limit_async(
        self,
        request: dysms_20170620_models.CreateFlowLimitRequest,
    ) -> dysms_20170620_models.CreateFlowLimitResponse:
        """
        @param request: CreateFlowLimitRequest
        @return: CreateFlowLimitResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_limit_with_options_async(request, runtime)

    def create_flow_limit_new_with_options(
        self,
        request: dysms_20170620_models.CreateFlowLimitNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateFlowLimitNewResponse:
        """
        @param request: CreateFlowLimitNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFlowLimitNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.daily_limit):
            query['DailyLimit'] = request.daily_limit
        if not UtilClient.is_unset(request.hour_limit):
            query['HourLimit'] = request.hour_limit
        if not UtilClient.is_unset(request.minute_limit):
            query['MinuteLimit'] = request.minute_limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowLimitNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateFlowLimitNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_limit_new_with_options_async(
        self,
        request: dysms_20170620_models.CreateFlowLimitNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateFlowLimitNewResponse:
        """
        @param request: CreateFlowLimitNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFlowLimitNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.daily_limit):
            query['DailyLimit'] = request.daily_limit
        if not UtilClient.is_unset(request.hour_limit):
            query['HourLimit'] = request.hour_limit
        if not UtilClient.is_unset(request.minute_limit):
            query['MinuteLimit'] = request.minute_limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowLimitNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateFlowLimitNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_flow_limit_new(
        self,
        request: dysms_20170620_models.CreateFlowLimitNewRequest,
    ) -> dysms_20170620_models.CreateFlowLimitNewResponse:
        """
        @param request: CreateFlowLimitNewRequest
        @return: CreateFlowLimitNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_flow_limit_new_with_options(request, runtime)

    async def create_flow_limit_new_async(
        self,
        request: dysms_20170620_models.CreateFlowLimitNewRequest,
    ) -> dysms_20170620_models.CreateFlowLimitNewResponse:
        """
        @param request: CreateFlowLimitNewRequest
        @return: CreateFlowLimitNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_limit_new_with_options_async(request, runtime)

    def create_message_callback_new_with_options(
        self,
        request: dysms_20170620_models.CreateMessageCallbackNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateMessageCallbackNewResponse:
        """
        @param request: CreateMessageCallbackNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMessageCallbackNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMessageCallbackNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateMessageCallbackNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_message_callback_new_with_options_async(
        self,
        request: dysms_20170620_models.CreateMessageCallbackNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateMessageCallbackNewResponse:
        """
        @param request: CreateMessageCallbackNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMessageCallbackNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMessageCallbackNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateMessageCallbackNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_message_callback_new(
        self,
        request: dysms_20170620_models.CreateMessageCallbackNewRequest,
    ) -> dysms_20170620_models.CreateMessageCallbackNewResponse:
        """
        @param request: CreateMessageCallbackNewRequest
        @return: CreateMessageCallbackNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_message_callback_new_with_options(request, runtime)

    async def create_message_callback_new_async(
        self,
        request: dysms_20170620_models.CreateMessageCallbackNewRequest,
    ) -> dysms_20170620_models.CreateMessageCallbackNewResponse:
        """
        @param request: CreateMessageCallbackNewRequest
        @return: CreateMessageCallbackNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_message_callback_new_with_options_async(request, runtime)

    def create_message_callback_test_new_with_options(
        self,
        request: dysms_20170620_models.CreateMessageCallbackTestNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateMessageCallbackTestNewResponse:
        """
        @param request: CreateMessageCallbackTestNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMessageCallbackTestNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.method):
            query['Method'] = request.method
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMessageCallbackTestNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateMessageCallbackTestNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_message_callback_test_new_with_options_async(
        self,
        request: dysms_20170620_models.CreateMessageCallbackTestNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateMessageCallbackTestNewResponse:
        """
        @param request: CreateMessageCallbackTestNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMessageCallbackTestNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.method):
            query['Method'] = request.method
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMessageCallbackTestNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateMessageCallbackTestNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_message_callback_test_new(
        self,
        request: dysms_20170620_models.CreateMessageCallbackTestNewRequest,
    ) -> dysms_20170620_models.CreateMessageCallbackTestNewResponse:
        """
        @param request: CreateMessageCallbackTestNewRequest
        @return: CreateMessageCallbackTestNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_message_callback_test_new_with_options(request, runtime)

    async def create_message_callback_test_new_async(
        self,
        request: dysms_20170620_models.CreateMessageCallbackTestNewRequest,
    ) -> dysms_20170620_models.CreateMessageCallbackTestNewResponse:
        """
        @param request: CreateMessageCallbackTestNewRequest
        @return: CreateMessageCallbackTestNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_message_callback_test_new_with_options_async(request, runtime)

    def create_message_queue_new_with_options(
        self,
        request: dysms_20170620_models.CreateMessageQueueNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateMessageQueueNewResponse:
        """
        @param request: CreateMessageQueueNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMessageQueueNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.queue_type):
            query['QueueType'] = request.queue_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMessageQueueNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateMessageQueueNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_message_queue_new_with_options_async(
        self,
        request: dysms_20170620_models.CreateMessageQueueNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateMessageQueueNewResponse:
        """
        @param request: CreateMessageQueueNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMessageQueueNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.queue_type):
            query['QueueType'] = request.queue_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMessageQueueNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateMessageQueueNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_message_queue_new(
        self,
        request: dysms_20170620_models.CreateMessageQueueNewRequest,
    ) -> dysms_20170620_models.CreateMessageQueueNewResponse:
        """
        @param request: CreateMessageQueueNewRequest
        @return: CreateMessageQueueNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_message_queue_new_with_options(request, runtime)

    async def create_message_queue_new_async(
        self,
        request: dysms_20170620_models.CreateMessageQueueNewRequest,
    ) -> dysms_20170620_models.CreateMessageQueueNewResponse:
        """
        @param request: CreateMessageQueueNewRequest
        @return: CreateMessageQueueNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_message_queue_new_with_options_async(request, runtime)

    def create_phone_white_list_with_options(
        self,
        request: dysms_20170620_models.CreatePhoneWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreatePhoneWhiteListResponse:
        """
        @param request: CreatePhoneWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePhoneWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_numbers):
            query['PhoneNumbers'] = request.phone_numbers
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePhoneWhiteList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreatePhoneWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_phone_white_list_with_options_async(
        self,
        request: dysms_20170620_models.CreatePhoneWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreatePhoneWhiteListResponse:
        """
        @param request: CreatePhoneWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePhoneWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_numbers):
            query['PhoneNumbers'] = request.phone_numbers
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePhoneWhiteList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreatePhoneWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_phone_white_list(
        self,
        request: dysms_20170620_models.CreatePhoneWhiteListRequest,
    ) -> dysms_20170620_models.CreatePhoneWhiteListResponse:
        """
        @param request: CreatePhoneWhiteListRequest
        @return: CreatePhoneWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_phone_white_list_with_options(request, runtime)

    async def create_phone_white_list_async(
        self,
        request: dysms_20170620_models.CreatePhoneWhiteListRequest,
    ) -> dysms_20170620_models.CreatePhoneWhiteListResponse:
        """
        @param request: CreatePhoneWhiteListRequest
        @return: CreatePhoneWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_phone_white_list_with_options_async(request, runtime)

    def create_phone_white_list_new_with_options(
        self,
        tmp_req: dysms_20170620_models.CreatePhoneWhiteListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreatePhoneWhiteListNewResponse:
        """
        @param tmp_req: CreatePhoneWhiteListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePhoneWhiteListNewResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysms_20170620_models.CreatePhoneWhiteListNewShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.remarks):
            request.remarks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.remarks, 'Remarks', 'json')
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_numbers):
            query['PhoneNumbers'] = request.phone_numbers
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.remarks_shrink):
            query['Remarks'] = request.remarks_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePhoneWhiteListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreatePhoneWhiteListNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_phone_white_list_new_with_options_async(
        self,
        tmp_req: dysms_20170620_models.CreatePhoneWhiteListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreatePhoneWhiteListNewResponse:
        """
        @param tmp_req: CreatePhoneWhiteListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePhoneWhiteListNewResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysms_20170620_models.CreatePhoneWhiteListNewShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.remarks):
            request.remarks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.remarks, 'Remarks', 'json')
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_numbers):
            query['PhoneNumbers'] = request.phone_numbers
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.remarks_shrink):
            query['Remarks'] = request.remarks_shrink
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePhoneWhiteListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreatePhoneWhiteListNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_phone_white_list_new(
        self,
        request: dysms_20170620_models.CreatePhoneWhiteListNewRequest,
    ) -> dysms_20170620_models.CreatePhoneWhiteListNewResponse:
        """
        @param request: CreatePhoneWhiteListNewRequest
        @return: CreatePhoneWhiteListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_phone_white_list_new_with_options(request, runtime)

    async def create_phone_white_list_new_async(
        self,
        request: dysms_20170620_models.CreatePhoneWhiteListNewRequest,
    ) -> dysms_20170620_models.CreatePhoneWhiteListNewResponse:
        """
        @param request: CreatePhoneWhiteListNewRequest
        @return: CreatePhoneWhiteListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_phone_white_list_new_with_options_async(request, runtime)

    def create_pkg_threshold_with_options(
        self,
        request: dysms_20170620_models.CreatePkgThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreatePkgThresholdResponse:
        """
        @param request: CreatePkgThresholdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePkgThresholdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.package_warning_limit):
            query['PackageWarningLimit'] = request.package_warning_limit
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePkgThreshold',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreatePkgThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pkg_threshold_with_options_async(
        self,
        request: dysms_20170620_models.CreatePkgThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreatePkgThresholdResponse:
        """
        @param request: CreatePkgThresholdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePkgThresholdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.package_warning_limit):
            query['PackageWarningLimit'] = request.package_warning_limit
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePkgThreshold',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreatePkgThresholdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pkg_threshold(
        self,
        request: dysms_20170620_models.CreatePkgThresholdRequest,
    ) -> dysms_20170620_models.CreatePkgThresholdResponse:
        """
        @param request: CreatePkgThresholdRequest
        @return: CreatePkgThresholdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_pkg_threshold_with_options(request, runtime)

    async def create_pkg_threshold_async(
        self,
        request: dysms_20170620_models.CreatePkgThresholdRequest,
    ) -> dysms_20170620_models.CreatePkgThresholdResponse:
        """
        @param request: CreatePkgThresholdRequest
        @return: CreatePkgThresholdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_pkg_threshold_with_options_async(request, runtime)

    def create_pkg_threshold_new_with_options(
        self,
        request: dysms_20170620_models.CreatePkgThresholdNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreatePkgThresholdNewResponse:
        """
        @param request: CreatePkgThresholdNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePkgThresholdNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.package_warning_limit):
            query['PackageWarningLimit'] = request.package_warning_limit
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePkgThresholdNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreatePkgThresholdNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pkg_threshold_new_with_options_async(
        self,
        request: dysms_20170620_models.CreatePkgThresholdNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreatePkgThresholdNewResponse:
        """
        @param request: CreatePkgThresholdNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePkgThresholdNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.package_warning_limit):
            query['PackageWarningLimit'] = request.package_warning_limit
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePkgThresholdNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreatePkgThresholdNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pkg_threshold_new(
        self,
        request: dysms_20170620_models.CreatePkgThresholdNewRequest,
    ) -> dysms_20170620_models.CreatePkgThresholdNewResponse:
        """
        @param request: CreatePkgThresholdNewRequest
        @return: CreatePkgThresholdNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_pkg_threshold_new_with_options(request, runtime)

    async def create_pkg_threshold_new_async(
        self,
        request: dysms_20170620_models.CreatePkgThresholdNewRequest,
    ) -> dysms_20170620_models.CreatePkgThresholdNewResponse:
        """
        @param request: CreatePkgThresholdNewRequest
        @return: CreatePkgThresholdNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_pkg_threshold_new_with_options_async(request, runtime)

    def create_prev_limit_new_with_options(
        self,
        request: dysms_20170620_models.CreatePrevLimitNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreatePrevLimitNewResponse:
        """
        @param request: CreatePrevLimitNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePrevLimitNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hour_limit):
            query['HourLimit'] = request.hour_limit
        if not UtilClient.is_unset(request.increase_rate):
            query['IncreaseRate'] = request.increase_rate
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.success_rate):
            query['SuccessRate'] = request.success_rate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePrevLimitNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreatePrevLimitNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_prev_limit_new_with_options_async(
        self,
        request: dysms_20170620_models.CreatePrevLimitNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreatePrevLimitNewResponse:
        """
        @param request: CreatePrevLimitNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePrevLimitNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hour_limit):
            query['HourLimit'] = request.hour_limit
        if not UtilClient.is_unset(request.increase_rate):
            query['IncreaseRate'] = request.increase_rate
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.success_rate):
            query['SuccessRate'] = request.success_rate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePrevLimitNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreatePrevLimitNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_prev_limit_new(
        self,
        request: dysms_20170620_models.CreatePrevLimitNewRequest,
    ) -> dysms_20170620_models.CreatePrevLimitNewResponse:
        """
        @param request: CreatePrevLimitNewRequest
        @return: CreatePrevLimitNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_prev_limit_new_with_options(request, runtime)

    async def create_prev_limit_new_async(
        self,
        request: dysms_20170620_models.CreatePrevLimitNewRequest,
    ) -> dysms_20170620_models.CreatePrevLimitNewResponse:
        """
        @param request: CreatePrevLimitNewRequest
        @return: CreatePrevLimitNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_prev_limit_new_with_options_async(request, runtime)

    def create_product_with_options(
        self,
        request: dysms_20170620_models.CreateProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateProductResponse:
        """
        @param request: CreateProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProductResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProduct',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_product_with_options_async(
        self,
        request: dysms_20170620_models.CreateProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateProductResponse:
        """
        @param request: CreateProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProductResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProduct',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_product(
        self,
        request: dysms_20170620_models.CreateProductRequest,
    ) -> dysms_20170620_models.CreateProductResponse:
        """
        @param request: CreateProductRequest
        @return: CreateProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_product_with_options(request, runtime)

    async def create_product_async(
        self,
        request: dysms_20170620_models.CreateProductRequest,
    ) -> dysms_20170620_models.CreateProductResponse:
        """
        @param request: CreateProductRequest
        @return: CreateProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_product_with_options_async(request, runtime)

    def create_product_new_with_options(
        self,
        request: dysms_20170620_models.CreateProductNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateProductNewResponse:
        """
        @param request: CreateProductNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProductNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProductNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateProductNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_product_new_with_options_async(
        self,
        request: dysms_20170620_models.CreateProductNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateProductNewResponse:
        """
        @param request: CreateProductNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProductNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProductNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateProductNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_product_new(
        self,
        request: dysms_20170620_models.CreateProductNewRequest,
    ) -> dysms_20170620_models.CreateProductNewResponse:
        """
        @param request: CreateProductNewRequest
        @return: CreateProductNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_product_new_with_options(request, runtime)

    async def create_product_new_async(
        self,
        request: dysms_20170620_models.CreateProductNewRequest,
    ) -> dysms_20170620_models.CreateProductNewResponse:
        """
        @param request: CreateProductNewRequest
        @return: CreateProductNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_product_new_with_options_async(request, runtime)

    def create_short_url_new_with_options(
        self,
        request: dysms_20170620_models.CreateShortUrlNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateShortUrlNewResponse:
        """
        @param request: CreateShortUrlNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateShortUrlNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effect_day):
            query['EffectDay'] = request.effect_day
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
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
            action='CreateShortUrlNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateShortUrlNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_short_url_new_with_options_async(
        self,
        request: dysms_20170620_models.CreateShortUrlNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateShortUrlNewResponse:
        """
        @param request: CreateShortUrlNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateShortUrlNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effect_day):
            query['EffectDay'] = request.effect_day
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
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
            action='CreateShortUrlNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateShortUrlNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_short_url_new(
        self,
        request: dysms_20170620_models.CreateShortUrlNewRequest,
    ) -> dysms_20170620_models.CreateShortUrlNewResponse:
        """
        @param request: CreateShortUrlNewRequest
        @return: CreateShortUrlNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_short_url_new_with_options(request, runtime)

    async def create_short_url_new_async(
        self,
        request: dysms_20170620_models.CreateShortUrlNewRequest,
    ) -> dysms_20170620_models.CreateShortUrlNewResponse:
        """
        @param request: CreateShortUrlNewRequest
        @return: CreateShortUrlNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_short_url_new_with_options_async(request, runtime)

    def create_sms_detect_task_new_with_options(
        self,
        request: dysms_20170620_models.CreateSmsDetectTaskNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateSmsDetectTaskNewResponse:
        """
        @param request: CreateSmsDetectTaskNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsDetectTaskNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check):
            query['Check'] = request.check
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sms_content):
            query['SmsContent'] = request.sms_content
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param):
            query['TemplateParam'] = request.template_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmsDetectTaskNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateSmsDetectTaskNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sms_detect_task_new_with_options_async(
        self,
        request: dysms_20170620_models.CreateSmsDetectTaskNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateSmsDetectTaskNewResponse:
        """
        @param request: CreateSmsDetectTaskNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsDetectTaskNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check):
            query['Check'] = request.check
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sms_content):
            query['SmsContent'] = request.sms_content
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param):
            query['TemplateParam'] = request.template_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmsDetectTaskNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateSmsDetectTaskNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sms_detect_task_new(
        self,
        request: dysms_20170620_models.CreateSmsDetectTaskNewRequest,
    ) -> dysms_20170620_models.CreateSmsDetectTaskNewResponse:
        """
        @param request: CreateSmsDetectTaskNewRequest
        @return: CreateSmsDetectTaskNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sms_detect_task_new_with_options(request, runtime)

    async def create_sms_detect_task_new_async(
        self,
        request: dysms_20170620_models.CreateSmsDetectTaskNewRequest,
    ) -> dysms_20170620_models.CreateSmsDetectTaskNewResponse:
        """
        @param request: CreateSmsDetectTaskNewRequest
        @return: CreateSmsDetectTaskNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_sms_detect_task_new_with_options_async(request, runtime)

    def create_sms_internal_apply_with_options(
        self,
        request: dysms_20170620_models.CreateSmsInternalApplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateSmsInternalApplyResponse:
        """
        @param request: CreateSmsInternalApplyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsInternalApplyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_download_link):
            query['AppDownloadLink'] = request.app_download_link
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.industry):
            query['Industry'] = request.industry
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_link):
            query['PageLink'] = request.page_link
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmsInternalApply',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateSmsInternalApplyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sms_internal_apply_with_options_async(
        self,
        request: dysms_20170620_models.CreateSmsInternalApplyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateSmsInternalApplyResponse:
        """
        @param request: CreateSmsInternalApplyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsInternalApplyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_download_link):
            query['AppDownloadLink'] = request.app_download_link
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.industry):
            query['Industry'] = request.industry
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_link):
            query['PageLink'] = request.page_link
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmsInternalApply',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateSmsInternalApplyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sms_internal_apply(
        self,
        request: dysms_20170620_models.CreateSmsInternalApplyRequest,
    ) -> dysms_20170620_models.CreateSmsInternalApplyResponse:
        """
        @param request: CreateSmsInternalApplyRequest
        @return: CreateSmsInternalApplyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sms_internal_apply_with_options(request, runtime)

    async def create_sms_internal_apply_async(
        self,
        request: dysms_20170620_models.CreateSmsInternalApplyRequest,
    ) -> dysms_20170620_models.CreateSmsInternalApplyResponse:
        """
        @param request: CreateSmsInternalApplyRequest
        @return: CreateSmsInternalApplyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_sms_internal_apply_with_options_async(request, runtime)

    def create_sms_product_for_channel_cust_with_options(
        self,
        request: dysms_20170620_models.CreateSmsProductForChannelCustRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateSmsProductForChannelCustResponse:
        """
        @param request: CreateSmsProductForChannelCustRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsProductForChannelCustResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.only_check_opened):
            query['OnlyCheckOpened'] = request.only_check_opened
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmsProductForChannelCust',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateSmsProductForChannelCustResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sms_product_for_channel_cust_with_options_async(
        self,
        request: dysms_20170620_models.CreateSmsProductForChannelCustRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateSmsProductForChannelCustResponse:
        """
        @param request: CreateSmsProductForChannelCustRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsProductForChannelCustResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.only_check_opened):
            query['OnlyCheckOpened'] = request.only_check_opened
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmsProductForChannelCust',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateSmsProductForChannelCustResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sms_product_for_channel_cust(
        self,
        request: dysms_20170620_models.CreateSmsProductForChannelCustRequest,
    ) -> dysms_20170620_models.CreateSmsProductForChannelCustResponse:
        """
        @param request: CreateSmsProductForChannelCustRequest
        @return: CreateSmsProductForChannelCustResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sms_product_for_channel_cust_with_options(request, runtime)

    async def create_sms_product_for_channel_cust_async(
        self,
        request: dysms_20170620_models.CreateSmsProductForChannelCustRequest,
    ) -> dysms_20170620_models.CreateSmsProductForChannelCustResponse:
        """
        @param request: CreateSmsProductForChannelCustRequest
        @return: CreateSmsProductForChannelCustResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_sms_product_for_channel_cust_with_options_async(request, runtime)

    def create_sms_saas_task_with_options(
        self,
        request: dysms_20170620_models.CreateSmsSaasTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateSmsSaasTaskResponse:
        """
        @param request: CreateSmsSaasTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsSaasTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.order_time):
            query['OrderTime'] = request.order_time
        if not UtilClient.is_unset(request.oss_file_name):
            query['OssFileName'] = request.oss_file_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_list):
            query['PhoneList'] = request.phone_list
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.schedule_type):
            query['ScheduleType'] = request.schedule_type
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sms_content):
            query['SmsContent'] = request.sms_content
        if not UtilClient.is_unset(request.sms_template_code):
            query['SmsTemplateCode'] = request.sms_template_code
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.valid_count):
            query['ValidCount'] = request.valid_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmsSaasTask',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateSmsSaasTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sms_saas_task_with_options_async(
        self,
        request: dysms_20170620_models.CreateSmsSaasTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateSmsSaasTaskResponse:
        """
        @param request: CreateSmsSaasTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsSaasTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.order_time):
            query['OrderTime'] = request.order_time
        if not UtilClient.is_unset(request.oss_file_name):
            query['OssFileName'] = request.oss_file_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_list):
            query['PhoneList'] = request.phone_list
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.schedule_type):
            query['ScheduleType'] = request.schedule_type
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sms_content):
            query['SmsContent'] = request.sms_content
        if not UtilClient.is_unset(request.sms_template_code):
            query['SmsTemplateCode'] = request.sms_template_code
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.valid_count):
            query['ValidCount'] = request.valid_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmsSaasTask',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateSmsSaasTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sms_saas_task(
        self,
        request: dysms_20170620_models.CreateSmsSaasTaskRequest,
    ) -> dysms_20170620_models.CreateSmsSaasTaskResponse:
        """
        @param request: CreateSmsSaasTaskRequest
        @return: CreateSmsSaasTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sms_saas_task_with_options(request, runtime)

    async def create_sms_saas_task_async(
        self,
        request: dysms_20170620_models.CreateSmsSaasTaskRequest,
    ) -> dysms_20170620_models.CreateSmsSaasTaskResponse:
        """
        @param request: CreateSmsSaasTaskRequest
        @return: CreateSmsSaasTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_sms_saas_task_with_options_async(request, runtime)

    def create_sms_saas_task_new_with_options(
        self,
        request: dysms_20170620_models.CreateSmsSaasTaskNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateSmsSaasTaskNewResponse:
        """
        @param request: CreateSmsSaasTaskNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsSaasTaskNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.data_ability_task_id):
            query['DataAbilityTaskId'] = request.data_ability_task_id
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.order_time):
            query['OrderTime'] = request.order_time
        if not UtilClient.is_unset(request.oss_file_name):
            query['OssFileName'] = request.oss_file_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_list):
            query['PhoneList'] = request.phone_list
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.schedule_type):
            query['ScheduleType'] = request.schedule_type
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sms_content):
            query['SmsContent'] = request.sms_content
        if not UtilClient.is_unset(request.sms_template_code):
            query['SmsTemplateCode'] = request.sms_template_code
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.valid_count):
            query['ValidCount'] = request.valid_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmsSaasTaskNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateSmsSaasTaskNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sms_saas_task_new_with_options_async(
        self,
        request: dysms_20170620_models.CreateSmsSaasTaskNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateSmsSaasTaskNewResponse:
        """
        @param request: CreateSmsSaasTaskNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsSaasTaskNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.data_ability_task_id):
            query['DataAbilityTaskId'] = request.data_ability_task_id
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.order_time):
            query['OrderTime'] = request.order_time
        if not UtilClient.is_unset(request.oss_file_name):
            query['OssFileName'] = request.oss_file_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_list):
            query['PhoneList'] = request.phone_list
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.schedule_type):
            query['ScheduleType'] = request.schedule_type
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sms_content):
            query['SmsContent'] = request.sms_content
        if not UtilClient.is_unset(request.sms_template_code):
            query['SmsTemplateCode'] = request.sms_template_code
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.valid_count):
            query['ValidCount'] = request.valid_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmsSaasTaskNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateSmsSaasTaskNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sms_saas_task_new(
        self,
        request: dysms_20170620_models.CreateSmsSaasTaskNewRequest,
    ) -> dysms_20170620_models.CreateSmsSaasTaskNewResponse:
        """
        @param request: CreateSmsSaasTaskNewRequest
        @return: CreateSmsSaasTaskNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sms_saas_task_new_with_options(request, runtime)

    async def create_sms_saas_task_new_async(
        self,
        request: dysms_20170620_models.CreateSmsSaasTaskNewRequest,
    ) -> dysms_20170620_models.CreateSmsSaasTaskNewResponse:
        """
        @param request: CreateSmsSaasTaskNewRequest
        @return: CreateSmsSaasTaskNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_sms_saas_task_new_with_options_async(request, runtime)

    def create_sms_send_fail_details_download_with_options(
        self,
        request: dysms_20170620_models.CreateSmsSendFailDetailsDownloadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateSmsSendFailDetailsDownloadResponse:
        """
        @param request: CreateSmsSendFailDetailsDownloadRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsSendFailDetailsDownloadResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
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
            action='CreateSmsSendFailDetailsDownload',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateSmsSendFailDetailsDownloadResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sms_send_fail_details_download_with_options_async(
        self,
        request: dysms_20170620_models.CreateSmsSendFailDetailsDownloadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateSmsSendFailDetailsDownloadResponse:
        """
        @param request: CreateSmsSendFailDetailsDownloadRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsSendFailDetailsDownloadResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
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
            action='CreateSmsSendFailDetailsDownload',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateSmsSendFailDetailsDownloadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sms_send_fail_details_download(
        self,
        request: dysms_20170620_models.CreateSmsSendFailDetailsDownloadRequest,
    ) -> dysms_20170620_models.CreateSmsSendFailDetailsDownloadResponse:
        """
        @param request: CreateSmsSendFailDetailsDownloadRequest
        @return: CreateSmsSendFailDetailsDownloadResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sms_send_fail_details_download_with_options(request, runtime)

    async def create_sms_send_fail_details_download_async(
        self,
        request: dysms_20170620_models.CreateSmsSendFailDetailsDownloadRequest,
    ) -> dysms_20170620_models.CreateSmsSendFailDetailsDownloadResponse:
        """
        @param request: CreateSmsSendFailDetailsDownloadRequest
        @return: CreateSmsSendFailDetailsDownloadResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_sms_send_fail_details_download_with_options_async(request, runtime)

    def create_sms_sign_with_options(
        self,
        request: dysms_20170620_models.CreateSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateSmsSignResponse:
        """
        @param request: CreateSmsSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extend_message):
            query['ExtendMessage'] = request.extend_message
        if not UtilClient.is_unset(request.file_ids):
            query['FileIds'] = request.file_ids
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmsSign',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateSmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sms_sign_with_options_async(
        self,
        request: dysms_20170620_models.CreateSmsSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateSmsSignResponse:
        """
        @param request: CreateSmsSignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extend_message):
            query['ExtendMessage'] = request.extend_message
        if not UtilClient.is_unset(request.file_ids):
            query['FileIds'] = request.file_ids
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmsSign',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateSmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sms_sign(
        self,
        request: dysms_20170620_models.CreateSmsSignRequest,
    ) -> dysms_20170620_models.CreateSmsSignResponse:
        """
        @param request: CreateSmsSignRequest
        @return: CreateSmsSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sms_sign_with_options(request, runtime)

    async def create_sms_sign_async(
        self,
        request: dysms_20170620_models.CreateSmsSignRequest,
    ) -> dysms_20170620_models.CreateSmsSignResponse:
        """
        @param request: CreateSmsSignRequest
        @return: CreateSmsSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_sms_sign_with_options_async(request, runtime)

    def create_sms_sign_new_with_options(
        self,
        tmp_req: dysms_20170620_models.CreateSmsSignNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateSmsSignNewResponse:
        """
        @param tmp_req: CreateSmsSignNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsSignNewResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysms_20170620_models.CreateSmsSignNewShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.more_data):
            request.more_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.more_data, 'MoreData', 'json')
        query = {}
        if not UtilClient.is_unset(request.application_scene_id):
            query['ApplicationSceneId'] = request.application_scene_id
        if not UtilClient.is_unset(request.apply_source):
            query['ApplySource'] = request.apply_source
        if not UtilClient.is_unset(request.authorization):
            query['Authorization'] = request.authorization
        if not UtilClient.is_unset(request.authorization_eff_time):
            query['AuthorizationEffTime'] = request.authorization_eff_time
        if not UtilClient.is_unset(request.authorization_letter):
            query['AuthorizationLetter'] = request.authorization_letter
        if not UtilClient.is_unset(request.authorization_letter_audit_pass):
            query['AuthorizationLetterAuditPass'] = request.authorization_letter_audit_pass
        if not UtilClient.is_unset(request.authorization_letter_id):
            query['AuthorizationLetterId'] = request.authorization_letter_id
        if not UtilClient.is_unset(request.authorization_letter_name):
            query['AuthorizationLetterName'] = request.authorization_letter_name
        if not UtilClient.is_unset(request.authorization_sign_scope):
            query['AuthorizationSignScope'] = request.authorization_sign_scope
        if not UtilClient.is_unset(request.create_sign_gray):
            query['CreateSignGray'] = request.create_sign_gray
        if not UtilClient.is_unset(request.enable_authorization_letter):
            query['EnableAuthorizationLetter'] = request.enable_authorization_letter
        if not UtilClient.is_unset(request.extend_message):
            query['ExtendMessage'] = request.extend_message
        if not UtilClient.is_unset(request.file_ids):
            query['FileIds'] = request.file_ids
        if not UtilClient.is_unset(request.is_authorization_letter_ocrcomplete):
            query['IsAuthorizationLetterOCRComplete'] = request.is_authorization_letter_ocrcomplete
        if not UtilClient.is_unset(request.is_authorization_letter_ocrdiff):
            query['IsAuthorizationLetterOCRDiff'] = request.is_authorization_letter_ocrdiff
        if not UtilClient.is_unset(request.is_sign_scope_ocrdiff):
            query['IsSignScopeOCRDiff'] = request.is_sign_scope_ocrdiff
        if not UtilClient.is_unset(request.more_data_shrink):
            query['MoreData'] = request.more_data_shrink
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.organization_code):
            query['OrganizationCode'] = request.organization_code
        if not UtilClient.is_unset(request.oss_keys):
            query['OssKeys'] = request.oss_keys
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_authorization):
            query['ProxyAuthorization'] = request.proxy_authorization
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.qualification_type):
            query['QualificationType'] = request.qualification_type
        if not UtilClient.is_unset(request.qualification_version):
            query['QualificationVersion'] = request.qualification_version
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.sign_code):
            query['SignCode'] = request.sign_code
        if not UtilClient.is_unset(request.sign_id):
            query['SignId'] = request.sign_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sign_scope_ocr):
            query['SignScopeOCR'] = request.sign_scope_ocr
        if not UtilClient.is_unset(request.sign_upgrade):
            query['SignUpgrade'] = request.sign_upgrade
        if not UtilClient.is_unset(request.third_party):
            query['ThirdParty'] = request.third_party
        if not UtilClient.is_unset(request.user_view_file_name):
            query['UserViewFileName'] = request.user_view_file_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmsSignNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateSmsSignNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sms_sign_new_with_options_async(
        self,
        tmp_req: dysms_20170620_models.CreateSmsSignNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateSmsSignNewResponse:
        """
        @param tmp_req: CreateSmsSignNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsSignNewResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysms_20170620_models.CreateSmsSignNewShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.more_data):
            request.more_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.more_data, 'MoreData', 'json')
        query = {}
        if not UtilClient.is_unset(request.application_scene_id):
            query['ApplicationSceneId'] = request.application_scene_id
        if not UtilClient.is_unset(request.apply_source):
            query['ApplySource'] = request.apply_source
        if not UtilClient.is_unset(request.authorization):
            query['Authorization'] = request.authorization
        if not UtilClient.is_unset(request.authorization_eff_time):
            query['AuthorizationEffTime'] = request.authorization_eff_time
        if not UtilClient.is_unset(request.authorization_letter):
            query['AuthorizationLetter'] = request.authorization_letter
        if not UtilClient.is_unset(request.authorization_letter_audit_pass):
            query['AuthorizationLetterAuditPass'] = request.authorization_letter_audit_pass
        if not UtilClient.is_unset(request.authorization_letter_id):
            query['AuthorizationLetterId'] = request.authorization_letter_id
        if not UtilClient.is_unset(request.authorization_letter_name):
            query['AuthorizationLetterName'] = request.authorization_letter_name
        if not UtilClient.is_unset(request.authorization_sign_scope):
            query['AuthorizationSignScope'] = request.authorization_sign_scope
        if not UtilClient.is_unset(request.create_sign_gray):
            query['CreateSignGray'] = request.create_sign_gray
        if not UtilClient.is_unset(request.enable_authorization_letter):
            query['EnableAuthorizationLetter'] = request.enable_authorization_letter
        if not UtilClient.is_unset(request.extend_message):
            query['ExtendMessage'] = request.extend_message
        if not UtilClient.is_unset(request.file_ids):
            query['FileIds'] = request.file_ids
        if not UtilClient.is_unset(request.is_authorization_letter_ocrcomplete):
            query['IsAuthorizationLetterOCRComplete'] = request.is_authorization_letter_ocrcomplete
        if not UtilClient.is_unset(request.is_authorization_letter_ocrdiff):
            query['IsAuthorizationLetterOCRDiff'] = request.is_authorization_letter_ocrdiff
        if not UtilClient.is_unset(request.is_sign_scope_ocrdiff):
            query['IsSignScopeOCRDiff'] = request.is_sign_scope_ocrdiff
        if not UtilClient.is_unset(request.more_data_shrink):
            query['MoreData'] = request.more_data_shrink
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.organization_code):
            query['OrganizationCode'] = request.organization_code
        if not UtilClient.is_unset(request.oss_keys):
            query['OssKeys'] = request.oss_keys
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.proxy_authorization):
            query['ProxyAuthorization'] = request.proxy_authorization
        if not UtilClient.is_unset(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not UtilClient.is_unset(request.qualification_type):
            query['QualificationType'] = request.qualification_type
        if not UtilClient.is_unset(request.qualification_version):
            query['QualificationVersion'] = request.qualification_version
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.sign_code):
            query['SignCode'] = request.sign_code
        if not UtilClient.is_unset(request.sign_id):
            query['SignId'] = request.sign_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sign_scope_ocr):
            query['SignScopeOCR'] = request.sign_scope_ocr
        if not UtilClient.is_unset(request.sign_upgrade):
            query['SignUpgrade'] = request.sign_upgrade
        if not UtilClient.is_unset(request.third_party):
            query['ThirdParty'] = request.third_party
        if not UtilClient.is_unset(request.user_view_file_name):
            query['UserViewFileName'] = request.user_view_file_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmsSignNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateSmsSignNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sms_sign_new(
        self,
        request: dysms_20170620_models.CreateSmsSignNewRequest,
    ) -> dysms_20170620_models.CreateSmsSignNewResponse:
        """
        @param request: CreateSmsSignNewRequest
        @return: CreateSmsSignNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sms_sign_new_with_options(request, runtime)

    async def create_sms_sign_new_async(
        self,
        request: dysms_20170620_models.CreateSmsSignNewRequest,
    ) -> dysms_20170620_models.CreateSmsSignNewResponse:
        """
        @param request: CreateSmsSignNewRequest
        @return: CreateSmsSignNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_sms_sign_new_with_options_async(request, runtime)

    def create_sms_template_new_with_options(
        self,
        tmp_req: dysms_20170620_models.CreateSmsTemplateNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateSmsTemplateNewResponse:
        """
        @param tmp_req: CreateSmsTemplateNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsTemplateNewResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysms_20170620_models.CreateSmsTemplateNewShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.more_data):
            request.more_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.more_data, 'MoreData', 'json')
        query = {}
        if not UtilClient.is_unset(request.ai_template):
            query['AiTemplate'] = request.ai_template
        if not UtilClient.is_unset(request.ai_template_uuid):
            query['AiTemplateUuid'] = request.ai_template_uuid
        if not UtilClient.is_unset(request.application_scene_id):
            query['ApplicationSceneId'] = request.application_scene_id
        if not UtilClient.is_unset(request.apply_source):
            query['ApplySource'] = request.apply_source
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.intl_type):
            query['IntlType'] = request.intl_type
        if not UtilClient.is_unset(request.more_data_shrink):
            query['MoreData'] = request.more_data_shrink
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.oss_keys):
            query['OssKeys'] = request.oss_keys
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.product_url):
            query['ProductUrl'] = request.product_url
        if not UtilClient.is_unset(request.related_sign_name):
            query['RelatedSignName'] = request.related_sign_name
        if not UtilClient.is_unset(request.related_sign_order_id):
            query['RelatedSignOrderId'] = request.related_sign_order_id
        if not UtilClient.is_unset(request.related_sign_usage_name):
            query['RelatedSignUsageName'] = request.related_sign_usage_name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rmd_template_id):
            query['RmdTemplateId'] = request.rmd_template_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_content):
            query['TemplateContent'] = request.template_content
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_rule):
            query['TemplateRule'] = request.template_rule
        if not UtilClient.is_unset(request.user_view_file_name):
            query['UserViewFileName'] = request.user_view_file_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmsTemplateNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateSmsTemplateNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sms_template_new_with_options_async(
        self,
        tmp_req: dysms_20170620_models.CreateSmsTemplateNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateSmsTemplateNewResponse:
        """
        @param tmp_req: CreateSmsTemplateNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSmsTemplateNewResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysms_20170620_models.CreateSmsTemplateNewShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.more_data):
            request.more_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.more_data, 'MoreData', 'json')
        query = {}
        if not UtilClient.is_unset(request.ai_template):
            query['AiTemplate'] = request.ai_template
        if not UtilClient.is_unset(request.ai_template_uuid):
            query['AiTemplateUuid'] = request.ai_template_uuid
        if not UtilClient.is_unset(request.application_scene_id):
            query['ApplicationSceneId'] = request.application_scene_id
        if not UtilClient.is_unset(request.apply_source):
            query['ApplySource'] = request.apply_source
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.intl_type):
            query['IntlType'] = request.intl_type
        if not UtilClient.is_unset(request.more_data_shrink):
            query['MoreData'] = request.more_data_shrink
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.oss_keys):
            query['OssKeys'] = request.oss_keys
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.product_url):
            query['ProductUrl'] = request.product_url
        if not UtilClient.is_unset(request.related_sign_name):
            query['RelatedSignName'] = request.related_sign_name
        if not UtilClient.is_unset(request.related_sign_order_id):
            query['RelatedSignOrderId'] = request.related_sign_order_id
        if not UtilClient.is_unset(request.related_sign_usage_name):
            query['RelatedSignUsageName'] = request.related_sign_usage_name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rmd_template_id):
            query['RmdTemplateId'] = request.rmd_template_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_content):
            query['TemplateContent'] = request.template_content
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_rule):
            query['TemplateRule'] = request.template_rule
        if not UtilClient.is_unset(request.user_view_file_name):
            query['UserViewFileName'] = request.user_view_file_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSmsTemplateNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateSmsTemplateNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sms_template_new(
        self,
        request: dysms_20170620_models.CreateSmsTemplateNewRequest,
    ) -> dysms_20170620_models.CreateSmsTemplateNewResponse:
        """
        @param request: CreateSmsTemplateNewRequest
        @return: CreateSmsTemplateNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sms_template_new_with_options(request, runtime)

    async def create_sms_template_new_async(
        self,
        request: dysms_20170620_models.CreateSmsTemplateNewRequest,
    ) -> dysms_20170620_models.CreateSmsTemplateNewResponse:
        """
        @param request: CreateSmsTemplateNewRequest
        @return: CreateSmsTemplateNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_sms_template_new_with_options_async(request, runtime)

    def create_warning_threshold_with_options(
        self,
        request: dysms_20170620_models.CreateWarningThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateWarningThresholdResponse:
        """
        @param request: CreateWarningThresholdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWarningThresholdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.daily_halt_limit):
            query['DailyHaltLimit'] = request.daily_halt_limit
        if not UtilClient.is_unset(request.daily_warning_limit):
            query['DailyWarningLimit'] = request.daily_warning_limit
        if not UtilClient.is_unset(request.monthly_halt_limit):
            query['MonthlyHaltLimit'] = request.monthly_halt_limit
        if not UtilClient.is_unset(request.monthly_warning_limit):
            query['MonthlyWarningLimit'] = request.monthly_warning_limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWarningThreshold',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateWarningThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_warning_threshold_with_options_async(
        self,
        request: dysms_20170620_models.CreateWarningThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateWarningThresholdResponse:
        """
        @param request: CreateWarningThresholdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWarningThresholdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.daily_halt_limit):
            query['DailyHaltLimit'] = request.daily_halt_limit
        if not UtilClient.is_unset(request.daily_warning_limit):
            query['DailyWarningLimit'] = request.daily_warning_limit
        if not UtilClient.is_unset(request.monthly_halt_limit):
            query['MonthlyHaltLimit'] = request.monthly_halt_limit
        if not UtilClient.is_unset(request.monthly_warning_limit):
            query['MonthlyWarningLimit'] = request.monthly_warning_limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWarningThreshold',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateWarningThresholdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_warning_threshold(
        self,
        request: dysms_20170620_models.CreateWarningThresholdRequest,
    ) -> dysms_20170620_models.CreateWarningThresholdResponse:
        """
        @param request: CreateWarningThresholdRequest
        @return: CreateWarningThresholdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_warning_threshold_with_options(request, runtime)

    async def create_warning_threshold_async(
        self,
        request: dysms_20170620_models.CreateWarningThresholdRequest,
    ) -> dysms_20170620_models.CreateWarningThresholdResponse:
        """
        @param request: CreateWarningThresholdRequest
        @return: CreateWarningThresholdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_warning_threshold_with_options_async(request, runtime)

    def create_warning_threshold_new_with_options(
        self,
        request: dysms_20170620_models.CreateWarningThresholdNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateWarningThresholdNewResponse:
        """
        @param request: CreateWarningThresholdNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWarningThresholdNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.daily_halt_limit):
            query['DailyHaltLimit'] = request.daily_halt_limit
        if not UtilClient.is_unset(request.daily_warning_limit):
            query['DailyWarningLimit'] = request.daily_warning_limit
        if not UtilClient.is_unset(request.monthly_halt_limit):
            query['MonthlyHaltLimit'] = request.monthly_halt_limit
        if not UtilClient.is_unset(request.monthly_warning_limit):
            query['MonthlyWarningLimit'] = request.monthly_warning_limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWarningThresholdNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateWarningThresholdNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_warning_threshold_new_with_options_async(
        self,
        request: dysms_20170620_models.CreateWarningThresholdNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.CreateWarningThresholdNewResponse:
        """
        @param request: CreateWarningThresholdNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWarningThresholdNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.daily_halt_limit):
            query['DailyHaltLimit'] = request.daily_halt_limit
        if not UtilClient.is_unset(request.daily_warning_limit):
            query['DailyWarningLimit'] = request.daily_warning_limit
        if not UtilClient.is_unset(request.monthly_halt_limit):
            query['MonthlyHaltLimit'] = request.monthly_halt_limit
        if not UtilClient.is_unset(request.monthly_warning_limit):
            query['MonthlyWarningLimit'] = request.monthly_warning_limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWarningThresholdNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.CreateWarningThresholdNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_warning_threshold_new(
        self,
        request: dysms_20170620_models.CreateWarningThresholdNewRequest,
    ) -> dysms_20170620_models.CreateWarningThresholdNewResponse:
        """
        @param request: CreateWarningThresholdNewRequest
        @return: CreateWarningThresholdNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_warning_threshold_new_with_options(request, runtime)

    async def create_warning_threshold_new_async(
        self,
        request: dysms_20170620_models.CreateWarningThresholdNewRequest,
    ) -> dysms_20170620_models.CreateWarningThresholdNewResponse:
        """
        @param request: CreateWarningThresholdNewRequest
        @return: CreateWarningThresholdNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_warning_threshold_new_with_options_async(request, runtime)

    def del_card_send_export_info_with_options(
        self,
        request: dysms_20170620_models.DelCardSendExportInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DelCardSendExportInfoResponse:
        """
        @summary 删除导出记录
        
        @param request: DelCardSendExportInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DelCardSendExportInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelCardSendExportInfo',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DelCardSendExportInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def del_card_send_export_info_with_options_async(
        self,
        request: dysms_20170620_models.DelCardSendExportInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DelCardSendExportInfoResponse:
        """
        @summary 删除导出记录
        
        @param request: DelCardSendExportInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DelCardSendExportInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelCardSendExportInfo',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DelCardSendExportInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def del_card_send_export_info(
        self,
        request: dysms_20170620_models.DelCardSendExportInfoRequest,
    ) -> dysms_20170620_models.DelCardSendExportInfoResponse:
        """
        @summary 删除导出记录
        
        @param request: DelCardSendExportInfoRequest
        @return: DelCardSendExportInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.del_card_send_export_info_with_options(request, runtime)

    async def del_card_send_export_info_async(
        self,
        request: dysms_20170620_models.DelCardSendExportInfoRequest,
    ) -> dysms_20170620_models.DelCardSendExportInfoResponse:
        """
        @summary 删除导出记录
        
        @param request: DelCardSendExportInfoRequest
        @return: DelCardSendExportInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.del_card_send_export_info_with_options_async(request, runtime)

    def delete_card_message_callback_with_options(
        self,
        request: dysms_20170620_models.DeleteCardMessageCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeleteCardMessageCallbackResponse:
        """
        @summary 删除消息回调
        
        @param request: DeleteCardMessageCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCardMessageCallbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCardMessageCallback',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeleteCardMessageCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_card_message_callback_with_options_async(
        self,
        request: dysms_20170620_models.DeleteCardMessageCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeleteCardMessageCallbackResponse:
        """
        @summary 删除消息回调
        
        @param request: DeleteCardMessageCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCardMessageCallbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCardMessageCallback',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeleteCardMessageCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_card_message_callback(
        self,
        request: dysms_20170620_models.DeleteCardMessageCallbackRequest,
    ) -> dysms_20170620_models.DeleteCardMessageCallbackResponse:
        """
        @summary 删除消息回调
        
        @param request: DeleteCardMessageCallbackRequest
        @return: DeleteCardMessageCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_card_message_callback_with_options(request, runtime)

    async def delete_card_message_callback_async(
        self,
        request: dysms_20170620_models.DeleteCardMessageCallbackRequest,
    ) -> dysms_20170620_models.DeleteCardMessageCallbackResponse:
        """
        @summary 删除消息回调
        
        @param request: DeleteCardMessageCallbackRequest
        @return: DeleteCardMessageCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_card_message_callback_with_options_async(request, runtime)

    def delete_card_message_queue_with_options(
        self,
        request: dysms_20170620_models.DeleteCardMessageQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeleteCardMessageQueueResponse:
        """
        @param request: DeleteCardMessageQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCardMessageQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.queue_type):
            query['QueueType'] = request.queue_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCardMessageQueue',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeleteCardMessageQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_card_message_queue_with_options_async(
        self,
        request: dysms_20170620_models.DeleteCardMessageQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeleteCardMessageQueueResponse:
        """
        @param request: DeleteCardMessageQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCardMessageQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.queue_type):
            query['QueueType'] = request.queue_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCardMessageQueue',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeleteCardMessageQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_card_message_queue(
        self,
        request: dysms_20170620_models.DeleteCardMessageQueueRequest,
    ) -> dysms_20170620_models.DeleteCardMessageQueueResponse:
        """
        @param request: DeleteCardMessageQueueRequest
        @return: DeleteCardMessageQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_card_message_queue_with_options(request, runtime)

    async def delete_card_message_queue_async(
        self,
        request: dysms_20170620_models.DeleteCardMessageQueueRequest,
    ) -> dysms_20170620_models.DeleteCardMessageQueueResponse:
        """
        @param request: DeleteCardMessageQueueRequest
        @return: DeleteCardMessageQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_card_message_queue_with_options_async(request, runtime)

    def delete_contacts_with_options(
        self,
        request: dysms_20170620_models.DeleteContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeleteContactsResponse:
        """
        @param request: DeleteContactsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteContactsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContacts',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeleteContactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contacts_with_options_async(
        self,
        request: dysms_20170620_models.DeleteContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeleteContactsResponse:
        """
        @param request: DeleteContactsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteContactsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContacts',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeleteContactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contacts(
        self,
        request: dysms_20170620_models.DeleteContactsRequest,
    ) -> dysms_20170620_models.DeleteContactsResponse:
        """
        @param request: DeleteContactsRequest
        @return: DeleteContactsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_contacts_with_options(request, runtime)

    async def delete_contacts_async(
        self,
        request: dysms_20170620_models.DeleteContactsRequest,
    ) -> dysms_20170620_models.DeleteContactsResponse:
        """
        @param request: DeleteContactsRequest
        @return: DeleteContactsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_contacts_with_options_async(request, runtime)

    def delete_contacts_new_with_options(
        self,
        request: dysms_20170620_models.DeleteContactsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeleteContactsNewResponse:
        """
        @param request: DeleteContactsNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteContactsNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContactsNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeleteContactsNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contacts_new_with_options_async(
        self,
        request: dysms_20170620_models.DeleteContactsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeleteContactsNewResponse:
        """
        @param request: DeleteContactsNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteContactsNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContactsNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeleteContactsNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contacts_new(
        self,
        request: dysms_20170620_models.DeleteContactsNewRequest,
    ) -> dysms_20170620_models.DeleteContactsNewResponse:
        """
        @param request: DeleteContactsNewRequest
        @return: DeleteContactsNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_contacts_new_with_options(request, runtime)

    async def delete_contacts_new_async(
        self,
        request: dysms_20170620_models.DeleteContactsNewRequest,
    ) -> dysms_20170620_models.DeleteContactsNewResponse:
        """
        @param request: DeleteContactsNewRequest
        @return: DeleteContactsNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_contacts_new_with_options_async(request, runtime)

    def delete_digital_template_new_with_options(
        self,
        request: dysms_20170620_models.DeleteDigitalTemplateNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeleteDigitalTemplateNewResponse:
        """
        @param request: DeleteDigitalTemplateNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDigitalTemplateNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_state):
            query['AuditState'] = request.audit_state
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDigitalTemplateNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeleteDigitalTemplateNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_digital_template_new_with_options_async(
        self,
        request: dysms_20170620_models.DeleteDigitalTemplateNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeleteDigitalTemplateNewResponse:
        """
        @param request: DeleteDigitalTemplateNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDigitalTemplateNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_state):
            query['AuditState'] = request.audit_state
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDigitalTemplateNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeleteDigitalTemplateNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_digital_template_new(
        self,
        request: dysms_20170620_models.DeleteDigitalTemplateNewRequest,
    ) -> dysms_20170620_models.DeleteDigitalTemplateNewResponse:
        """
        @param request: DeleteDigitalTemplateNewRequest
        @return: DeleteDigitalTemplateNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_digital_template_new_with_options(request, runtime)

    async def delete_digital_template_new_async(
        self,
        request: dysms_20170620_models.DeleteDigitalTemplateNewRequest,
    ) -> dysms_20170620_models.DeleteDigitalTemplateNewResponse:
        """
        @param request: DeleteDigitalTemplateNewRequest
        @return: DeleteDigitalTemplateNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_digital_template_new_with_options_async(request, runtime)

    def delete_message_callback_new_with_options(
        self,
        request: dysms_20170620_models.DeleteMessageCallbackNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeleteMessageCallbackNewResponse:
        """
        @param request: DeleteMessageCallbackNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMessageCallbackNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMessageCallbackNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeleteMessageCallbackNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_message_callback_new_with_options_async(
        self,
        request: dysms_20170620_models.DeleteMessageCallbackNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeleteMessageCallbackNewResponse:
        """
        @param request: DeleteMessageCallbackNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMessageCallbackNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMessageCallbackNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeleteMessageCallbackNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_message_callback_new(
        self,
        request: dysms_20170620_models.DeleteMessageCallbackNewRequest,
    ) -> dysms_20170620_models.DeleteMessageCallbackNewResponse:
        """
        @param request: DeleteMessageCallbackNewRequest
        @return: DeleteMessageCallbackNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_message_callback_new_with_options(request, runtime)

    async def delete_message_callback_new_async(
        self,
        request: dysms_20170620_models.DeleteMessageCallbackNewRequest,
    ) -> dysms_20170620_models.DeleteMessageCallbackNewResponse:
        """
        @param request: DeleteMessageCallbackNewRequest
        @return: DeleteMessageCallbackNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_message_callback_new_with_options_async(request, runtime)

    def delete_message_queue_new_with_options(
        self,
        request: dysms_20170620_models.DeleteMessageQueueNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeleteMessageQueueNewResponse:
        """
        @param request: DeleteMessageQueueNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMessageQueueNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.queue_type):
            query['QueueType'] = request.queue_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMessageQueueNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeleteMessageQueueNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_message_queue_new_with_options_async(
        self,
        request: dysms_20170620_models.DeleteMessageQueueNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeleteMessageQueueNewResponse:
        """
        @param request: DeleteMessageQueueNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMessageQueueNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.queue_type):
            query['QueueType'] = request.queue_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMessageQueueNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeleteMessageQueueNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_message_queue_new(
        self,
        request: dysms_20170620_models.DeleteMessageQueueNewRequest,
    ) -> dysms_20170620_models.DeleteMessageQueueNewResponse:
        """
        @param request: DeleteMessageQueueNewRequest
        @return: DeleteMessageQueueNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_message_queue_new_with_options(request, runtime)

    async def delete_message_queue_new_async(
        self,
        request: dysms_20170620_models.DeleteMessageQueueNewRequest,
    ) -> dysms_20170620_models.DeleteMessageQueueNewResponse:
        """
        @param request: DeleteMessageQueueNewRequest
        @return: DeleteMessageQueueNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_message_queue_new_with_options_async(request, runtime)

    def delete_or_cancele_task_with_options(
        self,
        request: dysms_20170620_models.DeleteOrCanceleTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeleteOrCanceleTaskResponse:
        """
        @param request: DeleteOrCanceleTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteOrCanceleTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_deleted):
            query['IsDeleted'] = request.is_deleted
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOrCanceleTask',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeleteOrCanceleTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_or_cancele_task_with_options_async(
        self,
        request: dysms_20170620_models.DeleteOrCanceleTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeleteOrCanceleTaskResponse:
        """
        @param request: DeleteOrCanceleTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteOrCanceleTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_deleted):
            query['IsDeleted'] = request.is_deleted
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOrCanceleTask',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeleteOrCanceleTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_or_cancele_task(
        self,
        request: dysms_20170620_models.DeleteOrCanceleTaskRequest,
    ) -> dysms_20170620_models.DeleteOrCanceleTaskResponse:
        """
        @param request: DeleteOrCanceleTaskRequest
        @return: DeleteOrCanceleTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_or_cancele_task_with_options(request, runtime)

    async def delete_or_cancele_task_async(
        self,
        request: dysms_20170620_models.DeleteOrCanceleTaskRequest,
    ) -> dysms_20170620_models.DeleteOrCanceleTaskResponse:
        """
        @param request: DeleteOrCanceleTaskRequest
        @return: DeleteOrCanceleTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_or_cancele_task_with_options_async(request, runtime)

    def delete_or_cancele_task_new_with_options(
        self,
        request: dysms_20170620_models.DeleteOrCanceleTaskNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeleteOrCanceleTaskNewResponse:
        """
        @param request: DeleteOrCanceleTaskNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteOrCanceleTaskNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_deleted):
            query['IsDeleted'] = request.is_deleted
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOrCanceleTaskNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeleteOrCanceleTaskNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_or_cancele_task_new_with_options_async(
        self,
        request: dysms_20170620_models.DeleteOrCanceleTaskNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeleteOrCanceleTaskNewResponse:
        """
        @param request: DeleteOrCanceleTaskNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteOrCanceleTaskNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_deleted):
            query['IsDeleted'] = request.is_deleted
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOrCanceleTaskNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeleteOrCanceleTaskNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_or_cancele_task_new(
        self,
        request: dysms_20170620_models.DeleteOrCanceleTaskNewRequest,
    ) -> dysms_20170620_models.DeleteOrCanceleTaskNewResponse:
        """
        @param request: DeleteOrCanceleTaskNewRequest
        @return: DeleteOrCanceleTaskNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_or_cancele_task_new_with_options(request, runtime)

    async def delete_or_cancele_task_new_async(
        self,
        request: dysms_20170620_models.DeleteOrCanceleTaskNewRequest,
    ) -> dysms_20170620_models.DeleteOrCanceleTaskNewResponse:
        """
        @param request: DeleteOrCanceleTaskNewRequest
        @return: DeleteOrCanceleTaskNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_or_cancele_task_new_with_options_async(request, runtime)

    def delete_phone_white_list_with_options(
        self,
        request: dysms_20170620_models.DeletePhoneWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeletePhoneWhiteListResponse:
        """
        @param request: DeletePhoneWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePhoneWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePhoneWhiteList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeletePhoneWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_phone_white_list_with_options_async(
        self,
        request: dysms_20170620_models.DeletePhoneWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeletePhoneWhiteListResponse:
        """
        @param request: DeletePhoneWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePhoneWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePhoneWhiteList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeletePhoneWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_phone_white_list(
        self,
        request: dysms_20170620_models.DeletePhoneWhiteListRequest,
    ) -> dysms_20170620_models.DeletePhoneWhiteListResponse:
        """
        @param request: DeletePhoneWhiteListRequest
        @return: DeletePhoneWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_phone_white_list_with_options(request, runtime)

    async def delete_phone_white_list_async(
        self,
        request: dysms_20170620_models.DeletePhoneWhiteListRequest,
    ) -> dysms_20170620_models.DeletePhoneWhiteListResponse:
        """
        @param request: DeletePhoneWhiteListRequest
        @return: DeletePhoneWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_phone_white_list_with_options_async(request, runtime)

    def delete_phone_white_list_new_with_options(
        self,
        request: dysms_20170620_models.DeletePhoneWhiteListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeletePhoneWhiteListNewResponse:
        """
        @param request: DeletePhoneWhiteListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePhoneWhiteListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePhoneWhiteListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeletePhoneWhiteListNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_phone_white_list_new_with_options_async(
        self,
        request: dysms_20170620_models.DeletePhoneWhiteListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeletePhoneWhiteListNewResponse:
        """
        @param request: DeletePhoneWhiteListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePhoneWhiteListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePhoneWhiteListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeletePhoneWhiteListNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_phone_white_list_new(
        self,
        request: dysms_20170620_models.DeletePhoneWhiteListNewRequest,
    ) -> dysms_20170620_models.DeletePhoneWhiteListNewResponse:
        """
        @param request: DeletePhoneWhiteListNewRequest
        @return: DeletePhoneWhiteListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_phone_white_list_new_with_options(request, runtime)

    async def delete_phone_white_list_new_async(
        self,
        request: dysms_20170620_models.DeletePhoneWhiteListNewRequest,
    ) -> dysms_20170620_models.DeletePhoneWhiteListNewResponse:
        """
        @param request: DeletePhoneWhiteListNewRequest
        @return: DeletePhoneWhiteListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_phone_white_list_new_with_options_async(request, runtime)

    def delete_short_url_new_with_options(
        self,
        request: dysms_20170620_models.DeleteShortUrlNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeleteShortUrlNewResponse:
        """
        @param request: DeleteShortUrlNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteShortUrlNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteShortUrlNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeleteShortUrlNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_short_url_new_with_options_async(
        self,
        request: dysms_20170620_models.DeleteShortUrlNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeleteShortUrlNewResponse:
        """
        @param request: DeleteShortUrlNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteShortUrlNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteShortUrlNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeleteShortUrlNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_short_url_new(
        self,
        request: dysms_20170620_models.DeleteShortUrlNewRequest,
    ) -> dysms_20170620_models.DeleteShortUrlNewResponse:
        """
        @param request: DeleteShortUrlNewRequest
        @return: DeleteShortUrlNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_short_url_new_with_options(request, runtime)

    async def delete_short_url_new_async(
        self,
        request: dysms_20170620_models.DeleteShortUrlNewRequest,
    ) -> dysms_20170620_models.DeleteShortUrlNewResponse:
        """
        @param request: DeleteShortUrlNewRequest
        @return: DeleteShortUrlNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_short_url_new_with_options_async(request, runtime)

    def delete_sms_template_new_with_options(
        self,
        request: dysms_20170620_models.DeleteSmsTemplateNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeleteSmsTemplateNewResponse:
        """
        @param request: DeleteSmsTemplateNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSmsTemplateNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_sms_sign):
            query['IsSmsSign'] = request.is_sms_sign
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sms_template_ids):
            query['SmsTemplateIds'] = request.sms_template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmsTemplateNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeleteSmsTemplateNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sms_template_new_with_options_async(
        self,
        request: dysms_20170620_models.DeleteSmsTemplateNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.DeleteSmsTemplateNewResponse:
        """
        @param request: DeleteSmsTemplateNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSmsTemplateNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_sms_sign):
            query['IsSmsSign'] = request.is_sms_sign
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sms_template_ids):
            query['SmsTemplateIds'] = request.sms_template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmsTemplateNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.DeleteSmsTemplateNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sms_template_new(
        self,
        request: dysms_20170620_models.DeleteSmsTemplateNewRequest,
    ) -> dysms_20170620_models.DeleteSmsTemplateNewResponse:
        """
        @param request: DeleteSmsTemplateNewRequest
        @return: DeleteSmsTemplateNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_sms_template_new_with_options(request, runtime)

    async def delete_sms_template_new_async(
        self,
        request: dysms_20170620_models.DeleteSmsTemplateNewRequest,
    ) -> dysms_20170620_models.DeleteSmsTemplateNewResponse:
        """
        @param request: DeleteSmsTemplateNewRequest
        @return: DeleteSmsTemplateNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_sms_template_new_with_options_async(request, runtime)

    def export_card_sms_history_with_options(
        self,
        request: dysms_20170620_models.ExportCardSmsHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.ExportCardSmsHistoryResponse:
        """
        @summary 发送纪录信息导出
        
        @param request: ExportCardSmsHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportCardSmsHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_send):
            query['ApiSend'] = request.api_send
        if not UtilClient.is_unset(request.card_template_type):
            query['CardTemplateType'] = request.card_template_type
        if not UtilClient.is_unset(request.gmt_create):
            query['GmtCreate'] = request.gmt_create
        if not UtilClient.is_unset(request.receive_state):
            query['ReceiveState'] = request.receive_state
        if not UtilClient.is_unset(request.receiver):
            query['Receiver'] = request.receiver
        if not UtilClient.is_unset(request.render_state):
            query['RenderState'] = request.render_state
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.tmp_code):
            query['TmpCode'] = request.tmp_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportCardSmsHistory',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.ExportCardSmsHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_card_sms_history_with_options_async(
        self,
        request: dysms_20170620_models.ExportCardSmsHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.ExportCardSmsHistoryResponse:
        """
        @summary 发送纪录信息导出
        
        @param request: ExportCardSmsHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportCardSmsHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_send):
            query['ApiSend'] = request.api_send
        if not UtilClient.is_unset(request.card_template_type):
            query['CardTemplateType'] = request.card_template_type
        if not UtilClient.is_unset(request.gmt_create):
            query['GmtCreate'] = request.gmt_create
        if not UtilClient.is_unset(request.receive_state):
            query['ReceiveState'] = request.receive_state
        if not UtilClient.is_unset(request.receiver):
            query['Receiver'] = request.receiver
        if not UtilClient.is_unset(request.render_state):
            query['RenderState'] = request.render_state
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.tmp_code):
            query['TmpCode'] = request.tmp_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportCardSmsHistory',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.ExportCardSmsHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_card_sms_history(
        self,
        request: dysms_20170620_models.ExportCardSmsHistoryRequest,
    ) -> dysms_20170620_models.ExportCardSmsHistoryResponse:
        """
        @summary 发送纪录信息导出
        
        @param request: ExportCardSmsHistoryRequest
        @return: ExportCardSmsHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_card_sms_history_with_options(request, runtime)

    async def export_card_sms_history_async(
        self,
        request: dysms_20170620_models.ExportCardSmsHistoryRequest,
    ) -> dysms_20170620_models.ExportCardSmsHistoryResponse:
        """
        @summary 发送纪录信息导出
        
        @param request: ExportCardSmsHistoryRequest
        @return: ExportCardSmsHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_card_sms_history_with_options_async(request, runtime)

    def export_card_sms_statistics_with_options(
        self,
        request: dysms_20170620_models.ExportCardSmsStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.ExportCardSmsStatisticsResponse:
        """
        @summary 导出发送统计信息-解析统计
        
        @param request: ExportCardSmsStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportCardSmsStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_tmp_code):
            query['CustomTmpCode'] = request.custom_tmp_code
        if not UtilClient.is_unset(request.send_date_end):
            query['SendDateEnd'] = request.send_date_end
        if not UtilClient.is_unset(request.send_date_start):
            query['SendDateStart'] = request.send_date_start
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.tmp_code):
            query['TmpCode'] = request.tmp_code
        if not UtilClient.is_unset(request.tmp_name):
            query['TmpName'] = request.tmp_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportCardSmsStatistics',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.ExportCardSmsStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_card_sms_statistics_with_options_async(
        self,
        request: dysms_20170620_models.ExportCardSmsStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.ExportCardSmsStatisticsResponse:
        """
        @summary 导出发送统计信息-解析统计
        
        @param request: ExportCardSmsStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportCardSmsStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_tmp_code):
            query['CustomTmpCode'] = request.custom_tmp_code
        if not UtilClient.is_unset(request.send_date_end):
            query['SendDateEnd'] = request.send_date_end
        if not UtilClient.is_unset(request.send_date_start):
            query['SendDateStart'] = request.send_date_start
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.tmp_code):
            query['TmpCode'] = request.tmp_code
        if not UtilClient.is_unset(request.tmp_name):
            query['TmpName'] = request.tmp_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportCardSmsStatistics',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.ExportCardSmsStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_card_sms_statistics(
        self,
        request: dysms_20170620_models.ExportCardSmsStatisticsRequest,
    ) -> dysms_20170620_models.ExportCardSmsStatisticsResponse:
        """
        @summary 导出发送统计信息-解析统计
        
        @param request: ExportCardSmsStatisticsRequest
        @return: ExportCardSmsStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_card_sms_statistics_with_options(request, runtime)

    async def export_card_sms_statistics_async(
        self,
        request: dysms_20170620_models.ExportCardSmsStatisticsRequest,
    ) -> dysms_20170620_models.ExportCardSmsStatisticsResponse:
        """
        @summary 导出发送统计信息-解析统计
        
        @param request: ExportCardSmsStatisticsRequest
        @return: ExportCardSmsStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_card_sms_statistics_with_options_async(request, runtime)

    def export_card_sms_statistics_send_with_options(
        self,
        request: dysms_20170620_models.ExportCardSmsStatisticsSendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.ExportCardSmsStatisticsSendResponse:
        """
        @summary 导出发送统计信息-发送+解析统计
        
        @param request: ExportCardSmsStatisticsSendRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportCardSmsStatisticsSendResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_tmp_code):
            query['CustomTmpCode'] = request.custom_tmp_code
        if not UtilClient.is_unset(request.send_date_end):
            query['SendDateEnd'] = request.send_date_end
        if not UtilClient.is_unset(request.send_date_start):
            query['SendDateStart'] = request.send_date_start
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.tmp_code):
            query['TmpCode'] = request.tmp_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportCardSmsStatisticsSend',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.ExportCardSmsStatisticsSendResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_card_sms_statistics_send_with_options_async(
        self,
        request: dysms_20170620_models.ExportCardSmsStatisticsSendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.ExportCardSmsStatisticsSendResponse:
        """
        @summary 导出发送统计信息-发送+解析统计
        
        @param request: ExportCardSmsStatisticsSendRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportCardSmsStatisticsSendResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_tmp_code):
            query['CustomTmpCode'] = request.custom_tmp_code
        if not UtilClient.is_unset(request.send_date_end):
            query['SendDateEnd'] = request.send_date_end
        if not UtilClient.is_unset(request.send_date_start):
            query['SendDateStart'] = request.send_date_start
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.tmp_code):
            query['TmpCode'] = request.tmp_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportCardSmsStatisticsSend',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.ExportCardSmsStatisticsSendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_card_sms_statistics_send(
        self,
        request: dysms_20170620_models.ExportCardSmsStatisticsSendRequest,
    ) -> dysms_20170620_models.ExportCardSmsStatisticsSendResponse:
        """
        @summary 导出发送统计信息-发送+解析统计
        
        @param request: ExportCardSmsStatisticsSendRequest
        @return: ExportCardSmsStatisticsSendResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_card_sms_statistics_send_with_options(request, runtime)

    async def export_card_sms_statistics_send_async(
        self,
        request: dysms_20170620_models.ExportCardSmsStatisticsSendRequest,
    ) -> dysms_20170620_models.ExportCardSmsStatisticsSendResponse:
        """
        @summary 导出发送统计信息-发送+解析统计
        
        @param request: ExportCardSmsStatisticsSendRequest
        @return: ExportCardSmsStatisticsSendResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_card_sms_statistics_send_with_options_async(request, runtime)

    def export_tmp_effect_report_data_with_options(
        self,
        request: dysms_20170620_models.ExportTmpEffectReportDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.ExportTmpEffectReportDataResponse:
        """
        @summary 发送效果统计导出
        
        @param request: ExportTmpEffectReportDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportTmpEffectReportDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.tmp_code):
            query['TmpCode'] = request.tmp_code
        if not UtilClient.is_unset(request.tmp_name):
            query['TmpName'] = request.tmp_name
        if not UtilClient.is_unset(request.vendor_code):
            query['VendorCode'] = request.vendor_code
        if not UtilClient.is_unset(request.vendor_name):
            query['VendorName'] = request.vendor_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportTmpEffectReportData',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.ExportTmpEffectReportDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_tmp_effect_report_data_with_options_async(
        self,
        request: dysms_20170620_models.ExportTmpEffectReportDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.ExportTmpEffectReportDataResponse:
        """
        @summary 发送效果统计导出
        
        @param request: ExportTmpEffectReportDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportTmpEffectReportDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.tmp_code):
            query['TmpCode'] = request.tmp_code
        if not UtilClient.is_unset(request.tmp_name):
            query['TmpName'] = request.tmp_name
        if not UtilClient.is_unset(request.vendor_code):
            query['VendorCode'] = request.vendor_code
        if not UtilClient.is_unset(request.vendor_name):
            query['VendorName'] = request.vendor_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportTmpEffectReportData',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.ExportTmpEffectReportDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_tmp_effect_report_data(
        self,
        request: dysms_20170620_models.ExportTmpEffectReportDataRequest,
    ) -> dysms_20170620_models.ExportTmpEffectReportDataResponse:
        """
        @summary 发送效果统计导出
        
        @param request: ExportTmpEffectReportDataRequest
        @return: ExportTmpEffectReportDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_tmp_effect_report_data_with_options(request, runtime)

    async def export_tmp_effect_report_data_async(
        self,
        request: dysms_20170620_models.ExportTmpEffectReportDataRequest,
    ) -> dysms_20170620_models.ExportTmpEffectReportDataResponse:
        """
        @summary 发送效果统计导出
        
        @param request: ExportTmpEffectReportDataRequest
        @return: ExportTmpEffectReportDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_tmp_effect_report_data_with_options_async(request, runtime)

    def get_letter_of_authorization_with_options(
        self,
        request: dysms_20170620_models.GetLetterOfAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.GetLetterOfAuthorizationResponse:
        """
        @summary 授权书下载
        
        @param request: GetLetterOfAuthorizationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLetterOfAuthorizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
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
            action='GetLetterOfAuthorization',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.GetLetterOfAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_letter_of_authorization_with_options_async(
        self,
        request: dysms_20170620_models.GetLetterOfAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.GetLetterOfAuthorizationResponse:
        """
        @summary 授权书下载
        
        @param request: GetLetterOfAuthorizationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLetterOfAuthorizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
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
            action='GetLetterOfAuthorization',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.GetLetterOfAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_letter_of_authorization(
        self,
        request: dysms_20170620_models.GetLetterOfAuthorizationRequest,
    ) -> dysms_20170620_models.GetLetterOfAuthorizationResponse:
        """
        @summary 授权书下载
        
        @param request: GetLetterOfAuthorizationRequest
        @return: GetLetterOfAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_letter_of_authorization_with_options(request, runtime)

    async def get_letter_of_authorization_async(
        self,
        request: dysms_20170620_models.GetLetterOfAuthorizationRequest,
    ) -> dysms_20170620_models.GetLetterOfAuthorizationResponse:
        """
        @summary 授权书下载
        
        @param request: GetLetterOfAuthorizationRequest
        @return: GetLetterOfAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_letter_of_authorization_with_options_async(request, runtime)

    def list_push_msg_with_options(
        self,
        request: dysms_20170620_models.ListPushMsgRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.ListPushMsgResponse:
        """
        @summary 获取推送的消息信息
        
        @param request: ListPushMsgRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPushMsgResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.msg_type):
            query['MsgType'] = request.msg_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.push_time):
            query['PushTime'] = request.push_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPushMsg',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.ListPushMsgResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_push_msg_with_options_async(
        self,
        request: dysms_20170620_models.ListPushMsgRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.ListPushMsgResponse:
        """
        @summary 获取推送的消息信息
        
        @param request: ListPushMsgRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPushMsgResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.msg_type):
            query['MsgType'] = request.msg_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.push_time):
            query['PushTime'] = request.push_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPushMsg',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.ListPushMsgResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_push_msg(
        self,
        request: dysms_20170620_models.ListPushMsgRequest,
    ) -> dysms_20170620_models.ListPushMsgResponse:
        """
        @summary 获取推送的消息信息
        
        @param request: ListPushMsgRequest
        @return: ListPushMsgResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_push_msg_with_options(request, runtime)

    async def list_push_msg_async(
        self,
        request: dysms_20170620_models.ListPushMsgRequest,
    ) -> dysms_20170620_models.ListPushMsgResponse:
        """
        @summary 获取推送的消息信息
        
        @param request: ListPushMsgRequest
        @return: ListPushMsgResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_push_msg_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: dysms_20170620_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.ListTagResourcesResponse:
        """
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
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
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tag_owner_uid):
            query['TagOwnerUid'] = request.tag_owner_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: dysms_20170620_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.ListTagResourcesResponse:
        """
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
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
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tag_owner_uid):
            query['TagOwnerUid'] = request.tag_owner_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: dysms_20170620_models.ListTagResourcesRequest,
    ) -> dysms_20170620_models.ListTagResourcesResponse:
        """
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: dysms_20170620_models.ListTagResourcesRequest,
    ) -> dysms_20170620_models.ListTagResourcesResponse:
        """
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def open_short_url_product_with_options(
        self,
        request: dysms_20170620_models.OpenShortUrlProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.OpenShortUrlProductResponse:
        """
        @param request: OpenShortUrlProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenShortUrlProductResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='OpenShortUrlProduct',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.OpenShortUrlProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_short_url_product_with_options_async(
        self,
        request: dysms_20170620_models.OpenShortUrlProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.OpenShortUrlProductResponse:
        """
        @param request: OpenShortUrlProductRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenShortUrlProductResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='OpenShortUrlProduct',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.OpenShortUrlProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_short_url_product(
        self,
        request: dysms_20170620_models.OpenShortUrlProductRequest,
    ) -> dysms_20170620_models.OpenShortUrlProductResponse:
        """
        @param request: OpenShortUrlProductRequest
        @return: OpenShortUrlProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_short_url_product_with_options(request, runtime)

    async def open_short_url_product_async(
        self,
        request: dysms_20170620_models.OpenShortUrlProductRequest,
    ) -> dysms_20170620_models.OpenShortUrlProductResponse:
        """
        @param request: OpenShortUrlProductRequest
        @return: OpenShortUrlProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_short_url_product_with_options_async(request, runtime)

    def open_short_url_product_new_with_options(
        self,
        request: dysms_20170620_models.OpenShortUrlProductNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.OpenShortUrlProductNewResponse:
        """
        @param request: OpenShortUrlProductNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenShortUrlProductNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenShortUrlProductNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.OpenShortUrlProductNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_short_url_product_new_with_options_async(
        self,
        request: dysms_20170620_models.OpenShortUrlProductNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.OpenShortUrlProductNewResponse:
        """
        @param request: OpenShortUrlProductNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenShortUrlProductNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenShortUrlProductNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.OpenShortUrlProductNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_short_url_product_new(
        self,
        request: dysms_20170620_models.OpenShortUrlProductNewRequest,
    ) -> dysms_20170620_models.OpenShortUrlProductNewResponse:
        """
        @param request: OpenShortUrlProductNewRequest
        @return: OpenShortUrlProductNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_short_url_product_new_with_options(request, runtime)

    async def open_short_url_product_new_async(
        self,
        request: dysms_20170620_models.OpenShortUrlProductNewRequest,
    ) -> dysms_20170620_models.OpenShortUrlProductNewResponse:
        """
        @param request: OpenShortUrlProductNewRequest
        @return: OpenShortUrlProductNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_short_url_product_new_with_options_async(request, runtime)

    def openc_prev_flag_new_with_options(
        self,
        request: dysms_20170620_models.OpencPrevFlagNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.OpencPrevFlagNewResponse:
        """
        @param request: OpencPrevFlagNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpencPrevFlagNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_open):
            query['IsOpen'] = request.is_open
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpencPrevFlagNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.OpencPrevFlagNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def openc_prev_flag_new_with_options_async(
        self,
        request: dysms_20170620_models.OpencPrevFlagNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.OpencPrevFlagNewResponse:
        """
        @param request: OpencPrevFlagNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpencPrevFlagNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_open):
            query['IsOpen'] = request.is_open
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpencPrevFlagNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.OpencPrevFlagNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def openc_prev_flag_new(
        self,
        request: dysms_20170620_models.OpencPrevFlagNewRequest,
    ) -> dysms_20170620_models.OpencPrevFlagNewResponse:
        """
        @param request: OpencPrevFlagNewRequest
        @return: OpencPrevFlagNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.openc_prev_flag_new_with_options(request, runtime)

    async def openc_prev_flag_new_async(
        self,
        request: dysms_20170620_models.OpencPrevFlagNewRequest,
    ) -> dysms_20170620_models.OpencPrevFlagNewResponse:
        """
        @param request: OpencPrevFlagNewRequest
        @return: OpencPrevFlagNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.openc_prev_flag_new_with_options_async(request, runtime)

    def query_any_param_template_user_with_options(
        self,
        request: dysms_20170620_models.QueryAnyParamTemplateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryAnyParamTemplateUserResponse:
        """
        @param request: QueryAnyParamTemplateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAnyParamTemplateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAnyParamTemplateUser',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryAnyParamTemplateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_any_param_template_user_with_options_async(
        self,
        request: dysms_20170620_models.QueryAnyParamTemplateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryAnyParamTemplateUserResponse:
        """
        @param request: QueryAnyParamTemplateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAnyParamTemplateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAnyParamTemplateUser',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryAnyParamTemplateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_any_param_template_user(
        self,
        request: dysms_20170620_models.QueryAnyParamTemplateUserRequest,
    ) -> dysms_20170620_models.QueryAnyParamTemplateUserResponse:
        """
        @param request: QueryAnyParamTemplateUserRequest
        @return: QueryAnyParamTemplateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_any_param_template_user_with_options(request, runtime)

    async def query_any_param_template_user_async(
        self,
        request: dysms_20170620_models.QueryAnyParamTemplateUserRequest,
    ) -> dysms_20170620_models.QueryAnyParamTemplateUserResponse:
        """
        @param request: QueryAnyParamTemplateUserRequest
        @return: QueryAnyParamTemplateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_any_param_template_user_with_options_async(request, runtime)

    def query_authorization_with_options(
        self,
        request: dysms_20170620_models.QueryAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryAuthorizationResponse:
        """
        @summary 获取授权状态
        
        @param request: QueryAuthorizationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAuthorizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorize_code):
            query['AuthorizeCode'] = request.authorize_code
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
            action='QueryAuthorization',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_authorization_with_options_async(
        self,
        request: dysms_20170620_models.QueryAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryAuthorizationResponse:
        """
        @summary 获取授权状态
        
        @param request: QueryAuthorizationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAuthorizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorize_code):
            query['AuthorizeCode'] = request.authorize_code
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
            action='QueryAuthorization',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_authorization(
        self,
        request: dysms_20170620_models.QueryAuthorizationRequest,
    ) -> dysms_20170620_models.QueryAuthorizationResponse:
        """
        @summary 获取授权状态
        
        @param request: QueryAuthorizationRequest
        @return: QueryAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_authorization_with_options(request, runtime)

    async def query_authorization_async(
        self,
        request: dysms_20170620_models.QueryAuthorizationRequest,
    ) -> dysms_20170620_models.QueryAuthorizationResponse:
        """
        @summary 获取授权状态
        
        @param request: QueryAuthorizationRequest
        @return: QueryAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_authorization_with_options_async(request, runtime)

    def query_billing_statistics_with_options(
        self,
        request: dysms_20170620_models.QueryBillingStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryBillingStatisticsResponse:
        """
        @param request: QueryBillingStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryBillingStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not UtilClient.is_unset(request.item_name):
            query['ItemName'] = request.item_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBillingStatistics',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryBillingStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_billing_statistics_with_options_async(
        self,
        request: dysms_20170620_models.QueryBillingStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryBillingStatisticsResponse:
        """
        @param request: QueryBillingStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryBillingStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not UtilClient.is_unset(request.item_name):
            query['ItemName'] = request.item_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBillingStatistics',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryBillingStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_billing_statistics(
        self,
        request: dysms_20170620_models.QueryBillingStatisticsRequest,
    ) -> dysms_20170620_models.QueryBillingStatisticsResponse:
        """
        @param request: QueryBillingStatisticsRequest
        @return: QueryBillingStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_billing_statistics_with_options(request, runtime)

    async def query_billing_statistics_async(
        self,
        request: dysms_20170620_models.QueryBillingStatisticsRequest,
    ) -> dysms_20170620_models.QueryBillingStatisticsResponse:
        """
        @param request: QueryBillingStatisticsRequest
        @return: QueryBillingStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_billing_statistics_with_options_async(request, runtime)

    def query_card_message_queue_with_options(
        self,
        request: dysms_20170620_models.QueryCardMessageQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryCardMessageQueueResponse:
        """
        @param request: QueryCardMessageQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCardMessageQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.queue_types):
            query['QueueTypes'] = request.queue_types
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCardMessageQueue',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryCardMessageQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_card_message_queue_with_options_async(
        self,
        request: dysms_20170620_models.QueryCardMessageQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryCardMessageQueueResponse:
        """
        @param request: QueryCardMessageQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCardMessageQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.queue_types):
            query['QueueTypes'] = request.queue_types
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCardMessageQueue',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryCardMessageQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_card_message_queue(
        self,
        request: dysms_20170620_models.QueryCardMessageQueueRequest,
    ) -> dysms_20170620_models.QueryCardMessageQueueResponse:
        """
        @param request: QueryCardMessageQueueRequest
        @return: QueryCardMessageQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_card_message_queue_with_options(request, runtime)

    async def query_card_message_queue_async(
        self,
        request: dysms_20170620_models.QueryCardMessageQueueRequest,
    ) -> dysms_20170620_models.QueryCardMessageQueueResponse:
        """
        @param request: QueryCardMessageQueueRequest
        @return: QueryCardMessageQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_card_message_queue_with_options_async(request, runtime)

    def query_card_send_export_info_with_options(
        self,
        request: dysms_20170620_models.QueryCardSendExportInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryCardSendExportInfoResponse:
        """
        @summary 查询发送记录导出信息
        
        @param request: QueryCardSendExportInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCardSendExportInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCardSendExportInfo',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryCardSendExportInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_card_send_export_info_with_options_async(
        self,
        request: dysms_20170620_models.QueryCardSendExportInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryCardSendExportInfoResponse:
        """
        @summary 查询发送记录导出信息
        
        @param request: QueryCardSendExportInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCardSendExportInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCardSendExportInfo',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryCardSendExportInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_card_send_export_info(
        self,
        request: dysms_20170620_models.QueryCardSendExportInfoRequest,
    ) -> dysms_20170620_models.QueryCardSendExportInfoResponse:
        """
        @summary 查询发送记录导出信息
        
        @param request: QueryCardSendExportInfoRequest
        @return: QueryCardSendExportInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_card_send_export_info_with_options(request, runtime)

    async def query_card_send_export_info_async(
        self,
        request: dysms_20170620_models.QueryCardSendExportInfoRequest,
    ) -> dysms_20170620_models.QueryCardSendExportInfoResponse:
        """
        @summary 查询发送记录导出信息
        
        @param request: QueryCardSendExportInfoRequest
        @return: QueryCardSendExportInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_card_send_export_info_with_options_async(request, runtime)

    def query_card_sms_history_with_options(
        self,
        request: dysms_20170620_models.QueryCardSmsHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryCardSmsHistoryResponse:
        """
        @summary 分页查询发送纪录信息
        
        @param request: QueryCardSmsHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCardSmsHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_send):
            query['ApiSend'] = request.api_send
        if not UtilClient.is_unset(request.card_template_type):
            query['CardTemplateType'] = request.card_template_type
        if not UtilClient.is_unset(request.gmt_create):
            query['GmtCreate'] = request.gmt_create
        if not UtilClient.is_unset(request.max_id):
            query['MaxId'] = request.max_id
        if not UtilClient.is_unset(request.min_id):
            query['MinId'] = request.min_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.receive_state):
            query['ReceiveState'] = request.receive_state
        if not UtilClient.is_unset(request.receiver):
            query['Receiver'] = request.receiver
        if not UtilClient.is_unset(request.render_state):
            query['RenderState'] = request.render_state
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.tmp_code):
            query['TmpCode'] = request.tmp_code
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCardSmsHistory',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryCardSmsHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_card_sms_history_with_options_async(
        self,
        request: dysms_20170620_models.QueryCardSmsHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryCardSmsHistoryResponse:
        """
        @summary 分页查询发送纪录信息
        
        @param request: QueryCardSmsHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCardSmsHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_send):
            query['ApiSend'] = request.api_send
        if not UtilClient.is_unset(request.card_template_type):
            query['CardTemplateType'] = request.card_template_type
        if not UtilClient.is_unset(request.gmt_create):
            query['GmtCreate'] = request.gmt_create
        if not UtilClient.is_unset(request.max_id):
            query['MaxId'] = request.max_id
        if not UtilClient.is_unset(request.min_id):
            query['MinId'] = request.min_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.receive_state):
            query['ReceiveState'] = request.receive_state
        if not UtilClient.is_unset(request.receiver):
            query['Receiver'] = request.receiver
        if not UtilClient.is_unset(request.render_state):
            query['RenderState'] = request.render_state
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.tmp_code):
            query['TmpCode'] = request.tmp_code
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCardSmsHistory',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryCardSmsHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_card_sms_history(
        self,
        request: dysms_20170620_models.QueryCardSmsHistoryRequest,
    ) -> dysms_20170620_models.QueryCardSmsHistoryResponse:
        """
        @summary 分页查询发送纪录信息
        
        @param request: QueryCardSmsHistoryRequest
        @return: QueryCardSmsHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_card_sms_history_with_options(request, runtime)

    async def query_card_sms_history_async(
        self,
        request: dysms_20170620_models.QueryCardSmsHistoryRequest,
    ) -> dysms_20170620_models.QueryCardSmsHistoryResponse:
        """
        @summary 分页查询发送纪录信息
        
        @param request: QueryCardSmsHistoryRequest
        @return: QueryCardSmsHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_card_sms_history_with_options_async(request, runtime)

    def query_card_sms_history_detail_with_options(
        self,
        request: dysms_20170620_models.QueryCardSmsHistoryDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryCardSmsHistoryDetailResponse:
        """
        @summary 查询发送纪录信息详情
        
        @param request: QueryCardSmsHistoryDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCardSmsHistoryDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gmt_create):
            query['GmtCreate'] = request.gmt_create
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCardSmsHistoryDetail',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryCardSmsHistoryDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_card_sms_history_detail_with_options_async(
        self,
        request: dysms_20170620_models.QueryCardSmsHistoryDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryCardSmsHistoryDetailResponse:
        """
        @summary 查询发送纪录信息详情
        
        @param request: QueryCardSmsHistoryDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCardSmsHistoryDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gmt_create):
            query['GmtCreate'] = request.gmt_create
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCardSmsHistoryDetail',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryCardSmsHistoryDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_card_sms_history_detail(
        self,
        request: dysms_20170620_models.QueryCardSmsHistoryDetailRequest,
    ) -> dysms_20170620_models.QueryCardSmsHistoryDetailResponse:
        """
        @summary 查询发送纪录信息详情
        
        @param request: QueryCardSmsHistoryDetailRequest
        @return: QueryCardSmsHistoryDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_card_sms_history_detail_with_options(request, runtime)

    async def query_card_sms_history_detail_async(
        self,
        request: dysms_20170620_models.QueryCardSmsHistoryDetailRequest,
    ) -> dysms_20170620_models.QueryCardSmsHistoryDetailResponse:
        """
        @summary 查询发送纪录信息详情
        
        @param request: QueryCardSmsHistoryDetailRequest
        @return: QueryCardSmsHistoryDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_card_sms_history_detail_with_options_async(request, runtime)

    def query_card_sms_statistics_with_options(
        self,
        request: dysms_20170620_models.QueryCardSmsStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryCardSmsStatisticsResponse:
        """
        @summary 分页查询发送统计信息-解析统计
        
        @param request: QueryCardSmsStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCardSmsStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_tmp_code):
            query['CustomTmpCode'] = request.custom_tmp_code
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.send_date_end):
            query['SendDateEnd'] = request.send_date_end
        if not UtilClient.is_unset(request.send_date_start):
            query['SendDateStart'] = request.send_date_start
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.tmp_code):
            query['TmpCode'] = request.tmp_code
        if not UtilClient.is_unset(request.tmp_name):
            query['TmpName'] = request.tmp_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCardSmsStatistics',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryCardSmsStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_card_sms_statistics_with_options_async(
        self,
        request: dysms_20170620_models.QueryCardSmsStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryCardSmsStatisticsResponse:
        """
        @summary 分页查询发送统计信息-解析统计
        
        @param request: QueryCardSmsStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCardSmsStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_tmp_code):
            query['CustomTmpCode'] = request.custom_tmp_code
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.send_date_end):
            query['SendDateEnd'] = request.send_date_end
        if not UtilClient.is_unset(request.send_date_start):
            query['SendDateStart'] = request.send_date_start
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.tmp_code):
            query['TmpCode'] = request.tmp_code
        if not UtilClient.is_unset(request.tmp_name):
            query['TmpName'] = request.tmp_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCardSmsStatistics',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryCardSmsStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_card_sms_statistics(
        self,
        request: dysms_20170620_models.QueryCardSmsStatisticsRequest,
    ) -> dysms_20170620_models.QueryCardSmsStatisticsResponse:
        """
        @summary 分页查询发送统计信息-解析统计
        
        @param request: QueryCardSmsStatisticsRequest
        @return: QueryCardSmsStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_card_sms_statistics_with_options(request, runtime)

    async def query_card_sms_statistics_async(
        self,
        request: dysms_20170620_models.QueryCardSmsStatisticsRequest,
    ) -> dysms_20170620_models.QueryCardSmsStatisticsResponse:
        """
        @summary 分页查询发送统计信息-解析统计
        
        @param request: QueryCardSmsStatisticsRequest
        @return: QueryCardSmsStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_card_sms_statistics_with_options_async(request, runtime)

    def query_card_sms_statistics_list_with_options(
        self,
        request: dysms_20170620_models.QueryCardSmsStatisticsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryCardSmsStatisticsListResponse:
        """
        @summary 按时间查询发送统计信息-解析统计
        
        @param request: QueryCardSmsStatisticsListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCardSmsStatisticsListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_tmp_code):
            query['CustomTmpCode'] = request.custom_tmp_code
        if not UtilClient.is_unset(request.send_date_end):
            query['SendDateEnd'] = request.send_date_end
        if not UtilClient.is_unset(request.send_date_start):
            query['SendDateStart'] = request.send_date_start
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.tmp_code):
            query['TmpCode'] = request.tmp_code
        if not UtilClient.is_unset(request.tmp_name):
            query['TmpName'] = request.tmp_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCardSmsStatisticsList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryCardSmsStatisticsListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_card_sms_statistics_list_with_options_async(
        self,
        request: dysms_20170620_models.QueryCardSmsStatisticsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryCardSmsStatisticsListResponse:
        """
        @summary 按时间查询发送统计信息-解析统计
        
        @param request: QueryCardSmsStatisticsListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCardSmsStatisticsListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_tmp_code):
            query['CustomTmpCode'] = request.custom_tmp_code
        if not UtilClient.is_unset(request.send_date_end):
            query['SendDateEnd'] = request.send_date_end
        if not UtilClient.is_unset(request.send_date_start):
            query['SendDateStart'] = request.send_date_start
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.tmp_code):
            query['TmpCode'] = request.tmp_code
        if not UtilClient.is_unset(request.tmp_name):
            query['TmpName'] = request.tmp_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCardSmsStatisticsList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryCardSmsStatisticsListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_card_sms_statistics_list(
        self,
        request: dysms_20170620_models.QueryCardSmsStatisticsListRequest,
    ) -> dysms_20170620_models.QueryCardSmsStatisticsListResponse:
        """
        @summary 按时间查询发送统计信息-解析统计
        
        @param request: QueryCardSmsStatisticsListRequest
        @return: QueryCardSmsStatisticsListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_card_sms_statistics_list_with_options(request, runtime)

    async def query_card_sms_statistics_list_async(
        self,
        request: dysms_20170620_models.QueryCardSmsStatisticsListRequest,
    ) -> dysms_20170620_models.QueryCardSmsStatisticsListResponse:
        """
        @summary 按时间查询发送统计信息-解析统计
        
        @param request: QueryCardSmsStatisticsListRequest
        @return: QueryCardSmsStatisticsListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_card_sms_statistics_list_with_options_async(request, runtime)

    def query_card_sms_statistics_send_with_options(
        self,
        request: dysms_20170620_models.QueryCardSmsStatisticsSendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryCardSmsStatisticsSendResponse:
        """
        @summary 分页查询发送统计信息-发送+解析统计
        
        @param request: QueryCardSmsStatisticsSendRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCardSmsStatisticsSendResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_tmp_code):
            query['CustomTmpCode'] = request.custom_tmp_code
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.send_date_end):
            query['SendDateEnd'] = request.send_date_end
        if not UtilClient.is_unset(request.send_date_start):
            query['SendDateStart'] = request.send_date_start
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.tmp_code):
            query['TmpCode'] = request.tmp_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCardSmsStatisticsSend',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryCardSmsStatisticsSendResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_card_sms_statistics_send_with_options_async(
        self,
        request: dysms_20170620_models.QueryCardSmsStatisticsSendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryCardSmsStatisticsSendResponse:
        """
        @summary 分页查询发送统计信息-发送+解析统计
        
        @param request: QueryCardSmsStatisticsSendRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCardSmsStatisticsSendResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_tmp_code):
            query['CustomTmpCode'] = request.custom_tmp_code
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.send_date_end):
            query['SendDateEnd'] = request.send_date_end
        if not UtilClient.is_unset(request.send_date_start):
            query['SendDateStart'] = request.send_date_start
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.tmp_code):
            query['TmpCode'] = request.tmp_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCardSmsStatisticsSend',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryCardSmsStatisticsSendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_card_sms_statistics_send(
        self,
        request: dysms_20170620_models.QueryCardSmsStatisticsSendRequest,
    ) -> dysms_20170620_models.QueryCardSmsStatisticsSendResponse:
        """
        @summary 分页查询发送统计信息-发送+解析统计
        
        @param request: QueryCardSmsStatisticsSendRequest
        @return: QueryCardSmsStatisticsSendResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_card_sms_statistics_send_with_options(request, runtime)

    async def query_card_sms_statistics_send_async(
        self,
        request: dysms_20170620_models.QueryCardSmsStatisticsSendRequest,
    ) -> dysms_20170620_models.QueryCardSmsStatisticsSendResponse:
        """
        @summary 分页查询发送统计信息-发送+解析统计
        
        @param request: QueryCardSmsStatisticsSendRequest
        @return: QueryCardSmsStatisticsSendResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_card_sms_statistics_send_with_options_async(request, runtime)

    def query_card_sms_statistics_send_list_with_options(
        self,
        request: dysms_20170620_models.QueryCardSmsStatisticsSendListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryCardSmsStatisticsSendListResponse:
        """
        @summary 按日期查询发送统计信息-发送+解析统计
        
        @param request: QueryCardSmsStatisticsSendListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCardSmsStatisticsSendListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_tmp_code):
            query['CustomTmpCode'] = request.custom_tmp_code
        if not UtilClient.is_unset(request.send_date_end):
            query['SendDateEnd'] = request.send_date_end
        if not UtilClient.is_unset(request.send_date_start):
            query['SendDateStart'] = request.send_date_start
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.tmp_code):
            query['TmpCode'] = request.tmp_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCardSmsStatisticsSendList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryCardSmsStatisticsSendListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_card_sms_statistics_send_list_with_options_async(
        self,
        request: dysms_20170620_models.QueryCardSmsStatisticsSendListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryCardSmsStatisticsSendListResponse:
        """
        @summary 按日期查询发送统计信息-发送+解析统计
        
        @param request: QueryCardSmsStatisticsSendListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCardSmsStatisticsSendListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_tmp_code):
            query['CustomTmpCode'] = request.custom_tmp_code
        if not UtilClient.is_unset(request.send_date_end):
            query['SendDateEnd'] = request.send_date_end
        if not UtilClient.is_unset(request.send_date_start):
            query['SendDateStart'] = request.send_date_start
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.tmp_code):
            query['TmpCode'] = request.tmp_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCardSmsStatisticsSendList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryCardSmsStatisticsSendListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_card_sms_statistics_send_list(
        self,
        request: dysms_20170620_models.QueryCardSmsStatisticsSendListRequest,
    ) -> dysms_20170620_models.QueryCardSmsStatisticsSendListResponse:
        """
        @summary 按日期查询发送统计信息-发送+解析统计
        
        @param request: QueryCardSmsStatisticsSendListRequest
        @return: QueryCardSmsStatisticsSendListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_card_sms_statistics_send_list_with_options(request, runtime)

    async def query_card_sms_statistics_send_list_async(
        self,
        request: dysms_20170620_models.QueryCardSmsStatisticsSendListRequest,
    ) -> dysms_20170620_models.QueryCardSmsStatisticsSendListResponse:
        """
        @summary 按日期查询发送统计信息-发送+解析统计
        
        @param request: QueryCardSmsStatisticsSendListRequest
        @return: QueryCardSmsStatisticsSendListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_card_sms_statistics_send_list_with_options_async(request, runtime)

    def query_common_cust_info_with_options(
        self,
        request: dysms_20170620_models.QueryCommonCustInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryCommonCustInfoResponse:
        """
        @param request: QueryCommonCustInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCommonCustInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCommonCustInfo',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryCommonCustInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_common_cust_info_with_options_async(
        self,
        request: dysms_20170620_models.QueryCommonCustInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryCommonCustInfoResponse:
        """
        @param request: QueryCommonCustInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCommonCustInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCommonCustInfo',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryCommonCustInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_common_cust_info(
        self,
        request: dysms_20170620_models.QueryCommonCustInfoRequest,
    ) -> dysms_20170620_models.QueryCommonCustInfoResponse:
        """
        @param request: QueryCommonCustInfoRequest
        @return: QueryCommonCustInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_common_cust_info_with_options(request, runtime)

    async def query_common_cust_info_async(
        self,
        request: dysms_20170620_models.QueryCommonCustInfoRequest,
    ) -> dysms_20170620_models.QueryCommonCustInfoResponse:
        """
        @param request: QueryCommonCustInfoRequest
        @return: QueryCommonCustInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_common_cust_info_with_options_async(request, runtime)

    def query_contacts_list_with_options(
        self,
        request: dysms_20170620_models.QueryContactsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryContactsListResponse:
        """
        @param request: QueryContactsListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryContactsListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryContactsList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryContactsListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_contacts_list_with_options_async(
        self,
        request: dysms_20170620_models.QueryContactsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryContactsListResponse:
        """
        @param request: QueryContactsListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryContactsListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryContactsList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryContactsListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_contacts_list(
        self,
        request: dysms_20170620_models.QueryContactsListRequest,
    ) -> dysms_20170620_models.QueryContactsListResponse:
        """
        @param request: QueryContactsListRequest
        @return: QueryContactsListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_contacts_list_with_options(request, runtime)

    async def query_contacts_list_async(
        self,
        request: dysms_20170620_models.QueryContactsListRequest,
    ) -> dysms_20170620_models.QueryContactsListResponse:
        """
        @param request: QueryContactsListRequest
        @return: QueryContactsListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_contacts_list_with_options_async(request, runtime)

    def query_contacts_list_new_with_options(
        self,
        request: dysms_20170620_models.QueryContactsListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryContactsListNewResponse:
        """
        @param request: QueryContactsListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryContactsListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryContactsListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryContactsListNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_contacts_list_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryContactsListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryContactsListNewResponse:
        """
        @param request: QueryContactsListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryContactsListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryContactsListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryContactsListNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_contacts_list_new(
        self,
        request: dysms_20170620_models.QueryContactsListNewRequest,
    ) -> dysms_20170620_models.QueryContactsListNewResponse:
        """
        @param request: QueryContactsListNewRequest
        @return: QueryContactsListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_contacts_list_new_with_options(request, runtime)

    async def query_contacts_list_new_async(
        self,
        request: dysms_20170620_models.QueryContactsListNewRequest,
    ) -> dysms_20170620_models.QueryContactsListNewResponse:
        """
        @param request: QueryContactsListNewRequest
        @return: QueryContactsListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_contacts_list_new_with_options_async(request, runtime)

    def query_daily_bill_info_leaf_new_with_options(
        self,
        request: dysms_20170620_models.QueryDailyBillInfoLeafNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryDailyBillInfoLeafNewResponse:
        """
        @param request: QueryDailyBillInfoLeafNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDailyBillInfoLeafNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.item_name):
            query['ItemName'] = request.item_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subject_item_id):
            query['SubjectItemId'] = request.subject_item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDailyBillInfoLeafNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryDailyBillInfoLeafNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_daily_bill_info_leaf_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryDailyBillInfoLeafNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryDailyBillInfoLeafNewResponse:
        """
        @param request: QueryDailyBillInfoLeafNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDailyBillInfoLeafNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.item_name):
            query['ItemName'] = request.item_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subject_item_id):
            query['SubjectItemId'] = request.subject_item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDailyBillInfoLeafNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryDailyBillInfoLeafNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_daily_bill_info_leaf_new(
        self,
        request: dysms_20170620_models.QueryDailyBillInfoLeafNewRequest,
    ) -> dysms_20170620_models.QueryDailyBillInfoLeafNewResponse:
        """
        @param request: QueryDailyBillInfoLeafNewRequest
        @return: QueryDailyBillInfoLeafNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_daily_bill_info_leaf_new_with_options(request, runtime)

    async def query_daily_bill_info_leaf_new_async(
        self,
        request: dysms_20170620_models.QueryDailyBillInfoLeafNewRequest,
    ) -> dysms_20170620_models.QueryDailyBillInfoLeafNewResponse:
        """
        @param request: QueryDailyBillInfoLeafNewRequest
        @return: QueryDailyBillInfoLeafNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_daily_bill_info_leaf_new_with_options_async(request, runtime)

    def query_digital_template_detail_with_options(
        self,
        request: dysms_20170620_models.QueryDigitalTemplateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryDigitalTemplateDetailResponse:
        """
        @param request: QueryDigitalTemplateDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDigitalTemplateDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_state):
            query['AuditState'] = request.audit_state
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDigitalTemplateDetail',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryDigitalTemplateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_digital_template_detail_with_options_async(
        self,
        request: dysms_20170620_models.QueryDigitalTemplateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryDigitalTemplateDetailResponse:
        """
        @param request: QueryDigitalTemplateDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDigitalTemplateDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_state):
            query['AuditState'] = request.audit_state
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDigitalTemplateDetail',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryDigitalTemplateDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_digital_template_detail(
        self,
        request: dysms_20170620_models.QueryDigitalTemplateDetailRequest,
    ) -> dysms_20170620_models.QueryDigitalTemplateDetailResponse:
        """
        @param request: QueryDigitalTemplateDetailRequest
        @return: QueryDigitalTemplateDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_digital_template_detail_with_options(request, runtime)

    async def query_digital_template_detail_async(
        self,
        request: dysms_20170620_models.QueryDigitalTemplateDetailRequest,
    ) -> dysms_20170620_models.QueryDigitalTemplateDetailResponse:
        """
        @param request: QueryDigitalTemplateDetailRequest
        @return: QueryDigitalTemplateDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_digital_template_detail_with_options_async(request, runtime)

    def query_digital_template_detail_new_with_options(
        self,
        request: dysms_20170620_models.QueryDigitalTemplateDetailNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryDigitalTemplateDetailNewResponse:
        """
        @param request: QueryDigitalTemplateDetailNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDigitalTemplateDetailNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_state):
            query['AuditState'] = request.audit_state
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDigitalTemplateDetailNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryDigitalTemplateDetailNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_digital_template_detail_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryDigitalTemplateDetailNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryDigitalTemplateDetailNewResponse:
        """
        @param request: QueryDigitalTemplateDetailNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDigitalTemplateDetailNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_state):
            query['AuditState'] = request.audit_state
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDigitalTemplateDetailNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryDigitalTemplateDetailNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_digital_template_detail_new(
        self,
        request: dysms_20170620_models.QueryDigitalTemplateDetailNewRequest,
    ) -> dysms_20170620_models.QueryDigitalTemplateDetailNewResponse:
        """
        @param request: QueryDigitalTemplateDetailNewRequest
        @return: QueryDigitalTemplateDetailNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_digital_template_detail_new_with_options(request, runtime)

    async def query_digital_template_detail_new_async(
        self,
        request: dysms_20170620_models.QueryDigitalTemplateDetailNewRequest,
    ) -> dysms_20170620_models.QueryDigitalTemplateDetailNewResponse:
        """
        @param request: QueryDigitalTemplateDetailNewRequest
        @return: QueryDigitalTemplateDetailNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_digital_template_detail_new_with_options_async(request, runtime)

    def query_digital_template_last_range_with_options(
        self,
        request: dysms_20170620_models.QueryDigitalTemplateLastRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryDigitalTemplateLastRangeResponse:
        """
        @param request: QueryDigitalTemplateLastRangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDigitalTemplateLastRangeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDigitalTemplateLastRange',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryDigitalTemplateLastRangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_digital_template_last_range_with_options_async(
        self,
        request: dysms_20170620_models.QueryDigitalTemplateLastRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryDigitalTemplateLastRangeResponse:
        """
        @param request: QueryDigitalTemplateLastRangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDigitalTemplateLastRangeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDigitalTemplateLastRange',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryDigitalTemplateLastRangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_digital_template_last_range(
        self,
        request: dysms_20170620_models.QueryDigitalTemplateLastRangeRequest,
    ) -> dysms_20170620_models.QueryDigitalTemplateLastRangeResponse:
        """
        @param request: QueryDigitalTemplateLastRangeRequest
        @return: QueryDigitalTemplateLastRangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_digital_template_last_range_with_options(request, runtime)

    async def query_digital_template_last_range_async(
        self,
        request: dysms_20170620_models.QueryDigitalTemplateLastRangeRequest,
    ) -> dysms_20170620_models.QueryDigitalTemplateLastRangeResponse:
        """
        @param request: QueryDigitalTemplateLastRangeRequest
        @return: QueryDigitalTemplateLastRangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_digital_template_last_range_with_options_async(request, runtime)

    def query_digital_template_last_range_new_with_options(
        self,
        request: dysms_20170620_models.QueryDigitalTemplateLastRangeNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryDigitalTemplateLastRangeNewResponse:
        """
        @param request: QueryDigitalTemplateLastRangeNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDigitalTemplateLastRangeNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_state):
            query['AuditState'] = request.audit_state
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_type):
            query['ProdType'] = request.prod_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDigitalTemplateLastRangeNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryDigitalTemplateLastRangeNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_digital_template_last_range_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryDigitalTemplateLastRangeNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryDigitalTemplateLastRangeNewResponse:
        """
        @param request: QueryDigitalTemplateLastRangeNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDigitalTemplateLastRangeNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_state):
            query['AuditState'] = request.audit_state
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_type):
            query['ProdType'] = request.prod_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDigitalTemplateLastRangeNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryDigitalTemplateLastRangeNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_digital_template_last_range_new(
        self,
        request: dysms_20170620_models.QueryDigitalTemplateLastRangeNewRequest,
    ) -> dysms_20170620_models.QueryDigitalTemplateLastRangeNewResponse:
        """
        @param request: QueryDigitalTemplateLastRangeNewRequest
        @return: QueryDigitalTemplateLastRangeNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_digital_template_last_range_new_with_options(request, runtime)

    async def query_digital_template_last_range_new_async(
        self,
        request: dysms_20170620_models.QueryDigitalTemplateLastRangeNewRequest,
    ) -> dysms_20170620_models.QueryDigitalTemplateLastRangeNewResponse:
        """
        @param request: QueryDigitalTemplateLastRangeNewRequest
        @return: QueryDigitalTemplateLastRangeNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_digital_template_last_range_new_with_options_async(request, runtime)

    def query_digital_template_page_list_with_options(
        self,
        request: dysms_20170620_models.QueryDigitalTemplatePageListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryDigitalTemplatePageListResponse:
        """
        @param request: QueryDigitalTemplatePageListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDigitalTemplatePageListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_state):
            query['AuditState'] = request.audit_state
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDigitalTemplatePageList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryDigitalTemplatePageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_digital_template_page_list_with_options_async(
        self,
        request: dysms_20170620_models.QueryDigitalTemplatePageListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryDigitalTemplatePageListResponse:
        """
        @param request: QueryDigitalTemplatePageListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDigitalTemplatePageListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_state):
            query['AuditState'] = request.audit_state
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDigitalTemplatePageList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryDigitalTemplatePageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_digital_template_page_list(
        self,
        request: dysms_20170620_models.QueryDigitalTemplatePageListRequest,
    ) -> dysms_20170620_models.QueryDigitalTemplatePageListResponse:
        """
        @param request: QueryDigitalTemplatePageListRequest
        @return: QueryDigitalTemplatePageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_digital_template_page_list_with_options(request, runtime)

    async def query_digital_template_page_list_async(
        self,
        request: dysms_20170620_models.QueryDigitalTemplatePageListRequest,
    ) -> dysms_20170620_models.QueryDigitalTemplatePageListResponse:
        """
        @param request: QueryDigitalTemplatePageListRequest
        @return: QueryDigitalTemplatePageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_digital_template_page_list_with_options_async(request, runtime)

    def query_digital_template_page_list_new_with_options(
        self,
        request: dysms_20170620_models.QueryDigitalTemplatePageListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryDigitalTemplatePageListNewResponse:
        """
        @param request: QueryDigitalTemplatePageListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDigitalTemplatePageListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_state):
            query['AuditState'] = request.audit_state
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDigitalTemplatePageListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryDigitalTemplatePageListNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_digital_template_page_list_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryDigitalTemplatePageListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryDigitalTemplatePageListNewResponse:
        """
        @param request: QueryDigitalTemplatePageListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDigitalTemplatePageListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_state):
            query['AuditState'] = request.audit_state
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDigitalTemplatePageListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryDigitalTemplatePageListNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_digital_template_page_list_new(
        self,
        request: dysms_20170620_models.QueryDigitalTemplatePageListNewRequest,
    ) -> dysms_20170620_models.QueryDigitalTemplatePageListNewResponse:
        """
        @param request: QueryDigitalTemplatePageListNewRequest
        @return: QueryDigitalTemplatePageListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_digital_template_page_list_new_with_options(request, runtime)

    async def query_digital_template_page_list_new_async(
        self,
        request: dysms_20170620_models.QueryDigitalTemplatePageListNewRequest,
    ) -> dysms_20170620_models.QueryDigitalTemplatePageListNewResponse:
        """
        @param request: QueryDigitalTemplatePageListNewRequest
        @return: QueryDigitalTemplatePageListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_digital_template_page_list_new_with_options_async(request, runtime)

    def query_domain_list_with_options(
        self,
        request: dysms_20170620_models.QueryDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryDomainListResponse:
        """
        @param request: QueryDomainListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_list_with_options_async(
        self,
        request: dysms_20170620_models.QueryDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryDomainListResponse:
        """
        @param request: QueryDomainListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryDomainListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_list(
        self,
        request: dysms_20170620_models.QueryDomainListRequest,
    ) -> dysms_20170620_models.QueryDomainListResponse:
        """
        @param request: QueryDomainListRequest
        @return: QueryDomainListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_domain_list_with_options(request, runtime)

    async def query_domain_list_async(
        self,
        request: dysms_20170620_models.QueryDomainListRequest,
    ) -> dysms_20170620_models.QueryDomainListResponse:
        """
        @param request: QueryDomainListRequest
        @return: QueryDomainListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_list_with_options_async(request, runtime)

    def query_domain_list_new_with_options(
        self,
        request: dysms_20170620_models.QueryDomainListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryDomainListNewResponse:
        """
        @param request: QueryDomainListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryDomainListNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_list_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryDomainListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryDomainListNewResponse:
        """
        @param request: QueryDomainListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDomainListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryDomainListNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_list_new(
        self,
        request: dysms_20170620_models.QueryDomainListNewRequest,
    ) -> dysms_20170620_models.QueryDomainListNewResponse:
        """
        @param request: QueryDomainListNewRequest
        @return: QueryDomainListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_domain_list_new_with_options(request, runtime)

    async def query_domain_list_new_async(
        self,
        request: dysms_20170620_models.QueryDomainListNewRequest,
    ) -> dysms_20170620_models.QueryDomainListNewResponse:
        """
        @param request: QueryDomainListNewRequest
        @return: QueryDomainListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_domain_list_new_with_options_async(request, runtime)

    def query_export_send_record_list_new_with_options(
        self,
        request: dysms_20170620_models.QueryExportSendRecordListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryExportSendRecordListNewResponse:
        """
        @param request: QueryExportSendRecordListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryExportSendRecordListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_status):
            query['ApplyStatus'] = request.apply_status
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryExportSendRecordListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryExportSendRecordListNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_export_send_record_list_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryExportSendRecordListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryExportSendRecordListNewResponse:
        """
        @param request: QueryExportSendRecordListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryExportSendRecordListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_status):
            query['ApplyStatus'] = request.apply_status
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryExportSendRecordListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryExportSendRecordListNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_export_send_record_list_new(
        self,
        request: dysms_20170620_models.QueryExportSendRecordListNewRequest,
    ) -> dysms_20170620_models.QueryExportSendRecordListNewResponse:
        """
        @param request: QueryExportSendRecordListNewRequest
        @return: QueryExportSendRecordListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_export_send_record_list_new_with_options(request, runtime)

    async def query_export_send_record_list_new_async(
        self,
        request: dysms_20170620_models.QueryExportSendRecordListNewRequest,
    ) -> dysms_20170620_models.QueryExportSendRecordListNewResponse:
        """
        @param request: QueryExportSendRecordListNewRequest
        @return: QueryExportSendRecordListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_export_send_record_list_new_with_options_async(request, runtime)

    def query_fail_detail_download_with_options(
        self,
        request: dysms_20170620_models.QueryFailDetailDownloadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryFailDetailDownloadResponse:
        """
        @param request: QueryFailDetailDownloadRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFailDetailDownloadResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_instance_id):
            query['TaskInstanceId'] = request.task_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFailDetailDownload',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryFailDetailDownloadResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_fail_detail_download_with_options_async(
        self,
        request: dysms_20170620_models.QueryFailDetailDownloadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryFailDetailDownloadResponse:
        """
        @param request: QueryFailDetailDownloadRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFailDetailDownloadResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_instance_id):
            query['TaskInstanceId'] = request.task_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFailDetailDownload',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryFailDetailDownloadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_fail_detail_download(
        self,
        request: dysms_20170620_models.QueryFailDetailDownloadRequest,
    ) -> dysms_20170620_models.QueryFailDetailDownloadResponse:
        """
        @param request: QueryFailDetailDownloadRequest
        @return: QueryFailDetailDownloadResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_fail_detail_download_with_options(request, runtime)

    async def query_fail_detail_download_async(
        self,
        request: dysms_20170620_models.QueryFailDetailDownloadRequest,
    ) -> dysms_20170620_models.QueryFailDetailDownloadResponse:
        """
        @param request: QueryFailDetailDownloadRequest
        @return: QueryFailDetailDownloadResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_fail_detail_download_with_options_async(request, runtime)

    def query_fail_detail_download_new_with_options(
        self,
        request: dysms_20170620_models.QueryFailDetailDownloadNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryFailDetailDownloadNewResponse:
        """
        @param request: QueryFailDetailDownloadNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFailDetailDownloadNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_instance_id):
            query['TaskInstanceId'] = request.task_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFailDetailDownloadNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryFailDetailDownloadNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_fail_detail_download_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryFailDetailDownloadNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryFailDetailDownloadNewResponse:
        """
        @param request: QueryFailDetailDownloadNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFailDetailDownloadNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_instance_id):
            query['TaskInstanceId'] = request.task_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFailDetailDownloadNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryFailDetailDownloadNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_fail_detail_download_new(
        self,
        request: dysms_20170620_models.QueryFailDetailDownloadNewRequest,
    ) -> dysms_20170620_models.QueryFailDetailDownloadNewResponse:
        """
        @param request: QueryFailDetailDownloadNewRequest
        @return: QueryFailDetailDownloadNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_fail_detail_download_new_with_options(request, runtime)

    async def query_fail_detail_download_new_async(
        self,
        request: dysms_20170620_models.QueryFailDetailDownloadNewRequest,
    ) -> dysms_20170620_models.QueryFailDetailDownloadNewResponse:
        """
        @param request: QueryFailDetailDownloadNewRequest
        @return: QueryFailDetailDownloadNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_fail_detail_download_new_with_options_async(request, runtime)

    def query_flow_limit_with_options(
        self,
        request: dysms_20170620_models.QueryFlowLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryFlowLimitResponse:
        """
        @param request: QueryFlowLimitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFlowLimitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFlowLimit',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryFlowLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_flow_limit_with_options_async(
        self,
        request: dysms_20170620_models.QueryFlowLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryFlowLimitResponse:
        """
        @param request: QueryFlowLimitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFlowLimitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFlowLimit',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryFlowLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_flow_limit(
        self,
        request: dysms_20170620_models.QueryFlowLimitRequest,
    ) -> dysms_20170620_models.QueryFlowLimitResponse:
        """
        @param request: QueryFlowLimitRequest
        @return: QueryFlowLimitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_flow_limit_with_options(request, runtime)

    async def query_flow_limit_async(
        self,
        request: dysms_20170620_models.QueryFlowLimitRequest,
    ) -> dysms_20170620_models.QueryFlowLimitResponse:
        """
        @param request: QueryFlowLimitRequest
        @return: QueryFlowLimitResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_flow_limit_with_options_async(request, runtime)

    def query_flow_limit_new_with_options(
        self,
        request: dysms_20170620_models.QueryFlowLimitNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryFlowLimitNewResponse:
        """
        @param request: QueryFlowLimitNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFlowLimitNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFlowLimitNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryFlowLimitNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_flow_limit_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryFlowLimitNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryFlowLimitNewResponse:
        """
        @param request: QueryFlowLimitNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFlowLimitNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFlowLimitNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryFlowLimitNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_flow_limit_new(
        self,
        request: dysms_20170620_models.QueryFlowLimitNewRequest,
    ) -> dysms_20170620_models.QueryFlowLimitNewResponse:
        """
        @param request: QueryFlowLimitNewRequest
        @return: QueryFlowLimitNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_flow_limit_new_with_options(request, runtime)

    async def query_flow_limit_new_async(
        self,
        request: dysms_20170620_models.QueryFlowLimitNewRequest,
    ) -> dysms_20170620_models.QueryFlowLimitNewResponse:
        """
        @param request: QueryFlowLimitNewRequest
        @return: QueryFlowLimitNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_flow_limit_new_with_options_async(request, runtime)

    def query_index_col_record_with_options(
        self,
        request: dysms_20170620_models.QueryIndexColRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryIndexColRecordResponse:
        """
        @param request: QueryIndexColRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryIndexColRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_instance_id):
            query['TaskInstanceId'] = request.task_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryIndexColRecord',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryIndexColRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_index_col_record_with_options_async(
        self,
        request: dysms_20170620_models.QueryIndexColRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryIndexColRecordResponse:
        """
        @param request: QueryIndexColRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryIndexColRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_instance_id):
            query['TaskInstanceId'] = request.task_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryIndexColRecord',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryIndexColRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_index_col_record(
        self,
        request: dysms_20170620_models.QueryIndexColRecordRequest,
    ) -> dysms_20170620_models.QueryIndexColRecordResponse:
        """
        @param request: QueryIndexColRecordRequest
        @return: QueryIndexColRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_index_col_record_with_options(request, runtime)

    async def query_index_col_record_async(
        self,
        request: dysms_20170620_models.QueryIndexColRecordRequest,
    ) -> dysms_20170620_models.QueryIndexColRecordResponse:
        """
        @param request: QueryIndexColRecordRequest
        @return: QueryIndexColRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_index_col_record_with_options_async(request, runtime)

    def query_learning_status_new_with_options(
        self,
        request: dysms_20170620_models.QueryLearningStatusNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryLearningStatusNewResponse:
        """
        @param request: QueryLearningStatusNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryLearningStatusNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryLearningStatusNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryLearningStatusNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_learning_status_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryLearningStatusNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryLearningStatusNewResponse:
        """
        @param request: QueryLearningStatusNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryLearningStatusNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryLearningStatusNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryLearningStatusNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_learning_status_new(
        self,
        request: dysms_20170620_models.QueryLearningStatusNewRequest,
    ) -> dysms_20170620_models.QueryLearningStatusNewResponse:
        """
        @param request: QueryLearningStatusNewRequest
        @return: QueryLearningStatusNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_learning_status_new_with_options(request, runtime)

    async def query_learning_status_new_async(
        self,
        request: dysms_20170620_models.QueryLearningStatusNewRequest,
    ) -> dysms_20170620_models.QueryLearningStatusNewResponse:
        """
        @param request: QueryLearningStatusNewRequest
        @return: QueryLearningStatusNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_learning_status_new_with_options_async(request, runtime)

    def query_marketing_assistant_status_with_options(
        self,
        request: dysms_20170620_models.QueryMarketingAssistantStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryMarketingAssistantStatusResponse:
        """
        @param request: QueryMarketingAssistantStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMarketingAssistantStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMarketingAssistantStatus',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryMarketingAssistantStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_marketing_assistant_status_with_options_async(
        self,
        request: dysms_20170620_models.QueryMarketingAssistantStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryMarketingAssistantStatusResponse:
        """
        @param request: QueryMarketingAssistantStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMarketingAssistantStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMarketingAssistantStatus',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryMarketingAssistantStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_marketing_assistant_status(
        self,
        request: dysms_20170620_models.QueryMarketingAssistantStatusRequest,
    ) -> dysms_20170620_models.QueryMarketingAssistantStatusResponse:
        """
        @param request: QueryMarketingAssistantStatusRequest
        @return: QueryMarketingAssistantStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_marketing_assistant_status_with_options(request, runtime)

    async def query_marketing_assistant_status_async(
        self,
        request: dysms_20170620_models.QueryMarketingAssistantStatusRequest,
    ) -> dysms_20170620_models.QueryMarketingAssistantStatusResponse:
        """
        @param request: QueryMarketingAssistantStatusRequest
        @return: QueryMarketingAssistantStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_marketing_assistant_status_with_options_async(request, runtime)

    def query_message_callback_new_with_options(
        self,
        request: dysms_20170620_models.QueryMessageCallbackNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryMessageCallbackNewResponse:
        """
        @param request: QueryMessageCallbackNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMessageCallbackNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMessageCallbackNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryMessageCallbackNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_message_callback_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryMessageCallbackNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryMessageCallbackNewResponse:
        """
        @param request: QueryMessageCallbackNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMessageCallbackNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMessageCallbackNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryMessageCallbackNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_message_callback_new(
        self,
        request: dysms_20170620_models.QueryMessageCallbackNewRequest,
    ) -> dysms_20170620_models.QueryMessageCallbackNewResponse:
        """
        @param request: QueryMessageCallbackNewRequest
        @return: QueryMessageCallbackNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_message_callback_new_with_options(request, runtime)

    async def query_message_callback_new_async(
        self,
        request: dysms_20170620_models.QueryMessageCallbackNewRequest,
    ) -> dysms_20170620_models.QueryMessageCallbackNewResponse:
        """
        @param request: QueryMessageCallbackNewRequest
        @return: QueryMessageCallbackNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_message_callback_new_with_options_async(request, runtime)

    def query_message_queue_new_with_options(
        self,
        request: dysms_20170620_models.QueryMessageQueueNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryMessageQueueNewResponse:
        """
        @param request: QueryMessageQueueNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMessageQueueNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.queue_types):
            query['QueueTypes'] = request.queue_types
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMessageQueueNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryMessageQueueNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_message_queue_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryMessageQueueNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryMessageQueueNewResponse:
        """
        @param request: QueryMessageQueueNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMessageQueueNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.queue_types):
            query['QueueTypes'] = request.queue_types
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMessageQueueNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryMessageQueueNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_message_queue_new(
        self,
        request: dysms_20170620_models.QueryMessageQueueNewRequest,
    ) -> dysms_20170620_models.QueryMessageQueueNewResponse:
        """
        @param request: QueryMessageQueueNewRequest
        @return: QueryMessageQueueNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_message_queue_new_with_options(request, runtime)

    async def query_message_queue_new_async(
        self,
        request: dysms_20170620_models.QueryMessageQueueNewRequest,
    ) -> dysms_20170620_models.QueryMessageQueueNewResponse:
        """
        @param request: QueryMessageQueueNewRequest
        @return: QueryMessageQueueNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_message_queue_new_with_options_async(request, runtime)

    def query_monthly_bill_info_leaf_new_with_options(
        self,
        request: dysms_20170620_models.QueryMonthlyBillInfoLeafNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryMonthlyBillInfoLeafNewResponse:
        """
        @param request: QueryMonthlyBillInfoLeafNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMonthlyBillInfoLeafNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.item_name):
            query['ItemName'] = request.item_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subject_item_id):
            query['SubjectItemId'] = request.subject_item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMonthlyBillInfoLeafNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryMonthlyBillInfoLeafNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_monthly_bill_info_leaf_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryMonthlyBillInfoLeafNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryMonthlyBillInfoLeafNewResponse:
        """
        @param request: QueryMonthlyBillInfoLeafNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMonthlyBillInfoLeafNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.item_name):
            query['ItemName'] = request.item_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subject_item_id):
            query['SubjectItemId'] = request.subject_item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMonthlyBillInfoLeafNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryMonthlyBillInfoLeafNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_monthly_bill_info_leaf_new(
        self,
        request: dysms_20170620_models.QueryMonthlyBillInfoLeafNewRequest,
    ) -> dysms_20170620_models.QueryMonthlyBillInfoLeafNewResponse:
        """
        @param request: QueryMonthlyBillInfoLeafNewRequest
        @return: QueryMonthlyBillInfoLeafNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_monthly_bill_info_leaf_new_with_options(request, runtime)

    async def query_monthly_bill_info_leaf_new_async(
        self,
        request: dysms_20170620_models.QueryMonthlyBillInfoLeafNewRequest,
    ) -> dysms_20170620_models.QueryMonthlyBillInfoLeafNewResponse:
        """
        @param request: QueryMonthlyBillInfoLeafNewRequest
        @return: QueryMonthlyBillInfoLeafNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_monthly_bill_info_leaf_new_with_options_async(request, runtime)

    def query_monthly_bill_rental_with_options(
        self,
        request: dysms_20170620_models.QueryMonthlyBillRentalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryMonthlyBillRentalResponse:
        """
        @param request: QueryMonthlyBillRentalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMonthlyBillRentalResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMonthlyBillRental',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryMonthlyBillRentalResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_monthly_bill_rental_with_options_async(
        self,
        request: dysms_20170620_models.QueryMonthlyBillRentalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryMonthlyBillRentalResponse:
        """
        @param request: QueryMonthlyBillRentalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMonthlyBillRentalResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMonthlyBillRental',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryMonthlyBillRentalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_monthly_bill_rental(
        self,
        request: dysms_20170620_models.QueryMonthlyBillRentalRequest,
    ) -> dysms_20170620_models.QueryMonthlyBillRentalResponse:
        """
        @param request: QueryMonthlyBillRentalRequest
        @return: QueryMonthlyBillRentalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_monthly_bill_rental_with_options(request, runtime)

    async def query_monthly_bill_rental_async(
        self,
        request: dysms_20170620_models.QueryMonthlyBillRentalRequest,
    ) -> dysms_20170620_models.QueryMonthlyBillRentalResponse:
        """
        @param request: QueryMonthlyBillRentalRequest
        @return: QueryMonthlyBillRentalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_monthly_bill_rental_with_options_async(request, runtime)

    def query_monthly_bill_rental_new_with_options(
        self,
        request: dysms_20170620_models.QueryMonthlyBillRentalNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryMonthlyBillRentalNewResponse:
        """
        @param request: QueryMonthlyBillRentalNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMonthlyBillRentalNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMonthlyBillRentalNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryMonthlyBillRentalNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_monthly_bill_rental_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryMonthlyBillRentalNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryMonthlyBillRentalNewResponse:
        """
        @param request: QueryMonthlyBillRentalNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMonthlyBillRentalNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMonthlyBillRentalNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryMonthlyBillRentalNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_monthly_bill_rental_new(
        self,
        request: dysms_20170620_models.QueryMonthlyBillRentalNewRequest,
    ) -> dysms_20170620_models.QueryMonthlyBillRentalNewResponse:
        """
        @param request: QueryMonthlyBillRentalNewRequest
        @return: QueryMonthlyBillRentalNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_monthly_bill_rental_new_with_options(request, runtime)

    async def query_monthly_bill_rental_new_async(
        self,
        request: dysms_20170620_models.QueryMonthlyBillRentalNewRequest,
    ) -> dysms_20170620_models.QueryMonthlyBillRentalNewResponse:
        """
        @param request: QueryMonthlyBillRentalNewRequest
        @return: QueryMonthlyBillRentalNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_monthly_bill_rental_new_with_options_async(request, runtime)

    def query_msg_count_with_options(
        self,
        request: dysms_20170620_models.QueryMsgCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryMsgCountResponse:
        """
        @param request: QueryMsgCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMsgCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMsgCount',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryMsgCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_msg_count_with_options_async(
        self,
        request: dysms_20170620_models.QueryMsgCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryMsgCountResponse:
        """
        @param request: QueryMsgCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMsgCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMsgCount',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryMsgCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_msg_count(
        self,
        request: dysms_20170620_models.QueryMsgCountRequest,
    ) -> dysms_20170620_models.QueryMsgCountResponse:
        """
        @param request: QueryMsgCountRequest
        @return: QueryMsgCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_msg_count_with_options(request, runtime)

    async def query_msg_count_async(
        self,
        request: dysms_20170620_models.QueryMsgCountRequest,
    ) -> dysms_20170620_models.QueryMsgCountResponse:
        """
        @param request: QueryMsgCountRequest
        @return: QueryMsgCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_msg_count_with_options_async(request, runtime)

    def query_open_status_with_options(
        self,
        request: dysms_20170620_models.QueryOpenStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryOpenStatusResponse:
        """
        @param request: QueryOpenStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOpenStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bus_offer):
            query['BusOffer'] = request.bus_offer
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOpenStatus',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryOpenStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_open_status_with_options_async(
        self,
        request: dysms_20170620_models.QueryOpenStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryOpenStatusResponse:
        """
        @param request: QueryOpenStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOpenStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bus_offer):
            query['BusOffer'] = request.bus_offer
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOpenStatus',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryOpenStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_open_status(
        self,
        request: dysms_20170620_models.QueryOpenStatusRequest,
    ) -> dysms_20170620_models.QueryOpenStatusResponse:
        """
        @param request: QueryOpenStatusRequest
        @return: QueryOpenStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_open_status_with_options(request, runtime)

    async def query_open_status_async(
        self,
        request: dysms_20170620_models.QueryOpenStatusRequest,
    ) -> dysms_20170620_models.QueryOpenStatusResponse:
        """
        @param request: QueryOpenStatusRequest
        @return: QueryOpenStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_open_status_with_options_async(request, runtime)

    def query_openc_flag_new_with_options(
        self,
        request: dysms_20170620_models.QueryOpencFlagNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryOpencFlagNewResponse:
        """
        @param request: QueryOpencFlagNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOpencFlagNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOpencFlagNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryOpencFlagNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_openc_flag_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryOpencFlagNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryOpencFlagNewResponse:
        """
        @param request: QueryOpencFlagNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOpencFlagNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOpencFlagNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryOpencFlagNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_openc_flag_new(
        self,
        request: dysms_20170620_models.QueryOpencFlagNewRequest,
    ) -> dysms_20170620_models.QueryOpencFlagNewResponse:
        """
        @param request: QueryOpencFlagNewRequest
        @return: QueryOpencFlagNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_openc_flag_new_with_options(request, runtime)

    async def query_openc_flag_new_async(
        self,
        request: dysms_20170620_models.QueryOpencFlagNewRequest,
    ) -> dysms_20170620_models.QueryOpencFlagNewResponse:
        """
        @param request: QueryOpencFlagNewRequest
        @return: QueryOpencFlagNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_openc_flag_new_with_options_async(request, runtime)

    def query_phone_white_list_with_options(
        self,
        request: dysms_20170620_models.QueryPhoneWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryPhoneWhiteListResponse:
        """
        @param request: QueryPhoneWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPhoneWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPhoneWhiteList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryPhoneWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_phone_white_list_with_options_async(
        self,
        request: dysms_20170620_models.QueryPhoneWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryPhoneWhiteListResponse:
        """
        @param request: QueryPhoneWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPhoneWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPhoneWhiteList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryPhoneWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_phone_white_list(
        self,
        request: dysms_20170620_models.QueryPhoneWhiteListRequest,
    ) -> dysms_20170620_models.QueryPhoneWhiteListResponse:
        """
        @param request: QueryPhoneWhiteListRequest
        @return: QueryPhoneWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_phone_white_list_with_options(request, runtime)

    async def query_phone_white_list_async(
        self,
        request: dysms_20170620_models.QueryPhoneWhiteListRequest,
    ) -> dysms_20170620_models.QueryPhoneWhiteListResponse:
        """
        @param request: QueryPhoneWhiteListRequest
        @return: QueryPhoneWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_phone_white_list_with_options_async(request, runtime)

    def query_phone_white_list_new_with_options(
        self,
        request: dysms_20170620_models.QueryPhoneWhiteListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryPhoneWhiteListNewResponse:
        """
        @param request: QueryPhoneWhiteListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPhoneWhiteListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPhoneWhiteListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryPhoneWhiteListNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_phone_white_list_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryPhoneWhiteListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryPhoneWhiteListNewResponse:
        """
        @param request: QueryPhoneWhiteListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPhoneWhiteListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPhoneWhiteListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryPhoneWhiteListNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_phone_white_list_new(
        self,
        request: dysms_20170620_models.QueryPhoneWhiteListNewRequest,
    ) -> dysms_20170620_models.QueryPhoneWhiteListNewResponse:
        """
        @param request: QueryPhoneWhiteListNewRequest
        @return: QueryPhoneWhiteListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_phone_white_list_new_with_options(request, runtime)

    async def query_phone_white_list_new_async(
        self,
        request: dysms_20170620_models.QueryPhoneWhiteListNewRequest,
    ) -> dysms_20170620_models.QueryPhoneWhiteListNewResponse:
        """
        @param request: QueryPhoneWhiteListNewRequest
        @return: QueryPhoneWhiteListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_phone_white_list_new_with_options_async(request, runtime)

    def query_pkg_threshold_with_options(
        self,
        request: dysms_20170620_models.QueryPkgThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryPkgThresholdResponse:
        """
        @param request: QueryPkgThresholdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPkgThresholdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPkgThreshold',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryPkgThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_pkg_threshold_with_options_async(
        self,
        request: dysms_20170620_models.QueryPkgThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryPkgThresholdResponse:
        """
        @param request: QueryPkgThresholdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPkgThresholdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPkgThreshold',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryPkgThresholdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_pkg_threshold(
        self,
        request: dysms_20170620_models.QueryPkgThresholdRequest,
    ) -> dysms_20170620_models.QueryPkgThresholdResponse:
        """
        @param request: QueryPkgThresholdRequest
        @return: QueryPkgThresholdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_pkg_threshold_with_options(request, runtime)

    async def query_pkg_threshold_async(
        self,
        request: dysms_20170620_models.QueryPkgThresholdRequest,
    ) -> dysms_20170620_models.QueryPkgThresholdResponse:
        """
        @param request: QueryPkgThresholdRequest
        @return: QueryPkgThresholdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_pkg_threshold_with_options_async(request, runtime)

    def query_pkg_threshold_new_with_options(
        self,
        request: dysms_20170620_models.QueryPkgThresholdNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryPkgThresholdNewResponse:
        """
        @param request: QueryPkgThresholdNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPkgThresholdNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPkgThresholdNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryPkgThresholdNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_pkg_threshold_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryPkgThresholdNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryPkgThresholdNewResponse:
        """
        @param request: QueryPkgThresholdNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPkgThresholdNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPkgThresholdNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryPkgThresholdNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_pkg_threshold_new(
        self,
        request: dysms_20170620_models.QueryPkgThresholdNewRequest,
    ) -> dysms_20170620_models.QueryPkgThresholdNewResponse:
        """
        @param request: QueryPkgThresholdNewRequest
        @return: QueryPkgThresholdNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_pkg_threshold_new_with_options(request, runtime)

    async def query_pkg_threshold_new_async(
        self,
        request: dysms_20170620_models.QueryPkgThresholdNewRequest,
    ) -> dysms_20170620_models.QueryPkgThresholdNewResponse:
        """
        @param request: QueryPkgThresholdNewRequest
        @return: QueryPkgThresholdNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_pkg_threshold_new_with_options_async(request, runtime)

    def query_prev_limit_new_with_options(
        self,
        request: dysms_20170620_models.QueryPrevLimitNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryPrevLimitNewResponse:
        """
        @param request: QueryPrevLimitNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPrevLimitNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPrevLimitNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryPrevLimitNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_prev_limit_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryPrevLimitNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryPrevLimitNewResponse:
        """
        @param request: QueryPrevLimitNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPrevLimitNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPrevLimitNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryPrevLimitNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_prev_limit_new(
        self,
        request: dysms_20170620_models.QueryPrevLimitNewRequest,
    ) -> dysms_20170620_models.QueryPrevLimitNewResponse:
        """
        @param request: QueryPrevLimitNewRequest
        @return: QueryPrevLimitNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_prev_limit_new_with_options(request, runtime)

    async def query_prev_limit_new_async(
        self,
        request: dysms_20170620_models.QueryPrevLimitNewRequest,
    ) -> dysms_20170620_models.QueryPrevLimitNewResponse:
        """
        @param request: QueryPrevLimitNewRequest
        @return: QueryPrevLimitNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_prev_limit_new_with_options_async(request, runtime)

    def query_saas_record_with_options(
        self,
        request: dysms_20170620_models.QuerySaasRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySaasRecordResponse:
        """
        @param request: QuerySaasRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySaasRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.index_col):
            query['IndexCol'] = request.index_col
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.result):
            query['Result'] = request.result
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_instance_id):
            query['TaskInstanceId'] = request.task_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySaasRecord',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySaasRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_saas_record_with_options_async(
        self,
        request: dysms_20170620_models.QuerySaasRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySaasRecordResponse:
        """
        @param request: QuerySaasRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySaasRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.index_col):
            query['IndexCol'] = request.index_col
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.result):
            query['Result'] = request.result
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_instance_id):
            query['TaskInstanceId'] = request.task_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySaasRecord',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySaasRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_saas_record(
        self,
        request: dysms_20170620_models.QuerySaasRecordRequest,
    ) -> dysms_20170620_models.QuerySaasRecordResponse:
        """
        @param request: QuerySaasRecordRequest
        @return: QuerySaasRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_saas_record_with_options(request, runtime)

    async def query_saas_record_async(
        self,
        request: dysms_20170620_models.QuerySaasRecordRequest,
    ) -> dysms_20170620_models.QuerySaasRecordResponse:
        """
        @param request: QuerySaasRecordRequest
        @return: QuerySaasRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_saas_record_with_options_async(request, runtime)

    def query_saas_record_new_with_options(
        self,
        request: dysms_20170620_models.QuerySaasRecordNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySaasRecordNewResponse:
        """
        @param request: QuerySaasRecordNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySaasRecordNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.index_col):
            query['IndexCol'] = request.index_col
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.result):
            query['Result'] = request.result
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_instance_id):
            query['TaskInstanceId'] = request.task_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySaasRecordNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySaasRecordNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_saas_record_new_with_options_async(
        self,
        request: dysms_20170620_models.QuerySaasRecordNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySaasRecordNewResponse:
        """
        @param request: QuerySaasRecordNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySaasRecordNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.index_col):
            query['IndexCol'] = request.index_col
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.result):
            query['Result'] = request.result
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_instance_id):
            query['TaskInstanceId'] = request.task_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySaasRecordNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySaasRecordNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_saas_record_new(
        self,
        request: dysms_20170620_models.QuerySaasRecordNewRequest,
    ) -> dysms_20170620_models.QuerySaasRecordNewResponse:
        """
        @param request: QuerySaasRecordNewRequest
        @return: QuerySaasRecordNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_saas_record_new_with_options(request, runtime)

    async def query_saas_record_new_async(
        self,
        request: dysms_20170620_models.QuerySaasRecordNewRequest,
    ) -> dysms_20170620_models.QuerySaasRecordNewResponse:
        """
        @param request: QuerySaasRecordNewRequest
        @return: QuerySaasRecordNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_saas_record_new_with_options_async(request, runtime)

    def query_send_details_by_phone_num_with_options(
        self,
        request: dysms_20170620_models.QuerySendDetailsByPhoneNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySendDetailsByPhoneNumResponse:
        """
        @param request: QuerySendDetailsByPhoneNumRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySendDetailsByPhoneNumResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.error_code):
            query['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_date):
            query['SendDate'] = request.send_date
        if not UtilClient.is_unset(request.send_status):
            query['SendStatus'] = request.send_status
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySendDetailsByPhoneNum',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySendDetailsByPhoneNumResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_send_details_by_phone_num_with_options_async(
        self,
        request: dysms_20170620_models.QuerySendDetailsByPhoneNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySendDetailsByPhoneNumResponse:
        """
        @param request: QuerySendDetailsByPhoneNumRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySendDetailsByPhoneNumResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.error_code):
            query['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_date):
            query['SendDate'] = request.send_date
        if not UtilClient.is_unset(request.send_status):
            query['SendStatus'] = request.send_status
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySendDetailsByPhoneNum',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySendDetailsByPhoneNumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_send_details_by_phone_num(
        self,
        request: dysms_20170620_models.QuerySendDetailsByPhoneNumRequest,
    ) -> dysms_20170620_models.QuerySendDetailsByPhoneNumResponse:
        """
        @param request: QuerySendDetailsByPhoneNumRequest
        @return: QuerySendDetailsByPhoneNumResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_send_details_by_phone_num_with_options(request, runtime)

    async def query_send_details_by_phone_num_async(
        self,
        request: dysms_20170620_models.QuerySendDetailsByPhoneNumRequest,
    ) -> dysms_20170620_models.QuerySendDetailsByPhoneNumResponse:
        """
        @param request: QuerySendDetailsByPhoneNumRequest
        @return: QuerySendDetailsByPhoneNumResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_send_details_by_phone_num_with_options_async(request, runtime)

    def query_send_details_by_phone_num_new_with_options(
        self,
        request: dysms_20170620_models.QuerySendDetailsByPhoneNumNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySendDetailsByPhoneNumNewResponse:
        """
        @param request: QuerySendDetailsByPhoneNumNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySendDetailsByPhoneNumNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.error_code):
            query['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_date):
            query['SendDate'] = request.send_date
        if not UtilClient.is_unset(request.send_status):
            query['SendStatus'] = request.send_status
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.statistics_status):
            query['StatisticsStatus'] = request.statistics_status
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySendDetailsByPhoneNumNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySendDetailsByPhoneNumNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_send_details_by_phone_num_new_with_options_async(
        self,
        request: dysms_20170620_models.QuerySendDetailsByPhoneNumNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySendDetailsByPhoneNumNewResponse:
        """
        @param request: QuerySendDetailsByPhoneNumNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySendDetailsByPhoneNumNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.error_code):
            query['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.send_date):
            query['SendDate'] = request.send_date
        if not UtilClient.is_unset(request.send_status):
            query['SendStatus'] = request.send_status
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.statistics_status):
            query['StatisticsStatus'] = request.statistics_status
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySendDetailsByPhoneNumNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySendDetailsByPhoneNumNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_send_details_by_phone_num_new(
        self,
        request: dysms_20170620_models.QuerySendDetailsByPhoneNumNewRequest,
    ) -> dysms_20170620_models.QuerySendDetailsByPhoneNumNewResponse:
        """
        @param request: QuerySendDetailsByPhoneNumNewRequest
        @return: QuerySendDetailsByPhoneNumNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_send_details_by_phone_num_new_with_options(request, runtime)

    async def query_send_details_by_phone_num_new_async(
        self,
        request: dysms_20170620_models.QuerySendDetailsByPhoneNumNewRequest,
    ) -> dysms_20170620_models.QuerySendDetailsByPhoneNumNewResponse:
        """
        @param request: QuerySendDetailsByPhoneNumNewRequest
        @return: QuerySendDetailsByPhoneNumNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_send_details_by_phone_num_new_with_options_async(request, runtime)

    def query_send_fail_details_with_options(
        self,
        request: dysms_20170620_models.QuerySendFailDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySendFailDetailsResponse:
        """
        @param request: QuerySendFailDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySendFailDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
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
            action='QuerySendFailDetails',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySendFailDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_send_fail_details_with_options_async(
        self,
        request: dysms_20170620_models.QuerySendFailDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySendFailDetailsResponse:
        """
        @param request: QuerySendFailDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySendFailDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
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
            action='QuerySendFailDetails',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySendFailDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_send_fail_details(
        self,
        request: dysms_20170620_models.QuerySendFailDetailsRequest,
    ) -> dysms_20170620_models.QuerySendFailDetailsResponse:
        """
        @param request: QuerySendFailDetailsRequest
        @return: QuerySendFailDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_send_fail_details_with_options(request, runtime)

    async def query_send_fail_details_async(
        self,
        request: dysms_20170620_models.QuerySendFailDetailsRequest,
    ) -> dysms_20170620_models.QuerySendFailDetailsResponse:
        """
        @param request: QuerySendFailDetailsRequest
        @return: QuerySendFailDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_send_fail_details_with_options_async(request, runtime)

    def query_send_fail_details_new_with_options(
        self,
        request: dysms_20170620_models.QuerySendFailDetailsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySendFailDetailsNewResponse:
        """
        @param request: QuerySendFailDetailsNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySendFailDetailsNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
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
            action='QuerySendFailDetailsNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySendFailDetailsNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_send_fail_details_new_with_options_async(
        self,
        request: dysms_20170620_models.QuerySendFailDetailsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySendFailDetailsNewResponse:
        """
        @param request: QuerySendFailDetailsNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySendFailDetailsNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
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
            action='QuerySendFailDetailsNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySendFailDetailsNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_send_fail_details_new(
        self,
        request: dysms_20170620_models.QuerySendFailDetailsNewRequest,
    ) -> dysms_20170620_models.QuerySendFailDetailsNewResponse:
        """
        @param request: QuerySendFailDetailsNewRequest
        @return: QuerySendFailDetailsNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_send_fail_details_new_with_options(request, runtime)

    async def query_send_fail_details_new_async(
        self,
        request: dysms_20170620_models.QuerySendFailDetailsNewRequest,
    ) -> dysms_20170620_models.QuerySendFailDetailsNewResponse:
        """
        @param request: QuerySendFailDetailsNewRequest
        @return: QuerySendFailDetailsNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_send_fail_details_new_with_options_async(request, runtime)

    def query_send_to_globe_status_with_options(
        self,
        request: dysms_20170620_models.QuerySendToGlobeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySendToGlobeStatusResponse:
        """
        @param request: QuerySendToGlobeStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySendToGlobeStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySendToGlobeStatus',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySendToGlobeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_send_to_globe_status_with_options_async(
        self,
        request: dysms_20170620_models.QuerySendToGlobeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySendToGlobeStatusResponse:
        """
        @param request: QuerySendToGlobeStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySendToGlobeStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySendToGlobeStatus',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySendToGlobeStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_send_to_globe_status(
        self,
        request: dysms_20170620_models.QuerySendToGlobeStatusRequest,
    ) -> dysms_20170620_models.QuerySendToGlobeStatusResponse:
        """
        @param request: QuerySendToGlobeStatusRequest
        @return: QuerySendToGlobeStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_send_to_globe_status_with_options(request, runtime)

    async def query_send_to_globe_status_async(
        self,
        request: dysms_20170620_models.QuerySendToGlobeStatusRequest,
    ) -> dysms_20170620_models.QuerySendToGlobeStatusResponse:
        """
        @param request: QuerySendToGlobeStatusRequest
        @return: QuerySendToGlobeStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_send_to_globe_status_with_options_async(request, runtime)

    def query_short_url_detail_new_with_options(
        self,
        request: dysms_20170620_models.QueryShortUrlDetailNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryShortUrlDetailNewResponse:
        """
        @param request: QueryShortUrlDetailNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryShortUrlDetailNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.short_url_id):
            query['ShortUrlId'] = request.short_url_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryShortUrlDetailNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryShortUrlDetailNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_short_url_detail_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryShortUrlDetailNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryShortUrlDetailNewResponse:
        """
        @param request: QueryShortUrlDetailNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryShortUrlDetailNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.short_url_id):
            query['ShortUrlId'] = request.short_url_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryShortUrlDetailNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryShortUrlDetailNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_short_url_detail_new(
        self,
        request: dysms_20170620_models.QueryShortUrlDetailNewRequest,
    ) -> dysms_20170620_models.QueryShortUrlDetailNewResponse:
        """
        @param request: QueryShortUrlDetailNewRequest
        @return: QueryShortUrlDetailNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_short_url_detail_new_with_options(request, runtime)

    async def query_short_url_detail_new_async(
        self,
        request: dysms_20170620_models.QueryShortUrlDetailNewRequest,
    ) -> dysms_20170620_models.QueryShortUrlDetailNewResponse:
        """
        @param request: QueryShortUrlDetailNewRequest
        @return: QueryShortUrlDetailNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_short_url_detail_new_with_options_async(request, runtime)

    def query_short_url_list_new_with_options(
        self,
        request: dysms_20170620_models.QueryShortUrlListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryShortUrlListNewResponse:
        """
        @param request: QueryShortUrlListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryShortUrlListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
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
            action='QueryShortUrlListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryShortUrlListNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_short_url_list_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryShortUrlListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryShortUrlListNewResponse:
        """
        @param request: QueryShortUrlListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryShortUrlListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
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
            action='QueryShortUrlListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryShortUrlListNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_short_url_list_new(
        self,
        request: dysms_20170620_models.QueryShortUrlListNewRequest,
    ) -> dysms_20170620_models.QueryShortUrlListNewResponse:
        """
        @param request: QueryShortUrlListNewRequest
        @return: QueryShortUrlListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_short_url_list_new_with_options(request, runtime)

    async def query_short_url_list_new_async(
        self,
        request: dysms_20170620_models.QueryShortUrlListNewRequest,
    ) -> dysms_20170620_models.QueryShortUrlListNewResponse:
        """
        @param request: QueryShortUrlListNewRequest
        @return: QueryShortUrlListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_short_url_list_new_with_options_async(request, runtime)

    def query_short_url_status_with_options(
        self,
        request: dysms_20170620_models.QueryShortUrlStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryShortUrlStatusResponse:
        """
        @param request: QueryShortUrlStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryShortUrlStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryShortUrlStatus',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryShortUrlStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_short_url_status_with_options_async(
        self,
        request: dysms_20170620_models.QueryShortUrlStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryShortUrlStatusResponse:
        """
        @param request: QueryShortUrlStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryShortUrlStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryShortUrlStatus',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryShortUrlStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_short_url_status(
        self,
        request: dysms_20170620_models.QueryShortUrlStatusRequest,
    ) -> dysms_20170620_models.QueryShortUrlStatusResponse:
        """
        @param request: QueryShortUrlStatusRequest
        @return: QueryShortUrlStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_short_url_status_with_options(request, runtime)

    async def query_short_url_status_async(
        self,
        request: dysms_20170620_models.QueryShortUrlStatusRequest,
    ) -> dysms_20170620_models.QueryShortUrlStatusResponse:
        """
        @param request: QueryShortUrlStatusRequest
        @return: QueryShortUrlStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_short_url_status_with_options_async(request, runtime)

    def query_sls_status_new_with_options(
        self,
        request: dysms_20170620_models.QuerySlsStatusNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySlsStatusNewResponse:
        """
        @param request: QuerySlsStatusNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySlsStatusNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySlsStatusNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySlsStatusNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sls_status_new_with_options_async(
        self,
        request: dysms_20170620_models.QuerySlsStatusNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySlsStatusNewResponse:
        """
        @param request: QuerySlsStatusNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySlsStatusNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySlsStatusNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySlsStatusNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sls_status_new(
        self,
        request: dysms_20170620_models.QuerySlsStatusNewRequest,
    ) -> dysms_20170620_models.QuerySlsStatusNewResponse:
        """
        @param request: QuerySlsStatusNewRequest
        @return: QuerySlsStatusNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sls_status_new_with_options(request, runtime)

    async def query_sls_status_new_async(
        self,
        request: dysms_20170620_models.QuerySlsStatusNewRequest,
    ) -> dysms_20170620_models.QuerySlsStatusNewResponse:
        """
        @param request: QuerySlsStatusNewRequest
        @return: QuerySlsStatusNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sls_status_new_with_options_async(request, runtime)

    def query_sms_base_screen_new_with_options(
        self,
        request: dysms_20170620_models.QuerySmsBaseScreenNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsBaseScreenNewResponse:
        """
        @param request: QuerySmsBaseScreenNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsBaseScreenNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsBaseScreenNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsBaseScreenNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_base_screen_new_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsBaseScreenNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsBaseScreenNewResponse:
        """
        @param request: QuerySmsBaseScreenNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsBaseScreenNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsBaseScreenNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsBaseScreenNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_base_screen_new(
        self,
        request: dysms_20170620_models.QuerySmsBaseScreenNewRequest,
    ) -> dysms_20170620_models.QuerySmsBaseScreenNewResponse:
        """
        @param request: QuerySmsBaseScreenNewRequest
        @return: QuerySmsBaseScreenNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_base_screen_new_with_options(request, runtime)

    async def query_sms_base_screen_new_async(
        self,
        request: dysms_20170620_models.QuerySmsBaseScreenNewRequest,
    ) -> dysms_20170620_models.QuerySmsBaseScreenNewResponse:
        """
        @param request: QuerySmsBaseScreenNewRequest
        @return: QuerySmsBaseScreenNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_base_screen_new_with_options_async(request, runtime)

    def query_sms_detect_counts_with_options(
        self,
        request: dysms_20170620_models.QuerySmsDetectCountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsDetectCountsResponse:
        """
        @param request: QuerySmsDetectCountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsDetectCountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsDetectCounts',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsDetectCountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_detect_counts_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsDetectCountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsDetectCountsResponse:
        """
        @param request: QuerySmsDetectCountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsDetectCountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsDetectCounts',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsDetectCountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_detect_counts(
        self,
        request: dysms_20170620_models.QuerySmsDetectCountsRequest,
    ) -> dysms_20170620_models.QuerySmsDetectCountsResponse:
        """
        @param request: QuerySmsDetectCountsRequest
        @return: QuerySmsDetectCountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_detect_counts_with_options(request, runtime)

    async def query_sms_detect_counts_async(
        self,
        request: dysms_20170620_models.QuerySmsDetectCountsRequest,
    ) -> dysms_20170620_models.QuerySmsDetectCountsResponse:
        """
        @param request: QuerySmsDetectCountsRequest
        @return: QuerySmsDetectCountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_detect_counts_with_options_async(request, runtime)

    def query_sms_detect_counts_new_with_options(
        self,
        request: dysms_20170620_models.QuerySmsDetectCountsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsDetectCountsNewResponse:
        """
        @param request: QuerySmsDetectCountsNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsDetectCountsNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsDetectCountsNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsDetectCountsNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_detect_counts_new_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsDetectCountsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsDetectCountsNewResponse:
        """
        @param request: QuerySmsDetectCountsNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsDetectCountsNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsDetectCountsNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsDetectCountsNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_detect_counts_new(
        self,
        request: dysms_20170620_models.QuerySmsDetectCountsNewRequest,
    ) -> dysms_20170620_models.QuerySmsDetectCountsNewResponse:
        """
        @param request: QuerySmsDetectCountsNewRequest
        @return: QuerySmsDetectCountsNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_detect_counts_new_with_options(request, runtime)

    async def query_sms_detect_counts_new_async(
        self,
        request: dysms_20170620_models.QuerySmsDetectCountsNewRequest,
    ) -> dysms_20170620_models.QuerySmsDetectCountsNewResponse:
        """
        @param request: QuerySmsDetectCountsNewRequest
        @return: QuerySmsDetectCountsNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_detect_counts_new_with_options_async(request, runtime)

    def query_sms_detect_list_with_options(
        self,
        request: dysms_20170620_models.QuerySmsDetectListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsDetectListResponse:
        """
        @param request: QuerySmsDetectListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsDetectListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsDetectList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsDetectListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_detect_list_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsDetectListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsDetectListResponse:
        """
        @param request: QuerySmsDetectListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsDetectListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsDetectList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsDetectListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_detect_list(
        self,
        request: dysms_20170620_models.QuerySmsDetectListRequest,
    ) -> dysms_20170620_models.QuerySmsDetectListResponse:
        """
        @param request: QuerySmsDetectListRequest
        @return: QuerySmsDetectListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_detect_list_with_options(request, runtime)

    async def query_sms_detect_list_async(
        self,
        request: dysms_20170620_models.QuerySmsDetectListRequest,
    ) -> dysms_20170620_models.QuerySmsDetectListResponse:
        """
        @param request: QuerySmsDetectListRequest
        @return: QuerySmsDetectListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_detect_list_with_options_async(request, runtime)

    def query_sms_detect_list_new_with_options(
        self,
        request: dysms_20170620_models.QuerySmsDetectListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsDetectListNewResponse:
        """
        @param request: QuerySmsDetectListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsDetectListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsDetectListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsDetectListNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_detect_list_new_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsDetectListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsDetectListNewResponse:
        """
        @param request: QuerySmsDetectListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsDetectListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsDetectListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsDetectListNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_detect_list_new(
        self,
        request: dysms_20170620_models.QuerySmsDetectListNewRequest,
    ) -> dysms_20170620_models.QuerySmsDetectListNewResponse:
        """
        @param request: QuerySmsDetectListNewRequest
        @return: QuerySmsDetectListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_detect_list_new_with_options(request, runtime)

    async def query_sms_detect_list_new_async(
        self,
        request: dysms_20170620_models.QuerySmsDetectListNewRequest,
    ) -> dysms_20170620_models.QuerySmsDetectListNewResponse:
        """
        @param request: QuerySmsDetectListNewRequest
        @return: QuerySmsDetectListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_detect_list_new_with_options_async(request, runtime)

    def query_sms_package_detail_with_options(
        self,
        request: dysms_20170620_models.QuerySmsPackageDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsPackageDetailResponse:
        """
        @param request: QuerySmsPackageDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsPackageDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsPackageDetail',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsPackageDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_package_detail_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsPackageDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsPackageDetailResponse:
        """
        @param request: QuerySmsPackageDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsPackageDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsPackageDetail',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsPackageDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_package_detail(
        self,
        request: dysms_20170620_models.QuerySmsPackageDetailRequest,
    ) -> dysms_20170620_models.QuerySmsPackageDetailResponse:
        """
        @param request: QuerySmsPackageDetailRequest
        @return: QuerySmsPackageDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_package_detail_with_options(request, runtime)

    async def query_sms_package_detail_async(
        self,
        request: dysms_20170620_models.QuerySmsPackageDetailRequest,
    ) -> dysms_20170620_models.QuerySmsPackageDetailResponse:
        """
        @param request: QuerySmsPackageDetailRequest
        @return: QuerySmsPackageDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_package_detail_with_options_async(request, runtime)

    def query_sms_package_detail_new_with_options(
        self,
        request: dysms_20170620_models.QuerySmsPackageDetailNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsPackageDetailNewResponse:
        """
        @param request: QuerySmsPackageDetailNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsPackageDetailNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsPackageDetailNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsPackageDetailNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_package_detail_new_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsPackageDetailNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsPackageDetailNewResponse:
        """
        @param request: QuerySmsPackageDetailNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsPackageDetailNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsPackageDetailNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsPackageDetailNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_package_detail_new(
        self,
        request: dysms_20170620_models.QuerySmsPackageDetailNewRequest,
    ) -> dysms_20170620_models.QuerySmsPackageDetailNewResponse:
        """
        @param request: QuerySmsPackageDetailNewRequest
        @return: QuerySmsPackageDetailNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_package_detail_new_with_options(request, runtime)

    async def query_sms_package_detail_new_async(
        self,
        request: dysms_20170620_models.QuerySmsPackageDetailNewRequest,
    ) -> dysms_20170620_models.QuerySmsPackageDetailNewResponse:
        """
        @param request: QuerySmsPackageDetailNewRequest
        @return: QuerySmsPackageDetailNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_package_detail_new_with_options_async(request, runtime)

    def query_sms_package_new_with_options(
        self,
        request: dysms_20170620_models.QuerySmsPackageNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsPackageNewResponse:
        """
        @param request: QuerySmsPackageNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsPackageNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.time):
            query['Time'] = request.time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsPackageNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsPackageNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_package_new_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsPackageNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsPackageNewResponse:
        """
        @param request: QuerySmsPackageNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsPackageNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.time):
            query['Time'] = request.time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsPackageNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsPackageNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_package_new(
        self,
        request: dysms_20170620_models.QuerySmsPackageNewRequest,
    ) -> dysms_20170620_models.QuerySmsPackageNewResponse:
        """
        @param request: QuerySmsPackageNewRequest
        @return: QuerySmsPackageNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_package_new_with_options(request, runtime)

    async def query_sms_package_new_async(
        self,
        request: dysms_20170620_models.QuerySmsPackageNewRequest,
    ) -> dysms_20170620_models.QuerySmsPackageNewResponse:
        """
        @param request: QuerySmsPackageNewRequest
        @return: QuerySmsPackageNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_package_new_with_options_async(request, runtime)

    def query_sms_package_order_list_with_options(
        self,
        request: dysms_20170620_models.QuerySmsPackageOrderListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsPackageOrderListResponse:
        """
        @param request: QuerySmsPackageOrderListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsPackageOrderListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsPackageOrderList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsPackageOrderListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_package_order_list_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsPackageOrderListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsPackageOrderListResponse:
        """
        @param request: QuerySmsPackageOrderListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsPackageOrderListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsPackageOrderList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsPackageOrderListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_package_order_list(
        self,
        request: dysms_20170620_models.QuerySmsPackageOrderListRequest,
    ) -> dysms_20170620_models.QuerySmsPackageOrderListResponse:
        """
        @param request: QuerySmsPackageOrderListRequest
        @return: QuerySmsPackageOrderListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_package_order_list_with_options(request, runtime)

    async def query_sms_package_order_list_async(
        self,
        request: dysms_20170620_models.QuerySmsPackageOrderListRequest,
    ) -> dysms_20170620_models.QuerySmsPackageOrderListResponse:
        """
        @param request: QuerySmsPackageOrderListRequest
        @return: QuerySmsPackageOrderListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_package_order_list_with_options_async(request, runtime)

    def query_sms_package_order_list_new_with_options(
        self,
        request: dysms_20170620_models.QuerySmsPackageOrderListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsPackageOrderListNewResponse:
        """
        @param request: QuerySmsPackageOrderListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsPackageOrderListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsPackageOrderListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsPackageOrderListNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_package_order_list_new_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsPackageOrderListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsPackageOrderListNewResponse:
        """
        @param request: QuerySmsPackageOrderListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsPackageOrderListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsPackageOrderListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsPackageOrderListNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_package_order_list_new(
        self,
        request: dysms_20170620_models.QuerySmsPackageOrderListNewRequest,
    ) -> dysms_20170620_models.QuerySmsPackageOrderListNewResponse:
        """
        @param request: QuerySmsPackageOrderListNewRequest
        @return: QuerySmsPackageOrderListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_package_order_list_new_with_options(request, runtime)

    async def query_sms_package_order_list_new_async(
        self,
        request: dysms_20170620_models.QuerySmsPackageOrderListNewRequest,
    ) -> dysms_20170620_models.QuerySmsPackageOrderListNewResponse:
        """
        @param request: QuerySmsPackageOrderListNewRequest
        @return: QuerySmsPackageOrderListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_package_order_list_new_with_options_async(request, runtime)

    def query_sms_package_summary_with_options(
        self,
        request: dysms_20170620_models.QuerySmsPackageSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsPackageSummaryResponse:
        """
        @param request: QuerySmsPackageSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsPackageSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsPackageSummary',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsPackageSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_package_summary_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsPackageSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsPackageSummaryResponse:
        """
        @param request: QuerySmsPackageSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsPackageSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsPackageSummary',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsPackageSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_package_summary(
        self,
        request: dysms_20170620_models.QuerySmsPackageSummaryRequest,
    ) -> dysms_20170620_models.QuerySmsPackageSummaryResponse:
        """
        @param request: QuerySmsPackageSummaryRequest
        @return: QuerySmsPackageSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_package_summary_with_options(request, runtime)

    async def query_sms_package_summary_async(
        self,
        request: dysms_20170620_models.QuerySmsPackageSummaryRequest,
    ) -> dysms_20170620_models.QuerySmsPackageSummaryResponse:
        """
        @param request: QuerySmsPackageSummaryRequest
        @return: QuerySmsPackageSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_package_summary_with_options_async(request, runtime)

    def query_sms_package_summary_new_with_options(
        self,
        request: dysms_20170620_models.QuerySmsPackageSummaryNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsPackageSummaryNewResponse:
        """
        @param request: QuerySmsPackageSummaryNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsPackageSummaryNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsPackageSummaryNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsPackageSummaryNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_package_summary_new_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsPackageSummaryNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsPackageSummaryNewResponse:
        """
        @param request: QuerySmsPackageSummaryNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsPackageSummaryNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsPackageSummaryNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsPackageSummaryNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_package_summary_new(
        self,
        request: dysms_20170620_models.QuerySmsPackageSummaryNewRequest,
    ) -> dysms_20170620_models.QuerySmsPackageSummaryNewResponse:
        """
        @param request: QuerySmsPackageSummaryNewRequest
        @return: QuerySmsPackageSummaryNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_package_summary_new_with_options(request, runtime)

    async def query_sms_package_summary_new_async(
        self,
        request: dysms_20170620_models.QuerySmsPackageSummaryNewRequest,
    ) -> dysms_20170620_models.QuerySmsPackageSummaryNewResponse:
        """
        @param request: QuerySmsPackageSummaryNewRequest
        @return: QuerySmsPackageSummaryNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_package_summary_new_with_options_async(request, runtime)

    def query_sms_saas_task_detail_with_options(
        self,
        request: dysms_20170620_models.QuerySmsSaasTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSaasTaskDetailResponse:
        """
        @param request: QuerySmsSaasTaskDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSaasTaskDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_instance_id):
            query['TaskInstanceId'] = request.task_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSaasTaskDetail',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSaasTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_saas_task_detail_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsSaasTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSaasTaskDetailResponse:
        """
        @param request: QuerySmsSaasTaskDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSaasTaskDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_instance_id):
            query['TaskInstanceId'] = request.task_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSaasTaskDetail',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSaasTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_saas_task_detail(
        self,
        request: dysms_20170620_models.QuerySmsSaasTaskDetailRequest,
    ) -> dysms_20170620_models.QuerySmsSaasTaskDetailResponse:
        """
        @param request: QuerySmsSaasTaskDetailRequest
        @return: QuerySmsSaasTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_saas_task_detail_with_options(request, runtime)

    async def query_sms_saas_task_detail_async(
        self,
        request: dysms_20170620_models.QuerySmsSaasTaskDetailRequest,
    ) -> dysms_20170620_models.QuerySmsSaasTaskDetailResponse:
        """
        @param request: QuerySmsSaasTaskDetailRequest
        @return: QuerySmsSaasTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_saas_task_detail_with_options_async(request, runtime)

    def query_sms_saas_task_detail_new_with_options(
        self,
        request: dysms_20170620_models.QuerySmsSaasTaskDetailNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSaasTaskDetailNewResponse:
        """
        @param request: QuerySmsSaasTaskDetailNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSaasTaskDetailNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSaasTaskDetailNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSaasTaskDetailNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_saas_task_detail_new_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsSaasTaskDetailNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSaasTaskDetailNewResponse:
        """
        @param request: QuerySmsSaasTaskDetailNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSaasTaskDetailNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSaasTaskDetailNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSaasTaskDetailNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_saas_task_detail_new(
        self,
        request: dysms_20170620_models.QuerySmsSaasTaskDetailNewRequest,
    ) -> dysms_20170620_models.QuerySmsSaasTaskDetailNewResponse:
        """
        @param request: QuerySmsSaasTaskDetailNewRequest
        @return: QuerySmsSaasTaskDetailNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_saas_task_detail_new_with_options(request, runtime)

    async def query_sms_saas_task_detail_new_async(
        self,
        request: dysms_20170620_models.QuerySmsSaasTaskDetailNewRequest,
    ) -> dysms_20170620_models.QuerySmsSaasTaskDetailNewResponse:
        """
        @param request: QuerySmsSaasTaskDetailNewRequest
        @return: QuerySmsSaasTaskDetailNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_saas_task_detail_new_with_options_async(request, runtime)

    def query_sms_saas_task_list_with_options(
        self,
        request: dysms_20170620_models.QuerySmsSaasTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSaasTaskListResponse:
        """
        @param request: QuerySmsSaasTaskListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSaasTaskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSaasTaskList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSaasTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_saas_task_list_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsSaasTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSaasTaskListResponse:
        """
        @param request: QuerySmsSaasTaskListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSaasTaskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSaasTaskList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSaasTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_saas_task_list(
        self,
        request: dysms_20170620_models.QuerySmsSaasTaskListRequest,
    ) -> dysms_20170620_models.QuerySmsSaasTaskListResponse:
        """
        @param request: QuerySmsSaasTaskListRequest
        @return: QuerySmsSaasTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_saas_task_list_with_options(request, runtime)

    async def query_sms_saas_task_list_async(
        self,
        request: dysms_20170620_models.QuerySmsSaasTaskListRequest,
    ) -> dysms_20170620_models.QuerySmsSaasTaskListResponse:
        """
        @param request: QuerySmsSaasTaskListRequest
        @return: QuerySmsSaasTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_saas_task_list_with_options_async(request, runtime)

    def query_sms_saas_task_list_new_with_options(
        self,
        request: dysms_20170620_models.QuerySmsSaasTaskListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSaasTaskListNewResponse:
        """
        @param request: QuerySmsSaasTaskListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSaasTaskListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSaasTaskListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSaasTaskListNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_saas_task_list_new_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsSaasTaskListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSaasTaskListNewResponse:
        """
        @param request: QuerySmsSaasTaskListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSaasTaskListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSaasTaskListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSaasTaskListNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_saas_task_list_new(
        self,
        request: dysms_20170620_models.QuerySmsSaasTaskListNewRequest,
    ) -> dysms_20170620_models.QuerySmsSaasTaskListNewResponse:
        """
        @param request: QuerySmsSaasTaskListNewRequest
        @return: QuerySmsSaasTaskListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_saas_task_list_new_with_options(request, runtime)

    async def query_sms_saas_task_list_new_async(
        self,
        request: dysms_20170620_models.QuerySmsSaasTaskListNewRequest,
    ) -> dysms_20170620_models.QuerySmsSaasTaskListNewResponse:
        """
        @param request: QuerySmsSaasTaskListNewRequest
        @return: QuerySmsSaasTaskListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_saas_task_list_new_with_options_async(request, runtime)

    def query_sms_send_fail_details_url_with_options(
        self,
        request: dysms_20170620_models.QuerySmsSendFailDetailsUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSendFailDetailsUrlResponse:
        """
        @param request: QuerySmsSendFailDetailsUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSendFailDetailsUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
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
            action='QuerySmsSendFailDetailsUrl',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSendFailDetailsUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_send_fail_details_url_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsSendFailDetailsUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSendFailDetailsUrlResponse:
        """
        @param request: QuerySmsSendFailDetailsUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSendFailDetailsUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
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
            action='QuerySmsSendFailDetailsUrl',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSendFailDetailsUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_send_fail_details_url(
        self,
        request: dysms_20170620_models.QuerySmsSendFailDetailsUrlRequest,
    ) -> dysms_20170620_models.QuerySmsSendFailDetailsUrlResponse:
        """
        @param request: QuerySmsSendFailDetailsUrlRequest
        @return: QuerySmsSendFailDetailsUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_send_fail_details_url_with_options(request, runtime)

    async def query_sms_send_fail_details_url_async(
        self,
        request: dysms_20170620_models.QuerySmsSendFailDetailsUrlRequest,
    ) -> dysms_20170620_models.QuerySmsSendFailDetailsUrlResponse:
        """
        @param request: QuerySmsSendFailDetailsUrlRequest
        @return: QuerySmsSendFailDetailsUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_send_fail_details_url_with_options_async(request, runtime)

    def query_sms_send_fail_details_url_new_with_options(
        self,
        request: dysms_20170620_models.QuerySmsSendFailDetailsUrlNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSendFailDetailsUrlNewResponse:
        """
        @param request: QuerySmsSendFailDetailsUrlNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSendFailDetailsUrlNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
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
            action='QuerySmsSendFailDetailsUrlNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSendFailDetailsUrlNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_send_fail_details_url_new_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsSendFailDetailsUrlNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSendFailDetailsUrlNewResponse:
        """
        @param request: QuerySmsSendFailDetailsUrlNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSendFailDetailsUrlNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
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
            action='QuerySmsSendFailDetailsUrlNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSendFailDetailsUrlNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_send_fail_details_url_new(
        self,
        request: dysms_20170620_models.QuerySmsSendFailDetailsUrlNewRequest,
    ) -> dysms_20170620_models.QuerySmsSendFailDetailsUrlNewResponse:
        """
        @param request: QuerySmsSendFailDetailsUrlNewRequest
        @return: QuerySmsSendFailDetailsUrlNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_send_fail_details_url_new_with_options(request, runtime)

    async def query_sms_send_fail_details_url_new_async(
        self,
        request: dysms_20170620_models.QuerySmsSendFailDetailsUrlNewRequest,
    ) -> dysms_20170620_models.QuerySmsSendFailDetailsUrlNewResponse:
        """
        @param request: QuerySmsSendFailDetailsUrlNewRequest
        @return: QuerySmsSendFailDetailsUrlNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_send_fail_details_url_new_with_options_async(request, runtime)

    def query_sms_sign_detail_by_sign_id_new_with_options(
        self,
        request: dysms_20170620_models.QuerySmsSignDetailBySignIdNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSignDetailBySignIdNewResponse:
        """
        @param request: QuerySmsSignDetailBySignIdNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSignDetailBySignIdNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_gray):
            query['SignGray'] = request.sign_gray
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSignDetailBySignIdNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSignDetailBySignIdNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_sign_detail_by_sign_id_new_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsSignDetailBySignIdNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSignDetailBySignIdNewResponse:
        """
        @param request: QuerySmsSignDetailBySignIdNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSignDetailBySignIdNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_gray):
            query['SignGray'] = request.sign_gray
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSignDetailBySignIdNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSignDetailBySignIdNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_sign_detail_by_sign_id_new(
        self,
        request: dysms_20170620_models.QuerySmsSignDetailBySignIdNewRequest,
    ) -> dysms_20170620_models.QuerySmsSignDetailBySignIdNewResponse:
        """
        @param request: QuerySmsSignDetailBySignIdNewRequest
        @return: QuerySmsSignDetailBySignIdNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_sign_detail_by_sign_id_new_with_options(request, runtime)

    async def query_sms_sign_detail_by_sign_id_new_async(
        self,
        request: dysms_20170620_models.QuerySmsSignDetailBySignIdNewRequest,
    ) -> dysms_20170620_models.QuerySmsSignDetailBySignIdNewResponse:
        """
        @param request: QuerySmsSignDetailBySignIdNewRequest
        @return: QuerySmsSignDetailBySignIdNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_sign_detail_by_sign_id_new_with_options_async(request, runtime)

    def query_sms_sign_last_range_with_options(
        self,
        request: dysms_20170620_models.QuerySmsSignLastRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSignLastRangeResponse:
        """
        @param request: QuerySmsSignLastRangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSignLastRangeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_state):
            query['AuditState'] = request.audit_state
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.is_globe_sign):
            query['IsGlobeSign'] = request.is_globe_sign
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.need_default_sign):
            query['NeedDefaultSign'] = request.need_default_sign
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
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
            action='QuerySmsSignLastRange',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSignLastRangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_sign_last_range_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsSignLastRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSignLastRangeResponse:
        """
        @param request: QuerySmsSignLastRangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSignLastRangeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_state):
            query['AuditState'] = request.audit_state
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.is_globe_sign):
            query['IsGlobeSign'] = request.is_globe_sign
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.need_default_sign):
            query['NeedDefaultSign'] = request.need_default_sign
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
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
            action='QuerySmsSignLastRange',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSignLastRangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_sign_last_range(
        self,
        request: dysms_20170620_models.QuerySmsSignLastRangeRequest,
    ) -> dysms_20170620_models.QuerySmsSignLastRangeResponse:
        """
        @param request: QuerySmsSignLastRangeRequest
        @return: QuerySmsSignLastRangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_sign_last_range_with_options(request, runtime)

    async def query_sms_sign_last_range_async(
        self,
        request: dysms_20170620_models.QuerySmsSignLastRangeRequest,
    ) -> dysms_20170620_models.QuerySmsSignLastRangeResponse:
        """
        @param request: QuerySmsSignLastRangeRequest
        @return: QuerySmsSignLastRangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_sign_last_range_with_options_async(request, runtime)

    def query_sms_sign_last_range_new_with_options(
        self,
        request: dysms_20170620_models.QuerySmsSignLastRangeNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSignLastRangeNewResponse:
        """
        @param request: QuerySmsSignLastRangeNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSignLastRangeNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_state):
            query['AuditState'] = request.audit_state
        if not UtilClient.is_unset(request.is_globe_sign):
            query['IsGlobeSign'] = request.is_globe_sign
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.need_default_sign):
            query['NeedDefaultSign'] = request.need_default_sign
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSignLastRangeNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSignLastRangeNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_sign_last_range_new_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsSignLastRangeNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSignLastRangeNewResponse:
        """
        @param request: QuerySmsSignLastRangeNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSignLastRangeNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_state):
            query['AuditState'] = request.audit_state
        if not UtilClient.is_unset(request.is_globe_sign):
            query['IsGlobeSign'] = request.is_globe_sign
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.need_default_sign):
            query['NeedDefaultSign'] = request.need_default_sign
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSignLastRangeNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSignLastRangeNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_sign_last_range_new(
        self,
        request: dysms_20170620_models.QuerySmsSignLastRangeNewRequest,
    ) -> dysms_20170620_models.QuerySmsSignLastRangeNewResponse:
        """
        @param request: QuerySmsSignLastRangeNewRequest
        @return: QuerySmsSignLastRangeNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_sign_last_range_new_with_options(request, runtime)

    async def query_sms_sign_last_range_new_async(
        self,
        request: dysms_20170620_models.QuerySmsSignLastRangeNewRequest,
    ) -> dysms_20170620_models.QuerySmsSignLastRangeNewResponse:
        """
        @param request: QuerySmsSignLastRangeNewRequest
        @return: QuerySmsSignLastRangeNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_sign_last_range_new_with_options_async(request, runtime)

    def query_sms_sign_list_with_options(
        self,
        request: dysms_20170620_models.QuerySmsSignListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSignListResponse:
        """
        @param request: QuerySmsSignListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSignListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_state):
            query['AuditState'] = request.audit_state
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.is_globe_sign):
            query['IsGlobeSign'] = request.is_globe_sign
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSignList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSignListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_sign_list_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsSignListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSignListResponse:
        """
        @param request: QuerySmsSignListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSignListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_state):
            query['AuditState'] = request.audit_state
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.is_globe_sign):
            query['IsGlobeSign'] = request.is_globe_sign
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSignList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSignListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_sign_list(
        self,
        request: dysms_20170620_models.QuerySmsSignListRequest,
    ) -> dysms_20170620_models.QuerySmsSignListResponse:
        """
        @param request: QuerySmsSignListRequest
        @return: QuerySmsSignListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_sign_list_with_options(request, runtime)

    async def query_sms_sign_list_async(
        self,
        request: dysms_20170620_models.QuerySmsSignListRequest,
    ) -> dysms_20170620_models.QuerySmsSignListResponse:
        """
        @param request: QuerySmsSignListRequest
        @return: QuerySmsSignListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_sign_list_with_options_async(request, runtime)

    def query_sms_sign_list_new_with_options(
        self,
        tmp_req: dysms_20170620_models.QuerySmsSignListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSignListNewResponse:
        """
        @param tmp_req: QuerySmsSignListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSignListNewResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysms_20170620_models.QuerySmsSignListNewShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.operator_codes):
            request.operator_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operator_codes, 'OperatorCodes', 'json')
        query = {}
        if not UtilClient.is_unset(request.aggregated_register_status):
            query['AggregatedRegisterStatus'] = request.aggregated_register_status
        if not UtilClient.is_unset(request.audit_state):
            query['AuditState'] = request.audit_state
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.is_globe_sign):
            query['IsGlobeSign'] = request.is_globe_sign
        if not UtilClient.is_unset(request.operator_codes_shrink):
            query['OperatorCodes'] = request.operator_codes_shrink
        if not UtilClient.is_unset(request.operator_register_status):
            query['OperatorRegisterStatus'] = request.operator_register_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.qualification_name):
            query['QualificationName'] = request.qualification_name
        if not UtilClient.is_unset(request.register_result):
            query['RegisterResult'] = request.register_result
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sign_source):
            query['SignSource'] = request.sign_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSignListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSignListNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_sign_list_new_with_options_async(
        self,
        tmp_req: dysms_20170620_models.QuerySmsSignListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSignListNewResponse:
        """
        @param tmp_req: QuerySmsSignListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSignListNewResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dysms_20170620_models.QuerySmsSignListNewShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.operator_codes):
            request.operator_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operator_codes, 'OperatorCodes', 'json')
        query = {}
        if not UtilClient.is_unset(request.aggregated_register_status):
            query['AggregatedRegisterStatus'] = request.aggregated_register_status
        if not UtilClient.is_unset(request.audit_state):
            query['AuditState'] = request.audit_state
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.is_globe_sign):
            query['IsGlobeSign'] = request.is_globe_sign
        if not UtilClient.is_unset(request.operator_codes_shrink):
            query['OperatorCodes'] = request.operator_codes_shrink
        if not UtilClient.is_unset(request.operator_register_status):
            query['OperatorRegisterStatus'] = request.operator_register_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.qualification_name):
            query['QualificationName'] = request.qualification_name
        if not UtilClient.is_unset(request.register_result):
            query['RegisterResult'] = request.register_result
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sign_source):
            query['SignSource'] = request.sign_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSignListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSignListNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_sign_list_new(
        self,
        request: dysms_20170620_models.QuerySmsSignListNewRequest,
    ) -> dysms_20170620_models.QuerySmsSignListNewResponse:
        """
        @param request: QuerySmsSignListNewRequest
        @return: QuerySmsSignListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_sign_list_new_with_options(request, runtime)

    async def query_sms_sign_list_new_async(
        self,
        request: dysms_20170620_models.QuerySmsSignListNewRequest,
    ) -> dysms_20170620_models.QuerySmsSignListNewResponse:
        """
        @param request: QuerySmsSignListNewRequest
        @return: QuerySmsSignListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_sign_list_new_with_options_async(request, runtime)

    def query_sms_sign_valid_with_options(
        self,
        request: dysms_20170620_models.QuerySmsSignValidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSignValidResponse:
        """
        @param request: QuerySmsSignValidRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSignValidResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSignValid',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSignValidResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_sign_valid_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsSignValidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSignValidResponse:
        """
        @param request: QuerySmsSignValidRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSignValidResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSignValid',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSignValidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_sign_valid(
        self,
        request: dysms_20170620_models.QuerySmsSignValidRequest,
    ) -> dysms_20170620_models.QuerySmsSignValidResponse:
        """
        @param request: QuerySmsSignValidRequest
        @return: QuerySmsSignValidResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_sign_valid_with_options(request, runtime)

    async def query_sms_sign_valid_async(
        self,
        request: dysms_20170620_models.QuerySmsSignValidRequest,
    ) -> dysms_20170620_models.QuerySmsSignValidResponse:
        """
        @param request: QuerySmsSignValidRequest
        @return: QuerySmsSignValidResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_sign_valid_with_options_async(request, runtime)

    def query_sms_sign_valid_new_with_options(
        self,
        request: dysms_20170620_models.QuerySmsSignValidNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSignValidNewResponse:
        """
        @param request: QuerySmsSignValidNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSignValidNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sign_upgrade):
            query['SignUpgrade'] = request.sign_upgrade
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSignValidNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSignValidNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_sign_valid_new_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsSignValidNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsSignValidNewResponse:
        """
        @param request: QuerySmsSignValidNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsSignValidNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.sign_upgrade):
            query['SignUpgrade'] = request.sign_upgrade
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsSignValidNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsSignValidNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_sign_valid_new(
        self,
        request: dysms_20170620_models.QuerySmsSignValidNewRequest,
    ) -> dysms_20170620_models.QuerySmsSignValidNewResponse:
        """
        @param request: QuerySmsSignValidNewRequest
        @return: QuerySmsSignValidNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_sign_valid_new_with_options(request, runtime)

    async def query_sms_sign_valid_new_async(
        self,
        request: dysms_20170620_models.QuerySmsSignValidNewRequest,
    ) -> dysms_20170620_models.QuerySmsSignValidNewResponse:
        """
        @param request: QuerySmsSignValidNewRequest
        @return: QuerySmsSignValidNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_sign_valid_new_with_options_async(request, runtime)

    def query_sms_statistics_with_options(
        self,
        request: dysms_20170620_models.QuerySmsStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsStatisticsResponse:
        """
        @param request: QuerySmsStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsStatistics',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_statistics_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsStatisticsResponse:
        """
        @param request: QuerySmsStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsStatistics',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_statistics(
        self,
        request: dysms_20170620_models.QuerySmsStatisticsRequest,
    ) -> dysms_20170620_models.QuerySmsStatisticsResponse:
        """
        @param request: QuerySmsStatisticsRequest
        @return: QuerySmsStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_statistics_with_options(request, runtime)

    async def query_sms_statistics_async(
        self,
        request: dysms_20170620_models.QuerySmsStatisticsRequest,
    ) -> dysms_20170620_models.QuerySmsStatisticsResponse:
        """
        @param request: QuerySmsStatisticsRequest
        @return: QuerySmsStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_statistics_with_options_async(request, runtime)

    def query_sms_statistics_by_template_with_options(
        self,
        request: dysms_20170620_models.QuerySmsStatisticsByTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsStatisticsByTemplateResponse:
        """
        @param request: QuerySmsStatisticsByTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsStatisticsByTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsStatisticsByTemplate',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsStatisticsByTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_statistics_by_template_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsStatisticsByTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsStatisticsByTemplateResponse:
        """
        @param request: QuerySmsStatisticsByTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsStatisticsByTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsStatisticsByTemplate',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsStatisticsByTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_statistics_by_template(
        self,
        request: dysms_20170620_models.QuerySmsStatisticsByTemplateRequest,
    ) -> dysms_20170620_models.QuerySmsStatisticsByTemplateResponse:
        """
        @param request: QuerySmsStatisticsByTemplateRequest
        @return: QuerySmsStatisticsByTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_statistics_by_template_with_options(request, runtime)

    async def query_sms_statistics_by_template_async(
        self,
        request: dysms_20170620_models.QuerySmsStatisticsByTemplateRequest,
    ) -> dysms_20170620_models.QuerySmsStatisticsByTemplateResponse:
        """
        @param request: QuerySmsStatisticsByTemplateRequest
        @return: QuerySmsStatisticsByTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_statistics_by_template_with_options_async(request, runtime)

    def query_sms_statistics_by_template_new_with_options(
        self,
        request: dysms_20170620_models.QuerySmsStatisticsByTemplateNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsStatisticsByTemplateNewResponse:
        """
        @param request: QuerySmsStatisticsByTemplateNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsStatisticsByTemplateNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsStatisticsByTemplateNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsStatisticsByTemplateNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_statistics_by_template_new_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsStatisticsByTemplateNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsStatisticsByTemplateNewResponse:
        """
        @param request: QuerySmsStatisticsByTemplateNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsStatisticsByTemplateNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsStatisticsByTemplateNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsStatisticsByTemplateNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_statistics_by_template_new(
        self,
        request: dysms_20170620_models.QuerySmsStatisticsByTemplateNewRequest,
    ) -> dysms_20170620_models.QuerySmsStatisticsByTemplateNewResponse:
        """
        @param request: QuerySmsStatisticsByTemplateNewRequest
        @return: QuerySmsStatisticsByTemplateNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_statistics_by_template_new_with_options(request, runtime)

    async def query_sms_statistics_by_template_new_async(
        self,
        request: dysms_20170620_models.QuerySmsStatisticsByTemplateNewRequest,
    ) -> dysms_20170620_models.QuerySmsStatisticsByTemplateNewResponse:
        """
        @param request: QuerySmsStatisticsByTemplateNewRequest
        @return: QuerySmsStatisticsByTemplateNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_statistics_by_template_new_with_options_async(request, runtime)

    def query_sms_statistics_new_with_options(
        self,
        request: dysms_20170620_models.QuerySmsStatisticsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsStatisticsNewResponse:
        """
        @param request: QuerySmsStatisticsNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsStatisticsNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsStatisticsNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsStatisticsNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_statistics_new_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsStatisticsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsStatisticsNewResponse:
        """
        @param request: QuerySmsStatisticsNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsStatisticsNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsStatisticsNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsStatisticsNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_statistics_new(
        self,
        request: dysms_20170620_models.QuerySmsStatisticsNewRequest,
    ) -> dysms_20170620_models.QuerySmsStatisticsNewResponse:
        """
        @param request: QuerySmsStatisticsNewRequest
        @return: QuerySmsStatisticsNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_statistics_new_with_options(request, runtime)

    async def query_sms_statistics_new_async(
        self,
        request: dysms_20170620_models.QuerySmsStatisticsNewRequest,
    ) -> dysms_20170620_models.QuerySmsStatisticsNewResponse:
        """
        @param request: QuerySmsStatisticsNewRequest
        @return: QuerySmsStatisticsNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_statistics_new_with_options_async(request, runtime)

    def query_sms_statistics_url_with_options(
        self,
        request: dysms_20170620_models.QuerySmsStatisticsUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsStatisticsUrlResponse:
        """
        @param request: QuerySmsStatisticsUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsStatisticsUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsStatisticsUrl',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsStatisticsUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_statistics_url_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsStatisticsUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsStatisticsUrlResponse:
        """
        @param request: QuerySmsStatisticsUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsStatisticsUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsStatisticsUrl',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsStatisticsUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_statistics_url(
        self,
        request: dysms_20170620_models.QuerySmsStatisticsUrlRequest,
    ) -> dysms_20170620_models.QuerySmsStatisticsUrlResponse:
        """
        @param request: QuerySmsStatisticsUrlRequest
        @return: QuerySmsStatisticsUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_statistics_url_with_options(request, runtime)

    async def query_sms_statistics_url_async(
        self,
        request: dysms_20170620_models.QuerySmsStatisticsUrlRequest,
    ) -> dysms_20170620_models.QuerySmsStatisticsUrlResponse:
        """
        @param request: QuerySmsStatisticsUrlRequest
        @return: QuerySmsStatisticsUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_statistics_url_with_options_async(request, runtime)

    def query_sms_statistics_url_new_with_options(
        self,
        request: dysms_20170620_models.QuerySmsStatisticsUrlNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsStatisticsUrlNewResponse:
        """
        @param request: QuerySmsStatisticsUrlNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsStatisticsUrlNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsStatisticsUrlNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsStatisticsUrlNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_statistics_url_new_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsStatisticsUrlNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsStatisticsUrlNewResponse:
        """
        @param request: QuerySmsStatisticsUrlNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsStatisticsUrlNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsStatisticsUrlNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsStatisticsUrlNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_statistics_url_new(
        self,
        request: dysms_20170620_models.QuerySmsStatisticsUrlNewRequest,
    ) -> dysms_20170620_models.QuerySmsStatisticsUrlNewResponse:
        """
        @param request: QuerySmsStatisticsUrlNewRequest
        @return: QuerySmsStatisticsUrlNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_statistics_url_new_with_options(request, runtime)

    async def query_sms_statistics_url_new_async(
        self,
        request: dysms_20170620_models.QuerySmsStatisticsUrlNewRequest,
    ) -> dysms_20170620_models.QuerySmsStatisticsUrlNewResponse:
        """
        @param request: QuerySmsStatisticsUrlNewRequest
        @return: QuerySmsStatisticsUrlNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_statistics_url_new_with_options_async(request, runtime)

    def query_sms_step_with_options(
        self,
        request: dysms_20170620_models.QuerySmsStepRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsStepResponse:
        """
        @param request: QuerySmsStepRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsStepResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsStep',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsStepResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_step_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsStepRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsStepResponse:
        """
        @param request: QuerySmsStepRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsStepResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsStep',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsStepResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_step(
        self,
        request: dysms_20170620_models.QuerySmsStepRequest,
    ) -> dysms_20170620_models.QuerySmsStepResponse:
        """
        @param request: QuerySmsStepRequest
        @return: QuerySmsStepResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_step_with_options(request, runtime)

    async def query_sms_step_async(
        self,
        request: dysms_20170620_models.QuerySmsStepRequest,
    ) -> dysms_20170620_models.QuerySmsStepResponse:
        """
        @param request: QuerySmsStepRequest
        @return: QuerySmsStepResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_step_with_options_async(request, runtime)

    def query_sms_template_by_code_with_options(
        self,
        request: dysms_20170620_models.QuerySmsTemplateByCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsTemplateByCodeResponse:
        """
        @param request: QuerySmsTemplateByCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsTemplateByCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
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
            action='QuerySmsTemplateByCode',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsTemplateByCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_template_by_code_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsTemplateByCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsTemplateByCodeResponse:
        """
        @param request: QuerySmsTemplateByCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsTemplateByCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
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
            action='QuerySmsTemplateByCode',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsTemplateByCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_template_by_code(
        self,
        request: dysms_20170620_models.QuerySmsTemplateByCodeRequest,
    ) -> dysms_20170620_models.QuerySmsTemplateByCodeResponse:
        """
        @param request: QuerySmsTemplateByCodeRequest
        @return: QuerySmsTemplateByCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_template_by_code_with_options(request, runtime)

    async def query_sms_template_by_code_async(
        self,
        request: dysms_20170620_models.QuerySmsTemplateByCodeRequest,
    ) -> dysms_20170620_models.QuerySmsTemplateByCodeResponse:
        """
        @param request: QuerySmsTemplateByCodeRequest
        @return: QuerySmsTemplateByCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_template_by_code_with_options_async(request, runtime)

    def query_sms_template_by_code_new_with_options(
        self,
        request: dysms_20170620_models.QuerySmsTemplateByCodeNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsTemplateByCodeNewResponse:
        """
        @param request: QuerySmsTemplateByCodeNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsTemplateByCodeNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
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
            action='QuerySmsTemplateByCodeNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsTemplateByCodeNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_template_by_code_new_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsTemplateByCodeNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsTemplateByCodeNewResponse:
        """
        @param request: QuerySmsTemplateByCodeNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsTemplateByCodeNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
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
            action='QuerySmsTemplateByCodeNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsTemplateByCodeNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_template_by_code_new(
        self,
        request: dysms_20170620_models.QuerySmsTemplateByCodeNewRequest,
    ) -> dysms_20170620_models.QuerySmsTemplateByCodeNewResponse:
        """
        @param request: QuerySmsTemplateByCodeNewRequest
        @return: QuerySmsTemplateByCodeNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_template_by_code_new_with_options(request, runtime)

    async def query_sms_template_by_code_new_async(
        self,
        request: dysms_20170620_models.QuerySmsTemplateByCodeNewRequest,
    ) -> dysms_20170620_models.QuerySmsTemplateByCodeNewResponse:
        """
        @param request: QuerySmsTemplateByCodeNewRequest
        @return: QuerySmsTemplateByCodeNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_template_by_code_new_with_options_async(request, runtime)

    def query_sms_template_last_range_with_options(
        self,
        request: dysms_20170620_models.QuerySmsTemplateLastRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsTemplateLastRangeResponse:
        """
        @param request: QuerySmsTemplateLastRangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsTemplateLastRangeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.need_default_template):
            query['NeedDefaultTemplate'] = request.need_default_template
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsTemplateLastRange',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsTemplateLastRangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_template_last_range_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsTemplateLastRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsTemplateLastRangeResponse:
        """
        @param request: QuerySmsTemplateLastRangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsTemplateLastRangeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.need_default_template):
            query['NeedDefaultTemplate'] = request.need_default_template
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsTemplateLastRange',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsTemplateLastRangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_template_last_range(
        self,
        request: dysms_20170620_models.QuerySmsTemplateLastRangeRequest,
    ) -> dysms_20170620_models.QuerySmsTemplateLastRangeResponse:
        """
        @param request: QuerySmsTemplateLastRangeRequest
        @return: QuerySmsTemplateLastRangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_template_last_range_with_options(request, runtime)

    async def query_sms_template_last_range_async(
        self,
        request: dysms_20170620_models.QuerySmsTemplateLastRangeRequest,
    ) -> dysms_20170620_models.QuerySmsTemplateLastRangeResponse:
        """
        @param request: QuerySmsTemplateLastRangeRequest
        @return: QuerySmsTemplateLastRangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_template_last_range_with_options_async(request, runtime)

    def query_sms_template_last_range_new_with_options(
        self,
        request: dysms_20170620_models.QuerySmsTemplateLastRangeNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsTemplateLastRangeNewResponse:
        """
        @param request: QuerySmsTemplateLastRangeNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsTemplateLastRangeNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.filter_any_param):
            query['FilterAnyParam'] = request.filter_any_param
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.need_default_template):
            query['NeedDefaultTemplate'] = request.need_default_template
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsTemplateLastRangeNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsTemplateLastRangeNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_template_last_range_new_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsTemplateLastRangeNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsTemplateLastRangeNewResponse:
        """
        @param request: QuerySmsTemplateLastRangeNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsTemplateLastRangeNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.filter_any_param):
            query['FilterAnyParam'] = request.filter_any_param
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.need_default_template):
            query['NeedDefaultTemplate'] = request.need_default_template
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_id):
            query['ProdId'] = request.prod_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsTemplateLastRangeNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsTemplateLastRangeNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_template_last_range_new(
        self,
        request: dysms_20170620_models.QuerySmsTemplateLastRangeNewRequest,
    ) -> dysms_20170620_models.QuerySmsTemplateLastRangeNewResponse:
        """
        @param request: QuerySmsTemplateLastRangeNewRequest
        @return: QuerySmsTemplateLastRangeNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_template_last_range_new_with_options(request, runtime)

    async def query_sms_template_last_range_new_async(
        self,
        request: dysms_20170620_models.QuerySmsTemplateLastRangeNewRequest,
    ) -> dysms_20170620_models.QuerySmsTemplateLastRangeNewResponse:
        """
        @param request: QuerySmsTemplateLastRangeNewRequest
        @return: QuerySmsTemplateLastRangeNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_template_last_range_new_with_options_async(request, runtime)

    def query_sms_template_list_with_options(
        self,
        request: dysms_20170620_models.QuerySmsTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsTemplateListResponse:
        """
        @param request: QuerySmsTemplateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsTemplateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_state):
            query['AuditState'] = request.audit_state
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_type):
            query['ProdType'] = request.prod_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsTemplateList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_template_list_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsTemplateListResponse:
        """
        @param request: QuerySmsTemplateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsTemplateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_state):
            query['AuditState'] = request.audit_state
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_type):
            query['ProdType'] = request.prod_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsTemplateList',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_template_list(
        self,
        request: dysms_20170620_models.QuerySmsTemplateListRequest,
    ) -> dysms_20170620_models.QuerySmsTemplateListResponse:
        """
        @param request: QuerySmsTemplateListRequest
        @return: QuerySmsTemplateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_template_list_with_options(request, runtime)

    async def query_sms_template_list_async(
        self,
        request: dysms_20170620_models.QuerySmsTemplateListRequest,
    ) -> dysms_20170620_models.QuerySmsTemplateListResponse:
        """
        @param request: QuerySmsTemplateListRequest
        @return: QuerySmsTemplateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_template_list_with_options_async(request, runtime)

    def query_sms_template_list_new_with_options(
        self,
        request: dysms_20170620_models.QuerySmsTemplateListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsTemplateListNewResponse:
        """
        @param request: QuerySmsTemplateListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsTemplateListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_state):
            query['AuditState'] = request.audit_state
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.intl_type):
            query['IntlType'] = request.intl_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_type):
            query['ProdType'] = request.prod_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_list_string):
            query['TagListString'] = request.tag_list_string
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsTemplateListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsTemplateListNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_template_list_new_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsTemplateListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsTemplateListNewResponse:
        """
        @param request: QuerySmsTemplateListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsTemplateListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_state):
            query['AuditState'] = request.audit_state
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.intl_type):
            query['IntlType'] = request.intl_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prod_type):
            query['ProdType'] = request.prod_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_list_string):
            query['TagListString'] = request.tag_list_string
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsTemplateListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsTemplateListNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_template_list_new(
        self,
        request: dysms_20170620_models.QuerySmsTemplateListNewRequest,
    ) -> dysms_20170620_models.QuerySmsTemplateListNewResponse:
        """
        @param request: QuerySmsTemplateListNewRequest
        @return: QuerySmsTemplateListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_template_list_new_with_options(request, runtime)

    async def query_sms_template_list_new_async(
        self,
        request: dysms_20170620_models.QuerySmsTemplateListNewRequest,
    ) -> dysms_20170620_models.QuerySmsTemplateListNewResponse:
        """
        @param request: QuerySmsTemplateListNewRequest
        @return: QuerySmsTemplateListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_template_list_new_with_options_async(request, runtime)

    def query_sms_user_tags_with_options(
        self,
        request: dysms_20170620_models.QuerySmsUserTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsUserTagsResponse:
        """
        @param request: QuerySmsUserTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsUserTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsUserTags',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsUserTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_user_tags_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsUserTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsUserTagsResponse:
        """
        @param request: QuerySmsUserTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsUserTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsUserTags',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsUserTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_user_tags(
        self,
        request: dysms_20170620_models.QuerySmsUserTagsRequest,
    ) -> dysms_20170620_models.QuerySmsUserTagsResponse:
        """
        @param request: QuerySmsUserTagsRequest
        @return: QuerySmsUserTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_user_tags_with_options(request, runtime)

    async def query_sms_user_tags_async(
        self,
        request: dysms_20170620_models.QuerySmsUserTagsRequest,
    ) -> dysms_20170620_models.QuerySmsUserTagsResponse:
        """
        @param request: QuerySmsUserTagsRequest
        @return: QuerySmsUserTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_user_tags_with_options_async(request, runtime)

    def query_sms_user_tags_new_with_options(
        self,
        request: dysms_20170620_models.QuerySmsUserTagsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsUserTagsNewResponse:
        """
        @param request: QuerySmsUserTagsNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsUserTagsNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsUserTagsNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsUserTagsNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_user_tags_new_with_options_async(
        self,
        request: dysms_20170620_models.QuerySmsUserTagsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QuerySmsUserTagsNewResponse:
        """
        @param request: QuerySmsUserTagsNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsUserTagsNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsUserTagsNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QuerySmsUserTagsNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_user_tags_new(
        self,
        request: dysms_20170620_models.QuerySmsUserTagsNewRequest,
    ) -> dysms_20170620_models.QuerySmsUserTagsNewResponse:
        """
        @param request: QuerySmsUserTagsNewRequest
        @return: QuerySmsUserTagsNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_user_tags_new_with_options(request, runtime)

    async def query_sms_user_tags_new_async(
        self,
        request: dysms_20170620_models.QuerySmsUserTagsNewRequest,
    ) -> dysms_20170620_models.QuerySmsUserTagsNewResponse:
        """
        @param request: QuerySmsUserTagsNewRequest
        @return: QuerySmsUserTagsNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_user_tags_new_with_options_async(request, runtime)

    def query_standar_template_collections_with_options(
        self,
        request: dysms_20170620_models.QueryStandarTemplateCollectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryStandarTemplateCollectionsResponse:
        """
        @param request: QueryStandarTemplateCollectionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryStandarTemplateCollectionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_content):
            query['TemplateContent'] = request.template_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStandarTemplateCollections',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryStandarTemplateCollectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_standar_template_collections_with_options_async(
        self,
        request: dysms_20170620_models.QueryStandarTemplateCollectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryStandarTemplateCollectionsResponse:
        """
        @param request: QueryStandarTemplateCollectionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryStandarTemplateCollectionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_content):
            query['TemplateContent'] = request.template_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStandarTemplateCollections',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryStandarTemplateCollectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_standar_template_collections(
        self,
        request: dysms_20170620_models.QueryStandarTemplateCollectionsRequest,
    ) -> dysms_20170620_models.QueryStandarTemplateCollectionsResponse:
        """
        @param request: QueryStandarTemplateCollectionsRequest
        @return: QueryStandarTemplateCollectionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_standar_template_collections_with_options(request, runtime)

    async def query_standar_template_collections_async(
        self,
        request: dysms_20170620_models.QueryStandarTemplateCollectionsRequest,
    ) -> dysms_20170620_models.QueryStandarTemplateCollectionsResponse:
        """
        @param request: QueryStandarTemplateCollectionsRequest
        @return: QueryStandarTemplateCollectionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_standar_template_collections_with_options_async(request, runtime)

    def query_standar_template_collections_new_with_options(
        self,
        request: dysms_20170620_models.QueryStandarTemplateCollectionsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryStandarTemplateCollectionsNewResponse:
        """
        @param request: QueryStandarTemplateCollectionsNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryStandarTemplateCollectionsNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_content):
            query['TemplateContent'] = request.template_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStandarTemplateCollectionsNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryStandarTemplateCollectionsNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_standar_template_collections_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryStandarTemplateCollectionsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryStandarTemplateCollectionsNewResponse:
        """
        @param request: QueryStandarTemplateCollectionsNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryStandarTemplateCollectionsNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_content):
            query['TemplateContent'] = request.template_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStandarTemplateCollectionsNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryStandarTemplateCollectionsNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_standar_template_collections_new(
        self,
        request: dysms_20170620_models.QueryStandarTemplateCollectionsNewRequest,
    ) -> dysms_20170620_models.QueryStandarTemplateCollectionsNewResponse:
        """
        @param request: QueryStandarTemplateCollectionsNewRequest
        @return: QueryStandarTemplateCollectionsNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_standar_template_collections_new_with_options(request, runtime)

    async def query_standar_template_collections_new_async(
        self,
        request: dysms_20170620_models.QueryStandarTemplateCollectionsNewRequest,
    ) -> dysms_20170620_models.QueryStandarTemplateCollectionsNewResponse:
        """
        @param request: QueryStandarTemplateCollectionsNewRequest
        @return: QueryStandarTemplateCollectionsNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_standar_template_collections_new_with_options_async(request, runtime)

    def query_standard_protocol_with_options(
        self,
        request: dysms_20170620_models.QueryStandardProtocolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryStandardProtocolResponse:
        """
        @param request: QueryStandardProtocolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryStandardProtocolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStandardProtocol',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryStandardProtocolResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_standard_protocol_with_options_async(
        self,
        request: dysms_20170620_models.QueryStandardProtocolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryStandardProtocolResponse:
        """
        @param request: QueryStandardProtocolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryStandardProtocolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStandardProtocol',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryStandardProtocolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_standard_protocol(
        self,
        request: dysms_20170620_models.QueryStandardProtocolRequest,
    ) -> dysms_20170620_models.QueryStandardProtocolResponse:
        """
        @param request: QueryStandardProtocolRequest
        @return: QueryStandardProtocolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_standard_protocol_with_options(request, runtime)

    async def query_standard_protocol_async(
        self,
        request: dysms_20170620_models.QueryStandardProtocolRequest,
    ) -> dysms_20170620_models.QueryStandardProtocolResponse:
        """
        @param request: QueryStandardProtocolRequest
        @return: QueryStandardProtocolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_standard_protocol_with_options_async(request, runtime)

    def query_standard_protocol_list_new_with_options(
        self,
        request: dysms_20170620_models.QueryStandardProtocolListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryStandardProtocolListNewResponse:
        """
        @param request: QueryStandardProtocolListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryStandardProtocolListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStandardProtocolListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryStandardProtocolListNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_standard_protocol_list_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryStandardProtocolListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryStandardProtocolListNewResponse:
        """
        @param request: QueryStandardProtocolListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryStandardProtocolListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStandardProtocolListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryStandardProtocolListNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_standard_protocol_list_new(
        self,
        request: dysms_20170620_models.QueryStandardProtocolListNewRequest,
    ) -> dysms_20170620_models.QueryStandardProtocolListNewResponse:
        """
        @param request: QueryStandardProtocolListNewRequest
        @return: QueryStandardProtocolListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_standard_protocol_list_new_with_options(request, runtime)

    async def query_standard_protocol_list_new_async(
        self,
        request: dysms_20170620_models.QueryStandardProtocolListNewRequest,
    ) -> dysms_20170620_models.QueryStandardProtocolListNewResponse:
        """
        @param request: QueryStandardProtocolListNewRequest
        @return: QueryStandardProtocolListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_standard_protocol_list_new_with_options_async(request, runtime)

    def query_tag_resources_with_options(
        self,
        request: dysms_20170620_models.QueryTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryTagResourcesResponse:
        """
        @param request: QueryTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
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
            action='QueryTagResources',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_tag_resources_with_options_async(
        self,
        request: dysms_20170620_models.QueryTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryTagResourcesResponse:
        """
        @param request: QueryTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
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
            action='QueryTagResources',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_tag_resources(
        self,
        request: dysms_20170620_models.QueryTagResourcesRequest,
    ) -> dysms_20170620_models.QueryTagResourcesResponse:
        """
        @param request: QueryTagResourcesRequest
        @return: QueryTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_tag_resources_with_options(request, runtime)

    async def query_tag_resources_async(
        self,
        request: dysms_20170620_models.QueryTagResourcesRequest,
    ) -> dysms_20170620_models.QueryTagResourcesResponse:
        """
        @param request: QueryTagResourcesRequest
        @return: QueryTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_tag_resources_with_options_async(request, runtime)

    def query_tag_resources_new_with_options(
        self,
        request: dysms_20170620_models.QueryTagResourcesNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryTagResourcesNewResponse:
        """
        @param request: QueryTagResourcesNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTagResourcesNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
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
        if not UtilClient.is_unset(request.resource_id_list_string):
            query['ResourceIdListString'] = request.resource_id_list_string
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tag_list_string):
            query['TagListString'] = request.tag_list_string
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTagResourcesNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryTagResourcesNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_tag_resources_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryTagResourcesNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryTagResourcesNewResponse:
        """
        @param request: QueryTagResourcesNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTagResourcesNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
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
        if not UtilClient.is_unset(request.resource_id_list_string):
            query['ResourceIdListString'] = request.resource_id_list_string
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tag_list_string):
            query['TagListString'] = request.tag_list_string
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTagResourcesNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryTagResourcesNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_tag_resources_new(
        self,
        request: dysms_20170620_models.QueryTagResourcesNewRequest,
    ) -> dysms_20170620_models.QueryTagResourcesNewResponse:
        """
        @param request: QueryTagResourcesNewRequest
        @return: QueryTagResourcesNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_tag_resources_new_with_options(request, runtime)

    async def query_tag_resources_new_async(
        self,
        request: dysms_20170620_models.QueryTagResourcesNewRequest,
    ) -> dysms_20170620_models.QueryTagResourcesNewResponse:
        """
        @param request: QueryTagResourcesNewRequest
        @return: QueryTagResourcesNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_tag_resources_new_with_options_async(request, runtime)

    def query_tmp_effect_report_data_with_options(
        self,
        request: dysms_20170620_models.QueryTmpEffectReportDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryTmpEffectReportDataResponse:
        """
        @summary 发送效果统计
        
        @param request: QueryTmpEffectReportDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTmpEffectReportDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.tmp_code):
            query['TmpCode'] = request.tmp_code
        if not UtilClient.is_unset(request.tmp_name):
            query['TmpName'] = request.tmp_name
        if not UtilClient.is_unset(request.vendor_code):
            query['VendorCode'] = request.vendor_code
        if not UtilClient.is_unset(request.vendor_name):
            query['VendorName'] = request.vendor_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTmpEffectReportData',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryTmpEffectReportDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_tmp_effect_report_data_with_options_async(
        self,
        request: dysms_20170620_models.QueryTmpEffectReportDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryTmpEffectReportDataResponse:
        """
        @summary 发送效果统计
        
        @param request: QueryTmpEffectReportDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTmpEffectReportDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.tmp_code):
            query['TmpCode'] = request.tmp_code
        if not UtilClient.is_unset(request.tmp_name):
            query['TmpName'] = request.tmp_name
        if not UtilClient.is_unset(request.vendor_code):
            query['VendorCode'] = request.vendor_code
        if not UtilClient.is_unset(request.vendor_name):
            query['VendorName'] = request.vendor_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTmpEffectReportData',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryTmpEffectReportDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_tmp_effect_report_data(
        self,
        request: dysms_20170620_models.QueryTmpEffectReportDataRequest,
    ) -> dysms_20170620_models.QueryTmpEffectReportDataResponse:
        """
        @summary 发送效果统计
        
        @param request: QueryTmpEffectReportDataRequest
        @return: QueryTmpEffectReportDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_tmp_effect_report_data_with_options(request, runtime)

    async def query_tmp_effect_report_data_async(
        self,
        request: dysms_20170620_models.QueryTmpEffectReportDataRequest,
    ) -> dysms_20170620_models.QueryTmpEffectReportDataResponse:
        """
        @summary 发送效果统计
        
        @param request: QueryTmpEffectReportDataRequest
        @return: QueryTmpEffectReportDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_tmp_effect_report_data_with_options_async(request, runtime)

    def query_tmp_effect_report_day_data_with_options(
        self,
        request: dysms_20170620_models.QueryTmpEffectReportDayDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryTmpEffectReportDayDataResponse:
        """
        @summary 发送效果统计-日报
        
        @param request: QueryTmpEffectReportDayDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTmpEffectReportDayDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.tmp_code):
            query['TmpCode'] = request.tmp_code
        if not UtilClient.is_unset(request.tmp_name):
            query['TmpName'] = request.tmp_name
        if not UtilClient.is_unset(request.vendor_name):
            query['VendorName'] = request.vendor_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTmpEffectReportDayData',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryTmpEffectReportDayDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_tmp_effect_report_day_data_with_options_async(
        self,
        request: dysms_20170620_models.QueryTmpEffectReportDayDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryTmpEffectReportDayDataResponse:
        """
        @summary 发送效果统计-日报
        
        @param request: QueryTmpEffectReportDayDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTmpEffectReportDayDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.tmp_code):
            query['TmpCode'] = request.tmp_code
        if not UtilClient.is_unset(request.tmp_name):
            query['TmpName'] = request.tmp_name
        if not UtilClient.is_unset(request.vendor_name):
            query['VendorName'] = request.vendor_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTmpEffectReportDayData',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryTmpEffectReportDayDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_tmp_effect_report_day_data(
        self,
        request: dysms_20170620_models.QueryTmpEffectReportDayDataRequest,
    ) -> dysms_20170620_models.QueryTmpEffectReportDayDataResponse:
        """
        @summary 发送效果统计-日报
        
        @param request: QueryTmpEffectReportDayDataRequest
        @return: QueryTmpEffectReportDayDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_tmp_effect_report_day_data_with_options(request, runtime)

    async def query_tmp_effect_report_day_data_async(
        self,
        request: dysms_20170620_models.QueryTmpEffectReportDayDataRequest,
    ) -> dysms_20170620_models.QueryTmpEffectReportDayDataResponse:
        """
        @summary 发送效果统计-日报
        
        @param request: QueryTmpEffectReportDayDataRequest
        @return: QueryTmpEffectReportDayDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_tmp_effect_report_day_data_with_options_async(request, runtime)

    def query_usertag_existence_with_options(
        self,
        request: dysms_20170620_models.QueryUsertagExistenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryUsertagExistenceResponse:
        """
        @param request: QueryUsertagExistenceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryUsertagExistenceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.usertag_position):
            query['UsertagPosition'] = request.usertag_position
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUsertagExistence',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryUsertagExistenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_usertag_existence_with_options_async(
        self,
        request: dysms_20170620_models.QueryUsertagExistenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryUsertagExistenceResponse:
        """
        @param request: QueryUsertagExistenceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryUsertagExistenceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.usertag_position):
            query['UsertagPosition'] = request.usertag_position
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUsertagExistence',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryUsertagExistenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_usertag_existence(
        self,
        request: dysms_20170620_models.QueryUsertagExistenceRequest,
    ) -> dysms_20170620_models.QueryUsertagExistenceResponse:
        """
        @param request: QueryUsertagExistenceRequest
        @return: QueryUsertagExistenceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_usertag_existence_with_options(request, runtime)

    async def query_usertag_existence_async(
        self,
        request: dysms_20170620_models.QueryUsertagExistenceRequest,
    ) -> dysms_20170620_models.QueryUsertagExistenceResponse:
        """
        @param request: QueryUsertagExistenceRequest
        @return: QueryUsertagExistenceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_usertag_existence_with_options_async(request, runtime)

    def query_warning_threshold_with_options(
        self,
        request: dysms_20170620_models.QueryWarningThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryWarningThresholdResponse:
        """
        @param request: QueryWarningThresholdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryWarningThresholdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWarningThreshold',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryWarningThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_warning_threshold_with_options_async(
        self,
        request: dysms_20170620_models.QueryWarningThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryWarningThresholdResponse:
        """
        @param request: QueryWarningThresholdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryWarningThresholdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWarningThreshold',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryWarningThresholdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_warning_threshold(
        self,
        request: dysms_20170620_models.QueryWarningThresholdRequest,
    ) -> dysms_20170620_models.QueryWarningThresholdResponse:
        """
        @param request: QueryWarningThresholdRequest
        @return: QueryWarningThresholdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_warning_threshold_with_options(request, runtime)

    async def query_warning_threshold_async(
        self,
        request: dysms_20170620_models.QueryWarningThresholdRequest,
    ) -> dysms_20170620_models.QueryWarningThresholdResponse:
        """
        @param request: QueryWarningThresholdRequest
        @return: QueryWarningThresholdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_warning_threshold_with_options_async(request, runtime)

    def query_warning_threshold_new_with_options(
        self,
        request: dysms_20170620_models.QueryWarningThresholdNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryWarningThresholdNewResponse:
        """
        @param request: QueryWarningThresholdNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryWarningThresholdNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWarningThresholdNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryWarningThresholdNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_warning_threshold_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryWarningThresholdNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryWarningThresholdNewResponse:
        """
        @param request: QueryWarningThresholdNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryWarningThresholdNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWarningThresholdNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryWarningThresholdNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_warning_threshold_new(
        self,
        request: dysms_20170620_models.QueryWarningThresholdNewRequest,
    ) -> dysms_20170620_models.QueryWarningThresholdNewResponse:
        """
        @param request: QueryWarningThresholdNewRequest
        @return: QueryWarningThresholdNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_warning_threshold_new_with_options(request, runtime)

    async def query_warning_threshold_new_async(
        self,
        request: dysms_20170620_models.QueryWarningThresholdNewRequest,
    ) -> dysms_20170620_models.QueryWarningThresholdNewResponse:
        """
        @param request: QueryWarningThresholdNewRequest
        @return: QueryWarningThresholdNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_warning_threshold_new_with_options_async(request, runtime)

    def query_work_ord_audit_list_new_with_options(
        self,
        request: dysms_20170620_models.QueryWorkOrdAuditListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryWorkOrdAuditListNewResponse:
        """
        @param request: QueryWorkOrdAuditListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryWorkOrdAuditListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWorkOrdAuditListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryWorkOrdAuditListNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_work_ord_audit_list_new_with_options_async(
        self,
        request: dysms_20170620_models.QueryWorkOrdAuditListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.QueryWorkOrdAuditListNewResponse:
        """
        @param request: QueryWorkOrdAuditListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryWorkOrdAuditListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWorkOrdAuditListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.QueryWorkOrdAuditListNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_work_ord_audit_list_new(
        self,
        request: dysms_20170620_models.QueryWorkOrdAuditListNewRequest,
    ) -> dysms_20170620_models.QueryWorkOrdAuditListNewResponse:
        """
        @param request: QueryWorkOrdAuditListNewRequest
        @return: QueryWorkOrdAuditListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_work_ord_audit_list_new_with_options(request, runtime)

    async def query_work_ord_audit_list_new_async(
        self,
        request: dysms_20170620_models.QueryWorkOrdAuditListNewRequest,
    ) -> dysms_20170620_models.QueryWorkOrdAuditListNewResponse:
        """
        @param request: QueryWorkOrdAuditListNewRequest
        @return: QueryWorkOrdAuditListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_work_ord_audit_list_new_with_options_async(request, runtime)

    def save_contacts_new_with_options(
        self,
        request: dysms_20170620_models.SaveContactsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.SaveContactsNewResponse:
        """
        @param request: SaveContactsNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveContactsNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.open_pkg_warning):
            query['OpenPkgWarning'] = request.open_pkg_warning
        if not UtilClient.is_unset(request.open_prevent_brush_warning):
            query['OpenPreventBrushWarning'] = request.open_prevent_brush_warning
        if not UtilClient.is_unset(request.open_send_warning):
            query['OpenSendWarning'] = request.open_send_warning
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.receive_sign_template_audit_result):
            query['ReceiveSignTemplateAuditResult'] = request.receive_sign_template_audit_result
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.verification_code):
            query['VerificationCode'] = request.verification_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveContactsNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.SaveContactsNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_contacts_new_with_options_async(
        self,
        request: dysms_20170620_models.SaveContactsNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.SaveContactsNewResponse:
        """
        @param request: SaveContactsNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveContactsNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.open_pkg_warning):
            query['OpenPkgWarning'] = request.open_pkg_warning
        if not UtilClient.is_unset(request.open_prevent_brush_warning):
            query['OpenPreventBrushWarning'] = request.open_prevent_brush_warning
        if not UtilClient.is_unset(request.open_send_warning):
            query['OpenSendWarning'] = request.open_send_warning
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.receive_sign_template_audit_result):
            query['ReceiveSignTemplateAuditResult'] = request.receive_sign_template_audit_result
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.verification_code):
            query['VerificationCode'] = request.verification_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveContactsNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.SaveContactsNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_contacts_new(
        self,
        request: dysms_20170620_models.SaveContactsNewRequest,
    ) -> dysms_20170620_models.SaveContactsNewResponse:
        """
        @param request: SaveContactsNewRequest
        @return: SaveContactsNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_contacts_new_with_options(request, runtime)

    async def save_contacts_new_async(
        self,
        request: dysms_20170620_models.SaveContactsNewRequest,
    ) -> dysms_20170620_models.SaveContactsNewResponse:
        """
        @param request: SaveContactsNewRequest
        @return: SaveContactsNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_contacts_new_with_options_async(request, runtime)

    def save_learning_status_new_with_options(
        self,
        request: dysms_20170620_models.SaveLearningStatusNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.SaveLearningStatusNewResponse:
        """
        @param request: SaveLearningStatusNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveLearningStatusNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveLearningStatusNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.SaveLearningStatusNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_learning_status_new_with_options_async(
        self,
        request: dysms_20170620_models.SaveLearningStatusNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.SaveLearningStatusNewResponse:
        """
        @param request: SaveLearningStatusNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveLearningStatusNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveLearningStatusNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.SaveLearningStatusNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_learning_status_new(
        self,
        request: dysms_20170620_models.SaveLearningStatusNewRequest,
    ) -> dysms_20170620_models.SaveLearningStatusNewResponse:
        """
        @param request: SaveLearningStatusNewRequest
        @return: SaveLearningStatusNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_learning_status_new_with_options(request, runtime)

    async def save_learning_status_new_async(
        self,
        request: dysms_20170620_models.SaveLearningStatusNewRequest,
    ) -> dysms_20170620_models.SaveLearningStatusNewResponse:
        """
        @param request: SaveLearningStatusNewRequest
        @return: SaveLearningStatusNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_learning_status_new_with_options_async(request, runtime)

    def select_tag_resource_with_options(
        self,
        request: dysms_20170620_models.SelectTagResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.SelectTagResourceResponse:
        """
        @param request: SelectTagResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SelectTagResourceResponse
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
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.tag_value):
            query['TagValue'] = request.tag_value
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SelectTagResource',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.SelectTagResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def select_tag_resource_with_options_async(
        self,
        request: dysms_20170620_models.SelectTagResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.SelectTagResourceResponse:
        """
        @param request: SelectTagResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SelectTagResourceResponse
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
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.tag_value):
            query['TagValue'] = request.tag_value
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SelectTagResource',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.SelectTagResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def select_tag_resource(
        self,
        request: dysms_20170620_models.SelectTagResourceRequest,
    ) -> dysms_20170620_models.SelectTagResourceResponse:
        """
        @param request: SelectTagResourceRequest
        @return: SelectTagResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.select_tag_resource_with_options(request, runtime)

    async def select_tag_resource_async(
        self,
        request: dysms_20170620_models.SelectTagResourceRequest,
    ) -> dysms_20170620_models.SelectTagResourceResponse:
        """
        @param request: SelectTagResourceRequest
        @return: SelectTagResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.select_tag_resource_with_options_async(request, runtime)

    def select_tag_resource_new_with_options(
        self,
        request: dysms_20170620_models.SelectTagResourceNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.SelectTagResourceNewResponse:
        """
        @param request: SelectTagResourceNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SelectTagResourceNewResponse
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
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.tag_value):
            query['TagValue'] = request.tag_value
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SelectTagResourceNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.SelectTagResourceNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def select_tag_resource_new_with_options_async(
        self,
        request: dysms_20170620_models.SelectTagResourceNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.SelectTagResourceNewResponse:
        """
        @param request: SelectTagResourceNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SelectTagResourceNewResponse
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
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.tag_value):
            query['TagValue'] = request.tag_value
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SelectTagResourceNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.SelectTagResourceNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def select_tag_resource_new(
        self,
        request: dysms_20170620_models.SelectTagResourceNewRequest,
    ) -> dysms_20170620_models.SelectTagResourceNewResponse:
        """
        @param request: SelectTagResourceNewRequest
        @return: SelectTagResourceNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.select_tag_resource_new_with_options(request, runtime)

    async def select_tag_resource_new_async(
        self,
        request: dysms_20170620_models.SelectTagResourceNewRequest,
    ) -> dysms_20170620_models.SelectTagResourceNewResponse:
        """
        @param request: SelectTagResourceNewRequest
        @return: SelectTagResourceNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.select_tag_resource_new_with_options_async(request, runtime)

    def send_sms_test_with_options(
        self,
        request: dysms_20170620_models.SendSmsTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.SendSmsTestResponse:
        """
        @param request: SendSmsTestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendSmsTestResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.nc_token):
            query['NcToken'] = request.nc_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.remote_ip):
            query['RemoteIp'] = request.remote_ip
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.sig):
            query['Sig'] = request.sig
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param):
            query['TemplateParam'] = request.template_param
        if not UtilClient.is_unset(request.test_type):
            query['TestType'] = request.test_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendSmsTest',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.SendSmsTestResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_sms_test_with_options_async(
        self,
        request: dysms_20170620_models.SendSmsTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.SendSmsTestResponse:
        """
        @param request: SendSmsTestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendSmsTestResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.nc_token):
            query['NcToken'] = request.nc_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.remote_ip):
            query['RemoteIp'] = request.remote_ip
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.sig):
            query['Sig'] = request.sig
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param):
            query['TemplateParam'] = request.template_param
        if not UtilClient.is_unset(request.test_type):
            query['TestType'] = request.test_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendSmsTest',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.SendSmsTestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_sms_test(
        self,
        request: dysms_20170620_models.SendSmsTestRequest,
    ) -> dysms_20170620_models.SendSmsTestResponse:
        """
        @param request: SendSmsTestRequest
        @return: SendSmsTestResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_sms_test_with_options(request, runtime)

    async def send_sms_test_async(
        self,
        request: dysms_20170620_models.SendSmsTestRequest,
    ) -> dysms_20170620_models.SendSmsTestResponse:
        """
        @param request: SendSmsTestRequest
        @return: SendSmsTestResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_sms_test_with_options_async(request, runtime)

    def send_sms_test_new_with_options(
        self,
        request: dysms_20170620_models.SendSmsTestNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.SendSmsTestNewResponse:
        """
        @param request: SendSmsTestNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendSmsTestNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.nc_token):
            query['NcToken'] = request.nc_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.remote_ip):
            query['RemoteIp'] = request.remote_ip
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.sig):
            query['Sig'] = request.sig
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param):
            query['TemplateParam'] = request.template_param
        if not UtilClient.is_unset(request.test_type):
            query['TestType'] = request.test_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendSmsTestNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.SendSmsTestNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_sms_test_new_with_options_async(
        self,
        request: dysms_20170620_models.SendSmsTestNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.SendSmsTestNewResponse:
        """
        @param request: SendSmsTestNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendSmsTestNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.nc_token):
            query['NcToken'] = request.nc_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.remote_ip):
            query['RemoteIp'] = request.remote_ip
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.sig):
            query['Sig'] = request.sig
        if not UtilClient.is_unset(request.sign_name):
            query['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param):
            query['TemplateParam'] = request.template_param
        if not UtilClient.is_unset(request.test_type):
            query['TestType'] = request.test_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendSmsTestNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.SendSmsTestNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_sms_test_new(
        self,
        request: dysms_20170620_models.SendSmsTestNewRequest,
    ) -> dysms_20170620_models.SendSmsTestNewResponse:
        """
        @param request: SendSmsTestNewRequest
        @return: SendSmsTestNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_sms_test_new_with_options(request, runtime)

    async def send_sms_test_new_async(
        self,
        request: dysms_20170620_models.SendSmsTestNewRequest,
    ) -> dysms_20170620_models.SendSmsTestNewResponse:
        """
        @param request: SendSmsTestNewRequest
        @return: SendSmsTestNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_sms_test_new_with_options_async(request, runtime)

    def send_verification_with_options(
        self,
        request: dysms_20170620_models.SendVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.SendVerificationResponse:
        """
        @param request: SendVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerification',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.SendVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_verification_with_options_async(
        self,
        request: dysms_20170620_models.SendVerificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.SendVerificationResponse:
        """
        @param request: SendVerificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendVerificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerification',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.SendVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_verification(
        self,
        request: dysms_20170620_models.SendVerificationRequest,
    ) -> dysms_20170620_models.SendVerificationResponse:
        """
        @param request: SendVerificationRequest
        @return: SendVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_verification_with_options(request, runtime)

    async def send_verification_async(
        self,
        request: dysms_20170620_models.SendVerificationRequest,
    ) -> dysms_20170620_models.SendVerificationResponse:
        """
        @param request: SendVerificationRequest
        @return: SendVerificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_verification_with_options_async(request, runtime)

    def send_verification_new_with_options(
        self,
        request: dysms_20170620_models.SendVerificationNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.SendVerificationNewResponse:
        """
        @param request: SendVerificationNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendVerificationNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerificationNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.SendVerificationNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_verification_new_with_options_async(
        self,
        request: dysms_20170620_models.SendVerificationNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.SendVerificationNewResponse:
        """
        @param request: SendVerificationNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendVerificationNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerificationNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.SendVerificationNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_verification_new(
        self,
        request: dysms_20170620_models.SendVerificationNewRequest,
    ) -> dysms_20170620_models.SendVerificationNewResponse:
        """
        @param request: SendVerificationNewRequest
        @return: SendVerificationNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_verification_new_with_options(request, runtime)

    async def send_verification_new_async(
        self,
        request: dysms_20170620_models.SendVerificationNewRequest,
    ) -> dysms_20170620_models.SendVerificationNewResponse:
        """
        @param request: SendVerificationNewRequest
        @return: SendVerificationNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_verification_new_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: dysms_20170620_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.TagResourcesResponse:
        """
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
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: dysms_20170620_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.TagResourcesResponse:
        """
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
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: dysms_20170620_models.TagResourcesRequest,
    ) -> dysms_20170620_models.TagResourcesResponse:
        """
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: dysms_20170620_models.TagResourcesRequest,
    ) -> dysms_20170620_models.TagResourcesResponse:
        """
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def tag_resources_new_with_options(
        self,
        request: dysms_20170620_models.TagResourcesNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.TagResourcesNewResponse:
        """
        @param request: TagResourcesNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesNewResponse
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
        if not UtilClient.is_unset(request.resource_id_list_string):
            query['ResourceIdListString'] = request.resource_id_list_string
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tag_list_string):
            query['TagListString'] = request.tag_list_string
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResourcesNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.TagResourcesNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_new_with_options_async(
        self,
        request: dysms_20170620_models.TagResourcesNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.TagResourcesNewResponse:
        """
        @param request: TagResourcesNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesNewResponse
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
        if not UtilClient.is_unset(request.resource_id_list_string):
            query['ResourceIdListString'] = request.resource_id_list_string
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tag_list_string):
            query['TagListString'] = request.tag_list_string
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResourcesNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.TagResourcesNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources_new(
        self,
        request: dysms_20170620_models.TagResourcesNewRequest,
    ) -> dysms_20170620_models.TagResourcesNewResponse:
        """
        @param request: TagResourcesNewRequest
        @return: TagResourcesNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_new_with_options(request, runtime)

    async def tag_resources_new_async(
        self,
        request: dysms_20170620_models.TagResourcesNewRequest,
    ) -> dysms_20170620_models.TagResourcesNewResponse:
        """
        @param request: TagResourcesNewRequest
        @return: TagResourcesNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_new_with_options_async(request, runtime)

    def tag_resources_system_tags_with_options(
        self,
        request: dysms_20170620_models.TagResourcesSystemTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.TagResourcesSystemTagsResponse:
        """
        @param request: TagResourcesSystemTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesSystemTagsResponse
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
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tag_owner_uid):
            query['TagOwnerUid'] = request.tag_owner_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResourcesSystemTags',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.TagResourcesSystemTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_system_tags_with_options_async(
        self,
        request: dysms_20170620_models.TagResourcesSystemTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.TagResourcesSystemTagsResponse:
        """
        @param request: TagResourcesSystemTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesSystemTagsResponse
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
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tag_owner_uid):
            query['TagOwnerUid'] = request.tag_owner_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResourcesSystemTags',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.TagResourcesSystemTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources_system_tags(
        self,
        request: dysms_20170620_models.TagResourcesSystemTagsRequest,
    ) -> dysms_20170620_models.TagResourcesSystemTagsResponse:
        """
        @param request: TagResourcesSystemTagsRequest
        @return: TagResourcesSystemTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_system_tags_with_options(request, runtime)

    async def tag_resources_system_tags_async(
        self,
        request: dysms_20170620_models.TagResourcesSystemTagsRequest,
    ) -> dysms_20170620_models.TagResourcesSystemTagsResponse:
        """
        @param request: TagResourcesSystemTagsRequest
        @return: TagResourcesSystemTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_system_tags_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: dysms_20170620_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.UntagResourcesResponse:
        """
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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: dysms_20170620_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.UntagResourcesResponse:
        """
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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: dysms_20170620_models.UntagResourcesRequest,
    ) -> dysms_20170620_models.UntagResourcesResponse:
        """
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: dysms_20170620_models.UntagResourcesRequest,
    ) -> dysms_20170620_models.UntagResourcesResponse:
        """
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def untag_resources_new_with_options(
        self,
        request: dysms_20170620_models.UntagResourcesNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.UntagResourcesNewResponse:
        """
        @param request: UntagResourcesNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesNewResponse
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
        if not UtilClient.is_unset(request.resource_id_list_string):
            query['ResourceIdListString'] = request.resource_id_list_string
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_list_string):
            query['TagListString'] = request.tag_list_string
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResourcesNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.UntagResourcesNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_new_with_options_async(
        self,
        request: dysms_20170620_models.UntagResourcesNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.UntagResourcesNewResponse:
        """
        @param request: UntagResourcesNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesNewResponse
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
        if not UtilClient.is_unset(request.resource_id_list_string):
            query['ResourceIdListString'] = request.resource_id_list_string
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_list_string):
            query['TagListString'] = request.tag_list_string
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResourcesNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.UntagResourcesNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources_new(
        self,
        request: dysms_20170620_models.UntagResourcesNewRequest,
    ) -> dysms_20170620_models.UntagResourcesNewResponse:
        """
        @param request: UntagResourcesNewRequest
        @return: UntagResourcesNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_new_with_options(request, runtime)

    async def untag_resources_new_async(
        self,
        request: dysms_20170620_models.UntagResourcesNewRequest,
    ) -> dysms_20170620_models.UntagResourcesNewResponse:
        """
        @param request: UntagResourcesNewRequest
        @return: UntagResourcesNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_new_with_options_async(request, runtime)

    def untag_resources_system_tags_with_options(
        self,
        request: dysms_20170620_models.UntagResourcesSystemTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.UntagResourcesSystemTagsResponse:
        """
        @param request: UntagResourcesSystemTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesSystemTagsResponse
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
        if not UtilClient.is_unset(request.tag_owner_uid):
            query['TagOwnerUid'] = request.tag_owner_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResourcesSystemTags',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.UntagResourcesSystemTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_system_tags_with_options_async(
        self,
        request: dysms_20170620_models.UntagResourcesSystemTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.UntagResourcesSystemTagsResponse:
        """
        @param request: UntagResourcesSystemTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesSystemTagsResponse
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
        if not UtilClient.is_unset(request.tag_owner_uid):
            query['TagOwnerUid'] = request.tag_owner_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResourcesSystemTags',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.UntagResourcesSystemTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources_system_tags(
        self,
        request: dysms_20170620_models.UntagResourcesSystemTagsRequest,
    ) -> dysms_20170620_models.UntagResourcesSystemTagsResponse:
        """
        @param request: UntagResourcesSystemTagsRequest
        @return: UntagResourcesSystemTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_system_tags_with_options(request, runtime)

    async def untag_resources_system_tags_async(
        self,
        request: dysms_20170620_models.UntagResourcesSystemTagsRequest,
    ) -> dysms_20170620_models.UntagResourcesSystemTagsResponse:
        """
        @param request: UntagResourcesSystemTagsRequest
        @return: UntagResourcesSystemTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_system_tags_with_options_async(request, runtime)

    def update_ip_white_list_new_with_options(
        self,
        request: dysms_20170620_models.UpdateIpWhiteListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.UpdateIpWhiteListNewResponse:
        """
        @param request: UpdateIpWhiteListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIpWhiteListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feature_code):
            query['FeatureCode'] = request.feature_code
        if not UtilClient.is_unset(request.ip_white_list):
            query['IpWhiteList'] = request.ip_white_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.real_name_ins_id):
            query['RealNameInsId'] = request.real_name_ins_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIpWhiteListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.UpdateIpWhiteListNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ip_white_list_new_with_options_async(
        self,
        request: dysms_20170620_models.UpdateIpWhiteListNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.UpdateIpWhiteListNewResponse:
        """
        @param request: UpdateIpWhiteListNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIpWhiteListNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feature_code):
            query['FeatureCode'] = request.feature_code
        if not UtilClient.is_unset(request.ip_white_list):
            query['IpWhiteList'] = request.ip_white_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.real_name_ins_id):
            query['RealNameInsId'] = request.real_name_ins_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIpWhiteListNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.UpdateIpWhiteListNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ip_white_list_new(
        self,
        request: dysms_20170620_models.UpdateIpWhiteListNewRequest,
    ) -> dysms_20170620_models.UpdateIpWhiteListNewResponse:
        """
        @param request: UpdateIpWhiteListNewRequest
        @return: UpdateIpWhiteListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_ip_white_list_new_with_options(request, runtime)

    async def update_ip_white_list_new_async(
        self,
        request: dysms_20170620_models.UpdateIpWhiteListNewRequest,
    ) -> dysms_20170620_models.UpdateIpWhiteListNewResponse:
        """
        @param request: UpdateIpWhiteListNewRequest
        @return: UpdateIpWhiteListNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_ip_white_list_new_with_options_async(request, runtime)

    def update_partner_template_new_with_options(
        self,
        request: dysms_20170620_models.UpdatePartnerTemplateNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.UpdatePartnerTemplateNewResponse:
        """
        @param request: UpdatePartnerTemplateNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePartnerTemplateNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePartnerTemplateNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.UpdatePartnerTemplateNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_partner_template_new_with_options_async(
        self,
        request: dysms_20170620_models.UpdatePartnerTemplateNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.UpdatePartnerTemplateNewResponse:
        """
        @param request: UpdatePartnerTemplateNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePartnerTemplateNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePartnerTemplateNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.UpdatePartnerTemplateNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_partner_template_new(
        self,
        request: dysms_20170620_models.UpdatePartnerTemplateNewRequest,
    ) -> dysms_20170620_models.UpdatePartnerTemplateNewResponse:
        """
        @param request: UpdatePartnerTemplateNewRequest
        @return: UpdatePartnerTemplateNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_partner_template_new_with_options(request, runtime)

    async def update_partner_template_new_async(
        self,
        request: dysms_20170620_models.UpdatePartnerTemplateNewRequest,
    ) -> dysms_20170620_models.UpdatePartnerTemplateNewResponse:
        """
        @param request: UpdatePartnerTemplateNewRequest
        @return: UpdatePartnerTemplateNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_partner_template_new_with_options_async(request, runtime)

    def update_sls_status_new_with_options(
        self,
        request: dysms_20170620_models.UpdateSlsStatusNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.UpdateSlsStatusNewResponse:
        """
        @param request: UpdateSlsStatusNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSlsStatusNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_status):
            query['AuthStatus'] = request.auth_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.save_time):
            query['SaveTime'] = request.save_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSlsStatusNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.UpdateSlsStatusNewResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sls_status_new_with_options_async(
        self,
        request: dysms_20170620_models.UpdateSlsStatusNewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.UpdateSlsStatusNewResponse:
        """
        @param request: UpdateSlsStatusNewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSlsStatusNewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_status):
            query['AuthStatus'] = request.auth_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.save_time):
            query['SaveTime'] = request.save_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSlsStatusNew',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.UpdateSlsStatusNewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sls_status_new(
        self,
        request: dysms_20170620_models.UpdateSlsStatusNewRequest,
    ) -> dysms_20170620_models.UpdateSlsStatusNewResponse:
        """
        @param request: UpdateSlsStatusNewRequest
        @return: UpdateSlsStatusNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_sls_status_new_with_options(request, runtime)

    async def update_sls_status_new_async(
        self,
        request: dysms_20170620_models.UpdateSlsStatusNewRequest,
    ) -> dysms_20170620_models.UpdateSlsStatusNewResponse:
        """
        @param request: UpdateSlsStatusNewRequest
        @return: UpdateSlsStatusNewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_sls_status_new_with_options_async(request, runtime)

    def upload_card_res_with_options(
        self,
        request: dysms_20170620_models.UploadCardResRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.UploadCardResResponse:
        """
        @summary 上传卡片素材并获取素材id
        
        @param request: UploadCardResRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadCardResResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.caller_type):
            query['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            query['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.extend_info):
            query['ExtendInfo'] = request.extend_info
        if not UtilClient.is_unset(request.file_size):
            query['FileSize'] = request.file_size
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.memo):
            query['Memo'] = request.memo
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadCardRes',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.UploadCardResResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_card_res_with_options_async(
        self,
        request: dysms_20170620_models.UploadCardResRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.UploadCardResResponse:
        """
        @summary 上传卡片素材并获取素材id
        
        @param request: UploadCardResRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadCardResResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.caller_type):
            query['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            query['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.extend_info):
            query['ExtendInfo'] = request.extend_info
        if not UtilClient.is_unset(request.file_size):
            query['FileSize'] = request.file_size
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.memo):
            query['Memo'] = request.memo
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadCardRes',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.UploadCardResResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_card_res(
        self,
        request: dysms_20170620_models.UploadCardResRequest,
    ) -> dysms_20170620_models.UploadCardResResponse:
        """
        @summary 上传卡片素材并获取素材id
        
        @param request: UploadCardResRequest
        @return: UploadCardResResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_card_res_with_options(request, runtime)

    async def upload_card_res_async(
        self,
        request: dysms_20170620_models.UploadCardResRequest,
    ) -> dysms_20170620_models.UploadCardResResponse:
        """
        @summary 上传卡片素材并获取素材id
        
        @param request: UploadCardResRequest
        @return: UploadCardResResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_card_res_with_options_async(request, runtime)

    def upload_card_res_with_dync_param_with_options(
        self,
        request: dysms_20170620_models.UploadCardResWithDyncParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.UploadCardResWithDyncParamResponse:
        """
        @summary 上传动参图片素材
        
        @param request: UploadCardResWithDyncParamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadCardResWithDyncParamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dynamic_param):
            query['DynamicParam'] = request.dynamic_param
        if not UtilClient.is_unset(request.expired_times):
            query['ExpiredTimes'] = request.expired_times
        if not UtilClient.is_unset(request.file_size):
            query['FileSize'] = request.file_size
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.memo):
            query['Memo'] = request.memo
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadCardResWithDyncParam',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.UploadCardResWithDyncParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_card_res_with_dync_param_with_options_async(
        self,
        request: dysms_20170620_models.UploadCardResWithDyncParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.UploadCardResWithDyncParamResponse:
        """
        @summary 上传动参图片素材
        
        @param request: UploadCardResWithDyncParamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadCardResWithDyncParamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dynamic_param):
            query['DynamicParam'] = request.dynamic_param
        if not UtilClient.is_unset(request.expired_times):
            query['ExpiredTimes'] = request.expired_times
        if not UtilClient.is_unset(request.file_size):
            query['FileSize'] = request.file_size
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.memo):
            query['Memo'] = request.memo
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadCardResWithDyncParam',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.UploadCardResWithDyncParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_card_res_with_dync_param(
        self,
        request: dysms_20170620_models.UploadCardResWithDyncParamRequest,
    ) -> dysms_20170620_models.UploadCardResWithDyncParamResponse:
        """
        @summary 上传动参图片素材
        
        @param request: UploadCardResWithDyncParamRequest
        @return: UploadCardResWithDyncParamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_card_res_with_dync_param_with_options(request, runtime)

    async def upload_card_res_with_dync_param_async(
        self,
        request: dysms_20170620_models.UploadCardResWithDyncParamRequest,
    ) -> dysms_20170620_models.UploadCardResWithDyncParamResponse:
        """
        @summary 上传动参图片素材
        
        @param request: UploadCardResWithDyncParamRequest
        @return: UploadCardResWithDyncParamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_card_res_with_dync_param_with_options_async(request, runtime)

    def validat_yun_sms_id_with_options(
        self,
        request: dysms_20170620_models.ValidatYunSmsIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.ValidatYunSmsIdResponse:
        """
        @param request: ValidatYunSmsIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidatYunSmsIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.data):
            query['data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidatYunSmsId',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.ValidatYunSmsIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def validat_yun_sms_id_with_options_async(
        self,
        request: dysms_20170620_models.ValidatYunSmsIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dysms_20170620_models.ValidatYunSmsIdResponse:
        """
        @param request: ValidatYunSmsIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidatYunSmsIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.data):
            query['data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidatYunSmsId',
            version='2017-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dysms_20170620_models.ValidatYunSmsIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validat_yun_sms_id(
        self,
        request: dysms_20170620_models.ValidatYunSmsIdRequest,
    ) -> dysms_20170620_models.ValidatYunSmsIdResponse:
        """
        @param request: ValidatYunSmsIdRequest
        @return: ValidatYunSmsIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.validat_yun_sms_id_with_options(request, runtime)

    async def validat_yun_sms_id_async(
        self,
        request: dysms_20170620_models.ValidatYunSmsIdRequest,
    ) -> dysms_20170620_models.ValidatYunSmsIdResponse:
        """
        @param request: ValidatYunSmsIdRequest
        @return: ValidatYunSmsIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.validat_yun_sms_id_with_options_async(request, runtime)
