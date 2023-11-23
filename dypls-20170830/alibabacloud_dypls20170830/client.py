# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dypls20170830 import models as dypls_20170830_models
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
        self._signature_algorithm = 'v2'
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('dypls', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def apply_ar_invoice_with_source_with_options(
        self,
        request: dypls_20170830_models.ApplyArInvoiceWithSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.ApplyArInvoiceWithSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.address):
            body_flat['Address'] = request.address
        if not UtilClient.is_unset(request.amount):
            body['Amount'] = request.amount
        if not UtilClient.is_unset(request.app_code):
            body['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.applier):
            body['Applier'] = request.applier
        if not UtilClient.is_unset(request.apply_date):
            body['ApplyDate'] = request.apply_date
        if not UtilClient.is_unset(request.currency_code):
            body['CurrencyCode'] = request.currency_code
        if not UtilClient.is_unset(request.customer):
            body_flat['Customer'] = request.customer
        if not UtilClient.is_unset(request.encrypt_props):
            body_flat['EncryptProps'] = request.encrypt_props
        if not UtilClient.is_unset(request.excluding_tax_amount):
            body['ExcludingTaxAmount'] = request.excluding_tax_amount
        if not UtilClient.is_unset(request.input_type):
            body['InputType'] = request.input_type
        if not UtilClient.is_unset(request.invoice_type):
            body['InvoiceType'] = request.invoice_type
        if not UtilClient.is_unset(request.is_merged):
            body['IsMerged'] = request.is_merged
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.material_type):
            body['MaterialType'] = request.material_type
        if not UtilClient.is_unset(request.memo):
            body['Memo'] = request.memo
        if not UtilClient.is_unset(request.ou_code):
            body['OuCode'] = request.ou_code
        if not UtilClient.is_unset(request.purchaser_bank_info):
            body['PurchaserBankInfo'] = request.purchaser_bank_info
        if not UtilClient.is_unset(request.purchaser_contact_info):
            body['PurchaserContactInfo'] = request.purchaser_contact_info
        if not UtilClient.is_unset(request.purchaser_name):
            body['PurchaserName'] = request.purchaser_name
        if not UtilClient.is_unset(request.purchaser_tax_no):
            body['PurchaserTaxNo'] = request.purchaser_tax_no
        if not UtilClient.is_unset(request.request_no):
            body['RequestNo'] = request.request_no
        if not UtilClient.is_unset(request.sign):
            body['Sign'] = request.sign
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.source_list):
            body['SourceList'] = request.source_list
        if not UtilClient.is_unset(request.tax_amount):
            body['TaxAmount'] = request.tax_amount
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyArInvoiceWithSource',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ApplyArInvoiceWithSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_ar_invoice_with_source_with_options_async(
        self,
        request: dypls_20170830_models.ApplyArInvoiceWithSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.ApplyArInvoiceWithSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.address):
            body_flat['Address'] = request.address
        if not UtilClient.is_unset(request.amount):
            body['Amount'] = request.amount
        if not UtilClient.is_unset(request.app_code):
            body['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.applier):
            body['Applier'] = request.applier
        if not UtilClient.is_unset(request.apply_date):
            body['ApplyDate'] = request.apply_date
        if not UtilClient.is_unset(request.currency_code):
            body['CurrencyCode'] = request.currency_code
        if not UtilClient.is_unset(request.customer):
            body_flat['Customer'] = request.customer
        if not UtilClient.is_unset(request.encrypt_props):
            body_flat['EncryptProps'] = request.encrypt_props
        if not UtilClient.is_unset(request.excluding_tax_amount):
            body['ExcludingTaxAmount'] = request.excluding_tax_amount
        if not UtilClient.is_unset(request.input_type):
            body['InputType'] = request.input_type
        if not UtilClient.is_unset(request.invoice_type):
            body['InvoiceType'] = request.invoice_type
        if not UtilClient.is_unset(request.is_merged):
            body['IsMerged'] = request.is_merged
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.material_type):
            body['MaterialType'] = request.material_type
        if not UtilClient.is_unset(request.memo):
            body['Memo'] = request.memo
        if not UtilClient.is_unset(request.ou_code):
            body['OuCode'] = request.ou_code
        if not UtilClient.is_unset(request.purchaser_bank_info):
            body['PurchaserBankInfo'] = request.purchaser_bank_info
        if not UtilClient.is_unset(request.purchaser_contact_info):
            body['PurchaserContactInfo'] = request.purchaser_contact_info
        if not UtilClient.is_unset(request.purchaser_name):
            body['PurchaserName'] = request.purchaser_name
        if not UtilClient.is_unset(request.purchaser_tax_no):
            body['PurchaserTaxNo'] = request.purchaser_tax_no
        if not UtilClient.is_unset(request.request_no):
            body['RequestNo'] = request.request_no
        if not UtilClient.is_unset(request.sign):
            body['Sign'] = request.sign
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.source_list):
            body['SourceList'] = request.source_list
        if not UtilClient.is_unset(request.tax_amount):
            body['TaxAmount'] = request.tax_amount
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyArInvoiceWithSource',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ApplyArInvoiceWithSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_ar_invoice_with_source(
        self,
        request: dypls_20170830_models.ApplyArInvoiceWithSourceRequest,
    ) -> dypls_20170830_models.ApplyArInvoiceWithSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_ar_invoice_with_source_with_options(request, runtime)

    async def apply_ar_invoice_with_source_async(
        self,
        request: dypls_20170830_models.ApplyArInvoiceWithSourceRequest,
    ) -> dypls_20170830_models.ApplyArInvoiceWithSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_ar_invoice_with_source_with_options_async(request, runtime)

    def apply_black_info_export_with_options(
        self,
        request: dypls_20170830_models.ApplyBlackInfoExportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.ApplyBlackInfoExportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
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
            action='ApplyBlackInfoExport',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ApplyBlackInfoExportResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_black_info_export_with_options_async(
        self,
        request: dypls_20170830_models.ApplyBlackInfoExportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.ApplyBlackInfoExportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
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
            action='ApplyBlackInfoExport',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ApplyBlackInfoExportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_black_info_export(
        self,
        request: dypls_20170830_models.ApplyBlackInfoExportRequest,
    ) -> dypls_20170830_models.ApplyBlackInfoExportResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_black_info_export_with_options(request, runtime)

    async def apply_black_info_export_async(
        self,
        request: dypls_20170830_models.ApplyBlackInfoExportRequest,
    ) -> dypls_20170830_models.ApplyBlackInfoExportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_black_info_export_with_options_async(request, runtime)

    def apply_call_record_export_with_options(
        self,
        request: dypls_20170830_models.ApplyCallRecordExportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.ApplyCallRecordExportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.call_date):
            query['CallDate'] = request.call_date
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not UtilClient.is_unset(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyCallRecordExport',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ApplyCallRecordExportResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_call_record_export_with_options_async(
        self,
        request: dypls_20170830_models.ApplyCallRecordExportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.ApplyCallRecordExportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.call_date):
            query['CallDate'] = request.call_date
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not UtilClient.is_unset(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyCallRecordExport',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ApplyCallRecordExportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_call_record_export(
        self,
        request: dypls_20170830_models.ApplyCallRecordExportRequest,
    ) -> dypls_20170830_models.ApplyCallRecordExportResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_call_record_export_with_options(request, runtime)

    async def apply_call_record_export_async(
        self,
        request: dypls_20170830_models.ApplyCallRecordExportRequest,
    ) -> dypls_20170830_models.ApplyCallRecordExportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_call_record_export_with_options_async(request, runtime)

    def apply_group_number_export_with_options(
        self,
        request: dypls_20170830_models.ApplyGroupNumberExportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.ApplyGroupNumberExportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
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
            action='ApplyGroupNumberExport',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ApplyGroupNumberExportResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_group_number_export_with_options_async(
        self,
        request: dypls_20170830_models.ApplyGroupNumberExportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.ApplyGroupNumberExportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
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
            action='ApplyGroupNumberExport',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ApplyGroupNumberExportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_group_number_export(
        self,
        request: dypls_20170830_models.ApplyGroupNumberExportRequest,
    ) -> dypls_20170830_models.ApplyGroupNumberExportResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_group_number_export_with_options(request, runtime)

    async def apply_group_number_export_async(
        self,
        request: dypls_20170830_models.ApplyGroupNumberExportRequest,
    ) -> dypls_20170830_models.ApplyGroupNumberExportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_group_number_export_with_options_async(request, runtime)

    def apply_ring_tone_with_options(
        self,
        request: dypls_20170830_models.ApplyRingToneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.ApplyRingToneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_type):
            query['PlayType'] = request.play_type
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
            action='ApplyRingTone',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ApplyRingToneResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_ring_tone_with_options_async(
        self,
        request: dypls_20170830_models.ApplyRingToneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.ApplyRingToneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_type):
            query['PlayType'] = request.play_type
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
            action='ApplyRingTone',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ApplyRingToneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_ring_tone(
        self,
        request: dypls_20170830_models.ApplyRingToneRequest,
    ) -> dypls_20170830_models.ApplyRingToneResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_ring_tone_with_options(request, runtime)

    async def apply_ring_tone_async(
        self,
        request: dypls_20170830_models.ApplyRingToneRequest,
    ) -> dypls_20170830_models.ApplyRingToneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_ring_tone_with_options_async(request, runtime)

    def batch_occupy_secret_res_with_options(
        self,
        tmp_req: dypls_20170830_models.BatchOccupySecretResRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.BatchOccupySecretResResponse:
        UtilClient.validate_model(tmp_req)
        request = dypls_20170830_models.BatchOccupySecretResShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.batch_occupy_list):
            request.batch_occupy_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.batch_occupy_list, 'BatchOccupyList', 'json')
        query = {}
        if not UtilClient.is_unset(request.batch_occupy_list_shrink):
            query['BatchOccupyList'] = request.batch_occupy_list_shrink
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
            action='BatchOccupySecretRes',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.BatchOccupySecretResResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_occupy_secret_res_with_options_async(
        self,
        tmp_req: dypls_20170830_models.BatchOccupySecretResRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.BatchOccupySecretResResponse:
        UtilClient.validate_model(tmp_req)
        request = dypls_20170830_models.BatchOccupySecretResShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.batch_occupy_list):
            request.batch_occupy_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.batch_occupy_list, 'BatchOccupyList', 'json')
        query = {}
        if not UtilClient.is_unset(request.batch_occupy_list_shrink):
            query['BatchOccupyList'] = request.batch_occupy_list_shrink
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
            action='BatchOccupySecretRes',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.BatchOccupySecretResResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_occupy_secret_res(
        self,
        request: dypls_20170830_models.BatchOccupySecretResRequest,
    ) -> dypls_20170830_models.BatchOccupySecretResResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_occupy_secret_res_with_options(request, runtime)

    async def batch_occupy_secret_res_async(
        self,
        request: dypls_20170830_models.BatchOccupySecretResRequest,
    ) -> dypls_20170830_models.BatchOccupySecretResResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_occupy_secret_res_with_options_async(request, runtime)

    def bind_resource_with_options(
        self,
        request: dypls_20170830_models.BindResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.BindResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asr_model_id):
            query['AsrModelId'] = request.asr_model_id
        if not UtilClient.is_unset(request.asr_status):
            query['AsrStatus'] = request.asr_status
        if not UtilClient.is_unset(request.axn_extension_b):
            query['AxnExtensionB'] = request.axn_extension_b
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.exp_time):
            query['ExpTime'] = request.exp_time
        if not UtilClient.is_unset(request.is_record):
            query['IsRecord'] = request.is_record
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not UtilClient.is_unset(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindResource',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.BindResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_resource_with_options_async(
        self,
        request: dypls_20170830_models.BindResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.BindResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asr_model_id):
            query['AsrModelId'] = request.asr_model_id
        if not UtilClient.is_unset(request.asr_status):
            query['AsrStatus'] = request.asr_status
        if not UtilClient.is_unset(request.axn_extension_b):
            query['AxnExtensionB'] = request.axn_extension_b
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.exp_time):
            query['ExpTime'] = request.exp_time
        if not UtilClient.is_unset(request.is_record):
            query['IsRecord'] = request.is_record
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not UtilClient.is_unset(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindResource',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.BindResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_resource(
        self,
        request: dypls_20170830_models.BindResourceRequest,
    ) -> dypls_20170830_models.BindResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_resource_with_options(request, runtime)

    async def bind_resource_async(
        self,
        request: dypls_20170830_models.BindResourceRequest,
    ) -> dypls_20170830_models.BindResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_resource_with_options_async(request, runtime)

    def black_operate_with_options(
        self,
        request: dypls_20170830_models.BlackOperateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.BlackOperateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.black_map):
            query['BlackMap'] = request.black_map
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
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
            action='BlackOperate',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.BlackOperateResponse(),
            self.call_api(params, req, runtime)
        )

    async def black_operate_with_options_async(
        self,
        request: dypls_20170830_models.BlackOperateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.BlackOperateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.black_map):
            query['BlackMap'] = request.black_map
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
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
            action='BlackOperate',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.BlackOperateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def black_operate(
        self,
        request: dypls_20170830_models.BlackOperateRequest,
    ) -> dypls_20170830_models.BlackOperateResponse:
        runtime = util_models.RuntimeOptions()
        return self.black_operate_with_options(request, runtime)

    async def black_operate_async(
        self,
        request: dypls_20170830_models.BlackOperateRequest,
    ) -> dypls_20170830_models.BlackOperateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.black_operate_with_options_async(request, runtime)

    def create_certify_info_with_options(
        self,
        request: dypls_20170830_models.CreateCertifyInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreateCertifyInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no):
            query['PhoneNo'] = request.phone_no
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
            action='CreateCertifyInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateCertifyInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_certify_info_with_options_async(
        self,
        request: dypls_20170830_models.CreateCertifyInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreateCertifyInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_no):
            query['PhoneNo'] = request.phone_no
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
            action='CreateCertifyInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateCertifyInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_certify_info(
        self,
        request: dypls_20170830_models.CreateCertifyInfoRequest,
    ) -> dypls_20170830_models.CreateCertifyInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_certify_info_with_options(request, runtime)

    async def create_certify_info_async(
        self,
        request: dypls_20170830_models.CreateCertifyInfoRequest,
    ) -> dypls_20170830_models.CreateCertifyInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_certify_info_with_options_async(request, runtime)

    def create_contacts_with_options(
        self,
        request: dypls_20170830_models.CreateContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreateContactsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='CreateContacts',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateContactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_contacts_with_options_async(
        self,
        request: dypls_20170830_models.CreateContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreateContactsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='CreateContacts',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateContactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_contacts(
        self,
        request: dypls_20170830_models.CreateContactsRequest,
    ) -> dypls_20170830_models.CreateContactsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_contacts_with_options(request, runtime)

    async def create_contacts_async(
        self,
        request: dypls_20170830_models.CreateContactsRequest,
    ) -> dypls_20170830_models.CreateContactsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_contacts_with_options_async(request, runtime)

    def create_group_detail_with_options(
        self,
        request: dypls_20170830_models.CreateGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreateGroupDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
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
            action='CreateGroupDetail',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateGroupDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_group_detail_with_options_async(
        self,
        request: dypls_20170830_models.CreateGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreateGroupDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
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
            action='CreateGroupDetail',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateGroupDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_group_detail(
        self,
        request: dypls_20170830_models.CreateGroupDetailRequest,
    ) -> dypls_20170830_models.CreateGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_group_detail_with_options(request, runtime)

    async def create_group_detail_async(
        self,
        request: dypls_20170830_models.CreateGroupDetailRequest,
    ) -> dypls_20170830_models.CreateGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_group_detail_with_options_async(request, runtime)

    def create_group_info_with_options(
        self,
        request: dypls_20170830_models.CreateGroupInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreateGroupInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
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
            action='CreateGroupInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateGroupInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_group_info_with_options_async(
        self,
        request: dypls_20170830_models.CreateGroupInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreateGroupInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
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
            action='CreateGroupInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateGroupInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_group_info(
        self,
        request: dypls_20170830_models.CreateGroupInfoRequest,
    ) -> dypls_20170830_models.CreateGroupInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_group_info_with_options(request, runtime)

    async def create_group_info_async(
        self,
        request: dypls_20170830_models.CreateGroupInfoRequest,
    ) -> dypls_20170830_models.CreateGroupInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_group_info_with_options_async(request, runtime)

    def create_logical_delete_with_options(
        self,
        request: dypls_20170830_models.CreateLogicalDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreateLogicalDeleteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.gmt_wakeup):
            query['GmtWakeup'] = request.gmt_wakeup
        if not UtilClient.is_unset(request.hid):
            query['Hid'] = request.hid
        if not UtilClient.is_unset(request.interrupt):
            query['Interrupt'] = request.interrupt
        if not UtilClient.is_unset(request.invoker):
            query['Invoker'] = request.invoker
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.success):
            query['Success'] = request.success
        if not UtilClient.is_unset(request.task_extra_data):
            query['TaskExtraData'] = request.task_extra_data
        if not UtilClient.is_unset(request.task_identifier):
            query['TaskIdentifier'] = request.task_identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLogicalDelete',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateLogicalDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_logical_delete_with_options_async(
        self,
        request: dypls_20170830_models.CreateLogicalDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreateLogicalDeleteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.gmt_wakeup):
            query['GmtWakeup'] = request.gmt_wakeup
        if not UtilClient.is_unset(request.hid):
            query['Hid'] = request.hid
        if not UtilClient.is_unset(request.interrupt):
            query['Interrupt'] = request.interrupt
        if not UtilClient.is_unset(request.invoker):
            query['Invoker'] = request.invoker
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.success):
            query['Success'] = request.success
        if not UtilClient.is_unset(request.task_extra_data):
            query['TaskExtraData'] = request.task_extra_data
        if not UtilClient.is_unset(request.task_identifier):
            query['TaskIdentifier'] = request.task_identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLogicalDelete',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateLogicalDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_logical_delete(
        self,
        request: dypls_20170830_models.CreateLogicalDeleteRequest,
    ) -> dypls_20170830_models.CreateLogicalDeleteResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_logical_delete_with_options(request, runtime)

    async def create_logical_delete_async(
        self,
        request: dypls_20170830_models.CreateLogicalDeleteRequest,
    ) -> dypls_20170830_models.CreateLogicalDeleteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_logical_delete_with_options_async(request, runtime)

    def create_message_callback_with_options(
        self,
        request: dypls_20170830_models.CreateMessageCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreateMessageCallbackResponse:
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
            action='CreateMessageCallback',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateMessageCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_message_callback_with_options_async(
        self,
        request: dypls_20170830_models.CreateMessageCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreateMessageCallbackResponse:
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
            action='CreateMessageCallback',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateMessageCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_message_callback(
        self,
        request: dypls_20170830_models.CreateMessageCallbackRequest,
    ) -> dypls_20170830_models.CreateMessageCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_message_callback_with_options(request, runtime)

    async def create_message_callback_async(
        self,
        request: dypls_20170830_models.CreateMessageCallbackRequest,
    ) -> dypls_20170830_models.CreateMessageCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_message_callback_with_options_async(request, runtime)

    def create_message_queue_with_options(
        self,
        request: dypls_20170830_models.CreateMessageQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreateMessageQueueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_ids):
            query['BillIds'] = request.bill_ids
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.queue_title):
            query['QueueTitle'] = request.queue_title
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMessageQueue',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateMessageQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_message_queue_with_options_async(
        self,
        request: dypls_20170830_models.CreateMessageQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreateMessageQueueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_ids):
            query['BillIds'] = request.bill_ids
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.queue_title):
            query['QueueTitle'] = request.queue_title
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMessageQueue',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateMessageQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_message_queue(
        self,
        request: dypls_20170830_models.CreateMessageQueueRequest,
    ) -> dypls_20170830_models.CreateMessageQueueResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_message_queue_with_options(request, runtime)

    async def create_message_queue_async(
        self,
        request: dypls_20170830_models.CreateMessageQueueRequest,
    ) -> dypls_20170830_models.CreateMessageQueueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_message_queue_with_options_async(request, runtime)

    def create_physical_delete_with_options(
        self,
        request: dypls_20170830_models.CreatePhysicalDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreatePhysicalDeleteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.gmt_wakeup):
            query['GmtWakeup'] = request.gmt_wakeup
        if not UtilClient.is_unset(request.hid):
            query['Hid'] = request.hid
        if not UtilClient.is_unset(request.interrupt):
            query['Interrupt'] = request.interrupt
        if not UtilClient.is_unset(request.invoker):
            query['Invoker'] = request.invoker
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.success):
            query['Success'] = request.success
        if not UtilClient.is_unset(request.task_extra_data):
            query['TaskExtraData'] = request.task_extra_data
        if not UtilClient.is_unset(request.task_identifier):
            query['TaskIdentifier'] = request.task_identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePhysicalDelete',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreatePhysicalDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_physical_delete_with_options_async(
        self,
        request: dypls_20170830_models.CreatePhysicalDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreatePhysicalDeleteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.gmt_wakeup):
            query['GmtWakeup'] = request.gmt_wakeup
        if not UtilClient.is_unset(request.hid):
            query['Hid'] = request.hid
        if not UtilClient.is_unset(request.interrupt):
            query['Interrupt'] = request.interrupt
        if not UtilClient.is_unset(request.invoker):
            query['Invoker'] = request.invoker
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.success):
            query['Success'] = request.success
        if not UtilClient.is_unset(request.task_extra_data):
            query['TaskExtraData'] = request.task_extra_data
        if not UtilClient.is_unset(request.task_identifier):
            query['TaskIdentifier'] = request.task_identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePhysicalDelete',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreatePhysicalDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_physical_delete(
        self,
        request: dypls_20170830_models.CreatePhysicalDeleteRequest,
    ) -> dypls_20170830_models.CreatePhysicalDeleteResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_physical_delete_with_options(request, runtime)

    async def create_physical_delete_async(
        self,
        request: dypls_20170830_models.CreatePhysicalDeleteRequest,
    ) -> dypls_20170830_models.CreatePhysicalDeleteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_physical_delete_with_options_async(request, runtime)

    def create_pool_info_with_options(
        self,
        request: dypls_20170830_models.CreatePoolInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreatePoolInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePoolInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreatePoolInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pool_info_with_options_async(
        self,
        request: dypls_20170830_models.CreatePoolInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreatePoolInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePoolInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreatePoolInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pool_info(
        self,
        request: dypls_20170830_models.CreatePoolInfoRequest,
    ) -> dypls_20170830_models.CreatePoolInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_pool_info_with_options(request, runtime)

    async def create_pool_info_async(
        self,
        request: dypls_20170830_models.CreatePoolInfoRequest,
    ) -> dypls_20170830_models.CreatePoolInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_pool_info_with_options_async(request, runtime)

    def create_product_with_options(
        self,
        request: dypls_20170830_models.CreateProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreateProductResponse:
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
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_product_with_options_async(
        self,
        request: dypls_20170830_models.CreateProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreateProductResponse:
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
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_product(
        self,
        request: dypls_20170830_models.CreateProductRequest,
    ) -> dypls_20170830_models.CreateProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_product_with_options(request, runtime)

    async def create_product_async(
        self,
        request: dypls_20170830_models.CreateProductRequest,
    ) -> dypls_20170830_models.CreateProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_product_with_options_async(request, runtime)

    def create_ring_tone_with_options(
        self,
        request: dypls_20170830_models.CreateRingToneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreateRingToneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.file_key):
            query['FileKey'] = request.file_key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_type):
            query['PlayType'] = request.play_type
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.ring_name):
            query['RingName'] = request.ring_name
        if not UtilClient.is_unset(request.tts):
            query['Tts'] = request.tts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRingTone',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateRingToneResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ring_tone_with_options_async(
        self,
        request: dypls_20170830_models.CreateRingToneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreateRingToneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.file_key):
            query['FileKey'] = request.file_key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_type):
            query['PlayType'] = request.play_type
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.ring_name):
            query['RingName'] = request.ring_name
        if not UtilClient.is_unset(request.tts):
            query['Tts'] = request.tts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRingTone',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateRingToneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ring_tone(
        self,
        request: dypls_20170830_models.CreateRingToneRequest,
    ) -> dypls_20170830_models.CreateRingToneResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ring_tone_with_options(request, runtime)

    async def create_ring_tone_async(
        self,
        request: dypls_20170830_models.CreateRingToneRequest,
    ) -> dypls_20170830_models.CreateRingToneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ring_tone_with_options_async(request, runtime)

    def create_subs_trial_with_options(
        self,
        request: dypls_20170830_models.CreateSubsTrialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreateSubsTrialResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_a):
            query['PhoneA'] = request.phone_a
        if not UtilClient.is_unset(request.phone_b):
            query['PhoneB'] = request.phone_b
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSubsTrial',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateSubsTrialResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_subs_trial_with_options_async(
        self,
        request: dypls_20170830_models.CreateSubsTrialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreateSubsTrialResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phone_a):
            query['PhoneA'] = request.phone_a
        if not UtilClient.is_unset(request.phone_b):
            query['PhoneB'] = request.phone_b
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSubsTrial',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateSubsTrialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_subs_trial(
        self,
        request: dypls_20170830_models.CreateSubsTrialRequest,
    ) -> dypls_20170830_models.CreateSubsTrialResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_subs_trial_with_options(request, runtime)

    async def create_subs_trial_async(
        self,
        request: dypls_20170830_models.CreateSubsTrialRequest,
    ) -> dypls_20170830_models.CreateSubsTrialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_subs_trial_with_options_async(request, runtime)

    def create_transfer_record_with_options(
        self,
        request: dypls_20170830_models.CreateTransferRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreateTransferRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        if not UtilClient.is_unset(request.origin_bill_id):
            query['OriginBillId'] = request.origin_bill_id
        if not UtilClient.is_unset(request.origin_name):
            query['OriginName'] = request.origin_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target_bill_id):
            query['TargetBillId'] = request.target_bill_id
        if not UtilClient.is_unset(request.target_name):
            query['TargetName'] = request.target_name
        if not UtilClient.is_unset(request.total):
            query['Total'] = request.total
        if not UtilClient.is_unset(request.transfer_type):
            query['TransferType'] = request.transfer_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransferRecord',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateTransferRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transfer_record_with_options_async(
        self,
        request: dypls_20170830_models.CreateTransferRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.CreateTransferRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.number_list):
            query['NumberList'] = request.number_list
        if not UtilClient.is_unset(request.origin_bill_id):
            query['OriginBillId'] = request.origin_bill_id
        if not UtilClient.is_unset(request.origin_name):
            query['OriginName'] = request.origin_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target_bill_id):
            query['TargetBillId'] = request.target_bill_id
        if not UtilClient.is_unset(request.target_name):
            query['TargetName'] = request.target_name
        if not UtilClient.is_unset(request.total):
            query['Total'] = request.total
        if not UtilClient.is_unset(request.transfer_type):
            query['TransferType'] = request.transfer_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransferRecord',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.CreateTransferRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transfer_record(
        self,
        request: dypls_20170830_models.CreateTransferRecordRequest,
    ) -> dypls_20170830_models.CreateTransferRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_transfer_record_with_options(request, runtime)

    async def create_transfer_record_async(
        self,
        request: dypls_20170830_models.CreateTransferRecordRequest,
    ) -> dypls_20170830_models.CreateTransferRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_transfer_record_with_options_async(request, runtime)

    def delete_certify_info_with_options(
        self,
        request: dypls_20170830_models.DeleteCertifyInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.DeleteCertifyInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certify_id):
            query['CertifyId'] = request.certify_id
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
            action='DeleteCertifyInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.DeleteCertifyInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_certify_info_with_options_async(
        self,
        request: dypls_20170830_models.DeleteCertifyInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.DeleteCertifyInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certify_id):
            query['CertifyId'] = request.certify_id
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
            action='DeleteCertifyInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.DeleteCertifyInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_certify_info(
        self,
        request: dypls_20170830_models.DeleteCertifyInfoRequest,
    ) -> dypls_20170830_models.DeleteCertifyInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_certify_info_with_options(request, runtime)

    async def delete_certify_info_async(
        self,
        request: dypls_20170830_models.DeleteCertifyInfoRequest,
    ) -> dypls_20170830_models.DeleteCertifyInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_certify_info_with_options_async(request, runtime)

    def delete_contacts_with_options(
        self,
        request: dypls_20170830_models.DeleteContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.DeleteContactsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContacts',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.DeleteContactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contacts_with_options_async(
        self,
        request: dypls_20170830_models.DeleteContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.DeleteContactsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContacts',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.DeleteContactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contacts(
        self,
        request: dypls_20170830_models.DeleteContactsRequest,
    ) -> dypls_20170830_models.DeleteContactsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_contacts_with_options(request, runtime)

    async def delete_contacts_async(
        self,
        request: dypls_20170830_models.DeleteContactsRequest,
    ) -> dypls_20170830_models.DeleteContactsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_contacts_with_options_async(request, runtime)

    def delete_group_detail_with_options(
        self,
        request: dypls_20170830_models.DeleteGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.DeleteGroupDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id_list):
            query['IdList'] = request.id_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
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
            action='DeleteGroupDetail',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.DeleteGroupDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_group_detail_with_options_async(
        self,
        request: dypls_20170830_models.DeleteGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.DeleteGroupDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id_list):
            query['IdList'] = request.id_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
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
            action='DeleteGroupDetail',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.DeleteGroupDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_group_detail(
        self,
        request: dypls_20170830_models.DeleteGroupDetailRequest,
    ) -> dypls_20170830_models.DeleteGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_group_detail_with_options(request, runtime)

    async def delete_group_detail_async(
        self,
        request: dypls_20170830_models.DeleteGroupDetailRequest,
    ) -> dypls_20170830_models.DeleteGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_group_detail_with_options_async(request, runtime)

    def delete_message_callback_with_options(
        self,
        request: dypls_20170830_models.DeleteMessageCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.DeleteMessageCallbackResponse:
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
            action='DeleteMessageCallback',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.DeleteMessageCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_message_callback_with_options_async(
        self,
        request: dypls_20170830_models.DeleteMessageCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.DeleteMessageCallbackResponse:
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
            action='DeleteMessageCallback',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.DeleteMessageCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_message_callback(
        self,
        request: dypls_20170830_models.DeleteMessageCallbackRequest,
    ) -> dypls_20170830_models.DeleteMessageCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_message_callback_with_options(request, runtime)

    async def delete_message_callback_async(
        self,
        request: dypls_20170830_models.DeleteMessageCallbackRequest,
    ) -> dypls_20170830_models.DeleteMessageCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_message_callback_with_options_async(request, runtime)

    def delete_ring_tone_with_options(
        self,
        request: dypls_20170830_models.DeleteRingToneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.DeleteRingToneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRingTone',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.DeleteRingToneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ring_tone_with_options_async(
        self,
        request: dypls_20170830_models.DeleteRingToneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.DeleteRingToneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRingTone',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.DeleteRingToneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ring_tone(
        self,
        request: dypls_20170830_models.DeleteRingToneRequest,
    ) -> dypls_20170830_models.DeleteRingToneResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ring_tone_with_options(request, runtime)

    async def delete_ring_tone_async(
        self,
        request: dypls_20170830_models.DeleteRingToneRequest,
    ) -> dypls_20170830_models.DeleteRingToneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ring_tone_with_options_async(request, runtime)

    def download_complete_with_options(
        self,
        request: dypls_20170830_models.DownloadCompleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.DownloadCompleteResponse:
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
            action='DownloadComplete',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.DownloadCompleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_complete_with_options_async(
        self,
        request: dypls_20170830_models.DownloadCompleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.DownloadCompleteResponse:
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
            action='DownloadComplete',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.DownloadCompleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_complete(
        self,
        request: dypls_20170830_models.DownloadCompleteRequest,
    ) -> dypls_20170830_models.DownloadCompleteResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_complete_with_options(request, runtime)

    async def download_complete_async(
        self,
        request: dypls_20170830_models.DownloadCompleteRequest,
    ) -> dypls_20170830_models.DownloadCompleteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_complete_with_options_async(request, runtime)

    def export_res_with_options(
        self,
        request: dypls_20170830_models.ExportResRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.ExportResResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_bind_status):
            query['ResBindStatus'] = request.res_bind_status
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportRes',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ExportResResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_res_with_options_async(
        self,
        request: dypls_20170830_models.ExportResRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.ExportResResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_bind_status):
            query['ResBindStatus'] = request.res_bind_status
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportRes',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ExportResResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_res(
        self,
        request: dypls_20170830_models.ExportResRequest,
    ) -> dypls_20170830_models.ExportResResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_res_with_options(request, runtime)

    async def export_res_async(
        self,
        request: dypls_20170830_models.ExportResRequest,
    ) -> dypls_20170830_models.ExportResResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_res_with_options_async(request, runtime)

    def get_einvoice_pdf_data_with_options(
        self,
        request: dypls_20170830_models.GetEinvoicePdfDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.GetEinvoicePdfDataResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_code):
            body['AppCode'] = request.app_code
        body_flat = {}
        if not UtilClient.is_unset(request.customer):
            body_flat['Customer'] = request.customer
        if not UtilClient.is_unset(request.encrypt_props):
            body_flat['EncryptProps'] = request.encrypt_props
        if not UtilClient.is_unset(request.invoice_code):
            body['InvoiceCode'] = request.invoice_code
        if not UtilClient.is_unset(request.invoice_no):
            body['InvoiceNo'] = request.invoice_no
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.sign):
            body['Sign'] = request.sign
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEinvoicePdfData',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.GetEinvoicePdfDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_einvoice_pdf_data_with_options_async(
        self,
        request: dypls_20170830_models.GetEinvoicePdfDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.GetEinvoicePdfDataResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_code):
            body['AppCode'] = request.app_code
        body_flat = {}
        if not UtilClient.is_unset(request.customer):
            body_flat['Customer'] = request.customer
        if not UtilClient.is_unset(request.encrypt_props):
            body_flat['EncryptProps'] = request.encrypt_props
        if not UtilClient.is_unset(request.invoice_code):
            body['InvoiceCode'] = request.invoice_code
        if not UtilClient.is_unset(request.invoice_no):
            body['InvoiceNo'] = request.invoice_no
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.sign):
            body['Sign'] = request.sign
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEinvoicePdfData',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.GetEinvoicePdfDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_einvoice_pdf_data(
        self,
        request: dypls_20170830_models.GetEinvoicePdfDataRequest,
    ) -> dypls_20170830_models.GetEinvoicePdfDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_einvoice_pdf_data_with_options(request, runtime)

    async def get_einvoice_pdf_data_async(
        self,
        request: dypls_20170830_models.GetEinvoicePdfDataRequest,
    ) -> dypls_20170830_models.GetEinvoicePdfDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_einvoice_pdf_data_with_options_async(request, runtime)

    def get_secret_asr_info_with_options(
        self,
        request: dypls_20170830_models.GetSecretAsrInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.GetSecretAsrInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.call_time):
            query['CallTime'] = request.call_time
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSecretAsrInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.GetSecretAsrInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_secret_asr_info_with_options_async(
        self,
        request: dypls_20170830_models.GetSecretAsrInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.GetSecretAsrInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.call_time):
            query['CallTime'] = request.call_time
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSecretAsrInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.GetSecretAsrInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_secret_asr_info(
        self,
        request: dypls_20170830_models.GetSecretAsrInfoRequest,
    ) -> dypls_20170830_models.GetSecretAsrInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_secret_asr_info_with_options(request, runtime)

    async def get_secret_asr_info_async(
        self,
        request: dypls_20170830_models.GetSecretAsrInfoRequest,
    ) -> dypls_20170830_models.GetSecretAsrInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_secret_asr_info_with_options_async(request, runtime)

    def get_user_resource_tag_status_with_options(
        self,
        request: dypls_20170830_models.GetUserResourceTagStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.GetUserResourceTagStatusResponse:
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
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserResourceTagStatus',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.GetUserResourceTagStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_resource_tag_status_with_options_async(
        self,
        request: dypls_20170830_models.GetUserResourceTagStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.GetUserResourceTagStatusResponse:
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
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserResourceTagStatus',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.GetUserResourceTagStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_resource_tag_status(
        self,
        request: dypls_20170830_models.GetUserResourceTagStatusRequest,
    ) -> dypls_20170830_models.GetUserResourceTagStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_resource_tag_status_with_options(request, runtime)

    async def get_user_resource_tag_status_async(
        self,
        request: dypls_20170830_models.GetUserResourceTagStatusRequest,
    ) -> dypls_20170830_models.GetUserResourceTagStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_resource_tag_status_with_options_async(request, runtime)

    def list_asr_language_models_with_options(
        self,
        request: dypls_20170830_models.ListAsrLanguageModelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.ListAsrLanguageModelsResponse:
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
            action='ListAsrLanguageModels',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ListAsrLanguageModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_asr_language_models_with_options_async(
        self,
        request: dypls_20170830_models.ListAsrLanguageModelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.ListAsrLanguageModelsResponse:
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
            action='ListAsrLanguageModels',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ListAsrLanguageModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_asr_language_models(
        self,
        request: dypls_20170830_models.ListAsrLanguageModelsRequest,
    ) -> dypls_20170830_models.ListAsrLanguageModelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_asr_language_models_with_options(request, runtime)

    async def list_asr_language_models_async(
        self,
        request: dypls_20170830_models.ListAsrLanguageModelsRequest,
    ) -> dypls_20170830_models.ListAsrLanguageModelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_asr_language_models_with_options_async(request, runtime)

    def lock_resource_with_options(
        self,
        request: dypls_20170830_models.LockResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.LockResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LockResource',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.LockResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def lock_resource_with_options_async(
        self,
        request: dypls_20170830_models.LockResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.LockResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LockResource',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.LockResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lock_resource(
        self,
        request: dypls_20170830_models.LockResourceRequest,
    ) -> dypls_20170830_models.LockResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.lock_resource_with_options(request, runtime)

    async def lock_resource_async(
        self,
        request: dypls_20170830_models.LockResourceRequest,
    ) -> dypls_20170830_models.LockResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.lock_resource_with_options_async(request, runtime)

    def occupy_secret_res_with_options(
        self,
        request: dypls_20170830_models.OccupySecretResRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.OccupySecretResResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.is_display_pool):
            query['IsDisplayPool'] = request.is_display_pool
        if not UtilClient.is_unset(request.no_like):
            query['NoLike'] = request.no_like
        if not UtilClient.is_unset(request.order_detail_id):
            query['OrderDetailId'] = request.order_detail_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.partner_key):
            query['PartnerKey'] = request.partner_key
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no_type):
            query['SecretNoType'] = request.secret_no_type
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        if not UtilClient.is_unset(request.secret_no):
            query['secretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OccupySecretRes',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.OccupySecretResResponse(),
            self.call_api(params, req, runtime)
        )

    async def occupy_secret_res_with_options_async(
        self,
        request: dypls_20170830_models.OccupySecretResRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.OccupySecretResResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.is_display_pool):
            query['IsDisplayPool'] = request.is_display_pool
        if not UtilClient.is_unset(request.no_like):
            query['NoLike'] = request.no_like
        if not UtilClient.is_unset(request.order_detail_id):
            query['OrderDetailId'] = request.order_detail_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.partner_key):
            query['PartnerKey'] = request.partner_key
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no_type):
            query['SecretNoType'] = request.secret_no_type
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        if not UtilClient.is_unset(request.secret_no):
            query['secretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OccupySecretRes',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.OccupySecretResResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def occupy_secret_res(
        self,
        request: dypls_20170830_models.OccupySecretResRequest,
    ) -> dypls_20170830_models.OccupySecretResResponse:
        runtime = util_models.RuntimeOptions()
        return self.occupy_secret_res_with_options(request, runtime)

    async def occupy_secret_res_async(
        self,
        request: dypls_20170830_models.OccupySecretResRequest,
    ) -> dypls_20170830_models.OccupySecretResResponse:
        runtime = util_models.RuntimeOptions()
        return await self.occupy_secret_res_with_options_async(request, runtime)

    def order_succeeded_callback_with_options(
        self,
        request: dypls_20170830_models.OrderSucceededCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.OrderSucceededCallbackResponse:
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
            action='OrderSucceededCallback',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.OrderSucceededCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def order_succeeded_callback_with_options_async(
        self,
        request: dypls_20170830_models.OrderSucceededCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.OrderSucceededCallbackResponse:
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
            action='OrderSucceededCallback',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.OrderSucceededCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def order_succeeded_callback(
        self,
        request: dypls_20170830_models.OrderSucceededCallbackRequest,
    ) -> dypls_20170830_models.OrderSucceededCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.order_succeeded_callback_with_options(request, runtime)

    async def order_succeeded_callback_async(
        self,
        request: dypls_20170830_models.OrderSucceededCallbackRequest,
    ) -> dypls_20170830_models.OrderSucceededCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.order_succeeded_callback_with_options_async(request, runtime)

    def pool_config_with_options(
        self,
        request: dypls_20170830_models.PoolConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.PoolConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.callback_type):
            query['CallbackType'] = request.callback_type
        if not UtilClient.is_unset(request.frozen_day):
            query['FrozenDay'] = request.frozen_day
        if not UtilClient.is_unset(request.need_all_call_records):
            query['NeedAllCallRecords'] = request.need_all_call_records
        if not UtilClient.is_unset(request.open_sms_white):
            query['OpenSmsWhite'] = request.open_sms_white
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_warning_limit):
            query['PoolWarningLimit'] = request.pool_warning_limit
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.select_xmode):
            query['SelectXMode'] = request.select_xmode
        if not UtilClient.is_unset(request.smart_sms_whitelist):
            query['SmartSmsWhitelist'] = request.smart_sms_whitelist
        if not UtilClient.is_unset(request.sms_channel):
            query['SmsChannel'] = request.sms_channel
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PoolConfig',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.PoolConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def pool_config_with_options_async(
        self,
        request: dypls_20170830_models.PoolConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.PoolConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.callback_type):
            query['CallbackType'] = request.callback_type
        if not UtilClient.is_unset(request.frozen_day):
            query['FrozenDay'] = request.frozen_day
        if not UtilClient.is_unset(request.need_all_call_records):
            query['NeedAllCallRecords'] = request.need_all_call_records
        if not UtilClient.is_unset(request.open_sms_white):
            query['OpenSmsWhite'] = request.open_sms_white
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_warning_limit):
            query['PoolWarningLimit'] = request.pool_warning_limit
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.select_xmode):
            query['SelectXMode'] = request.select_xmode
        if not UtilClient.is_unset(request.smart_sms_whitelist):
            query['SmartSmsWhitelist'] = request.smart_sms_whitelist
        if not UtilClient.is_unset(request.sms_channel):
            query['SmsChannel'] = request.sms_channel
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PoolConfig',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.PoolConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pool_config(
        self,
        request: dypls_20170830_models.PoolConfigRequest,
    ) -> dypls_20170830_models.PoolConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.pool_config_with_options(request, runtime)

    async def pool_config_async(
        self,
        request: dypls_20170830_models.PoolConfigRequest,
    ) -> dypls_20170830_models.PoolConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pool_config_with_options_async(request, runtime)

    def purchase_resources_with_options(
        self,
        request: dypls_20170830_models.PurchaseResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.PurchaseResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.buy_number):
            query['BuyNumber'] = request.buy_number
        if not UtilClient.is_unset(request.is_display_pool):
            query['IsDisplayPool'] = request.is_display_pool
        if not UtilClient.is_unset(request.no_like):
            query['NoLike'] = request.no_like
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.region_name):
            query['RegionName'] = request.region_name
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.spec_id):
            query['SpecId'] = request.spec_id
        if not UtilClient.is_unset(request.usage_scenarios):
            query['UsageScenarios'] = request.usage_scenarios
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PurchaseResources',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.PurchaseResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def purchase_resources_with_options_async(
        self,
        request: dypls_20170830_models.PurchaseResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.PurchaseResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.buy_number):
            query['BuyNumber'] = request.buy_number
        if not UtilClient.is_unset(request.is_display_pool):
            query['IsDisplayPool'] = request.is_display_pool
        if not UtilClient.is_unset(request.no_like):
            query['NoLike'] = request.no_like
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.region_name):
            query['RegionName'] = request.region_name
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.spec_id):
            query['SpecId'] = request.spec_id
        if not UtilClient.is_unset(request.usage_scenarios):
            query['UsageScenarios'] = request.usage_scenarios
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PurchaseResources',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.PurchaseResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def purchase_resources(
        self,
        request: dypls_20170830_models.PurchaseResourcesRequest,
    ) -> dypls_20170830_models.PurchaseResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.purchase_resources_with_options(request, runtime)

    async def purchase_resources_async(
        self,
        request: dypls_20170830_models.PurchaseResourcesRequest,
    ) -> dypls_20170830_models.PurchaseResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.purchase_resources_with_options_async(request, runtime)

    def query_binding_details_with_options(
        self,
        request: dypls_20170830_models.QueryBindingDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryBindingDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not UtilClient.is_unset(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        if not UtilClient.is_unset(request.sub_id):
            query['SubId'] = request.sub_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBindingDetails',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryBindingDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_binding_details_with_options_async(
        self,
        request: dypls_20170830_models.QueryBindingDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryBindingDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not UtilClient.is_unset(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        if not UtilClient.is_unset(request.sub_id):
            query['SubId'] = request.sub_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBindingDetails',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryBindingDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_binding_details(
        self,
        request: dypls_20170830_models.QueryBindingDetailsRequest,
    ) -> dypls_20170830_models.QueryBindingDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_binding_details_with_options(request, runtime)

    async def query_binding_details_async(
        self,
        request: dypls_20170830_models.QueryBindingDetailsRequest,
    ) -> dypls_20170830_models.QueryBindingDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_binding_details_with_options_async(request, runtime)

    def query_black_list_with_options(
        self,
        request: dypls_20170830_models.QueryBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryBlackListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.black_prefix):
            query['BlackPrefix'] = request.black_prefix
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
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
            action='QueryBlackList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_black_list_with_options_async(
        self,
        request: dypls_20170830_models.QueryBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryBlackListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.black_prefix):
            query['BlackPrefix'] = request.black_prefix
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
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
            action='QueryBlackList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryBlackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_black_list(
        self,
        request: dypls_20170830_models.QueryBlackListRequest,
    ) -> dypls_20170830_models.QueryBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_black_list_with_options(request, runtime)

    async def query_black_list_async(
        self,
        request: dypls_20170830_models.QueryBlackListRequest,
    ) -> dypls_20170830_models.QueryBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_black_list_with_options_async(request, runtime)

    def query_buy_page_init_data_with_options(
        self,
        request: dypls_20170830_models.QueryBuyPageInitDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryBuyPageInitDataResponse:
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
            action='QueryBuyPageInitData',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryBuyPageInitDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_buy_page_init_data_with_options_async(
        self,
        request: dypls_20170830_models.QueryBuyPageInitDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryBuyPageInitDataResponse:
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
            action='QueryBuyPageInitData',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryBuyPageInitDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_buy_page_init_data(
        self,
        request: dypls_20170830_models.QueryBuyPageInitDataRequest,
    ) -> dypls_20170830_models.QueryBuyPageInitDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_buy_page_init_data_with_options(request, runtime)

    async def query_buy_page_init_data_async(
        self,
        request: dypls_20170830_models.QueryBuyPageInitDataRequest,
    ) -> dypls_20170830_models.QueryBuyPageInitDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_buy_page_init_data_with_options_async(request, runtime)

    def query_buy_page_res_count_with_options(
        self,
        request: dypls_20170830_models.QueryBuyPageResCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryBuyPageResCountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.like):
            query['Like'] = request.like
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.spec_id):
            query['SpecId'] = request.spec_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBuyPageResCount',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryBuyPageResCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_buy_page_res_count_with_options_async(
        self,
        request: dypls_20170830_models.QueryBuyPageResCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryBuyPageResCountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.like):
            query['Like'] = request.like
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.spec_id):
            query['SpecId'] = request.spec_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBuyPageResCount',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryBuyPageResCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_buy_page_res_count(
        self,
        request: dypls_20170830_models.QueryBuyPageResCountRequest,
    ) -> dypls_20170830_models.QueryBuyPageResCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_buy_page_res_count_with_options(request, runtime)

    async def query_buy_page_res_count_async(
        self,
        request: dypls_20170830_models.QueryBuyPageResCountRequest,
    ) -> dypls_20170830_models.QueryBuyPageResCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_buy_page_res_count_with_options_async(request, runtime)

    def query_buy_page_res_info_with_options(
        self,
        request: dypls_20170830_models.QueryBuyPageResInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryBuyPageResInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.like):
            query['Like'] = request.like
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.spec_id):
            query['SpecId'] = request.spec_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBuyPageResInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryBuyPageResInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_buy_page_res_info_with_options_async(
        self,
        request: dypls_20170830_models.QueryBuyPageResInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryBuyPageResInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.like):
            query['Like'] = request.like
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.spec_id):
            query['SpecId'] = request.spec_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBuyPageResInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryBuyPageResInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_buy_page_res_info(
        self,
        request: dypls_20170830_models.QueryBuyPageResInfoRequest,
    ) -> dypls_20170830_models.QueryBuyPageResInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_buy_page_res_info_with_options(request, runtime)

    async def query_buy_page_res_info_async(
        self,
        request: dypls_20170830_models.QueryBuyPageResInfoRequest,
    ) -> dypls_20170830_models.QueryBuyPageResInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_buy_page_res_info_with_options_async(request, runtime)

    def query_buy_res_info_with_options(
        self,
        request: dypls_20170830_models.QueryBuyResInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryBuyResInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.like):
            query['Like'] = request.like
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.spec_id):
            query['SpecId'] = request.spec_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBuyResInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryBuyResInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_buy_res_info_with_options_async(
        self,
        request: dypls_20170830_models.QueryBuyResInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryBuyResInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.like):
            query['Like'] = request.like
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.spec_id):
            query['SpecId'] = request.spec_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBuyResInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryBuyResInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_buy_res_info(
        self,
        request: dypls_20170830_models.QueryBuyResInfoRequest,
    ) -> dypls_20170830_models.QueryBuyResInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_buy_res_info_with_options(request, runtime)

    async def query_buy_res_info_async(
        self,
        request: dypls_20170830_models.QueryBuyResInfoRequest,
    ) -> dypls_20170830_models.QueryBuyResInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_buy_res_info_with_options_async(request, runtime)

    def query_call_recording_list_with_options(
        self,
        request: dypls_20170830_models.QueryCallRecordingListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryCallRecordingListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.call_date):
            query['CallDate'] = request.call_date
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not UtilClient.is_unset(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCallRecordingList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryCallRecordingListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_call_recording_list_with_options_async(
        self,
        request: dypls_20170830_models.QueryCallRecordingListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryCallRecordingListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.call_date):
            query['CallDate'] = request.call_date
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_no_a):
            query['PhoneNoA'] = request.phone_no_a
        if not UtilClient.is_unset(request.phone_no_b):
            query['PhoneNoB'] = request.phone_no_b
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCallRecordingList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryCallRecordingListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_call_recording_list(
        self,
        request: dypls_20170830_models.QueryCallRecordingListRequest,
    ) -> dypls_20170830_models.QueryCallRecordingListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_call_recording_list_with_options(request, runtime)

    async def query_call_recording_list_async(
        self,
        request: dypls_20170830_models.QueryCallRecordingListRequest,
    ) -> dypls_20170830_models.QueryCallRecordingListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_call_recording_list_with_options_async(request, runtime)

    def query_certify_info_list_with_options(
        self,
        request: dypls_20170830_models.QueryCertifyInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryCertifyInfoListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certify_status):
            query['CertifyStatus'] = request.certify_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_no):
            query['PhoneNo'] = request.phone_no
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
            action='QueryCertifyInfoList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryCertifyInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_certify_info_list_with_options_async(
        self,
        request: dypls_20170830_models.QueryCertifyInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryCertifyInfoListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certify_status):
            query['CertifyStatus'] = request.certify_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_no):
            query['PhoneNo'] = request.phone_no
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
            action='QueryCertifyInfoList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryCertifyInfoListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_certify_info_list(
        self,
        request: dypls_20170830_models.QueryCertifyInfoListRequest,
    ) -> dypls_20170830_models.QueryCertifyInfoListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_certify_info_list_with_options(request, runtime)

    async def query_certify_info_list_async(
        self,
        request: dypls_20170830_models.QueryCertifyInfoListRequest,
    ) -> dypls_20170830_models.QueryCertifyInfoListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_certify_info_list_with_options_async(request, runtime)

    def query_certify_overview_info_with_options(
        self,
        request: dypls_20170830_models.QueryCertifyOverviewInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryCertifyOverviewInfoResponse:
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
            action='QueryCertifyOverviewInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryCertifyOverviewInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_certify_overview_info_with_options_async(
        self,
        request: dypls_20170830_models.QueryCertifyOverviewInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryCertifyOverviewInfoResponse:
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
            action='QueryCertifyOverviewInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryCertifyOverviewInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_certify_overview_info(
        self,
        request: dypls_20170830_models.QueryCertifyOverviewInfoRequest,
    ) -> dypls_20170830_models.QueryCertifyOverviewInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_certify_overview_info_with_options(request, runtime)

    async def query_certify_overview_info_async(
        self,
        request: dypls_20170830_models.QueryCertifyOverviewInfoRequest,
    ) -> dypls_20170830_models.QueryCertifyOverviewInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_certify_overview_info_with_options_async(request, runtime)

    def query_contacts_list_with_options(
        self,
        request: dypls_20170830_models.QueryContactsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryContactsListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
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
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryContactsListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_contacts_list_with_options_async(
        self,
        request: dypls_20170830_models.QueryContactsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryContactsListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
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
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryContactsListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_contacts_list(
        self,
        request: dypls_20170830_models.QueryContactsListRequest,
    ) -> dypls_20170830_models.QueryContactsListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_contacts_list_with_options(request, runtime)

    async def query_contacts_list_async(
        self,
        request: dypls_20170830_models.QueryContactsListRequest,
    ) -> dypls_20170830_models.QueryContactsListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_contacts_list_with_options_async(request, runtime)

    def query_cust_info_with_options(
        self,
        request: dypls_20170830_models.QueryCustInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryCustInfoResponse:
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
            action='QueryCustInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryCustInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cust_info_with_options_async(
        self,
        request: dypls_20170830_models.QueryCustInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryCustInfoResponse:
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
            action='QueryCustInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryCustInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cust_info(
        self,
        request: dypls_20170830_models.QueryCustInfoRequest,
    ) -> dypls_20170830_models.QueryCustInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_cust_info_with_options(request, runtime)

    async def query_cust_info_async(
        self,
        request: dypls_20170830_models.QueryCustInfoRequest,
    ) -> dypls_20170830_models.QueryCustInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_cust_info_with_options_async(request, runtime)

    def query_download_url_with_options(
        self,
        request: dypls_20170830_models.QueryDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryDownloadUrlResponse:
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
            action='QueryDownloadUrl',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_download_url_with_options_async(
        self,
        request: dypls_20170830_models.QueryDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryDownloadUrlResponse:
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
            action='QueryDownloadUrl',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_download_url(
        self,
        request: dypls_20170830_models.QueryDownloadUrlRequest,
    ) -> dypls_20170830_models.QueryDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_download_url_with_options(request, runtime)

    async def query_download_url_async(
        self,
        request: dypls_20170830_models.QueryDownloadUrlRequest,
    ) -> dypls_20170830_models.QueryDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_download_url_with_options_async(request, runtime)

    def query_effective_invoice_list_by_bill_nos_with_options(
        self,
        request: dypls_20170830_models.QueryEffectiveInvoiceListByBillNosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryEffectiveInvoiceListByBillNosResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_code):
            body['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.bill_no):
            body['BillNo'] = request.bill_no
        body_flat = {}
        if not UtilClient.is_unset(request.encrypt_props):
            body_flat['EncryptProps'] = request.encrypt_props
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.major_bill_no):
            body['MajorBillNo'] = request.major_bill_no
        if not UtilClient.is_unset(request.ou_code):
            body['OuCode'] = request.ou_code
        if not UtilClient.is_unset(request.related_system):
            body['RelatedSystem'] = request.related_system
        if not UtilClient.is_unset(request.sign):
            body['Sign'] = request.sign
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryEffectiveInvoiceListByBillNos',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryEffectiveInvoiceListByBillNosResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_effective_invoice_list_by_bill_nos_with_options_async(
        self,
        request: dypls_20170830_models.QueryEffectiveInvoiceListByBillNosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryEffectiveInvoiceListByBillNosResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_code):
            body['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.bill_no):
            body['BillNo'] = request.bill_no
        body_flat = {}
        if not UtilClient.is_unset(request.encrypt_props):
            body_flat['EncryptProps'] = request.encrypt_props
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.major_bill_no):
            body['MajorBillNo'] = request.major_bill_no
        if not UtilClient.is_unset(request.ou_code):
            body['OuCode'] = request.ou_code
        if not UtilClient.is_unset(request.related_system):
            body['RelatedSystem'] = request.related_system
        if not UtilClient.is_unset(request.sign):
            body['Sign'] = request.sign
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryEffectiveInvoiceListByBillNos',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryEffectiveInvoiceListByBillNosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_effective_invoice_list_by_bill_nos(
        self,
        request: dypls_20170830_models.QueryEffectiveInvoiceListByBillNosRequest,
    ) -> dypls_20170830_models.QueryEffectiveInvoiceListByBillNosResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_effective_invoice_list_by_bill_nos_with_options(request, runtime)

    async def query_effective_invoice_list_by_bill_nos_async(
        self,
        request: dypls_20170830_models.QueryEffectiveInvoiceListByBillNosRequest,
    ) -> dypls_20170830_models.QueryEffectiveInvoiceListByBillNosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_effective_invoice_list_by_bill_nos_with_options_async(request, runtime)

    def query_export_res_url_with_options(
        self,
        request: dypls_20170830_models.QueryExportResUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryExportResUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
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
            action='QueryExportResUrl',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryExportResUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_export_res_url_with_options_async(
        self,
        request: dypls_20170830_models.QueryExportResUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryExportResUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
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
            action='QueryExportResUrl',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryExportResUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_export_res_url(
        self,
        request: dypls_20170830_models.QueryExportResUrlRequest,
    ) -> dypls_20170830_models.QueryExportResUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_export_res_url_with_options(request, runtime)

    async def query_export_res_url_async(
        self,
        request: dypls_20170830_models.QueryExportResUrlRequest,
    ) -> dypls_20170830_models.QueryExportResUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_export_res_url_with_options_async(request, runtime)

    def query_group_detail_list_with_options(
        self,
        request: dypls_20170830_models.QueryGroupDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryGroupDetailListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
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
            action='QueryGroupDetailList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryGroupDetailListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_group_detail_list_with_options_async(
        self,
        request: dypls_20170830_models.QueryGroupDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryGroupDetailListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
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
            action='QueryGroupDetailList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryGroupDetailListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_group_detail_list(
        self,
        request: dypls_20170830_models.QueryGroupDetailListRequest,
    ) -> dypls_20170830_models.QueryGroupDetailListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_group_detail_list_with_options(request, runtime)

    async def query_group_detail_list_async(
        self,
        request: dypls_20170830_models.QueryGroupDetailListRequest,
    ) -> dypls_20170830_models.QueryGroupDetailListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_group_detail_list_with_options_async(request, runtime)

    def query_group_info_list_with_options(
        self,
        request: dypls_20170830_models.QueryGroupInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryGroupInfoListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.query_key):
            query['QueryKey'] = request.query_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGroupInfoList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryGroupInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_group_info_list_with_options_async(
        self,
        request: dypls_20170830_models.QueryGroupInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryGroupInfoListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.query_key):
            query['QueryKey'] = request.query_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGroupInfoList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryGroupInfoListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_group_info_list(
        self,
        request: dypls_20170830_models.QueryGroupInfoListRequest,
    ) -> dypls_20170830_models.QueryGroupInfoListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_group_info_list_with_options(request, runtime)

    async def query_group_info_list_async(
        self,
        request: dypls_20170830_models.QueryGroupInfoListRequest,
    ) -> dypls_20170830_models.QueryGroupInfoListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_group_info_list_with_options_async(request, runtime)

    def query_invoice_info_by_request_no_with_options(
        self,
        request: dypls_20170830_models.QueryInvoiceInfoByRequestNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryInvoiceInfoByRequestNoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_code):
            body['AppCode'] = request.app_code
        body_flat = {}
        if not UtilClient.is_unset(request.encrypt_props):
            body_flat['EncryptProps'] = request.encrypt_props
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.related_system):
            body['RelatedSystem'] = request.related_system
        if not UtilClient.is_unset(request.request_no):
            body['RequestNo'] = request.request_no
        if not UtilClient.is_unset(request.sign):
            body['Sign'] = request.sign
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryInvoiceInfoByRequestNo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryInvoiceInfoByRequestNoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_invoice_info_by_request_no_with_options_async(
        self,
        request: dypls_20170830_models.QueryInvoiceInfoByRequestNoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryInvoiceInfoByRequestNoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_code):
            body['AppCode'] = request.app_code
        body_flat = {}
        if not UtilClient.is_unset(request.encrypt_props):
            body_flat['EncryptProps'] = request.encrypt_props
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.related_system):
            body['RelatedSystem'] = request.related_system
        if not UtilClient.is_unset(request.request_no):
            body['RequestNo'] = request.request_no
        if not UtilClient.is_unset(request.sign):
            body['Sign'] = request.sign
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryInvoiceInfoByRequestNo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryInvoiceInfoByRequestNoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_invoice_info_by_request_no(
        self,
        request: dypls_20170830_models.QueryInvoiceInfoByRequestNoRequest,
    ) -> dypls_20170830_models.QueryInvoiceInfoByRequestNoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_invoice_info_by_request_no_with_options(request, runtime)

    async def query_invoice_info_by_request_no_async(
        self,
        request: dypls_20170830_models.QueryInvoiceInfoByRequestNoRequest,
    ) -> dypls_20170830_models.QueryInvoiceInfoByRequestNoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_invoice_info_by_request_no_with_options_async(request, runtime)

    def query_message_callback_info_with_options(
        self,
        request: dypls_20170830_models.QueryMessageCallbackInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryMessageCallbackInfoResponse:
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
            action='QueryMessageCallbackInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryMessageCallbackInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_message_callback_info_with_options_async(
        self,
        request: dypls_20170830_models.QueryMessageCallbackInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryMessageCallbackInfoResponse:
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
            action='QueryMessageCallbackInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryMessageCallbackInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_message_callback_info(
        self,
        request: dypls_20170830_models.QueryMessageCallbackInfoRequest,
    ) -> dypls_20170830_models.QueryMessageCallbackInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_message_callback_info_with_options(request, runtime)

    async def query_message_callback_info_async(
        self,
        request: dypls_20170830_models.QueryMessageCallbackInfoRequest,
    ) -> dypls_20170830_models.QueryMessageCallbackInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_message_callback_info_with_options_async(request, runtime)

    def query_message_queue_list_with_options(
        self,
        request: dypls_20170830_models.QueryMessageQueueListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryMessageQueueListResponse:
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
            action='QueryMessageQueueList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryMessageQueueListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_message_queue_list_with_options_async(
        self,
        request: dypls_20170830_models.QueryMessageQueueListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryMessageQueueListResponse:
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
            action='QueryMessageQueueList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryMessageQueueListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_message_queue_list(
        self,
        request: dypls_20170830_models.QueryMessageQueueListRequest,
    ) -> dypls_20170830_models.QueryMessageQueueListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_message_queue_list_with_options(request, runtime)

    async def query_message_queue_list_async(
        self,
        request: dypls_20170830_models.QueryMessageQueueListRequest,
    ) -> dypls_20170830_models.QueryMessageQueueListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_message_queue_list_with_options_async(request, runtime)

    def query_monthly_bill_info_with_options(
        self,
        request: dypls_20170830_models.QueryMonthlyBillInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryMonthlyBillInfoResponse:
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
            action='QueryMonthlyBillInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryMonthlyBillInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_monthly_bill_info_with_options_async(
        self,
        request: dypls_20170830_models.QueryMonthlyBillInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryMonthlyBillInfoResponse:
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
            action='QueryMonthlyBillInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryMonthlyBillInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_monthly_bill_info(
        self,
        request: dypls_20170830_models.QueryMonthlyBillInfoRequest,
    ) -> dypls_20170830_models.QueryMonthlyBillInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_monthly_bill_info_with_options(request, runtime)

    async def query_monthly_bill_info_async(
        self,
        request: dypls_20170830_models.QueryMonthlyBillInfoRequest,
    ) -> dypls_20170830_models.QueryMonthlyBillInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_monthly_bill_info_with_options_async(request, runtime)

    def query_monthly_statistics_info_with_options(
        self,
        request: dypls_20170830_models.QueryMonthlyStatisticsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryMonthlyStatisticsInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMonthlyStatisticsInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryMonthlyStatisticsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_monthly_statistics_info_with_options_async(
        self,
        request: dypls_20170830_models.QueryMonthlyStatisticsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryMonthlyStatisticsInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMonthlyStatisticsInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryMonthlyStatisticsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_monthly_statistics_info(
        self,
        request: dypls_20170830_models.QueryMonthlyStatisticsInfoRequest,
    ) -> dypls_20170830_models.QueryMonthlyStatisticsInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_monthly_statistics_info_with_options(request, runtime)

    async def query_monthly_statistics_info_async(
        self,
        request: dypls_20170830_models.QueryMonthlyStatisticsInfoRequest,
    ) -> dypls_20170830_models.QueryMonthlyStatisticsInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_monthly_statistics_info_with_options_async(request, runtime)

    def query_no_buy_tasks_with_options(
        self,
        request: dypls_20170830_models.QueryNoBuyTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryNoBuyTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
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
            action='QueryNoBuyTasks',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryNoBuyTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_no_buy_tasks_with_options_async(
        self,
        request: dypls_20170830_models.QueryNoBuyTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryNoBuyTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
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
            action='QueryNoBuyTasks',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryNoBuyTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_no_buy_tasks(
        self,
        request: dypls_20170830_models.QueryNoBuyTasksRequest,
    ) -> dypls_20170830_models.QueryNoBuyTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_no_buy_tasks_with_options(request, runtime)

    async def query_no_buy_tasks_async(
        self,
        request: dypls_20170830_models.QueryNoBuyTasksRequest,
    ) -> dypls_20170830_models.QueryNoBuyTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_no_buy_tasks_with_options_async(request, runtime)

    def query_no_distribute_with_options(
        self,
        request: dypls_20170830_models.QueryNoDistributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryNoDistributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
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
            action='QueryNoDistribute',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryNoDistributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_no_distribute_with_options_async(
        self,
        request: dypls_20170830_models.QueryNoDistributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryNoDistributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
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
            action='QueryNoDistribute',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryNoDistributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_no_distribute(
        self,
        request: dypls_20170830_models.QueryNoDistributeRequest,
    ) -> dypls_20170830_models.QueryNoDistributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_no_distribute_with_options(request, runtime)

    async def query_no_distribute_async(
        self,
        request: dypls_20170830_models.QueryNoDistributeRequest,
    ) -> dypls_20170830_models.QueryNoDistributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_no_distribute_with_options_async(request, runtime)

    def query_open_status_with_options(
        self,
        request: dypls_20170830_models.QueryOpenStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryOpenStatusResponse:
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
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryOpenStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_open_status_with_options_async(
        self,
        request: dypls_20170830_models.QueryOpenStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryOpenStatusResponse:
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
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryOpenStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_open_status(
        self,
        request: dypls_20170830_models.QueryOpenStatusRequest,
    ) -> dypls_20170830_models.QueryOpenStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_open_status_with_options(request, runtime)

    async def query_open_status_async(
        self,
        request: dypls_20170830_models.QueryOpenStatusRequest,
    ) -> dypls_20170830_models.QueryOpenStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_open_status_with_options_async(request, runtime)

    def query_package_detail_with_options(
        self,
        request: dypls_20170830_models.QueryPackageDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryPackageDetailResponse:
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPackageDetail',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPackageDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_package_detail_with_options_async(
        self,
        request: dypls_20170830_models.QueryPackageDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryPackageDetailResponse:
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPackageDetail',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPackageDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_package_detail(
        self,
        request: dypls_20170830_models.QueryPackageDetailRequest,
    ) -> dypls_20170830_models.QueryPackageDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_package_detail_with_options(request, runtime)

    async def query_package_detail_async(
        self,
        request: dypls_20170830_models.QueryPackageDetailRequest,
    ) -> dypls_20170830_models.QueryPackageDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_package_detail_with_options_async(request, runtime)

    def query_package_list_with_options(
        self,
        request: dypls_20170830_models.QueryPackageListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryPackageListResponse:
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
            action='QueryPackageList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPackageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_package_list_with_options_async(
        self,
        request: dypls_20170830_models.QueryPackageListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryPackageListResponse:
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
            action='QueryPackageList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPackageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_package_list(
        self,
        request: dypls_20170830_models.QueryPackageListRequest,
    ) -> dypls_20170830_models.QueryPackageListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_package_list_with_options(request, runtime)

    async def query_package_list_async(
        self,
        request: dypls_20170830_models.QueryPackageListRequest,
    ) -> dypls_20170830_models.QueryPackageListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_package_list_with_options_async(request, runtime)

    def query_package_statistics_with_options(
        self,
        request: dypls_20170830_models.QueryPackageStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryPackageStatisticsResponse:
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
            action='QueryPackageStatistics',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPackageStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_package_statistics_with_options_async(
        self,
        request: dypls_20170830_models.QueryPackageStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryPackageStatisticsResponse:
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
            action='QueryPackageStatistics',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPackageStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_package_statistics(
        self,
        request: dypls_20170830_models.QueryPackageStatisticsRequest,
    ) -> dypls_20170830_models.QueryPackageStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_package_statistics_with_options(request, runtime)

    async def query_package_statistics_async(
        self,
        request: dypls_20170830_models.QueryPackageStatisticsRequest,
    ) -> dypls_20170830_models.QueryPackageStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_package_statistics_with_options_async(request, runtime)

    def query_pool_city_list_with_options(
        self,
        request: dypls_20170830_models.QueryPoolCityListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryPoolCityListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
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
            action='QueryPoolCityList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPoolCityListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_pool_city_list_with_options_async(
        self,
        request: dypls_20170830_models.QueryPoolCityListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryPoolCityListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
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
            action='QueryPoolCityList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPoolCityListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_pool_city_list(
        self,
        request: dypls_20170830_models.QueryPoolCityListRequest,
    ) -> dypls_20170830_models.QueryPoolCityListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_pool_city_list_with_options(request, runtime)

    async def query_pool_city_list_async(
        self,
        request: dypls_20170830_models.QueryPoolCityListRequest,
    ) -> dypls_20170830_models.QueryPoolCityListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_pool_city_list_with_options_async(request, runtime)

    def query_pool_info_list_with_options(
        self,
        request: dypls_20170830_models.QueryPoolInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryPoolInfoListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_fuzzy_query):
            query['IsFuzzyQuery'] = request.is_fuzzy_query
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.search_param):
            query['SearchParam'] = request.search_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPoolInfoList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPoolInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_pool_info_list_with_options_async(
        self,
        request: dypls_20170830_models.QueryPoolInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryPoolInfoListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_fuzzy_query):
            query['IsFuzzyQuery'] = request.is_fuzzy_query
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.search_param):
            query['SearchParam'] = request.search_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPoolInfoList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPoolInfoListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_pool_info_list(
        self,
        request: dypls_20170830_models.QueryPoolInfoListRequest,
    ) -> dypls_20170830_models.QueryPoolInfoListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_pool_info_list_with_options(request, runtime)

    async def query_pool_info_list_async(
        self,
        request: dypls_20170830_models.QueryPoolInfoListRequest,
    ) -> dypls_20170830_models.QueryPoolInfoListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_pool_info_list_with_options_async(request, runtime)

    def query_pool_monthly_bill_info_with_options(
        self,
        request: dypls_20170830_models.QueryPoolMonthlyBillInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryPoolMonthlyBillInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
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
            action='QueryPoolMonthlyBillInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPoolMonthlyBillInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_pool_monthly_bill_info_with_options_async(
        self,
        request: dypls_20170830_models.QueryPoolMonthlyBillInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryPoolMonthlyBillInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
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
            action='QueryPoolMonthlyBillInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPoolMonthlyBillInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_pool_monthly_bill_info(
        self,
        request: dypls_20170830_models.QueryPoolMonthlyBillInfoRequest,
    ) -> dypls_20170830_models.QueryPoolMonthlyBillInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_pool_monthly_bill_info_with_options(request, runtime)

    async def query_pool_monthly_bill_info_async(
        self,
        request: dypls_20170830_models.QueryPoolMonthlyBillInfoRequest,
    ) -> dypls_20170830_models.QueryPoolMonthlyBillInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_pool_monthly_bill_info_with_options_async(request, runtime)

    def query_pool_statistics_info_with_options(
        self,
        request: dypls_20170830_models.QueryPoolStatisticsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryPoolStatisticsInfoResponse:
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
            action='QueryPoolStatisticsInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPoolStatisticsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_pool_statistics_info_with_options_async(
        self,
        request: dypls_20170830_models.QueryPoolStatisticsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryPoolStatisticsInfoResponse:
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
            action='QueryPoolStatisticsInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPoolStatisticsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_pool_statistics_info(
        self,
        request: dypls_20170830_models.QueryPoolStatisticsInfoRequest,
    ) -> dypls_20170830_models.QueryPoolStatisticsInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_pool_statistics_info_with_options(request, runtime)

    async def query_pool_statistics_info_async(
        self,
        request: dypls_20170830_models.QueryPoolStatisticsInfoRequest,
    ) -> dypls_20170830_models.QueryPoolStatisticsInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_pool_statistics_info_with_options_async(request, runtime)

    def query_pool_summary_info_with_options(
        self,
        request: dypls_20170830_models.QueryPoolSummaryInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryPoolSummaryInfoResponse:
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
            action='QueryPoolSummaryInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPoolSummaryInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_pool_summary_info_with_options_async(
        self,
        request: dypls_20170830_models.QueryPoolSummaryInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryPoolSummaryInfoResponse:
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
            action='QueryPoolSummaryInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPoolSummaryInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_pool_summary_info(
        self,
        request: dypls_20170830_models.QueryPoolSummaryInfoRequest,
    ) -> dypls_20170830_models.QueryPoolSummaryInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_pool_summary_info_with_options(request, runtime)

    async def query_pool_summary_info_async(
        self,
        request: dypls_20170830_models.QueryPoolSummaryInfoRequest,
    ) -> dypls_20170830_models.QueryPoolSummaryInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_pool_summary_info_with_options_async(request, runtime)

    def query_purchased_info_with_options(
        self,
        request: dypls_20170830_models.QueryPurchasedInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryPurchasedInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPurchasedInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPurchasedInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_purchased_info_with_options_async(
        self,
        request: dypls_20170830_models.QueryPurchasedInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryPurchasedInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPurchasedInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPurchasedInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_purchased_info(
        self,
        request: dypls_20170830_models.QueryPurchasedInfoRequest,
    ) -> dypls_20170830_models.QueryPurchasedInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_purchased_info_with_options(request, runtime)

    async def query_purchased_info_async(
        self,
        request: dypls_20170830_models.QueryPurchasedInfoRequest,
    ) -> dypls_20170830_models.QueryPurchasedInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_purchased_info_with_options_async(request, runtime)

    def query_purchased_res_list_with_options(
        self,
        request: dypls_20170830_models.QueryPurchasedResListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryPurchasedResListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.is_display_pool):
            query['IsDisplayPool'] = request.is_display_pool
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_bind_status):
            query['ResBindStatus'] = request.res_bind_status
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPurchasedResList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPurchasedResListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_purchased_res_list_with_options_async(
        self,
        request: dypls_20170830_models.QueryPurchasedResListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryPurchasedResListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.is_display_pool):
            query['IsDisplayPool'] = request.is_display_pool
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_bind_status):
            query['ResBindStatus'] = request.res_bind_status
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPurchasedResList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryPurchasedResListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_purchased_res_list(
        self,
        request: dypls_20170830_models.QueryPurchasedResListRequest,
    ) -> dypls_20170830_models.QueryPurchasedResListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_purchased_res_list_with_options(request, runtime)

    async def query_purchased_res_list_async(
        self,
        request: dypls_20170830_models.QueryPurchasedResListRequest,
    ) -> dypls_20170830_models.QueryPurchasedResListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_purchased_res_list_with_options_async(request, runtime)

    def query_qrcode_info_with_options(
        self,
        request: dypls_20170830_models.QueryQRCodeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryQRCodeInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_number):
            query['SecretNumber'] = request.secret_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryQRCodeInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryQRCodeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_qrcode_info_with_options_async(
        self,
        request: dypls_20170830_models.QueryQRCodeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryQRCodeInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_number):
            query['SecretNumber'] = request.secret_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryQRCodeInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryQRCodeInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_qrcode_info(
        self,
        request: dypls_20170830_models.QueryQRCodeInfoRequest,
    ) -> dypls_20170830_models.QueryQRCodeInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_qrcode_info_with_options(request, runtime)

    async def query_qrcode_info_async(
        self,
        request: dypls_20170830_models.QueryQRCodeInfoRequest,
    ) -> dypls_20170830_models.QueryQRCodeInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_qrcode_info_with_options_async(request, runtime)

    def query_recording_url_with_options(
        self,
        request: dypls_20170830_models.QueryRecordingUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryRecordingUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.call_date):
            query['CallDate'] = request.call_date
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordingUrl',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryRecordingUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_recording_url_with_options_async(
        self,
        request: dypls_20170830_models.QueryRecordingUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryRecordingUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.call_date):
            query['CallDate'] = request.call_date
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordingUrl',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryRecordingUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_recording_url(
        self,
        request: dypls_20170830_models.QueryRecordingUrlRequest,
    ) -> dypls_20170830_models.QueryRecordingUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_recording_url_with_options(request, runtime)

    async def query_recording_url_async(
        self,
        request: dypls_20170830_models.QueryRecordingUrlRequest,
    ) -> dypls_20170830_models.QueryRecordingUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_recording_url_with_options_async(request, runtime)

    def query_res_summary_info_with_options(
        self,
        request: dypls_20170830_models.QueryResSummaryInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryResSummaryInfoResponse:
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
            action='QueryResSummaryInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryResSummaryInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_res_summary_info_with_options_async(
        self,
        request: dypls_20170830_models.QueryResSummaryInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryResSummaryInfoResponse:
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
            action='QueryResSummaryInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryResSummaryInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_res_summary_info(
        self,
        request: dypls_20170830_models.QueryResSummaryInfoRequest,
    ) -> dypls_20170830_models.QueryResSummaryInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_res_summary_info_with_options(request, runtime)

    async def query_res_summary_info_async(
        self,
        request: dypls_20170830_models.QueryResSummaryInfoRequest,
    ) -> dypls_20170830_models.QueryResSummaryInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_res_summary_info_with_options_async(request, runtime)

    def query_ring_tone_url_with_options(
        self,
        request: dypls_20170830_models.QueryRingToneUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryRingToneUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.file_key):
            query['FileKey'] = request.file_key
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
            action='QueryRingToneUrl',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryRingToneUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ring_tone_url_with_options_async(
        self,
        request: dypls_20170830_models.QueryRingToneUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryRingToneUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.file_key):
            query['FileKey'] = request.file_key
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
            action='QueryRingToneUrl',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryRingToneUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ring_tone_url(
        self,
        request: dypls_20170830_models.QueryRingToneUrlRequest,
    ) -> dypls_20170830_models.QueryRingToneUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_ring_tone_url_with_options(request, runtime)

    async def query_ring_tone_url_async(
        self,
        request: dypls_20170830_models.QueryRingToneUrlRequest,
    ) -> dypls_20170830_models.QueryRingToneUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_ring_tone_url_with_options_async(request, runtime)

    def query_ring_tones_with_options(
        self,
        request: dypls_20170830_models.QueryRingTonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryRingTonesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.play_type):
            query['PlayType'] = request.play_type
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
            action='QueryRingTones',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryRingTonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ring_tones_with_options_async(
        self,
        request: dypls_20170830_models.QueryRingTonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryRingTonesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.play_type):
            query['PlayType'] = request.play_type
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
            action='QueryRingTones',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryRingTonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ring_tones(
        self,
        request: dypls_20170830_models.QueryRingTonesRequest,
    ) -> dypls_20170830_models.QueryRingTonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_ring_tones_with_options(request, runtime)

    async def query_ring_tones_async(
        self,
        request: dypls_20170830_models.QueryRingTonesRequest,
    ) -> dypls_20170830_models.QueryRingTonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_ring_tones_with_options_async(request, runtime)

    def query_simple_pool_info_list_with_options(
        self,
        request: dypls_20170830_models.QuerySimplePoolInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QuerySimplePoolInfoListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySimplePoolInfoList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QuerySimplePoolInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_simple_pool_info_list_with_options_async(
        self,
        request: dypls_20170830_models.QuerySimplePoolInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QuerySimplePoolInfoListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySimplePoolInfoList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QuerySimplePoolInfoListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_simple_pool_info_list(
        self,
        request: dypls_20170830_models.QuerySimplePoolInfoListRequest,
    ) -> dypls_20170830_models.QuerySimplePoolInfoListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_simple_pool_info_list_with_options(request, runtime)

    async def query_simple_pool_info_list_async(
        self,
        request: dypls_20170830_models.QuerySimplePoolInfoListRequest,
    ) -> dypls_20170830_models.QuerySimplePoolInfoListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_simple_pool_info_list_with_options_async(request, runtime)

    def query_statistics_info_with_options(
        self,
        request: dypls_20170830_models.QueryStatisticsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryStatisticsInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
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
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStatisticsInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryStatisticsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_statistics_info_with_options_async(
        self,
        request: dypls_20170830_models.QueryStatisticsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryStatisticsInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
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
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStatisticsInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryStatisticsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_statistics_info(
        self,
        request: dypls_20170830_models.QueryStatisticsInfoRequest,
    ) -> dypls_20170830_models.QueryStatisticsInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_statistics_info_with_options(request, runtime)

    async def query_statistics_info_async(
        self,
        request: dypls_20170830_models.QueryStatisticsInfoRequest,
    ) -> dypls_20170830_models.QueryStatisticsInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_statistics_info_with_options_async(request, runtime)

    def query_tag_open_status_with_options(
        self,
        request: dypls_20170830_models.QueryTagOpenStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryTagOpenStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attribute_key):
            query['AttributeKey'] = request.attribute_key
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sub_attribute_key):
            query['SubAttributeKey'] = request.sub_attribute_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTagOpenStatus',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryTagOpenStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_tag_open_status_with_options_async(
        self,
        request: dypls_20170830_models.QueryTagOpenStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryTagOpenStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attribute_key):
            query['AttributeKey'] = request.attribute_key
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sub_attribute_key):
            query['SubAttributeKey'] = request.sub_attribute_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTagOpenStatus',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryTagOpenStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_tag_open_status(
        self,
        request: dypls_20170830_models.QueryTagOpenStatusRequest,
    ) -> dypls_20170830_models.QueryTagOpenStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_tag_open_status_with_options(request, runtime)

    async def query_tag_open_status_async(
        self,
        request: dypls_20170830_models.QueryTagOpenStatusRequest,
    ) -> dypls_20170830_models.QueryTagOpenStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_tag_open_status_with_options_async(request, runtime)

    def query_transfer_details_with_options(
        self,
        request: dypls_20170830_models.QueryTransferDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryTransferDetailsResponse:
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
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTransferDetails',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryTransferDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_transfer_details_with_options_async(
        self,
        request: dypls_20170830_models.QueryTransferDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryTransferDetailsResponse:
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
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTransferDetails',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryTransferDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_transfer_details(
        self,
        request: dypls_20170830_models.QueryTransferDetailsRequest,
    ) -> dypls_20170830_models.QueryTransferDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_transfer_details_with_options(request, runtime)

    async def query_transfer_details_async(
        self,
        request: dypls_20170830_models.QueryTransferDetailsRequest,
    ) -> dypls_20170830_models.QueryTransferDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_transfer_details_with_options_async(request, runtime)

    def query_transfer_record_with_options(
        self,
        request: dypls_20170830_models.QueryTransferRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryTransferRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTransferRecord',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryTransferRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_transfer_record_with_options_async(
        self,
        request: dypls_20170830_models.QueryTransferRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryTransferRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTransferRecord',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryTransferRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_transfer_record(
        self,
        request: dypls_20170830_models.QueryTransferRecordRequest,
    ) -> dypls_20170830_models.QueryTransferRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_transfer_record_with_options(request, runtime)

    async def query_transfer_record_async(
        self,
        request: dypls_20170830_models.QueryTransferRecordRequest,
    ) -> dypls_20170830_models.QueryTransferRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_transfer_record_with_options_async(request, runtime)

    def query_transfer_records_with_options(
        self,
        request: dypls_20170830_models.QueryTransferRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryTransferRecordsResponse:
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
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTransferRecords',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryTransferRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_transfer_records_with_options_async(
        self,
        request: dypls_20170830_models.QueryTransferRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryTransferRecordsResponse:
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
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTransferRecords',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryTransferRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_transfer_records(
        self,
        request: dypls_20170830_models.QueryTransferRecordsRequest,
    ) -> dypls_20170830_models.QueryTransferRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_transfer_records_with_options(request, runtime)

    async def query_transfer_records_async(
        self,
        request: dypls_20170830_models.QueryTransferRecordsRequest,
    ) -> dypls_20170830_models.QueryTransferRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_transfer_records_with_options_async(request, runtime)

    def query_user_delete_status_with_options(
        self,
        request: dypls_20170830_models.QueryUserDeleteStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryUserDeleteStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.gmt_wakeup):
            query['GmtWakeup'] = request.gmt_wakeup
        if not UtilClient.is_unset(request.hid):
            query['Hid'] = request.hid
        if not UtilClient.is_unset(request.interrupt):
            query['Interrupt'] = request.interrupt
        if not UtilClient.is_unset(request.invoker):
            query['Invoker'] = request.invoker
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prompt):
            query['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.success):
            query['Success'] = request.success
        if not UtilClient.is_unset(request.task_extra_data):
            query['TaskExtraData'] = request.task_extra_data
        if not UtilClient.is_unset(request.task_identifier):
            query['TaskIdentifier'] = request.task_identifier
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserDeleteStatus',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryUserDeleteStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_delete_status_with_options_async(
        self,
        request: dypls_20170830_models.QueryUserDeleteStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryUserDeleteStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bid):
            query['Bid'] = request.bid
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.gmt_wakeup):
            query['GmtWakeup'] = request.gmt_wakeup
        if not UtilClient.is_unset(request.hid):
            query['Hid'] = request.hid
        if not UtilClient.is_unset(request.interrupt):
            query['Interrupt'] = request.interrupt
        if not UtilClient.is_unset(request.invoker):
            query['Invoker'] = request.invoker
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.prompt):
            query['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.success):
            query['Success'] = request.success
        if not UtilClient.is_unset(request.task_extra_data):
            query['TaskExtraData'] = request.task_extra_data
        if not UtilClient.is_unset(request.task_identifier):
            query['TaskIdentifier'] = request.task_identifier
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserDeleteStatus',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryUserDeleteStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_delete_status(
        self,
        request: dypls_20170830_models.QueryUserDeleteStatusRequest,
    ) -> dypls_20170830_models.QueryUserDeleteStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_user_delete_status_with_options(request, runtime)

    async def query_user_delete_status_async(
        self,
        request: dypls_20170830_models.QueryUserDeleteStatusRequest,
    ) -> dypls_20170830_models.QueryUserDeleteStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_user_delete_status_with_options_async(request, runtime)

    def query_user_info_with_options(
        self,
        request: dypls_20170830_models.QueryUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryUserInfoResponse:
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
            action='QueryUserInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_info_with_options_async(
        self,
        request: dypls_20170830_models.QueryUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryUserInfoResponse:
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
            action='QueryUserInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryUserInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_info(
        self,
        request: dypls_20170830_models.QueryUserInfoRequest,
    ) -> dypls_20170830_models.QueryUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_user_info_with_options(request, runtime)

    async def query_user_info_async(
        self,
        request: dypls_20170830_models.QueryUserInfoRequest,
    ) -> dypls_20170830_models.QueryUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_user_info_with_options_async(request, runtime)

    def query_user_res_pool_info_with_options(
        self,
        request: dypls_20170830_models.QueryUserResPoolInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryUserResPoolInfoResponse:
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
            action='QueryUserResPoolInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryUserResPoolInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_res_pool_info_with_options_async(
        self,
        request: dypls_20170830_models.QueryUserResPoolInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryUserResPoolInfoResponse:
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
            action='QueryUserResPoolInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryUserResPoolInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_res_pool_info(
        self,
        request: dypls_20170830_models.QueryUserResPoolInfoRequest,
    ) -> dypls_20170830_models.QueryUserResPoolInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_user_res_pool_info_with_options(request, runtime)

    async def query_user_res_pool_info_async(
        self,
        request: dypls_20170830_models.QueryUserResPoolInfoRequest,
    ) -> dypls_20170830_models.QueryUserResPoolInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_user_res_pool_info_with_options_async(request, runtime)

    def query_virtual_operation_show_with_options(
        self,
        request: dypls_20170830_models.QueryVirtualOperationShowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryVirtualOperationShowResponse:
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
            action='QueryVirtualOperationShow',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryVirtualOperationShowResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_virtual_operation_show_with_options_async(
        self,
        request: dypls_20170830_models.QueryVirtualOperationShowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryVirtualOperationShowResponse:
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
            action='QueryVirtualOperationShow',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryVirtualOperationShowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_virtual_operation_show(
        self,
        request: dypls_20170830_models.QueryVirtualOperationShowRequest,
    ) -> dypls_20170830_models.QueryVirtualOperationShowResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_virtual_operation_show_with_options(request, runtime)

    async def query_virtual_operation_show_async(
        self,
        request: dypls_20170830_models.QueryVirtualOperationShowRequest,
    ) -> dypls_20170830_models.QueryVirtualOperationShowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_virtual_operation_show_with_options_async(request, runtime)

    def query_warning_list_with_options(
        self,
        request: dypls_20170830_models.QueryWarningListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryWarningListResponse:
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
            action='QueryWarningList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryWarningListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_warning_list_with_options_async(
        self,
        request: dypls_20170830_models.QueryWarningListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryWarningListResponse:
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
            action='QueryWarningList',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryWarningListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_warning_list(
        self,
        request: dypls_20170830_models.QueryWarningListRequest,
    ) -> dypls_20170830_models.QueryWarningListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_warning_list_with_options(request, runtime)

    async def query_warning_list_async(
        self,
        request: dypls_20170830_models.QueryWarningListRequest,
    ) -> dypls_20170830_models.QueryWarningListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_warning_list_with_options_async(request, runtime)

    def query_waybill_order_info_with_options(
        self,
        request: dypls_20170830_models.QueryWaybillOrderInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryWaybillOrderInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.outer_order_code):
            query['OuterOrderCode'] = request.outer_order_code
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
            action='QueryWaybillOrderInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryWaybillOrderInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_waybill_order_info_with_options_async(
        self,
        request: dypls_20170830_models.QueryWaybillOrderInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryWaybillOrderInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.outer_order_code):
            query['OuterOrderCode'] = request.outer_order_code
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
            action='QueryWaybillOrderInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryWaybillOrderInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_waybill_order_info(
        self,
        request: dypls_20170830_models.QueryWaybillOrderInfoRequest,
    ) -> dypls_20170830_models.QueryWaybillOrderInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_waybill_order_info_with_options(request, runtime)

    async def query_waybill_order_info_async(
        self,
        request: dypls_20170830_models.QueryWaybillOrderInfoRequest,
    ) -> dypls_20170830_models.QueryWaybillOrderInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_waybill_order_info_with_options_async(request, runtime)

    def query_waybill_order_statistics_info_with_options(
        self,
        request: dypls_20170830_models.QueryWaybillOrderStatisticsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryWaybillOrderStatisticsInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWaybillOrderStatisticsInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryWaybillOrderStatisticsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_waybill_order_statistics_info_with_options_async(
        self,
        request: dypls_20170830_models.QueryWaybillOrderStatisticsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.QueryWaybillOrderStatisticsInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWaybillOrderStatisticsInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.QueryWaybillOrderStatisticsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_waybill_order_statistics_info(
        self,
        request: dypls_20170830_models.QueryWaybillOrderStatisticsInfoRequest,
    ) -> dypls_20170830_models.QueryWaybillOrderStatisticsInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_waybill_order_statistics_info_with_options(request, runtime)

    async def query_waybill_order_statistics_info_async(
        self,
        request: dypls_20170830_models.QueryWaybillOrderStatisticsInfoRequest,
    ) -> dypls_20170830_models.QueryWaybillOrderStatisticsInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_waybill_order_statistics_info_with_options_async(request, runtime)

    def release_resource_with_options(
        self,
        request: dypls_20170830_models.ReleaseResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.ReleaseResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.is_display_pool):
            query['IsDisplayPool'] = request.is_display_pool
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseResource',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ReleaseResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_resource_with_options_async(
        self,
        request: dypls_20170830_models.ReleaseResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.ReleaseResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.is_display_pool):
            query['IsDisplayPool'] = request.is_display_pool
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseResource',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ReleaseResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_resource(
        self,
        request: dypls_20170830_models.ReleaseResourceRequest,
    ) -> dypls_20170830_models.ReleaseResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_resource_with_options(request, runtime)

    async def release_resource_async(
        self,
        request: dypls_20170830_models.ReleaseResourceRequest,
    ) -> dypls_20170830_models.ReleaseResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_resource_with_options_async(request, runtime)

    def test_tts_ring_tone_with_options(
        self,
        request: dypls_20170830_models.TestTtsRingToneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.TestTtsRingToneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tts):
            query['Tts'] = request.tts
        if not UtilClient.is_unset(request.voice_speed):
            query['VoiceSpeed'] = request.voice_speed
        if not UtilClient.is_unset(request.voice_style):
            query['VoiceStyle'] = request.voice_style
        if not UtilClient.is_unset(request.voice_type):
            query['VoiceType'] = request.voice_type
        if not UtilClient.is_unset(request.voice_volume):
            query['VoiceVolume'] = request.voice_volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TestTtsRingTone',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.TestTtsRingToneResponse(),
            self.call_api(params, req, runtime)
        )

    async def test_tts_ring_tone_with_options_async(
        self,
        request: dypls_20170830_models.TestTtsRingToneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.TestTtsRingToneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tts):
            query['Tts'] = request.tts
        if not UtilClient.is_unset(request.voice_speed):
            query['VoiceSpeed'] = request.voice_speed
        if not UtilClient.is_unset(request.voice_style):
            query['VoiceStyle'] = request.voice_style
        if not UtilClient.is_unset(request.voice_type):
            query['VoiceType'] = request.voice_type
        if not UtilClient.is_unset(request.voice_volume):
            query['VoiceVolume'] = request.voice_volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TestTtsRingTone',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.TestTtsRingToneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def test_tts_ring_tone(
        self,
        request: dypls_20170830_models.TestTtsRingToneRequest,
    ) -> dypls_20170830_models.TestTtsRingToneResponse:
        runtime = util_models.RuntimeOptions()
        return self.test_tts_ring_tone_with_options(request, runtime)

    async def test_tts_ring_tone_async(
        self,
        request: dypls_20170830_models.TestTtsRingToneRequest,
    ) -> dypls_20170830_models.TestTtsRingToneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.test_tts_ring_tone_with_options_async(request, runtime)

    def unbind_resource_with_options(
        self,
        request: dypls_20170830_models.UnbindResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.UnbindResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.bind_ids):
            query['BindIds'] = request.bind_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindResource',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.UnbindResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_resource_with_options_async(
        self,
        request: dypls_20170830_models.UnbindResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.UnbindResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.bind_ids):
            query['BindIds'] = request.bind_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindResource',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.UnbindResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_resource(
        self,
        request: dypls_20170830_models.UnbindResourceRequest,
    ) -> dypls_20170830_models.UnbindResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_resource_with_options(request, runtime)

    async def unbind_resource_async(
        self,
        request: dypls_20170830_models.UnbindResourceRequest,
    ) -> dypls_20170830_models.UnbindResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_resource_with_options_async(request, runtime)

    def unlock_resource_with_options(
        self,
        request: dypls_20170830_models.UnlockResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.UnlockResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockResource',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.UnlockResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unlock_resource_with_options_async(
        self,
        request: dypls_20170830_models.UnlockResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.UnlockResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockResource',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.UnlockResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unlock_resource(
        self,
        request: dypls_20170830_models.UnlockResourceRequest,
    ) -> dypls_20170830_models.UnlockResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.unlock_resource_with_options(request, runtime)

    async def unlock_resource_async(
        self,
        request: dypls_20170830_models.UnlockResourceRequest,
    ) -> dypls_20170830_models.UnlockResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unlock_resource_with_options_async(request, runtime)

    def update_contacts_with_options(
        self,
        request: dypls_20170830_models.UpdateContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.UpdateContactsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='UpdateContacts',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.UpdateContactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_contacts_with_options_async(
        self,
        request: dypls_20170830_models.UpdateContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.UpdateContactsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='UpdateContacts',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.UpdateContactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_contacts(
        self,
        request: dypls_20170830_models.UpdateContactsRequest,
    ) -> dypls_20170830_models.UpdateContactsResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_contacts_with_options(request, runtime)

    async def update_contacts_async(
        self,
        request: dypls_20170830_models.UpdateContactsRequest,
    ) -> dypls_20170830_models.UpdateContactsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_contacts_with_options_async(request, runtime)

    def update_group_detail_with_options(
        self,
        request: dypls_20170830_models.UpdateGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.UpdateGroupDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroupDetail',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.UpdateGroupDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_group_detail_with_options_async(
        self,
        request: dypls_20170830_models.UpdateGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.UpdateGroupDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroupDetail',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.UpdateGroupDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_group_detail(
        self,
        request: dypls_20170830_models.UpdateGroupDetailRequest,
    ) -> dypls_20170830_models.UpdateGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_group_detail_with_options(request, runtime)

    async def update_group_detail_async(
        self,
        request: dypls_20170830_models.UpdateGroupDetailRequest,
    ) -> dypls_20170830_models.UpdateGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_group_detail_with_options_async(request, runtime)

    def update_group_info_with_options(
        self,
        request: dypls_20170830_models.UpdateGroupInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.UpdateGroupInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroupInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.UpdateGroupInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_group_info_with_options_async(
        self,
        request: dypls_20170830_models.UpdateGroupInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.UpdateGroupInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_key):
            query['PoolKey'] = request.pool_key
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroupInfo',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.UpdateGroupInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_group_info(
        self,
        request: dypls_20170830_models.UpdateGroupInfoRequest,
    ) -> dypls_20170830_models.UpdateGroupInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_group_info_with_options(request, runtime)

    async def update_group_info_async(
        self,
        request: dypls_20170830_models.UpdateGroupInfoRequest,
    ) -> dypls_20170830_models.UpdateGroupInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_group_info_with_options_async(request, runtime)

    def update_pool_name_with_options(
        self,
        request: dypls_20170830_models.UpdatePoolNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.UpdatePoolNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePoolName',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.UpdatePoolNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pool_name_with_options_async(
        self,
        request: dypls_20170830_models.UpdatePoolNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.UpdatePoolNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePoolName',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.UpdatePoolNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pool_name(
        self,
        request: dypls_20170830_models.UpdatePoolNameRequest,
    ) -> dypls_20170830_models.UpdatePoolNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_pool_name_with_options(request, runtime)

    async def update_pool_name_async(
        self,
        request: dypls_20170830_models.UpdatePoolNameRequest,
    ) -> dypls_20170830_models.UpdatePoolNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_pool_name_with_options_async(request, runtime)

    def update_res_remark_with_options(
        self,
        request: dypls_20170830_models.UpdateResRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.UpdateResRemarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResRemark',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.UpdateResRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_res_remark_with_options_async(
        self,
        request: dypls_20170830_models.UpdateResRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.UpdateResRemarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_id):
            query['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.res_type):
            query['ResType'] = request.res_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_no):
            query['SecretNo'] = request.secret_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResRemark',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.UpdateResRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_res_remark(
        self,
        request: dypls_20170830_models.UpdateResRemarkRequest,
    ) -> dypls_20170830_models.UpdateResRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_res_remark_with_options(request, runtime)

    async def update_res_remark_async(
        self,
        request: dypls_20170830_models.UpdateResRemarkRequest,
    ) -> dypls_20170830_models.UpdateResRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_res_remark_with_options_async(request, runtime)

    def validate_order_with_options(
        self,
        request: dypls_20170830_models.ValidateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.ValidateOrderResponse:
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
            action='ValidateOrder',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ValidateOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_order_with_options_async(
        self,
        request: dypls_20170830_models.ValidateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dypls_20170830_models.ValidateOrderResponse:
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
            action='ValidateOrder',
            version='2017-08-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dypls_20170830_models.ValidateOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_order(
        self,
        request: dypls_20170830_models.ValidateOrderRequest,
    ) -> dypls_20170830_models.ValidateOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.validate_order_with_options(request, runtime)

    async def validate_order_async(
        self,
        request: dypls_20170830_models.ValidateOrderRequest,
    ) -> dypls_20170830_models.ValidateOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.validate_order_with_options_async(request, runtime)
