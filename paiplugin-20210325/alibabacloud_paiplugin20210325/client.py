# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_paiplugin20210325 import models as pai_plugin_20210325_models
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
        self._endpoint = self.get_endpoint('paiplugin', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_signature(
        self,
        request: pai_plugin_20210325_models.CreateSignatureRequest,
    ) -> pai_plugin_20210325_models.CreateSignatureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_signature_with_options(request, headers, runtime)

    async def create_signature_async(
        self,
        request: pai_plugin_20210325_models.CreateSignatureRequest,
    ) -> pai_plugin_20210325_models.CreateSignatureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_signature_with_options_async(request, headers, runtime)

    def create_signature_with_options(
        self,
        request: pai_plugin_20210325_models.CreateSignatureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20210325_models.CreateSignatureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.certificates):
            body['Certificates'] = request.certificates
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.power_of_attorney):
            body['PowerOfAttorney'] = request.power_of_attorney
        if not UtilClient.is_unset(request.process_instance_id):
            body['ProcessInstanceID'] = request.process_instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_plugin_20210325_models.CreateSignatureResponse(),
            self.do_roarequest('CreateSignature', '2021-03-25', 'HTTPS', 'POST', 'AK', f'/api/v1/signatures', 'json', req, runtime)
        )

    async def create_signature_with_options_async(
        self,
        request: pai_plugin_20210325_models.CreateSignatureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20210325_models.CreateSignatureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.certificates):
            body['Certificates'] = request.certificates
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.power_of_attorney):
            body['PowerOfAttorney'] = request.power_of_attorney
        if not UtilClient.is_unset(request.process_instance_id):
            body['ProcessInstanceID'] = request.process_instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_plugin_20210325_models.CreateSignatureResponse(),
            await self.do_roarequest_async('CreateSignature', '2021-03-25', 'HTTPS', 'POST', 'AK', f'/api/v1/signatures', 'json', req, runtime)
        )

    def delete_template(
        self,
        id: str,
    ) -> pai_plugin_20210325_models.DeleteTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_template_with_options(id, headers, runtime)

    async def delete_template_async(
        self,
        id: str,
    ) -> pai_plugin_20210325_models.DeleteTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_template_with_options_async(id, headers, runtime)

    def delete_template_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20210325_models.DeleteTemplateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_plugin_20210325_models.DeleteTemplateResponse(),
            self.do_roarequest('DeleteTemplate', '2021-03-25', 'HTTPS', 'DELETE', 'AK', f'/api/v1/templates/{id}', 'json', req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20210325_models.DeleteTemplateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_plugin_20210325_models.DeleteTemplateResponse(),
            await self.do_roarequest_async('DeleteTemplate', '2021-03-25', 'HTTPS', 'DELETE', 'AK', f'/api/v1/templates/{id}', 'json', req, runtime)
        )

    def create_template(
        self,
        request: pai_plugin_20210325_models.CreateTemplateRequest,
    ) -> pai_plugin_20210325_models.CreateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_template_with_options(request, headers, runtime)

    async def create_template_async(
        self,
        request: pai_plugin_20210325_models.CreateTemplateRequest,
    ) -> pai_plugin_20210325_models.CreateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_template_with_options_async(request, headers, runtime)

    def create_template_with_options(
        self,
        request: pai_plugin_20210325_models.CreateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20210325_models.CreateTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.process_instance_id):
            body['ProcessInstanceID'] = request.process_instance_id
        if not UtilClient.is_unset(request.signature_id):
            body['SignatureID'] = request.signature_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_plugin_20210325_models.CreateTemplateResponse(),
            self.do_roarequest('CreateTemplate', '2021-03-25', 'HTTPS', 'POST', 'AK', f'/api/v1/templates', 'json', req, runtime)
        )

    async def create_template_with_options_async(
        self,
        request: pai_plugin_20210325_models.CreateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20210325_models.CreateTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.process_instance_id):
            body['ProcessInstanceID'] = request.process_instance_id
        if not UtilClient.is_unset(request.signature_id):
            body['SignatureID'] = request.signature_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_plugin_20210325_models.CreateTemplateResponse(),
            await self.do_roarequest_async('CreateTemplate', '2021-03-25', 'HTTPS', 'POST', 'AK', f'/api/v1/templates', 'json', req, runtime)
        )

    def list_templates(
        self,
        request: pai_plugin_20210325_models.ListTemplatesRequest,
    ) -> pai_plugin_20210325_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_templates_with_options(request, headers, runtime)

    async def list_templates_async(
        self,
        request: pai_plugin_20210325_models.ListTemplatesRequest,
    ) -> pai_plugin_20210325_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_templates_with_options_async(request, headers, runtime)

    def list_templates_with_options(
        self,
        request: pai_plugin_20210325_models.ListTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20210325_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_plugin_20210325_models.ListTemplatesResponse(),
            self.do_roarequest('ListTemplates', '2021-03-25', 'HTTPS', 'GET', 'AK', f'/api/v1/templates', 'json', req, runtime)
        )

    async def list_templates_with_options_async(
        self,
        request: pai_plugin_20210325_models.ListTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20210325_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_plugin_20210325_models.ListTemplatesResponse(),
            await self.do_roarequest_async('ListTemplates', '2021-03-25', 'HTTPS', 'GET', 'AK', f'/api/v1/templates', 'json', req, runtime)
        )

    def delete_schedule(
        self,
        id: str,
    ) -> pai_plugin_20210325_models.DeleteScheduleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_schedule_with_options(id, headers, runtime)

    async def delete_schedule_async(
        self,
        id: str,
    ) -> pai_plugin_20210325_models.DeleteScheduleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_schedule_with_options_async(id, headers, runtime)

    def delete_schedule_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20210325_models.DeleteScheduleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_plugin_20210325_models.DeleteScheduleResponse(),
            self.do_roarequest('DeleteSchedule', '2021-03-25', 'HTTPS', 'DELETE', 'AK', f'/api/v1/schedules/{id}', 'json', req, runtime)
        )

    async def delete_schedule_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20210325_models.DeleteScheduleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_plugin_20210325_models.DeleteScheduleResponse(),
            await self.do_roarequest_async('DeleteSchedule', '2021-03-25', 'HTTPS', 'DELETE', 'AK', f'/api/v1/schedules/{id}', 'json', req, runtime)
        )

    def get_template(
        self,
        id: str,
    ) -> pai_plugin_20210325_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_template_with_options(id, headers, runtime)

    async def get_template_async(
        self,
        id: str,
    ) -> pai_plugin_20210325_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_template_with_options_async(id, headers, runtime)

    def get_template_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20210325_models.GetTemplateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_plugin_20210325_models.GetTemplateResponse(),
            self.do_roarequest('GetTemplate', '2021-03-25', 'HTTPS', 'GET', 'AK', f'/api/v1/templates/{id}', 'json', req, runtime)
        )

    async def get_template_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20210325_models.GetTemplateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_plugin_20210325_models.GetTemplateResponse(),
            await self.do_roarequest_async('GetTemplate', '2021-03-25', 'HTTPS', 'GET', 'AK', f'/api/v1/templates/{id}', 'json', req, runtime)
        )

    def list_signatures(
        self,
        request: pai_plugin_20210325_models.ListSignaturesRequest,
    ) -> pai_plugin_20210325_models.ListSignaturesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_signatures_with_options(request, headers, runtime)

    async def list_signatures_async(
        self,
        request: pai_plugin_20210325_models.ListSignaturesRequest,
    ) -> pai_plugin_20210325_models.ListSignaturesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_signatures_with_options_async(request, headers, runtime)

    def list_signatures_with_options(
        self,
        request: pai_plugin_20210325_models.ListSignaturesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20210325_models.ListSignaturesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_plugin_20210325_models.ListSignaturesResponse(),
            self.do_roarequest('ListSignatures', '2021-03-25', 'HTTPS', 'GET', 'AK', f'/api/v1/signatures', 'json', req, runtime)
        )

    async def list_signatures_with_options_async(
        self,
        request: pai_plugin_20210325_models.ListSignaturesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20210325_models.ListSignaturesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_plugin_20210325_models.ListSignaturesResponse(),
            await self.do_roarequest_async('ListSignatures', '2021-03-25', 'HTTPS', 'GET', 'AK', f'/api/v1/signatures', 'json', req, runtime)
        )

    def get_signature(
        self,
        id: str,
    ) -> pai_plugin_20210325_models.GetSignatureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_signature_with_options(id, headers, runtime)

    async def get_signature_async(
        self,
        id: str,
    ) -> pai_plugin_20210325_models.GetSignatureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_signature_with_options_async(id, headers, runtime)

    def get_signature_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20210325_models.GetSignatureResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_plugin_20210325_models.GetSignatureResponse(),
            self.do_roarequest('GetSignature', '2021-03-25', 'HTTPS', 'GET', 'AK', f'/api/v1/signatures/{id}', 'json', req, runtime)
        )

    async def get_signature_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20210325_models.GetSignatureResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_plugin_20210325_models.GetSignatureResponse(),
            await self.do_roarequest_async('GetSignature', '2021-03-25', 'HTTPS', 'GET', 'AK', f'/api/v1/signatures/{id}', 'json', req, runtime)
        )

    def create_schedule(
        self,
        request: pai_plugin_20210325_models.CreateScheduleRequest,
    ) -> pai_plugin_20210325_models.CreateScheduleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_schedule_with_options(request, headers, runtime)

    async def create_schedule_async(
        self,
        request: pai_plugin_20210325_models.CreateScheduleRequest,
    ) -> pai_plugin_20210325_models.CreateScheduleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_schedule_with_options_async(request, headers, runtime)

    def create_schedule_with_options(
        self,
        request: pai_plugin_20210325_models.CreateScheduleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20210325_models.CreateScheduleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_address):
            body['DataAddress'] = request.data_address
        if not UtilClient.is_unset(request.data_source):
            body['DataSource'] = request.data_source
        if not UtilClient.is_unset(request.ding_bot_keyword):
            body['DingBotKeyword'] = request.ding_bot_keyword
        if not UtilClient.is_unset(request.ding_bot_token):
            body['DingBotToken'] = request.ding_bot_token
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.partition):
            body['Partition'] = request.partition
        if not UtilClient.is_unset(request.phone_number_column):
            body['PhoneNumberColumn'] = request.phone_number_column
        if not UtilClient.is_unset(request.send_time):
            body['SendTime'] = request.send_time
        if not UtilClient.is_unset(request.signature_id):
            body['SignatureID'] = request.signature_id
        if not UtilClient.is_unset(request.template_code_column):
            body['TemplateCodeColumn'] = request.template_code_column
        if not UtilClient.is_unset(request.template_id):
            body['TemplateID'] = request.template_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_plugin_20210325_models.CreateScheduleResponse(),
            self.do_roarequest('CreateSchedule', '2021-03-25', 'HTTPS', 'POST', 'AK', f'/api/v1/schedules', 'json', req, runtime)
        )

    async def create_schedule_with_options_async(
        self,
        request: pai_plugin_20210325_models.CreateScheduleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20210325_models.CreateScheduleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_address):
            body['DataAddress'] = request.data_address
        if not UtilClient.is_unset(request.data_source):
            body['DataSource'] = request.data_source
        if not UtilClient.is_unset(request.ding_bot_keyword):
            body['DingBotKeyword'] = request.ding_bot_keyword
        if not UtilClient.is_unset(request.ding_bot_token):
            body['DingBotToken'] = request.ding_bot_token
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.partition):
            body['Partition'] = request.partition
        if not UtilClient.is_unset(request.phone_number_column):
            body['PhoneNumberColumn'] = request.phone_number_column
        if not UtilClient.is_unset(request.send_time):
            body['SendTime'] = request.send_time
        if not UtilClient.is_unset(request.signature_id):
            body['SignatureID'] = request.signature_id
        if not UtilClient.is_unset(request.template_code_column):
            body['TemplateCodeColumn'] = request.template_code_column
        if not UtilClient.is_unset(request.template_id):
            body['TemplateID'] = request.template_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_plugin_20210325_models.CreateScheduleResponse(),
            await self.do_roarequest_async('CreateSchedule', '2021-03-25', 'HTTPS', 'POST', 'AK', f'/api/v1/schedules', 'json', req, runtime)
        )

    def list_schedules(
        self,
        request: pai_plugin_20210325_models.ListSchedulesRequest,
    ) -> pai_plugin_20210325_models.ListSchedulesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_schedules_with_options(request, headers, runtime)

    async def list_schedules_async(
        self,
        request: pai_plugin_20210325_models.ListSchedulesRequest,
    ) -> pai_plugin_20210325_models.ListSchedulesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_schedules_with_options_async(request, headers, runtime)

    def list_schedules_with_options(
        self,
        request: pai_plugin_20210325_models.ListSchedulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20210325_models.ListSchedulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_plugin_20210325_models.ListSchedulesResponse(),
            self.do_roarequest('ListSchedules', '2021-03-25', 'HTTPS', 'GET', 'AK', f'/api/v1/schedules', 'json', req, runtime)
        )

    async def list_schedules_with_options_async(
        self,
        request: pai_plugin_20210325_models.ListSchedulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20210325_models.ListSchedulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_plugin_20210325_models.ListSchedulesResponse(),
            await self.do_roarequest_async('ListSchedules', '2021-03-25', 'HTTPS', 'GET', 'AK', f'/api/v1/schedules', 'json', req, runtime)
        )

    def delete_signature(
        self,
        id: str,
    ) -> pai_plugin_20210325_models.DeleteSignatureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_signature_with_options(id, headers, runtime)

    async def delete_signature_async(
        self,
        id: str,
    ) -> pai_plugin_20210325_models.DeleteSignatureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_signature_with_options_async(id, headers, runtime)

    def delete_signature_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20210325_models.DeleteSignatureResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_plugin_20210325_models.DeleteSignatureResponse(),
            self.do_roarequest('DeleteSignature', '2021-03-25', 'HTTPS', 'DELETE', 'AK', f'/api/v1/signatures/{id}', 'json', req, runtime)
        )

    async def delete_signature_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_plugin_20210325_models.DeleteSignatureResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_plugin_20210325_models.DeleteSignatureResponse(),
            await self.do_roarequest_async('DeleteSignature', '2021-03-25', 'HTTPS', 'DELETE', 'AK', f'/api/v1/signatures/{id}', 'json', req, runtime)
        )
