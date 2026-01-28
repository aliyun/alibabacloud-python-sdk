# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_bailianvoicebot20250101 import models as main_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('bailianvoicebot', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def bridge_web_call_with_options(
        self,
        request: main_models.BridgeWebCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BridgeWebCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.business_unit_id):
            query['BusinessUnitId'] = request.business_unit_id
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.sample_rate):
            query['SampleRate'] = request.sample_rate
        if not DaraCore.is_null(request.sandbox):
            query['Sandbox'] = request.sandbox
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BridgeWebCall',
            version = '2025-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BridgeWebCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def bridge_web_call_with_options_async(
        self,
        request: main_models.BridgeWebCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BridgeWebCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.business_unit_id):
            query['BusinessUnitId'] = request.business_unit_id
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.sample_rate):
            query['SampleRate'] = request.sample_rate
        if not DaraCore.is_null(request.sandbox):
            query['Sandbox'] = request.sandbox
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.timeout_seconds):
            query['TimeoutSeconds'] = request.timeout_seconds
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BridgeWebCall',
            version = '2025-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BridgeWebCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bridge_web_call(
        self,
        request: main_models.BridgeWebCallRequest,
    ) -> main_models.BridgeWebCallResponse:
        runtime = RuntimeOptions()
        return self.bridge_web_call_with_options(request, runtime)

    async def bridge_web_call_async(
        self,
        request: main_models.BridgeWebCallRequest,
    ) -> main_models.BridgeWebCallResponse:
        runtime = RuntimeOptions()
        return await self.bridge_web_call_with_options_async(request, runtime)

    def create_application_with_options(
        self,
        request: main_models.CreateApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_unit_id):
            query['BusinessUnitId'] = request.business_unit_id
        if not DaraCore.is_null(request.concurrency):
            query['Concurrency'] = request.concurrency
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.nlu_access_type):
            query['NluAccessType'] = request.nlu_access_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplication',
            version = '2025-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_with_options_async(
        self,
        request: main_models.CreateApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_unit_id):
            query['BusinessUnitId'] = request.business_unit_id
        if not DaraCore.is_null(request.concurrency):
            query['Concurrency'] = request.concurrency
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.nlu_access_type):
            query['NluAccessType'] = request.nlu_access_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplication',
            version = '2025-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application(
        self,
        request: main_models.CreateApplicationRequest,
    ) -> main_models.CreateApplicationResponse:
        runtime = RuntimeOptions()
        return self.create_application_with_options(request, runtime)

    async def create_application_async(
        self,
        request: main_models.CreateApplicationRequest,
    ) -> main_models.CreateApplicationResponse:
        runtime = RuntimeOptions()
        return await self.create_application_with_options_async(request, runtime)

    def create_application_version_with_options(
        self,
        tmp_req: main_models.CreateApplicationVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationVersionResponse:
        tmp_req.validate()
        request = main_models.CreateApplicationVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.interaction_config):
            request.interaction_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.interaction_config, 'InteractionConfig', 'json')
        if not DaraCore.is_null(tmp_req.script_profile):
            request.script_profile_shrink = Utils.array_to_string_with_specified_style(tmp_req.script_profile, 'ScriptProfile', 'json')
        if not DaraCore.is_null(tmp_req.synthesizer_config):
            request.synthesizer_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.synthesizer_config, 'SynthesizerConfig', 'json')
        if not DaraCore.is_null(tmp_req.transcriber_config):
            request.transcriber_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.transcriber_config, 'TranscriberConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.business_unit_id):
            query['BusinessUnitId'] = request.business_unit_id
        if not DaraCore.is_null(request.interaction_config_shrink):
            query['InteractionConfig'] = request.interaction_config_shrink
        if not DaraCore.is_null(request.script_profile_shrink):
            query['ScriptProfile'] = request.script_profile_shrink
        if not DaraCore.is_null(request.source_version_id):
            query['SourceVersionId'] = request.source_version_id
        if not DaraCore.is_null(request.synthesizer_config_shrink):
            query['SynthesizerConfig'] = request.synthesizer_config_shrink
        if not DaraCore.is_null(request.transcriber_config_shrink):
            query['TranscriberConfig'] = request.transcriber_config_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplicationVersion',
            version = '2025-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_version_with_options_async(
        self,
        tmp_req: main_models.CreateApplicationVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationVersionResponse:
        tmp_req.validate()
        request = main_models.CreateApplicationVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.interaction_config):
            request.interaction_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.interaction_config, 'InteractionConfig', 'json')
        if not DaraCore.is_null(tmp_req.script_profile):
            request.script_profile_shrink = Utils.array_to_string_with_specified_style(tmp_req.script_profile, 'ScriptProfile', 'json')
        if not DaraCore.is_null(tmp_req.synthesizer_config):
            request.synthesizer_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.synthesizer_config, 'SynthesizerConfig', 'json')
        if not DaraCore.is_null(tmp_req.transcriber_config):
            request.transcriber_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.transcriber_config, 'TranscriberConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.business_unit_id):
            query['BusinessUnitId'] = request.business_unit_id
        if not DaraCore.is_null(request.interaction_config_shrink):
            query['InteractionConfig'] = request.interaction_config_shrink
        if not DaraCore.is_null(request.script_profile_shrink):
            query['ScriptProfile'] = request.script_profile_shrink
        if not DaraCore.is_null(request.source_version_id):
            query['SourceVersionId'] = request.source_version_id
        if not DaraCore.is_null(request.synthesizer_config_shrink):
            query['SynthesizerConfig'] = request.synthesizer_config_shrink
        if not DaraCore.is_null(request.transcriber_config_shrink):
            query['TranscriberConfig'] = request.transcriber_config_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplicationVersion',
            version = '2025-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application_version(
        self,
        request: main_models.CreateApplicationVersionRequest,
    ) -> main_models.CreateApplicationVersionResponse:
        runtime = RuntimeOptions()
        return self.create_application_version_with_options(request, runtime)

    async def create_application_version_async(
        self,
        request: main_models.CreateApplicationVersionRequest,
    ) -> main_models.CreateApplicationVersionResponse:
        runtime = RuntimeOptions()
        return await self.create_application_version_with_options_async(request, runtime)

    def delete_application_with_options(
        self,
        request: main_models.DeleteApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.business_unit_id):
            query['BusinessUnitId'] = request.business_unit_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplication',
            version = '2025-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_with_options_async(
        self,
        request: main_models.DeleteApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.business_unit_id):
            query['BusinessUnitId'] = request.business_unit_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplication',
            version = '2025-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application(
        self,
        request: main_models.DeleteApplicationRequest,
    ) -> main_models.DeleteApplicationResponse:
        runtime = RuntimeOptions()
        return self.delete_application_with_options(request, runtime)

    async def delete_application_async(
        self,
        request: main_models.DeleteApplicationRequest,
    ) -> main_models.DeleteApplicationResponse:
        runtime = RuntimeOptions()
        return await self.delete_application_with_options_async(request, runtime)

    def get_application_with_options(
        self,
        request: main_models.GetApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.business_unit_id):
            query['BusinessUnitId'] = request.business_unit_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplication',
            version = '2025-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_with_options_async(
        self,
        request: main_models.GetApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.business_unit_id):
            query['BusinessUnitId'] = request.business_unit_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplication',
            version = '2025-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application(
        self,
        request: main_models.GetApplicationRequest,
    ) -> main_models.GetApplicationResponse:
        runtime = RuntimeOptions()
        return self.get_application_with_options(request, runtime)

    async def get_application_async(
        self,
        request: main_models.GetApplicationRequest,
    ) -> main_models.GetApplicationResponse:
        runtime = RuntimeOptions()
        return await self.get_application_with_options_async(request, runtime)

    def list_applications_with_options(
        self,
        request: main_models.ListApplicationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_unit_id):
            query['BusinessUnitId'] = request.business_unit_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplications',
            version = '2025-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_with_options_async(
        self,
        request: main_models.ListApplicationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_unit_id):
            query['BusinessUnitId'] = request.business_unit_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_pattern):
            query['SearchPattern'] = request.search_pattern
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplications',
            version = '2025-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications(
        self,
        request: main_models.ListApplicationsRequest,
    ) -> main_models.ListApplicationsResponse:
        runtime = RuntimeOptions()
        return self.list_applications_with_options(request, runtime)

    async def list_applications_async(
        self,
        request: main_models.ListApplicationsRequest,
    ) -> main_models.ListApplicationsResponse:
        runtime = RuntimeOptions()
        return await self.list_applications_with_options_async(request, runtime)

    def publish_application_version_with_options(
        self,
        request: main_models.PublishApplicationVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishApplicationVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.business_unit_id):
            query['BusinessUnitId'] = request.business_unit_id
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishApplicationVersion',
            version = '2025-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishApplicationVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_application_version_with_options_async(
        self,
        request: main_models.PublishApplicationVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishApplicationVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.business_unit_id):
            query['BusinessUnitId'] = request.business_unit_id
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishApplicationVersion',
            version = '2025-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishApplicationVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_application_version(
        self,
        request: main_models.PublishApplicationVersionRequest,
    ) -> main_models.PublishApplicationVersionResponse:
        runtime = RuntimeOptions()
        return self.publish_application_version_with_options(request, runtime)

    async def publish_application_version_async(
        self,
        request: main_models.PublishApplicationVersionRequest,
    ) -> main_models.PublishApplicationVersionResponse:
        runtime = RuntimeOptions()
        return await self.publish_application_version_with_options_async(request, runtime)

    def update_application_with_options(
        self,
        request: main_models.UpdateApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.business_unit_id):
            query['BusinessUnitId'] = request.business_unit_id
        if not DaraCore.is_null(request.concurrency):
            query['Concurrency'] = request.concurrency
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplication',
            version = '2025-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_with_options_async(
        self,
        request: main_models.UpdateApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.business_unit_id):
            query['BusinessUnitId'] = request.business_unit_id
        if not DaraCore.is_null(request.concurrency):
            query['Concurrency'] = request.concurrency
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplication',
            version = '2025-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application(
        self,
        request: main_models.UpdateApplicationRequest,
    ) -> main_models.UpdateApplicationResponse:
        runtime = RuntimeOptions()
        return self.update_application_with_options(request, runtime)

    async def update_application_async(
        self,
        request: main_models.UpdateApplicationRequest,
    ) -> main_models.UpdateApplicationResponse:
        runtime = RuntimeOptions()
        return await self.update_application_with_options_async(request, runtime)

    def update_application_version_with_options(
        self,
        tmp_req: main_models.UpdateApplicationVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationVersionResponse:
        tmp_req.validate()
        request = main_models.UpdateApplicationVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.interaction_config):
            request.interaction_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.interaction_config, 'InteractionConfig', 'json')
        if not DaraCore.is_null(tmp_req.script_profile):
            request.script_profile_shrink = Utils.array_to_string_with_specified_style(tmp_req.script_profile, 'ScriptProfile', 'json')
        if not DaraCore.is_null(tmp_req.synthesizer_config):
            request.synthesizer_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.synthesizer_config, 'SynthesizerConfig', 'json')
        if not DaraCore.is_null(tmp_req.transcriber_config):
            request.transcriber_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.transcriber_config, 'TranscriberConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.business_unit_id):
            query['BusinessUnitId'] = request.business_unit_id
        if not DaraCore.is_null(request.interaction_config_shrink):
            query['InteractionConfig'] = request.interaction_config_shrink
        if not DaraCore.is_null(request.script_profile_shrink):
            query['ScriptProfile'] = request.script_profile_shrink
        if not DaraCore.is_null(request.synthesizer_config_shrink):
            query['SynthesizerConfig'] = request.synthesizer_config_shrink
        if not DaraCore.is_null(request.transcriber_config_shrink):
            query['TranscriberConfig'] = request.transcriber_config_shrink
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationVersion',
            version = '2025-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_version_with_options_async(
        self,
        tmp_req: main_models.UpdateApplicationVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationVersionResponse:
        tmp_req.validate()
        request = main_models.UpdateApplicationVersionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.interaction_config):
            request.interaction_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.interaction_config, 'InteractionConfig', 'json')
        if not DaraCore.is_null(tmp_req.script_profile):
            request.script_profile_shrink = Utils.array_to_string_with_specified_style(tmp_req.script_profile, 'ScriptProfile', 'json')
        if not DaraCore.is_null(tmp_req.synthesizer_config):
            request.synthesizer_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.synthesizer_config, 'SynthesizerConfig', 'json')
        if not DaraCore.is_null(tmp_req.transcriber_config):
            request.transcriber_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.transcriber_config, 'TranscriberConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.business_unit_id):
            query['BusinessUnitId'] = request.business_unit_id
        if not DaraCore.is_null(request.interaction_config_shrink):
            query['InteractionConfig'] = request.interaction_config_shrink
        if not DaraCore.is_null(request.script_profile_shrink):
            query['ScriptProfile'] = request.script_profile_shrink
        if not DaraCore.is_null(request.synthesizer_config_shrink):
            query['SynthesizerConfig'] = request.synthesizer_config_shrink
        if not DaraCore.is_null(request.transcriber_config_shrink):
            query['TranscriberConfig'] = request.transcriber_config_shrink
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationVersion',
            version = '2025-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_version(
        self,
        request: main_models.UpdateApplicationVersionRequest,
    ) -> main_models.UpdateApplicationVersionResponse:
        runtime = RuntimeOptions()
        return self.update_application_version_with_options(request, runtime)

    async def update_application_version_async(
        self,
        request: main_models.UpdateApplicationVersionRequest,
    ) -> main_models.UpdateApplicationVersionResponse:
        runtime = RuntimeOptions()
        return await self.update_application_version_with_options_async(request, runtime)
