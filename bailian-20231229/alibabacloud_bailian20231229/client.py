# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_bailian20231229 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

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
        self._endpoint = self.get_endpoint('bailian', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_category_with_options(
        self,
        workspace_id: str,
        request: main_models.AddCategoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddCategoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_name):
            body['CategoryName'] = request.category_name
        if not DaraCore.is_null(request.category_type):
            body['CategoryType'] = request.category_type
        if not DaraCore.is_null(request.parent_category_id):
            body['ParentCategoryId'] = request.parent_category_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddCategory',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/category/',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_category_with_options_async(
        self,
        workspace_id: str,
        request: main_models.AddCategoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddCategoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_name):
            body['CategoryName'] = request.category_name
        if not DaraCore.is_null(request.category_type):
            body['CategoryType'] = request.category_type
        if not DaraCore.is_null(request.parent_category_id):
            body['ParentCategoryId'] = request.parent_category_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddCategory',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/category/',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_category(
        self,
        workspace_id: str,
        request: main_models.AddCategoryRequest,
    ) -> main_models.AddCategoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_category_with_options(workspace_id, request, headers, runtime)

    async def add_category_async(
        self,
        workspace_id: str,
        request: main_models.AddCategoryRequest,
    ) -> main_models.AddCategoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_category_with_options_async(workspace_id, request, headers, runtime)

    def add_file_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.AddFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddFileResponse:
        tmp_req.validate()
        request = main_models.AddFileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.category_type):
            body['CategoryType'] = request.category_type
        if not DaraCore.is_null(request.lease_id):
            body['LeaseId'] = request.lease_id
        if not DaraCore.is_null(request.original_file_url):
            body['OriginalFileUrl'] = request.original_file_url
        if not DaraCore.is_null(request.parser):
            body['Parser'] = request.parser
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddFile',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/file',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_file_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.AddFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddFileResponse:
        tmp_req.validate()
        request = main_models.AddFileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.category_type):
            body['CategoryType'] = request.category_type
        if not DaraCore.is_null(request.lease_id):
            body['LeaseId'] = request.lease_id
        if not DaraCore.is_null(request.original_file_url):
            body['OriginalFileUrl'] = request.original_file_url
        if not DaraCore.is_null(request.parser):
            body['Parser'] = request.parser
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddFile',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/file',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_file(
        self,
        workspace_id: str,
        request: main_models.AddFileRequest,
    ) -> main_models.AddFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_file_with_options(workspace_id, request, headers, runtime)

    async def add_file_async(
        self,
        workspace_id: str,
        request: main_models.AddFileRequest,
    ) -> main_models.AddFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_file_with_options_async(workspace_id, request, headers, runtime)

    def add_files_from_authorized_oss_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.AddFilesFromAuthorizedOssRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddFilesFromAuthorizedOssResponse:
        tmp_req.validate()
        request = main_models.AddFilesFromAuthorizedOssShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.file_details):
            request.file_details_shrink = Utils.array_to_string_with_specified_style(tmp_req.file_details, 'FileDetails', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.category_type):
            body['CategoryType'] = request.category_type
        if not DaraCore.is_null(request.file_details_shrink):
            body['FileDetails'] = request.file_details_shrink
        if not DaraCore.is_null(request.oss_bucket_name):
            body['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.oss_region_id):
            body['OssRegionId'] = request.oss_region_id
        if not DaraCore.is_null(request.over_write_file_by_oss_key):
            body['OverWriteFileByOssKey'] = request.over_write_file_by_oss_key
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddFilesFromAuthorizedOss',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/file/fromoss',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFilesFromAuthorizedOssResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_files_from_authorized_oss_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.AddFilesFromAuthorizedOssRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddFilesFromAuthorizedOssResponse:
        tmp_req.validate()
        request = main_models.AddFilesFromAuthorizedOssShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.file_details):
            request.file_details_shrink = Utils.array_to_string_with_specified_style(tmp_req.file_details, 'FileDetails', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.category_type):
            body['CategoryType'] = request.category_type
        if not DaraCore.is_null(request.file_details_shrink):
            body['FileDetails'] = request.file_details_shrink
        if not DaraCore.is_null(request.oss_bucket_name):
            body['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.oss_region_id):
            body['OssRegionId'] = request.oss_region_id
        if not DaraCore.is_null(request.over_write_file_by_oss_key):
            body['OverWriteFileByOssKey'] = request.over_write_file_by_oss_key
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddFilesFromAuthorizedOss',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/file/fromoss',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddFilesFromAuthorizedOssResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_files_from_authorized_oss(
        self,
        workspace_id: str,
        request: main_models.AddFilesFromAuthorizedOssRequest,
    ) -> main_models.AddFilesFromAuthorizedOssResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_files_from_authorized_oss_with_options(workspace_id, request, headers, runtime)

    async def add_files_from_authorized_oss_async(
        self,
        workspace_id: str,
        request: main_models.AddFilesFromAuthorizedOssRequest,
    ) -> main_models.AddFilesFromAuthorizedOssResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_files_from_authorized_oss_with_options_async(workspace_id, request, headers, runtime)

    def apply_file_upload_lease_with_options(
        self,
        category_id: str,
        workspace_id: str,
        request: main_models.ApplyFileUploadLeaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ApplyFileUploadLeaseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_type):
            body['CategoryType'] = request.category_type
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.md_5):
            body['Md5'] = request.md_5
        if not DaraCore.is_null(request.size_in_bytes):
            body['SizeInBytes'] = request.size_in_bytes
        if not DaraCore.is_null(request.use_internal_endpoint):
            body['UseInternalEndpoint'] = request.use_internal_endpoint
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ApplyFileUploadLease',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/category/{DaraURL.percent_encode(category_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyFileUploadLeaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_file_upload_lease_with_options_async(
        self,
        category_id: str,
        workspace_id: str,
        request: main_models.ApplyFileUploadLeaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ApplyFileUploadLeaseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_type):
            body['CategoryType'] = request.category_type
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.md_5):
            body['Md5'] = request.md_5
        if not DaraCore.is_null(request.size_in_bytes):
            body['SizeInBytes'] = request.size_in_bytes
        if not DaraCore.is_null(request.use_internal_endpoint):
            body['UseInternalEndpoint'] = request.use_internal_endpoint
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ApplyFileUploadLease',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/category/{DaraURL.percent_encode(category_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyFileUploadLeaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_file_upload_lease(
        self,
        category_id: str,
        workspace_id: str,
        request: main_models.ApplyFileUploadLeaseRequest,
    ) -> main_models.ApplyFileUploadLeaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.apply_file_upload_lease_with_options(category_id, workspace_id, request, headers, runtime)

    async def apply_file_upload_lease_async(
        self,
        category_id: str,
        workspace_id: str,
        request: main_models.ApplyFileUploadLeaseRequest,
    ) -> main_models.ApplyFileUploadLeaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.apply_file_upload_lease_with_options_async(category_id, workspace_id, request, headers, runtime)

    def apply_temp_storage_lease_with_options(
        self,
        workspace_id: str,
        request: main_models.ApplyTempStorageLeaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ApplyTempStorageLeaseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.size_in_bytes):
            body['SizeInBytes'] = request.size_in_bytes
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ApplyTempStorageLease',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyTempStorageLeaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_temp_storage_lease_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ApplyTempStorageLeaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ApplyTempStorageLeaseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.size_in_bytes):
            body['SizeInBytes'] = request.size_in_bytes
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ApplyTempStorageLease',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyTempStorageLeaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_temp_storage_lease(
        self,
        workspace_id: str,
        request: main_models.ApplyTempStorageLeaseRequest,
    ) -> main_models.ApplyTempStorageLeaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.apply_temp_storage_lease_with_options(workspace_id, request, headers, runtime)

    async def apply_temp_storage_lease_async(
        self,
        workspace_id: str,
        request: main_models.ApplyTempStorageLeaseRequest,
    ) -> main_models.ApplyTempStorageLeaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.apply_temp_storage_lease_with_options_async(workspace_id, request, headers, runtime)

    def change_parse_setting_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.ChangeParseSettingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeParseSettingResponse:
        tmp_req.validate()
        request = main_models.ChangeParseSettingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parser_config):
            request.parser_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.parser_config, 'ParserConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.file_type):
            body['FileType'] = request.file_type
        if not DaraCore.is_null(request.parser):
            body['Parser'] = request.parser
        if not DaraCore.is_null(request.parser_config_shrink):
            body['ParserConfig'] = request.parser_config_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeParseSetting',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/parser/settings',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeParseSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_parse_setting_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.ChangeParseSettingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeParseSettingResponse:
        tmp_req.validate()
        request = main_models.ChangeParseSettingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parser_config):
            request.parser_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.parser_config, 'ParserConfig', 'json')
        body = {}
        if not DaraCore.is_null(request.category_id):
            body['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.file_type):
            body['FileType'] = request.file_type
        if not DaraCore.is_null(request.parser):
            body['Parser'] = request.parser
        if not DaraCore.is_null(request.parser_config_shrink):
            body['ParserConfig'] = request.parser_config_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeParseSetting',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/parser/settings',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeParseSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_parse_setting(
        self,
        workspace_id: str,
        request: main_models.ChangeParseSettingRequest,
    ) -> main_models.ChangeParseSettingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.change_parse_setting_with_options(workspace_id, request, headers, runtime)

    async def change_parse_setting_async(
        self,
        workspace_id: str,
        request: main_models.ChangeParseSettingRequest,
    ) -> main_models.ChangeParseSettingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.change_parse_setting_with_options_async(workspace_id, request, headers, runtime)

    def create_and_pulish_agent_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateAndPulishAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAndPulishAgentResponse:
        tmp_req.validate()
        request = main_models.CreateAndPulishAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.application_config):
            request.application_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.application_config, 'applicationConfig', 'json')
        if not DaraCore.is_null(tmp_req.sample_library):
            request.sample_library_shrink = Utils.array_to_string_with_specified_style(tmp_req.sample_library, 'sampleLibrary', 'json')
        body = {}
        if not DaraCore.is_null(request.application_config_shrink):
            body['applicationConfig'] = request.application_config_shrink
        if not DaraCore.is_null(request.instructions):
            body['instructions'] = request.instructions
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.sample_library_shrink):
            body['sampleLibrary'] = request.sample_library_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAndPulishAgent',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/application/agents',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAndPulishAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_and_pulish_agent_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateAndPulishAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAndPulishAgentResponse:
        tmp_req.validate()
        request = main_models.CreateAndPulishAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.application_config):
            request.application_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.application_config, 'applicationConfig', 'json')
        if not DaraCore.is_null(tmp_req.sample_library):
            request.sample_library_shrink = Utils.array_to_string_with_specified_style(tmp_req.sample_library, 'sampleLibrary', 'json')
        body = {}
        if not DaraCore.is_null(request.application_config_shrink):
            body['applicationConfig'] = request.application_config_shrink
        if not DaraCore.is_null(request.instructions):
            body['instructions'] = request.instructions
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.sample_library_shrink):
            body['sampleLibrary'] = request.sample_library_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAndPulishAgent',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/application/agents',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAndPulishAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_and_pulish_agent(
        self,
        workspace_id: str,
        request: main_models.CreateAndPulishAgentRequest,
    ) -> main_models.CreateAndPulishAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_and_pulish_agent_with_options(workspace_id, request, headers, runtime)

    async def create_and_pulish_agent_async(
        self,
        workspace_id: str,
        request: main_models.CreateAndPulishAgentRequest,
    ) -> main_models.CreateAndPulishAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_and_pulish_agent_with_options_async(workspace_id, request, headers, runtime)

    def create_index_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateIndexRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIndexResponse:
        tmp_req.validate()
        request = main_models.CreateIndexShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.category_ids):
            request.category_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.category_ids, 'CategoryIds', 'json')
        if not DaraCore.is_null(tmp_req.columns):
            request.columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.columns, 'Columns', 'json')
        if not DaraCore.is_null(tmp_req.data_source):
            request.data_source_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_source, 'DataSource', 'json')
        if not DaraCore.is_null(tmp_req.document_ids):
            request.document_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.document_ids, 'DocumentIds', 'json')
        if not DaraCore.is_null(tmp_req.table_ids):
            request.table_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.table_ids, 'TableIds', 'json')
        if not DaraCore.is_null(tmp_req.meta_extract_columns):
            request.meta_extract_columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.meta_extract_columns, 'metaExtractColumns', 'json')
        query = {}
        if not DaraCore.is_null(request.category_ids_shrink):
            query['CategoryIds'] = request.category_ids_shrink
        if not DaraCore.is_null(request.chunk_size):
            query['ChunkSize'] = request.chunk_size
        if not DaraCore.is_null(request.columns_shrink):
            query['Columns'] = request.columns_shrink
        if not DaraCore.is_null(request.create_index_type):
            query['CreateIndexType'] = request.create_index_type
        if not DaraCore.is_null(request.data_source_shrink):
            query['DataSource'] = request.data_source_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.document_ids_shrink):
            query['DocumentIds'] = request.document_ids_shrink
        if not DaraCore.is_null(request.embedding_model_name):
            query['EmbeddingModelName'] = request.embedding_model_name
        if not DaraCore.is_null(request.enable_rewrite):
            query['EnableRewrite'] = request.enable_rewrite
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.overlap_size):
            query['OverlapSize'] = request.overlap_size
        if not DaraCore.is_null(request.rerank_min_score):
            query['RerankMinScore'] = request.rerank_min_score
        if not DaraCore.is_null(request.rerank_model_name):
            query['RerankModelName'] = request.rerank_model_name
        if not DaraCore.is_null(request.separator):
            query['Separator'] = request.separator
        if not DaraCore.is_null(request.sink_instance_id):
            query['SinkInstanceId'] = request.sink_instance_id
        if not DaraCore.is_null(request.sink_region):
            query['SinkRegion'] = request.sink_region
        if not DaraCore.is_null(request.sink_type):
            query['SinkType'] = request.sink_type
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.structure_type):
            query['StructureType'] = request.structure_type
        if not DaraCore.is_null(request.table_ids_shrink):
            query['TableIds'] = request.table_ids_shrink
        if not DaraCore.is_null(request.chunk_mode):
            query['chunkMode'] = request.chunk_mode
        if not DaraCore.is_null(request.enable_headers):
            query['enableHeaders'] = request.enable_headers
        if not DaraCore.is_null(request.meta_extract_columns_shrink):
            query['metaExtractColumns'] = request.meta_extract_columns_shrink
        if not DaraCore.is_null(request.pipeline_commercial_cu):
            query['pipelineCommercialCu'] = request.pipeline_commercial_cu
        if not DaraCore.is_null(request.pipeline_commercial_type):
            query['pipelineCommercialType'] = request.pipeline_commercial_type
        if not DaraCore.is_null(request.pipeline_retrieve_rate_limit_strategy):
            query['pipelineRetrieveRateLimitStrategy'] = request.pipeline_retrieve_rate_limit_strategy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIndex',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/index/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_index_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.CreateIndexRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIndexResponse:
        tmp_req.validate()
        request = main_models.CreateIndexShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.category_ids):
            request.category_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.category_ids, 'CategoryIds', 'json')
        if not DaraCore.is_null(tmp_req.columns):
            request.columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.columns, 'Columns', 'json')
        if not DaraCore.is_null(tmp_req.data_source):
            request.data_source_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_source, 'DataSource', 'json')
        if not DaraCore.is_null(tmp_req.document_ids):
            request.document_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.document_ids, 'DocumentIds', 'json')
        if not DaraCore.is_null(tmp_req.table_ids):
            request.table_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.table_ids, 'TableIds', 'json')
        if not DaraCore.is_null(tmp_req.meta_extract_columns):
            request.meta_extract_columns_shrink = Utils.array_to_string_with_specified_style(tmp_req.meta_extract_columns, 'metaExtractColumns', 'json')
        query = {}
        if not DaraCore.is_null(request.category_ids_shrink):
            query['CategoryIds'] = request.category_ids_shrink
        if not DaraCore.is_null(request.chunk_size):
            query['ChunkSize'] = request.chunk_size
        if not DaraCore.is_null(request.columns_shrink):
            query['Columns'] = request.columns_shrink
        if not DaraCore.is_null(request.create_index_type):
            query['CreateIndexType'] = request.create_index_type
        if not DaraCore.is_null(request.data_source_shrink):
            query['DataSource'] = request.data_source_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.document_ids_shrink):
            query['DocumentIds'] = request.document_ids_shrink
        if not DaraCore.is_null(request.embedding_model_name):
            query['EmbeddingModelName'] = request.embedding_model_name
        if not DaraCore.is_null(request.enable_rewrite):
            query['EnableRewrite'] = request.enable_rewrite
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.overlap_size):
            query['OverlapSize'] = request.overlap_size
        if not DaraCore.is_null(request.rerank_min_score):
            query['RerankMinScore'] = request.rerank_min_score
        if not DaraCore.is_null(request.rerank_model_name):
            query['RerankModelName'] = request.rerank_model_name
        if not DaraCore.is_null(request.separator):
            query['Separator'] = request.separator
        if not DaraCore.is_null(request.sink_instance_id):
            query['SinkInstanceId'] = request.sink_instance_id
        if not DaraCore.is_null(request.sink_region):
            query['SinkRegion'] = request.sink_region
        if not DaraCore.is_null(request.sink_type):
            query['SinkType'] = request.sink_type
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.structure_type):
            query['StructureType'] = request.structure_type
        if not DaraCore.is_null(request.table_ids_shrink):
            query['TableIds'] = request.table_ids_shrink
        if not DaraCore.is_null(request.chunk_mode):
            query['chunkMode'] = request.chunk_mode
        if not DaraCore.is_null(request.enable_headers):
            query['enableHeaders'] = request.enable_headers
        if not DaraCore.is_null(request.meta_extract_columns_shrink):
            query['metaExtractColumns'] = request.meta_extract_columns_shrink
        if not DaraCore.is_null(request.pipeline_commercial_cu):
            query['pipelineCommercialCu'] = request.pipeline_commercial_cu
        if not DaraCore.is_null(request.pipeline_commercial_type):
            query['pipelineCommercialType'] = request.pipeline_commercial_type
        if not DaraCore.is_null(request.pipeline_retrieve_rate_limit_strategy):
            query['pipelineRetrieveRateLimitStrategy'] = request.pipeline_retrieve_rate_limit_strategy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIndex',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/index/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_index(
        self,
        workspace_id: str,
        request: main_models.CreateIndexRequest,
    ) -> main_models.CreateIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_index_with_options(workspace_id, request, headers, runtime)

    async def create_index_async(
        self,
        workspace_id: str,
        request: main_models.CreateIndexRequest,
    ) -> main_models.CreateIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_index_with_options_async(workspace_id, request, headers, runtime)

    def create_memory_with_options(
        self,
        workspace_id: str,
        request: main_models.CreateMemoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMemoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMemory',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/memories',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMemoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_memory_with_options_async(
        self,
        workspace_id: str,
        request: main_models.CreateMemoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMemoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMemory',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/memories',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMemoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_memory(
        self,
        workspace_id: str,
        request: main_models.CreateMemoryRequest,
    ) -> main_models.CreateMemoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_memory_with_options(workspace_id, request, headers, runtime)

    async def create_memory_async(
        self,
        workspace_id: str,
        request: main_models.CreateMemoryRequest,
    ) -> main_models.CreateMemoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_memory_with_options_async(workspace_id, request, headers, runtime)

    def create_memory_node_with_options(
        self,
        workspace_id: str,
        memory_id: str,
        request: main_models.CreateMemoryNodeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMemoryNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['content'] = request.content
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMemoryNode',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/memories/{DaraURL.percent_encode(memory_id)}/memoryNodes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMemoryNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_memory_node_with_options_async(
        self,
        workspace_id: str,
        memory_id: str,
        request: main_models.CreateMemoryNodeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMemoryNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['content'] = request.content
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMemoryNode',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/memories/{DaraURL.percent_encode(memory_id)}/memoryNodes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMemoryNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_memory_node(
        self,
        workspace_id: str,
        memory_id: str,
        request: main_models.CreateMemoryNodeRequest,
    ) -> main_models.CreateMemoryNodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_memory_node_with_options(workspace_id, memory_id, request, headers, runtime)

    async def create_memory_node_async(
        self,
        workspace_id: str,
        memory_id: str,
        request: main_models.CreateMemoryNodeRequest,
    ) -> main_models.CreateMemoryNodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_memory_node_with_options_async(workspace_id, memory_id, request, headers, runtime)

    def create_prompt_template_with_options(
        self,
        workspace_id: str,
        request: main_models.CreatePromptTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePromptTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['content'] = request.content
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePromptTemplate',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/promptTemplates',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePromptTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_prompt_template_with_options_async(
        self,
        workspace_id: str,
        request: main_models.CreatePromptTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePromptTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['content'] = request.content
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePromptTemplate',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/promptTemplates',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePromptTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_prompt_template(
        self,
        workspace_id: str,
        request: main_models.CreatePromptTemplateRequest,
    ) -> main_models.CreatePromptTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_prompt_template_with_options(workspace_id, request, headers, runtime)

    async def create_prompt_template_async(
        self,
        workspace_id: str,
        request: main_models.CreatePromptTemplateRequest,
    ) -> main_models.CreatePromptTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_prompt_template_with_options_async(workspace_id, request, headers, runtime)

    def delete_agent_with_options(
        self,
        workspace_id: str,
        app_code: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgent',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/application/agents/{DaraURL.percent_encode(app_code)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_agent_with_options_async(
        self,
        workspace_id: str,
        app_code: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgent',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/application/agents/{DaraURL.percent_encode(app_code)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_agent(
        self,
        workspace_id: str,
        app_code: str,
    ) -> main_models.DeleteAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_agent_with_options(workspace_id, app_code, headers, runtime)

    async def delete_agent_async(
        self,
        workspace_id: str,
        app_code: str,
    ) -> main_models.DeleteAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_agent_with_options_async(workspace_id, app_code, headers, runtime)

    def delete_category_with_options(
        self,
        category_id: str,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCategoryResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteCategory',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/category/{DaraURL.percent_encode(category_id)}/',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_category_with_options_async(
        self,
        category_id: str,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCategoryResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteCategory',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/category/{DaraURL.percent_encode(category_id)}/',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_category(
        self,
        category_id: str,
        workspace_id: str,
    ) -> main_models.DeleteCategoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_category_with_options(category_id, workspace_id, headers, runtime)

    async def delete_category_async(
        self,
        category_id: str,
        workspace_id: str,
    ) -> main_models.DeleteCategoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_category_with_options_async(category_id, workspace_id, headers, runtime)

    def delete_chunk_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.DeleteChunkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChunkResponse:
        tmp_req.validate()
        request = main_models.DeleteChunkShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.chunk_ids):
            request.chunk_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.chunk_ids, 'ChunkIds', 'json')
        query = {}
        if not DaraCore.is_null(request.chunk_ids_shrink):
            query['ChunkIds'] = request.chunk_ids_shrink
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChunk',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/chunk/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChunkResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_chunk_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.DeleteChunkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChunkResponse:
        tmp_req.validate()
        request = main_models.DeleteChunkShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.chunk_ids):
            request.chunk_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.chunk_ids, 'ChunkIds', 'json')
        query = {}
        if not DaraCore.is_null(request.chunk_ids_shrink):
            query['ChunkIds'] = request.chunk_ids_shrink
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChunk',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/chunk/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChunkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_chunk(
        self,
        workspace_id: str,
        request: main_models.DeleteChunkRequest,
    ) -> main_models.DeleteChunkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_chunk_with_options(workspace_id, request, headers, runtime)

    async def delete_chunk_async(
        self,
        workspace_id: str,
        request: main_models.DeleteChunkRequest,
    ) -> main_models.DeleteChunkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_chunk_with_options_async(workspace_id, request, headers, runtime)

    def delete_file_with_options(
        self,
        file_id: str,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFileResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteFile',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/file/{DaraURL.percent_encode(file_id)}/',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_file_with_options_async(
        self,
        file_id: str,
        workspace_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFileResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteFile',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/file/{DaraURL.percent_encode(file_id)}/',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_file(
        self,
        file_id: str,
        workspace_id: str,
    ) -> main_models.DeleteFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_file_with_options(file_id, workspace_id, headers, runtime)

    async def delete_file_async(
        self,
        file_id: str,
        workspace_id: str,
    ) -> main_models.DeleteFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_file_with_options_async(file_id, workspace_id, headers, runtime)

    def delete_index_with_options(
        self,
        workspace_id: str,
        request: main_models.DeleteIndexRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIndexResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.index_id):
            query['IndexId'] = request.index_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIndex',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/index/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_index_with_options_async(
        self,
        workspace_id: str,
        request: main_models.DeleteIndexRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIndexResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.index_id):
            query['IndexId'] = request.index_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIndex',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/index/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_index(
        self,
        workspace_id: str,
        request: main_models.DeleteIndexRequest,
    ) -> main_models.DeleteIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_index_with_options(workspace_id, request, headers, runtime)

    async def delete_index_async(
        self,
        workspace_id: str,
        request: main_models.DeleteIndexRequest,
    ) -> main_models.DeleteIndexResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_index_with_options_async(workspace_id, request, headers, runtime)

    def delete_index_document_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.DeleteIndexDocumentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIndexDocumentResponse:
        tmp_req.validate()
        request = main_models.DeleteIndexDocumentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.document_ids):
            request.document_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.document_ids, 'DocumentIds', 'json')
        query = {}
        if not DaraCore.is_null(request.document_ids_shrink):
            query['DocumentIds'] = request.document_ids_shrink
        if not DaraCore.is_null(request.index_id):
            query['IndexId'] = request.index_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIndexDocument',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/index/delete_index_document',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIndexDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_index_document_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.DeleteIndexDocumentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIndexDocumentResponse:
        tmp_req.validate()
        request = main_models.DeleteIndexDocumentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.document_ids):
            request.document_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.document_ids, 'DocumentIds', 'json')
        query = {}
        if not DaraCore.is_null(request.document_ids_shrink):
            query['DocumentIds'] = request.document_ids_shrink
        if not DaraCore.is_null(request.index_id):
            query['IndexId'] = request.index_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIndexDocument',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/index/delete_index_document',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIndexDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_index_document(
        self,
        workspace_id: str,
        request: main_models.DeleteIndexDocumentRequest,
    ) -> main_models.DeleteIndexDocumentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_index_document_with_options(workspace_id, request, headers, runtime)

    async def delete_index_document_async(
        self,
        workspace_id: str,
        request: main_models.DeleteIndexDocumentRequest,
    ) -> main_models.DeleteIndexDocumentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_index_document_with_options_async(workspace_id, request, headers, runtime)

    def delete_memory_with_options(
        self,
        workspace_id: str,
        memory_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMemoryResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMemory',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/memories/{DaraURL.percent_encode(memory_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMemoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_memory_with_options_async(
        self,
        workspace_id: str,
        memory_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMemoryResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMemory',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/memories/{DaraURL.percent_encode(memory_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMemoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_memory(
        self,
        workspace_id: str,
        memory_id: str,
    ) -> main_models.DeleteMemoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_memory_with_options(workspace_id, memory_id, headers, runtime)

    async def delete_memory_async(
        self,
        workspace_id: str,
        memory_id: str,
    ) -> main_models.DeleteMemoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_memory_with_options_async(workspace_id, memory_id, headers, runtime)

    def delete_memory_node_with_options(
        self,
        workspace_id: str,
        memory_id: str,
        memory_node_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMemoryNodeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMemoryNode',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/memories/{DaraURL.percent_encode(memory_id)}/memoryNodes/{DaraURL.percent_encode(memory_node_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMemoryNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_memory_node_with_options_async(
        self,
        workspace_id: str,
        memory_id: str,
        memory_node_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMemoryNodeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMemoryNode',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/memories/{DaraURL.percent_encode(memory_id)}/memoryNodes/{DaraURL.percent_encode(memory_node_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMemoryNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_memory_node(
        self,
        workspace_id: str,
        memory_id: str,
        memory_node_id: str,
    ) -> main_models.DeleteMemoryNodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_memory_node_with_options(workspace_id, memory_id, memory_node_id, headers, runtime)

    async def delete_memory_node_async(
        self,
        workspace_id: str,
        memory_id: str,
        memory_node_id: str,
    ) -> main_models.DeleteMemoryNodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_memory_node_with_options_async(workspace_id, memory_id, memory_node_id, headers, runtime)

    def delete_prompt_template_with_options(
        self,
        workspace_id: str,
        prompt_template_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePromptTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePromptTemplate',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/promptTemplates/{DaraURL.percent_encode(prompt_template_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePromptTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_prompt_template_with_options_async(
        self,
        workspace_id: str,
        prompt_template_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePromptTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePromptTemplate',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/promptTemplates/{DaraURL.percent_encode(prompt_template_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePromptTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_prompt_template(
        self,
        workspace_id: str,
        prompt_template_id: str,
    ) -> main_models.DeletePromptTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_prompt_template_with_options(workspace_id, prompt_template_id, headers, runtime)

    async def delete_prompt_template_async(
        self,
        workspace_id: str,
        prompt_template_id: str,
    ) -> main_models.DeletePromptTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_prompt_template_with_options_async(workspace_id, prompt_template_id, headers, runtime)

    def describe_file_with_options(
        self,
        workspace_id: str,
        file_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFileResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeFile',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/file/{DaraURL.percent_encode(file_id)}/',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_file_with_options_async(
        self,
        workspace_id: str,
        file_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFileResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeFile',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/file/{DaraURL.percent_encode(file_id)}/',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_file(
        self,
        workspace_id: str,
        file_id: str,
    ) -> main_models.DescribeFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_file_with_options(workspace_id, file_id, headers, runtime)

    async def describe_file_async(
        self,
        workspace_id: str,
        file_id: str,
    ) -> main_models.DescribeFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_file_with_options_async(workspace_id, file_id, headers, runtime)

    def get_alipay_transfer_status_with_options(
        self,
        request: main_models.GetAlipayTransferStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAlipayTransferStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code):
            query['code'] = request.code
        if not DaraCore.is_null(request.workspace_id):
            query['workspace_id'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAlipayTransferStatus',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/openapi/alipay/transfer/status',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlipayTransferStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_alipay_transfer_status_with_options_async(
        self,
        request: main_models.GetAlipayTransferStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAlipayTransferStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code):
            query['code'] = request.code
        if not DaraCore.is_null(request.workspace_id):
            query['workspace_id'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAlipayTransferStatus',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/openapi/alipay/transfer/status',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlipayTransferStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_alipay_transfer_status(
        self,
        request: main_models.GetAlipayTransferStatusRequest,
    ) -> main_models.GetAlipayTransferStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_alipay_transfer_status_with_options(request, headers, runtime)

    async def get_alipay_transfer_status_async(
        self,
        request: main_models.GetAlipayTransferStatusRequest,
    ) -> main_models.GetAlipayTransferStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_alipay_transfer_status_with_options_async(request, headers, runtime)

    def get_alipay_url_with_options(
        self,
        request: main_models.GetAlipayUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAlipayUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['app_id'] = request.app_id
        if not DaraCore.is_null(request.workspace_id):
            query['workspace_id'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAlipayUrl',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/openapi/alipay/transfer/url',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlipayUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_alipay_url_with_options_async(
        self,
        request: main_models.GetAlipayUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAlipayUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['app_id'] = request.app_id
        if not DaraCore.is_null(request.workspace_id):
            query['workspace_id'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAlipayUrl',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/openapi/alipay/transfer/url',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlipayUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_alipay_url(
        self,
        request: main_models.GetAlipayUrlRequest,
    ) -> main_models.GetAlipayUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_alipay_url_with_options(request, headers, runtime)

    async def get_alipay_url_async(
        self,
        request: main_models.GetAlipayUrlRequest,
    ) -> main_models.GetAlipayUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_alipay_url_with_options_async(request, headers, runtime)

    def get_available_parser_types_with_options(
        self,
        workspace_id: str,
        request: main_models.GetAvailableParserTypesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAvailableParserTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAvailableParserTypes',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/parser/parsertype',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAvailableParserTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_available_parser_types_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetAvailableParserTypesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAvailableParserTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAvailableParserTypes',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/parser/parsertype',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAvailableParserTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_available_parser_types(
        self,
        workspace_id: str,
        request: main_models.GetAvailableParserTypesRequest,
    ) -> main_models.GetAvailableParserTypesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_available_parser_types_with_options(workspace_id, request, headers, runtime)

    async def get_available_parser_types_async(
        self,
        workspace_id: str,
        request: main_models.GetAvailableParserTypesRequest,
    ) -> main_models.GetAvailableParserTypesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_available_parser_types_with_options_async(workspace_id, request, headers, runtime)

    def get_index_job_status_with_options(
        self,
        workspace_id: str,
        request: main_models.GetIndexJobStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIndexJobStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.index_id):
            query['IndexId'] = request.index_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIndexJobStatus',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/index/job/status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIndexJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_index_job_status_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetIndexJobStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIndexJobStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.index_id):
            query['IndexId'] = request.index_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIndexJobStatus',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/index/job/status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIndexJobStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_index_job_status(
        self,
        workspace_id: str,
        request: main_models.GetIndexJobStatusRequest,
    ) -> main_models.GetIndexJobStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_index_job_status_with_options(workspace_id, request, headers, runtime)

    async def get_index_job_status_async(
        self,
        workspace_id: str,
        request: main_models.GetIndexJobStatusRequest,
    ) -> main_models.GetIndexJobStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_index_job_status_with_options_async(workspace_id, request, headers, runtime)

    def get_index_monitor_with_options(
        self,
        workspace_id: str,
        request: main_models.GetIndexMonitorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIndexMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.index_id):
            query['IndexId'] = request.index_id
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIndexMonitor',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/rag/index/monitor',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIndexMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_index_monitor_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetIndexMonitorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIndexMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.index_id):
            query['IndexId'] = request.index_id
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIndexMonitor',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/rag/index/monitor',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIndexMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_index_monitor(
        self,
        workspace_id: str,
        request: main_models.GetIndexMonitorRequest,
    ) -> main_models.GetIndexMonitorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_index_monitor_with_options(workspace_id, request, headers, runtime)

    async def get_index_monitor_async(
        self,
        workspace_id: str,
        request: main_models.GetIndexMonitorRequest,
    ) -> main_models.GetIndexMonitorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_index_monitor_with_options_async(workspace_id, request, headers, runtime)

    def get_memory_with_options(
        self,
        workspace_id: str,
        memory_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMemoryResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMemory',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/memories/{DaraURL.percent_encode(memory_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMemoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_memory_with_options_async(
        self,
        workspace_id: str,
        memory_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMemoryResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMemory',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/memories/{DaraURL.percent_encode(memory_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMemoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_memory(
        self,
        workspace_id: str,
        memory_id: str,
    ) -> main_models.GetMemoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_memory_with_options(workspace_id, memory_id, headers, runtime)

    async def get_memory_async(
        self,
        workspace_id: str,
        memory_id: str,
    ) -> main_models.GetMemoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_memory_with_options_async(workspace_id, memory_id, headers, runtime)

    def get_memory_node_with_options(
        self,
        workspace_id: str,
        memory_id: str,
        memory_node_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMemoryNodeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMemoryNode',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/memories/{DaraURL.percent_encode(memory_id)}/memoryNodes/{DaraURL.percent_encode(memory_node_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMemoryNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_memory_node_with_options_async(
        self,
        workspace_id: str,
        memory_id: str,
        memory_node_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMemoryNodeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMemoryNode',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/memories/{DaraURL.percent_encode(memory_id)}/memoryNodes/{DaraURL.percent_encode(memory_node_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMemoryNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_memory_node(
        self,
        workspace_id: str,
        memory_id: str,
        memory_node_id: str,
    ) -> main_models.GetMemoryNodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_memory_node_with_options(workspace_id, memory_id, memory_node_id, headers, runtime)

    async def get_memory_node_async(
        self,
        workspace_id: str,
        memory_id: str,
        memory_node_id: str,
    ) -> main_models.GetMemoryNodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_memory_node_with_options_async(workspace_id, memory_id, memory_node_id, headers, runtime)

    def get_parse_settings_with_options(
        self,
        workspace_id: str,
        request: main_models.GetParseSettingsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetParseSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetParseSettings',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/parser/settings',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetParseSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_parse_settings_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetParseSettingsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetParseSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetParseSettings',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/parser/settings',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetParseSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_parse_settings(
        self,
        workspace_id: str,
        request: main_models.GetParseSettingsRequest,
    ) -> main_models.GetParseSettingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_parse_settings_with_options(workspace_id, request, headers, runtime)

    async def get_parse_settings_async(
        self,
        workspace_id: str,
        request: main_models.GetParseSettingsRequest,
    ) -> main_models.GetParseSettingsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_parse_settings_with_options_async(workspace_id, request, headers, runtime)

    def get_prompt_template_with_options(
        self,
        workspace_id: str,
        prompt_template_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPromptTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPromptTemplate',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/promptTemplates/{DaraURL.percent_encode(prompt_template_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPromptTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_prompt_template_with_options_async(
        self,
        workspace_id: str,
        prompt_template_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPromptTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPromptTemplate',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/promptTemplates/{DaraURL.percent_encode(prompt_template_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPromptTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_prompt_template(
        self,
        workspace_id: str,
        prompt_template_id: str,
    ) -> main_models.GetPromptTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_prompt_template_with_options(workspace_id, prompt_template_id, headers, runtime)

    async def get_prompt_template_async(
        self,
        workspace_id: str,
        prompt_template_id: str,
    ) -> main_models.GetPromptTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_prompt_template_with_options_async(workspace_id, prompt_template_id, headers, runtime)

    def get_published_agent_with_options(
        self,
        workspace_id: str,
        app_code: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPublishedAgentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPublishedAgent',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/application/agents/{DaraURL.percent_encode(app_code)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPublishedAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_published_agent_with_options_async(
        self,
        workspace_id: str,
        app_code: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPublishedAgentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPublishedAgent',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/application/agents/{DaraURL.percent_encode(app_code)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPublishedAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_published_agent(
        self,
        workspace_id: str,
        app_code: str,
    ) -> main_models.GetPublishedAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_published_agent_with_options(workspace_id, app_code, headers, runtime)

    async def get_published_agent_async(
        self,
        workspace_id: str,
        app_code: str,
    ) -> main_models.GetPublishedAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_published_agent_with_options_async(workspace_id, app_code, headers, runtime)

    def high_code_deploy_with_options(
        self,
        workspace_id: str,
        request: main_models.HighCodeDeployRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.HighCodeDeployResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_desc):
            body['agentDesc'] = request.agent_desc
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_name):
            body['agentName'] = request.agent_name
        if not DaraCore.is_null(request.source_code_name):
            body['sourceCodeName'] = request.source_code_name
        if not DaraCore.is_null(request.source_code_oss_url):
            body['sourceCodeOssUrl'] = request.source_code_oss_url
        if not DaraCore.is_null(request.telemetry_enabled):
            body['telemetryEnabled'] = request.telemetry_enabled
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'HighCodeDeploy',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/openapi/{DaraURL.percent_encode(workspace_id)}/highCode/publish',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HighCodeDeployResponse(),
            self.call_api(params, req, runtime)
        )

    async def high_code_deploy_with_options_async(
        self,
        workspace_id: str,
        request: main_models.HighCodeDeployRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.HighCodeDeployResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_desc):
            body['agentDesc'] = request.agent_desc
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_name):
            body['agentName'] = request.agent_name
        if not DaraCore.is_null(request.source_code_name):
            body['sourceCodeName'] = request.source_code_name
        if not DaraCore.is_null(request.source_code_oss_url):
            body['sourceCodeOssUrl'] = request.source_code_oss_url
        if not DaraCore.is_null(request.telemetry_enabled):
            body['telemetryEnabled'] = request.telemetry_enabled
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'HighCodeDeploy',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/openapi/{DaraURL.percent_encode(workspace_id)}/highCode/publish',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HighCodeDeployResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def high_code_deploy(
        self,
        workspace_id: str,
        request: main_models.HighCodeDeployRequest,
    ) -> main_models.HighCodeDeployResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.high_code_deploy_with_options(workspace_id, request, headers, runtime)

    async def high_code_deploy_async(
        self,
        workspace_id: str,
        request: main_models.HighCodeDeployRequest,
    ) -> main_models.HighCodeDeployResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.high_code_deploy_with_options_async(workspace_id, request, headers, runtime)

    def list_category_with_options(
        self,
        workspace_id: str,
        request: main_models.ListCategoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCategoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_name):
            body['CategoryName'] = request.category_name
        if not DaraCore.is_null(request.category_type):
            body['CategoryType'] = request.category_type
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.parent_category_id):
            body['ParentCategoryId'] = request.parent_category_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCategory',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/categories',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_category_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListCategoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCategoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_name):
            body['CategoryName'] = request.category_name
        if not DaraCore.is_null(request.category_type):
            body['CategoryType'] = request.category_type
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.parent_category_id):
            body['ParentCategoryId'] = request.parent_category_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListCategory',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/categories',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_category(
        self,
        workspace_id: str,
        request: main_models.ListCategoryRequest,
    ) -> main_models.ListCategoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_category_with_options(workspace_id, request, headers, runtime)

    async def list_category_async(
        self,
        workspace_id: str,
        request: main_models.ListCategoryRequest,
    ) -> main_models.ListCategoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_category_with_options_async(workspace_id, request, headers, runtime)

    def list_chunks_with_options(
        self,
        workspace_id: str,
        request: main_models.ListChunksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListChunksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.fields):
            body['Fields'] = request.fields
        if not DaraCore.is_null(request.file_id):
            body['FileId'] = request.file_id
        if not DaraCore.is_null(request.filed):
            body['Filed'] = request.filed
        if not DaraCore.is_null(request.index_id):
            body['IndexId'] = request.index_id
        if not DaraCore.is_null(request.page_num):
            body['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListChunks',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/index/list_chunks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChunksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chunks_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListChunksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListChunksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.fields):
            body['Fields'] = request.fields
        if not DaraCore.is_null(request.file_id):
            body['FileId'] = request.file_id
        if not DaraCore.is_null(request.filed):
            body['Filed'] = request.filed
        if not DaraCore.is_null(request.index_id):
            body['IndexId'] = request.index_id
        if not DaraCore.is_null(request.page_num):
            body['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListChunks',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/index/list_chunks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChunksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chunks(
        self,
        workspace_id: str,
        request: main_models.ListChunksRequest,
    ) -> main_models.ListChunksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_chunks_with_options(workspace_id, request, headers, runtime)

    async def list_chunks_async(
        self,
        workspace_id: str,
        request: main_models.ListChunksRequest,
    ) -> main_models.ListChunksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_chunks_with_options_async(workspace_id, request, headers, runtime)

    def list_file_with_options(
        self,
        workspace_id: str,
        request: main_models.ListFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFile',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/files',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_file_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFile',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/files',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_file(
        self,
        workspace_id: str,
        request: main_models.ListFileRequest,
    ) -> main_models.ListFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_file_with_options(workspace_id, request, headers, runtime)

    async def list_file_async(
        self,
        workspace_id: str,
        request: main_models.ListFileRequest,
    ) -> main_models.ListFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_file_with_options_async(workspace_id, request, headers, runtime)

    def list_index_documents_with_options(
        self,
        workspace_id: str,
        request: main_models.ListIndexDocumentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIndexDocumentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.document_name):
            query['DocumentName'] = request.document_name
        if not DaraCore.is_null(request.document_status):
            query['DocumentStatus'] = request.document_status
        if not DaraCore.is_null(request.enable_name_like):
            query['EnableNameLike'] = request.enable_name_like
        if not DaraCore.is_null(request.index_id):
            query['IndexId'] = request.index_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIndexDocuments',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/index/list_index_documents',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIndexDocumentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_index_documents_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListIndexDocumentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIndexDocumentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.document_name):
            query['DocumentName'] = request.document_name
        if not DaraCore.is_null(request.document_status):
            query['DocumentStatus'] = request.document_status
        if not DaraCore.is_null(request.enable_name_like):
            query['EnableNameLike'] = request.enable_name_like
        if not DaraCore.is_null(request.index_id):
            query['IndexId'] = request.index_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIndexDocuments',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/index/list_index_documents',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIndexDocumentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_index_documents(
        self,
        workspace_id: str,
        request: main_models.ListIndexDocumentsRequest,
    ) -> main_models.ListIndexDocumentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_index_documents_with_options(workspace_id, request, headers, runtime)

    async def list_index_documents_async(
        self,
        workspace_id: str,
        request: main_models.ListIndexDocumentsRequest,
    ) -> main_models.ListIndexDocumentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_index_documents_with_options_async(workspace_id, request, headers, runtime)

    def list_index_file_details_with_options(
        self,
        workspace_id: str,
        request: main_models.ListIndexFileDetailsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIndexFileDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.document_name):
            query['DocumentName'] = request.document_name
        if not DaraCore.is_null(request.document_status):
            query['DocumentStatus'] = request.document_status
        if not DaraCore.is_null(request.enable_name_like):
            query['EnableNameLike'] = request.enable_name_like
        if not DaraCore.is_null(request.index_id):
            query['IndexId'] = request.index_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIndexFileDetails',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/index/list_index_file_detail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIndexFileDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_index_file_details_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListIndexFileDetailsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIndexFileDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.document_name):
            query['DocumentName'] = request.document_name
        if not DaraCore.is_null(request.document_status):
            query['DocumentStatus'] = request.document_status
        if not DaraCore.is_null(request.enable_name_like):
            query['EnableNameLike'] = request.enable_name_like
        if not DaraCore.is_null(request.index_id):
            query['IndexId'] = request.index_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIndexFileDetails',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/index/list_index_file_detail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIndexFileDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_index_file_details(
        self,
        workspace_id: str,
        request: main_models.ListIndexFileDetailsRequest,
    ) -> main_models.ListIndexFileDetailsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_index_file_details_with_options(workspace_id, request, headers, runtime)

    async def list_index_file_details_async(
        self,
        workspace_id: str,
        request: main_models.ListIndexFileDetailsRequest,
    ) -> main_models.ListIndexFileDetailsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_index_file_details_with_options_async(workspace_id, request, headers, runtime)

    def list_indices_with_options(
        self,
        workspace_id: str,
        request: main_models.ListIndicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIndicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.index_name):
            query['IndexName'] = request.index_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIndices',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/index/list_indices',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIndicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_indices_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListIndicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIndicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.index_name):
            query['IndexName'] = request.index_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIndices',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/index/list_indices',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIndicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_indices(
        self,
        workspace_id: str,
        request: main_models.ListIndicesRequest,
    ) -> main_models.ListIndicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_indices_with_options(workspace_id, request, headers, runtime)

    async def list_indices_async(
        self,
        workspace_id: str,
        request: main_models.ListIndicesRequest,
    ) -> main_models.ListIndicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_indices_with_options_async(workspace_id, request, headers, runtime)

    def list_memories_with_options(
        self,
        workspace_id: str,
        request: main_models.ListMemoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMemoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMemories',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/memories',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMemoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_memories_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListMemoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMemoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMemories',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/memories',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMemoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_memories(
        self,
        workspace_id: str,
        request: main_models.ListMemoriesRequest,
    ) -> main_models.ListMemoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_memories_with_options(workspace_id, request, headers, runtime)

    async def list_memories_async(
        self,
        workspace_id: str,
        request: main_models.ListMemoriesRequest,
    ) -> main_models.ListMemoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_memories_with_options_async(workspace_id, request, headers, runtime)

    def list_memory_nodes_with_options(
        self,
        workspace_id: str,
        memory_id: str,
        request: main_models.ListMemoryNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMemoryNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMemoryNodes',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/memories/{DaraURL.percent_encode(memory_id)}/memoryNodes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMemoryNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_memory_nodes_with_options_async(
        self,
        workspace_id: str,
        memory_id: str,
        request: main_models.ListMemoryNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMemoryNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMemoryNodes',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/memories/{DaraURL.percent_encode(memory_id)}/memoryNodes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMemoryNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_memory_nodes(
        self,
        workspace_id: str,
        memory_id: str,
        request: main_models.ListMemoryNodesRequest,
    ) -> main_models.ListMemoryNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_memory_nodes_with_options(workspace_id, memory_id, request, headers, runtime)

    async def list_memory_nodes_async(
        self,
        workspace_id: str,
        memory_id: str,
        request: main_models.ListMemoryNodesRequest,
    ) -> main_models.ListMemoryNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_memory_nodes_with_options_async(workspace_id, memory_id, request, headers, runtime)

    def list_prompt_templates_with_options(
        self,
        workspace_id: str,
        request: main_models.ListPromptTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPromptTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPromptTemplates',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/promptTemplates',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPromptTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prompt_templates_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListPromptTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPromptTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPromptTemplates',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/promptTemplates',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPromptTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prompt_templates(
        self,
        workspace_id: str,
        request: main_models.ListPromptTemplatesRequest,
    ) -> main_models.ListPromptTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_prompt_templates_with_options(workspace_id, request, headers, runtime)

    async def list_prompt_templates_async(
        self,
        workspace_id: str,
        request: main_models.ListPromptTemplatesRequest,
    ) -> main_models.ListPromptTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_prompt_templates_with_options_async(workspace_id, request, headers, runtime)

    def list_published_agent_with_options(
        self,
        workspace_id: str,
        request: main_models.ListPublishedAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPublishedAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_no):
            query['pageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPublishedAgent',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/application/agents',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPublishedAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_published_agent_with_options_async(
        self,
        workspace_id: str,
        request: main_models.ListPublishedAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPublishedAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_no):
            query['pageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPublishedAgent',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/application/agents',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPublishedAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_published_agent(
        self,
        workspace_id: str,
        request: main_models.ListPublishedAgentRequest,
    ) -> main_models.ListPublishedAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_published_agent_with_options(workspace_id, request, headers, runtime)

    async def list_published_agent_async(
        self,
        workspace_id: str,
        request: main_models.ListPublishedAgentRequest,
    ) -> main_models.ListPublishedAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_published_agent_with_options_async(workspace_id, request, headers, runtime)

    def retrieve_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.RetrieveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RetrieveResponse:
        tmp_req.validate()
        request = main_models.RetrieveShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.images):
            request.images_shrink = Utils.array_to_string_with_specified_style(tmp_req.images, 'Images', 'simple')
        if not DaraCore.is_null(tmp_req.query_history):
            request.query_history_shrink = Utils.array_to_string_with_specified_style(tmp_req.query_history, 'QueryHistory', 'json')
        if not DaraCore.is_null(tmp_req.rerank):
            request.rerank_shrink = Utils.array_to_string_with_specified_style(tmp_req.rerank, 'Rerank', 'json')
        if not DaraCore.is_null(tmp_req.rewrite):
            request.rewrite_shrink = Utils.array_to_string_with_specified_style(tmp_req.rewrite, 'Rewrite', 'json')
        if not DaraCore.is_null(tmp_req.search_filters):
            request.search_filters_shrink = Utils.array_to_string_with_specified_style(tmp_req.search_filters, 'SearchFilters', 'json')
        query = {}
        if not DaraCore.is_null(request.dense_similarity_top_k):
            query['DenseSimilarityTopK'] = request.dense_similarity_top_k
        if not DaraCore.is_null(request.enable_reranking):
            query['EnableReranking'] = request.enable_reranking
        if not DaraCore.is_null(request.enable_rewrite):
            query['EnableRewrite'] = request.enable_rewrite
        if not DaraCore.is_null(request.images_shrink):
            query['Images'] = request.images_shrink
        if not DaraCore.is_null(request.index_id):
            query['IndexId'] = request.index_id
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.query_history_shrink):
            query['QueryHistory'] = request.query_history_shrink
        if not DaraCore.is_null(request.rerank_shrink):
            query['Rerank'] = request.rerank_shrink
        if not DaraCore.is_null(request.rerank_min_score):
            query['RerankMinScore'] = request.rerank_min_score
        if not DaraCore.is_null(request.rerank_top_n):
            query['RerankTopN'] = request.rerank_top_n
        if not DaraCore.is_null(request.rewrite_shrink):
            query['Rewrite'] = request.rewrite_shrink
        if not DaraCore.is_null(request.save_retriever_history):
            query['SaveRetrieverHistory'] = request.save_retriever_history
        if not DaraCore.is_null(request.search_filters_shrink):
            query['SearchFilters'] = request.search_filters_shrink
        if not DaraCore.is_null(request.sparse_similarity_top_k):
            query['SparseSimilarityTopK'] = request.sparse_similarity_top_k
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Retrieve',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/index/retrieve',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetrieveResponse(),
            self.call_api(params, req, runtime)
        )

    async def retrieve_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.RetrieveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RetrieveResponse:
        tmp_req.validate()
        request = main_models.RetrieveShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.images):
            request.images_shrink = Utils.array_to_string_with_specified_style(tmp_req.images, 'Images', 'simple')
        if not DaraCore.is_null(tmp_req.query_history):
            request.query_history_shrink = Utils.array_to_string_with_specified_style(tmp_req.query_history, 'QueryHistory', 'json')
        if not DaraCore.is_null(tmp_req.rerank):
            request.rerank_shrink = Utils.array_to_string_with_specified_style(tmp_req.rerank, 'Rerank', 'json')
        if not DaraCore.is_null(tmp_req.rewrite):
            request.rewrite_shrink = Utils.array_to_string_with_specified_style(tmp_req.rewrite, 'Rewrite', 'json')
        if not DaraCore.is_null(tmp_req.search_filters):
            request.search_filters_shrink = Utils.array_to_string_with_specified_style(tmp_req.search_filters, 'SearchFilters', 'json')
        query = {}
        if not DaraCore.is_null(request.dense_similarity_top_k):
            query['DenseSimilarityTopK'] = request.dense_similarity_top_k
        if not DaraCore.is_null(request.enable_reranking):
            query['EnableReranking'] = request.enable_reranking
        if not DaraCore.is_null(request.enable_rewrite):
            query['EnableRewrite'] = request.enable_rewrite
        if not DaraCore.is_null(request.images_shrink):
            query['Images'] = request.images_shrink
        if not DaraCore.is_null(request.index_id):
            query['IndexId'] = request.index_id
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.query_history_shrink):
            query['QueryHistory'] = request.query_history_shrink
        if not DaraCore.is_null(request.rerank_shrink):
            query['Rerank'] = request.rerank_shrink
        if not DaraCore.is_null(request.rerank_min_score):
            query['RerankMinScore'] = request.rerank_min_score
        if not DaraCore.is_null(request.rerank_top_n):
            query['RerankTopN'] = request.rerank_top_n
        if not DaraCore.is_null(request.rewrite_shrink):
            query['Rewrite'] = request.rewrite_shrink
        if not DaraCore.is_null(request.save_retriever_history):
            query['SaveRetrieverHistory'] = request.save_retriever_history
        if not DaraCore.is_null(request.search_filters_shrink):
            query['SearchFilters'] = request.search_filters_shrink
        if not DaraCore.is_null(request.sparse_similarity_top_k):
            query['SparseSimilarityTopK'] = request.sparse_similarity_top_k
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Retrieve',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/index/retrieve',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetrieveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retrieve(
        self,
        workspace_id: str,
        request: main_models.RetrieveRequest,
    ) -> main_models.RetrieveResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.retrieve_with_options(workspace_id, request, headers, runtime)

    async def retrieve_async(
        self,
        workspace_id: str,
        request: main_models.RetrieveRequest,
    ) -> main_models.RetrieveResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.retrieve_with_options_async(workspace_id, request, headers, runtime)

    def submit_index_add_documents_job_with_options(
        self,
        workspace_id: str,
        tmp_req: main_models.SubmitIndexAddDocumentsJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitIndexAddDocumentsJobResponse:
        tmp_req.validate()
        request = main_models.SubmitIndexAddDocumentsJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.category_ids):
            request.category_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.category_ids, 'CategoryIds', 'json')
        if not DaraCore.is_null(tmp_req.document_ids):
            request.document_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.document_ids, 'DocumentIds', 'json')
        query = {}
        if not DaraCore.is_null(request.category_ids_shrink):
            query['CategoryIds'] = request.category_ids_shrink
        if not DaraCore.is_null(request.chunk_mode):
            query['ChunkMode'] = request.chunk_mode
        if not DaraCore.is_null(request.chunk_size):
            query['ChunkSize'] = request.chunk_size
        if not DaraCore.is_null(request.document_ids_shrink):
            query['DocumentIds'] = request.document_ids_shrink
        if not DaraCore.is_null(request.enable_headers):
            query['EnableHeaders'] = request.enable_headers
        if not DaraCore.is_null(request.index_id):
            query['IndexId'] = request.index_id
        if not DaraCore.is_null(request.overlap_size):
            query['OverlapSize'] = request.overlap_size
        if not DaraCore.is_null(request.separator):
            query['Separator'] = request.separator
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitIndexAddDocumentsJob',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/index/add_documents_to_index',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitIndexAddDocumentsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_index_add_documents_job_with_options_async(
        self,
        workspace_id: str,
        tmp_req: main_models.SubmitIndexAddDocumentsJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitIndexAddDocumentsJobResponse:
        tmp_req.validate()
        request = main_models.SubmitIndexAddDocumentsJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.category_ids):
            request.category_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.category_ids, 'CategoryIds', 'json')
        if not DaraCore.is_null(tmp_req.document_ids):
            request.document_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.document_ids, 'DocumentIds', 'json')
        query = {}
        if not DaraCore.is_null(request.category_ids_shrink):
            query['CategoryIds'] = request.category_ids_shrink
        if not DaraCore.is_null(request.chunk_mode):
            query['ChunkMode'] = request.chunk_mode
        if not DaraCore.is_null(request.chunk_size):
            query['ChunkSize'] = request.chunk_size
        if not DaraCore.is_null(request.document_ids_shrink):
            query['DocumentIds'] = request.document_ids_shrink
        if not DaraCore.is_null(request.enable_headers):
            query['EnableHeaders'] = request.enable_headers
        if not DaraCore.is_null(request.index_id):
            query['IndexId'] = request.index_id
        if not DaraCore.is_null(request.overlap_size):
            query['OverlapSize'] = request.overlap_size
        if not DaraCore.is_null(request.separator):
            query['Separator'] = request.separator
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitIndexAddDocumentsJob',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/index/add_documents_to_index',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitIndexAddDocumentsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_index_add_documents_job(
        self,
        workspace_id: str,
        request: main_models.SubmitIndexAddDocumentsJobRequest,
    ) -> main_models.SubmitIndexAddDocumentsJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.submit_index_add_documents_job_with_options(workspace_id, request, headers, runtime)

    async def submit_index_add_documents_job_async(
        self,
        workspace_id: str,
        request: main_models.SubmitIndexAddDocumentsJobRequest,
    ) -> main_models.SubmitIndexAddDocumentsJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.submit_index_add_documents_job_with_options_async(workspace_id, request, headers, runtime)

    def submit_index_job_with_options(
        self,
        workspace_id: str,
        request: main_models.SubmitIndexJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitIndexJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.index_id):
            query['IndexId'] = request.index_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitIndexJob',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/index/submit_index_job',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitIndexJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_index_job_with_options_async(
        self,
        workspace_id: str,
        request: main_models.SubmitIndexJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitIndexJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.index_id):
            query['IndexId'] = request.index_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitIndexJob',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/index/submit_index_job',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitIndexJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_index_job(
        self,
        workspace_id: str,
        request: main_models.SubmitIndexJobRequest,
    ) -> main_models.SubmitIndexJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.submit_index_job_with_options(workspace_id, request, headers, runtime)

    async def submit_index_job_async(
        self,
        workspace_id: str,
        request: main_models.SubmitIndexJobRequest,
    ) -> main_models.SubmitIndexJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.submit_index_job_with_options_async(workspace_id, request, headers, runtime)

    def update_and_publish_agent_with_options(
        self,
        workspace_id: str,
        app_code: str,
        tmp_req: main_models.UpdateAndPublishAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAndPublishAgentResponse:
        tmp_req.validate()
        request = main_models.UpdateAndPublishAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.application_config):
            request.application_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.application_config, 'applicationConfig', 'json')
        if not DaraCore.is_null(tmp_req.sample_library):
            request.sample_library_shrink = Utils.array_to_string_with_specified_style(tmp_req.sample_library, 'sampleLibrary', 'json')
        body = {}
        if not DaraCore.is_null(request.application_config_shrink):
            body['applicationConfig'] = request.application_config_shrink
        if not DaraCore.is_null(request.instructions):
            body['instructions'] = request.instructions
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.sample_library_shrink):
            body['sampleLibrary'] = request.sample_library_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAndPublishAgent',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/application/agents/{DaraURL.percent_encode(app_code)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAndPublishAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_and_publish_agent_with_options_async(
        self,
        workspace_id: str,
        app_code: str,
        tmp_req: main_models.UpdateAndPublishAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAndPublishAgentResponse:
        tmp_req.validate()
        request = main_models.UpdateAndPublishAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.application_config):
            request.application_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.application_config, 'applicationConfig', 'json')
        if not DaraCore.is_null(tmp_req.sample_library):
            request.sample_library_shrink = Utils.array_to_string_with_specified_style(tmp_req.sample_library, 'sampleLibrary', 'json')
        body = {}
        if not DaraCore.is_null(request.application_config_shrink):
            body['applicationConfig'] = request.application_config_shrink
        if not DaraCore.is_null(request.instructions):
            body['instructions'] = request.instructions
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.sample_library_shrink):
            body['sampleLibrary'] = request.sample_library_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAndPublishAgent',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/application/agents/{DaraURL.percent_encode(app_code)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAndPublishAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_and_publish_agent(
        self,
        workspace_id: str,
        app_code: str,
        request: main_models.UpdateAndPublishAgentRequest,
    ) -> main_models.UpdateAndPublishAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_and_publish_agent_with_options(workspace_id, app_code, request, headers, runtime)

    async def update_and_publish_agent_async(
        self,
        workspace_id: str,
        app_code: str,
        request: main_models.UpdateAndPublishAgentRequest,
    ) -> main_models.UpdateAndPublishAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_and_publish_agent_with_options_async(workspace_id, app_code, request, headers, runtime)

    def update_and_publish_agent_selective_with_options(
        self,
        workspace_id: str,
        app_code: str,
        tmp_req: main_models.UpdateAndPublishAgentSelectiveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAndPublishAgentSelectiveResponse:
        tmp_req.validate()
        request = main_models.UpdateAndPublishAgentSelectiveShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.application_config):
            request.application_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.application_config, 'applicationConfig', 'json')
        if not DaraCore.is_null(tmp_req.sample_library):
            request.sample_library_shrink = Utils.array_to_string_with_specified_style(tmp_req.sample_library, 'sampleLibrary', 'json')
        body = {}
        if not DaraCore.is_null(request.application_config_shrink):
            body['applicationConfig'] = request.application_config_shrink
        if not DaraCore.is_null(request.instructions):
            body['instructions'] = request.instructions
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.sample_library_shrink):
            body['sampleLibrary'] = request.sample_library_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAndPublishAgentSelective',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/application/agents/{DaraURL.percent_encode(app_code)}/updateAndPublishAgentSelective',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAndPublishAgentSelectiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_and_publish_agent_selective_with_options_async(
        self,
        workspace_id: str,
        app_code: str,
        tmp_req: main_models.UpdateAndPublishAgentSelectiveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAndPublishAgentSelectiveResponse:
        tmp_req.validate()
        request = main_models.UpdateAndPublishAgentSelectiveShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.application_config):
            request.application_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.application_config, 'applicationConfig', 'json')
        if not DaraCore.is_null(tmp_req.sample_library):
            request.sample_library_shrink = Utils.array_to_string_with_specified_style(tmp_req.sample_library, 'sampleLibrary', 'json')
        body = {}
        if not DaraCore.is_null(request.application_config_shrink):
            body['applicationConfig'] = request.application_config_shrink
        if not DaraCore.is_null(request.instructions):
            body['instructions'] = request.instructions
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.sample_library_shrink):
            body['sampleLibrary'] = request.sample_library_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAndPublishAgentSelective',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/application/agents/{DaraURL.percent_encode(app_code)}/updateAndPublishAgentSelective',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAndPublishAgentSelectiveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_and_publish_agent_selective(
        self,
        workspace_id: str,
        app_code: str,
        request: main_models.UpdateAndPublishAgentSelectiveRequest,
    ) -> main_models.UpdateAndPublishAgentSelectiveResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_and_publish_agent_selective_with_options(workspace_id, app_code, request, headers, runtime)

    async def update_and_publish_agent_selective_async(
        self,
        workspace_id: str,
        app_code: str,
        request: main_models.UpdateAndPublishAgentSelectiveRequest,
    ) -> main_models.UpdateAndPublishAgentSelectiveResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_and_publish_agent_selective_with_options_async(workspace_id, app_code, request, headers, runtime)

    def update_chunk_with_options(
        self,
        workspace_id: str,
        request: main_models.UpdateChunkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateChunkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chunk_id):
            query['ChunkId'] = request.chunk_id
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.is_displayed_chunk_content):
            query['IsDisplayedChunkContent'] = request.is_displayed_chunk_content
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.content):
            query['content'] = request.content
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateChunk',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/chunk/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateChunkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_chunk_with_options_async(
        self,
        workspace_id: str,
        request: main_models.UpdateChunkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateChunkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chunk_id):
            query['ChunkId'] = request.chunk_id
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.is_displayed_chunk_content):
            query['IsDisplayedChunkContent'] = request.is_displayed_chunk_content
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.content):
            query['content'] = request.content
        if not DaraCore.is_null(request.title):
            query['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateChunk',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/chunk/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateChunkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_chunk(
        self,
        workspace_id: str,
        request: main_models.UpdateChunkRequest,
    ) -> main_models.UpdateChunkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_chunk_with_options(workspace_id, request, headers, runtime)

    async def update_chunk_async(
        self,
        workspace_id: str,
        request: main_models.UpdateChunkRequest,
    ) -> main_models.UpdateChunkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_chunk_with_options_async(workspace_id, request, headers, runtime)

    def update_file_tag_with_options(
        self,
        workspace_id: str,
        file_id: str,
        tmp_req: main_models.UpdateFileTagRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFileTagResponse:
        tmp_req.validate()
        request = main_models.UpdateFileTagShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFileTag',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/file/{DaraURL.percent_encode(file_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFileTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_file_tag_with_options_async(
        self,
        workspace_id: str,
        file_id: str,
        tmp_req: main_models.UpdateFileTagRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFileTagResponse:
        tmp_req.validate()
        request = main_models.UpdateFileTagShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFileTag',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/datacenter/file/{DaraURL.percent_encode(file_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFileTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_file_tag(
        self,
        workspace_id: str,
        file_id: str,
        request: main_models.UpdateFileTagRequest,
    ) -> main_models.UpdateFileTagResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_file_tag_with_options(workspace_id, file_id, request, headers, runtime)

    async def update_file_tag_async(
        self,
        workspace_id: str,
        file_id: str,
        request: main_models.UpdateFileTagRequest,
    ) -> main_models.UpdateFileTagResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_file_tag_with_options_async(workspace_id, file_id, request, headers, runtime)

    def update_memory_with_options(
        self,
        workspace_id: str,
        memory_id: str,
        request: main_models.UpdateMemoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMemoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMemory',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/memories/{DaraURL.percent_encode(memory_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMemoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_memory_with_options_async(
        self,
        workspace_id: str,
        memory_id: str,
        request: main_models.UpdateMemoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMemoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMemory',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/memories/{DaraURL.percent_encode(memory_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMemoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_memory(
        self,
        workspace_id: str,
        memory_id: str,
        request: main_models.UpdateMemoryRequest,
    ) -> main_models.UpdateMemoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_memory_with_options(workspace_id, memory_id, request, headers, runtime)

    async def update_memory_async(
        self,
        workspace_id: str,
        memory_id: str,
        request: main_models.UpdateMemoryRequest,
    ) -> main_models.UpdateMemoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_memory_with_options_async(workspace_id, memory_id, request, headers, runtime)

    def update_memory_node_with_options(
        self,
        workspace_id: str,
        memory_id: str,
        memory_node_id: str,
        request: main_models.UpdateMemoryNodeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMemoryNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['content'] = request.content
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMemoryNode',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/memories/{DaraURL.percent_encode(memory_id)}/memoryNodes/{DaraURL.percent_encode(memory_node_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMemoryNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_memory_node_with_options_async(
        self,
        workspace_id: str,
        memory_id: str,
        memory_node_id: str,
        request: main_models.UpdateMemoryNodeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMemoryNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['content'] = request.content
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMemoryNode',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/memories/{DaraURL.percent_encode(memory_id)}/memoryNodes/{DaraURL.percent_encode(memory_node_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMemoryNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_memory_node(
        self,
        workspace_id: str,
        memory_id: str,
        memory_node_id: str,
        request: main_models.UpdateMemoryNodeRequest,
    ) -> main_models.UpdateMemoryNodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_memory_node_with_options(workspace_id, memory_id, memory_node_id, request, headers, runtime)

    async def update_memory_node_async(
        self,
        workspace_id: str,
        memory_id: str,
        memory_node_id: str,
        request: main_models.UpdateMemoryNodeRequest,
    ) -> main_models.UpdateMemoryNodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_memory_node_with_options_async(workspace_id, memory_id, memory_node_id, request, headers, runtime)

    def update_prompt_template_with_options(
        self,
        workspace_id: str,
        prompt_template_id: str,
        request: main_models.UpdatePromptTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePromptTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['content'] = request.content
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePromptTemplate',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/promptTemplates/{DaraURL.percent_encode(prompt_template_id)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePromptTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_prompt_template_with_options_async(
        self,
        workspace_id: str,
        prompt_template_id: str,
        request: main_models.UpdatePromptTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePromptTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['content'] = request.content
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePromptTemplate',
            version = '2023-12-29',
            protocol = 'HTTPS',
            pathname = f'/{DaraURL.percent_encode(workspace_id)}/promptTemplates/{DaraURL.percent_encode(prompt_template_id)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePromptTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_prompt_template(
        self,
        workspace_id: str,
        prompt_template_id: str,
        request: main_models.UpdatePromptTemplateRequest,
    ) -> main_models.UpdatePromptTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_prompt_template_with_options(workspace_id, prompt_template_id, request, headers, runtime)

    async def update_prompt_template_async(
        self,
        workspace_id: str,
        prompt_template_id: str,
        request: main_models.UpdatePromptTemplateRequest,
    ) -> main_models.UpdatePromptTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_prompt_template_with_options_async(workspace_id, prompt_template_id, request, headers, runtime)
